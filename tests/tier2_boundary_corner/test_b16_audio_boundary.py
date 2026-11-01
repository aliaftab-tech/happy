"""
Feature 16 Boundary & Corner Cases: Audio Soundtrack
"""

import os
import pytest
from tests.e2e_harness import (
    MockAppSession,
)

AUDIO_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "website", "src", "assets", "audio", "bgm.mp3")
)


def test_b16_audio_file_extension():
    """T2.16.1: Audio file is a valid mp3 file."""
    assert AUDIO_FILE.endswith(".mp3")
    assert os.path.isfile(AUDIO_FILE)


def test_b16_audio_stress_toggle_100_times():
    """T2.16.2: Toggling audio 100 times executes rapidly and consistently."""
    app = MockAppSession()
    for _ in range(100):
        app.toggle_vinyl_music()
    assert app.is_playing_music is False


def test_b16_repeated_play_calls_safe():
    """T2.16.3: Calling play_music repeatedly when already playing stays True."""
    app = MockAppSession()
    for _ in range(10):
        app.play_music()
    assert app.is_playing_music is True


def test_b16_repeated_pause_calls_safe():
    """T2.16.4: Calling pause_music repeatedly when already paused stays False."""
    app = MockAppSession()
    for _ in range(10):
        app.pause_music()
    assert app.is_playing_music is False


def test_b16_audio_remains_active_across_20_screen_hops():
    """T2.16.5: Background audio stays playing across 20 arbitrary screen switches."""
    app = MockAppSession()
    app.play_music()
    screens = ["gift", "teaser", "rejection", "teaser", "menu", "cake", "menu", "memories", "menu", "letter", "menu", "finale", "menu"] * 2
    for scr in screens[:20]:
        app.set_screen(scr)
        assert app.is_playing_music is True
