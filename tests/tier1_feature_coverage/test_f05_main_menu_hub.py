"""
Feature 5: 2×2 Main Hub Menu (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 015-017
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_HUB_TITLE,
    HUB_CARDS,
    MockAppSession,
)


def test_f05_hub_title_heading():
    """T1.5.1: Verify kinetic typography title matches 'THESE ARE FOR YOU CUTIE'."""
    assert EXPECTED_HUB_TITLE == "THESE ARE FOR YOU CUTIE"
    assert "CUTIE" in EXPECTED_HUB_TITLE


def test_f05_hub_cards_count():
    """T1.5.2: Verify 4 squircle cards exist in the hub menu."""
    assert len(HUB_CARDS) == 4
    assert set(HUB_CARDS) == {"cake", "memories", "letter", "finale"}


def test_f05_hub_card_navigation_cake():
    """T1.5.3: Verify clicking 'cake' card transitions from 'menu' to 'cake'."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("cake")
    assert app.active_screen == "cake"


def test_f05_hub_card_navigation_all_cards():
    """T1.5.4: Verify selecting each valid card navigates to its respective screen."""
    for card in HUB_CARDS:
        app = MockAppSession(initial_screen="menu")
        app.select_hub_card(card)
        assert app.active_screen == card


def test_f05_hub_invalid_card_raises_error():
    """T1.5.5: Verify selecting an invalid card raises ValueError and keeps screen state intact."""
    app = MockAppSession(initial_screen="menu")
    with pytest.raises(ValueError, match="Unknown card"):
        app.select_hub_card("invalid_card_xyz")
    assert app.active_screen == "menu"
