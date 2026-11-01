"""
Feature 13: "I Love You" Teddy Bear Finale (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 045-047
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_FINALE_TITLE,
    MockAppSession,
)


def test_f13_finale_title_copy():
    """T1.13.1: Verify finale screen calligraphic title is 'I love you'."""
    assert EXPECTED_FINALE_TITLE == "I love you"


def test_f13_navigate_to_finale_screen():
    """T1.13.2: Verify selecting finale card from menu navigates to 'finale'."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("finale")
    assert app.active_screen == "finale"


def test_f13_finale_state_persistence():
    """T1.13.3: Verify finale screen maintains valid activeScreen state."""
    app = MockAppSession(initial_screen="finale")
    assert app.active_screen == "finale"
    assert len(app.console_errors) == 0


def test_f13_finale_audio_preservation():
    """T1.13.4: Verify entering finale retains playing music state."""
    app = MockAppSession(initial_screen="menu")
    app.play_music()
    app.select_hub_card("finale")
    assert app.active_screen == "finale"
    assert app.is_playing_music is True


def test_f13_finale_teddy_clean_history():
    """T1.13.5: Verify transition history accurately records entry into finale."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("finale")
    assert app.transition_history == ["menu", "finale"]
