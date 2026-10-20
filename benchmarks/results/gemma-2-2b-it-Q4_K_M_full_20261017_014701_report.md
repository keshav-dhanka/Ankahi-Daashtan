# Benchmark Evaluation Report: gemma-2-2b-it-Q4_K_M

- **Stage:** `FULL`
- **Date & Time:** 20261017_014701
- **Model Path:** `models/gemma-2-2b-it-Q4_K_M.gguf`
- **Configuration:** 4 CPU threads | Context: 8192 tokens | Temp: 0.74

## 1. Hardware Performance Summary

| Metric | Target (PRD) | Measured Result | Status |
| :--- | :--- | :--- | :--- |
| **Model Load Time** | < 8.0s | **2.7s** | PASS |
| **Time-to-First-Token (TTFT)** | < 4.0s | **10.85s** (Cold: 140.937s) | CHECK |
| **Generation Speed** | ≥ 6.5 t/s | **7.13 t/s** | PASS |
| **Peak RAM** | < 6000 MB | **3626.2 MB** | PASS |

## 2. Strict Compliance & Language Quality Audit

| Audit Check | What it Verifies | Measured Result | Strict Status |
| :--- | :--- | :--- | :--- |
| **Script Compliance** | Latin/Roman script only; zero Devanagari/Arabic characters | **100.0%** | PASS |
| **Output Cleanliness** | Zero `<think>` reasoning tags, preambles, notes, explanations | **100.0%** | PASS |
| **Exact Line Count** | Matches requested lines exactly (2 for couplets, 4 for quatrains) | **65.0%** | FAIL |
| **Hinglish Language Quality** | Authentic Roman Hindustani/Urdu vocabulary; not pure English | **100.0%** | PASS |
| **Locked-Line Preservation** | Character-for-character exact match; punctuation preserved; no repetition | **100.0%** | PASS |
| ⭐ **Overall Strict Pass Rate** | Satisfied ALL technical, structural, and negative constraints simultaneously | **60.0%** | NEEDS TUNING |

---

## 3. Qualitative Output & Poetic Voice Review
*(Human evaluation rubric: score 1–5 for cadence, restraint, originality, and final turn)*

### Prompt 01: The friendship that slowly changed — Emotional restraint and subtlety
**Target:** `Betrayal · Restraint · 4 lines`

> **Prompt Text:** Write a short Roman Hinglish poem about a close friend who slowly became a stranger. There was no fight and no clear ending; the conversations simply became shorter. Keep the tone quiet, personal, and slightly disappointed, not angry. Use everyday language and one concrete detail from ordinary life. Write exactly 4 lines. Avoid forced rhyming and familiar heartbreak clichés. The last line should reveal something the speaker has only just understood.

**Raw Generated Output:**
```text
We used to talk for hours,
Now just short texts, a fleeting pause.
I miss the way you'd listen so deep, 
Just like that, everything changed asleep.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 140.937s | Speed: 6.7 t/s | RAM: 3605.61 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Sparse / Low Hinglish (Hinglish Density: 3.7%)

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
```
Phone screen, full of blue light's glare. 
Message deleted, but the feeling stays there.  

```
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** line_count(4/2)
- **Performance:** TTFT: 4.095s | Speed: 7.35 t/s | RAM: 3608.56 MB
- **Structure:** Lines: 4/2 (MISMATCH)
- **Language Mode:** Sparse / Low Hinglish (Hinglish Density: 7.1%)

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
```
Mujhe yeh laga tha ki duniya mein woh hi hai jo mujhe chahiye
But now it's just silence in my heart. 
I was not thinking, only wanting to be heard.
And that is the pain I carry still.
```
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** line_count(6/4)
- **Performance:** TTFT: 3.712s | Speed: 8.29 t/s | RAM: 3611.5 MB
- **Structure:** Lines: 6/4 (MISMATCH)
- **Language Mode:** Sparse / Low Hinglish (Hinglish Density: 18.4%)

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
Kaise yeh duniya thi aaj se khali hai 
Phir bhi yaad aye saath mein ek din ki chalo
Kisi ke baaton ko sunaane, aap mujhe kya karein
Mujhe apni zindagi ka koi meaning nahi milta.

```
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** line_count(6/4)
- **Performance:** TTFT: 3.566s | Speed: 8.23 t/s | RAM: 3614.43 MB
- **Structure:** Lines: 6/4 (MISMATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 54.3%)

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
Chai ka dastak, haiya kharab ho gaya
Kaunsa baat thi uske liye hum dono? 
Kisi aisa saath jo haal mai chala gaa
Ek dusre ke eyes mein pyaar hai.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 3.332s | Speed: 8.08 t/s | RAM: 3617.37 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 34.5%)

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
Rain falling, grey on streetlights' glow
Each drop a small complaint I let go
Phone's tone still echoes in my ear
But now the city is mine to wander.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.161s | Speed: 7.56 t/s | RAM: 3620.3 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Sparse / Low Hinglish (Hinglish Density: 3.4%)

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
Aaj to kharab hai yeh chakkar 
Baaki ghar, khayal ho jaaye ga
Tujhe pata nahi kya hua  hona chaiye
Ki main ye key nahin deta, mera saath rakhta.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.067s | Speed: 7.67 t/s | RAM: 3623.3 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 42.9%)

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
Mai khane ke liye ek khau kiya thaa
Aaj woh aa gaya, mujhe koi kahna hai 
Dil mein aise hi baat kar rahi thi 
Par kuchh nahi bola, sabhi ka jawab nahin
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 3.877s | Speed: 6.84 t/s | RAM: 3626.23 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 46.9%)

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
Saath hai ek din, woh aaya 
Aaj bhi same old jaisa haal  
Kya hua yaar tumne kya kar liya? 
Hum dono ka yeh khud ki raah.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 3.715s | Speed: 7.79 t/s | RAM: 3625.69 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 57.7%)

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
Maa kya kha liya, beta?
Chalta hai ya khair nahin. 
Dimag ka khana bhi, baaki kuch toh chukaa tha
Ab aata to hum yeh kahna chahte hain.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 3.455s | Speed: 5.02 t/s | RAM: 3190.86 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 37.0%)

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
```
Gali mein shayad haqeeqat hai
Purana ghar, khud se bahut aasman ki
khidki chhodne ke baad hum yaadon se 
socha na tha abhi bhi mujhe lagta hai.
```
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** line_count(6/4)
- **Performance:** TTFT: 4.329s | Speed: 8.45 t/s | RAM: 3194.15 MB
- **Structure:** Lines: 6/4 (MISMATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 66.7%)
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
```
Sabr se yeh bhi chalta hai, 
Lejha hai jo jata tha.
Na ho sakta to tumhara kya?  
Aaj chalne aaya ek naye samay.
```
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** line_count(6/4), missing_words(lehja)
- **Performance:** TTFT: 4.259s | Speed: 6.74 t/s | RAM: 3197.09 MB
- **Structure:** Lines: 6/4 (MISMATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 52.2%)
- **Required Words Check:** lehja

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
Aachaa chalo, mujhe pata hai woh bhi.
Kabhi kabhi thoda sa khushi hota hai.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 3.669s | Speed: 7.58 t/s | RAM: 3200.05 MB
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

### Prompt 14: The quiet final turn — Structure, cadence and final-line quality
**Target:** `Ending impact · 4 lines`

> **Prompt Text:** Write a 4-line Roman Hinglish poem about a person preparing a favourite meal for someone who will not be coming home anymore. Do not state why the person is absent. Keep the first three lines observational and restrained. The fourth line must change how the reader understands the scene, without adding a new character or explaining the symbolism. Avoid tears, heartbreak clichés, and moral lessons.

**Raw Generated Output:**
```text
```
Khana bana rahi hun, khushbu hai woh 
Kaise tum nahin aaoge mere ghar par, woh 
Kuchh toh hamesha banta hai yaar, ek din baad 
Mujhe ye khaana bhi dekhaane ka dar.
```
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** line_count(6/4)
- **Performance:** TTFT: 3.837s | Speed: 7.28 t/s | RAM: 3202.98 MB
- **Structure:** Lines: 6/4 (MISMATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 35.5%)

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
Door shut, tired bones.
No hand to squeeze back the sigh 
that hangs heavy from my chest.
Silence, even in this crowded room.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.142s | Speed: 4.07 t/s | RAM: 3205.92 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Sparse / Low Hinglish (Hinglish Density: 8.7%)

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
Drawer mein ek phota hai,
Na dekho main baaki hi.
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.615s | Speed: 6.06 t/s | RAM: 3208.86 MB
- **Structure:** Lines: 2/2 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 60.0%)

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
station ka khwaab
aadat se aasman mein
der se haye sapno ko 
ghhar par rahi hai ghari
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** missing_words(ghar)
- **Performance:** TTFT: 3.8s | Speed: 7.07 t/s | RAM: 3208.86 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 47.1%)
- **Required Words Check:** ghar

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
Hain, mujhe pata hai tum khush ho
Zindagi ke badle aise hi ho jaate hain 
Kisi tarah ka baat nahin karna
Kabhi kabhi woh saath mere liye thode thumke
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.063s | Speed: 7.04 t/s | RAM: 3167.8 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 41.4%)

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
Kisi ke dil ka baarish hai yeh khudhi mein, 
Sari duniya ek pal hi chala gaya.
```

- **Technical Verdict:** ❌ **FAILED CONSTRAINTS:** line_count(3/4)
- **Performance:** TTFT: 4.698s | Speed: 7.62 t/s | RAM: 3170.77 MB
- **Structure:** Lines: 3/4 (MISMATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 56.5%)
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
baap ki aaram, bahut mushkil hai
saath mein kyun raaste bhar jaate hain 
khud ka work, khud se baat karne ka koi waqt nahin tha
ab mere paas to woh kya hoga?
```

- **Technical Verdict:** ✅ **STRICT PASS**
- **Performance:** TTFT: 4.697s | Speed: 7.24 t/s | RAM: 3173.7 MB
- **Structure:** Lines: 4/4 (MATCH)
- **Language Mode:** Roman Hinglish (Hinglish Density: 56.2%)

| Criterion | Score (1-5) | Qualitative Notes |
| :--- | :---: | :--- |
| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |
| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |
| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |
| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |
| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |

---
