"""
Feature 13 Boundary & Corner Cases: "I Love You" Teddy Bear Finale
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_FINALE_TITLE,
    MockAppSession,
)


def test_b13_finale_title_case_and_tokens():
    """T2.13.1: Finale title consists of 'I', 'love', 'you'."""
    tokens = EXPECTED_FINALE_TITLE.split()
    assert tokens == ["I", "love", "you"]


def test_b13_repeated_visits_to_finale():
    """T2.13.2: Visiting finale 5 times in a row leaves clean state."""
    app = MockAppSession(initial_screen="menu")
    for _ in range(5):
        app.select_hub_card("finale")
        app.click_finale_home()
    assert app.active_screen == "menu"
    assert len(app.console_errors) == 0


def test_b13_candle_state_intact_in_finale():
    """T2.13.3: Pre-existing candle blown state remains true in finale."""
    app = MockAppSession(initial_screen="cake")
    app.blow_candles()
    app.set_screen("finale")
    assert app.is_candle_blown is True


def test_b13_music_state_intact_in_finale():
    """T2.13.4: Pre-existing music playback remains true in finale."""
    app = MockAppSession(initial_screen="letter")
    app.play_music()
    app.set_screen("finale")
    assert app.is_playing_music is True


def test_b13_direct_navigation_to_finale_valid():
    """T2.13.5: Direct set_screen to 'finale' is within VALID_SCREENS contract."""
    app = MockAppSession()
    app.set_screen("finale")
    assert app.active_screen == "finale"
