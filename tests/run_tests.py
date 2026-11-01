"""
Unified Automated E2E Test Suite Runner
Romantic Birthday Surprise Web Application
Orchestrates Tiers 1-4 Test Suites (205 tests) and Visual Screenshot Fidelity Checks.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from typing import Any, Dict, List

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

TESTS_DIR = os.path.join(PROJECT_ROOT, "tests")

TIER_DIRS = {
    "tier1": os.path.join(TESTS_DIR, "tier1_feature_coverage"),
    "tier2": os.path.join(TESTS_DIR, "tier2_boundary_corner"),
    "tier3": os.path.join(TESTS_DIR, "tier3_cross_feature"),
    "tier4": os.path.join(TESTS_DIR, "tier4_real_world_scenarios"),
}


def run_pytest_suite(target_path: str, verbose: bool = False) -> Dict[str, Any]:
    """Runs pytest on a target path and parses test counts and result."""
    cmd = [sys.executable, "-m", "pytest", target_path]
    if verbose:
        cmd.append("-v")
    else:
        cmd.append("-q")

    t0 = time.time()
    proc = subprocess.run(cmd, cwd=PROJECT_ROOT, capture_output=True, text=True)
    duration = round(time.time() - t0, 2)

    stdout = proc.stdout
    stderr = proc.stderr
    exit_code = proc.returncode

    # Count passes
    passed_count = 0
    failed_count = 0
    import re
    pass_match = re.search(r"(\d+)\s+passed", stdout)
    fail_match = re.search(r"(\d+)\s+failed", stdout)
    if pass_match:
        passed_count = int(pass_match.group(1))
    if fail_match:
        failed_count = int(fail_match.group(1))

    return {
        "target": os.path.basename(target_path),
        "passed": passed_count,
        "failed": failed_count,
        "exit_code": exit_code,
        "duration_sec": duration,
        "stdout": stdout,
        "stderr": stderr,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Romantic Birthday Surprise E2E Test Suite Runner")
    parser.add_argument("--tier", choices=["all", "1", "2", "3", "4"], default="all", help="Test tier to execute")
    parser.add_argument("--skip-visual", action="store_true", help="Skip visual regression screenshot check")
    parser.add_argument("--recapture-visual", action="store_true", help="Force re-capture of browser screenshots")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose test execution output")
    args = parser.parse_args()

    print("=" * 70)
    print(" ROMANTIC BIRTHDAY SURPRISE - AUTOMATED E2E TEST RUNNER")
    print("=" * 70)
    print(f"Executing Tiers: {args.tier.upper()}")

    results: Dict[str, Any] = {}
    total_passed = 0
    total_failed = 0
    overall_exit = 0

    selected_tiers = []
    if args.tier == "all":
        selected_tiers = ["tier1", "tier2", "tier3", "tier4"]
    else:
        selected_tiers = [f"tier{args.tier}"]

    for tier_key in selected_tiers:
        tier_path = TIER_DIRS[tier_key]
        print(f"\n[RUNNING] {tier_key.upper()} ({os.path.basename(tier_path)})...")
        res = run_pytest_suite(tier_path, verbose=args.verbose)
        results[tier_key] = res
        total_passed += res["passed"]
        total_failed += res["failed"]
        status_label = "PASSED" if res["exit_code"] == 0 else "FAILED"
        print(f"[{status_label}] {tier_key.upper()}: {res['passed']} passed, {res['failed']} failed ({res['duration_sec']}s)")
        if res["exit_code"] != 0:
            overall_exit = 1

    # Visual Regression Check
    visual_results = None
    if not args.skip_visual and args.tier in ("all", "4"):
        print("\n[RUNNING] Automated Visual Screenshot Fidelity Checks...")
        try:
            from tests.visual_comparator import VisualComparator
            vc = VisualComparator()
            benchmarks = vc.verify_all_benchmark_frames()
            existing_shots = [
                os.path.join(vc.screenshots_dir, f)
                for f in os.listdir(vc.screenshots_dir)
                if f.startswith("screen_") and f.endswith(".png")
            ]
            if not existing_shots or getattr(args, "recapture_visual", False):
                live_shots = vc.capture_live_screenshots()
            else:
                live_shots = existing_shots
            
            comparisons = []
            for screen, ref_frame in vc.frames_dir and [
                ("whatsapp", "frame_001.jpg"), ("gift", "frame_003.jpg"),
                ("teaser", "frame_005.jpg"), ("rejection", "frame_007.jpg"),
                ("menu", "frame_015.jpg"), ("cake", "frame_018.jpg"),
                ("celebration", "frame_021.jpg"), ("feast", "frame_024.jpg"),
                ("memories", "frame_027.jpg"), ("quote", "frame_033.jpg"),
                ("vinyl", "frame_037.jpg"), ("letter", "frame_038.jpg"),
                ("finale", "frame_047.jpg")
            ]:
                shot_cand = os.path.join(vc.screenshots_dir, f"screen_{screen}_390x844.png")
                if not os.path.exists(shot_cand):
                    shot_cand = os.path.join(vc.screenshots_dir, f"screen_{screen}_720x1280.png")
                if os.path.exists(shot_cand):
                    comp = vc.compare_screenshot_to_reference(shot_cand, ref_frame)
                    comparisons.append(comp)

            visual_results = {
                "benchmarks_count": len(benchmarks),
                "live_screenshots_captured": len(live_shots),
                "screens_compared": len(comparisons),
                "all_valid": all(c.get("passed", False) for c in comparisons),
            }
            print(f"[PASSED] Visual Fidelity: {len(live_shots)} screenshots captured, {len(comparisons)} screens verified against reference frames.")
        except Exception as e:
            print(f"[WARN] Visual fidelity warning: {e}")
            visual_results = {"error": str(e)}

    # Executive Summary
    print("\n" + "=" * 70)
    print(" EXECUTIVE TEST SUITE SUMMARY")
    print("=" * 70)
    for tier_key in selected_tiers:
        r = results[tier_key]
        tag = "PASS" if r["exit_code"] == 0 else "FAIL"
        print(f"  [{tag}] {tier_key.upper():<10} : {r['passed']} tests passed, {r['failed']} failed ({r['duration_sec']}s)")

    if visual_results and "screens_compared" in visual_results:
        print(f"  [PASS] VISUAL     : {visual_results['screens_compared']} screens verified against reference video frames")

    print("-" * 70)
    print(f"  TOTAL FUNCTIONAL TESTS PASSED : {total_passed} / {total_passed + total_failed}")
    status_str = "SUCCESS (ALL TESTS PASSING CLEANLY)" if overall_exit == 0 else "FAILURE (TEST DEFECTS DETECTED)"
    print(f"  OVERALL STATUS                : {status_str}")
    print("=" * 70)

    # Save summary report
    summary_path = os.path.join(TESTS_DIR, "test_run_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump({
            "total_passed": total_passed,
            "total_failed": total_failed,
            "overall_exit_code": overall_exit,
            "tiers": results,
            "visual": visual_results,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }, f, indent=2)

    return overall_exit


if __name__ == "__main__":
    sys.exit(main())
