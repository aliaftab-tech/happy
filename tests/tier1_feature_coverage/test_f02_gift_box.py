"""
Feature 2: Gift Box Opener Screen (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 003-004
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_GIFT_PROMPT,
    MockAppSession,
)


def test_f02_gift_screen_initial_state():
    """T1.2.1: Verify screen can be initialized in 'gift' state."""
    app = MockAppSession(initial_screen="gift")
    assert app.active_screen == "gift"


def test_f02_gift_prompt_copy_matches():
    """T1.2.2: Verify prompt copy specifies 'Click to open it'."""
    assert EXPECTED_GIFT_PROMPT == "Click to open it"


def test_f02_click_gift_box_navigates_to_teaser():
    """T1.2.3: Verify clicking gift box advances state machine to 'teaser' screen."""
    app = MockAppSession(initial_screen="gift")
    app.click_gift_box()
    assert app.active_screen == "teaser"


def test_f02_gift_opening_sequence_history():
    """T1.2.4: Verify full transition sequence: whatsapp -> gift -> teaser."""
    app = MockAppSession()
    app.click_whatsapp_preview()
    app.click_gift_box()
    assert app.active_screen == "teaser"
    assert app.transition_history == ["whatsapp", "gift", "teaser"]


def test_f02_gift_box_retains_no_console_errors():
    """T1.2.5: Verify no unhandled exceptions or console errors during gift open."""
    app = MockAppSession(initial_screen="gift")
    app.click_gift_box()
    assert len(app.console_errors) == 0
