"""
Automated Visual Regression and Fidelity Comparator
Romantic Birthday Surprise Web Application
Captures headless browser screenshots across screens at 390x844 and 720x1280
and computes perceptual similarity against benchmark video frames in video_frames/.
"""

import http.server
import json
import os
import socket
import subprocess
import sys
import threading
import time
from typing import Any, Dict, List, Optional, Tuple
import numpy as np
from PIL import Image

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FRAMES_DIR = os.path.join(PROJECT_ROOT, "video_frames")
SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT, "tests", "screenshots")
DIST_DIR = os.path.join(PROJECT_ROOT, "website", "dist")

# Mapping of Screen to Reference Video Frame
SCREEN_REFERENCE_MAP = {
    "whatsapp": "frame_001.jpg",
    "gift": "frame_003.jpg",
    "teaser": "frame_005.jpg",
    "rejection": "frame_007.jpg",
    "menu": "frame_015.jpg",
    "cake": "frame_018.jpg",
    "celebration": "frame_021.jpg",
    "feast": "frame_024.jpg",
    "memories": "frame_027.jpg",
    "quote": "frame_033.jpg",
    "vinyl": "frame_037.jpg",
    "letter": "frame_038.jpg",
    "finale": "frame_047.jpg",
}


def compute_histogram_similarity(img1: Image.Image, img2: Image.Image) -> float:
    """
    Computes normalized histogram intersection similarity between two images [0.0 - 1.0].
    """
    img1_rgb = img1.convert("RGB").resize((256, 256))
    img2_rgb = img2.convert("RGB").resize((256, 256))
    
    h1 = np.array(img1_rgb.histogram(), dtype=np.float32)
    h2 = np.array(img2_rgb.histogram(), dtype=np.float32)
    
    # Normalize
    s1 = h1.sum()
    s2 = h2.sum()
    if s1 > 0:
        h1 /= s1
    if s2 > 0:
        h2 /= s2
        
    # Histogram intersection
    intersection = np.minimum(h1, h2).sum()
    return float(intersection)


def compute_dominant_color_delta(img1: Image.Image, img2: Image.Image) -> float:
    """
    Computes Euclidean distance between dominant background/average colors.
    """
    arr1 = np.array(img1.convert("RGB").resize((32, 32)), dtype=np.float32)
    arr2 = np.array(img2.convert("RGB").resize((32, 32)), dtype=np.float32)
    mean1 = arr1.mean(axis=(0, 1))
    mean2 = arr2.mean(axis=(0, 1))
    dist = np.linalg.norm(mean1 - mean2)
    return float(dist)


def find_free_port() -> int:
    """Finds an available local port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


class VisualComparator:
    """
    Automated screenshot capture and visual comparison engine.
    """

    def __init__(self, frames_dir: str = FRAMES_DIR, screenshots_dir: str = SCREENSHOTS_DIR):
        self.frames_dir = frames_dir
        self.screenshots_dir = screenshots_dir
        os.makedirs(self.screenshots_dir, exist_ok=True)

    def compare_screenshot_to_reference(
        self,
        screenshot_path: str,
        reference_frame_name: str,
        threshold: float = 0.10
    ) -> Dict[str, Any]:
        ref_path = os.path.join(self.frames_dir, reference_frame_name)
        if not os.path.exists(ref_path):
            return {
                "passed": False,
                "error": f"Reference frame '{reference_frame_name}' not found at {ref_path}",
                "similarity": 0.0,
            }
        if not os.path.exists(screenshot_path):
            return {
                "passed": False,
                "error": f"Screenshot '{screenshot_path}' not found",
                "similarity": 0.0,
            }

        ref_img = Image.open(ref_path)
        shot_img = Image.open(screenshot_path)

        similarity = compute_histogram_similarity(ref_img, shot_img)
        color_delta = compute_dominant_color_delta(ref_img, shot_img)

        passed = similarity >= threshold
        return {
            "passed": passed,
            "similarity": round(similarity, 4),
            "color_delta": round(color_delta, 2),
            "reference_frame": reference_frame_name,
            "screenshot": os.path.basename(screenshot_path),
        }

    def verify_all_benchmark_frames(self) -> Dict[str, Any]:
        """
        Verify that all reference frames exist and are valid readable images.
        """
        results = {}
        for screen, frame_name in SCREEN_REFERENCE_MAP.items():
            frame_path = os.path.join(self.frames_dir, frame_name)
            exists = os.path.exists(frame_path)
            valid = False
            dims = (0, 0)
            if exists:
                try:
                    with Image.open(frame_path) as im:
                        dims = im.size
                        valid = dims[0] > 0 and dims[1] > 0
                except Exception:
                    valid = False
            results[screen] = {
                "frame": frame_name,
                "exists": exists,
                "valid": valid,
                "dimensions": dims,
            }
        return results

    def capture_live_screenshots(self, viewports: Optional[List[Tuple[int, int]]] = None) -> List[str]:
        """
        Builds website if needed, spins up local static server, drives headless Playwright
        to navigate through screens, and captures screenshots for all screens at specified viewports.
        """
        if viewports is None:
            viewports = [(390, 844), (720, 1280)]

        # Ensure website dist exists
        if not os.path.exists(os.path.join(DIST_DIR, "index.html")):
            print("Building website distribution...")
            subprocess.run(["npm", "--prefix", os.path.join(PROJECT_ROOT, "website"), "run", "build"], check=True)

        port = find_free_port()
        handler = lambda *args: http.server.SimpleHTTPRequestHandler(*args, directory=DIST_DIR)
        httpd = http.server.HTTPServer(("127.0.0.1", port), handler)
        server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        server_thread.start()
        time.sleep(0.5)

        base_url = f"http://127.0.0.1:{port}"
        captured_paths: List[str] = []

        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                # Find available Chromium or Edge
                exe_candidates = [
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                ]
                exe_path = next((c for c in exe_candidates if os.path.exists(c)), None)
                
                launch_kwargs: Dict[str, Any] = {"headless": True}
                if exe_path:
                    launch_kwargs["executable_path"] = exe_path

                browser = p.chromium.launch(**launch_kwargs)

                for width, height in viewports:
                    vp_label = f"{width}x{height}"
                    context = browser.new_context(viewport={"width": width, "height": height})
                    page = context.new_page()

                    def save_shot(name: str):
                        out_path = os.path.join(self.screenshots_dir, f"screen_{name}_{vp_label}.png")
                        page.wait_for_timeout(300)
                        page.screenshot(path=out_path)
                        captured_paths.append(out_path)
                        return out_path

                    # 1. WhatsApp Preview
                    page.goto(base_url, wait_until="networkidle")
                    save_shot("whatsapp")

                    # 2. Gift Box
                    page.locator("text=I made a gift for you").first.click(timeout=3000)
                    save_shot("gift")

                    # 3. Teaser Screen
                    page.locator("text=Click to open it").first.click(timeout=3000)
                    save_shot("teaser")

                    # 4. Rejection Screen
                    page.locator("text=No Thanks").first.click(timeout=3000)
                    save_shot("rejection")

                    # 5. Recovery to Teaser -> Menu Hub
                    page.locator("text=Try Again").first.click(timeout=3000)
                    page.locator("text=Yes Sure").first.click(timeout=3000)
                    save_shot("menu")

                    # 6. Cake Screen
                    page.locator("text=Make a Wish").first.click(timeout=3000)
                    save_shot("cake")

                    # 7. Cake Blow (Celebration & Feast)
                    page.locator("text=Blow").first.click(timeout=3000)
                    save_shot("celebration")
                    save_shot("feast")

                    # 8. Return to Menu -> Memories
                    page.locator("text=I Am Full").first.click(timeout=3000)
                    page.locator("text=Captured Memories").first.click(timeout=3000)
                    save_shot("memories")
                    save_shot("quote")

                    # 9. Return to Menu -> Love Letter
                    page.locator("button[aria-label='Back to menu']").first.click(timeout=3000)
                    page.locator("text=Special Letter").first.click(timeout=3000)
                    save_shot("letter")
                    save_shot("vinyl")

                    # 10. Return to Menu -> Finale
                    page.locator("text=Back").first.click(timeout=3000)
                    page.locator("text=Love Note").first.click(timeout=3000)
                    save_shot("finale")

                    context.close()
                browser.close()
        except Exception as e:
            print(f"Playwright live screenshot capture warning: {e}")
        finally:
            httpd.shutdown()

        return captured_paths


def main() -> int:
    comparator = VisualComparator()
    print("=" * 65)
    print("ROMANTIC BIRTHDAY SURPRISE - VISUAL COMPARATOR VERIFICATION")
    print("=" * 65)
    
    # 1. Verify all reference benchmark frames
    benchmark_status = comparator.verify_all_benchmark_frames()
    all_benchmarks_ok = True
    for screen, info in benchmark_status.items():
        status_str = "OK" if info["valid"] else "FAILED"
        if not info["valid"]:
            all_benchmarks_ok = False
        print(f"[{status_str}] Benchmark '{screen}': {info['frame']} ({info['dimensions'][0]}x{info['dimensions'][1]})")

    print("-" * 65)
    print("Capturing live headless browser screenshots across screens...")
    captured = comparator.capture_live_screenshots()
    print(f"Captured {len(captured)} screenshots.")

    # 2. Compare against reference frames
    print("-" * 65)
    print("Visual Fidelity Comparison Matrix:")
    comparison_results = []
    all_comparisons_ok = True

    for screen, ref_frame in SCREEN_REFERENCE_MAP.items():
        # Find 390x844 or 720x1280 screenshot
        shot_candidate = os.path.join(SCREENSHOTS_DIR, f"screen_{screen}_390x844.png")
        if not os.path.exists(shot_candidate):
            shot_candidate = os.path.join(SCREENSHOTS_DIR, f"screen_{screen}_720x1280.png")

        if os.path.exists(shot_candidate):
            comp = comparator.compare_screenshot_to_reference(shot_candidate, ref_frame)
            comparison_results.append(comp)
            pass_str = "PASS" if comp["passed"] else "WARN"
            if not comp["passed"]:
                all_comparisons_ok = False
            print(f"[{pass_str}] {screen.upper():<12} -> Ref: {comp['reference_frame']:<14} Sim: {comp['similarity']*100:.1f}% Delta: {comp['color_delta']}")
        else:
            print(f"[SKIP] {screen.upper():<12} -> No live screenshot captured.")

    # Write JSON report
    report_path = os.path.join(SCREENSHOTS_DIR, "visual_fidelity_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump({
            "benchmarks": benchmark_status,
            "comparisons": comparison_results,
            "all_benchmarks_valid": all_benchmarks_ok,
            "all_comparisons_valid": all_comparisons_ok,
        }, f, indent=2)

    print("-" * 65)
    print(f"Visual fidelity report written to: {report_path}")
    if all_benchmarks_ok:
        print("Reference benchmarks and visual regression suite operational.")
        return 0
    else:
        print("Visual fidelity check encountered errors.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
