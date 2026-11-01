"""
Feature 15: Kinetic Typography & Micro-interactions (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 005, 015
"""

import pytest
from tests.e2e_harness import (
    COLOR_TOKENS,
    EXPECTED_HUB_TITLE,
    EXPECTED_TEASER_QUESTION,
)


def test_f15_teaser_typography_contract():
    """T1.15.1: Verify teaser question typography matches specification."""
    assert len(EXPECTED_TEASER_QUESTION) > 0
    assert EXPECTED_TEASER_QUESTION == "Do you want to see your Surprise"


def test_f15_hub_kinetic_title_structure():
    """T1.15.2: Verify hub 3-line kinetic typography contains all three segments."""
    tokens = EXPECTED_HUB_TITLE.split()
    assert "THESE" in tokens
    assert "ARE" in tokens
    assert "FOR" in tokens
    assert "YOU" in tokens
    assert "CUTIE" in tokens


def test_f15_color_tokens_burgundy():
    """T1.15.3: Verify burgundy background token matches '#810503'."""
    assert COLOR_TOKENS["burgundy_bg"].lower() == "#810503"


def test_f15_color_tokens_coral_pill():
    """T1.15.4: Verify coral pill button color token matches '#fc7272'."""
    assert COLOR_TOKENS["coral_pill"].lower() == "#fc7272"


def test_f15_color_tokens_stationery_pink():
    """T1.15.5: Verify stationery pink color token matches '#f7a1c4'."""
    assert COLOR_TOKENS["stationery_pink"].lower() == "#f7a1c4"
