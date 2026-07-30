import argparse
import os
import sys
import subprocess
from tracker.streak_manager import StreakManager
from tracker.git_helper import GitHelper

# Challenge Registry mapping Day numbers to metadata and paths
CHALLENGES = {
    1: {
        "title": "Decorators & Telemetry",
        "week": 1,
        "module": "Core Python Mastery",
        "path": "challenges/week1_core_mastery/day01_decorators_logging",
        "test": "challenges/week1_core_mastery/day01_decorators_logging/test_day01.py"
    },
    2: {
        "title": "Generators & Log Streaming",
        "week": 1,
        "module": "Core Python Mastery",
        "path": "challenges/week1_core_mastery/day02_generators_memory",
        "test": "challenges/week1_core_mastery/day02_generators_memory/test_day02.py"
    },
    3: {
        "title": "AsyncIO Concurrency & Semaphore Rate Limiting",
        "week": 1,
        "module": "Core Python Mastery",
        "path": "challenges/week1_core_mastery/day03_asyncio_concurrency",
        "test": "challenges/week1_core_mastery/day03_asyncio_concurrency/test_day03.py"
    },
    4: {
        "title": "Context Managers & Transaction Resource Guards",
        "week": 1,
        "module": "Core Python Mastery",
        "path": "challenges/week1_core_mastery/day04_context_managers",
        "test": "challenges/week1_core_mastery/day04_context_managers/test_day04.py"
    },
    5: {
        "title": "Dataclasses & Pydantic Request Validation",
        "week": 1,
        "module": "Core Python Mastery",
        "path": "challenges/week1_core_mastery/day05_dataclasses_pydantic",
        "test": "challenges/week1_core_mastery/day05_dataclasses_pydantic/test_day05.py"
    },
    6: {
        "title": "O(1) LRU Cache Implementation",
        "week": 2,
        "module": "System Design & Patterns",
        "path": "challenges/week2_system_design_patterns/day06_lru_cache",
        "test": "challenges/week2_system_design_patterns/day06_lru_cache/test_day06.py"
    },
    7: {
        "title": "Sliding Window API Rate Limiter",
        "week": 2,
        "module": "System Design & Patterns",
        "path": "challenges/week2_system_design_patterns/day07_rate_limiter",
        "test": "challenges/week2_system_design_patterns/day07_rate_limiter/test_day07.py"
    },
    8: {
        "title": "Factory & Strategy Design Patterns",
        "week": 2,
        "module": "System Design & Patterns",
        "path": "challenges/week2_system_design_patterns/day08_factory_strategy_pattern",
        "test": "challenges/week2_system_design_patterns/day08_factory_strategy_pattern/test_day08.py"
    }
}

def setup_encoding():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

def print_header():
    print("=" * 65)
    try:
        print(" 🚀 DAILY PYTHON BACKEND DEVELOPER UPSKILLING & GIT PUSH TRACKER")
    except UnicodeEncodeError:
        print(" [>] DAILY PYTHON BACKEND DEVELOPER UPSKILLING & GIT PUSH TRACKER")
    print("=" * 65)

def display_status(sm: StreakManager):
    status = sm.get_status()
    print_header()
    try:
        print(f" 🔥 Current Streak     : {status['streak']} Days")
        print(f" 🎯 Total Completed   : {status['total_completed']} / {len(CHALLENGES)} Challenges")
        print(f" 📅 Last Activity Date: {status['last_completed_date'] or 'None (Start today!)'}")
        print("-" * 65)
        print(" 📚 AVAILABLE CHALLENGES:")
        for day, meta in CHALLENGES.items():
            done_icon = "[x]" if day in status["completed_days"] else "[ ]"
            print(f"   {done_icon} Day {day:02d}: {meta['title']} ({meta['module']})")
    except UnicodeEncodeError:
        print(f" Current Streak     : {status['streak']} Days")
        print(f" Total Completed   : {status['total_completed']} / {len(CHALLENGES)} Challenges")
        print(f" Last Activity Date: {status['last_completed_date'] or 'None (Start today!)'}")
        print("-" * 65)
        print(" AVAILABLE CHALLENGES:")
        for day, meta in CHALLENGES.items():
            done_icon = "[x]" if day in status["completed_days"] else "[ ]"
            print(f"   {done_icon} Day {day:02d}: {meta['title']} ({meta['module']})")
    print("=" * 65)

def run_challenge_tests(day_number: int) -> bool:
    if day_number not in CHALLENGES:
        print(f"❌ Error: Day {day_number} challenge not found.")
        return False

    test_file = CHALLENGES[day_number]["test"]
    if not os.path.exists(test_file):
        print(f"❌ Error: Test file '{test_file}' not found.")
        return False

    print(f"\n🧪 Running pytest for Day {day_number:02d}: {CHALLENGES[day_number]['title']}...")
    result = subprocess.run([sys.executable, "-m", "pytest", test_file, "-v"])
    return result.returncode == 0

def complete_and_push(day_number: int, sm: StreakManager):
    if day_number not in CHALLENGES:
        print(f"❌ Error: Day {day_number} challenge not found.")
        return

    print(f"\n⚡ Validating solution for Day {day_number:02d}...")
    success = run_challenge_tests(day_number)
    if not success:
        print("\n❌ Tests failed! Please fix solution/starter before committing and pushing.")
        return

    # Update streak
    data = sm.mark_completed(day_number)
    print(f"\n🎉 Great job! Day {day_number} completed. Current Streak: {data['streak']} 🔥")

    # Push to git
    title = CHALLENGES[day_number]["title"]
    print("\n📦 Pushing progress to GitHub...")
    git_success, msg = GitHelper.commit_and_push(day_number, title, data["streak"])
    if git_success:
        print(f"✅ {msg}")
    else:
        print(f"⚠️ Git status: {msg}")

def main():
    setup_encoding()
    sm = StreakManager()
    parser = argparse.ArgumentParser(description="Daily Git Push Python Backend Tracker")
    parser.add_argument("--status", action="store_true", help="View current streak & challenge status")
    parser.add_argument("--test", type=int, help="Run pytest for a specific day challenge (e.g. --test 1)")
    parser.add_argument("--complete", type=int, help="Test, mark complete, commit and push a day (e.g. --complete 1)")
    parser.add_argument("--all-tests", action="store_true", help="Run pytest across all days")

    args = parser.parse_args()

    if args.status or (len(sys.argv) == 1):
        display_status(sm)
    elif args.test:
        run_challenge_tests(args.test)
    elif args.complete:
        complete_and_push(args.complete, sm)
    elif args.all_tests:
        print("🧪 Running all repository tests...")
        subprocess.run([sys.executable, "-m", "pytest", "-v"])

if __name__ == "__main__":
    main()
