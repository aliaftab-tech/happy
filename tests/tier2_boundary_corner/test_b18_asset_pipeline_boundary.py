"""
Feature 18 Boundary & Corner Cases: Graphic Asset Pipeline & Visual Fidelity
"""

import os
import pytest
from PIL import Image
from tests.e2e_harness import (
    CURATED_IMAGE_NAMES,
)
from tests.visual_comparator import (
    FRAMES_DIR,
    compute_dominant_color_delta,
    compute_histogram_similarity,
)

ASSETS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "website", "src", "assets", "images")
)


def test_b18_asset_file_extensions():
    """T2.18.1: Every asset in pipeline has .png extension."""
    for img_name in CURATED_IMAGE_NAMES:
        assert img_name.endswith(".png")


def test_b18_unique_asset_names():
    """T2.18.2: Asset names list contains no duplicate filenames."""
    assert len(CURATED_IMAGE_NAMES) == len(set(CURATED_IMAGE_NAMES))


def test_b18_images_loadable_by_pil():
    """T2.18.3: Every image can be successfully opened and parsed by PIL."""
    for img_name in CURATED_IMAGE_NAMES:
        path = os.path.join(ASSETS_DIR, img_name)
        with Image.open(path) as img:
            assert img.width > 0
            assert img.height > 0


def test_b18_identical_image_similarity_is_one():
    """T2.18.4: Computing histogram similarity on identical image yields exactly 1.0."""
    ref_path = os.path.join(FRAMES_DIR, "frame_001.jpg")
    with Image.open(ref_path) as img:
        sim = compute_histogram_similarity(img, img)
        assert abs(sim - 1.0) < 0.001
        delta = compute_dominant_color_delta(img, img)
        assert delta == 0.0


def test_b18_dissimilar_images_have_lower_similarity():
    """T2.18.5: Computing similarity on distinctly different frames yields score < 0.95."""
    path1 = os.path.join(FRAMES_DIR, "frame_001.jpg")
    path2 = os.path.join(FRAMES_DIR, "frame_007.jpg")
    with Image.open(path1) as img1, Image.open(path2) as img2:
        sim = compute_histogram_similarity(img1, img2)
        assert sim < 0.95
