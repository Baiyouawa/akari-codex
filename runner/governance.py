"""Governance and provenance tracking for Codex sessions.

Records:
  - task source and session metadata
  - model used and token consumption
  - commands executed and files touched
  - decisions made during the session
  - approvals granted or denied

All records are written to the repo for full auditability.
"""

from __future__ import annotations

import datetime
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .openai_backend import SessionResult


def _now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class ProvenanceRecord:
    """Full provenance trail for a single session."""
    session_id: str
    timestamp: str = field(default_factory=_now_iso)
    task_source: str = ""
    model: str = ""
    commands_executed: list[str] = field(default_factory=list)
    files_read: list[str] = field(default_factory=list)
    files_written: list[str] = field(default_factory=list)
    decisions_made: list[str] = field(default_factory=list)
    approvals_requested: list[dict[str, str]] = field(default_factory=list)
    approvals_granted: list[str] = field(default_factory=list)
    approvals_denied: list[str] = field(default_factory=list)
    token_usage: dict[str, int] = field(default_factory=dict)
    latency_seconds: float = 0.0
    success: bool = False
    error: str | None = None
    humanize_reviews: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "session_id": self.session_id,
            "timestamp": self.timestamp,
            "task_source": self.task_source,
            "model": self.model,
            "commands_executed": self.commands_executed,
            "files_read": self.files_read,
            "files_written": self.files_written,
            "decisions_made": self.decisions_made,
            "approvals": {
                "requested": self.approvals_requested,
                "granted": self.approvals_granted,
                "denied": self.approvals_denied,
            },
            "token_usage": self.token_usage,
            "latency_seconds": self.latency_seconds,
            "success": self.success,
            "error": self.error,
            "humanize_reviews": self.humanize_reviews,
        }


class ProvenanceTracker:
    """Tracks and records provenance for tool calls during a session."""

    def __init__(self, session_id: str, repo_root: Path):
        self.record = ProvenanceRecord(session_id=session_id)
        self.repo_root = repo_root

    def set_task(self, task_source: str) -> None:
        self.record.task_source = task_source

    def set_model(self, model: str) -> None:
        self.record.model = model

    def log_humanize_review(
        self,
        review_type: str,
        issues_found: int,
        has_critical: bool,
        summary: str,
        duration_seconds: float,
    ) -> None:
        """Record a Humanize/Codex review in the provenance trail."""
        self.record.humanize_reviews.append({
            "type": review_type,
            "timestamp": _now_iso(),
            "issues_found": issues_found,
            "has_critical": has_critical,
            "summary": summary[:500],
            "duration_seconds": round(duration_seconds, 2),
        })

    def log_tool_call(self, tool_name: str, args: dict[str, Any]) -> None:
        if tool_name == "run_shell":
            self.record.commands_executed.append(args.get("command", ""))
        elif tool_name == "read_file":
            self.record.files_read.append(args.get("path", ""))
        elif tool_name == "write_file":
            self.record.files_written.append(args.get("path", ""))
        elif tool_name == "log_decision":
            self.record.decisions_made.append(args.get("title", ""))
        elif tool_name == "request_approval":
            self.record.approvals_requested.append({
                "type": args.get("action_type", ""),
                "description": args.get("description", ""),
            })

    def finalize(self, result: SessionResult) -> None:
        self.record.token_usage = {
            "prompt_tokens": result.token_usage.prompt_tokens,
            "completion_tokens": result.token_usage.completion_tokens,
            "total_tokens": result.token_usage.total_tokens,
        }
        self.record.latency_seconds = result.latency_seconds
        self.record.success = result.success
        self.record.error = result.error

    def write(self) -> Path:
        artifacts_dir = self.repo_root / "artifacts"
        artifacts_dir.mkdir(parents=True, exist_ok=True)

        path = artifacts_dir / f"provenance-{self.record.session_id}.json"
        path.write_text(
            json.dumps(self.record.to_dict(), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        return path


class ApprovalGate:
    """Checks and enforces approval boundaries.

    Actions are classified as:
      - AUTO: execute without approval
      - APPROVAL_REQUIRED: must be approved before execution
      - DENIED: always blocked
    """

    AUTO_ACTIONS = frozenset({
        "read_file", "list_files", "search_text", "git_status",
    })

    APPROVAL_REQUIRED_PATTERNS = (
        "git push", "git force", "rm -rf", "rm -r",
        "deploy", "publish", "release",
    )

    ALWAYS_DENIED = (
        "rm -rf /", "mkfs", "dd if=", "shutdown", "reboot",
        "curl", "wget",
    )

    def __init__(self, repo_root: Path, policy: str = "standard"):
        self.repo_root = repo_root
        self.policy = policy
        self._pending_approvals: list[dict] = []

    def check_tool(self, tool_name: str, args: dict[str, Any]) -> str:
        """Returns 'auto', 'approval_required', or 'denied'."""
        if tool_name in self.AUTO_ACTIONS:
            return "auto"

        if tool_name == "write_file":
            path = args.get("path", "")
            if any(p in path for p in ("AGENTS.md", "decisions/", "infra/")):
                return "approval_required" if self.policy == "standard" else "auto"
            return "auto"

        if tool_name == "run_shell":
            cmd = args.get("command", "").lower()
            for pattern in self.ALWAYS_DENIED:
                if pattern in cmd:
                    return "denied"
            for pattern in self.APPROVAL_REQUIRED_PATTERNS:
                if pattern in cmd:
                    return "approval_required"
            return "auto"

        if tool_name == "request_approval":
            return "auto"

        if tool_name == "log_decision":
            return "auto"

        return "approval_required"

    def check_shell_command(self, command: str) -> str:
        """Convenience method for shell commands."""
        return self.check_tool("run_shell", {"command": command})

    def queue_approval(self, action_type: str, description: str) -> None:
        self._pending_approvals.append({
            "type": action_type,
            "description": description,
            "timestamp": _now_iso(),
            "status": "pending",
        })

    def get_pending(self) -> list[dict]:
        return list(self._pending_approvals)

    def write_pending_to_queue(self) -> None:
        if not self._pending_approvals:
            return
        queue_file = self.repo_root / "APPROVAL_QUEUE.md"
        if queue_file.is_file():
            content = queue_file.read_text(encoding="utf-8")
        else:
            content = "# Approval Queue\n\nItems requiring human review.\n"

        for item in self._pending_approvals:
            content += f"""
---

### [{item['status'].upper()}] {item['type']}

**Requested:** {item['timestamp']}
**Description:** {item['description']}
**Status:** {item['status']}

"""
        queue_file.write_text(content, encoding="utf-8")
        self._pending_approvals.clear()
