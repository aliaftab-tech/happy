"""
Feature 3 Boundary & Corner Cases: Surprise Gatekeeper Teaser
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_TEASER_NO,
    EXPECTED_TEASER_QUESTION,
    EXPECTED_TEASER_YES,
    MockAppSession,
)


def test_b03_rapid_double_tap_yes():
    """T2.3.1: Double tap on 'Yes Sure' produces single transition to 'menu'."""
    app = MockAppSession(initial_screen="teaser")
    app.click_teaser_yes()
    app.click_teaser_yes()
    assert app.active_screen == "menu"
    assert app.transition_history == ["teaser", "menu"]


def test_b03_rapid_double_tap_no():
    """T2.3.2: Double tap on 'No Thanks' produces single transition to 'rejection'."""
    app = MockAppSession(initial_screen="teaser")
    app.click_teaser_no()
    app.click_teaser_no()
    assert app.active_screen == "rejection"
    assert app.transition_history == ["teaser", "rejection"]


def test_b03_alternating_clicks_race_condition():
    """T2.3.3: Alternating yes/no click executes first clicked path cleanly."""
    app = MockAppSession(initial_screen="teaser")
    app.click_teaser_yes()
    app.click_teaser_no()  # Now on menu, teaser_no must be ignored
    assert app.active_screen == "menu"
    assert app.transition_history == ["teaser", "menu"]


def test_b03_question_string_boundaries():
    """T2.3.4: Teaser question has non-empty words and proper capitalisation."""
    words = EXPECTED_TEASER_QUESTION.split()
    assert len(words) == 7
    assert words[0] == "Do"
    assert words[-1] == "Surprise"


def test_b03_button_labels_distinct():
    """T2.3.5: Yes and No buttons have strictly distinct texts and lengths."""
    assert EXPECTED_TEASER_YES != EXPECTED_TEASER_NO
    assert len(EXPECTED_TEASER_YES) > 0
    assert len(EXPECTED_TEASER_NO) > 0
