"""
Feature 8 Boundary & Corner Cases: Bakery Feast
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_FEAST_FULL_BTN,
    EXPECTED_FEAST_HEADING,
    MockAppSession,
)


def test_b08_rapid_feast_full_clicks_idempotent():
    """T2.8.1: Rapid repeated clicks on 'I Am Full' transition to menu once."""
    app = MockAppSession(initial_screen="cake")
    app.blow_candles()
    for _ in range(5):
        app.click_feast_full()
    assert app.active_screen == "menu"
    assert app.transition_history == ["cake", "menu"]


def test_b08_click_full_blocked_from_other_screens():
    """T2.8.2: Calling click_feast_full from screens other than 'cake' is a no-op."""
    for scr in ["whatsapp", "gift", "teaser", "rejection", "memories", "letter", "finale"]:
        app = MockAppSession(initial_screen=scr)
        app.click_feast_full()
        assert app.active_screen == scr


def test_b08_reentry_after_full_allows_new_cycle():
    """T2.8.3: Returning to cake and resetting candles allows full sequence re-run."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("cake")
    app.blow_candles()
    app.click_feast_full()
    assert app.active_screen == "menu"
    
    app.select_hub_card("cake")
    app.reset_candles()
    assert not app.is_candle_blown
    app.blow_candles()
    assert app.is_candle_blown
    app.click_feast_full()
    assert app.active_screen == "menu"


def test_b08_heading_punctuation_boundary():
    """T2.8.4: Feast heading contains exclamation mark and uppercase 'CAKE!'."""
    assert EXPECTED_FEAST_HEADING.endswith("!")
    assert "CAKE!" in EXPECTED_FEAST_HEADING


def test_b08_button_words_count():
    """T2.8.5: 'I Am Full' consists of exactly 3 words."""
    words = EXPECTED_FEAST_FULL_BTN.split()
    assert len(words) == 3
    assert words == ["I", "Am", "Full"]
