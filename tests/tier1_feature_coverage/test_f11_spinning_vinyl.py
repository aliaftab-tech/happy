"""
Feature 11: Spinning Vinyl Record Player (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 037-038
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_VINYL_PROMPT,
    MockAppSession,
)


def test_f11_vinyl_prompt_copy():
    """T1.11.1: Verify vinyl player prompt matches 'Play this while you are reading'."""
    assert EXPECTED_VINYL_PROMPT == "Play this while you are reading"


def test_f11_vinyl_initial_audio_state():
    """T1.11.2: Verify audio starts paused initially."""
    app = MockAppSession(initial_screen="letter")
    assert app.is_playing_music is False


def test_f11_vinyl_toggle_play_pause():
    """T1.11.3: Verify tapping vinyl player toggles audio playback on and off."""
    app = MockAppSession(initial_screen="letter")
    app.toggle_vinyl_music()
    assert app.is_playing_music is True
    app.toggle_vinyl_music()
    assert app.is_playing_music is False


def test_f11_vinyl_music_plays_across_navigation():
    """T1.11.4: Verify vinyl music continues playing when navigating back to menu."""
    app = MockAppSession(initial_screen="letter")
    app.toggle_vinyl_music()
    assert app.is_playing_music is True
    app.click_letter_back()
    assert app.active_screen == "menu"
    assert app.is_playing_music is True


def test_f11_vinyl_explicit_play_and_pause():
    """T1.11.5: Verify direct play_music and pause_music controls function as expected."""
    app = MockAppSession(initial_screen="letter")
    app.play_music()
    assert app.is_playing_music is True
    app.pause_music()
    assert app.is_playing_music is False
