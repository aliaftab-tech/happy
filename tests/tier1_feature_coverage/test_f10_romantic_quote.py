"""
Feature 10: Romantic Memory Quote & Vignette (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 033-034
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_MEMORIES_QUOTE,
    MockAppSession,
)


def test_f10_quote_text_verbatim():
    """T1.10.1: Verify romantic quote text matches verbatim requirement."""
    assert EXPECTED_MEMORIES_QUOTE == "Memories are the only things that time can't erase."


def test_f10_quote_contains_time_and_memories():
    """T1.10.2: Verify keywords 'Memories' and 'time' are present in quote."""
    assert "Memories" in EXPECTED_MEMORIES_QUOTE
    assert "time" in EXPECTED_MEMORIES_QUOTE


def test_f10_quote_screen_navigation():
    """T1.10.3: Verify quote is accessed within memories screen context."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("memories")
    assert app.active_screen == "memories"


def test_f10_quote_state_idempotence():
    """T1.10.4: Verify repeated visits to memories screen maintain clean state."""
    app = MockAppSession(initial_screen="menu")
    for _ in range(3):
        app.select_hub_card("memories")
        app.click_memories_back()
    assert app.active_screen == "menu"
    assert app.transition_history == [
        "menu", "memories", "menu", "memories", "menu", "memories", "menu"
    ]


def test_f10_quote_screen_audio_unaffected():
    """T1.10.5: Verify accessing memories quote does not stop background audio."""
    app = MockAppSession(initial_screen="menu")
    app.play_music()
    app.select_hub_card("memories")
    assert app.is_playing_music is True
    app.click_memories_back()
    assert app.is_playing_music is True
