"""
Ankahi Dastaan — Benchmarking & Inference Validation Suite
Tests GGUF models on local CPU hardware across the 20-Prompt Evaluation Suite.
Measures:
- Time to First Token (TTFT)
- Sustained Generation Speed (tokens/sec)
- Peak RAM usage during inference (MB)
- Script Compliance (Strict Unicode verification for Roman Hinglish)
- Format, Cleanliness, Exact Line Count, and Negative Constraint Adherence
- Exact Pinned-Line Preservation
- Strict Technical Pass Composite Score
"""

import os
import sys
import time
import json
import argparse
import threading
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

import psutil
from llama_cpp import Llama

# Configure utf-8 standard output for Windows console/subprocesses
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Import benchmark prompts and evaluator
from prompts import PROMPTS
from evaluator import evaluate_output


class RAMMonitor:
    """Samples process memory periodically to capture peak RAM during inference."""
    def __init__(self, interval_sec: float = 0.1):
        self.interval = interval_sec
        self.peak_rss_mb = 0.0
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._process = psutil.Process(os.getpid())

    def start(self):
        self.peak_rss_mb = self._process.memory_info().rss / (1024 * 1024)
        self._running = True
        self._thread = threading.Thread(target=self._monitor, daemon=True)
        self._thread.start()

    def _monitor(self):
        while self._running:
            try:
                rss = self._process.memory_info().rss / (1024 * 1024)
                if rss > self.peak_rss_mb:
                    self.peak_rss_mb = rss
                time.sleep(self.interval)
            except Exception:
                break

    def stop(self) -> float:
        self._running = False
        if self._thread:
            self._thread.join(timeout=0.5)
        try:
            rss = self._process.memory_info().rss / (1024 * 1024)
            if rss > self.peak_rss_mb:
                self.peak_rss_mb = rss
        except Exception:
            pass
        return round(self.peak_rss_mb, 2)


def load_voice_card() -> str:
    """Loads master baked-in voice card from app/voice/skill.md."""
    voice_dir = Path(__file__).resolve().parent.parent / "app" / "voice"
    skill_path = voice_dir / "skill.md"

    if skill_path.exists():
        with open(skill_path, "r", encoding="utf-8") as f:
            system_text = f.read().strip()
    else:
        system_text = (
            "You are Ankahi Dastaan, an intimate Hinglish poetry companion.\n"
            "Write poetry strictly in Roman script — never Devanagari, never Arabic or Nastaliq characters.\n"
            "Writing style: Restrained emotion, couplet or 4-line structure, natural conversational cadence.\n"
            "Avoid forced rhymes, clichés, and moralizing conclusions. The final line lands the emotional truth softly.\n"
            "Output ONLY the poem verses. No titles, commentary, or translation."
        )

    return system_text


def format_prompt(model_path: str, system_prompt: str, user_prompt: str) -> str:
    """Formats prompt according to model-specific chat template."""
    filename = Path(model_path).name.lower()
    
    # Explicit generation instruction anchored right within the generation request (Action Item 3)
    reinforced_user_prompt = (
        "Write in Roman Hinglish only. Do not use English, Devanagari, or Arabic script. "
        "Output ONLY the poem verses without any title, preamble, note, or explanation.\n\n"
        f"{user_prompt}"
    )
    
    if "mistral" in filename:
        return f"<s>[INST] {system_prompt}\n\n{reinforced_user_prompt} [/INST]"
    elif "qwen3" in filename:
        # Qwen3 uses ChatML with /no_think and prefilled closed thinking tags to eliminate reasoning leakage
        return (
            f"<|im_start|>system\n/no_think\n{system_prompt}<|im_end|>\n"
            f"<|im_start|>user\n{reinforced_user_prompt}<|im_end|>\n"
            f"<|im_start|>assistant\n<think>\n\n</think>\n\n"
        )
    elif "qwen" in filename:
        # Qwen2.5 ChatML template
        return (
            f"<|im_start|>system\n{system_prompt}<|im_end|>\n"
            f"<|im_start|>user\n{reinforced_user_prompt}<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )
    elif "llama" in filename:
        return (
            f"<|start_header_id|>system<|end_header_id|>\n\n{system_prompt}<|eot_id|>"
            f"<|start_header_id|>user<|end_header_id|>\n\n{reinforced_user_prompt}<|eot_id|>"
            f"<|start_header_id|>assistant<|end_header_id|>\n\n"
        )
    elif "phi" in filename:
        return (
            f"<|system|>\n{system_prompt}<|end|>\n"
            f"<|user|>\n{reinforced_user_prompt}<|end|>\n"
            f"<|assistant|>\n"
        )
    elif "gemma" in filename:
        return (
            f"<start_of_turn>user\n{system_prompt}\n\n{reinforced_user_prompt}<end_of_turn>\n"
            f"<start_of_turn>model\n"
        )
    else:
        return f"### System:\n{system_prompt}\n\n### User:\n{reinforced_user_prompt}\n\n### Assistant:\n"


def get_stopping_strings(model_path: str) -> List[str]:
    """Returns model-appropriate stopping strings."""
    filename = Path(model_path).name.lower()
    stops = ["---", "###"]
    if "mistral" in filename:
        stops.extend(["</s>", "[INST]"])
    elif "qwen" in filename:
        stops.extend(["<|im_end|>", "<|endoftext|>"])
    elif "llama" in filename:
        stops.extend(["<|eot_id|>", "<|end_of_text|>"])
    elif "phi" in filename:
        stops.extend(["<|end|>", "<|endoftext|>"])
    elif "gemma" in filename:
        stops.extend(["<end_of_turn>", "<eos>"])
    return stops


def run_single_inference(
    llm: Llama,
    formatted_prompt: str,
    stop_strings: List[str],
    temperature: float = 0.74,
    top_p: float = 0.90,
    repeat_penalty: float = 1.18,
    max_tokens: int = 150
) -> Dict[str, Any]:
    """
    Executes a single generation with real-time token streaming to measure:
    - cold start / warm TTFT
    - tokens per second
    - peak RAM
    """
    ram_monitor = RAMMonitor(interval_sec=0.1)
    ram_monitor.start()
    
    t_start = time.perf_counter()
    t_first_token: Optional[float] = None
    generated_tokens: List[str] = []
    
    stream = llm(
        formatted_prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        repeat_penalty=repeat_penalty,
        stop=stop_strings,
        stream=True
    )
    
    for chunk in stream:
        token_text = chunk["choices"][0]["text"]
        if t_first_token is None and token_text.strip():
            t_first_token = time.perf_counter()
        generated_tokens.append(token_text)
        
    t_end = time.perf_counter()
    peak_ram = ram_monitor.stop()
    
    total_duration = t_end - t_start
    full_output = "".join(generated_tokens).strip()
    token_count = len(generated_tokens)
    
    if t_first_token is not None:
        ttft = t_first_token - t_start
        gen_time = t_end - t_first_token
        tok_per_sec = (token_count - 1) / gen_time if gen_time > 0 and token_count > 1 else 0.0
    else:
        ttft = total_duration
        tok_per_sec = 0.0
        
    return {
        "output_text": full_output,
        "token_count": token_count,
        "ttft_sec": round(ttft, 3),
        "total_duration_sec": round(total_duration, 3),
        "tokens_per_sec": round(tok_per_sec, 2),
        "peak_ram_mb": peak_ram
    }


def run_benchmark(
    model_path: str,
    stage: str = "smoke",
    prompt_ids: Optional[List[str]] = None,
    threads: int = 4,
    n_ctx: int = 8192,
    temperature: float = 0.74,
    max_tokens: int = 150,
    repeat_count: int = 1,
    cooldown_sec: int = 0
):
    print("=" * 80)
    print("ANKAHI DASTAAN — HARDWARE INFERENCE & STRICT COMPLIANCE BENCHMARK")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Model: {model_path}")
    print(f"Threads: {threads} | Context: {n_ctx} | Stage: {stage.upper()}")
    print("=" * 80)

    if cooldown_sec > 0:
        print(f"\n[Thermal Management] Cooling down CPU for {cooldown_sec} seconds before benchmark starts...")
        for remaining in range(cooldown_sec, 0, -10):
            print(f"  Cooling down... {remaining}s remaining")
            time.sleep(min(10, remaining))
        print("  CPU cooldown complete. System is thermally stable.")

    # 1. Select prompts
    if prompt_ids:
        target_prompts = [p for p in PROMPTS if p["id"] in prompt_ids]
    elif stage == "smoke":
        # Technical smoke test: Prompts 11 (script/words), 16 (strict couplet), 19 (pinned line)
        target_prompts = [p for p in PROMPTS if p["id"] in ["11", "16", "19"]]
    elif stage == "repeatability":
        # 5 representative prompts across all 5 categories
        target_prompts = [p for p in PROMPTS if p["id"] in ["01", "05", "11", "14", "19"]]
        repeat_count = 3
    else:
        # Full 20 prompts
        target_prompts = PROMPTS

    print(f"Loaded {len(target_prompts)} prompt(s). Executions per prompt: {repeat_count}")
    
    # 2. Load model
    print(f"\n[1/3] Loading GGUF model into memory...")
    t_load_start = time.perf_counter()
    llm = Llama(
        model_path=model_path,
        n_ctx=n_ctx,
        n_threads=threads,
        n_gpu_layers=0,  # CPU only
        verbose=False
    )
    t_load_end = time.perf_counter()
    model_load_time = round(t_load_end - t_load_start, 2)
    print(f"Model loaded successfully in {model_load_time}s.")

    system_prompt = load_voice_card()
    stop_strings = get_stopping_strings(model_path)
    model_name = Path(model_path).stem

    results = []
    
    print("\n[2/3] Executing Benchmark Runs...")
    print("-" * 85)
    print(f"{'ID':<4} | {'Prompt Name':<26} | {'TTFT':<6} | {'Speed':<8} | {'Lines':<5} | {'Hinglish%':<9} | {'Locked':<8} | {'Strict Verdict'}")
    print("-" * 85)

    for p_idx, prompt_meta in enumerate(target_prompts, 1):
        formatted = format_prompt(model_path, system_prompt, prompt_meta["prompt"])
        
        runs_data = []
        for r in range(repeat_count):
            run_metrics = run_single_inference(
                llm=llm,
                formatted_prompt=formatted,
                stop_strings=stop_strings,
                temperature=temperature,
                max_tokens=max_tokens
            )
            eval_metrics = evaluate_output(run_metrics["output_text"], prompt_meta)
            
            run_record = {
                "run_index": r + 1,
                "metrics": run_metrics,
                "evaluation": eval_metrics
            }
            runs_data.append(run_record)
            
            # Print live row for the run
            if r == 0 or repeat_count > 1:
                run_tag = f" r{r+1}" if repeat_count > 1 else ""
                lines_display = f"{eval_metrics['line_count']}/{eval_metrics['expected_lines']}"
                locked_display = "EXACT" if eval_metrics['pinned_line_status'] == "exact_match" else (
                    "FAIL" if eval_metrics['pinned_line_status'] != "not_applicable" else "N/A"
                )
                if eval_metrics["strict_pass"]:
                    verdict_display = "STRICT PASS"
                else:
                    verdict_display = f"FAIL: {', '.join(eval_metrics['failure_reasons'][:2])}"

                print(
                    f"{prompt_meta['id'] + run_tag:<4} | "
                    f"{prompt_meta['name'][:26]:<26} | "
                    f"{run_metrics['ttft_sec']:>4.1f}s | "
                    f"{run_metrics['tokens_per_sec']:>5.2f} t/s | "
                    f"{lines_display:<5} | "
                    f"{eval_metrics['hinglish_density_pct']:>7.1f}% | "
                    f"{locked_display:<8} | "
                    f"{verdict_display}"
                )

        results.append({
            "prompt_meta": prompt_meta,
            "runs": runs_data
        })

    # 3. Calculate Summary Statistics across all executions
    all_runs = [run for item in results for run in item["runs"]]
    
    all_ttft = [r["metrics"]["ttft_sec"] for r in all_runs]
    all_tps = [r["metrics"]["tokens_per_sec"] for r in all_runs if r["metrics"]["tokens_per_sec"] > 0]
    all_ram = [r["metrics"]["peak_ram_mb"] for r in all_runs]
    
    total_evals = len(all_runs)
    script_passes = sum(1 for r in all_runs if r["evaluation"]["script_compliant"])
    clean_passes = sum(1 for r in all_runs if len(r["evaluation"]["artifacts_found"]) == 0)
    line_passes = sum(1 for r in all_runs if r["evaluation"]["line_count_match"])
    hinglish_passes = sum(1 for r in all_runs if not r["evaluation"]["is_pure_english"])
    strict_passes = sum(1 for r in all_runs if r["evaluation"]["strict_pass"])

    # Locked line evaluation (only on prompts where pinned_line is set)
    locked_runs = [r for r in all_runs if r["evaluation"]["pinned_line_status"] != "not_applicable"]
    locked_passes = sum(1 for r in locked_runs if r["evaluation"]["pinned_line_status"] == "exact_match")
    locked_pct = round((locked_passes / len(locked_runs)) * 100, 1) if locked_runs else 100.0

    avg_ttft = round(sum(all_ttft) / len(all_ttft), 2) if all_ttft else 0.0
    avg_tps = round(sum(all_tps) / len(all_tps), 2) if all_tps else 0.0
    peak_ram = max(all_ram) if all_ram else 0.0
    
    script_pct = round((script_passes / total_evals) * 100, 1)
    clean_pct = round((clean_passes / total_evals) * 100, 1)
    line_pct = round((line_passes / total_evals) * 100, 1)
    hinglish_pct = round((hinglish_passes / total_evals) * 100, 1)
    strict_pct = round((strict_passes / total_evals) * 100, 1)

    print("-" * 85)
    print("\n[3/3] BENCHMARK SUMMARY & STRICT AUDIT:")
    print(f"  * Model Load Time:             {model_load_time}s")
    print(f"  * Avg Time-to-First-Token:     {avg_ttft}s (Cold TTFT: {all_ttft[0]}s)")
    print(f"  * Avg Sustained Speed:         {avg_tps} tokens/sec")
    print(f"  * Peak RAM Usage:              {peak_ram:.1f} MB")
    print("  --------------------------------------------------")
    print(f"  * Latin Script Compliance:     {script_pct}% ({script_passes}/{total_evals})")
    print(f"  * Output Cleanliness (no meta): {clean_pct}% ({clean_passes}/{total_evals})")
    print(f"  * Exact Line Count Adherence:  {line_pct}% ({line_passes}/{total_evals})")
    print(f"  * Roman Hinglish Fidelity:     {hinglish_pct}% ({hinglish_passes}/{total_evals} not pure English)")
    print(f"  * Locked-Line Integrity:       {locked_pct}% ({locked_passes}/{len(locked_runs)} exact matches)")
    print(f"  [RESULT] OVERALL STRICT PASS RATE: {strict_pct}% ({strict_passes}/{total_evals} satisfied all constraints)")
    print("=" * 85)

    # 4. Save Artifacts (JSON & Markdown Report)
    output_dir = Path(__file__).resolve().parent / "results"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = output_dir / f"{model_name}_{stage}_{timestamp}.json"
    md_path = output_dir / f"{model_name}_{stage}_{timestamp}_report.md"

    summary_data = {
        "model_name": model_name,
        "model_path": str(model_path),
        "stage": stage,
        "timestamp": timestamp,
        "threads": threads,
        "context_window": n_ctx,
        "model_load_time_sec": model_load_time,
        "avg_ttft_sec": avg_ttft,
        "cold_ttft_sec": all_ttft[0],
        "avg_tokens_per_sec": avg_tps,
        "peak_ram_mb": peak_ram,
        "script_compliance_pct": script_pct,
        "cleanliness_pct": clean_pct,
        "line_count_adherence_pct": line_pct,
        "hinglish_fidelity_pct": hinglish_pct,
        "locked_line_integrity_pct": locked_pct,
        "strict_pass_pct": strict_pct,
        "total_prompts_tested": len(target_prompts),
        "total_executions": total_evals,
        "detailed_results": results
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2, ensure_ascii=False)

    generate_markdown_report(md_path, summary_data)
    print(f"\nArtifacts generated:")
    print(f"  - Detailed JSON Data: {json_path}")
    print(f"  - Review Markdown Report: {md_path}")
    
    # Explicitly release GGUF memory before next run
    try:
        del llm
        import gc
        gc.collect()
    except Exception:
        pass

    return summary_data


def generate_markdown_report(report_path: Path, data: Dict[str, Any]):
    """Creates a comprehensive markdown report with performance, compliance audit, and human scoring rubric."""
    lines = [
        f"# Benchmark Evaluation Report: {data['model_name']}",
        f"",
        f"- **Stage:** `{data['stage'].upper()}`",
        f"- **Date & Time:** {data['timestamp']}",
        f"- **Model Path:** `{data['model_path']}`",
        f"- **Configuration:** {data['threads']} CPU threads | Context: {data['context_window']} tokens | Temp: 0.74",
        f"",
        f"## 1. Hardware Performance Summary",
        f"",
        f"| Metric | Target (PRD) | Measured Result | Status |",
        f"| :--- | :--- | :--- | :--- |",
        f"| **Model Load Time** | < 8.0s | **{data['model_load_time_sec']}s** | {'PASS' if data['model_load_time_sec'] < 8.0 else 'CHECK'} |",
        f"| **Time-to-First-Token (TTFT)** | < 4.0s | **{data['avg_ttft_sec']}s** (Cold: {data['cold_ttft_sec']}s) | {'PASS' if data['avg_ttft_sec'] < 4.0 else 'CHECK'} |",
        f"| **Generation Speed** | ≥ 6.5 t/s | **{data['avg_tokens_per_sec']} t/s** | {'PASS' if data['avg_tokens_per_sec'] >= 6.5 else 'AMEND PRD'} |",
        f"| **Peak RAM** | < 6000 MB | **{data['peak_ram_mb']:.1f} MB** | {'PASS' if data['peak_ram_mb'] < 6000 else 'CHECK'} |",
        f"",
        f"## 2. Strict Compliance & Language Quality Audit",
        f"",
        f"| Audit Check | What it Verifies | Measured Result | Strict Status |",
        f"| :--- | :--- | :--- | :--- |",
        f"| **Script Compliance** | Latin/Roman script only; zero Devanagari/Arabic characters | **{data['script_compliance_pct']}%** | {'PASS' if data['script_compliance_pct'] >= 99.0 else 'FAIL'} |",
        f"| **Output Cleanliness** | Zero `<think>` reasoning tags, preambles, notes, explanations | **{data['cleanliness_pct']}%** | {'PASS' if data['cleanliness_pct'] >= 99.0 else 'FAIL'} |",
        f"| **Exact Line Count** | Matches requested lines exactly (2 for couplets, 4 for quatrains) | **{data['line_count_adherence_pct']}%** | {'PASS' if data['line_count_adherence_pct'] >= 90.0 else 'FAIL'} |",
        f"| **Hinglish Language Quality** | Authentic Roman Hindustani/Urdu vocabulary; not pure English | **{data['hinglish_fidelity_pct']}%** | {'PASS' if data['hinglish_fidelity_pct'] >= 90.0 else 'FAIL'} |",
        f"| **Locked-Line Preservation** | Character-for-character exact match; punctuation preserved; no repetition | **{data['locked_line_integrity_pct']}%** | {'PASS' if data['locked_line_integrity_pct'] >= 99.0 else 'FAIL'} |",
        f"| ⭐ **Overall Strict Pass Rate** | Satisfied ALL technical, structural, and negative constraints simultaneously | **{data['strict_pass_pct']}%** | {'PASS' if data['strict_pass_pct'] >= 80.0 else 'NEEDS TUNING'} |",
        f"",
        f"---",
        f"",
        f"## 3. Qualitative Output & Poetic Voice Review",
        f"*(Human evaluation rubric: score 1–5 for cadence, restraint, originality, and final turn)*",
        f""
    ]

    for item in data["detailed_results"]:
        p = item["prompt_meta"]
        for r in item["runs"]:
            m = r["metrics"]
            ev = r["evaluation"]
            run_lbl = f" (Run {r['run_index']})" if len(item["runs"]) > 1 else ""
            
            lines.append(f"### Prompt {p['id']}: {p['name']}{run_lbl} — {p['category']}")
            lines.append(f"**Target:** `{p['target']}`")
            lines.append(f"")
            lines.append(f"> **Prompt Text:** {p['prompt']}")
            lines.append(f"")
            lines.append(f"**Raw Generated Output:**")
            lines.append(f"```text")
            lines.append(m['output_text'])
            lines.append(f"```")
            lines.append(f"")
            
            # Diagnostic Audit Details
            verdict_str = "✅ **STRICT PASS**" if ev['strict_pass'] else f"❌ **FAILED CONSTRAINTS:** {', '.join(ev['failure_reasons'])}"
            lines.append(f"- **Technical Verdict:** {verdict_str}")
            lines.append(f"- **Performance:** TTFT: {m['ttft_sec']}s | Speed: {m['tokens_per_sec']} t/s | RAM: {m['peak_ram_mb']} MB")
            lines.append(f"- **Structure:** Lines: {ev['line_count']}/{ev['expected_lines']} ({'MATCH' if ev['line_count_match'] else 'MISMATCH'})")
            lines.append(f"- **Language Mode:** {ev['language_mode']} (Hinglish Density: {ev['hinglish_density_pct']}%)")
            
            if ev['pinned_line_status'] != "not_applicable":
                lines.append(f"- **Locked-Line Status:** `{ev['pinned_line_status']}` (Preserved: {ev['pinned_line_preserved']})")
            if ev['required_words']:
                missing_str = ", ".join(ev['missing_required_words']) if ev['missing_required_words'] else "None (all present)"
                lines.append(f"- **Required Words Check:** {missing_str}")
            if ev['forbidden_violations']:
                lines.append(f"- ⚠️ **Forbidden Violations Detected:** {', '.join(ev['forbidden_violations'])}")
            if ev['artifacts_found']:
                lines.append(f"- ⚠️ **Output Artifacts Detected:** {', '.join(ev['artifacts_found'])}")
                
            lines.append(f"")
            lines.append(f"| Criterion | Score (1-5) | Qualitative Notes |")
            lines.append(f"| :--- | :---: | :--- |")
            lines.append(f"| **Natural Cadence** | [ ] | Natural conversational rhythm, avoids childish forced rhymes |")
            lines.append(f"| **Emotional Restraint** | [ ] | Understated, quiet realization, avoids melodrama |")
            lines.append(f"| **Originality & Anti-Cliché** | [ ] | Concrete domestic details, avoids stock poetic tropes |")
            lines.append(f"| **Final Turn Impact** | [ ] | Soft emotional landing or shift in final line |")
            lines.append(f"| **Instruction Adherence** | [ ] | Followed all scenario nuances and constraints |")
            lines.append(f"")
            lines.append(f"---")
            lines.append(f"")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ankahi Dastaan Inference Benchmark Suite")
    parser.add_argument("--model", type=str, default="models/qwen2.5-3b-instruct-q4_k_m.gguf", help="Path to GGUF model")
    parser.add_argument("--stage", type=str, choices=["smoke", "full", "repeatability"], default="smoke", help="Benchmark stage")
    parser.add_argument("--prompts", type=str, default=None, help="Comma-separated prompt IDs (e.g. 11,16,19)")
    parser.add_argument("--threads", type=int, default=4, help="CPU threads")
    parser.add_argument("--n_ctx", type=int, default=8192, help="Context length")
    parser.add_argument("--temp", type=float, default=0.74, help="Sampling temperature")
    parser.add_argument("--max_tokens", type=int, default=150, help="Max tokens per generation")
    parser.add_argument("--cooldown", type=int, default=0, help="Pre-benchmark thermal cooldown period in seconds (e.g. 60)")

    args = parser.parse_args()
    
    p_ids = [pid.strip() for pid in args.prompts.split(",")] if args.prompts else None
    
    run_benchmark(
        model_path=args.model,
        stage=args.stage,
        prompt_ids=p_ids,
        threads=args.threads,
        n_ctx=args.n_ctx,
        temperature=args.temp,
        max_tokens=args.max_tokens,
        cooldown_sec=args.cooldown
    )
