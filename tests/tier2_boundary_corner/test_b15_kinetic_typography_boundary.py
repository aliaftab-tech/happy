"""
Feature 15 Boundary & Corner Cases: Kinetic Typography & Micro-interactions
"""

import pytest
from tests.e2e_harness import (
    COLOR_TOKENS,
    EXPECTED_CAKE_WISH_HEADING,
    EXPECTED_FEAST_HEADING,
    EXPECTED_HUB_TITLE,
    EXPECTED_TEASER_QUESTION,
)


def test_b15_all_color_tokens_are_valid_hex():
    """T2.15.1: All color tokens start with '#' and have length 7."""
    for name, hex_code in COLOR_TOKENS.items():
        assert hex_code.startswith("#"), f"Token {name} does not start with #: {hex_code}"
        assert len(hex_code) == 7, f"Token {name} is not 7 chars: {hex_code}"
        # Valid hex digits
        int(hex_code[1:], 16)


def test_b15_terracotta_squircle_token():
    """T2.15.2: Terracotta squircle token matches '#a7302c'."""
    assert COLOR_TOKENS["terracotta_squircle"].lower() == "#a7302c"


def test_b15_headings_no_html_injection():
    """T2.15.3: Headings contain no unescaped raw HTML script tags."""
    for text in [EXPECTED_TEASER_QUESTION, EXPECTED_HUB_TITLE, EXPECTED_CAKE_WISH_HEADING, EXPECTED_FEAST_HEADING]:
        assert "<script>" not in text.lower()
        assert "javascript:" not in text.lower()


def test_b15_headings_strip_clean():
    """T2.15.4: All heading constants have no accidental leading/trailing whitespace."""
    for text in [EXPECTED_TEASER_QUESTION, EXPECTED_HUB_TITLE, EXPECTED_CAKE_WISH_HEADING, EXPECTED_FEAST_HEADING]:
        assert text == text.strip()


def test_b15_non_empty_typography_constants():
    """T2.15.5: All typography constants are non-empty strings."""
    assert len(EXPECTED_TEASER_QUESTION) > 10
    assert len(EXPECTED_HUB_TITLE) > 10
    assert len(EXPECTED_CAKE_WISH_HEADING) > 10
    assert len(EXPECTED_FEAST_HEADING) > 5
