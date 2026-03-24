"""Atomic task claiming for fleet workers.

Aligned with upstream task-claims.ts:
  - Scheduler claims a task *before* spawning the worker
  - Claims stored in fleet/claims.json protected by fcntl file lock
  - release on worker completion (success or failure)
"""

from __future__ import annotations

import json
import time
import uuid
from pathlib import Path
from typing import Any

from .file_lock import file_lock


class TaskClaimStore:
    """Manages atomic task claims backed by a JSON file."""

    def __init__(self, repo_root: Path):
        self._store_dir = repo_root / ".fleet"
        self._store_dir.mkdir(parents=True, exist_ok=True)
        self._claims_file = self._store_dir / "claims.json"

    def _load(self) -> dict[str, Any]:
        if not self._claims_file.is_file():
            return {"claims": {}}
        try:
            return json.loads(self._claims_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {"claims": {}}

    def _save(self, data: dict[str, Any]) -> None:
        self._claims_file.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def try_claim(
        self,
        task_id: str,
        worker_id: str,
        session_id: str,
        project: str = "",
    ) -> str | None:
        """Atomically claim a task. Returns claim_id on success, None if already claimed."""
        with file_lock(self._claims_file):
            data = self._load()
            claims = data.get("claims", {})

            for claim in claims.values():
                if claim.get("task_id") == task_id and claim.get("active"):
                    return None

            claim_id = f"claim-{uuid.uuid4().hex[:12]}"
            claims[claim_id] = {
                "task_id": task_id,
                "worker_id": worker_id,
                "session_id": session_id,
                "project": project,
                "claimed_at": time.time(),
                "active": True,
            }
            data["claims"] = claims
            self._save(data)
            return claim_id

    def release_claim(self, claim_id: str) -> None:
        """Release a specific claim."""
        with file_lock(self._claims_file):
            data = self._load()
            claims = data.get("claims", {})
            if claim_id in claims:
                claims[claim_id]["active"] = False
                claims[claim_id]["released_at"] = time.time()
                data["claims"] = claims
                self._save(data)

    def release_agent_claims(self, session_id: str) -> None:
        """Release all claims held by a session (cleanup on exit)."""
        with file_lock(self._claims_file):
            data = self._load()
            claims = data.get("claims", {})
            changed = False
            for claim in claims.values():
                if claim.get("session_id") == session_id and claim.get("active"):
                    claim["active"] = False
                    claim["released_at"] = time.time()
                    changed = True
            if changed:
                data["claims"] = claims
                self._save(data)

    def get_active_claims(self) -> dict[str, dict[str, Any]]:
        """Return all currently active claims, keyed by claim_id."""
        with file_lock(self._claims_file):
            data = self._load()
            return {
                cid: claim
                for cid, claim in data.get("claims", {}).items()
                if claim.get("active")
            }

    def get_claimed_task_ids(self) -> set[str]:
        """Return set of task_ids that are currently claimed."""
        active = self.get_active_claims()
        return {c["task_id"] for c in active.values()}

    def get_active_per_project(self) -> dict[str, int]:
        """Count active claims per project."""
        active = self.get_active_claims()
        counts: dict[str, int] = {}
        for claim in active.values():
            proj = claim.get("project", "")
            counts[proj] = counts.get(proj, 0) + 1
        return counts

    def cleanup_stale(self, max_age_seconds: float = 7200) -> int:
        """Remove claims older than max_age that are still active (stuck workers)."""
        now = time.time()
        removed = 0
        with file_lock(self._claims_file):
            data = self._load()
            claims = data.get("claims", {})
            for claim in claims.values():
                if claim.get("active") and (now - claim.get("claimed_at", 0)) > max_age_seconds:
                    claim["active"] = False
                    claim["released_at"] = now
                    claim["release_reason"] = "stale_cleanup"
                    removed += 1
            if removed:
                data["claims"] = claims
                self._save(data)
        return removed
