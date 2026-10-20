# Benchmark Evaluation Report: mistral-7b-instruct-v0.2.Q4_K_M

- **Stage:** `SMOKE`
- **Date & Time:** 20261016_225324
- **Model Path:** `models/mistral-7b-instruct-v0.2.Q4_K_M.gguf`
- **Threads:** 4 CPU threads | Context: 2048 tokens

## 1. Hardware Performance Summary

| Metric | Target (PRD) | Measured Result | Status |
| :--- | :--- | :--- | :--- |
| **Model Load Time** | < 8.0s | **18.46s** | CHECK |
| **Time-to-First-Token (TTFT)** | < 4.0s | **35.81s** (Cold: 82.872s) | CHECK |
| **Generation Speed** | ≥ 6.5 t/s | **2.99 t/s** | AMEND PRD |
| **Peak RAM** | < 6000 MB | **5966.2 MB** | PASS |
| **Script Compliance** | ≥ 99% | **100.0%** | PASS |

---

## 2. Qualitative Output & Voice Fidelity Review
*(Fill in the 1–5 scoring rubric below based on human evaluation)*

### Prompt 11: Roman script discipline (Roman Hinglish and language control)
**Target:** `Script compliance · 4 lines`

> **Prompt Text:** Write a 4-line poem in Roman Hinglish about a person returning to their childhood neighbourhood. Use the words "gali", "purana", "khidki", and "shayad" naturally. All Hindi and Urdu words must be written in Roman script. Do not use Devanagari, Arabic, or Nastaliq characters. Do not add a title, transliteration, explanation, or English introduction. Keep the poem understated and end with an observation about change.

**Generated Poem Output:**
```text
Purana gali mein woh aaya, khidki se nazar aata hai,
Kuchh ishq-e-junoon ke zindagi ki qismat hue, shayad,
Phir bhi un sab ke doston ne rahi, gali ka andhera,
Woh kabhii usse wapis paa jata tha, purana samaya. (Change: Aki sab thekhra, gali ke qabil nahin ab)
```

- **TTFT:** 82.872s | **Speed:** 2.99 t/s | **Lines:** 4/4 | **Script Valid:** True

| Criterion | Score (1-5) | Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural rhythm, conversational flow |
| **Emotional Restraint** | [ ] | Understated, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Fresh imagery, avoids stock clichés |
| **Final Turn Impact** | [ ] | Quiet landing in final line |
| **Instruction Adherence** | [ ] | Met line count and explicit constraints |

---

### Prompt 16: No explanation after the poem (Structure, cadence and final-line quality)
**Target:** `Format compliance · 2 lines`

> **Prompt Text:** Write one Roman Hinglish couplet about keeping an old photograph in a drawer but no longer looking at it. Output exactly 2 poetic lines and nothing else. No title, preamble, quotation marks, commentary, translation, or explanation. Avoid familiar phrases about memories and time healing everything. Use conversational language, no forced rhyme, and let the second line carry the emotional shift.

**Generated Poem Output:**
```text
Old photograph in a drawer lies,
Glimmer of past in forgotten eyes.
```

- **TTFT:** 11.324s | **Speed:** 2.91 t/s | **Lines:** 2/2 | **Script Valid:** True

| Criterion | Score (1-5) | Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural rhythm, conversational flow |
| **Emotional Restraint** | [ ] | Understated, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Fresh imagery, avoids stock clichés |
| **Final Turn Impact** | [ ] | Quiet landing in final line |
| **Instruction Adherence** | [ ] | Met line count and explicit constraints |

---

### Prompt 19: The user protects the opening line (Robustness and creative control)
**Target:** `Pinned-line revision · 4 lines`

> **Prompt Text:** The first line is locked and must remain exactly unchanged: "Aaj bhi darwaza dheere se band kiya."
Write 3 additional lines of Roman Hinglish poetry that continue naturally from it. Do not rewrite, punctuate differently, or repeat the locked line. Keep the tone understated and conversational. Avoid forced rhyme, generic heartbreak language, and moralizing. Make the final line reveal a new detail about why the speaker still closes the door that way.

**Generated Poem Output:**
```text
Aaj bhi darwaza dheere se band kiya,
Khud ko kah raha tha ek baar-baar, "Aisa hi rahega?"
Hamein unki aankhen zaroor dekhi,
Par woh meri awaadh ke siva kabhi.

Aaj bhi darwaza dheere se band kiya,
Uski jhoolan mein raaton ka talismann,
Mujhe unki aasman ke tamanna batayi,
Lekin uske baare mein main sabse pehle mann.

Aaj bhi dar
```

- **TTFT:** 13.24s | **Speed:** 3.07 t/s | **Lines:** 9/4 | **Script Valid:** True

| Criterion | Score (1-5) | Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural rhythm, conversational flow |
| **Emotional Restraint** | [ ] | Understated, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Fresh imagery, avoids stock clichés |
| **Final Turn Impact** | [ ] | Quiet landing in final line |
| **Instruction Adherence** | [ ] | Met line count and explicit constraints |

---
