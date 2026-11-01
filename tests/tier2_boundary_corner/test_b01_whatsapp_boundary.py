"""
Feature 1 Boundary & Corner Cases: WhatsApp Preview
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_DOMAIN,
    EXPECTED_WHATSAPP_TITLE,
    MockAppSession,
)


def test_b01_rapid_multiple_clicks_idempotent():
    """T2.1.1: Rapid repeated clicks on preview do not advance beyond 'gift'."""
    app = MockAppSession()
    for _ in range(5):
        app.click_whatsapp_preview()
    assert app.active_screen == "gift"
    assert app.transition_history == ["whatsapp", "gift"]


def test_b01_click_ignored_on_other_screens():
    """T2.1.2: Calling preview click when not on whatsapp screen is a no-op."""
    app = MockAppSession(initial_screen="menu")
    app.click_whatsapp_preview()
    assert app.active_screen == "menu"
    assert app.transition_history == ["menu"]


def test_b01_set_invalid_screen_raises_value_error():
    """T2.1.3: Setting an unrecognized screen name raises ValueError."""
    app = MockAppSession()
    with pytest.raises(ValueError, match="Invalid screen state"):
        app.set_screen("non_existent_screen")


def test_b01_domain_structure_validation():
    """T2.1.4: Domain has valid TLD and subdomains."""
    parts = EXPECTED_DOMAIN.split(".")
    assert len(parts) >= 3
    assert parts[-1] == "site"
    assert parts[0] == "dua-digitals"


def test_b01_empty_initial_screen_rejection():
    """T2.1.5: Empty string as screen raises ValueError."""
    app = MockAppSession()
    with pytest.raises(ValueError):
        app.set_screen("")
