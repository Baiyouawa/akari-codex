"""Fleet dashboard — silent event collector with on-demand rendering.

Architecture:
  - Workers send FleetProgressEvent via a shared multiprocessing.Queue
  - A lightweight background thread drains events and updates internal state
  - NO automatic terminal output — the console calls render_snapshot()
    or render_report() explicitly when the user asks for status
"""

from __future__ import annotations

import shutil
import threading
import time
from dataclasses import dataclass, field
from multiprocessing import Queue
from typing import Any


@dataclass
class FleetProgressEvent:
    """Progress event sent from a worker subprocess to the dashboard."""

    worker_id: str
    session_id: str
    project: str
    event_type: str  # spawn | thinking | tool_exec | chatter | done | error
    turn: int = 0
    max_turns: int = 64
    tool_name: str | None = None
    tool_args_preview: str | None = None
    message: str = ""
    task_text: str = ""
    is_idle: bool = False
    deliverables: list[str] = field(default_factory=list)
    total_tokens: int = 0
    duration_seconds: float = 0.0


_PHASE_ICONS = {
    "spawn": "🚀",
    "thinking": "🧠",
    "tool_exec": "⚡",
    "chatter": "💬",
    "done": "✅",
    "error": "❌",
}

_TOOL_ICONS = {
    "read_file": "📖",
    "write_file": "✏️",
    "list_files": "📂",
    "search_text": "🔍",
    "run_shell": "💻",
    "git_status": "📊",
    "log_decision": "📝",
    "request_approval": "🔒",
}

_CHATTER_TEMPLATES = {
    "spawn": ["领到任务了，开工！", "收到，马上开始", "我来处理这个", "了解，这个交给我"],
    "search_text": ["我搜搜看有没有相关资料...", "让我查一下...", "翻翻文档看看..."],
    "read_file": ["读一下这个文件", "看看里面写了什么", "研究一下这份材料"],
    "write_file": ["写好了，保存中", "产出就绪，写入文件", "成果已记录"],
    "run_shell": ["跑个命令验证一下", "执行中..."],
    "thinking": ["让我想想...", "分析中...", "综合考虑一下...", "梳理思路中..."],
    "done_ok": ["搞定了！", "任务完成，交付！", "结束，成果已提交", "完工！"],
    "done_fail": ["遇到困难，先撤了", "这个有点棘手，需要升级处理", "出了点问题..."],
}


def _pick_chatter(category: str, worker_id: str) -> str:
    templates = _CHATTER_TEMPLATES.get(category, ["..."])
    return templates[hash(worker_id) % len(templates)]


@dataclass
class _WorkerState:
    worker_id: str
    session_id: str
    project: str
    task_text: str = ""
    phase: str = "spawn"
    turn: int = 0
    max_turns: int = 64
    tool_name: str | None = None
    last_message: str = ""
    started_at: float = field(default_factory=time.time)
    is_idle: bool = False
    finished: bool = False
    ok: bool = False
    deliverables: list[str] = field(default_factory=list)
    total_tokens: int = 0
    duration_seconds: float = 0.0


class DashboardRenderer:
    """Silently collects worker events; renders on demand only."""

    def __init__(self, event_queue: Queue, max_workers: int = 32):
        self._queue = event_queue
        self._max_workers = max_workers
        self._workers: dict[str, _WorkerState] = {}
        self._recent_chatter: list[tuple[str, str, str]] = []
        self._lock = threading.Lock()
        self._running = False
        self._thread: threading.Thread | None = None
        self._total_completed = 0
        self._total_ok = 0

    def start(self) -> None:
        self._running = True
        self._thread = threading.Thread(
            target=self._drain_loop, name="fleet-dashboard", daemon=True
        )
        self._thread.start()

    def stop(self) -> None:
        self._running = False
        if self._thread:
            self._thread.join(timeout=3)

    # ── background drain (no rendering) ──────────────────────────

    def _drain_loop(self) -> None:
        while self._running:
            self._drain_events()
            time.sleep(0.5)
        self._drain_events()

    def _drain_events(self) -> None:
        if self._queue is None:
            return
        while not self._queue.empty():
            try:
                event: FleetProgressEvent = self._queue.get_nowait()
                self._process_event(event)
            except Exception:
                break

    def _process_event(self, event: FleetProgressEvent) -> None:
        with self._lock:
            wid = event.worker_id

            if event.event_type == "spawn":
                self._workers[wid] = _WorkerState(
                    worker_id=wid,
                    session_id=event.session_id,
                    project=event.project,
                    task_text=event.task_text,
                    max_turns=event.max_turns,
                    is_idle=event.is_idle,
                    last_message=_pick_chatter("spawn", wid),
                )
                self._add_chatter(wid, "🚀", self._workers[wid].last_message)
                return

            if wid not in self._workers:
                return

            ws = self._workers[wid]

            if event.event_type == "thinking":
                ws.phase = "thinking"
                ws.turn = event.turn
                ws.tool_name = None
                ws.last_message = _pick_chatter("thinking", wid + str(event.turn))

            elif event.event_type == "tool_exec":
                ws.phase = "tool_exec"
                ws.turn = event.turn
                ws.tool_name = event.tool_name
                tool_cat = event.tool_name if event.tool_name in _CHATTER_TEMPLATES else "thinking"
                chatter = _pick_chatter(tool_cat, wid + str(event.turn))
                if event.tool_args_preview:
                    chatter = f"{chatter} ({event.tool_args_preview[:40]})"
                ws.last_message = chatter
                icon = _TOOL_ICONS.get(event.tool_name or "", "⚡")
                self._add_chatter_dedup(wid, icon, chatter)

            elif event.event_type == "chatter":
                ws.last_message = event.message
                self._add_chatter_dedup(wid, "💬", event.message)

            elif event.event_type == "done":
                if ws.finished:
                    return
                ws.phase = "done"
                ws.finished = True
                ws.ok = "ok" in event.message.lower() or event.message == ""
                ws.deliverables = event.deliverables
                ws.total_tokens = event.total_tokens
                ws.duration_seconds = event.duration_seconds
                self._total_completed += 1
                if ws.ok:
                    self._total_ok += 1
                    ws.last_message = _pick_chatter("done_ok", wid)
                    self._add_chatter(wid, "✅", ws.last_message)
                else:
                    ws.last_message = _pick_chatter("done_fail", wid)
                    self._add_chatter(wid, "❌", ws.last_message)

            elif event.event_type == "error":
                if ws.finished:
                    return
                ws.phase = "error"
                ws.finished = True
                ws.ok = False
                ws.duration_seconds = event.duration_seconds
                self._total_completed += 1
                ws.last_message = event.message[:60] if event.message else "出错了"
                self._add_chatter(wid, "❌", ws.last_message)

    def _add_chatter(self, worker_id: str, icon: str, message: str) -> None:
        self._recent_chatter.append((worker_id, icon, message))
        if len(self._recent_chatter) > 20:
            self._recent_chatter = self._recent_chatter[-20:]

    def _add_chatter_dedup(self, worker_id: str, icon: str, message: str) -> None:
        for wid, _, msg in reversed(self._recent_chatter):
            if wid == worker_id:
                if msg == message:
                    return
                break
        self._add_chatter(worker_id, icon, message)

    # ── public on-demand render methods ──────────────────────────

    def is_all_done(self) -> bool:
        with self._lock:
            if not self._workers:
                return False
            return all(w.finished for w in self._workers.values())

    def render_snapshot(self) -> str:
        """Return a multi-line string showing current fleet status."""
        self._drain_events()
        with self._lock:
            return self._build_snapshot()

    def render_report(self) -> str:
        """Return the final deliverables report."""
        self._drain_events()
        with self._lock:
            finished = [w for w in self._workers.values() if w.finished]
            if not finished:
                return "  还没有完成的任务。"
            return self._build_report(finished)

    # ── internal formatting ──────────────────────────────────────

    def _build_snapshot(self) -> str:
        w = shutil.get_terminal_size((100, 24)).columns
        lines: list[str] = []

        active = [ws for ws in self._workers.values() if not ws.finished]
        finished = [ws for ws in self._workers.values() if ws.finished]
        total_active = len(active)

        lines.append(f"{'─' * w}")
        lines.append(
            f"  🚢 Fleet Dashboard  |  "
            f"Active: {total_active}/{self._max_workers}  |  "
            f"Done: {self._total_completed} "
            f"(✅{self._total_ok} ❌{self._total_completed - self._total_ok})"
        )
        lines.append(f"{'─' * w}")

        if not active and self._total_completed == 0:
            lines.append("  ⏳ 等待 worker 启动...")
            return "\n".join(lines)

        proj_active: dict[str, int] = {}
        proj_done: dict[str, int] = {}
        for ws in active:
            proj_active[ws.project] = proj_active.get(ws.project, 0) + 1
        for ws in finished:
            proj_done[ws.project] = proj_done.get(ws.project, 0) + 1
        all_projects = sorted(set(proj_active) | set(proj_done))

        if all_projects:
            parts = []
            for proj in all_projects:
                a = proj_active.get(proj, 0)
                d = proj_done.get(proj, 0)
                if a > 0:
                    parts.append(f"{proj}: {a} agent{'s' if a > 1 else ''} running, {d} done")
                else:
                    parts.append(f"{proj}: {d} done")
            lines.append("  " + "  |  ".join(parts))
            lines.append(f"{'─' * w}")

        for proj in all_projects:
            proj_workers = sorted(
                [ws for ws in active if ws.project == proj],
                key=lambda x: x.worker_id,
            )
            if proj_workers:
                for ws in proj_workers:
                    lines.append(self._format_worker_line(ws, w))

        if not active and self._total_completed > 0:
            lines.append("  🏁 所有任务已完成。输入 report 查看交付报告")

        if self._recent_chatter:
            lines.append("")
            lines.append(f"  {'─' * (w - 4)}")
            lines.append("  💬 最近动态:")
            for wid, icon, msg in self._recent_chatter[-8:]:
                short_wid = wid.replace("fleet-worker-", "W")
                proj = ""
                if wid in self._workers:
                    proj = f"/{self._workers[wid].project}"
                line = f"    {icon} [{short_wid}{proj}] {msg}"
                if len(line) > w:
                    line = line[:w - 1]
                lines.append(line)

        lines.append(f"{'─' * w}")
        return "\n".join(lines)

    def _build_report(self, finished: list[_WorkerState]) -> str:
        w = shutil.get_terminal_size((100, 24)).columns
        lines: list[str] = []

        ok_workers = [ws for ws in finished if ws.ok]
        fail_workers = [ws for ws in finished if not ws.ok]
        total_tokens = sum(ws.total_tokens for ws in finished)
        total_secs = sum(ws.duration_seconds for ws in finished)

        lines.append(f"{'═' * w}")
        lines.append(
            f"  🏁 Fleet 执行报告  |  "
            f"✅ {len(ok_workers)} 成功  "
            f"❌ {len(fail_workers)} 失败  |  "
            f"Token: {total_tokens:,}  "
            f"耗时: {total_secs:.0f}s"
        )
        lines.append(f"{'═' * w}")

        by_project: dict[str, list[_WorkerState]] = {}
        for ws in finished:
            by_project.setdefault(ws.project, []).append(ws)

        for proj, workers in sorted(by_project.items()):
            proj_ok = sum(1 for ws in workers if ws.ok)
            proj_fail = sum(1 for ws in workers if not ws.ok)
            lines.append("")
            lines.append(f"  📂 {proj}  (✅{proj_ok} ❌{proj_fail})")
            lines.append(f"  {'─' * (w - 4)}")

            for ws in workers:
                short_id = ws.worker_id.replace("fleet-worker-", "W")
                icon = "✅" if ws.ok else "❌"
                idle_tag = " [idle]" if ws.is_idle else ""
                task_preview = ws.task_text[:50]
                if len(ws.task_text) > 50:
                    task_preview += "..."

                lines.append(
                    f"  {icon} {short_id}{idle_tag}: {task_preview}"
                    f"  ({ws.turn}轮, {ws.duration_seconds:.0f}s, "
                    f"{ws.total_tokens:,}tok)"
                )

                if ws.deliverables:
                    for fpath in ws.deliverables:
                        lines.append(f"     📄 {fpath}")

                if not ws.ok and ws.last_message:
                    lines.append(f"     ⚠️  {ws.last_message}")

        lines.append("")
        lines.append(f"{'═' * w}")
        return "\n".join(lines)

    def _format_worker_line(self, ws: _WorkerState, max_width: int) -> str:
        elapsed = time.time() - ws.started_at
        pct = min(ws.turn / max(ws.max_turns, 1) * 100, 99)

        bar_len = 10
        filled = int(bar_len * pct / 100)
        bar = "█" * filled + "░" * (bar_len - filled)

        short_id = ws.worker_id.replace("fleet-worker-", "W")
        phase_icon = _PHASE_ICONS.get(ws.phase, "·")
        idle_tag = " [idle]" if ws.is_idle else ""

        if ws.phase == "tool_exec" and ws.tool_name:
            tool_icon = _TOOL_ICONS.get(ws.tool_name, "⚡")
            detail = f"{tool_icon}{ws.tool_name}"
        elif ws.phase == "thinking":
            detail = "🧠 思考中"
        else:
            detail = ws.last_message[:30] if ws.last_message else ""

        line = (
            f"  {phase_icon} {short_id} [{bar}] "
            f"T{ws.turn}/{ws.max_turns} "
            f"{ws.project} "
            f"{detail}{idle_tag} "
            f"({elapsed:.0f}s)"
        )

        if len(line) > max_width:
            line = line[:max_width - 1]
        return line
