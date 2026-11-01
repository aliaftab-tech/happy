"""
Feature 9 Boundary & Corner Cases: Scrapbook Polaroid Gallery
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_MEMORIES_HEADING,
    MockAppSession,
)


def test_b09_rapid_back_clicks_idempotent():
    """T2.9.1: Rapid back clicks on memories gallery exit to menu once."""
    app = MockAppSession(initial_screen="memories")
    for _ in range(5):
        app.click_memories_back()
    assert app.active_screen == "menu"
    assert app.transition_history == ["memories", "menu"]


def test_b09_back_blocked_on_other_screens():
    """T2.9.2: Calling click_memories_back from 'cake' or 'letter' does nothing."""
    for scr in ["cake", "letter", "finale", "whatsapp"]:
        app = MockAppSession(initial_screen=scr)
        app.click_memories_back()
        assert app.active_screen == scr


def test_b09_frequent_gallery_visits():
    """T2.9.3: Visiting memories gallery 5 times in succession maintains state integrity."""
    app = MockAppSession(initial_screen="menu")
    for _ in range(5):
        app.select_hub_card("memories")
        app.click_memories_back()
    assert app.active_screen == "menu"
    assert len(app.transition_history) == 11


def test_b09_heading_title_casing():
    """T2.9.4: Memories heading uses Title Case and contains 'Captured'."""
    assert EXPECTED_MEMORIES_HEADING.istitle()
    assert "Captured" in EXPECTED_MEMORIES_HEADING
    assert "Memories" in EXPECTED_MEMORIES_HEADING


def test_b09_music_state_persistence():
    """T2.9.5: Entering memories with music on maintains music continuously."""
    app = MockAppSession(initial_screen="memories")
    app.play_music()
    assert app.is_playing_music is True
    app.click_memories_back()
    assert app.is_playing_music is True
