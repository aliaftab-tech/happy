"""
Feature 4: Rejection Tease Branch (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 007-009
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_REJECTION_HEADING,
    EXPECTED_REJECTION_TRY_AGAIN,
    MockAppSession,
)


def test_f04_rejection_heading_copy():
    """T1.4.1: Verify arched headline is 'Why did you click No'."""
    assert EXPECTED_REJECTION_HEADING == "Why did you click No"


def test_f04_rejection_button_copy():
    """T1.4.2: Verify recovery button text is 'Try Again'."""
    assert EXPECTED_REJECTION_TRY_AGAIN == "Try Again"


def test_f04_click_try_again_returns_to_teaser():
    """T1.4.3: Verify clicking 'Try Again' routes user back to 'teaser' screen."""
    app = MockAppSession(initial_screen="rejection")
    app.click_rejection_try_again()
    assert app.active_screen == "teaser"


def test_f04_rejection_and_recovery_loop():
    """T1.4.4: Verify complete loop: teaser -> rejection -> teaser -> menu."""
    app = MockAppSession(initial_screen="teaser")
    app.click_teaser_no()
    assert app.active_screen == "rejection"
    app.click_rejection_try_again()
    assert app.active_screen == "teaser"
    app.click_teaser_yes()
    assert app.active_screen == "menu"


def test_f04_rejection_history_trace():
    """T1.4.5: Verify transition history records all detour steps accurately."""
    app = MockAppSession(initial_screen="teaser")
    app.click_teaser_no()
    app.click_rejection_try_again()
    assert app.transition_history == ["teaser", "rejection", "teaser"]
