"""
Ankahi Dastaan — Finalists 20-Prompt Benchmark Suite Runner
Evaluates all 4 finalist GGUF models across the complete 20-prompt evaluation suite:
1. Qwen2.5-3B-Instruct (Primary Baseline)
2. Gemma-2-2B-IT (Fast Draft Candidate)
3. Llama-3.2-3B-Instruct (Main Challenger)
4. Qwen3-4B (Experimental 4B)

Enforces a 60-second cooldown period before each model run to ensure thermal stability.
Aggregates performance and compliance into a unified comparative report.
"""

import os
import sys
import time
import json
from datetime import datetime
from pathlib import Path

# Add benchmarks directory to sys.path
BENCHMARK_DIR = Path(__file__).resolve().parent
if str(BENCHMARK_DIR) not in sys.path:
    sys.path.insert(0, str(BENCHMARK_DIR))

from test_inference import run_benchmark

FINALISTS = [
    {
        "name": "Qwen2.5-3B-Instruct",
        "path": "models/qwen2.5-3b-instruct-q4_k_m.gguf",
        "role": "Confirmed Primary Baseline"
    },
    {
        "name": "Gemma-2-2B-IT",
        "path": "models/gemma-2-2b-it-Q4_K_M.gguf",
        "role": "Fast Draft Candidate"
    },
    {
        "name": "Llama-3.2-3B-Instruct",
        "path": "models/Llama-3.2-3B-Instruct-Q4_K_M.gguf",
        "role": "Secondary Challenger"
    },
    {
        "name": "Qwen3-4B",
        "path": "models/Qwen3-4B-Q4_K_M.gguf",
        "role": "Experimental 4B Reasoner"
    }
]


def run_finalists_suite():
    print("=" * 90)
    print("ANKAHI DASTAAN — FULL 20-PROMPT BENCHMARK SUITE ON THE 4 FINALISTS")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Models to evaluate (with 60-second thermal cooldown between each):")
    for idx, f in enumerate(FINALISTS, 1):
        print(f"  {idx}. {f['name']} ({f['role']}) -> {f['path']}")
    print("=" * 90)

    results_by_model = []

    for idx, model_info in enumerate(FINALISTS, 1):
        print(f"\n" + "#" * 90)
        print(f"### [MODEL {idx}/4] EVALUATING: {model_info['name']} ({model_info['role']})")
        print("#" * 90)

        # Enforce 60-second cooldown before starting each model
        summary = run_benchmark(
            model_path=model_info["path"],
            stage="full",
            prompt_ids=None,
            threads=4,
            n_ctx=8192,
            temperature=0.74,
            max_tokens=150,
            repeat_count=1,
            cooldown_sec=60
        )
        
        results_by_model.append({
            "model_info": model_info,
            "summary": summary
        })

    # Save Unified Comparative Report
    generate_unified_report(results_by_model)


def generate_unified_report(results: list):
    output_dir = BENCHMARK_DIR / "results"
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = output_dir / f"FINALISTS_20_PROMPTS_COMPARATIVE_REPORT_{timestamp}.md"
    json_path = output_dir / f"finalists_20_prompts_summary_{timestamp}.json"

    # Save raw aggregated JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    lines = [
        "# Ankahi Dastaan — Finalists 20-Prompt Comparative Evaluation Report",
        "",
        f"- **Date & Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "- **Hardware:** HP 240 G8 (Intel Core i3-1115G4 @ 3.00GHz, 16 GB RAM, CPU-only)",
        "- **Context Window:** 8192 tokens | CPU Threads: 4",
        "- **Protocol:** 60-second thermal normalization cooldown preceding each model run",
        "- **Master Voice Card:** Tier 1 Baked-In Voice Card (`app/voice/skill.md`) loaded",
        "",
        "---",
        "",
        "## 1. Hardware Performance Summary (Full 20 Prompts)",
        "",
        "| Model | Role | Load Time | Cold TTFT | Warm TTFT (Avg) | Speed (tok/s) | Peak RAM | PRD Status |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |"
    ]

    for item in results:
        info = item["model_info"]
        s = item["summary"]
        status = "PASS" if s["avg_tokens_per_sec"] >= 5.5 and s["peak_ram_mb"] < 6000 else "CHECK"
        lines.append(
            f"| **{info['name']}** | {info['role']} | **{s['model_load_time_sec']}s** | "
            f"{s['cold_ttft_sec']}s | **{s['avg_ttft_sec']}s** | **{s['avg_tokens_per_sec']} t/s** | "
            f"**{s['peak_ram_mb']:.1f} MB** | **{status}** |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 2. Strict Multi-Metric Compliance & Language Quality Audit",
        "",
        "| Model | Script Compliance | Output Cleanliness | Line Count Adherence | Roman Hinglish Fidelity | Locked Line Integrity | ⭐ Overall Strict Pass |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |"
    ])

    for item in results:
        info = item["model_info"]
        s = item["summary"]
        lines.append(
            f"| **{info['name']}** | {s['script_compliance_pct']}% | "
            f"{s['cleanliness_pct']}% | {s['line_count_adherence_pct']}% | "
            f"{s['hinglish_fidelity_pct']}% | {s['locked_line_integrity_pct']}% | "
            f"**{s['strict_pass_pct']}%** ({int(round(s['strict_pass_pct'] * s['total_prompts_tested'] / 100))}/{s['total_prompts_tested']}) |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 3. Side-by-Side Qualitative Verse Comparison across Key Prompts",
        ""
    ])

    # Sample key prompts for side-by-side comparison: 01 (Friendship), 05 (Chai), 11 (Script), 16 (Couplet), 19 (Pinned)
    key_prompt_ids = ["01", "05", "11", "16", "19"]
    
    first_summary = results[0]["summary"]["detailed_results"]
    for prompt_id in key_prompt_ids:
        # Find prompt meta
        p_item = next((item for item in first_summary if item["prompt_meta"]["id"] == prompt_id), None)
        if not p_item:
            continue
        p = p_item["prompt_meta"]
        lines.append(f"### Prompt {p['id']}: {p['name']} ({p['category']})")
        lines.append(f"**Target:** `{p['target']}`")
        lines.append(f"> **Prompt Text:** {p['prompt']}")
        lines.append("")

        for item in results:
            m_name = item["model_info"]["name"]
            res = next((r for r in item["summary"]["detailed_results"] if r["prompt_meta"]["id"] == prompt_id), None)
            if res:
                run0 = res["runs"][0]
                text = run0["metrics"]["output_text"]
                ev = run0["evaluation"]
                v_badge = "✅ STRICT PASS" if ev["strict_pass"] else f"❌ FAIL ({', '.join(ev['failure_reasons'][:2])})"
                lines.append(f"#### **{m_name}** — {v_badge} (Speed: {run0['metrics']['tokens_per_sec']} t/s | Hinglish: {ev['hinglish_density_pct']}%)")
                lines.append("```text")
                lines.append(text)
                lines.append("```")
                lines.append("")

        lines.append("---")
        lines.append("")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("\n" + "=" * 90)
    print("UNIFIED FINALISTS COMPARATIVE REPORT SAVED:")
    print(f"  Markdown: {report_path}")
    print(f"  JSON:     {json_path}")
    print("=" * 90)


if __name__ == "__main__":
    run_finalists_suite()
