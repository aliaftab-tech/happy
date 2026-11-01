"""
Feature 2 Boundary & Corner Cases: Gift Box Opener
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_GIFT_PROMPT,
    MockAppSession,
)


def test_b02_rapid_multiple_clicks_idempotent():
    """T2.2.1: Repeated clicks on gift box do not advance past 'teaser'."""
    app = MockAppSession(initial_screen="gift")
    for _ in range(10):
        app.click_gift_box()
    assert app.active_screen == "teaser"
    assert app.transition_history == ["gift", "teaser"]


def test_b02_click_ignored_on_unrelated_screens():
    """T2.2.2: Calling gift box click when on 'cake' is a no-op."""
    app = MockAppSession(initial_screen="cake")
    app.click_gift_box()
    assert app.active_screen == "cake"
    assert app.transition_history == ["cake"]


def test_b02_prompt_whitespace_boundary():
    """T2.2.3: Prompt text has no extraneous whitespace padding."""
    assert EXPECTED_GIFT_PROMPT == EXPECTED_GIFT_PROMPT.strip()
    assert len(EXPECTED_GIFT_PROMPT) > 0


def test_b02_audio_state_untouched_on_gift_open():
    """T2.2.4: Opening gift box preserves music state if previously active."""
    app = MockAppSession(initial_screen="gift")
    app.play_music()
    assert app.is_playing_music is True
    app.click_gift_box()
    assert app.active_screen == "teaser"
    assert app.is_playing_music is True


def test_b02_candle_state_untouched_on_gift_open():
    """T2.2.5: Opening gift box does not touch candle state."""
    app = MockAppSession(initial_screen="gift")
    assert app.is_candle_blown is False
    app.click_gift_box()
    assert app.is_candle_blown is False
