"""Git rebase-and-push with session branch fallback.

Aligned with upstream rebase-push.ts + ADR 0055:
  - Triple retry: pull --rebase --autostash, exponential backoff
  - Session branch fallback on persistent conflict
  - Branch cleanup for stale session branches (keep 3 days)
"""

from __future__ import annotations

import random
import re
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass
class RebasePushResult:
    status: str  # pushed | branch-fallback | nothing-to-push | error
    branch: str | None = None
    error: str | None = None


SESSION_BRANCH_RE = re.compile(r"^session-.+")


def _run_git(args: list[str], cwd: str, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git"] + args,
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=cwd,
        env={"GIT_TERMINAL_PROMPT": "0", "HOME": str(Path.home())},
    )


def count_unpushed_commits(cwd: str) -> int:
    """Count commits ahead of upstream."""
    try:
        r = _run_git(["rev-list", "--count", "@{upstream}..HEAD"], cwd)
        return int(r.stdout.strip()) if r.returncode == 0 else 0
    except (subprocess.TimeoutExpired, ValueError):
        return 0


def get_head_commit(cwd: str) -> str:
    """Get current HEAD commit hash."""
    try:
        r = _run_git(["rev-parse", "HEAD"], cwd)
        return r.stdout.strip() if r.returncode == 0 else ""
    except subprocess.TimeoutExpired:
        return ""


def get_current_branch(cwd: str) -> str:
    """Get current branch name."""
    try:
        r = _run_git(["branch", "--show-current"], cwd)
        return r.stdout.strip() if r.returncode == 0 else "main"
    except subprocess.TimeoutExpired:
        return "main"


def rebase_and_push(
    cwd: str,
    session_id: str,
    max_retries: int = 3,
    target_branch: str | None = None,
) -> RebasePushResult:
    """Rebase onto remote and push, with session branch fallback.

    Flow (aligned with upstream):
      1. Check for unpushed commits
      2. If on a session branch, switch to main
      3. Try pull --rebase --autostash up to max_retries times
      4. On persistent failure, create session-{id} branch and push there
    """
    unpushed = count_unpushed_commits(cwd)
    if unpushed == 0:
        return RebasePushResult(status="nothing-to-push")

    current = get_current_branch(cwd)
    if target_branch is None:
        target_branch = "main" if SESSION_BRANCH_RE.match(current) else current

    if current != target_branch:
        r = _run_git(["checkout", target_branch], cwd)
        if r.returncode != 0:
            return RebasePushResult(status="error", error=f"checkout failed: {r.stderr}")

    for attempt in range(max_retries):
        r = _run_git(
            ["pull", "--rebase", "--autostash", "origin", target_branch],
            cwd,
            timeout=120,
        )
        if r.returncode == 0:
            push_r = _run_git(["push", "origin", target_branch], cwd, timeout=120)
            if push_r.returncode == 0:
                return RebasePushResult(status="pushed")
            if attempt < max_retries - 1:
                backoff = (2 ** attempt) + random.uniform(0, 1)
                time.sleep(backoff)
                continue
        else:
            _run_git(["rebase", "--abort"], cwd)
            if attempt < max_retries - 1:
                backoff = (2 ** attempt) + random.uniform(0, 1)
                time.sleep(backoff)

    fallback_branch = f"session-{session_id}"
    _run_git(["checkout", "-b", fallback_branch], cwd)
    push_r = _run_git(["push", "origin", fallback_branch], cwd, timeout=120)

    _run_git(["checkout", target_branch], cwd)
    _run_git(["branch", "-D", fallback_branch], cwd)

    if push_r.returncode == 0:
        return RebasePushResult(status="branch-fallback", branch=fallback_branch)
    else:
        return RebasePushResult(
            status="error",
            error=f"fallback push failed: {push_r.stderr}",
            branch=fallback_branch,
        )


def cleanup_session_branches(
    cwd: str,
    keep_days: int = 3,
    dry_run: bool = False,
) -> list[str]:
    """Remove remote session branches older than keep_days (ADR 0055)."""
    deleted: list[str] = []

    r = _run_git(["branch", "-r", "--list", "origin/session-*"], cwd)
    if r.returncode != 0:
        return deleted

    cutoff = time.time() - (keep_days * 86400)

    for line in r.stdout.strip().splitlines():
        branch = line.strip()
        if not branch:
            continue

        local_name = branch.replace("origin/", "")
        log_r = _run_git(
            ["log", "-1", "--format=%ct", branch],
            cwd,
        )
        if log_r.returncode != 0:
            continue

        try:
            commit_time = int(log_r.stdout.strip())
        except ValueError:
            continue

        if commit_time < cutoff:
            if not dry_run:
                _run_git(["push", "origin", "--delete", local_name], cwd, timeout=30)
            deleted.append(local_name)

    return deleted


def auto_commit_orphaned_files(cwd: str, session_id: str) -> bool:
    """Commit any uncommitted files left by a worker session."""
    status = _run_git(["status", "--porcelain"], cwd)
    if not status.stdout.strip():
        return False

    _run_git(["add", "-A"], cwd)
    _run_git(
        ["commit", "-m", f"[fleet/{session_id}] auto-commit orphaned files"],
        cwd,
    )
    return True
