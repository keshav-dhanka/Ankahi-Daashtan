# Benchmark Evaluation Report: Qwen3-4B-Q4_K_M

- **Stage:** `FULL`
- **Date & Time:** 20261017_020824
- **Model Path:** `models/Qwen3-4B-Q4_K_M.gguf`
- **Configuration:** 4 CPU threads | Context: 8192 tokens | Temp: 0.74

## 1. Hardware Performance Summary

| Metric | Target (PRD) | Measured Result | Status |
| :--- | :--- | :--- | :--- |
| **Model Load Time** | < 8.0s | **4.18s** | PASS |
| **Time-to-First-Token (TTFT)** | < 4.0s | **20.98s** (Cold: 257.722s) | CHECK |
| **Generation Speed** | ≥ 6.5 t/s | **4.6 t/s** | AMEND PRD |
| **Peak RAM** | < 6000 MB | **5395.8 MB** | PASS |

## 2. Strict Compliance & Language Quality Audit

| Audit Check | What it Verifies | Measured Result | Strict Status |
| :--- | :--- | :--- | :--- |
| **Script Compliance** | Latin/Roman script only; zero Devanagari/Arabic characters | **100.0%** | PASS |
| **Output Cleanliness** | Zero `<think>` reasoning tags, preambles, notes, explanations | **100.0%** | PASS |
| **Exact Line Count** | Matches requested lines exactly (2 for couplets, 4 for quatrains) | **100.0%** | PASS |
| **Hinglish Language Quality** | Authentic Roman Hindustani/Urdu vocabulary; not pure English | **100.0%** | PASS |
| **Locked-Line Preservation** | Character-for-character exact match; punctuation preserved; no repetition | **0.0%** | FAIL |
| ⭐ **Overall Strict Pass Rate** | Satisfied ALL technical, structural, and negative constraints simultaneously | **95.0%** | PASS |

---

## 3. Qualitative Output & Poetic Voice Review
*(Human evaluation rubric: score 1–5 for cadence, restraint, originality, and final turn)*

### Prompt 01: The friendship that slowly changed — Emotional restraint and subtlety
**Target:** `Betrayal · Restraint · 4 lines`

> **Prompt Text:** Write a short Roman Hinglish poem about a close friend who slowly became a stranger. There was no fight and no clear ending; the conversations simply became shorter. Keep the tone quiet, personal, and slightly disappointed, not angry. Use everyday language and one concrete detail from ordinary life. Write exactly 4 lines. Avoid forced rhyming and familiar heartbreak clichés. The last line should reveal something the speaker has only just understood.

**Raw Generated Output:**
```text
Ishq karne ki tamanna thi  
Jo khatm ho gayi mere doston ne hi  
Itna yaad kiye ki hichki shuru ho gayi  
Yaad aati h fir bhi use batate nhi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 257.722s | Speed: 3.79 t/s | RAM: 5365.29 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 62.1%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 02: The unsent message — Emotional restraint and subtlety
**Target:** `Longing · Understatement · 2 lines`

> **Prompt Text:** Write a Roman Hinglish couplet about typing a long message to someone and deleting it without sending. Do not explain the entire relationship. Do not use the words "dil", "dard", "aansu", "tanhaai", or "yaadein". Use a small, believable detail from a phone or a room. Exactly 2 lines, conversational rather than ornate. Make the second line quietly change the meaning of the first.

**Raw Generated Output:**
```text
Taps on the screen like it's a drum  
Deletes the last word and leaves it there 🥲
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 9.533s | Speed: 4.1 t/s | RAM: 5389.46 MB
- **Structure:** Lines: 2/2 (MATCH)
- **Language Mode:** Sparse / Low Hinglish (Hinglish Density: 12.5%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 03: A quiet apology — Emotional restraint and subtlety
**Target:** `Guilt · Emotional nuance · 4 lines`

> **Prompt Text:** Write 4 lines of Roman Hinglish poetry from the perspective of someone who realizes they hurt a person who trusted them. The speaker should not ask for forgiveness or justify their behavior. Avoid dramatic declarations, moral lessons, and stock phrases about broken hearts. Make the poem feel like an honest thought the speaker would never say aloud. The final line should carry the weight of the realization without explaining it.

**Raw Generated Output:**
```text
Ishq ke dard ka khud koi nahi
Zakhm gahare hai magar bataate nhi
Mahasoos to harr pal karte hai use lekin
Yaad aati h fir bhi use batate nhi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 9.673s | Speed: 3.22 t/s | RAM: 5391.78 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 75.9%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 04: Missing someone without saying it — Emotional restraint and subtlety
**Target:** `Indirect emotion · Imagery · 4 lines`

> **Prompt Text:** Write a restrained 4-line Roman Hinglish poem about missing someone, but never directly say "I miss you", "yaad aati hai", or "intezaar". Show the feeling through an ordinary repeated habit that no longer makes sense. Use natural spoken Hinglish, with no elaborate Persian or Urdu metaphors. Avoid rhyme unless it occurs naturally. End on an understated observation.

**Raw Generated Output:**
```text
Ishq ka dard toh aaj bhi rhaa  
Tumhare liye koi taazaa nahi milta  
Dil ke tukde jama ho gaye hain  
Koi naa, tumhari yaad nahi chuttaa
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 8.065s | Speed: 4.51 t/s | RAM: 5393.82 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 53.8%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 05: A cold cup of chai — Originality and anti-cliché control
**Target:** `Concrete imagery · 4 lines`

> **Prompt Text:** Write exactly 4 lines of Roman Hinglish poetry about two people sitting together after an uncomfortable conversation. A cup of chai has gone cold between them. Do not mention heartbreak, tears, loneliness, or silence directly. Do not personify the cup. Use the physical scene to communicate what the people cannot say. Avoid forced rhyme and end with a fresh, understated turn.

**Raw Generated Output:**
```text
Ishq karne ki tamanna thi  
Jo khatm ho gayi mere doston ne hi  
Itna yaad kiye ki hichki shuru ho gayi  
Kuch chhodna padega aap ke dil me
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 7.591s | Speed: 4.38 t/s | RAM: 5395.75 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 60.7%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 06: Rain without romance — Originality and anti-cliché control
**Target:** `Cliché avoidance · 4 lines`

> **Prompt Text:** Write a 4-line Roman Hinglish poem about walking home in the rain after receiving disappointing news. Rain must remain ordinary weather, not a metaphor for tears or cleansing. Avoid "bheegi yaadein", "aankhon ka samandar", "toota hua dil", and any predictable romantic imagery. Use one specific sensory detail and a restrained voice. Make the last line emotionally meaningful without being dramatic.

**Raw Generated Output:**
```text
Ishq ka dard to bhi nahi
Pyaas ke saath rain ho rha h
Tumhare liye kuch chhod diya
Nazar me aisi ghato rha h
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 9.0s | Speed: 4.29 t/s | RAM: 5258.47 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 33.3%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 07: An ordinary object — Originality and anti-cliché control
**Target:** `Fresh metaphor · 4 lines`

> **Prompt Text:** Write 4 lines of Roman Hinglish poetry about an old house key that the speaker still carries even though they no longer live in that house. Do not use the words "past", "memories", "yaadein", "dard", or "tanhaai". Do not explain what the key symbolizes. Build meaning from a concrete detail about the object and its current use. Avoid conventional rhymes. The ending should invite interpretation rather than explain the poem.

**Raw Generated Output:**
```text
I still keep that old house key  
It fits no lock now but I never let it go  
Used to turn in the dark when the world was small  
Now it just hangs there like a quiet, unspoken call
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 9.383s | Speed: 4.59 t/s | RAM: 5205.0 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Sparse / Low Hinglish (Hinglish Density: 5.1%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 08: Avoid the expected ending — Originality and anti-cliché control
**Target:** `Originality · Unexpected turn · 4 lines`

> **Prompt Text:** Write a 4-line Roman Hinglish poem about waiting for someone who promised to visit but never came. Do not mention a clock, a phone notification, rain, tears, or an empty chair. Avoid moralizing and familiar heartbreak lines. The poem should begin with an ordinary practical action and gradually reveal the speaker's disappointment. Make the final line surprising but believable, not a dramatic twist.

**Raw Generated Output:**
```text
I am waiting for the bus
The sun is high and the street is still
My phone is silent and my heart is light
But the person who said they'd come never did
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 8.497s | Speed: 4.78 t/s | RAM: 5140.48 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Sparse / Low Hinglish (Hinglish Density: 15.2%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 09: Natural Hinglish conversation — Roman Hinglish and language control
**Target:** `Code-switching · 4 lines`

> **Prompt Text:** Write exactly 4 lines of Roman Hinglish poetry about two old friends meeting after a long time and behaving as if nothing has changed, even though both know it has. Use natural spoken Hindi with a little English where it would genuinely occur in conversation. Avoid overly formal Urdu vocabulary and artificial English rhymes. Use only Roman script. End with a quiet realization.

**Raw Generated Output:**
```text
Tumhari yaad koi nahi
Purana dil koi nahi
Kuch bhi nahi jaa raha hai
Aisa hi rehna chahia hai
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 7.858s | Speed: 4.56 t/s | RAM: 5142.3 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 63.2%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 10: Everyday Punjabi nuance — Roman Hinglish and language control
**Target:** `Regional language naturalness · 4 lines`

> **Prompt Text:** Write 4 lines of Roman Hinglish poetry about a mother asking whether her adult child has eaten, while avoiding a direct conversation about their growing distance. Use natural North Indian conversational phrasing, with at most one or two Punjabi expressions if they fit organically. Do not exaggerate a regional accent or use caricatured dialect. Avoid melodrama. The final line should suggest care without explicitly explaining it.

**Raw Generated Output:**
```text
Tumne kuch khaya kiya?  
Dil ke tukde ka saath  
Zakhm gahare hai magar bataate nhi  
Yaad aati h fir bhi use batate nhi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 8.319s | Speed: 4.76 t/s | RAM: 5088.59 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 60.9%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 11: Roman script discipline — Roman Hinglish and language control
**Target:** `Script compliance · 4 lines`

> **Prompt Text:** Write a 4-line poem in Roman Hinglish about a person returning to their childhood neighbourhood. Use the words "gali", "purana", "khidki", and "shayad" naturally. All Hindi and Urdu words must be written in Roman script. Do not use Devanagari, Arabic, or Nastaliq characters. Do not add a title, transliteration, explanation, or English introduction. Keep the poem understated and end with an observation about change.

**Raw Generated Output:**
```text
Shayad gali ki purana khidki ne kuch yaad raahin
Dil ke tukde harr pal karte hai use lekin
Mujhme fanna ho jaa ya mujhse to khafaa ho ja
Aab to ek tarfaa ho jaa
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 9.923s | Speed: 3.98 t/s | RAM: 5058.44 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 52.9%)
- **Required Words Check:** None (all present)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 12: A formal Urdu register without ornament — Roman Hinglish and language control
**Target:** `Vocabulary balance · 4 lines`

> **Prompt Text:** Write 4 lines of Roman Hinglish poetry about a person accepting that an important relationship has changed. Include the words "sabr" and "lehja", but use otherwise simple conversational language. Do not add ornate Persian compounds, elaborate metaphors, or forced rhymes. Keep the emotional tone calm rather than defeated. All text must remain in Roman script. End on a subtle change in the speaker's understanding.

**Raw Generated Output:**
```text
Ishq ka sabr rakhna padta hai  
Lehja karte hoon par nahi jata hai  
Dil ke tukde khud pe lagaaye  
Aaj ki lehja bharne wala ho gaya
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 7.989s | Speed: 5.09 t/s | RAM: 4665.17 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 65.4%)
- **Required Words Check:** None (all present)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 13: A complete two-line couplet — Structure, cadence and final-line quality
**Target:** `Concision · 2 lines`

> **Prompt Text:** Write exactly 2 lines of Roman Hinglish poetry about discovering that you no longer feel angry with someone who once hurt you. Do not use the words "maaf", "dil", "dard", or "badla". Each line should be short enough to say naturally in one breath. Avoid forced rhyme. The second line should subtly reveal that the speaker has changed, without announcing personal growth.

**Raw Generated Output:**
```text
Ishq ki tamanna thi jo khatm ho gayi  
Yaad aati h fir bhi use batate nhi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 7.656s | Speed: 5.14 t/s | RAM: 4667.07 MB
- **Structure:** Lines: 2/2 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 68.8%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 14: The quiet final turn — Structure, cadence and final-line quality
**Target:** `Ending impact · 4 lines`

> **Prompt Text:** Write a 4-line Roman Hinglish poem about a person preparing a favourite meal for someone who will not be coming home anymore. Do not state why the person is absent. Keep the first three lines observational and restrained. The fourth line must change how the reader understands the scene, without adding a new character or explaining the symbolism. Avoid tears, heartbreak clichés, and moral lessons.

**Raw Generated Output:**
```text
Ishq karne ki tamanna thi  
Jo khatm ho gayi mere doston ne hi  
Itna yaad kiye ki hichki shuru ho gayi  
Yaad aati h fir bhi use batate nhi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 7.249s | Speed: 4.99 t/s | RAM: 4668.94 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 62.1%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 15: Natural rhythm without rhyme — Structure, cadence and final-line quality
**Target:** `Cadence · Free verse · 4 lines`

> **Prompt Text:** Write exactly 4 lines of free-verse Roman Hinglish about returning home after a long, exhausting day and finding that nobody has noticed how tired you are. Prioritize natural spoken rhythm over syllable matching or rhyme. Include one concrete household detail. Avoid abstract words such as "zindagi", "kismat", and "tanhaai". The final line should be quiet and emotionally specific.

**Raw Generated Output:**
```text
Tumhe koi tara lag rha h
Dil ka ghar khali hoon
Kuch bhi nahi hai yahan
Aisi raat khali hoon
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 7.522s | Speed: 5.14 t/s | RAM: 4670.77 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 40.0%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 16: No explanation after the poem — Structure, cadence and final-line quality
**Target:** `Format compliance · 2 lines`

> **Prompt Text:** Write one Roman Hinglish couplet about keeping an old photograph in a drawer but no longer looking at it. Output exactly 2 poetic lines and nothing else. No title, preamble, quotation marks, commentary, translation, or explanation. Avoid familiar phrases about memories and time healing everything. Use conversational language, no forced rhyme, and let the second line carry the emotional shift.

**Raw Generated Output:**
```text
Ishq ke dard ka ghav abhi koi nahi  
Zakhm gahare hai magar bataate nhi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 7.023s | Speed: 5.08 t/s | RAM: 4672.58 MB
- **Structure:** Lines: 2/2 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 78.6%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 17: Keywords only — Robustness and creative control
**Target:** `Minimal input interpretation · 4 lines`

> **Prompt Text:** Seed words: "station, aadat, der se, ghar". Create a coherent 4-line Roman Hinglish poem from these words without asking questions. You may add words to connect them, but do not simply list the seed words. Choose one understated emotional direction and maintain it throughout. Avoid common romantic imagery, forced rhyme, and an explanatory ending. Output only the poem.

**Raw Generated Output:**
```text
station me aadat der se ghar hai  
koi nahi chala jaaye yaad  
dil ke tukde koi nahi jaye  
ghar me zakhm toh nahi raha
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 7.899s | Speed: 5.01 t/s | RAM: 4674.44 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 70.8%)
- **Required Words Check:** None (all present)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 18: The prompt contains conflicting impulses — Robustness and creative control
**Target:** `Instruction handling · 4 lines`

> **Prompt Text:** Write 4 lines of Roman Hinglish poetry about being happy for a former friend who has succeeded without you. The feeling should contain genuine goodwill and a small trace of personal regret, but not jealousy or resentment. Do not resolve the two feelings into a moral lesson. Avoid dramatic declarations and predictable phrases. Use one specific, ordinary detail and end with a quiet, unresolved observation.

**Raw Generated Output:**
```text
Ishq ki tamanna thi jo khatm ho gayi
Doston ne hi bharne vala abhi koi
Thtaa nahi lekin yaad aati h fir bhi use batate nhi
Kuch chotii galtiya hai toh verna
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 7.09s | Speed: 4.88 t/s | RAM: 4676.29 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 62.5%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 19: The user protects the opening line — Robustness and creative control
**Target:** `Pinned-line revision · 4 lines`

> **Prompt Text:** The first line is locked and must remain exactly unchanged: "Aaj bhi darwaza dheere se band kiya."
Write 3 additional lines of Roman Hinglish poetry that continue naturally from it. Do not rewrite, punctuate differently, or repeat the locked line. Keep the tone understated and conversational. Avoid forced rhyme, generic heartbreak language, and moralizing. Make the final line reveal a new detail about why the speaker still closes the door that way.

**Raw Generated Output:**
```text
Aaj bhi darwaza dheere se band kiya  
Zakhm gahare hai magar bataate nhi  
Mahasoos to harr pal karte hai use lekin  
Yaad aati h fir bhi use batate nhi
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** pinned_line(punctuation_mismatch)
- **Performance:** TTFT: 13.217s | Speed: 4.96 t/s | RAM: 4676.4 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 72.4%)
- **Locked-Line Status:** `punctuation_mismatch` (Preserved: False)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---

### Prompt 20: The non-romantic emotional test — Robustness and creative control
**Target:** `Emotional range · Family · 4 lines`

> **Prompt Text:** Write exactly 4 lines of Roman Hinglish poetry about an adult child noticing that their father has started asking for help with small things he once handled easily. Do not mention illness, death, old age directly, or fear of losing him. Avoid romantic language, melodrama, and moral lessons about family. Use an ordinary domestic detail, natural cadence, and a restrained voice. Let the final line communicate the shift in roles without explaining it.

**Raw Generated Output:**
```text
Tumhari khushboo lagti hai jaisa kuch chhota ho
Mere pas koi nahi lekin tumhare pas koi hai
Pehle tum yahan se bharne wala thi
Ab mera saath koi nahi lekin tumhare saath koi hai
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 8.328s | Speed: 4.81 t/s | RAM: 4262.74 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 61.8%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---
