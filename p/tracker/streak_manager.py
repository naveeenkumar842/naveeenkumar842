import json
import os
from datetime import datetime, timedelta
from typing import Dict, Any, List

PROGRESS_FILE = ".progress.json"

def get_default_progress() -> Dict[str, Any]:
    return {
        "streak": 0,
        "last_completed_date": None,
        "completed_days": [],
        "total_completed": 0,
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }

class StreakManager:
    def __init__(self, progress_path: str = PROGRESS_FILE):
        self.progress_path = progress_path
        self.data = self._load_progress()

    def _load_progress(self) -> Dict[str, Any]:
        if not os.path.exists(self.progress_path):
            return get_default_progress()
        try:
            with open(self.progress_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return get_default_progress()

    def _save_progress(self) -> None:
        with open(self.progress_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def get_status(self) -> Dict[str, Any]:
        self._update_streak_integrity()
        return self.data

    def _update_streak_integrity(self) -> None:
        last_date_str = self.data.get("last_completed_date")
        if not last_date_str:
            return

        today = datetime.now().date()
        last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()

        # If more than 1 day has passed without activity, reset streak
        if (today - last_date).days > 1:
            self.data["streak"] = 0
            self._save_progress()

    def mark_completed(self, day_number: int) -> Dict[str, Any]:
        today_str = datetime.now().strftime("%Y-%m-%d")
        today = datetime.now().date()

        if day_number not in self.data["completed_days"]:
            self.data["completed_days"].append(day_number)
            self.data["completed_days"].sort()
            self.data["total_completed"] += 1

        last_date_str = self.data.get("last_completed_date")
        if last_date_str:
            last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()
            if last_date == today - timedelta(days=1):
                self.data["streak"] += 1
            elif last_date == today:
                # Same day completion, keep current streak
                pass
            else:
                self.data["streak"] = 1
        else:
            self.data["streak"] = 1

        self.data["last_completed_date"] = today_str
        self._save_progress()
        return self.data
