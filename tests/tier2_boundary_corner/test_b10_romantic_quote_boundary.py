"""
Feature 10 Boundary & Corner Cases: Romantic Memory Quote & Vignette
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_MEMORIES_QUOTE,
    MockAppSession,
)


def test_b10_quote_apostrophe_verbatim():
    """T2.10.1: Quote contains contraction 'can't' rather than 'cannot'."""
    assert "can't" in EXPECTED_MEMORIES_QUOTE
    assert "cannot" not in EXPECTED_MEMORIES_QUOTE


def test_b10_quote_punctuation_ending():
    """T2.10.2: Quote ends with a period."""
    assert EXPECTED_MEMORIES_QUOTE.endswith(".")


def test_b10_quote_character_length_bounds():
    """T2.10.3: Quote string length falls within 40 to 80 characters."""
    length = len(EXPECTED_MEMORIES_QUOTE)
    assert 40 <= length <= 80


def test_b10_quote_view_does_not_mutate_candles():
    """T2.10.4: Visiting quote view leaves candle state unaffected."""
    app = MockAppSession(initial_screen="memories")
    app.is_candle_blown = True
    app.click_memories_back()
    assert app.is_candle_blown is True


def test_b10_quote_word_count_bounds():
    """T2.10.5: Quote consists of exactly 9 words."""
    words = EXPECTED_MEMORIES_QUOTE.split()
    assert len(words) == 9
