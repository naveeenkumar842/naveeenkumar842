import os
import json
import pytest
from tracker.streak_manager import StreakManager

def test_streak_manager_initialization(tmp_path):
    progress_file = tmp_path / ".progress.json"
    sm = StreakManager(progress_path=str(progress_file))
    status = sm.get_status()

    assert status["streak"] == 0
    assert status["total_completed"] == 0
    assert status["completed_days"] == []

def test_mark_completed(tmp_path):
    progress_file = tmp_path / ".progress.json"
    sm = StreakManager(progress_path=str(progress_file))

    status = sm.mark_completed(1)
    assert status["streak"] == 1
    assert status["total_completed"] == 1
    assert 1 in status["completed_days"]
    assert status["last_completed_date"] is not None

def test_multiple_completions(tmp_path):
    progress_file = tmp_path / ".progress.json"
    sm = StreakManager(progress_path=str(progress_file))

    sm.mark_completed(1)
    sm.mark_completed(2)
    status = sm.get_status()

    assert status["total_completed"] == 2
    assert status["completed_days"] == [1, 2]
