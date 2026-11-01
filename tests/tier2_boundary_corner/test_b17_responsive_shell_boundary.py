"""
Feature 17 Boundary & Corner Cases: Responsive Shell
"""

import pytest
from tests.e2e_harness import (
    VIEWPORT_DESKTOP,
    VIEWPORT_HD,
    VIEWPORT_IPHONE,
    VIEWPORT_MOBILE_SE,
    VIEWPORT_TABLET,
)


def test_b17_all_viewport_dimensions_positive():
    """T2.17.1: All viewport width and height values are positive integers."""
    for vp in [VIEWPORT_IPHONE, VIEWPORT_HD, VIEWPORT_DESKTOP, VIEWPORT_MOBILE_SE, VIEWPORT_TABLET]:
        assert isinstance(vp[0], int) and vp[0] > 0
        assert isinstance(vp[1], int) and vp[1] > 0


def test_b17_mobile_viewports_are_portrait():
    """T2.17.2: Mobile viewports have height > width (portrait orientation)."""
    for vp in [VIEWPORT_IPHONE, VIEWPORT_HD, VIEWPORT_MOBILE_SE]:
        assert vp[1] > vp[0], f"Viewport {vp} is not portrait"


def test_b17_desktop_viewport_is_landscape():
    """T2.17.3: Desktop viewport has width > height (landscape orientation)."""
    assert VIEWPORT_DESKTOP[0] > VIEWPORT_DESKTOP[1]


def test_b17_mobile_minimum_width_boundary():
    """T2.17.4: Minimum supported mobile width is at least 320px."""
    assert VIEWPORT_MOBILE_SE[0] >= 320


def test_b17_tablet_aspect_ratio_bounds():
    """T2.17.5: Tablet aspect ratio is within standard 4:3 bounds."""
    ratio = VIEWPORT_TABLET[1] / VIEWPORT_TABLET[0]
    assert 1.2 <= ratio <= 1.4  # ~1.33
