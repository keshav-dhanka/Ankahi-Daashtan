# Benchmark Evaluation Report: Phi-3.5-mini-instruct-Q4_K_M

- **Stage:** `SMOKE`
- **Date & Time:** 20261017_000313
- **Model Path:** `models/Phi-3.5-mini-instruct-Q4_K_M.gguf`
- **Threads:** 4 CPU threads | Context: 2048 tokens

## 1. Hardware Performance Summary

| Metric | Target (PRD) | Measured Result | Status |
| :--- | :--- | :--- | :--- |
| **Model Load Time** | < 8.0s | **3.2s** | PASS |
| **Time-to-First-Token (TTFT)** | < 4.0s | **27.84s** (Cold: 67.735s) | CHECK |
| **Generation Speed** | ≥ 6.5 t/s | **4.49 t/s** | AMEND PRD |
| **Peak RAM** | < 6000 MB | **4418.8 MB** | PASS |
| **Script Compliance** | ≥ 99% | **100.0%** | PASS |

---

## 2. Qualitative Output & Voice Fidelity Review
*(Fill in the 1–5 scoring rubric below based on human evaluation)*

### Prompt 11: Roman script discipline (Roman Hinglish and language control)
**Target:** `Script compliance · 4 lines`

> **Prompt Text:** Write a 4-line poem in Roman Hinglish about a person returning to their childhood neighbourhood. Use the words "gali", "purana", "khidki", and "shayad" naturally. All Hindi and Urdu words must be written in Roman script. Do not use Devanagari, Arabic, or Nastaliq characters. Do not add a title, transliteration, explanation, or English introduction. Keep the poem understated and end with an observation about change.

**Generated Poem Output:**
```text
Gali mein khidki ki puran,
Nostalgia's shayad jagah se bhi aansoo.  
Zindagi ko pilaane woh chandi ho jaaye hazaar,   
Rajaas ka rang aur marham pe hota naha gaya karo sahara banjarein vrat karoonaan shayad na change lagta raha thahai.
```

- **TTFT:** 67.735s | **Speed:** 4.17 t/s | **Lines:** 4/4 | **Script Valid:** True

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
Pahunch ka drawer, ghar par nahi bhool se khush hua fotoon tak
Safar ko karun mein dholak na chahe lag raha ho.
```

- **TTFT:** 7.061s | **Speed:** 4.79 t/s | **Lines:** 2/2 | **Script Valid:** True

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
Sab kuch bhi sakhti, jis se aansooni dhoondh raha hai.
Nazar ke chanchal ne humara saath tak hota ho jaise naa band karte theek nahin; 
Koi jo ek baat kiya lagaai hi kuch bhi nikalta, jiski taadpatti par aavashyak hai.
```

- **TTFT:** 8.714s | **Speed:** 4.5 t/s | **Lines:** 3/4 | **Script Valid:** True

| Criterion | Score (1-5) | Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural rhythm, conversational flow |
| **Emotional Restraint** | [ ] | Understated, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Fresh imagery, avoids stock clichés |
| **Final Turn Impact** | [ ] | Quiet landing in final line |
| **Instruction Adherence** | [ ] | Met line count and explicit constraints |

---
