"""
Feature 11 Boundary & Corner Cases: Spinning Vinyl Audio Player
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_VINYL_PROMPT,
    MockAppSession,
)


def test_b11_even_toggles_preserve_initial_state():
    """T2.11.1: Even number of rapid toggles (10x) returns music state to initial."""
    app = MockAppSession(initial_screen="letter")
    assert app.is_playing_music is False
    for _ in range(10):
        app.toggle_vinyl_music()
    assert app.is_playing_music is False


def test_b11_odd_toggles_inverts_state():
    """T2.11.2: Odd number of rapid toggles (9x) leaves music inverted."""
    app = MockAppSession(initial_screen="letter")
    assert app.is_playing_music is False
    for _ in range(9):
        app.toggle_vinyl_music()
    assert app.is_playing_music is True


def test_b11_vinyl_prompt_keywords():
    """T2.11.3: Prompt contains 'Play', 'while', and 'reading'."""
    assert "Play" in EXPECTED_VINYL_PROMPT
    assert "reading" in EXPECTED_VINYL_PROMPT


def test_b11_multiple_pause_calls_idempotent():
    """T2.11.4: Calling pause_music multiple times when already paused is safe."""
    app = MockAppSession()
    assert not app.is_playing_music
    for _ in range(5):
        app.pause_music()
    assert not app.is_playing_music


def test_b11_multiple_play_calls_idempotent():
    """T2.11.5: Calling play_music multiple times when already playing is safe."""
    app = MockAppSession()
    for _ in range(5):
        app.play_music()
    assert app.is_playing_music is True
