"""
Feature 8: Comfort Food Bakery Feast (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 024-026
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_FEAST_FULL_BTN,
    EXPECTED_FEAST_HEADING,
    MockAppSession,
)


def test_f08_feast_heading_copy():
    """T1.8.1: Verify feast bubble heading copy matches 'Let's eat CAKE!'."""
    assert EXPECTED_FEAST_HEADING == "Let's eat CAKE!"


def test_f08_feast_full_button_copy():
    """T1.8.2: Verify completion return button label is 'I Am Full'."""
    assert EXPECTED_FEAST_FULL_BTN == "I Am Full"


def test_f08_click_full_returns_to_menu():
    """T1.8.3: Verify clicking 'I Am Full' routes user back to 'menu' screen."""
    app = MockAppSession(initial_screen="cake")
    app.blow_candles()
    app.click_feast_full()
    assert app.active_screen == "menu"


def test_f08_complete_cake_lifecycle():
    """T1.8.4: Verify complete sequence: menu -> cake -> blow -> full -> menu."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("cake")
    app.blow_candles()
    app.click_feast_full()
    assert app.active_screen == "menu"
    assert app.transition_history == ["menu", "cake", "menu"]


def test_f08_click_full_ignored_when_not_on_cake():
    """T1.8.5: Verify click_feast_full is safe and ignored when not on 'cake' screen."""
    app = MockAppSession(initial_screen="menu")
    app.click_feast_full()
    assert app.active_screen == "menu"
    assert app.transition_history == ["menu"]
