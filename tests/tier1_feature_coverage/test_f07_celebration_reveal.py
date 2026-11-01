"""
Feature 7: Birthday Celebration Reveal (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 021-023
"""

import pytest
from tests.e2e_harness import (
    MockAppSession,
)


def test_f07_celebration_state_triggered_by_blowing():
    """T1.7.1: Verify celebration state is active when candles are blown."""
    app = MockAppSession(initial_screen="cake")
    assert not app.is_candle_blown
    app.blow_candles()
    assert app.is_candle_blown is True


def test_f07_celebration_keeps_screen_context():
    """T1.7.2: Verify cake screen remains active while celebration unfolds."""
    app = MockAppSession(initial_screen="cake")
    app.blow_candles()
    assert app.active_screen == "cake"


def test_f07_celebration_history_trace():
    """T1.7.3: Verify celebration flow from hub into cake and candle blowing."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("cake")
    app.blow_candles()
    assert app.transition_history == ["menu", "cake"]
    assert app.is_candle_blown is True


def test_f07_celebration_reset_capability():
    """T1.7.4: Verify celebration candles can be reset programmatically."""
    app = MockAppSession(initial_screen="cake")
    app.blow_candles()
    assert app.is_candle_blown is True
    app.reset_candles()
    assert app.is_candle_blown is False


def test_f07_celebration_console_clean():
    """T1.7.5: Verify no unhandled errors recorded during celebration trigger."""
    app = MockAppSession(initial_screen="cake")
    app.blow_candles()
    assert len(app.console_errors) == 0
