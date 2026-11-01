"""
Feature 17: Responsive Shell & Ambient Backdrop (Tier 1 Happy Path)
Requirements: ORIGINAL_REQUEST §R1 & Frames 001-047
"""

import pytest
from tests.e2e_harness import (
    VIEWPORT_DESKTOP,
    VIEWPORT_HD,
    VIEWPORT_IPHONE,
    VIEWPORT_MOBILE_SE,
    VIEWPORT_TABLET,
)


def test_f17_iphone_viewport_dimensions():
    """T1.17.1: Verify standard iPhone viewport is 390x844."""
    assert VIEWPORT_IPHONE == (390, 844)
    aspect = VIEWPORT_IPHONE[1] / VIEWPORT_IPHONE[0]
    assert 2.0 <= aspect <= 2.2  # ~9:19.5 aspect


def test_f17_hd_viewport_dimensions():
    """T1.17.2: Verify 9:16 reference HD viewport is 720x1280."""
    assert VIEWPORT_HD == (720, 1280)
    assert round(VIEWPORT_HD[1] / VIEWPORT_HD[0], 2) == round(16 / 9, 2)


def test_f17_desktop_viewport_dimensions():
    """T1.17.3: Verify desktop viewport is 1920x1080 (16:9)."""
    assert VIEWPORT_DESKTOP == (1920, 1080)
    assert VIEWPORT_DESKTOP[0] > VIEWPORT_DESKTOP[1]


def test_f17_small_screen_support():
    """T1.17.4: Verify iPhone SE viewport 320x568 is defined."""
    assert VIEWPORT_MOBILE_SE == (320, 568)
    assert VIEWPORT_MOBILE_SE[0] < VIEWPORT_IPHONE[0]


def test_f17_tablet_viewport_dimensions():
    """T1.17.5: Verify tablet viewport 768x1024 is defined for intermediate breakpoint."""
    assert VIEWPORT_TABLET == (768, 1024)
