"""Fleet worker executor: single worker lifecycle.

Aligned with upstream fleet-executor.ts:
  1. Receive task assignment (FleetExecutionOpts)
  2. Create isolated CodexConfig with write_scope
  3. Run agent session via CodexBackend
  4. Auto-commit orphaned files
  5. Rebase and push (triple retry + session branch fallback)
  6. Release task claim
  7. Return FleetWorkerResult
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from multiprocessing import Queue
from pathlib import Path
from typing import Any

from .config import FleetConfig, FleetTask, FleetWorkerResult, SkillType, WorkerRole
from .dashboard import FleetProgressEvent
from .rebase_push import auto_commit_orphaned_files, get_head_commit, rebase_and_push
from .task_claims import TaskClaimStore

logger = logging.getLogger("fleet.executor")


@dataclass
class FleetExecutionOpts:
    """Input to a single fleet worker execution."""

    task: FleetTask
    session_id: str
    claim_id: str
    prompt: str
    repo_root: Path
    worker_role: WorkerRole = WorkerRole.DEFAULT
    max_turns: int = 64
    timeout_seconds: int = 900


def _make_progress_callback(
    opts: FleetExecutionOpts,
    event_queue: Queue | None,
) -> Any:
    """Create a ProgressCallback that sends events to the dashboard queue.

    Throttling: consecutive 'thinking' events for the same turn are suppressed
    so the dashboard is not flooded when the LLM streams for a long time.
    tool_exec events are always forwarded (they represent real state changes).
    """
    if event_queue is None:
        return None

    wid = opts.session_id.rsplit("-", 2)[0] if "-" in opts.session_id else opts.session_id
    _last_sent: dict[str, Any] = {"phase": None, "turn": -1}

    def _callback(
        turn: int,
        max_turns: int,
        phase: str,
        tool_name: str | None = None,
        tool_args_preview: str | None = None,
    ) -> None:
        event_type = "thinking" if phase == "llm_thinking" else (
            "tool_exec" if phase == "tool_exec" else "done"
        )

        if event_type == "thinking" and _last_sent["phase"] == "thinking" and _last_sent["turn"] == turn:
            return

        _last_sent["phase"] = event_type
        _last_sent["turn"] = turn

        try:
            event_queue.put_nowait(FleetProgressEvent(
                worker_id=wid,
                session_id=opts.session_id,
                project=opts.task.project,
                event_type=event_type,
                turn=turn,
                max_turns=max_turns,
                tool_name=tool_name,
                tool_args_preview=tool_args_preview,
            ))
        except Exception:
            pass

    return _callback


def execute_fleet_worker(
    opts: FleetExecutionOpts,
    fleet_config: FleetConfig,
    claims: TaskClaimStore,
    codex_config: Any | None = None,
    event_queue: Queue | None = None,
) -> FleetWorkerResult:
    """Execute a single fleet worker session.

    This runs in a subprocess — each worker gets its own CodexBackend,
    ToolExecutor, and SessionRunner instances.
    """
    from runner.config import CodexConfig
    from runner.openai_backend import CodexBackend
    from runner.tools import TOOL_DEFINITIONS, ToolExecutor

    start_time = time.time()
    result = FleetWorkerResult(
        task_id=opts.task.task_id,
        project=opts.task.project,
        session_id=opts.session_id,
        ok=False,
        skill_type=opts.task.skill_type,
        worker_role=opts.worker_role,
    )

    wid = opts.session_id.rsplit("-", 2)[0] if "-" in opts.session_id else opts.session_id

    def _send_event(event_type: str, message: str = "", **kwargs: Any) -> None:
        if event_queue is None:
            return
        try:
            event_queue.put_nowait(FleetProgressEvent(
                worker_id=wid,
                session_id=opts.session_id,
                project=opts.task.project,
                event_type=event_type,
                message=message,
                task_text=opts.task.text,
                **kwargs,
            ))
        except Exception:
            pass

    _send_event("spawn", task_text=opts.task.text, max_turns=opts.max_turns)

    cwd = str(opts.repo_root)
    head_before = get_head_commit(cwd)
    result.head_before = head_before

    try:
        if codex_config is None:
            codex_config = CodexConfig.from_env()

        scoped_config = codex_config.with_write_scope(
            f"projects/{opts.task.project}"
        )
        scoped_config = _override_turns(scoped_config, opts.max_turns)

        tool_executor = ToolExecutor(scoped_config)
        backend = CodexBackend(scoped_config, tool_executor=tool_executor)

        progress_cb = _make_progress_callback(opts, event_queue)

        logger.info(
            "Worker %s starting task %s (project=%s, skill=%s)",
            opts.session_id,
            opts.task.task_id[:8],
            opts.task.project,
            opts.task.skill_type,
        )

        session_result = backend.run_session(
            task_id=opts.task.task_id,
            task_context=opts.prompt,
            tools_registry=TOOL_DEFINITIONS,
            progress_callback=progress_cb,
        )

        result.turns = session_result.turns
        result.total_tokens = session_result.token_usage.total_tokens
        _save_fleet_session_log(opts, session_result, opts.repo_root)

        blocked, blocked_reason = _detect_blocked(
            session_result, opts, opts.repo_root
        )
        result.blocked = blocked
        result.blocked_reason = blocked_reason

        if session_result.success:
            _send_event("chatter", message=f"任务执行完毕，{result.turns}轮，提交中...")
            auto_commit_orphaned_files(cwd, opts.session_id)

            push_result = rebase_and_push(cwd, opts.session_id)
            result.push_result = push_result.status

            result.head_after = get_head_commit(cwd)
            result.ok = True

            written = _extract_written_files(session_result.tool_calls_log)
            elapsed = time.time() - start_time

            done_msg = "ok (blocked)" if blocked else "ok"
            _send_event(
                "done", message=done_msg,
                deliverables=written,
                total_tokens=result.total_tokens,
                duration_seconds=elapsed,
            )

            logger.info(
                "Worker %s completed task %s: turns=%d tokens=%d push=%s files=%d%s",
                opts.session_id,
                opts.task.task_id[:8],
                result.turns,
                result.total_tokens,
                result.push_result,
                len(written),
                f" BLOCKED: {blocked_reason[:80]}" if blocked else "",
            )
        else:
            result.error = session_result.error
            elapsed = time.time() - start_time
            _send_event(
                "error", message=result.error or "unknown error",
                duration_seconds=elapsed,
            )
            logger.warning(
                "Worker %s failed task %s: %s",
                opts.session_id,
                opts.task.task_id[:8],
                result.error,
            )

    except Exception as e:
        result.error = f"{type(e).__name__}: {e}"
        _send_event("error", message=result.error)
        logger.exception("Worker %s crashed", opts.session_id)

    finally:
        result.duration_seconds = time.time() - start_time

        try:
            if opts.claim_id:
                claims.release_claim(opts.claim_id)
            claims.release_agent_claims(opts.session_id)
        except Exception:
            logger.exception("Failed to release claims for %s", opts.session_id)

    return result


_BLOCKED_KEYWORDS = (
    "blocked", "blocker", "cannot proceed", "cannot complete",
    "阻塞", "无法继续", "无法完成", "需要审批", "approval needed",
)


def _detect_blocked(
    session_result: Any,
    opts: FleetExecutionOpts,
    repo_root: Path,
) -> tuple[bool, str]:
    """Detect if a worker session ended in a blocked state.

    Checks the final output text and any log files written by the worker
    for blocked-related keywords. Returns (is_blocked, reason).
    """
    output = (session_result.final_output or "").lower()
    for kw in _BLOCKED_KEYWORDS:
        if kw in output:
            reason = _extract_blocked_reason(session_result.final_output or "")
            return True, reason

    written = _extract_written_files(session_result.tool_calls_log)
    for fpath in written:
        full = repo_root / fpath if not Path(fpath).is_absolute() else Path(fpath)
        if not full.is_file():
            continue
        try:
            content = full.read_text(errors="replace")[:4000].lower()
        except Exception:
            continue
        if "outcome: blocked" in content or "## blocker" in content.lower():
            reason = _extract_blocked_reason(content)
            return True, reason

    return False, ""


def _extract_blocked_reason(text: str) -> str:
    """Extract a concise blocked reason from output text."""
    import re
    for pattern in (
        r"## Blocker\s*\n(.*?)(?:\n##|\Z)",
        r"Blocker:\s*(.+)",
        r"blocked[:\s]+(.{10,200})",
    ):
        m = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if m:
            return m.group(1).strip()[:300]
    return text[:200].strip()


def _save_fleet_session_log(
    opts: FleetExecutionOpts,
    session_result: Any,
    repo_root: Path,
    *,
    is_idle: bool = False,
) -> None:
    """Append this agent's work into a per-task session log file.

    Multiple agents on the same task_id (or project) append to the same
    JSON file.  Each entry is tagged with the worker/agent ID so reviews
    can distinguish who did what.
    """
    import datetime
    import json

    logs_dir = repo_root / "logs" / "sessions"
    logs_dir.mkdir(parents=True, exist_ok=True)

    task_slug = (
        opts.task.task_id.replace("/", "_").replace(" ", "-")[:60]
        if opts.task.task_id
        else "unknown"
    )
    log_path = logs_dir / f"fleet-{opts.task.project}-{task_slug}.jsonl"

    wid = opts.session_id.rsplit("-", 2)[0] if "-" in opts.session_id else opts.session_id

    entry = {
        "agent_id": wid,
        "session_id": opts.session_id,
        "project": opts.task.project,
        "task_id": opts.task.task_id,
        "task_text": opts.task.text,
        "timestamp": datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=8))
        ).strftime("%Y-%m-%d %H:%M:%S CST"),
        "model": "gpt-5.4",
        "turns": session_result.turns,
        "success": session_result.success,
        "error": session_result.error,
        "is_idle": is_idle,
        "token_usage": {
            "prompt_tokens": session_result.token_usage.prompt_tokens,
            "completion_tokens": session_result.token_usage.completion_tokens,
            "total_tokens": session_result.token_usage.total_tokens,
        },
        "tool_calls_count": len(session_result.tool_calls_log),
        "deliverables": _extract_written_files(session_result.tool_calls_log),
        "output_preview": (session_result.final_output or "")[:1000],
    }

    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception:
        logger.warning("Failed to write session log to %s", log_path)


def _extract_written_files(tool_calls_log: list[dict[str, Any]]) -> list[str]:
    """Extract unique file paths written during a session from tool call history."""
    seen: set[str] = set()
    result: list[str] = []
    for entry in tool_calls_log:
        if entry.get("tool") in ("write_file", "log_decision"):
            path = entry.get("args", {}).get("path", "")
            if path and path not in seen:
                seen.add(path)
                result.append(path)
    return result


def _override_turns(config: Any, max_turns: int) -> Any:
    """Create a config copy with overridden max_turns."""
    from dataclasses import replace
    return replace(config, max_turns=max_turns)


def execute_idle_worker(
    session_id: str,
    prompt: str,
    exploration_type: str,
    project: str,
    repo_root: Path,
    fleet_config: FleetConfig,
    claims: TaskClaimStore,
    codex_config: Any | None = None,
    event_queue: Queue | None = None,
) -> FleetWorkerResult:
    """Execute an idle exploration session (ADR 0048).

    Similar to regular workers but:
      - No task claim needed
      - Results marked as is_idle=True
      - Shorter max_turns
    """
    from runner.config import CodexConfig
    from runner.openai_backend import CodexBackend
    from runner.tools import TOOL_DEFINITIONS, ToolExecutor

    start_time = time.time()
    result = FleetWorkerResult(
        task_id=f"idle-{exploration_type}",
        project=project,
        session_id=session_id,
        ok=False,
        is_idle=True,
        idle_exploration_type=exploration_type,
    )

    wid = session_id.rsplit("-", 2)[0] if "-" in session_id else session_id

    def _send_event(event_type: str, message: str = "", **kwargs: Any) -> None:
        if event_queue is None:
            return
        try:
            event_queue.put_nowait(FleetProgressEvent(
                worker_id=wid,
                session_id=session_id,
                project=project,
                event_type=event_type,
                message=message,
                is_idle=True,
                task_text=f"idle:{exploration_type}",
                **kwargs,
            ))
        except Exception:
            pass

    _send_event("spawn", max_turns=32)

    try:
        if codex_config is None:
            codex_config = CodexConfig.from_env()

        scoped_config = codex_config.with_write_scope(f"projects/{project}")
        scoped_config = _override_turns(scoped_config, 32)

        tool_executor = ToolExecutor(scoped_config)
        backend = CodexBackend(scoped_config, tool_executor=tool_executor)

        idle_opts = FleetExecutionOpts(
            task=FleetTask(
                task_id=f"idle-{exploration_type}",
                text=f"idle:{exploration_type}",
                project=project,
            ),
            session_id=session_id,
            claim_id="",
            prompt=prompt,
            repo_root=repo_root,
            max_turns=32,
        )
        progress_cb = _make_progress_callback(idle_opts, event_queue)

        session_result = backend.run_session(
            task_id=f"idle-{exploration_type}",
            task_context=prompt,
            tools_registry=TOOL_DEFINITIONS,
            progress_callback=progress_cb,
        )

        result.turns = session_result.turns
        result.total_tokens = session_result.token_usage.total_tokens
        _save_fleet_session_log(idle_opts, session_result, repo_root, is_idle=True)

        if session_result.success:
            cwd = str(repo_root)
            auto_commit_orphaned_files(cwd, session_id)
            push_result = rebase_and_push(cwd, session_id)
            result.push_result = push_result.status
            result.ok = True
            written = _extract_written_files(session_result.tool_calls_log)
            elapsed = time.time() - start_time
            _send_event(
                "done", message="ok",
                deliverables=written,
                total_tokens=result.total_tokens,
                duration_seconds=elapsed,
            )
        else:
            elapsed = time.time() - start_time
            _send_event(
                "error", message=session_result.error or "failed",
                duration_seconds=elapsed,
            )

    except Exception as e:
        result.error = f"{type(e).__name__}: {e}"
        elapsed = time.time() - start_time
        _send_event("error", message=result.error, duration_seconds=elapsed)
        logger.exception("Idle worker %s crashed", session_id)

    finally:
        result.duration_seconds = time.time() - start_time
        try:
            claims.release_agent_claims(session_id)
        except Exception:
            pass

    return result
