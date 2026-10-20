# Benchmark Evaluation Report: Llama-3.2-3B-Instruct-Q4_K_M

- **Stage:** `FULL`
- **Date & Time:** 20261017_015647
- **Model Path:** `models/Llama-3.2-3B-Instruct-Q4_K_M.gguf`
- **Configuration:** 4 CPU threads | Context: 8192 tokens | Temp: 0.74

## 1. Hardware Performance Summary

| Metric | Target (PRD) | Measured Result | Status |
| :--- | :--- | :--- | :--- |
| **Model Load Time** | < 8.0s | **3.48s** | PASS |
| **Time-to-First-Token (TTFT)** | < 4.0s | **15.25s** (Cold: 200.091s) | CHECK |
| **Generation Speed** | ≥ 6.5 t/s | **6.36 t/s** | AMEND PRD |
| **Peak RAM** | < 6000 MB | **4455.3 MB** | PASS |

## 2. Strict Compliance & Language Quality Audit

| Audit Check | What it Verifies | Measured Result | Strict Status |
| :--- | :--- | :--- | :--- |
| **Script Compliance** | Latin/Roman script only; zero Devanagari/Arabic characters | **100.0%** | PASS |
| **Output Cleanliness** | Zero `<think>` reasoning tags, preambles, notes, explanations | **100.0%** | PASS |
| **Exact Line Count** | Matches requested lines exactly (2 for couplets, 4 for quatrains) | **100.0%** | PASS |
| **Hinglish Language Quality** | Authentic Roman Hindustani/Urdu vocabulary; not pure English | **100.0%** | PASS |
| **Locked-Line Preservation** | Character-for-character exact match; punctuation preserved; no repetition | **100.0%** | PASS |
| ⭐ **Overall Strict Pass Rate** | Satisfied ALL technical, structural, and negative constraints simultaneously | **95.0%** | PASS |

---

## 3. Qualitative Output & Poetic Voice Review
*(Human evaluation rubric: score 1–5 for cadence, restraint, originality, and final turn)*

### Prompt 01: The friendship that slowly changed — Emotional restraint and subtlety
**Target:** `Betrayal · Restraint · 4 lines`

> **Prompt Text:** Write a short Roman Hinglish poem about a close friend who slowly became a stranger. There was no fight and no clear ending; the conversations simply became shorter. Keep the tone quiet, personal, and slightly disappointed, not angry. Use everyday language and one concrete detail from ordinary life. Write exactly 4 lines. Avoid forced rhyming and familiar heartbreak clichés. The last line should reveal something the speaker has only just understood.

**Raw Generated Output:**
```text
Me tumse baat karte samay, tere doston ne hi kahaa
Aapke paas ek chai ka cup tha jo hum bhi usee tak pehle nahi pilaaya tha
Ab vah toh bahut different ho gaya hai aur mere saath kuchh nahin hai
Mujhe lagta hai ki woh abhi teri dosti hi thaa
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 200.091s | Speed: 4.87 t/s | RAM: 4432.05 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 50.0%)

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
Kuch likhne ki koshish to karoon, lekin fir se wapas chal jaa rahoon.
Aise hi main khuda ko yaad dilata hoon.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 6.592s | Speed: 5.19 t/s | RAM: 4434.59 MB
- **Structure:** Lines: 2/2 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 47.6%)

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
Mere dost ko tum saabit ho gaya
Kisi na kisi baat ki wajah se
Maine khud hi apni azaadi kiya hai
Ab teri zulf dhoondhna mushkil hai
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.424s | Speed: 5.99 t/s | RAM: 4436.19 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 55.6%)

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
Maine har din coffee khaana aur gulaal lagaane ka hissa ban gaya
Lagta hai wo hamesha raha, lekin ab bina use nahi kiya jaa sakta
Gulaal lagakar thoda chota sa aansoo nikalta tha jo khulne par nahin tha
Ab woh gulaal ka hissa ban gaya toh coffee khaana hi zyada mushkil ho raha hai
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.386s | Speed: 5.8 t/s | RAM: 4437.92 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 29.6%)

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
Chai ka thanda hua, hum dono ek side par hai
Achha nahi kuchh bolne ki zaroorat thi, lekin samajh mein raha tha
Kisi aur ko yah nahi dikhai de sakte, yeh kheltaa hai jahan hum rahe the
Ab thanda chai ka saamna karke ek dusre ke aankhon se milte hain
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.486s | Speed: 6.48 t/s | RAM: 4439.6 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 50.0%)

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
Mujhe rain ki dhoop peh chalna hai,
Jisne mere din ka mula kharab kar diya.
Paani mein mere aansoo naa aa rahe the,
Lekin humare paae ke andar thandak ho gayi.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.547s | Speed: 6.49 t/s | RAM: 4441.26 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 38.7%)

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
Mere ishq ki duniya mein
Kisi kaam ke liye toh leke hi aao
Hansat khali gharon se joochte hain
Iska khafaayat bhi kuch nahi hai
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 6.001s | Speed: 6.42 t/s | RAM: 4442.89 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 48.0%)

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
Kuch nahi karta, main uski baat sunta hoon
Usne promise kiya tha, woh bhi aane ka
Ab toh mere liye yah hi maza nahin hai
Main toofan mein chaltaa hu, jo wo haath na de.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.356s | Speed: 6.31 t/s | RAM: 4444.44 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 45.7%)

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
Bilkul, mere dost ke liye toh nahi tha koi badlaav
Aagey bhi jaise aapne kab se kuch nahi dekha hai
Kafi saal ho gaye hain, aur ab bhi tum hi hai
Ek samay ka intezar reh gya, phir woh khataab bhi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.838s | Speed: 6.64 t/s | RAM: 4445.96 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 61.0%)

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
Mere ishq ka thoda tamanna hai ki tum kha kar ho
Aur main bhi khana khao, na toh tum phooche nahi?
Kya tum apne andar hichki se chhoo gaye ho?
Main din raat dosti ke sath rahoon, tere dil ko.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.786s | Speed: 6.79 t/s | RAM: 4447.61 MB
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

### Prompt 11: Roman script discipline — Roman Hinglish and language control
**Target:** `Script compliance · 4 lines`

> **Prompt Text:** Write a 4-line poem in Roman Hinglish about a person returning to their childhood neighbourhood. Use the words "gali", "purana", "khidki", and "shayad" naturally. All Hindi and Urdu words must be written in Roman script. Do not use Devanagari, Arabic, or Nastaliq characters. Do not add a title, transliteration, explanation, or English introduction. Keep the poem understated and end with an observation about change.

**Raw Generated Output:**
```text
Mere purane shehar ke gali mein ja raha hoon
Jo khidki se apne aas-paas ki duniya dekhti thi
Ab yeh sahi nahi hai, shayad kuchh badal gaya tha
Lekin yah bhi thaa jo meri pyaar di chhaon mein raha
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** missing_words(purana)
- **Performance:** TTFT: 6.092s | Speed: 6.65 t/s | RAM: 4449.21 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 59.0%)
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
Mujhe ab sabr hai ki tumne kuch badal diya
Lehja ho gayi, woh to ek bar baaki rehta tha
Main hamesha samjhaa thaa ki tum mere liye hi
Aaj mujhe lagta hai ki yeh ek naya dil hai
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.3s | Speed: 6.75 t/s | RAM: 4450.75 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 63.2%)
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
Mujhe aasamand hua hai, o jalwa se hi
Neeche gire hue khilte ho tumhari choti si zubaan
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.151s | Speed: 6.51 t/s | RAM: 4452.25 MB
- **Structure:** Lines: 2/2 (MATCH)
- **Language Mode:** Sparse / Low Hinglish (Hinglish Density: 17.6%)

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
Mere khana ko thoda zyada tayar kar raha hoon
Bina kisi aur ke liye, apne aas-paas hi rehta hai
Kitchen mein dhoop aa rahi hai, pyazon ki tasveer
Achcha, ab humein sab kuch bhi nahi chaahe
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.274s | Speed: 6.55 t/s | RAM: 4453.74 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 44.4%)

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
Mere dimaag toot gaya, jaise kisi neeche ki cheez phooch li
Hum aage badhte hain, jabhi toh kaam chalta nahi hai
Main khade ho jaata hu, aur dekhta hu ki kitni si baat
Jabhi bhi main apne khilone ko uthaata hu, wo toot jati hi rahi
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.303s | Speed: 6.36 t/s | RAM: 4455.31 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 39.1%)

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
Maine us photo ko drawer mein rakha hai
Lekin ab to main usse nahi dekhta toh kya hua?
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.124s | Speed: 6.82 t/s | RAM: 4438.87 MB
- **Structure:** Lines: 2/2 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 55.6%)

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
Der se kuch nahi hai, ek aadat hai
Ghar mein ho tumne station ki baath lii
Lagta hai ke wo kaam karne wale hi thein
Aise hi hain unki zarooraten
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.24s | Speed: 6.88 t/s | RAM: 4440.43 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 50.0%)
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
Tumne apni zindagi ko thoda aur accha banaya hai
Mujhe lagta tha ki tum isse kar sakte hi nahi
Ab tum apna safar karta ho, ek baar phir bhi woh coffee kiya hai
Kisi ne yaad rakha to mujh par zikr nahin hota
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.77s | Speed: 6.76 t/s | RAM: 4441.93 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 48.8%)

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
Aaj bhi darwaza dheere se band kiya.
Kuch palon pehle, maine use to khatam kar diya tha
Lekin ab tak bhi, wo nahi aata hai mujhe apne ghar ke andar
Kyunki woh band rehna hain jo mere haathon mein rahenge.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 6.719s | Speed: 6.47 t/s | RAM: 4443.55 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 50.0%)
- **Locked-Line Status:** `exact_match` (Preserved: True)

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
Tum karke ek saal se nahi karta, ab tumhara bina kuch nahi hota
Kya tumne apni zindagi ki baat suni aur khud ka sawaal pucha?
Tere haath mein thoda pressure aa raha hai, mujhe bas karna hoga
Ab tu mere saamne chadta hai, jaise ek aapka dost
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 5.609s | Speed: 6.43 t/s | RAM: 4445.13 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 57.4%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---
