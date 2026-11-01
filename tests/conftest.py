"""
Pytest configuration and global fixtures for Romantic Birthday Surprise E2E suite.
"""

import os
import pytest
from tests.e2e_harness import (
    E2EBrowserDriver,
    MockAppSession,
    VIEWPORT_IPHONE,
    VIEWPORT_HD,
    VIEWPORT_DESKTOP,
)


@pytest.fixture(scope="function")
def mock_app():
    """Provides a fresh isolated mock application state session."""
    return MockAppSession(initial_screen="whatsapp")


@pytest.fixture(scope="function")
def driver():
    """Provides a managed E2E browser driver session."""
    drv = E2EBrowserDriver()
    drv.start()
    yield drv
    drv.stop()


@pytest.fixture
def iphone_viewport():
    return VIEWPORT_IPHONE


@pytest.fixture
def hd_viewport():
    return VIEWPORT_HD


@pytest.fixture
def desktop_viewport():
    return VIEWPORT_DESKTOP
