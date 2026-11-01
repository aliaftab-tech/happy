"""
Feature 7 Boundary & Corner Cases: Celebration Reveal
"""

import pytest
from tests.e2e_harness import (
    MockAppSession,
)


def test_b07_celebration_state_persists_across_screens():
    """T2.7.1: Blown candle celebration state persists when navigating away."""
    app = MockAppSession(initial_screen="cake")
    app.blow_candles()
    assert app.is_candle_blown is True
    app.set_screen("menu")
    assert app.is_candle_blown is True
    app.set_screen("cake")
    assert app.is_candle_blown is True


def test_b07_celebration_with_music_playing():
    """T2.7.2: Triggering celebration while music is playing preserves music."""
    app = MockAppSession(initial_screen="cake")
    app.play_music()
    assert app.is_playing_music is True
    app.blow_candles()
    assert app.is_candle_blown is True
    assert app.is_playing_music is True


def test_b07_celebration_with_music_paused():
    """T2.7.3: Triggering celebration does not forcibly start music if paused."""
    app = MockAppSession(initial_screen="cake")
    assert app.is_playing_music is False
    app.blow_candles()
    assert app.is_playing_music is False


def test_b07_rapid_celebrate_reset_stress():
    """T2.7.4: Rapid celebration and reset cycles (20x) maintain boolean integrity."""
    app = MockAppSession(initial_screen="cake")
    for _ in range(20):
        app.blow_candles()
        assert app.is_candle_blown is True
        app.reset_candles()
        assert app.is_candle_blown is False
    assert len(app.console_errors) == 0


def test_b07_blowing_does_not_mutate_transition_history():
    """T2.7.5: Blowing candles changes candle state without adding new screen transition entries."""
    app = MockAppSession(initial_screen="cake")
    initial_len = len(app.transition_history)
    app.blow_candles()
    assert len(app.transition_history) == initial_len
