#!/usr/bin/env python3
"""
Root E2E Test Suite Launcher
Romantic Birthday Surprise Web Application
Delegates directly to tests/run_tests.py
"""

import os
import subprocess
import sys

if __name__ == "__main__":
    tests_runner = os.path.join(os.path.dirname(__file__), "tests", "run_tests.py")
    res = subprocess.run([sys.executable, tests_runner, *sys.argv[1:]])
    sys.exit(res.returncode)
