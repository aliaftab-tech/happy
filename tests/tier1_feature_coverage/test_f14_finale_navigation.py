"""
Feature 14: Finale Navigation (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frame 047
"""

import pytest
from tests.e2e_harness import (
    MockAppSession,
)


def test_f14_finale_home_returns_to_menu():
    """T1.14.1: Verify clicking Home button on finale returns to 'menu'."""
    app = MockAppSession(initial_screen="finale")
    app.click_finale_home()
    assert app.active_screen == "menu"


def test_f14_finale_complete_roundtrip():
    """T1.14.2: Verify complete menu -> finale -> menu loop."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("finale")
    assert app.active_screen == "finale"
    app.click_finale_home()
    assert app.active_screen == "menu"
    assert app.transition_history == ["menu", "finale", "menu"]


def test_f14_finale_home_ignored_when_not_on_finale():
    """T1.14.3: Verify click_finale_home is safe and does not alter non-finale screens."""
    app = MockAppSession(initial_screen="cake")
    app.click_finale_home()
    assert app.active_screen == "cake"


def test_f14_multiple_home_clicks_idempotent():
    """T1.14.4: Verify repeated clicks on Home after reaching menu cause no error."""
    app = MockAppSession(initial_screen="finale")
    app.click_finale_home()
    assert app.active_screen == "menu"
    app.click_finale_home()
    assert app.active_screen == "menu"


def test_f14_finale_home_preserves_audio():
    """T1.14.5: Verify navigating Home from Finale keeps music playing."""
    app = MockAppSession(initial_screen="finale")
    app.play_music()
    app.click_finale_home()
    assert app.active_screen == "menu"
    assert app.is_playing_music is True
