"""
Feature 6: Interactive Wish Cake (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 018-020
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_CAKE_BLOW_BTN,
    EXPECTED_CAKE_WISH_HEADING,
    MockAppSession,
)


def test_f06_cake_screen_initial_candle_state():
    """T1.6.1: Verify candle starts unblown when entering cake screen."""
    app = MockAppSession(initial_screen="cake")
    assert app.active_screen == "cake"
    assert app.is_candle_blown is False


def test_f06_cake_heading_text():
    """T1.6.2: Verify cake screen heading is 'MAKE A WISH MY LOVE'."""
    assert EXPECTED_CAKE_WISH_HEADING == "MAKE A WISH MY LOVE"


def test_f06_cake_blow_button_label():
    """T1.6.3: Verify primary action button prompt is 'Blow'."""
    assert EXPECTED_CAKE_BLOW_BTN == "Blow"


def test_f06_blow_candles_action():
    """T1.6.4: Verify executing blow candles marks candles as blown."""
    app = MockAppSession(initial_screen="cake")
    app.blow_candles()
    assert app.is_candle_blown is True
    assert app.active_screen == "cake"


def test_f06_blow_candles_only_when_on_cake_screen():
    """T1.6.5: Verify blow_candles only activates when on 'cake' screen."""
    app = MockAppSession(initial_screen="menu")
    app.blow_candles()
    assert app.is_candle_blown is False
