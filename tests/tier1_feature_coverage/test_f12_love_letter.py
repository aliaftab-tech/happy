"""
Feature 12: Special Birthday Love Letter (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 038-042
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_LETTER_BACK,
    LETTER_FOOTER_1,
    LETTER_FOOTER_2,
    LETTER_PARAGRAPH_1,
    LETTER_PARAGRAPH_2,
    LETTER_PARAGRAPH_3,
    MockAppSession,
)


def test_f12_letter_verbatim_paragraphs():
    """T1.12.1: Verify all 3 paragraphs of the love letter are defined verbatim."""
    assert "Today is all about celebrating someone truly special" in LETTER_PARAGRAPH_1
    assert "Thank you for being such an amazing person" in LETTER_PARAGRAPH_2
    assert "May this new chapter of your life be filled with peace" in LETTER_PARAGRAPH_3


def test_f12_letter_footer_copy():
    """T1.12.2: Verify letter footer matches celebratory closings."""
    assert LETTER_FOOTER_1 == "HAPPY BIRTHDAY ONCE AGAIN."
    assert "MAY YOUR DAY BE AS BEAUTIFUL AS YOUR HEART" in LETTER_FOOTER_2


def test_f12_letter_back_button_label():
    """T1.12.3: Verify letter return button label is 'Back'."""
    assert EXPECTED_LETTER_BACK == "Back"


def test_f12_letter_back_navigation():
    """T1.12.4: Verify clicking 'Back' on letter screen returns to 'menu'."""
    app = MockAppSession(initial_screen="letter")
    app.click_letter_back()
    assert app.active_screen == "menu"


def test_f12_letter_full_roundtrip():
    """T1.12.5: Verify hub -> letter -> hub navigation sequence."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("letter")
    assert app.active_screen == "letter"
    app.click_letter_back()
    assert app.active_screen == "menu"
    assert app.transition_history == ["menu", "letter", "menu"]
