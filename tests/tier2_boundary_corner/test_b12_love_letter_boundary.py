"""
Feature 12 Boundary & Corner Cases: Special Birthday Love Letter
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_LETTER_BACK,
    LETTER_PARAGRAPH_1,
    LETTER_PARAGRAPH_2,
    LETTER_PARAGRAPH_3,
    MockAppSession,
)


def test_b12_rapid_back_clicks_idempotent():
    """T2.12.1: Rapid back clicks on letter screen transition to menu once."""
    app = MockAppSession(initial_screen="letter")
    for _ in range(5):
        app.click_letter_back()
    assert app.active_screen == "menu"
    assert app.transition_history == ["letter", "menu"]


def test_b12_back_blocked_on_other_screens():
    """T2.12.2: Calling click_letter_back from non-letter screens is a no-op."""
    for scr in ["whatsapp", "gift", "teaser", "cake", "finale"]:
        app = MockAppSession(initial_screen=scr)
        app.click_letter_back()
        assert app.active_screen == scr


def test_b12_paragraph_1_word_count_boundary():
    """T2.12.3: Paragraph 1 has at least 30 words and contains 'happiness'."""
    words = LETTER_PARAGRAPH_1.split()
    assert len(words) >= 30
    assert "happiness," in words or "happiness" in LETTER_PARAGRAPH_1


def test_b12_paragraph_2_sentiments():
    """T2.12.4: Paragraph 2 contains key phrases for comfort and brightening days."""
    assert "comfortable" in LETTER_PARAGRAPH_2
    assert "brightens days" in LETTER_PARAGRAPH_2
    assert "loved you are" in LETTER_PARAGRAPH_2


def test_b12_paragraph_3_emoji_and_closure():
    """T2.12.5: Paragraph 3 contains tulip emoji and closure words."""
    assert "🌷" in LETTER_PARAGRAPH_3
    assert "dreams" in LETTER_PARAGRAPH_3
    assert "wonderful person" in LETTER_PARAGRAPH_3
