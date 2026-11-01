"""
Tier 3: Cross-Feature Combinations & State Transitions (Pairwise & Integration)
Requirements: TEST_INFRA.md & PROJECT.md
"""

import pytest
from tests.e2e_harness import (
    HUB_CARDS,
    VALID_SCREENS,
    MockAppSession,
)


def test_t3_01_intro_pipeline_continuity():
    """T3.1: Sequential transition whatsapp -> gift -> teaser."""
    app = MockAppSession()
    assert app.active_screen == "whatsapp"
    app.click_whatsapp_preview()
    assert app.active_screen == "gift"
    app.click_gift_box()
    assert app.active_screen == "teaser"
    assert app.transition_history == ["whatsapp", "gift", "teaser"]


def test_t3_02_rejection_branch_loopback():
    """T3.2: Rejection branch transition teaser -> rejection -> teaser."""
    app = MockAppSession(initial_screen="teaser")
    app.click_teaser_no()
    assert app.active_screen == "rejection"
    app.click_rejection_try_again()
    assert app.active_screen == "teaser"
    assert app.transition_history == ["teaser", "rejection", "teaser"]


def test_t3_03_teaser_acceptance_into_hub():
    """T3.3: Teaser acceptance transition teaser -> menu."""
    app = MockAppSession(initial_screen="teaser")
    app.click_teaser_yes()
    assert app.active_screen == "menu"
    assert app.transition_history == ["teaser", "menu"]


def test_t3_04_menu_to_cake_and_return():
    """T3.4: Menu to Cake, blow candles, return via 'I Am Full'."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("cake")
    assert app.active_screen == "cake"
    app.blow_candles()
    assert app.is_candle_blown is True
    app.click_feast_full()
    assert app.active_screen == "menu"
    assert app.transition_history == ["menu", "cake", "menu"]


def test_t3_05_menu_to_memories_and_return():
    """T3.5: Menu to Memories gallery, view polaroids, return via arrow back."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("memories")
    assert app.active_screen == "memories"
    app.click_memories_back()
    assert app.active_screen == "menu"
    assert app.transition_history == ["menu", "memories", "menu"]


def test_t3_06_menu_to_letter_and_return():
    """T3.6: Menu to Love Letter, read, return via pill Back button."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("letter")
    assert app.active_screen == "letter"
    app.click_letter_back()
    assert app.active_screen == "menu"
    assert app.transition_history == ["menu", "letter", "menu"]


def test_t3_07_menu_to_finale_and_return():
    """T3.7: Menu to Finale screen, view teddy bear, return via Home button."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("finale")
    assert app.active_screen == "finale"
    app.click_finale_home()
    assert app.active_screen == "menu"
    assert app.transition_history == ["menu", "finale", "menu"]


def test_t3_08_audio_persistence_letter_to_memories():
    """T3.8: Audio started on Letter screen persists when navigating to Memories."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("letter")
    app.play_music()
    assert app.is_playing_music is True
    app.click_letter_back()
    assert app.active_screen == "menu"
    assert app.is_playing_music is True
    app.select_hub_card("memories")
    assert app.active_screen == "memories"
    assert app.is_playing_music is True


def test_t3_09_audio_persistence_letter_to_cake_with_blow():
    """T3.9: Audio continues playing through candle blowing on cake screen."""
    app = MockAppSession(initial_screen="letter")
    app.play_music()
    app.click_letter_back()
    app.select_hub_card("cake")
    assert app.is_playing_music is True
    app.blow_candles()
    assert app.is_candle_blown is True
    assert app.is_playing_music is True
    app.click_feast_full()
    assert app.active_screen == "menu"
    assert app.is_playing_music is True


def test_t3_10_audio_persistence_letter_to_finale():
    """T3.10: Audio continues playing through finale screen and back."""
    app = MockAppSession(initial_screen="letter")
    app.play_music()
    app.click_letter_back()
    app.select_hub_card("finale")
    assert app.is_playing_music is True
    app.click_finale_home()
    assert app.active_screen == "menu"
    assert app.is_playing_music is True


def test_t3_11_cake_candle_persistence_across_all_hub_visits():
    """T3.11: Blown candle state persists across visits to all other screens."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("cake")
    app.blow_candles()
    app.click_feast_full()
    
    # Visit all other 3 hub cards
    for card in ["memories", "letter", "finale"]:
        app.select_hub_card(card)
        if card == "memories":
            app.click_memories_back()
        elif card == "letter":
            app.click_letter_back()
        elif card == "finale":
            app.click_finale_home()
        assert app.is_candle_blown is True

    # Re-visit cake
    app.select_hub_card("cake")
    assert app.is_candle_blown is True


def test_t3_12_cake_reset_and_revisit():
    """T3.12: Explicit candle reset returns cake to initial unblown condition."""
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("cake")
    app.blow_candles()
    assert app.is_candle_blown is True
    app.reset_candles()
    assert app.is_candle_blown is False
    app.click_feast_full()
    app.select_hub_card("cake")
    assert app.is_candle_blown is False


def test_t3_13_audio_toggle_off_in_letter_after_hub_visit():
    """T3.13: Starting music in letter, navigating out and back, pausing music cleanly."""
    app = MockAppSession(initial_screen="letter")
    app.toggle_vinyl_music()
    assert app.is_playing_music is True
    app.click_letter_back()
    assert app.active_screen == "menu"
    app.select_hub_card("letter")
    assert app.is_playing_music is True
    app.toggle_vinyl_music()
    assert app.is_playing_music is False


def test_t3_14_rapid_switching_cake_and_memories():
    """T3.14: Rapid interleaved switching between Cake and Memories via Menu."""
    app = MockAppSession(initial_screen="menu")
    for _ in range(4):
        app.select_hub_card("cake")
        app.click_feast_full()
        app.select_hub_card("memories")
        app.click_memories_back()
    assert app.active_screen == "menu"
    assert len(app.transition_history) == 17  # menu + 4 * 4


def test_t3_15_rapid_switching_letter_and_finale():
    """T3.15: Rapid interleaved switching between Letter and Finale via Menu."""
    app = MockAppSession(initial_screen="menu")
    for _ in range(4):
        app.select_hub_card("letter")
        app.click_letter_back()
        app.select_hub_card("finale")
        app.click_finale_home()
    assert app.active_screen == "menu"
    assert len(app.transition_history) == 17


def test_t3_16_rejection_recovery_then_full_hub_exploration():
    """T3.16: Teaser rejection -> recovery -> Hub -> visit all 4 cards in sequence."""
    app = MockAppSession()
    app.click_whatsapp_preview()
    app.click_gift_box()
    app.click_teaser_no()
    app.click_rejection_try_again()
    app.click_teaser_yes()
    assert app.active_screen == "menu"
    
    app.select_hub_card("cake")
    app.click_feast_full()
    app.select_hub_card("memories")
    app.click_memories_back()
    app.select_hub_card("letter")
    app.click_letter_back()
    app.select_hub_card("finale")
    app.click_finale_home()
    assert app.active_screen == "menu"


def test_t3_17_full_state_reset_simulation():
    """T3.17: Verifying independent new session starts with clean default state."""
    app1 = MockAppSession()
    app1.play_music()
    app1.set_screen("cake")
    app1.blow_candles()
    
    app2 = MockAppSession()
    assert app2.active_screen == "whatsapp"
    assert app2.is_candle_blown is False
    assert app2.is_playing_music is False
    assert app2.transition_history == ["whatsapp"]


def test_t3_18_screen_history_monotonicity():
    """T3.18: Transition history length grows monotonically with every valid transition."""
    app = MockAppSession()
    history_lengths = [len(app.transition_history)]
    
    steps = [
        lambda: app.click_whatsapp_preview(),
        lambda: app.click_gift_box(),
        lambda: app.click_teaser_yes(),
        lambda: app.select_hub_card("cake"),
        lambda: app.click_feast_full(),
        lambda: app.select_hub_card("finale"),
        lambda: app.click_finale_home(),
    ]
    for step in steps:
        step()
        history_lengths.append(len(app.transition_history))
        
    for i in range(len(history_lengths) - 1):
        assert history_lengths[i + 1] == history_lengths[i] + 1


def test_t3_19_all_screens_reachability():
    """T3.19: Every screen in VALID_SCREENS is reachable from initial whatsapp."""
    reached_screens = set()
    
    app = MockAppSession()
    reached_screens.add(app.active_screen)
    
    app.click_whatsapp_preview()
    reached_screens.add(app.active_screen)
    
    app.click_gift_box()
    reached_screens.add(app.active_screen)
    
    app.click_teaser_no()
    reached_screens.add(app.active_screen)
    
    app.click_rejection_try_again()
    app.click_teaser_yes()
    reached_screens.add(app.active_screen)
    
    for card in HUB_CARDS:
        app.select_hub_card(card)
        reached_screens.add(app.active_screen)
        app.set_screen("menu")
        
    assert reached_screens == VALID_SCREENS


def test_t3_20_invalid_card_selection_from_non_menu_screens():
    """T3.20: Attempting select_hub_card from all non-menu screens raises RuntimeError."""
    for scr in VALID_SCREENS - {"menu"}:
        app = MockAppSession(initial_screen=scr)
        with pytest.raises(RuntimeError, match="Cannot select card"):
            app.select_hub_card("cake")
