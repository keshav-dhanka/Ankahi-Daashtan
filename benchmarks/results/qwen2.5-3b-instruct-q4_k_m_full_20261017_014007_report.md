# Benchmark Evaluation Report: qwen2.5-3b-instruct-q4_k_m

- **Stage:** `FULL`
- **Date & Time:** 20261017_014007
- **Model Path:** `models/qwen2.5-3b-instruct-q4_k_m.gguf`
- **Configuration:** 4 CPU threads | Context: 8192 tokens | Temp: 0.74

## 1. Hardware Performance Summary

| Metric | Target (PRD) | Measured Result | Status |
| :--- | :--- | :--- | :--- |
| **Model Load Time** | < 8.0s | **3.83s** | PASS |
| **Time-to-First-Token (TTFT)** | < 4.0s | **13.65s** (Cold: 170.985s) | CHECK |
| **Generation Speed** | ≥ 6.5 t/s | **6.95 t/s** | PASS |
| **Peak RAM** | < 6000 MB | **3725.5 MB** | PASS |

## 2. Strict Compliance & Language Quality Audit

| Audit Check | What it Verifies | Measured Result | Strict Status |
| :--- | :--- | :--- | :--- |
| **Script Compliance** | Latin/Roman script only; zero Devanagari/Arabic characters | **100.0%** | PASS |
| **Output Cleanliness** | Zero `<think>` reasoning tags, preambles, notes, explanations | **100.0%** | PASS |
| **Exact Line Count** | Matches requested lines exactly (2 for couplets, 4 for quatrains) | **85.0%** | FAIL |
| **Hinglish Language Quality** | Authentic Roman Hindustani/Urdu vocabulary; not pure English | **100.0%** | PASS |
| **Locked-Line Preservation** | Character-for-character exact match; punctuation preserved; no repetition | **0.0%** | FAIL |
| ⭐ **Overall Strict Pass Rate** | Satisfied ALL technical, structural, and negative constraints simultaneously | **70.0%** | NEEDS TUNING |

---

## 3. Qualitative Output & Poetic Voice Review
*(Human evaluation rubric: score 1–5 for cadence, restraint, originality, and final turn)*

### Prompt 01: The friendship that slowly changed — Emotional restraint and subtlety
**Target:** `Betrayal · Restraint · 4 lines`

> **Prompt Text:** Write a short Roman Hinglish poem about a close friend who slowly became a stranger. There was no fight and no clear ending; the conversations simply became shorter. Keep the tone quiet, personal, and slightly disappointed, not angry. Use everyday language and one concrete detail from ordinary life. Write exactly 4 lines. Avoid forced rhyming and familiar heartbreak clichés. The last line should reveal something the speaker has only just understood.

**Raw Generated Output:**
```text
Aashiq dosti ki hai, jo zikhna milti thi
Khareedne vapas aa gaye vo hevaan karta hi
Yaad aati h fir bhi use batate nhi
Ek dard-e-dil jataa hotaa tha magar nahi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 170.985s | Speed: 6.1 t/s | RAM: 3690.14 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 54.8%)

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
Aphone pe shuru karte thi typing, 
Khatam ho gaye to delete vapas aa gaya.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 7.058s | Speed: 5.75 t/s | RAM: 3692.41 MB
- **Structure:** Lines: 2/2 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 50.0%)

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
Ishq karne ki tamanna thi
Jo khatm ho gayi mere doston ne hi
Intezaar ke baad yahin jaati h fir bhi 
Yaad aati h fir bhi use batate nhi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.37s | Speed: 6.3 t/s | RAM: 3694.31 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 58.6%)

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
```
Aisa lagta hai jaise ek baar chutti aa gayi
Is taraf se ab vo to kal nahi aayee naa
Dosti ka khafaa hua, kitni yaad aati hi ho 
Yaada ko khol do, yeh galtiya ho jaaye
```
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** line_count(6/4)
- **Performance:** TTFT: 6.662s | Speed: 7.66 t/s | RAM: 3696.18 MB
- **Structure:** Lines: 6/4 (MISMATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 36.1%)

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
Jo chai kho gaya hai, dard-e-dil jataane din
Bhi na karein or mere doston ne hi bade khayal
Zakhm gahaa hai magar zabaan ki aashiyaan ni
Yaad aa raha hoon toh ishq ke saraam daala hone ko
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.124s | Speed: 6.75 t/s | RAM: 3698.12 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 45.9%)

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
Ishq karne ki tamanna thi
Jo khatm ho gayi mere doston ne hi  
Jhar ke chhupke pani ka tair 
Toota hua dil, ek tarfaa ho jaa
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** forbidden_words(2)
- **Performance:** TTFT: 4.752s | Speed: 7.95 t/s | RAM: 3700.06 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 46.2%)
- ⚠️ **Forbidden Violations Detected:** banned_word:toota hua dil, cliché:toota hua dil

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
**Ishq karne ki tamanna thi**
Jo khatm ho gayi mere doston ne hi
Jahan key laagti hai uske behtar
Rang mein khali bane ke tum jaa jaao
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.517s | Speed: 6.47 t/s | RAM: 3701.91 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 48.1%)

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
Ishq karne ki tamanna thi
Jo khatm ho gayi mere doston ne hi
Intezaar ke bad, aashiq se nahi aa gaya  
Yaad aati h fir bhi use batate nhi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.382s | Speed: 7.53 t/s | RAM: 3703.73 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 65.5%)

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
Ishq karne ki tamanna thi
Jo khatm ho gayi mere doston ne hi
Aur ab tak ek baar toh bataao 
Yaad aati h fir bhi use batate nhi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.629s | Speed: 7.26 t/s | RAM: 3705.54 MB
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

### Prompt 10: Everyday Punjabi nuance — Roman Hinglish and language control
**Target:** `Regional language naturalness · 4 lines`

> **Prompt Text:** Write 4 lines of Roman Hinglish poetry about a mother asking whether her adult child has eaten, while avoiding a direct conversation about their growing distance. Use natural North Indian conversational phrasing, with at most one or two Punjabi expressions if they fit organically. Do not exaggerate a regional accent or use caricatured dialect. Avoid melodrama. The final line should suggest care without explicitly explaining it.

**Raw Generated Output:**
```text
Mujhse kaise hoga, dost? 
Jiska aam ko khaye?
Chupchup aa jao na, 
Nahi to maa hi bataati.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.76s | Speed: 7.46 t/s | RAM: 3707.42 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 23.5%)

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
Ishq karne ki tamanna thi
Jo khatm ho gayi mere gali ne hi  
Khidki aur khud se shayad aate hain  
Shayad to sabhi nahin chutti hai
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** missing_words(purana)
- **Performance:** TTFT: 5.93s | Speed: 7.66 t/s | RAM: 3709.21 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 61.5%)
- **Required Words Check:** purana

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
```
Sabhon ke lehja hai, maa thak rahi h
Aur yeh baari bhi nahin aata kisaki
Kisi dosto ko ishq se bahut sabr ho jaao
Leh jo nayi baar jaye to ab mujhe naa chahie.
```
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** line_count(6/4)
- **Performance:** TTFT: 4.972s | Speed: 7.57 t/s | RAM: 3711.08 MB
- **Structure:** Lines: 6/4 (MISMATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 41.2%)
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
Mujhse khul jaao, zyaad nahi
Inteqaal ho gaya hai use lekin
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.923s | Speed: 6.65 t/s | RAM: 3712.93 MB
- **Structure:** Lines: 2/2 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 45.5%)

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
Zakhm gahare hai magar bataate nhi
Mahasoos to harr pal karte hai use lekin
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.696s | Speed: 7.53 t/s | RAM: 3714.72 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 70.4%)

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
Ek din bhi toh ghaas ke jhalam ka kahaan hai
Kaal shuru ho rahi h, zakhm ne dard se khadraa ho jaao
Ghar mei baap ki saraahon mein raag hi nahi aaya
Mujhe dhoom karne wali chhaon main thaaqat na aa gayee
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.057s | Speed: 7.2 t/s | RAM: 3716.53 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 45.2%)

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
Chalo phota kya hua drawer mein
Doston ne hi apna dharti chhod diya
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.592s | Speed: 6.86 t/s | RAM: 3718.32 MB
- **Structure:** Lines: 2/2 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 38.5%)

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
Der se ghara, aadat mein station par
Dard-e-dil hai, der ka ghar yaad raha 
Khafaa to harr pal karte hai use lekin
Yaad aati h fir bhi usse batate nhi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.351s | Speed: 6.68 t/s | RAM: 3720.13 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 60.0%)
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
```
Ishq karne ki tamanna thi
Jo khatm ho gayi mere doston ne hi
Aashiq se ye baap zulfon ka ghav jaa
Yaad aati h fir bhi use batate nhi
```
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** line_count(6/4)
- **Performance:** TTFT: 4.564s | Speed: 6.41 t/s | RAM: 3721.95 MB
- **Structure:** Lines: 6/4 (MISMATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 55.2%)

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
Zakhm zaafe hai, aashiq ke doosre doston ne hi
Tumse to kuchh nahi laga tha yeh chhaon khulna

Yaad aati h fir bhi use batate nhi
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** pinned_line(punctuation_mismatch)
- **Performance:** TTFT: 6.954s | Speed: 6.28 t/s | RAM: 3723.75 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 57.6%)
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
Ishq karne ki tamanna thi
Jo khatm ho gayi mere doston ne hi
Zakhm gahare hai magar bataate nhi
Yaad aati h fir bhi use batate nhi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.663s | Speed: 7.01 t/s | RAM: 3725.54 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 66.7%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---
