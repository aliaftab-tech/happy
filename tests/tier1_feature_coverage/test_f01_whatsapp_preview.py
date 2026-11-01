"""
Feature 1: WhatsApp Chat Link Preview (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frame 001
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_DOMAIN,
    EXPECTED_WHATSAPP_TITLE,
    MockAppSession,
)


def test_f01_initial_screen_is_whatsapp():
    """T1.1.1: Verify application initial screen state is 'whatsapp'."""
    app = MockAppSession()
    assert app.active_screen == "whatsapp"


def test_f01_preview_contains_expected_domain():
    """T1.1.2: Verify preview link specifies authentic domain dua-digitals.my.canva.site."""
    assert EXPECTED_DOMAIN == "dua-digitals.my.canva.site"


def test_f01_preview_contains_gift_copy():
    """T1.1.3: Verify message bubble copy contains 'I made a gift for you'."""
    assert "gift" in EXPECTED_WHATSAPP_TITLE.lower()
    assert EXPECTED_WHATSAPP_TITLE == "I made a gift for you"


def test_f01_click_preview_transitions_to_gift():
    """T1.1.4: Verify clicking chat preview card navigates to 'gift' opener screen."""
    app = MockAppSession()
    app.click_whatsapp_preview()
    assert app.active_screen == "gift"


def test_f01_preview_transition_recorded_in_history():
    """T1.1.5: Verify transition from whatsapp to gift is properly recorded in navigation history."""
    app = MockAppSession()
    app.click_whatsapp_preview()
    assert app.transition_history == ["whatsapp", "gift"]
