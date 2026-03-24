"""File-based locking using fcntl for atomic fleet operations.

Protects shared resources (claims.json, TASKS.md, idle-cooldown.json)
from concurrent access by multiple fleet workers.
"""

from __future__ import annotations

import fcntl
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Generator


class LockTimeout(Exception):
    """Raised when a lock cannot be acquired within the timeout."""


@contextmanager
def file_lock(
    path: Path | str,
    *,
    timeout_seconds: float = 10.0,
    poll_interval: float = 0.05,
) -> Generator[None, None, None]:
    """Acquire an exclusive file lock using fcntl.flock.

    The lock file is created alongside the target: ``<path>.lock``.
    On timeout, raises ``LockTimeout``.
    """
    lock_path = Path(f"{path}.lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)

    fd = None
    deadline = time.monotonic() + timeout_seconds
    try:
        fd = open(lock_path, "w")  # noqa: SIM115
        while True:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except (OSError, BlockingIOError):
                if time.monotonic() >= deadline:
                    raise LockTimeout(
                        f"Could not acquire lock on {lock_path} "
                        f"within {timeout_seconds}s"
                    )
                time.sleep(poll_interval)
        yield
    finally:
        if fd is not None:
            try:
                fcntl.flock(fd, fcntl.LOCK_UN)
            except OSError:
                pass
            fd.close()
