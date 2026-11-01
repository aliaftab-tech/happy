"""
Feature 14 Boundary & Corner Cases: Finale Navigation
"""

import pytest
from tests.e2e_harness import (
    MockAppSession,
)


def test_b14_rapid_home_clicks_idempotent():
    """T2.14.1: Rapid clicks on Home button on finale produce single transition."""
    app = MockAppSession(initial_screen="finale")
    for _ in range(5):
        app.click_finale_home()
    assert app.active_screen == "menu"
    assert app.transition_history == ["finale", "menu"]


def test_b14_home_click_blocked_on_other_screens():
    """T2.14.2: Calling click_finale_home from other screens is a no-op."""
    for scr in ["whatsapp", "gift", "teaser", "cake", "memories"]:
        app = MockAppSession(initial_screen=scr)
        app.click_finale_home()
        assert app.active_screen == scr


def test_b14_interleaved_cake_and_finale_navigation():
    """T2.14.3: Switching between cake and finale via home and menu works smoothly."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("finale")
    app.click_finale_home()
    assert app.active_screen == "menu"
    app.select_hub_card("cake")
    app.click_feast_full()
    assert app.active_screen == "menu"


def test_b14_history_integrity_on_home_return():
    """T2.14.4: Exact history sequence recorded for finale navigation."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("finale")
    app.click_finale_home()
    assert app.transition_history == ["menu", "finale", "menu"]


def test_b14_zero_console_errors_across_home_navigation():
    """T2.14.5: Zero errors logged during finale to menu navigation."""
    app = MockAppSession(initial_screen="finale")
    app.click_finale_home()
    assert len(app.console_errors) == 0
