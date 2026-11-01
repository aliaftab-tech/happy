"""
Feature 3: Surprise Gatekeeper Screen (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 005-006
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_TEASER_NO,
    EXPECTED_TEASER_QUESTION,
    EXPECTED_TEASER_YES,
    MockAppSession,
)


def test_f03_teaser_question_matches_verbatim():
    """T1.3.1: Verify headline text contains 'Do you want to see your Surprise'."""
    assert EXPECTED_TEASER_QUESTION == "Do you want to see your Surprise"


def test_f03_teaser_buttons_labels():
    """T1.3.2: Verify action buttons are 'Yes Sure' and 'No Thanks'."""
    assert EXPECTED_TEASER_YES == "Yes Sure"
    assert EXPECTED_TEASER_NO == "No Thanks"


def test_f03_click_yes_sure_transitions_to_menu():
    """T1.3.3: Verify clicking 'Yes Sure' transitions activeScreen to 'menu'."""
    app = MockAppSession(initial_screen="teaser")
    app.click_teaser_yes()
    assert app.active_screen == "menu"


def test_f03_click_no_thanks_transitions_to_rejection():
    """T1.3.4: Verify clicking 'No Thanks' transitions activeScreen to 'rejection'."""
    app = MockAppSession(initial_screen="teaser")
    app.click_teaser_no()
    assert app.active_screen == "rejection"


def test_f03_teaser_accept_path_preserves_audio_state():
    """T1.3.5: Verify accepting surprise maintains audio context stability."""
    app = MockAppSession(initial_screen="teaser")
    assert not app.is_playing_music
    app.click_teaser_yes()
    assert app.active_screen == "menu"
    assert not app.is_playing_music
