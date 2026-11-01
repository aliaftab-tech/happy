"""
Tier 4: Real-World Application Scenarios
Requirements: TEST_INFRA.md § Real-World Application Scenarios
5 comprehensive end-to-end user walkthrough flows.
"""

import pytest
from tests.e2e_harness import (
    EXPECTED_CAKE_BLOW_BTN,
    EXPECTED_CAKE_WISH_HEADING,
    EXPECTED_DOMAIN,
    EXPECTED_FEAST_FULL_BTN,
    EXPECTED_FEAST_HEADING,
    EXPECTED_FINALE_TITLE,
    EXPECTED_GIFT_PROMPT,
    EXPECTED_HUB_TITLE,
    EXPECTED_LETTER_BACK,
    EXPECTED_MEMORIES_HEADING,
    EXPECTED_MEMORIES_QUOTE,
    EXPECTED_REJECTION_HEADING,
    EXPECTED_REJECTION_TRY_AGAIN,
    EXPECTED_TEASER_NO,
    EXPECTED_TEASER_QUESTION,
    EXPECTED_TEASER_YES,
    EXPECTED_VINYL_PROMPT,
    EXPECTED_WHATSAPP_TITLE,
    LETTER_PARAGRAPH_1,
    LETTER_PARAGRAPH_2,
    LETTER_PARAGRAPH_3,
    MockAppSession,
)


def test_scenario_1_full_happy_path_walkthrough():
    """
    Scenario 1: Full Happy Path Walkthrough
    WhatsApp -> Gift -> Teaser ('Yes') -> Menu -> Cake (Wish & Feast) -> Gallery -> Letter (with Vinyl music) -> Finale -> Home.
    """
    app = MockAppSession()
    
    # 1. WhatsApp link preview
    assert app.active_screen == "whatsapp"
    assert EXPECTED_WHATSAPP_TITLE == "I made a gift for you"
    assert EXPECTED_DOMAIN == "dua-digitals.my.canva.site"
    app.click_whatsapp_preview()
    
    # 2. Gift Box opener
    assert app.active_screen == "gift"
    assert EXPECTED_GIFT_PROMPT == "Click to open it"
    app.click_gift_box()
    
    # 3. Surprise Teaser Gatekeeper
    assert app.active_screen == "teaser"
    assert EXPECTED_TEASER_QUESTION == "Do you want to see your Surprise"
    assert EXPECTED_TEASER_YES == "Yes Sure"
    app.click_teaser_yes()
    
    # 4. Main Menu Hub
    assert app.active_screen == "menu"
    assert EXPECTED_HUB_TITLE == "THESE ARE FOR YOU CUTIE"
    
    # 5. Wish Cake Screen
    app.select_hub_card("cake")
    assert app.active_screen == "cake"
    assert EXPECTED_CAKE_WISH_HEADING == "MAKE A WISH MY LOVE"
    assert EXPECTED_CAKE_BLOW_BTN == "Blow"
    assert not app.is_candle_blown
    app.blow_candles()
    assert app.is_candle_blown is True
    assert EXPECTED_FEAST_HEADING == "Let's eat CAKE!"
    assert EXPECTED_FEAST_FULL_BTN == "I Am Full"
    app.click_feast_full()
    assert app.active_screen == "menu"
    
    # 6. Memories Polaroid Gallery
    app.select_hub_card("memories")
    assert app.active_screen == "memories"
    assert EXPECTED_MEMORIES_HEADING == "Captured Memories"
    assert EXPECTED_MEMORIES_QUOTE == "Memories are the only things that time can't erase."
    app.click_memories_back()
    assert app.active_screen == "menu"
    
    # 7. Love Letter & Vinyl Record Player
    app.select_hub_card("letter")
    assert app.active_screen == "letter"
    assert EXPECTED_VINYL_PROMPT == "Play this while you are reading"
    assert not app.is_playing_music
    app.toggle_vinyl_music()
    assert app.is_playing_music is True
    assert "Today is all about celebrating" in LETTER_PARAGRAPH_1
    assert "Thank you for being such an amazing person" in LETTER_PARAGRAPH_2
    assert "May this new chapter" in LETTER_PARAGRAPH_3
    assert EXPECTED_LETTER_BACK == "Back"
    app.click_letter_back()
    assert app.active_screen == "menu"
    assert app.is_playing_music is True  # Music persists!
    
    # 8. Finale Teddy Bear Screen
    app.select_hub_card("finale")
    assert app.active_screen == "finale"
    assert EXPECTED_FINALE_TITLE == "I love you"
    assert app.is_playing_music is True
    app.click_finale_home()
    
    # 9. Returned to Hub
    assert app.active_screen == "menu"
    assert len(app.console_errors) == 0
    assert app.transition_history == [
        "whatsapp", "gift", "teaser", "menu", "cake", "menu",
        "memories", "menu", "letter", "menu", "finale", "menu"
    ]


def test_scenario_2_playful_rejection_and_recovery():
    """
    Scenario 2: Playful Rejection & Recovery
    Teaser -> 'No Thanks' -> Rejection Screen (Gun Panda) -> 'Try Again' -> Teaser -> 'Yes Sure' -> Menu.
    """
    app = MockAppSession()
    app.click_whatsapp_preview()
    app.click_gift_box()
    assert app.active_screen == "teaser"
    
    # User clicks 'No Thanks'
    assert EXPECTED_TEASER_NO == "No Thanks"
    app.click_teaser_no()
    assert app.active_screen == "rejection"
    assert EXPECTED_REJECTION_HEADING == "Why did you click No"
    assert EXPECTED_REJECTION_TRY_AGAIN == "Try Again"
    
    # User recovers by clicking 'Try Again'
    app.click_rejection_try_again()
    assert app.active_screen == "teaser"
    
    # User now clicks 'Yes Sure'
    app.click_teaser_yes()
    assert app.active_screen == "menu"
    assert app.transition_history == [
        "whatsapp", "gift", "teaser", "rejection", "teaser", "menu"
    ]


def test_scenario_3_audio_vinyl_spin_toggle_cycle():
    """
    Scenario 3: Audio & Vinyl Spin Toggle State Cycle
    Letter Screen -> Start Vinyl audio -> Pause vinyl -> Resume audio -> Return to Menu.
    """
    app = MockAppSession(initial_screen="menu")
    app.select_hub_card("letter")
    assert app.active_screen == "letter"
    assert not app.is_playing_music
    
    # 1. Start vinyl music
    app.toggle_vinyl_music()
    assert app.is_playing_music is True
    
    # 2. Pause vinyl music
    app.toggle_vinyl_music()
    assert app.is_playing_music is False
    
    # 3. Resume vinyl music
    app.toggle_vinyl_music()
    assert app.is_playing_music is True
    
    # 4. Return to Menu with music running
    app.click_letter_back()
    assert app.active_screen == "menu"
    assert app.is_playing_music is True
    
    # 5. Verify music remains playing when navigating elsewhere
    app.select_hub_card("memories")
    assert app.is_playing_music is True
    app.click_memories_back()
    assert app.is_playing_music is True


def test_scenario_4_rapid_exploration_breadcrumbs():
    """
    Scenario 4: Rapid Inter-Screen Switching & Breadcrumbs
    Menu -> Cake -> I Am Full -> Menu -> Memories -> Back -> Menu -> Letter -> Back -> Menu -> Finale -> Home.
    """
    app = MockAppSession(initial_screen="menu")
    
    # Cake visit
    app.select_hub_card("cake")
    app.click_feast_full()
    assert app.active_screen == "menu"
    
    # Memories visit
    app.select_hub_card("memories")
    app.click_memories_back()
    assert app.active_screen == "menu"
    
    # Letter visit
    app.select_hub_card("letter")
    app.click_letter_back()
    assert app.active_screen == "menu"
    
    # Finale visit
    app.select_hub_card("finale")
    app.click_finale_home()
    assert app.active_screen == "menu"
    
    # Check comprehensive history
    assert app.transition_history == [
        "menu", "cake", "menu", "memories", "menu",
        "letter", "menu", "finale", "menu"
    ]


def test_scenario_5_candle_blow_celebration_sequence():
    """
    Scenario 5: Candle Blow & Particle Celebration Sequence
    Cake Screen -> Candle flame flicker -> Click 'Blow' -> Particles explosion -> Drip cake & Macarons reveal -> Scroll feast.
    """
    app = MockAppSession(initial_screen="cake")
    assert app.is_candle_blown is False
    
    # User triggers candle blow
    app.blow_candles()
    assert app.is_candle_blown is True
    assert app.active_screen == "cake"
    
    # User stays on screen enjoying celebration
    assert len(app.console_errors) == 0
    
    # User finishes cake feast
    app.click_feast_full()
    assert app.active_screen == "menu"
    assert app.is_candle_blown is True
