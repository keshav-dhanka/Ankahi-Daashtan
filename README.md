# Ankahi Dastaan (अनकही दास्तान)

<p align="center">
  <em>An intimate, offline Roman Hinglish poetry companion tailored for Windows.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows%2010%2F11-0078D6?style=flat-square&logo=windows" alt="Platform" />
  <img src="https://img.shields.io/badge/Engine-llama.cpp%20(GGUF)-orange?style=flat-square" alt="Engine" />
  <img src="https://img.shields.io/badge/Runtime-Python%203.11%20%7C%20AVX2-blue?style=flat-square" alt="Python" />
  <img src="https://img.shields.io/badge/Privacy-100%25%20Offline%20Local--First-green?style=flat-square" alt="Privacy" />
  <img src="https://img.shields.io/badge/UI-PyWebView%20%7C%20Cyber--Sufi-9cf?style=flat-square" alt="UI" />
</p>

---

## 1. What is Ankahi Dastaan?

**Ankahi Dastaan (अनकही दास्तान)** is a distraction-free, local desktop poetry companion. You type a raw emotion, a broken line, or half a thought in Hinglish or English, and the application generates two or three restrained poetic interpretations written in authentic **Roman Hinglish**.

Unlike generic chatbot wrappers, Ankahi Dastaan is built around a distinct, personal poetic voice:
- **Bulle Shah Directness:** Plain words with immense emotional weight.
- **Urdu Emotional Restraint:** Grief and longing are stated simply, like a cup of tea left cold on a table.
- **The Turn (*Misra-e-Sani*):** The final line carries the weight—landing an unforced realization, a quiet twist, or a direct address rather than a moralizing conclusion.
- **Strict Anti-Cliché Engine:** Explicitly prohibits worn-out tropes (*shama-parwana*, *jaam-e-sharab*, *toota hua dil*, *aansuon ka samandar*).
- **100% Air-Gapped & Private:** Powered by quantized GGUF models running directly on your laptop CPU. No API keys, no internet calls, and no data leaving your machine.

---

## 2. Key Architecture & Features

### 3-Tier Personalized Voice Engine
1. **Tier 1 — Baked-In Voice Card (`app/voice/skill.md`):** Master craft guidelines defining emotional restraint, line length (2–4 lines, 5–10 words/line), rhythm over forced rhyme, vocabulary tables, and prompt-anchoring directives.
2. **Tier 2 — Adaptive Few-Shot Retrieval:** Dynamic tag matching against authentic reference poems in `app/voice/user_poems.md`, injecting relevant context without bloating the prompt.
3. **Tier 3 — Deterministic Preference Extractor (`user_preferences.json`):** Learns from manual line edits over time (e.g., lexical replacements, contractions like *nhi*, *h*, *vo*).

### Precision Line-Level Locking
Pin individual lines that you love with a single click. When regenerating, the application keeps locked lines intact character-for-character while re-crafting surrounding verses.

### Multi-Model Hot-Swap Selector
Seamlessly toggle between four calibrated local models directly from the UI dropdown:
- **Llama 3.2 3B Instruct:** *Recommended · Top Creative Voice* (Best originality, 100% line count control, 95% strict pass rate).
- **Qwen 2.5 3B Instruct:** *Fast Baseline · Low RAM* (Balanced 7.0 t/s throughput, 3.7 GB RAM).
- **Gemma 2 2B IT:** *Quick Draft · Lightest* (Fastest response, 3.6 GB RAM).
- **Qwen3 4B Instruct:** *Experimental 4B Reasoner* (Deep reasoning with `/no_think` suppression).

### Hardware-Calibrated Thermal Management
Tuned specifically for entry-level laptops (e.g. Intel Core i3 with 2 performance cores):
- Real-time token streaming with live `tok/s` feedback.
- Thermal throttling detection with graceful user advisories (*"Laptop thoda garam hai — thoda slow chalega"*).
- Instant cooperative cancellation via the `Esc` key (< 300 ms CPU recovery).

---

## 3. Empirical Hardware Benchmarks (HP 240 G8)

All four finalist models were evaluated across the complete **20-Prompt Evaluation Suite** (80 total generations) on an **HP 240 G8** laptop (Intel Core i3-1115G4 @ 3.00GHz, 16 GB RAM, CPU-only, 4 threads, AVX2 enabled) under a strict 60-second thermal normalization cooldown protocol:

| Model | Model File | Model Load | Cold TTFT | Warm TTFT (Avg) | Speed | Peak RAM | Strict Pass Rate | Architectural Role |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Llama-3.2-3B-Instruct** | `Llama-3.2-3B-Instruct-Q4_K_M.gguf` | 3.48s | 200.1s | 15.25s | **6.36 t/s** | 4,455 MB | **95.0%** (19/20) | **Recommended (Top Creative Voice)** |
| **Qwen2.5-3B-Instruct** | `qwen2.5-3b-instruct-q4_k_m.gguf` | 3.83s | 170.9s | 13.65s | **6.95 t/s** | 3,726 MB | **70.0%** (14/20) | **Fast Baseline (High Speed & Low RAM)** |
| **Gemma-2-2B-IT** | `gemma-2-2b-it-Q4_K_M.gguf` | **2.70s** | **140.9s** | **10.85s** | **7.13 t/s** | **3,626 MB** | **60.0%** (12/20) | **Quick Draft (Ultra-Fast Ideation)** |
| **Qwen3-4B** | `Qwen3-4B-Q4_K_M.gguf` | 4.18s | 257.7s | 20.98s | 4.60 t/s | 5,396 MB | 95.0% (19/20) | **Experimental 4B (Heavier RAM & Slower)** |

> *Eliminated Models:* **Mistral-7B** (2.99 t/s, 5.97 GB RAM, looped on locked lines) and **Phi-3.5-mini** (dropped pinned lines, hallucination spirals) were eliminated after failing strict hardware and creative criteria.

---

## 4. Target Architecture & Directory Structure

```text
Ankahi Daastan/
├── ANKAHI_DAASTAN_FINAL_PRD.md     # Master Product Requirements Document (v2.2)
├── README.md                       # Project documentation & overview
├── .gitignore                      # Git ignore specifications
├── main.py                         # Application launcher (PyWebView + FastAPI thread)
├── build.bat                       # PyInstaller standalone build script
│
├── app/                            # Backend Application Package
│   ├── __init__.py
│   ├── config.py                   # Runtime parameters, paths, model metadata
│   ├── main.py                     # FastAPI app, SSE streaming endpoints, model switcher
│   ├── engine.py                   # llama.cpp inference, streaming, cancellation tokens
│   │
│   ├── db/                         # Database Module
│   │   ├── __init__.py
│   │   ├── database.py             # SQLite WAL connection & schema migrations
│   │   └── models.py               # Data models (conversations, poems, pinned lines)
│   │
│   └── voice/                      # 3-Tier Voice Engine
│       ├── skill.md                # Master Baked-In Voice Card (Tier 1)
│       ├── user_poems.md           # Authentic reference poems (Tier 2)
│       ├── retriever.py            # BM25 adaptive example retriever (Tier 2)
│       └── preferences.py          # Deterministic preference engine (Tier 3)
│
├── ui/                             # Desktop Frontend (Local HTML / Vanilla CSS / JS)
│   ├── index.html                  # Frameless desktop layout
│   ├── css/
│   │   ├── main.css                # Obsidian & Terracotta Cyber-Sufi theme
│   │   ├── cards.css               # Dual variation cards, line-editing, lock icons
│   │   └── sidebar.css             # Session history & Diwan library modal
│   ├── js/
│   │   ├── app.js                  # Main UI controller & SSE stream consumer
│   │   ├── model_selector.js       # Dropdown component with live metrics
│   │   ├── editor.js               # In-place line editor & line-locking logic
│   │   └── diwan.js                # Diwan saved poems, tags, and export
│   └── assets/                     # 100% locally bundled fonts & icons
│       ├── fonts/                  # Inter & Lora/Outfit WOFF2 files
│       └── icon.ico
│
├── data/                           # Local database & user files (Gitignored)
│   └── ankahi_daastan.db           # SQLite database in WAL mode
│
├── models/                         # GGUF model weights (Gitignored)
│   ├── Llama-3.2-3B-Instruct-Q4_K_M.gguf   # Recommended primary
│   ├── qwen2.5-3b-instruct-q4_k_m.gguf     # Fast baseline
│   ├── gemma-2-2b-it-Q4_K_M.gguf           # Quick draft
│   └── Qwen3-4B-Q4_K_M.gguf                # Experimental 4B
│
├── benchmarks/                     # Performance & Validation Suite (Completed)
│   ├── prompts.py                  # 20-prompt evaluation suite (5 categories)
│   ├── evaluator.py                # Strict multi-metric evaluation engine
│   ├── test_inference.py           # CLI benchmark runner
│   ├── run_finalists_suite.py      # Master finalists runner
│   └── results/                    # Benchmark JSONs & comparative Markdown reports
│
└── venv/                           # Python 3.11 virtual environment (AVX2)
```

---

## 5. Getting Started

### Prerequisites
- **OS:** Windows 10 or 11 (64-bit)
- **CPU:** x86_64 CPU with AVX2 instruction support
- **RAM:** Minimum 8 GB (16 GB recommended)
- **Python:** Python 3.11 (via `uv` or official installer)

### Setup Virtual Environment
```powershell
# Clone the repository
git clone https://github.com/keshav-dhanka/Ankahi-Daashtan.git
cd Ankahi-Daashtan

# Create a virtual environment with Python 3.11
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\Activate.ps1

# Install requirements with pre-compiled AVX2 wheels
pip install llama-cpp-python psutil pywebview fastapi uvicorn
```

### Acquiring Model Weights
Download the quantized `.gguf` files and place them in the `models/` directory:
- [Llama-3.2-3B-Instruct-Q4_K_M.gguf](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF) *(Recommended Default)*
- [qwen2.5-3b-instruct-q4_k_m.gguf](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF)
- [gemma-2-2b-it-Q4_K_M.gguf](https://huggingface.co/bartowski/gemma-2-2b-it-GGUF)
- [Qwen3-4B-Q4_K_M.gguf](https://huggingface.co/Qwen) *(or compatible Qwen GGUF weights)*

---

## 6. Running Benchmarks

### 1. Single Model Smoke Test (Quick Audit)
```powershell
.\venv\Scripts\python.exe benchmarks/test_inference.py --model models/Llama-3.2-3B-Instruct-Q4_K_M.gguf --stage smoke
```

### 2. Repeatability Benchmark (5 Prompts × 3 Repetitions)
```powershell
.\venv\Scripts\python.exe benchmarks/test_inference.py --model models/qwen2.5-3b-instruct-q4_k_m.gguf --stage repeatability
```

### 3. Master Finalists Suite (All 4 Models × 20 Prompts)
```powershell
.\venv\Scripts\python.exe benchmarks/run_finalists_suite.py
```
*Includes an automated 60-second thermal cooldown between each model run to ensure accurate, non-throttled benchmarks.*

---

## 7. Writing Style Guidelines (At a Glance)

| Criterion | What It Means in Ankahi Dastaan |
| :--- | :--- |
| **Script Rule** | **Roman Hinglish only.** Pure Latin characters (`a-z`). Zero Devanagari (`हिंदी`) and zero Arabic/Nastaliq (`اردو`). |
| **Structure** | Exactly 2 lines (couplet) or 4 lines (quatrain). Concise (5–10 words per line). |
| **Tone** | Conversational intimacy, quiet realization, domestic observation. Never theatrical self-pity. |
| **The Turn** | The last line either makes a demand, reveals an unexpected domestic detail, or states the quiet truth. |
| **Negative Constraints** | Strictly forbidden: *shama-parwana*, *jaam-e-sharab*, *aansuon ka samandar*, *toota hua dil*, *zulfon ki chhaon*. |

---

## 8. Development Roadmap

- [x] **Phase 1: Hardware Benchmarking & Evaluator Calibration (Completed)**
  - [x] Multi-model CPU evaluation suite with AVX2 acceleration.
  - [x] Strict compliance evaluator (exact locked line, cleanliness, Hinglish density).
  - [x] Resolution of Qwen3 reasoning leakage via `/no_think` suppression.
  - [x] Full 20-prompt empirical evaluation across all 4 finalists under thermal cooldown.
  - [x] Master Baked-In Voice Card established in `app/voice/skill.md`.
- [ ] **Phase 2: Core Desktop MVP Scaffolding (Current Priority)**
  - [ ] Local SQLite database (`data/ankahi_daastan.db`) in WAL mode with line-level pinning.
  - [ ] Local FastAPI SSE streaming server with token-level streaming and cooperative cancellation.
  - [ ] Model selector dropdown component with dynamic GGUF hot-swapping.
  - [ ] Frameless `PyWebView` desktop window with Cyber-Sufi dark palette.
  - [ ] Dual/triple variation cards with in-place line editing and line-pinning icons.
  - [ ] Sidebar chat history with session persistence.
- [ ] **Phase 3: Diwan Library & Preference Learning**
  - [ ] Personal Diwan view with tags, favorites, and markdown/text export.
  - [ ] Dynamic Tier 2 BM25 retrieval for voice samples.
  - [ ] Automatic learning from line edits (`user_preferences.json`).
- [ ] **Phase 4: Windows Hardening & Standalone Packaging**
  - [ ] `%LOCALAPPDATA%` storage boundary enforcement.
  - [ ] Zero-network packet audit (100% air-gapped verification).
  - [ ] Standalone Windows executable build script (`build.bat`) via PyInstaller.

---

## 9. Author & Acknowledgments

- **Author & Poet:** Keshav Dhanka
- **Project:** Ankahi Dastaan (अनकही दास्तान)
- **Repository:** [github.com/keshav-dhanka/Ankahi-Daashtan](https://github.com/keshav-dhanka/Ankahi-Daashtan)
- **Inspiration:** The timeless directness of Bulle Shah and contemporary Roman Hindustani poetry.
