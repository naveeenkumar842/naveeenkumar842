import subprocess
import sys
from typing import Tuple

class GitHelper:
    @staticmethod
    def run_command(cmd: list) -> Tuple[bool, str]:
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            return True, result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return False, e.stderr.strip() or e.stdout.strip()

    @classmethod
    def is_git_repo(cls) -> bool:
        success, _ = cls.run_command(["git", "rev-parse", "--is-inside-work-tree"])
        return success

    @classmethod
    def commit_and_push(cls, day_number: int, challenge_title: str, streak: int) -> Tuple[bool, str]:
        if not cls.is_git_repo():
            return False, "Not a git repository. Initialize git with 'git init' first."

        # Stage all changes
        success, out = cls.run_command(["git", "add", "."])
        if not success:
            return False, f"Failed to stage changes: {out}"

        # Create conventional commit message
        commit_msg = f"feat(day-{day_number:02d}): complete {challenge_title} [streak: {streak}🔥]"
        
        # Commit
        success, out = cls.run_command(["git", "commit", "-m", commit_msg])
        if not success and "nothing to commit" not in out:
            return False, f"Commit failed: {out}"

        # Get current branch
        _, branch = cls.run_command(["git", "branch", "--show-current"])
        branch = branch or "main"

        # Push to remote
        success, out = cls.run_command(["git", "push", "origin", branch])
        if not success:
            # Fallback to plain push if tracking isn't set up yet
            success, out = cls.run_command(["git", "push", "-u", "origin", branch])
            if not success:
                return False, f"Git push failed (configured remote origin may be missing or authentication required): {out}"

        return True, f"Successfully committed and pushed Day {day_number}! Commit: '{commit_msg}'"
