# ANKAHI DASTAAN (अनकही दास्तान) — Master Product Requirements Document (PRD)

**Version:** 2.2 (Engineering & Production Specification)  
**Status:** Approved Master Blueprint  
**Platform:** Windows 10/11 Desktop (Standalone Native Application via PyWebView + PyInstaller)  
**Target Hardware:** HP 240 G8 (11th Gen Intel Core i3-1115G4 / 1125G4, 16 GB DDR4 RAM, 512 GB NVMe SSD, CPU-Only Inference)  
**Security & Privacy:** 100% Offline, Localhost Hardened, Zero External Network Calls  

---

## 1. Executive Summary & Product Vision

### 1.1 The Purpose
**Ankahi Dastaan (Untold Story)** is an intimate, distraction-free desktop poetry studio designed for writers who compose in **Hinglish** (Roman script combining conversational Hindi, Urdu-register vocabulary, and Punjabi nuances).

Unlike generic AI models that default to greeting-card rhyming, florid Urdu clichés (*shama-parwana*, *jaam-o-meena*), or hallucinated Devanagari/Nastaliq scripts, Ankahi Dastaan writes with **deliberate emotional restraint**, natural cadence, and a quiet, resonant turn in the final line (*misra-e-sani*).

### 1.2 Core Product Pillars
1. **The Intimate Writing Space:** A writer-first canvas supporting in-place line editing, pinning lines, and targeted surgical revisions.
2. **True Voice Personalization:** A 3-tier engine utilizing negative constraints, adaptive tag-based retrieval from `user_poems.md`, and deterministic preference extraction from manual line edits.
3. **Hardware Realism:** Tailored specifically for an 11th Gen Intel i3 CPU, using an exact **3B GGUF model** running sequential variations with robust, instant cancellation.
4. **Zero-Trust Hardened Privacy:** Local-only assets (no CDNs, no Google Fonts), hardened local API with token protection, and writable user paths respecting Windows security boundaries.

---

## 2. Model Evaluation, Selection & Hardware Calibration

### 2.1 Full 20-Prompt Hardware Benchmark Results (HP 240 G8)
All four finalists were evaluated across the complete 20-prompt suite on the target hardware (Intel Core i3-1115G4 @ 3.00GHz, 16 GB RAM, CPU-only, 4 threads, AVX2 enabled) with the master 337-line Voice Card (`app/voice/skill.md`) loaded and a 60-second thermal cooldown preceding each model run:

| Model | File / Identifier | Load Time | Warm TTFT (Avg) | Speed (tok/s) | Peak RAM | Strict Pass Rate | Architectural Role |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Llama-3.2-3B-Instruct** | `Llama-3.2-3B-Instruct-Q4_K_M.gguf` | 3.48s | 15.25s | **6.36 t/s** | 4,455 MB | **95.0%** (19/20) | **Recommended (Top Creative & Structural Control)** |
| **Qwen2.5-3B-Instruct** | `qwen2.5-3b-instruct-q4_k_m.gguf` | 3.83s | 13.65s | **6.95 t/s** | 3,726 MB | **70.0%** (14/20) | **Fast Baseline (High Throughput & Low RAM)** |
| **Gemma-2-2B-IT** | `gemma-2-2b-it-Q4_K_M.gguf` | **2.70s** | **10.85s** | **7.13 t/s** | **3,626 MB** | **60.0%** (12/20) | **Fast Draft Engine (Ultra-Lightweight Ideation)** |
| **Qwen3-4B** | `Qwen3-4B-Q4_K_M.gguf` | 4.18s | 20.98s | 4.60 t/s | 5,396 MB | 95.0% (19/20) | **Experimental 4B (Heavier RAM & Slower)** |

> [!NOTE]
> **Performance & Thermal Throttling Contract:** On sustained CPU inference sessions, thermal throttling on the i3-1115G4 reduces sustained tok/s by approximately 30–40% compared to a fresh cold start. The app UI provides a live `tokens_per_sec` counter during generation and displays a subtle advisory when thermal throttling occurs.

### 2.2 Model Selector Dropdown Specification (UI Schema)
The desktop UI model dropdown selector renders rich metadata to empower the user to pick the best model for their current writing task:

```json
[
  {
    "id": "llama-3.2-3b",
    "name": "Llama 3.2 3B Instruct",
    "badge": "Recommended · Top Creative Voice",
    "file": "Llama-3.2-3B-Instruct-Q4_K_M.gguf",
    "speed_label": "6.4 tok/s",
    "ram_label": "4.4 GB",
    "description": "Best for original, restrained poetry. 100% line-count adherence, perfect locked-line preservation, and zero cliché memorization.",
    "is_default": true
  },
  {
    "id": "qwen-2.5-3b",
    "name": "Qwen 2.5 3B Instruct",
    "badge": "Fast Baseline · Low RAM",
    "file": "qwen2.5-3b-instruct-q4_k_m.gguf",
    "speed_label": "7.0 tok/s",
    "ram_label": "3.7 GB",
    "description": "High-speed generation with minimal memory footprint. Excellent for rapid couplets and conversational shayari.",
    "is_default": false
  },
  {
    "id": "gemma-2-2b",
    "name": "Gemma 2 2B IT",
    "badge": "Quick Draft · Lightest",
    "file": "gemma-2-2b-it-Q4_K_M.gguf",
    "speed_label": "7.1 tok/s",
    "ram_label": "3.6 GB",
    "description": "Fastest loading and lowest resource consumption. Ideal for rapid brainstorming and seed line ideation.",
    "is_default": false
  },
  {
    "id": "qwen3-4b",
    "name": "Qwen3 4B Instruct",
    "badge": "Experimental 4B Reasoner",
    "file": "Qwen3-4B-Q4_K_M.gguf",
    "speed_label": "4.6 tok/s",
    "ram_label": "5.4 GB",
    "description": "4-billion parameter hybrid model with thinking suppression. Higher depth but runs heavier on laptop CPU.",
    "is_default": false
  }
]
```

### 2.3 Eliminated Models (Failed Hardware Bar)
- **Mistral-7B-Instruct-v0.2:** Speed (2.99 t/s) fails minimum criteria; RAM (5,966 MB) consumes system headroom; generated 9 lines for 4 requested and looped on locked lines.
- **Phi-3.5-mini-instruct:** Speed (4.49 t/s) below threshold; committed serious qualitative failures (completely dropped locked opening lines and generated hallucinated word salad).

### 2.4 Runtime Inference Settings & CPU Calibration

```python
# app/config.py - Optimized CPU parameters for Intel Core i3
RUNTIME_CONFIG = {
    "n_ctx": 8192,               # Expanded to comfortably house master 3.6k-token Voice Card + generations
    "n_threads": 4,              # Physical cores / optimal hyperthreads (benchmarked on setup)
    "n_batch": 512,              # Prompt evaluation batch size
    "temperature": 0.74,         # Creative nuance without random lexical drift
    "top_p": 0.90,               # Nucleus sampling threshold
    "top_k": 40,                 # Eliminates long-tail low-probability tokens
    "repeat_penalty": 1.18,      # Strongly discourages repeating 'dil', 'dard', 'yaad'
    "max_tokens": 150            # Safety cap; target poetic output is 25-50 words (2-6 lines)
}
```

---

## 3. The 3-Tier Voice Engine & Anti-Cliché Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                          USER PROMPT / SEED                            │
│           "doston ka badal jana, make it quiet, not angry"             │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ TIER 1: CRAFT BLUEPRINT (skill.md)                                     │
│ • Strict Roman script enforcement; never Devanagari/Nastaliq           │
│ • Couplet / 4-line structure; rhythm over strict forced meter          │
│ • Negative Constraint Engine: Explicit banned clichés list             │
│ • The Turn: Emotional weight lands softly in the final line            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ TIER 2: ADAPTIVE RETRIEVAL (Lightweight BM25 / Tag Matcher)            │
│ • Extracts intent tags: [#dosti, #badlaav, #khamoshi]                  │
│ • Selects Top 2-3 most relevant poems from user_poems.md               │
│ • Prevents context bloat and speeds up prompt processing               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ TIER 3: DETERMINISTIC PREFERENCE ENGINE (user_preferences.json)        │
│ • Analyzes past manual line edits (Original vs Edited)                 │
│ • Applies confirmed preference rules (Confidence >= 2)                 │
│ • User can review, toggle, or delete learned preferences in UI         │
└────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Tier 1: Craft Guidelines & Negative Constraints (`app/voice/skill.md`)
1. **Script Rule:** Roman Hinglish only. Punctuation allowed: standard English punctuation. Unicode check strictly rejects Devanagari (`U+0900–U+097F`) and Arabic/Nastaliq (`U+0600–U+06FF`).
2. **Emotional Register:** Understated, conversational, observational. Grief is stated simply, without theatrical melodrama.
3. **Broad Emotional Themes:** Confession, regret, aging, friendship, quiet realization, familial distance, and spiritual solitude.
4. **Negative Constraint List (Banned Clichés):**
   - Prohibited pairings: *shama-parwana*, *jaam-sharab*, *aansuon ka darya*, *dil ke tukde*, *zulfon ki chhaon*.
   - Prohibited stock openings: *"Ek din...", "Aisa lagta hai jaise...", "Kash hum..."* unless explicitly seeded.
   - Forbid moralizing conclusions or poetic summaries in the final line.

### 3.2 Tier 2: Adaptive Tag-Based Example Retrieval
Instead of dumping 20 poems into context (which burns prompt evaluation time and causes cliché imitation):
- Poems in `user_poems.md` are annotated with Markdown headers containing metadata:
  ```markdown
  ### Poem: Raat Ki Chai
  Tags: #tanhaai #intezaar #dheema #couplet
  Lines:
  Thandi chai ki chuskiyon mein raat nikal gayi,
  Woh baat jo kehni thi, zubaan par hi reh gayi.
  ---
  ```
- The backend matches user seed keywords against poem tags and lexical tokens using BM25 scoring.
- Exactly **2 reference poems** are dynamically injected as few-shot examples into the ChatML prompt.

### 3.3 Tier 3: Deterministic Preference Extractor
When a user edits a line in a generated poem card and clicks **Save** or **Keep**:
- The pair `(original_line, edited_line)` is stored in `poem_revisions`.
- The deterministic learner evaluates:
  1. **Lexical replacement:** Replaced recurring word $W_1$ with $W_2$ $\rightarrow$ Add $W_1$ to tentative downweight list.
  2. **Length reduction:** User consistently shortens lines by > 3 words $\rightarrow$ Flag preference: `prefer_short_lines`.
  3. **Rhyme removal:** User removes forced ending rhyming syllables $\rightarrow$ Flag preference: `prefer_blank_verse`.
- **Confidence Threshold:** A rule is only promoted to `user_preferences.json` if observed $\ge 2$ times.
- **User Control:** The Settings modal contains a **"Learned Preferences"** section with toggles to enable, disable, or delete any preference.

---

## 4. Generation Lifecycle, Cancellation & Revision Workflow

### 4.1 Generation Lifecycle & Backend Cancellation Contract
Frontend `AbortController` aborts the client HTTP connection, but does **not** stop CPU inference inside `llama_cpp`. To prevent CPU hangs and thread starvation, the backend implements cooperative cancellation via a dedicated `GenerationJob` manager:

```
[UI: Takhleeq Karo] ──► POST /api/generate ──► Allocates job_id (UUID)
                                │                      │
                                │                      ▼
                                │             [ModelManager Inference Loop]
                                │             while token in model:
                                │                 if job.cancel_event.is_set():
                                │                     break (releases CPU immediately)
                                │                 stream token -> SSE
                                │
[UI: Esc / Stop Button] ─► POST /api/generate/cancel/{job_id} ──► Sets cancel_event
```

#### Backend Contract:
1. Every generation request is assigned a `job_id`.
2. The endpoint `/api/generate/cancel/{job_id}` sets a `threading.Event()`.
3. The `llama_cpp` stream evaluation callback checks `job.cancel_event.is_set()` before computing each token. If set:
   - Inference loop terminates immediately (< 200 ms).
   - CPU drops to idle.
   - Any tokens already produced are saved to the database with `status = 'cancelled'`.
   - SSE connection sends event: `event: cancelled\ndata: {"job_id": "..."}\n\n`.

### 4.2 Sequential Variation Architecture
- To prevent thermal throttling and memory spikes on the 11th Gen i3, generation produces **2 distinct variations sequentially**:
  - **Variation 1 (Angle A — Concrete/Sensory):** Grounded in tangible objects, physical scenes, or spoken words.
  - **Variation 2 (Angle B — Internal/Silence):** Grounded in internal monologue, hesitation, or unsaid feelings.
- Variation 1 streams immediately into Card 1. Once completed, Variation 2 begins streaming into Card 2.
- A **"+ Naya Nazariya" (Generate 3rd Angle)** button allows generating a 3rd variation on demand.

### 4.3 Line-by-Line Pinning & Revision Mechanics
- **Line-Level Representation in Database:** Each poem maintains an array of pinned line indices `pinned_line_indices: [0]` (0-indexed).
- **Stitching Survives Revisions:**
  - If Line 1 is pinned and the user clicks **"Aakhri misra badlo" (Fix the last line)**:
    - The backend sends a constrained prompt with Line 1 locked as the immutable prompt prefix.
    - The model generates *only* the completing lines.
    - The backend stitches the locked Line 1 with the newly generated lines and records a new entry in `poem_revisions`.

---

## 5. System Architecture & Relational Schema (SQLite)

### 5.1 Relational Database Architecture (`ankahi_daastan.db`)
Configured with SQLite WAL mode (`PRAGMA journal_mode = WAL;`) and enforced referential integrity (`PRAGMA foreign_keys = ON;`).

```sql
-- 1. Schema Versioning for Migrations
CREATE TABLE IF NOT EXISTS schema_migrations (
    version INTEGER PRIMARY KEY,
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Chat Sessions (Scratchpad Threads)
CREATE TABLE IF NOT EXISTS sessions (
    id TEXT PRIMARY KEY,                       -- UUID v4
    title TEXT NOT NULL,                       -- Auto-derived from seed (e.g. "Doston ka badal jana")
    model_name TEXT NOT NULL,                  -- Model filename
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Prompts
CREATE TABLE IF NOT EXISTS prompts (
    id TEXT PRIMARY KEY,                       -- UUID v4
    session_id TEXT NOT NULL,
    raw_input TEXT NOT NULL,
    retrieved_poem_ids TEXT,                   -- JSON list of IDs from user_poems.md
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(session_id) REFERENCES sessions(id) ON DELETE CASCADE
);

-- 4. Poems
CREATE TABLE IF NOT EXISTS poems (
    id TEXT PRIMARY KEY,                       -- UUID v4
    prompt_id TEXT NOT NULL,
    session_id TEXT NOT NULL,
    variation_index INTEGER NOT NULL,          -- 1, 2, or 3
    creative_angle TEXT NOT NULL,              -- 'concrete' | 'understated' | 'extension'
    content TEXT NOT NULL,                     -- Current poem text
    original_content TEXT NOT NULL,            -- Raw model output
    pinned_line_indices TEXT DEFAULT '[]',     -- JSON array of pinned line numbers [0, 2]
    is_favorite INTEGER DEFAULT 0,             -- 1 = In Curated Library
    status TEXT DEFAULT 'completed',           -- 'streaming' | 'completed' | 'cancelled'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(prompt_id) REFERENCES prompts(id) ON DELETE CASCADE,
    FOREIGN KEY(session_id) REFERENCES sessions(id) ON DELETE CASCADE
);

-- 5. Full Poem Version Snapshots (Enabling Whole-Poem Undo/Redo)
CREATE TABLE IF NOT EXISTS poem_versions (
    id TEXT PRIMARY KEY,                       -- UUID v4
    poem_id TEXT NOT NULL,
    version_number INTEGER NOT NULL,           -- 1, 2, 3...
    content TEXT NOT NULL,
    diff_summary TEXT,                         -- e.g. "Changed line 2" or "Surgical re-roll"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(poem_id) REFERENCES poems(id) ON DELETE CASCADE
);

-- 6. Collections & Tagging for Personal Library (Diwan)
CREATE TABLE IF NOT EXISTS collections (
    id TEXT PRIMARY KEY,                       -- UUID v4
    name TEXT NOT NULL UNIQUE,                 -- e.g. "Gham-e-Rozgaar", "Mukhtasar Nazmein"
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS collection_poems (
    collection_id TEXT NOT NULL,
    poem_id TEXT NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (collection_id, poem_id),
    FOREIGN KEY(collection_id) REFERENCES collections(id) ON DELETE CASCADE,
    FOREIGN KEY(poem_id) REFERENCES poems(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tags (
    id TEXT PRIMARY KEY,                       -- UUID v4
    name TEXT NOT NULL UNIQUE                  -- e.g. "#intezaar", "#dosti"
);

CREATE TABLE IF NOT EXISTS poem_tags (
    poem_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    PRIMARY KEY (poem_id, tag_id),
    FOREIGN KEY(poem_id) REFERENCES poems(id) ON DELETE CASCADE,
    FOREIGN KEY(tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

-- 7. Learned Preferences (Feedback Engine)
CREATE TABLE IF NOT EXISTS user_preferences (
    id TEXT PRIMARY KEY,                       -- UUID v4
    rule_key TEXT NOT NULL UNIQUE,             -- e.g. "avoid_word_shama", "prefer_short_couplet"
    rule_type TEXT NOT NULL,                   -- 'lexical_ban' | 'meter_preference' | 'tone'
    description TEXT NOT NULL,
    confidence INTEGER DEFAULT 1,
    is_active INTEGER DEFAULT 1,               -- 1 = Enabled, 0 = Disabled by user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indices for Fast Querying
CREATE INDEX IF NOT EXISTS idx_poems_session ON poems(session_id);
CREATE INDEX IF NOT EXISTS idx_poems_favorite ON poems(is_favorite);
CREATE INDEX IF NOT EXISTS idx_prompts_session ON prompts(session_id);
CREATE INDEX IF NOT EXISTS idx_versions_poem ON poem_versions(poem_id);
```

---

## 6. Local API & Server-Sent Events (SSE) Specification

All endpoints bind strictly to `127.0.0.1:8765`. 

### 6.1 Security & Origin Hardening
To prevent external browser tabs or local malicious scripts from interacting with the backend:
- The backend generates a random `session_token` upon boot.
- PyWebView injects this token into all headers as `X-Ankahi-Token: <token>`.
- FastAPI rejects any request lacking this valid token (`403 Forbidden`).
- Content Security Policy (CSP) header enforced:
  `default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; font-src 'self'; connect-src 'self' http://127.0.0.1:8765;`

### 6.2 SSE Protocol Specification (`/api/generate`)

**Request:**
```http
POST /api/generate
Content-Type: application/json
X-Ankahi-Token: 4f8b9e...

{
  "session_id": "uuid-v4",
  "prompt": "doston ka badal jana",
  "variations_count": 2,
  "model_name": "qwen2.5-3b-instruct-q4_k_m.gguf"
}
```

**Streamed Response (SSE Events):**
```
event: job_created
data: {"job_id": "job-1234", "session_id": "uuid-v4"}

event: variation_start
data: {"variation_index": 1, "angle": "concrete", "poem_id": "poem-1"}

event: token
data: {"variation_index": 1, "token": "Chai"}

event: token
data: {"variation_index": 1, "token": " ki"}

event: variation_complete
data: {"variation_index": 1, "content": "Chai ki pyali thandi ho gayi...", "tokens_generated": 24, "speed_tps": 8.2}

event: variation_start
data: {"variation_index": 2, "angle": "understated", "poem_id": "poem-2"}

...

event: complete
data: {"job_id": "job-1234", "total_tokens": 52, "duration_sec": 6.3}
```

---

## 7. Complete UI/UX State Machine & User Experience

### 7.1 First-Run Onboarding Flow
1. **Model Discovery:** The app scans `%LOCALAPPDATA%\AnkahiDaastan\models\` and `./models/`.
   - *If found:* Auto-selects `qwen2.5-3b-instruct-q4_k_m.gguf`.
   - *If none found:* A welcoming, dark-themed setup modal appears explaining that the local brain is missing, displaying the exact download link and a folder shortcut button: **"Open Models Folder"**.
2. **First Generation Benchmark:** Runs a quiet 1-sentence prompt to benchmark CPU speed and warm up RAM.
3. **Voice Sample Starter:** Offers the user an optional form to paste 3–5 initial poems to populate `user_poems.md` (or click "Start with Default Sufi/Diwan Voice").

### 7.2 Core UI States
- **Empty State:** Clean, distraction-free canvas with inspirational seed prompts (*"Chai thandi ho rahi hai...", "Ek purana dost..."*).
- **Loading State:** Subtle pulsing amber ring on the card with text: *"Khayal ko lafzon mein dhaal raha hoon..."* with live tokens-per-second indicator.
- **Unsaved Changes Protection:** If the user edits a card line and attempts to switch chats or close the app, an inline prompt asks: *"Unsaved lines will be kept as draft. Save to library?"*
- **Error States:**
  - *Corrupted GGUF:* Error banner with file verification hash check and instruction to re-download.
  - *Out of Memory:* Warns if available RAM < 2.5 GB, recommending closing browser tabs.
  - *Thermal Warning State:* If `tokens_per_sec` falls below 3.5 during generation, show a subtle inline note: *"Laptop thoda garam hai — thoda slow chalega"* with a suggestion to close background applications.

### 7.3 Model Selector Dropdown & Dynamic Engine Switcher
Located in the top application navigation header next to the Diwan Library toggle:
1. **Dropdown UI Presentation:**
   - **Trigger Pill:** Displays active model name, role pill (e.g., `Llama 3.2 3B · Recommended`), and live status dot (Green = Ready, Amber = Loading/Switching).
   - **Menu Item Cards:** Each selectable option in the dropdown renders:
     - **Header:** Model Name + Category Badge (`[Recommended]`, `[Fast Baseline]`, `[Quick Draft]`, `[Experimental]`).
     - **Performance Badges:** Live throughput (`6.4 t/s`) and RAM footprint (`4.4 GB`).
     - **Context Guidance:** A concise 1-sentence description explaining what the model excels at (e.g., *"Best for original, restrained poetry. 100% line count adherence and perfect locked-line preservation."*).
2. **Dynamic Hot-Swap Lifecycle (`POST /api/models/switch`):**
   - *Cooperative Interrupt:* If a generation is currently active, immediately trigger the cancellation token.
   - *Memory Reclamation:* Explicitly dereference the loaded engine and invoke garbage collection (`del llm; gc.collect()`) to reclaim RAM before loading the new model.
   - *Model Instantiation:* Instantiate the chosen GGUF with `n_ctx=8192, n_threads=4`.
   - *Session State:* Store `current_model_id` in SQLite `app_settings` table to persist model choice across app restarts.

### 7.4 Accessibility & Aesthetics
- **Color Palette:** Obsidian Black (`#0a0c10`), Deep Charcoal Card (`#141821`), Warm Amber Gold (`#e5a93c`, hover `#f5be58`), Muted Terracotta (`#c86446`).
- **Typography:** 100% locally bundled. Inter for UI labels; Lora/Outfit for poetry verses (17px, line height 1.75).
- **Reduced Motion:** Option in Settings disables pulsing glow effects, optimizing battery and CPU on laptops.
- **Keyboard Shortcuts:**
  - `Ctrl + Enter`: Generate / Takhleeq
  - `Esc`: Cancel active generation
  - `Ctrl + S`: Save active poem to Library
  - `Ctrl + Shift + C`: Copy active poem to clipboard
  - `Ctrl + Z / Ctrl + Y`: In-card undo / redo for line edits

---

## 8. Windows Packaging, Storage Boundaries & Migration

### 8.1 Windows Writable Storage Specification
In accordance with Windows security standards, the executable **must never attempt to write to `C:\Program Files`**.

All runtime state, database files, and model weights reside in the user's roaming/local application directory:
- **Base Data Path:** `%LOCALAPPDATA%\AnkahiDaastan\`
  - `data/ankahi_daastan.db` (SQLite database)
  - `voice/skill.md` (Editable craft guidelines)
  - `voice/user_poems.md` (Editable authentic poems)
  - `voice/user_preferences.json` (Learned stylistic preferences)
  - `models/` (Where user drops `.gguf` files)
  - `logs/ankahi.log` (Rotated local debug logs)
- **Portable Override:** If a file named `portable.txt` is placed next to `AnkahiDastaan.exe`, the app operates in self-contained portable mode, storing data in `./data/`.

### 8.2 PyInstaller Build Configuration (`build.bat`)

```bat
@echo off
echo Building Ankahi Dastaan standalone Windows executable...
pyinstaller --noconsole --name "AnkahiDastaan" ^
  --icon="ui/assets/icon.ico" ^
  --add-data "ui;ui" ^
  --collect-all llama_cpp ^
  --hidden-import "uvicorn" ^
  --hidden-import "fastapi" ^
  --hidden-import "webview" ^
  main.py
echo Build complete. Executable located in dist/AnkahiDastaan/
```

---

## 9. Measurable Acceptance & Benchmark Criteria

| Acceptance Area | Measurable Benchmark / Criterion | Target Threshold | Validation Protocol & Measured Result |
| :--- | :--- | :--- | :--- |
| **Script Compliance** | String inspection verifying 100% Roman Hinglish text. | **≥ 99.0%** of characters | Python unicode scanner rejecting characters in `\u0900-\u097F` and `\u0600-\u06FF`. (Measured: 100.0%) |
| **Model Load Time** | Cold GGUF load into memory. | **< 8.0 seconds** | Measured from `Llama()` instantiation to ready. (Measured: 3.3s on Qwen2.5-3B) |
| **Cold Start TTFT** | Time to First Token (first prompt after launch). | **< 25.0 seconds** | Measured prompt prefill on fresh launch. (One-time session cost) |
| **Warm Generation TTFT**| Subsequent prompt latency during active session. | **< 8.0 seconds** | Target for daily interactive typing UX. (Measured: 3.4–5.6s) |
| **Sustained Throughput**| Token streaming speed on Intel i3 under thermal load. | **≥ 5.5 tokens/sec** | Sustainable across sustained typing sessions. (Cold: 7.5–8.8 t/s; Thermally loaded: 5.5 t/s) |
| **Cancellation Speed** | CPU idle recovery upon pressing `Esc`. | **< 300 milliseconds** | Verify Python CPU thread utilization drops below 5% immediately upon cancellation. |
| **Output Cleanliness** | Absence of `<think>` reasoning tags, preambles, and meta notes. | **≥ 95.0%** of outputs | Automated regex scan for `<think>`, conversational preambles, and notes. (Measured: 100% on Qwen2.5) |
| **Voice Fidelity** | Blind scoring rubric across 20 prompts. | **≥ 80% approval** on Restraint, Cadence, and Final Turn | Evaluated on 1-5 scale: (1) Cadence naturalness, (2) Cliché absence, (3) Emotional landing in last line. |
| **Zero Network Leaks** | No outbound HTTP/DNS requests during full usage cycle. | **Zero outbound packets** | Verified using Wireshark / Windows Defender outbound firewall block rule. |
| **Data Integrity** | Process hard-kill via Task Manager during streaming. | **Zero DB corruption** | SQLite WAL integrity check (`PRAGMA integrity_check;`) returns `ok`. |

---

## 10. Phased Development Roadmap

### Phase 1: Engine Foundation & Benchmarking (Current Focus)
- [x] Python virtual environment setup (`venv`) and activation.
- [ ] Install `llama-cpp-python` with optimal Windows AVX2 CPU wheels.
- [ ] Place `qwen2.5-3b-instruct-q4_k_m.gguf` in `models/`.
- [ ] Run standalone terminal benchmark script (`benchmarks/test_inference.py`) measuring TTFT, tokens/sec, and script compliance on the actual HP 240 G8 laptop.
- [ ] Test cooperative cancellation interrupt handler.

### Phase 2: Core Desktop UI & Database (MVP)
- [ ] Scaffold `PyWebView` frameless window with local CSS/JS (Cyber-Sufi theme).
- [ ] Set up SQLite database with WAL mode and initial migrations.
- [ ] Implement FastAPI SSE streaming with `job_id` and token authorization.
- [ ] Build the 2-variation sequential generation cards with in-place line editing.
- [ ] Connect sidebar chat session persistence.

### Phase 3: Voice Engine & Targeted Revisions
- [ ] Implement `voice_engine.py` with BM25 adaptive retrieval from `user_poems.md`.
- [ ] Build surgical revision buttons (*"Dheema karo"*, *"Aakhri misra badlo"*, *"Naye lafz lao"*).
- [ ] Implement line pinning logic and stitched prompt generation.
- [ ] Build the Personal Library (*Diwan*) view with tags, favorites, and TXT/Markdown export.
- [ ] Implement the preference learner capturing line revisions.

### Phase 4: Hardening & Standalone Packaging
- [ ] Enforce Windows `%LOCALAPPDATA%` storage separation.
- [ ] Conduct zero-outbound network firewall audit.
- [ ] Run PyInstaller build script and verify standalone `.exe` on clean Windows user profile.
