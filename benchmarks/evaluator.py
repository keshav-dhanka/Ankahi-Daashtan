"""
Ankahi Dastaan — Comprehensive Benchmark Evaluator
Performs rigorous structural, lexical, script, and negative constraint verification.
Separates superficial script compliance from genuine language quality and constraint adherence.
"""

import re
from typing import Dict, Any, List, Optional

DEVANAGARI_REGEX = re.compile(r'[\u0900-\u097F]')
ARABIC_REGEX = re.compile(r'[\u0600-\u06FF]')
THINK_TAG_REGEX = re.compile(r'<think>.*?</think>', re.DOTALL | re.IGNORECASE)
OPEN_THINK_REGEX = re.compile(r'</?think>', re.IGNORECASE)

# Universal clichés forbidden by skill.md
GLOBAL_FORBIDDEN_CLICHES = [
    "shama", "parwana", "jaam-e-sharab", "jaam", "sharab", 
    "aansuon ka samandar", "toota hua dil", "zulfon ki chhaon",
    "zindagi ek safar hai", "waqt sab theek kar deta hai"
]

# Prompt-specific forbidden words and clichés
PROMPT_FORBIDDEN_WORDS = {
    "02": ["dil", "dard", "aansu", "tanhaai", "yaadein"],
    "04": ["i miss you", "yaad aati hai", "intezaar"],
    "05": ["heartbreak", "tears", "loneliness", "silence", "aansu", "tanhaai", "khamoshi"],
    "06": ["bheegi yaadein", "aankhon ka samandar", "toota hua dil"],
    "07": ["past", "memories", "yaadein", "dard", "tanhaai"],
    "08": ["clock", "ghadi", "rain", "baarish", "tears", "aansu", "empty chair"],
    "13": ["maaf", "dil", "dard", "badla"],
    "14": ["tears", "aansu", "heartbreak"],
    "15": ["zindagi", "kismat", "tanhaai"],
    "20": ["illness", "bimari", "death", "maut", "old age", "buddhapa"]
}

# Prompt-specific required words
PROMPT_REQUIRED_WORDS = {
    "11": ["gali", "purana", "khidki", "shayad"],
    "12": ["sabr", "lehja"],
    "17": ["station", "aadat", "der se", "ghar"]
}

# Common Roman Hinglish vocabulary indicators (Hindi, Urdu, Punjabi words)
HINGLISH_MARKERS = {
    "hai", "hain", "tha", "thi", "the", "ke", "ki", "ko", "se", "mein", "me", "par", "pe",
    "aur", "or", "yeh", "woh", "wo", "kya", "kyun", "hum", "main", "mera", "meri", "mere",
    "tera", "teri", "tere", "tum", "tu", "apna", "apne", "apni", "nahi", "nhi", "na", "bhi",
    "ek", "kuch", "saath", "raat", "din", "aaj", "kal", "baat", "door", "paas", "gaya", "gayi",
    "gaye", "aaya", "aayi", "dekh", "dekha", "sun", "bol", "dil", "dard", "ishq", "yaad",
    "yaadein", "khamoshi", "intezaar", "zakhm", "sabr", "lehja", "fanna", "khafaa", "zalim",
    "hevaan", "hichki", "aashik", "khidki", "gali", "purana", "purani", "shayad", "chuskiyon",
    "darwaza", "dheere", "aadat", "khamakha", "tehzeeb", "rasta", "neend", "toot", "jaye",
    "kabhi", "ab", "aab", "jab", "tab", "har", "harr", "pal", "waqt", "lamha", "lamhe",
    "ankhen", "aankhein", "aankh", "chehra", "baatein", "chup", "shor", "suno", "kaho", "jaao",
    "aao", "chal", "chale", "rahein", "mod", "kahani", "dastaan", "ankahi", "soch", "socha",
    "samjha", "ehsaas", "mehsoos", "mahasoos", "huye", "hua", "hui", "hota", "hoti", "hote",
    "karta", "karti", "karte", "rakha", "rakhi", "rakhe", "sirf", "bas", "khatm", "shuru",
    "tamanna", "dost", "doston", "ghav", "ghavon", "bharne", "khuredne", "vapas", "wapas",
    "vala", "wali", "wale", "koi", "mila", "mili", "mile", "magar", "lekin", "fir", "phir",
    "batate", "jataate", "gahare", "gehre", "dheeme", "ruk", "ruka", "badal", "badle",
    "alag", "saal", "baras", "subah", "shaam", "dhoop", "chhaon", "roshni", "andhera",
    "ghar", "makaan", "kamra", "darwaaza", "khidkiyan", "mez", "chaye", "chai", "pyali",
    "tasveer", "khat", "kagaz", "lafz", "alfaaz", "baaki", "koyi", "sab", "log", "apne",
    "anjaan", "ajnabi", "khwaab", "khwab", "haath", "qadam", "kadam", "safarnama", "khabar",
    "bekhabar", "sukoon", "sawal", "jawab", "ummeed", "aas", "tasalli", "khud", "khudi",
    "rab", "rabba", "bande", "dilyaan", "vich", "wich", "rehenda", "dhaain", "faqir", "kafi",
    "sach", "jhooth", "aashiq", "vese", "verna", "kl", "agr", "kr", "bataao", "naa", "thaa",
    "nhii", "dungaa", "achaa", "achaanji"
}


def evaluate_output(output_text: str, prompt_meta: Dict[str, Any]) -> Dict[str, Any]:
    """
    Rigorously evaluates generated output text against prompt specifications.
    Distinguishes script compliance from language quality, structural adherence,
    constraint violations, exact pinned-line preservation, and cleanliness.
    """
    raw_text = output_text
    cleaned_text = output_text.strip()
    
    # 1. Artifact & Meta-commentary Detection (<think>, preambles, explanations)
    artifacts_found = []
    if OPEN_THINK_REGEX.search(raw_text):
        artifacts_found.append("contains_<think>_reasoning_tags")
        
    # Check for conversational preamble
    first_chunk = cleaned_text[:120].lower()
    preambles = ["here is", "sure, here", "sure!", "couplet:", "poem:", "verse:", "here's a poem", "here's the poem"]
    if any(first_chunk.startswith(p) for p in preambles):
        artifacts_found.append("conversational_preamble")
        
    # Check for parenthetical commentary or post-poem explanation
    if "(change:" in cleaned_text.lower():
        artifacts_found.append("parenthetical_commentary")
    if "(note:" in cleaned_text.lower():
        artifacts_found.append("parenthetical_note")
    if re.search(r'\b(the final line reveals|explanation:|meaning:|note:|translation:)\b', cleaned_text, re.IGNORECASE):
        artifacts_found.append("post_poem_explanation")

    # Clean lines (excluding empty lines)
    raw_lines = [line.strip() for line in cleaned_text.split('\n') if line.strip()]
    
    # 2. Script Compliance (Strict Unicode check for non-Latin characters)
    devanagari_chars = len(DEVANAGARI_REGEX.findall(cleaned_text))
    arabic_chars = len(ARABIC_REGEX.findall(cleaned_text))
    illegal_chars = devanagari_chars + arabic_chars
    total_chars = max(len(cleaned_text), 1)
    
    script_compliant = (illegal_chars == 0)
    compliance_percentage = round(((total_chars - illegal_chars) / total_chars) * 100.0, 2)

    # 3. Language Quality: Check if model reverted to pure English vs Hinglish
    tokens = [re.sub(r'[^\w]', '', w.lower()) for w in cleaned_text.split() if re.sub(r'[^\w]', '', w.lower())]
    hinglish_token_count = sum(1 for t in tokens if t in HINGLISH_MARKERS)
    total_tokens = max(len(tokens), 1)
    hinglish_density_pct = round((hinglish_token_count / total_tokens) * 100.0, 1)
    
    # Pure English check (0 Hinglish tokens with sufficient word length)
    is_pure_english = (hinglish_token_count == 0 and total_tokens >= 6)
    if is_pure_english:
        language_mode = "Pure English (Failed Hinglish requirement)"
    elif hinglish_density_pct >= 20.0:
        language_mode = "Roman Hinglish"
    else:
        language_mode = "Sparse / Low Hinglish"

    # 4. Line Count Verification
    actual_line_count = len(raw_lines)
    expected_lines = prompt_meta.get("expected_lines")
    line_count_match = (actual_line_count == expected_lines) if expected_lines else True

    # 5. Exact Pinned Line Verification (Character-for-character check)
    pinned_line = prompt_meta.get("pinned_line")
    pinned_line_status = "not_applicable"
    pinned_line_preserved = None
    
    if pinned_line:
        if not raw_lines:
            pinned_line_status = "missing_output"
            pinned_line_preserved = False
        else:
            first_line = raw_lines[0].strip()
            # Exact character-for-character check (including punctuation)
            if first_line == pinned_line.strip():
                # Check that it's NOT repeated later in the poem
                repeated = any(pinned_line.lower() in l.lower() for l in raw_lines[1:])
                if repeated:
                    pinned_line_status = "repeated_in_subsequent_lines"
                    pinned_line_preserved = False
                else:
                    pinned_line_status = "exact_match"
                    pinned_line_preserved = True
            else:
                # Punctuation vs text mismatch
                if re.sub(r'[^\w\s]', '', first_line).strip() == re.sub(r'[^\w\s]', '', pinned_line).strip():
                    pinned_line_status = "punctuation_mismatch"
                else:
                    pinned_line_status = "text_mismatch"
                pinned_line_preserved = False

    # 6. Required Words Verification (per prompt)
    prompt_id = str(prompt_meta.get("id"))
    required_words = PROMPT_REQUIRED_WORDS.get(prompt_id, [])
    missing_required_words = []
    for rw in required_words:
        pattern = r'(?:\b|^)' + re.escape(rw) + r'(?:\b|$)'
        if not re.search(pattern, cleaned_text, re.IGNORECASE):
            missing_required_words.append(rw)
            
    required_words_passed = (len(missing_required_words) == 0)

    # 7. Forbidden Words Check (Negative Constraints)
    forbidden_violations = []
    specific_bans = PROMPT_FORBIDDEN_WORDS.get(prompt_id, [])

    for w in specific_bans:
        pattern = r'(?:\b|^)' + re.escape(w) + r'(?:\b|$)'
        if re.search(pattern, cleaned_text, re.IGNORECASE):
            forbidden_violations.append(f"banned_word:{w}")

    # Check global clichés (only if not an intentional seed word)
    for cliché in GLOBAL_FORBIDDEN_CLICHES:
        pattern = r'(?:\b|^)' + re.escape(cliché) + r'(?:\b|$)'
        if re.search(pattern, cleaned_text, re.IGNORECASE):
            forbidden_violations.append(f"cliché:{cliché}")

    # 8. Composite Structural & Compliance Verdict
    # PASS requires:
    # - Script compliant (no non-Latin chars)
    # - Not reverted to pure English
    # - Exact line count match
    # - Pinned line preserved (if applicable)
    # - All required words included
    # - Zero forbidden word violations
    # - Zero artifact/meta-commentary leaks
    pinned_passed = (pinned_line_status == "exact_match") if pinned_line else True
    
    strict_pass = (
        script_compliant
        and (not is_pure_english)
        and line_count_match
        and pinned_passed
        and required_words_passed
        and (len(forbidden_violations) == 0)
        and (len(artifacts_found) == 0)
    )

    failure_reasons = []
    if not script_compliant:
        failure_reasons.append(f"illegal_script_chars({illegal_chars})")
    if is_pure_english:
        failure_reasons.append("pure_english_reversion")
    if not line_count_match:
        failure_reasons.append(f"line_count({actual_line_count}/{expected_lines})")
    if pinned_line and not pinned_passed:
        failure_reasons.append(f"pinned_line({pinned_line_status})")
    if not required_words_passed:
        failure_reasons.append(f"missing_words({','.join(missing_required_words)})")
    if forbidden_violations:
        failure_reasons.append(f"forbidden_words({len(forbidden_violations)})")
    if artifacts_found:
        failure_reasons.append(f"artifacts({','.join(artifacts_found)})")

    return {
        "strict_pass": strict_pass,
        "failure_reasons": failure_reasons,
        "script_compliant": script_compliant,
        "compliance_percentage": compliance_percentage,
        "illegal_char_count": illegal_chars,
        "is_pure_english": is_pure_english,
        "hinglish_density_pct": hinglish_density_pct,
        "language_mode": language_mode,
        "line_count": actual_line_count,
        "expected_lines": expected_lines,
        "line_count_match": line_count_match,
        "word_count": len(tokens),
        "pinned_line_status": pinned_line_status,
        "pinned_line_preserved": pinned_line_preserved,
        "required_words": required_words,
        "missing_required_words": missing_required_words,
        "required_words_passed": required_words_passed,
        "forbidden_violations": forbidden_violations,
        "artifacts_found": artifacts_found,
        "clean_lines": raw_lines
    }
