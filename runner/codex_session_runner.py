"""End-to-end Codex session runner.

Implements the full session lifecycle:
  1. Orient — read repo state, identify tasks
  2. Select — pick a task
  3. Execute — run through the Codex backend with tools
  4. Commit — write findings, logs, update task state

Usage:
    python -m runner.codex_session_runner --task tasks/demo_task.md
    python -m runner.codex_session_runner --scheduler
    python -m runner.codex_session_runner --orient-only
"""

from __future__ import annotations

import argparse
import datetime
import json
import shutil
import subprocess
import sys
import uuid
from pathlib import Path

from .config import CodexConfig
from .governance import ApprovalGate, ProvenanceTracker
from .openai_backend import CodexBackend, SessionResult
from .tools import TOOL_DEFINITIONS, ToolExecutor


# ── Progress bar rendering ──────────────────────────────────────────

_PHASE_LABELS = {
    "llm_thinking": "LLM 思考中",
    "tool_exec":    "执行工具",
    "finalizing":   "生成总结",
}

_TOOL_ICONS = {
    "read_file":        "📖",
    "write_file":       "✏️",
    "list_files":       "📂",
    "search_text":      "🔍",
    "run_shell":        "💻",
    "git_status":       "📊",
    "log_decision":     "📝",
    "request_approval": "🔒",
}


def _render_progress(
    turn: int,
    max_turns: int,
    phase: str,
    tool_name: str | None = None,
    tool_args_preview: str | None = None,
) -> None:
    """Print a dynamic single-line progress bar to stderr."""
    terminal_width = shutil.get_terminal_size((80, 24)).columns

    pct = min(turn / max(max_turns, 1) * 100, 99)
    if phase == "finalizing":
        pct = 100

    bar_total = 20
    filled = int(bar_total * pct / 100)
    bar = "█" * filled + "░" * (bar_total - filled)

    phase_label = _PHASE_LABELS.get(phase, phase)

    if phase == "tool_exec" and tool_name:
        icon = _TOOL_ICONS.get(tool_name, "🔧")
        detail = f"{icon} {tool_name}"
        if tool_args_preview:
            max_args_len = terminal_width - 50
            if max_args_len > 10:
                preview = tool_args_preview[:max_args_len]
                detail += f"({preview})"
    elif phase == "finalizing":
        detail = "✅ 完成"
    else:
        detail = "🧠 ..."

    line = f"\r  [{bar}] {pct:5.1f}% | 轮次 {turn}/{max_turns} | {phase_label} {detail}"

    if len(line) > terminal_width:
        line = line[:terminal_width - 1]

    print(line, end="", flush=True, file=sys.stderr)

    if phase == "finalizing":
        print(file=sys.stderr)


def _now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _generate_session_id() -> str:
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d-%H%M%S")
    short_uuid = uuid.uuid4().hex[:8]
    return f"session-{ts}-{short_uuid}"


class SessionRunner:
    """Orchestrates a single agent session end-to-end."""

    def __init__(self, config: CodexConfig, approval_policy: str = "standard"):
        self.config = config
        self.repo_root = config.repo_home
        self.tool_executor = ToolExecutor(config)
        self.backend = CodexBackend(config, tool_executor=self.tool_executor)
        self.session_id = _generate_session_id()
        self.provenance = ProvenanceTracker(self.session_id, self.repo_root)
        self.approval_gate = ApprovalGate(self.repo_root, policy=approval_policy)

    def orient(self) -> dict:
        """Phase 1: Read repo state and identify available tasks."""
        state: dict = {
            "session_id": self.session_id,
            "timestamp": _now_iso(),
            "repo_root": str(self.repo_root),
        }

        agents_md = self.repo_root / "AGENTS.md"
        if agents_md.is_file():
            content = agents_md.read_text(encoding="utf-8")
            state["agents_md_loaded"] = True
            state["agents_md_preview"] = content[:2000]
        else:
            state["agents_md_loaded"] = False

        state["git_status"] = self._get_git_status()

        tasks_files = list(self.repo_root.rglob("TASKS.md"))
        task_summary: list[dict] = []
        for tf in tasks_files:
            content = tf.read_text(encoding="utf-8", errors="replace")
            open_tasks = [
                line.strip()
                for line in content.splitlines()
                if line.strip().startswith("- [ ]")
            ]
            task_summary.append({
                "file": str(tf.relative_to(self.repo_root)),
                "total_open": len(open_tasks),
                "tasks_preview": open_tasks[:10],
            })
        state["task_files"] = task_summary

        recent_logs = self._get_recent_logs(limit=5)
        state["recent_logs"] = recent_logs

        state["skills"] = self._list_skills()

        return state

    def select_task(self, task_path: str | None = None) -> dict:
        """Phase 2: Select a task to execute.

        If task_path is provided, use that specific task.
        Otherwise, scan TASKS.md files for the highest-priority unblocked task.
        """
        if task_path:
            full_path = self.repo_root / task_path
            if not full_path.is_file():
                return {"error": f"Task file not found: {task_path}"}
            content = full_path.read_text(encoding="utf-8")
            return {
                "task_id": task_path,
                "content": content,
                "source": "explicit",
            }

        for tf in sorted(self.repo_root.rglob("TASKS.md")):
            content = tf.read_text(encoding="utf-8", errors="replace")
            for line in content.splitlines():
                stripped = line.strip()
                if not stripped.startswith("- [ ]"):
                    continue
                if "[blocked-by:" in stripped:
                    continue
                if "[in-progress:" in stripped:
                    continue
                return {
                    "task_id": str(tf.relative_to(self.repo_root)),
                    "content": stripped,
                    "source": "auto-selected",
                }

        return {"error": "No unblocked tasks found"}

    def execute(self, task: dict) -> SessionResult:
        """Phase 3 & 4: Run the Codex backend on the selected task."""
        orient_state = self.orient()
        repo_state_summary = json.dumps({
            "git_status": orient_state.get("git_status", ""),
            "open_tasks": orient_state.get("task_files", []),
            "recent_logs": orient_state.get("recent_logs", []),
        }, indent=2, default=str)

        result = self.backend.run_session(
            task_id=task.get("task_id", "unknown"),
            task_context=task.get("content", ""),
            repo_state=repo_state_summary,
            tools_registry=TOOL_DEFINITIONS,
            progress_callback=_render_progress,
        )
        return result

    def write_session_log(self, result: SessionResult) -> Path:
        """Phase 5: Write session log to logs/sessions/."""
        logs_dir = self.repo_root / "logs" / "sessions"
        logs_dir.mkdir(parents=True, exist_ok=True)

        log_data = {
            "session_id": self.session_id,
            "timestamp": _now_iso(),
            "task_id": result.task_id,
            "model": result.model,
            "turns": result.turns,
            "success": result.success,
            "error": result.error,
            "token_usage": {
                "prompt_tokens": result.token_usage.prompt_tokens,
                "completion_tokens": result.token_usage.completion_tokens,
                "total_tokens": result.token_usage.total_tokens,
            },
            "latency_seconds": round(result.latency_seconds, 2),
            "tool_calls": result.tool_calls_log,
            "output_preview": result.final_output[:2000],
        }

        log_path = logs_dir / f"{self.session_id}.json"
        log_path.write_text(
            json.dumps(log_data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        return log_path

    def write_failure_log(self, result: SessionResult) -> Path | None:
        """Write failure details if the session failed."""
        if result.success:
            return None

        failures_dir = self.repo_root / "logs" / "failures"
        failures_dir.mkdir(parents=True, exist_ok=True)

        failure_data = {
            "session_id": self.session_id,
            "timestamp": _now_iso(),
            "task_id": result.task_id,
            "error": result.error,
            "last_tool_call": result.tool_calls_log[-1] if result.tool_calls_log else None,
            "turns_before_failure": result.turns,
            "token_usage": {
                "prompt_tokens": result.token_usage.prompt_tokens,
                "completion_tokens": result.token_usage.completion_tokens,
                "total_tokens": result.token_usage.total_tokens,
            },
            "recovery_recommendation": "Review the error and last tool call. Retry with adjusted parameters or escalate.",
        }

        fail_path = failures_dir / f"failure-{self.session_id}.json"
        fail_path.write_text(
            json.dumps(failure_data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        return fail_path

    def run(self, task_path: str | None = None) -> SessionResult:
        """Full session lifecycle: orient → select → execute → commit."""
        print(f"[{self.session_id}] Starting session...")
        print(f"  Model: {self.config.model}")
        print(f"  Repo:  {self.repo_root}")

        print(f"[{self.session_id}] Phase 1: Orient")
        orient_state = self.orient()
        task_count = sum(t["total_open"] for t in orient_state.get("task_files", []))
        print(f"  Found {task_count} open tasks across {len(orient_state.get('task_files', []))} TASKS.md files")

        print(f"[{self.session_id}] Phase 2: Select task")
        task = self.select_task(task_path)
        if "error" in task:
            print(f"  ERROR: {task['error']}")
            err_result = SessionResult(
                task_id=task_path or "none",
                model=self.config.model,
                error=task["error"],
            )
            self.write_failure_log(err_result)
            return err_result

        print(f"  Selected: {task['task_id']} ({task['source']})")

        self.provenance.set_task(task.get("task_id", "unknown"))
        self.provenance.set_model(self.config.model)

        print(f"[{self.session_id}] Phase 3-4: Execute via Codex backend")
        result = self.execute(task)

        self.provenance.finalize(result)

        print(f"[{self.session_id}] Phase 5: Write logs and provenance")
        log_path = self.write_session_log(result)
        print(f"  Session log: {log_path}")

        prov_path = self.provenance.write()
        print(f"  Provenance:  {prov_path}")

        self.approval_gate.write_pending_to_queue()

        if not result.success:
            fail_path = self.write_failure_log(result)
            print(f"  Failure log: {fail_path}")
            print(f"  ERROR: {result.error}")
        else:
            print(f"  Success! {result.turns} turns, {result.token_usage.total_tokens} tokens")
            print(f"  Latency: {result.latency_seconds:.1f}s")

        return result

    def _get_git_status(self) -> str:
        try:
            proc = subprocess.run(
                ["git", "status", "--porcelain", "--branch"],
                capture_output=True, text=True, timeout=10,
                cwd=str(self.repo_root),
            )
            return proc.stdout.strip() or "(clean)"
        except Exception:
            return "(not a git repo)"

    def _get_recent_logs(self, limit: int = 5) -> list[dict]:
        logs_dir = self.repo_root / "logs" / "sessions"
        if not logs_dir.is_dir():
            return []
        log_files = sorted(logs_dir.glob("*.json"), reverse=True)[:limit]
        results = []
        for lf in log_files:
            try:
                data = json.loads(lf.read_text(encoding="utf-8"))
                results.append({
                    "file": lf.name,
                    "task_id": data.get("task_id"),
                    "success": data.get("success"),
                    "timestamp": data.get("timestamp"),
                })
            except (json.JSONDecodeError, KeyError):
                pass
        return results

    def _list_skills(self) -> list[str]:
        skills_dir = self.repo_root / "skills"
        if not skills_dir.is_dir():
            return []
        return sorted(d.name for d in skills_dir.iterdir() if d.is_dir())


def main() -> None:
    parser = argparse.ArgumentParser(
        description="OpenAkari-Codex Session Runner",
    )
    parser.add_argument(
        "--task",
        type=str,
        default=None,
        help="Path to a specific task file (relative to repo root)",
    )
    parser.add_argument(
        "--orient-only",
        action="store_true",
        help="Only run the orient phase and print state",
    )
    parser.add_argument(
        "--scheduler",
        action="store_true",
        help="Run in scheduler mode (auto-select tasks)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without calling the API",
    )
    args = parser.parse_args()

    try:
        config = CodexConfig.from_env()
    except EnvironmentError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)

    errors = config.validate()
    if errors:
        for err in errors:
            print(f"Validation error: {err}", file=sys.stderr)
        sys.exit(1)

    runner = SessionRunner(config)

    if args.orient_only:
        state = runner.orient()
        print(json.dumps(state, indent=2, default=str))
        return

    if args.dry_run:
        print("=== DRY RUN ===")
        state = runner.orient()
        task = runner.select_task(args.task)
        print(f"Would execute task: {json.dumps(task, indent=2)}")
        print(f"Model: {config.model}")
        print(f"Max turns: {config.max_turns}")
        return

    result = runner.run(task_path=args.task)
    sys.exit(0 if result.success else 1)


if __name__ == "__main__":
    main()
