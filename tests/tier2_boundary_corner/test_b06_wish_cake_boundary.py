"""
Feature 6 Boundary & Corner Cases: Interactive Wish Cake
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_CAKE_BLOW_BTN,
    EXPECTED_CAKE_WISH_HEADING,
    MockAppSession,
)


def test_b06_rapid_candle_blowing_idempotent():
    """T2.6.1: Repeated blow_candles calls in rapid succession remain safe."""
    app = MockAppSession(initial_screen="cake")
    for _ in range(5):
        app.blow_candles()
    assert app.is_candle_blown is True
    assert app.active_screen == "cake"


def test_b06_blow_candles_blocked_on_other_screens():
    """T2.6.2: Calling blow_candles from 'whatsapp', 'teaser', 'menu' is blocked."""
    for scr in ["whatsapp", "teaser", "menu", "memories", "letter"]:
        app = MockAppSession(initial_screen=scr)
        app.blow_candles()
        assert app.is_candle_blown is False


def test_b06_blow_reset_blow_cycle():
    """T2.6.3: Cycle of blow -> reset -> blow maintains consistent state."""
    app = MockAppSession(initial_screen="cake")
    app.blow_candles()
    assert app.is_candle_blown is True
    app.reset_candles()
    assert app.is_candle_blown is False
    app.blow_candles()
    assert app.is_candle_blown is True


def test_b06_wish_heading_casing_and_words():
    """T2.6.4: Wish heading is uppercase and contains romantic terms."""
    assert EXPECTED_CAKE_WISH_HEADING.isupper()
    assert "WISH" in EXPECTED_CAKE_WISH_HEADING
    assert "LOVE" in EXPECTED_CAKE_WISH_HEADING


def test_b06_blow_btn_single_word_boundary():
    """T2.6.5: Blow button label consists of a single concise verb."""
    assert len(EXPECTED_CAKE_BLOW_BTN.split()) == 1
    assert EXPECTED_CAKE_BLOW_BTN == "Blow"
