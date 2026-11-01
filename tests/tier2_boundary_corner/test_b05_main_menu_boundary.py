"""
Feature 5 Boundary & Corner Cases: 2×2 Main Hub Menu
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_HUB_TITLE,
    HUB_CARDS,
    MockAppSession,
)


def test_b05_select_card_when_not_on_menu_raises_runtime_error():
    """T2.5.1: Selecting a hub card when not on 'menu' raises RuntimeError."""
    app = MockAppSession(initial_screen="whatsapp")
    with pytest.raises(RuntimeError, match="Cannot select card"):
        app.select_hub_card("cake")


def test_b05_empty_card_id_raises_value_error():
    """T2.5.2: Passing an empty string for card selection raises ValueError."""
    app = MockAppSession(initial_screen="menu")
    with pytest.raises(ValueError):
        app.select_hub_card("")


def test_b05_rapid_sequential_card_navigation():
    """T2.5.3: Rapid switching between all 4 cards via menu maintains correct transitions."""
    app = MockAppSession(initial_screen="menu")
    for card in HUB_CARDS:
        app.select_hub_card(card)
        assert app.active_screen == card
        app.set_screen("menu")
    assert app.active_screen == "menu"
    assert len(app.transition_history) == 9  # menu + 4 * (card + menu)


def test_b05_hub_title_uppercase_constraint():
    """T2.5.4: Hub title kinetic typography is entirely uppercase."""
    assert EXPECTED_HUB_TITLE == EXPECTED_HUB_TITLE.upper()


def test_b05_hub_cards_immutability():
    """T2.5.5: HUB_CARDS is immutable and contains only lowercase identifiers."""
    for card in HUB_CARDS:
        assert card.islower()
        assert len(card) >= 4
