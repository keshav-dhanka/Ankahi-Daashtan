# Ankahi Dastaan — Finalists 20-Prompt Comparative Evaluation Report

- **Date & Time:** 2026-10-17 02:08:25
- **Hardware:** HP 240 G8 (Intel Core i3-1115G4 @ 3.00GHz, 16 GB RAM, CPU-only)
- **Context Window:** 8192 tokens | CPU Threads: 4
- **Protocol:** 60-second thermal normalization cooldown preceding each model run
- **Master Voice Card:** Tier 1 Baked-In Voice Card (`app/voice/skill.md`) loaded

---

## 1. Hardware Performance Summary (Full 20 Prompts)

| Model | Role | Load Time | Cold TTFT | Warm TTFT (Avg) | Speed (tok/s) | Peak RAM | PRD Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Qwen2.5-3B-Instruct** | Confirmed Primary Baseline | **3.83s** | 170.985s | **13.65s** | **6.95 t/s** | **3725.5 MB** | **PASS** |
| **Gemma-2-2B-IT** | Fast Draft Candidate | **2.7s** | 140.937s | **10.85s** | **7.13 t/s** | **3626.2 MB** | **PASS** |
| **Llama-3.2-3B-Instruct** | Secondary Challenger | **3.48s** | 200.091s | **15.25s** | **6.36 t/s** | **4455.3 MB** | **PASS** |
| **Qwen3-4B** | Experimental 4B Reasoner | **4.18s** | 257.722s | **20.98s** | **4.6 t/s** | **5395.8 MB** | **CHECK** |

---

## 2. Strict Multi-Metric Compliance & Language Quality Audit

| Model | Script Compliance | Output Cleanliness | Line Count Adherence | Roman Hinglish Fidelity | Locked Line Integrity | ⭐ Overall Strict Pass |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Qwen2.5-3B-Instruct** | 100.0% | 100.0% | 85.0% | 100.0% | 0.0% | **70.0%** (14/20) |
| **Gemma-2-2B-IT** | 100.0% | 100.0% | 65.0% | 100.0% | 100.0% | **60.0%** (12/20) |
| **Llama-3.2-3B-Instruct** | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | **95.0%** (19/20) |
| **Qwen3-4B** | 100.0% | 100.0% | 100.0% | 100.0% | 0.0% | **95.0%** (19/20) |

---

## 3. Side-by-Side Qualitative Verse Comparison across Key Prompts

### Prompt 01: The friendship that slowly changed (Emotional restraint and subtlety)
**Target:** `Betrayal · Restraint · 4 lines`
> **Prompt Text:** Write a short Roman Hinglish poem about a close friend who slowly became a stranger. There was no fight and no clear ending; the conversations simply became shorter. Keep the tone quiet, personal, and slightly disappointed, not angry. Use everyday language and one concrete detail from ordinary life. Write exactly 4 lines. Avoid forced rhyming and familiar heartbreak clichés. The last line should reveal something the speaker has only just understood.

#### **Qwen2.5-3B-Instruct** — ✅ STRICT PASS (Speed: 6.1 t/s | Hinglish: 54.8%)
```text
Aashiq dosti ki hai, jo zikhna milti thi
Khareedne vapas aa gaye vo hevaan karta hi
Yaad aati h fir bhi use batate nhi
Ek dard-e-dil jataa hotaa tha magar nahi
```

#### **Gemma-2-2B-IT** — ✅ STRICT PASS (Speed: 6.7 t/s | Hinglish: 3.7%)
```text
We used to talk for hours,
Now just short texts, a fleeting pause.
I miss the way you'd listen so deep, 
Just like that, everything changed asleep.
```

#### **Llama-3.2-3B-Instruct** — ✅ STRICT PASS (Speed: 4.87 t/s | Hinglish: 50.0%)
```text
Me tumse baat karte samay, tere doston ne hi kahaa
Aapke paas ek chai ka cup tha jo hum bhi usee tak pehle nahi pilaaya tha
Ab vah toh bahut different ho gaya hai aur mere saath kuchh nahin hai
Mujhe lagta hai ki woh abhi teri dosti hi thaa
```

#### **Qwen3-4B** — ✅ STRICT PASS (Speed: 3.79 t/s | Hinglish: 62.1%)
```text
Ishq karne ki tamanna thi  
Jo khatm ho gayi mere doston ne hi  
Itna yaad kiye ki hichki shuru ho gayi  
Yaad aati h fir bhi use batate nhi
```

---

### Prompt 05: A cold cup of chai (Originality and anti-cliché control)
**Target:** `Concrete imagery · 4 lines`
> **Prompt Text:** Write exactly 4 lines of Roman Hinglish poetry about two people sitting together after an uncomfortable conversation. A cup of chai has gone cold between them. Do not mention heartbreak, tears, loneliness, or silence directly. Do not personify the cup. Use the physical scene to communicate what the people cannot say. Avoid forced rhyme and end with a fresh, understated turn.

#### **Qwen2.5-3B-Instruct** — ✅ STRICT PASS (Speed: 6.75 t/s | Hinglish: 45.9%)
```text
Jo chai kho gaya hai, dard-e-dil jataane din
Bhi na karein or mere doston ne hi bade khayal
Zakhm gahaa hai magar zabaan ki aashiyaan ni
Yaad aa raha hoon toh ishq ke saraam daala hone ko
```

#### **Gemma-2-2B-IT** — ✅ STRICT PASS (Speed: 8.08 t/s | Hinglish: 34.5%)
```text
Chai ka dastak, haiya kharab ho gaya
Kaunsa baat thi uske liye hum dono? 
Kisi aisa saath jo haal mai chala gaa
Ek dusre ke eyes mein pyaar hai.
```

#### **Llama-3.2-3B-Instruct** — ✅ STRICT PASS (Speed: 6.48 t/s | Hinglish: 50.0%)
```text
Chai ka thanda hua, hum dono ek side par hai
Achha nahi kuchh bolne ki zaroorat thi, lekin samajh mein raha tha
Kisi aur ko yah nahi dikhai de sakte, yeh kheltaa hai jahan hum rahe the
Ab thanda chai ka saamna karke ek dusre ke aankhon se milte hain
```

#### **Qwen3-4B** — ✅ STRICT PASS (Speed: 4.38 t/s | Hinglish: 60.7%)
```text
Ishq karne ki tamanna thi  
Jo khatm ho gayi mere doston ne hi  
Itna yaad kiye ki hichki shuru ho gayi  
Kuch chhodna padega aap ke dil me
```

---

### Prompt 11: Roman script discipline (Roman Hinglish and language control)
**Target:** `Script compliance · 4 lines`
> **Prompt Text:** Write a 4-line poem in Roman Hinglish about a person returning to their childhood neighbourhood. Use the words "gali", "purana", "khidki", and "shayad" naturally. All Hindi and Urdu words must be written in Roman script. Do not use Devanagari, Arabic, or Nastaliq characters. Do not add a title, transliteration, explanation, or English introduction. Keep the poem understated and end with an observation about change.

#### **Qwen2.5-3B-Instruct** — ❌ FAIL (missing_words(purana)) (Speed: 7.66 t/s | Hinglish: 61.5%)
```text
Ishq karne ki tamanna thi
Jo khatm ho gayi mere gali ne hi  
Khidki aur khud se shayad aate hain  
Shayad to sabhi nahin chutti hai
```

#### **Gemma-2-2B-IT** — ❌ FAIL (line_count(6/4)) (Speed: 8.45 t/s | Hinglish: 66.7%)
```text
```
Gali mein shayad haqeeqat hai
Purana ghar, khud se bahut aasman ki
khidki chhodne ke baad hum yaadon se 
socha na tha abhi bhi mujhe lagta hai.
```
```

#### **Llama-3.2-3B-Instruct** — ❌ FAIL (missing_words(purana)) (Speed: 6.65 t/s | Hinglish: 59.0%)
```text
Mere purane shehar ke gali mein ja raha hoon
Jo khidki se apne aas-paas ki duniya dekhti thi
Ab yeh sahi nahi hai, shayad kuchh badal gaya tha
Lekin yah bhi thaa jo meri pyaar di chhaon mein raha
```

#### **Qwen3-4B** — ✅ STRICT PASS (Speed: 3.98 t/s | Hinglish: 52.9%)
```text
Shayad gali ki purana khidki ne kuch yaad raahin
Dil ke tukde harr pal karte hai use lekin
Mujhme fanna ho jaa ya mujhse to khafaa ho ja
Aab to ek tarfaa ho jaa
```

---

### Prompt 16: No explanation after the poem (Structure, cadence and final-line quality)
**Target:** `Format compliance · 2 lines`
> **Prompt Text:** Write one Roman Hinglish couplet about keeping an old photograph in a drawer but no longer looking at it. Output exactly 2 poetic lines and nothing else. No title, preamble, quotation marks, commentary, translation, or explanation. Avoid familiar phrases about memories and time healing everything. Use conversational language, no forced rhyme, and let the second line carry the emotional shift.

#### **Qwen2.5-3B-Instruct** — ✅ STRICT PASS (Speed: 6.86 t/s | Hinglish: 38.5%)
```text
Chalo phota kya hua drawer mein
Doston ne hi apna dharti chhod diya
```

#### **Gemma-2-2B-IT** — ✅ STRICT PASS (Speed: 6.06 t/s | Hinglish: 60.0%)
```text
Drawer mein ek phota hai,
Na dekho main baaki hi.
```

#### **Llama-3.2-3B-Instruct** — ✅ STRICT PASS (Speed: 6.82 t/s | Hinglish: 55.6%)
```text
Maine us photo ko drawer mein rakha hai
Lekin ab to main usse nahi dekhta toh kya hua?
```

#### **Qwen3-4B** — ✅ STRICT PASS (Speed: 5.08 t/s | Hinglish: 78.6%)
```text
Ishq ke dard ka ghav abhi koi nahi  
Zakhm gahare hai magar bataate nhi
```

---

### Prompt 19: The user protects the opening line (Robustness and creative control)
**Target:** `Pinned-line revision · 4 lines`
> **Prompt Text:** The first line is locked and must remain exactly unchanged: "Aaj bhi darwaza dheere se band kiya."
Write 3 additional lines of Roman Hinglish poetry that continue naturally from it. Do not rewrite, punctuate differently, or repeat the locked line. Keep the tone understated and conversational. Avoid forced rhyme, generic heartbreak language, and moralizing. Make the final line reveal a new detail about why the speaker still closes the door that way.

#### **Qwen2.5-3B-Instruct** — ❌ FAIL (pinned_line(punctuation_mismatch)) (Speed: 6.28 t/s | Hinglish: 57.6%)
```text
Aaj bhi darwaza dheere se band kiya
Zakhm zaafe hai, aashiq ke doosre doston ne hi
Tumse to kuchh nahi laga tha yeh chhaon khulna

Yaad aati h fir bhi use batate nhi
```

#### **Gemma-2-2B-IT** — ❌ FAIL (line_count(3/4)) (Speed: 7.62 t/s | Hinglish: 56.5%)
```text
Aaj bhi darwaza dheere se band kiya.
Kisi ke dil ka baarish hai yeh khudhi mein, 
Sari duniya ek pal hi chala gaya.
```

#### **Llama-3.2-3B-Instruct** — ✅ STRICT PASS (Speed: 6.47 t/s | Hinglish: 50.0%)
```text
Aaj bhi darwaza dheere se band kiya.
Kuch palon pehle, maine use to khatam kar diya tha
Lekin ab tak bhi, wo nahi aata hai mujhe apne ghar ke andar
Kyunki woh band rehna hain jo mere haathon mein rahenge.
```

#### **Qwen3-4B** — ❌ FAIL (pinned_line(punctuation_mismatch)) (Speed: 4.96 t/s | Hinglish: 72.4%)
```text
Aaj bhi darwaza dheere se band kiya  
Zakhm gahare hai magar bataate nhi  
Mahasoos to harr pal karte hai use lekin  
Yaad aati h fir bhi use batate nhi
```

---
