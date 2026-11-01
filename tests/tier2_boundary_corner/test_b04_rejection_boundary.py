"""
Feature 4 Boundary & Corner Cases: Rejection Tease Branch
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_REJECTION_HEADING,
    EXPECTED_REJECTION_TRY_AGAIN,
    MockAppSession,
)


def test_b04_rapid_try_again_clicks_idempotent():
    """T2.4.1: Multiple rapid clicks on 'Try Again' result in exactly one transition to teaser."""
    app = MockAppSession(initial_screen="rejection")
    for _ in range(5):
        app.click_rejection_try_again()
    assert app.active_screen == "teaser"
    assert app.transition_history == ["rejection", "teaser"]


def test_b04_deep_rejection_loop_stress():
    """T2.4.2: Repeated cycle (10x) of rejecting and retrying maintains state consistency."""
    app = MockAppSession(initial_screen="teaser")
    for _ in range(10):
        app.click_teaser_no()
        assert app.active_screen == "rejection"
        app.click_rejection_try_again()
        assert app.active_screen == "teaser"
    assert app.active_screen == "teaser"
    assert len(app.transition_history) == 21


def test_b04_try_again_ignored_on_other_screens():
    """T2.4.3: Calling try_again from 'menu' does not change screen."""
    app = MockAppSession(initial_screen="menu")
    app.click_rejection_try_again()
    assert app.active_screen == "menu"
    assert app.transition_history == ["menu"]


def test_b04_heading_tokens_integrity():
    """T2.4.4: Rejection heading tokens match expected words."""
    words = EXPECTED_REJECTION_HEADING.split()
    assert words == ["Why", "did", "you", "click", "No"]


def test_b04_try_again_button_tokens():
    """T2.4.5: Try again button text contains exactly 'Try Again'."""
    assert EXPECTED_REJECTION_TRY_AGAIN == "Try Again"
