"""
Feature 18: Graphic Asset Pipeline & Visual Fidelity (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & R3
"""

import os
import pytest
from tests.e2e_harness import (
    CURATED_IMAGE_NAMES,
)
from tests.visual_comparator import (
    FRAMES_DIR,
    SCREEN_REFERENCE_MAP,
)

ASSETS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "website", "src", "assets", "images")
)


def test_f18_curated_assets_count():
    """T1.18.1: Verify at least 20 curated PNG assets are specified in pipeline."""
    assert len(CURATED_IMAGE_NAMES) >= 20


def test_f18_all_curated_images_exist_on_disk():
    """T1.18.2: Verify every curated asset file actually exists in the assets directory."""
    for img_name in CURATED_IMAGE_NAMES:
        path = os.path.join(ASSETS_DIR, img_name)
        assert os.path.exists(path), f"Asset missing: {img_name}"


def test_f18_asset_sizes_non_empty():
    """T1.18.3: Verify all curated images are non-empty (>1KB)."""
    for img_name in CURATED_IMAGE_NAMES:
        path = os.path.join(ASSETS_DIR, img_name)
        assert os.path.getsize(path) > 1000, f"Asset too small or empty: {img_name}"


def test_f18_video_reference_frames_exist():
    """T1.18.4: Verify benchmark video reference frames exist in video_frames/."""
    assert os.path.exists(FRAMES_DIR)
    frames = [f for f in os.listdir(FRAMES_DIR) if f.endswith(".jpg")]
    assert len(frames) >= 40, f"Expected at least 40 reference frames, got {len(frames)}"


def test_f18_screen_reference_map_coverage():
    """T1.18.5: Verify visual comparator maps all major application screens."""
    required_screens = {
        "whatsapp", "gift", "teaser", "rejection", "menu", "cake",
        "celebration", "feast", "memories", "quote", "vinyl", "letter", "finale"
    }
    assert set(SCREEN_REFERENCE_MAP.keys()) == required_screens
    for screen, frame_name in SCREEN_REFERENCE_MAP.items():
        frame_path = os.path.join(FRAMES_DIR, frame_name)
        assert os.path.exists(frame_path), f"Mapped frame missing: {frame_name} for {screen}"
