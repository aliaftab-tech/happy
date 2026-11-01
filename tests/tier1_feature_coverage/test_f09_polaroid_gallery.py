"""
Feature 9: Scrapbook Polaroid Gallery (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 027-032
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_MEMORIES_HEADING,
    MockAppSession,
)


def test_f09_memories_heading_copy():
    """T1.9.1: Verify cursive heading is 'Captured Memories'."""
    assert EXPECTED_MEMORIES_HEADING == "Captured Memories"


def test_f09_navigate_to_memories_screen():
    """T1.9.2: Verify selecting 'memories' from menu activates memories screen."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("memories")
    assert app.active_screen == "memories"


def test_f09_memories_back_button_returns_to_menu():
    """T1.9.3: Verify clicking back button navigates from memories back to menu."""
    app = MockAppSession(initial_screen="memories")
    app.click_memories_back()
    assert app.active_screen == "menu"


def test_f09_memories_full_navigation_history():
    """T1.9.4: Verify complete roundtrip: menu -> memories -> menu."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("memories")
    app.click_memories_back()
    assert app.transition_history == ["menu", "memories", "menu"]


def test_f09_memories_back_ignored_on_other_screens():
    """T1.9.5: Verify click_memories_back does not affect other screens."""
    app = MockAppSession(initial_screen="cake")
    app.click_memories_back()
    assert app.active_screen == "cake"
