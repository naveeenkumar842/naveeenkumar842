#!/usr/bin/env python3
"""
Root entry point for the Daily Git Push Backend Python Tracker.
Usage:
    python daily_push.py                 # View progress dashboard
    python daily_push.py --status        # View streak & challenge list
    python daily_push.py --test 1        # Run pytest for Day 1 challenge
    python daily_push.py --complete 1    # Test, mark complete, commit & push Day 1
    python daily_push.py --all-tests     # Run pytest across all daily test suites
"""

import sys
from tracker.cli import main

if __name__ == "__main__":
    main()
