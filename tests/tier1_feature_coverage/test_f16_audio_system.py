"""
Feature 16: Audio Soundtrack & Sound Effects (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Audio Stream
"""

import os
import pytest
from tests.e2e_harness import (
    MockAppSession,
)

AUDIO_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "website", "src", "assets", "audio", "bgm.mp3")
)


def test_f16_audio_file_exists():
    """T1.16.1: Verify bgm.mp3 audio asset exists on disk."""
    assert os.path.exists(AUDIO_FILE)
    assert os.path.getsize(AUDIO_FILE) > 500000  # > 500KB


def test_f16_audio_starts_unplayed():
    """T1.16.2: Verify audio starts in non-playing state to comply with browser autoplay policies."""
    app = MockAppSession()
    assert app.is_playing_music is False


def test_f16_audio_play_and_pause():
    """T1.16.3: Verify explicit play and pause triggers."""
    app = MockAppSession()
    app.play_music()
    assert app.is_playing_music is True
    app.pause_music()
    assert app.is_playing_music is False


def test_f16_audio_toggle():
    """T1.16.4: Verify audio toggle flips state back and forth."""
    app = MockAppSession()
    app.toggle_vinyl_music()
    assert app.is_playing_music is True
    app.toggle_vinyl_music()
    assert app.is_playing_music is False


def test_f16_audio_persists_through_all_screens():
    """T1.16.5: Verify audio persists across all screen navigation transitions."""
    app = MockAppSession()
    app.play_music()
    for screen in ["gift", "teaser", "menu", "cake", "memories", "letter", "finale"]:
        app.set_screen(screen)
        assert app.is_playing_music is True
