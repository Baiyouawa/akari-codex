"""Unified interactive fleet console.

Design: fleet runs silently in the background. The user is always at the
interactive prompt and can type commands at any time.  Dashboard output
is *only* shown when the user explicitly asks (status / report).

Usage:
    python3 -m fleet.console              # interactive
    python3 -m fleet.console --workers 4  # start with 4 workers immediately
"""

from __future__ import annotations

import os
import readline  # noqa: F401 — enables arrow-key history in input()
import shutil
import textwrap
import time
from pathlib import Path
from typing import Any

from .config import FleetConfig
from .scheduler import (
    FleetScheduler,
    start_fleet,
    stop_fleet,
    fleet_status,
    get_fleet_scheduler,
)
from .task_scanner import scan_available_tasks
from .task_supply import scan_task_supply


def _term_width() -> int:
    return shutil.get_terminal_size((100, 24)).columns


def _print_banner() -> None:
    w = _term_width()
    print()
    print(f"{'═' * w}")
    print("  🚢 OpenAkari Fleet Console — Multi-Agent 控制台")
    print(f"{'═' * w}")


def _print_supply_overview(repo_root: Path) -> None:
    snap = scan_task_supply(repo_root)
    w = _term_width()

    print()
    print("  📋 任务概览")
    print(f"  {'─' * (w - 4)}")
    print(
        f"  Ready: {snap.total_ready}  |  "
        f"Blocked: {snap.total_blocked}  |  "
        f"Requires-Opus: {snap.total_requires_opus}"
    )
    print()

    if snap.by_project:
        for project, stats in snap.by_project.items():
            ready = stats["fleet_eligible_unblocked"]
            blocked = stats["fleet_eligible_blocked"]
            opus = stats["requires_opus"]
            bar_len = min(ready, 20)
            bar = "█" * bar_len + "░" * (20 - bar_len)
            print(f"  [{bar}] {project}: {ready} ready, {blocked} blocked, {opus} opus")
    print()


def _print_help() -> None:
    w = _term_width()
    print(f"\n  {'─' * (w - 4)}")
    print(textwrap.dedent("""\
      🎮 命令指南:

      🚀 舰队控制:
        start [N] [项目名]  启动舰队 (例: start 4 moe — 仅跑 moe 项目)
        stop               优雅停止舰队
        status / s         查看当前运行状态
        report / r         查看交付报告（含文件路径）
        scale N            调整 worker 上限

      📋 任务管理:
        tasks              查看可用任务（带编号）
        add <项目> <描述>   添加新任务
        del <编号>          删除任务（编号从 tasks 命令获取）

      🤖 自然语言:
        直接输入中文指令，系统自动理解并执行
        例: "执行 moe 任务" → 只启动 moe 项目的 worker

      ⏹ 退出:
        exit / quit / Ctrl+C
    """))


def _handle_command(
    cmd: str,
    repo_root: Path,
    config: FleetConfig,
    bot: Any | None,
) -> bool:
    """Handle a console command. Returns True to continue, False to exit."""
    parts = cmd.strip().split(None, 2)
    if not parts:
        return True

    verb = parts[0].lower()

    # ── exit ─────────────────────────────────────────────────────
    if verb in ("exit", "quit", "退出", "q"):
        scheduler = get_fleet_scheduler()
        if scheduler and scheduler._running:
            print("  ⏳ 正在停止舰队...")
            stop_fleet()
            time.sleep(1)
        print("  👋 再见!")
        return False

    # ── help ─────────────────────────────────────────────────────
    if verb in ("help", "帮助", "h", "?"):
        _print_help()
        return True

    # ── start [N] [project] ────────────────────────────────────
    if verb in ("start", "启动", "launch"):
        n = None
        proj_filter: set[str] = set()
        for p in parts[1:]:
            if p.isdigit():
                n = int(p)
            else:
                proj_filter.add(p)

        existing = get_fleet_scheduler()
        if existing and existing._running:
            if proj_filter:
                for pf in proj_filter:
                    existing.add_project_filter(pf)
                print(f"  ✅ 已添加项目筛选: {', '.join(sorted(existing.config.project_filter))}")
            else:
                active = existing.metrics.get_active_count()
                done = existing.metrics._total_completed
                print(f"  ⚠️  舰队已在运行 (active: {active}, done: {done})")
            print(f"  💡 用 scale N 调整数量，或 stop 后重新启动")
            return True

        if n is None:
            n = min(4, config.max_workers)

        from dataclasses import replace
        new_config = replace(
            config,
            max_workers=n,
            project_filter=frozenset(proj_filter),
            idle_exploration_enabled=not bool(proj_filter),
        )
        scope_msg = f" (仅 {', '.join(sorted(proj_filter))})" if proj_filter else " (所有项目)"
        print(f"  🚀 启动舰队: {n} workers{scope_msg} — 后台运行中")
        start_fleet(repo_root=repo_root, fleet_config=new_config, background=True)
        print(f"  💡 输入 status 查看进度，report 查看结果")
        return True

    # ── stop ─────────────────────────────────────────────────────
    if verb in ("stop", "停止"):
        scheduler = get_fleet_scheduler()
        if not scheduler or not scheduler._running:
            print("  ⚠️  舰队未在运行")
            return True
        print("  ⏳ 正在停止舰队...")
        result = stop_fleet()
        print(f"  ✅ {result}")
        return True

    # ── status (on-demand snapshot) ──────────────────────────────
    if verb in ("status", "s", "状态", "舰队状态"):
        scheduler = get_fleet_scheduler()
        if not scheduler:
            print("  ⚠️  舰队未运行。输入 start 启动")
            return True
        if scheduler._dashboard:
            print(scheduler._dashboard.render_snapshot())
        else:
            print(f"\n{fleet_status()}\n")
        return True

    # ── report (on-demand deliverables) ──────────────────────────
    if verb in ("report", "r", "报告", "交付", "结果"):
        scheduler = get_fleet_scheduler()
        if not scheduler or not scheduler._dashboard:
            print("  ⚠️  舰队未运行或没有执行记录")
            return True
        print(scheduler._dashboard.render_report())
        return True

    # ── scale ────────────────────────────────────────────────────
    if verb in ("scale", "调整"):
        if len(parts) < 2 or not parts[1].isdigit():
            print("  ⚠️  用法: scale <数量>  例如: scale 8")
            return True
        n = int(parts[1])
        scheduler = get_fleet_scheduler()
        if scheduler and scheduler._running:
            from dataclasses import replace
            scheduler.config = replace(scheduler.config, max_workers=n)
            scheduler.metrics._max_workers = n
            print(f"  ✅ Worker 上限调整为 {n}（下一轮 refill 生效）")
        else:
            print(f"  ⚠️  舰队未运行。先 start {n} 启动")
        return True

    # ── tasks ────────────────────────────────────────────────────
    if verb in ("tasks", "任务"):
        _print_supply_overview(repo_root)
        tasks = scan_available_tasks(repo_root)
        fleet_tasks = [t for t in tasks if t.fleet_eligible and not t.blocked]
        if fleet_tasks:
            print(f"  📋 Fleet-eligible 任务 ({len(fleet_tasks)} 个):\n")
            for i, t in enumerate(fleet_tasks[:15], 1):
                skill = f"[{t.skill_type.value}]" if t.skill_type else ""
                print(f"    {i:2d}. [{t.project}] {t.text[:60]} {skill}")
            if len(fleet_tasks) > 15:
                print(f"    ... 还有 {len(fleet_tasks) - 15} 个")
        else:
            print("  📭 没有可用任务")
        print()
        return True

    # ── del / delete ─────────────────────────────────────────────
    if verb in ("del", "delete", "删除") and len(parts) >= 2:
        try:
            idx = int(parts[1]) - 1
        except ValueError:
            print("  ⚠️  用法: del <编号>  (先用 tasks 查看编号)")
            return True
        all_tasks = scan_available_tasks(repo_root)
        fleet_tasks = [t for t in all_tasks if t.fleet_eligible and not t.blocked]
        if idx < 0 or idx >= len(fleet_tasks):
            print(f"  ❌ 编号 {idx + 1} 无效。共 {len(fleet_tasks)} 个任务，先用 tasks 查看")
            return True
        target = fleet_tasks[idx]
        tasks_file = repo_root / "projects" / target.project / "TASKS.md"
        if tasks_file.is_file():
            lines = tasks_file.read_text(encoding="utf-8").splitlines(keepends=True)
            new_lines = [l for l in lines if target.text[:40] not in l]
            if len(new_lines) < len(lines):
                tasks_file.write_text("".join(new_lines), encoding="utf-8")
                print(f"  🗑️  已删除: [{target.project}] {target.text[:60]}")
            else:
                print(f"  ⚠️  未找到匹配行，请手动编辑 {tasks_file}")
        return True

    # ── add ──────────────────────────────────────────────────────
    if verb == "add" and len(parts) >= 3:
        project = parts[1]
        task_desc = parts[2]
        tasks_file = repo_root / "projects" / project / "TASKS.md"
        if not tasks_file.is_file():
            projects_dir = repo_root / "projects"
            available = [p.name for p in projects_dir.iterdir() if p.is_dir()] if projects_dir.is_dir() else []
            print(f"  ❌ 项目不存在: {project}")
            if available:
                print(f"  💡 可用项目: {', '.join(available)}")
            return True
        content = tasks_file.read_text(encoding="utf-8")
        new_entry = f"\n- [ ] {task_desc} [zero-resource]\n  Done when: TBD\n"
        tasks_file.write_text(content + new_entry, encoding="utf-8")
        print(f"  ✅ 任务已添加到 projects/{project}/TASKS.md")
        scheduler = get_fleet_scheduler()
        if scheduler and scheduler._running:
            print("     舰队下一轮 refill 会自动认领")
        else:
            print("     输入 start 启动舰队来执行")
        return True

    # ── fallback: natural language via ChatBot ───────────────────
    if bot is not None:
        print("  🧠 正在理解你的意图...")
        actions = bot._call_coordinator(cmd)
        if not actions:
            print("  👋 你好！直接用自然语言跟我说话就行，比如「看看状态」「帮我调研MoE」")
            return True

        for i, action in enumerate(actions):
            action_type = action.get("action", "")
            if len(actions) > 1:
                print(f"  📌 指令 {i+1}/{len(actions)}: {action_type}")
            else:
                print(f"  📌 识别到: {action_type}")

            if action_type in ("run_task", "lit_review"):
                _dispatch_as_fleet_task(action, repo_root, config, bot)
                continue

            if action_type == "fleet_start":
                _handle_command(
                    f"start {action.get('max_workers', config.max_workers)}",
                    repo_root, config, bot,
                )
                continue
            if action_type == "fleet_status":
                _handle_command("status", repo_root, config, bot)
                continue
            if action_type == "fleet_stop":
                _handle_command("stop", repo_root, config, bot)
                continue

            result = bot.dispatch(action)
            print(f"\n{result}\n")

        return True

    print(f"  ❓ 未知命令: {verb}")
    print(f"  💡 输入 help 查看命令列表，或直接用中文下指令")
    return True


def _dispatch_as_fleet_task(
    action: dict,
    repo_root: Path,
    config: FleetConfig,
    bot: Any | None,
) -> bool:
    """Convert a blocking action (run_task / lit_review) into a fleet background task."""
    action_type = action.get("action", "")
    project = action.get("project", "")

    if action_type == "lit_review":
        topic = action.get("topic", "")
        scope = action.get("scope", "")
        task_text = f"文献调研: {topic}"
        if scope:
            task_text += f" (范围: {scope})"
    else:
        task_text = action.get("task_description", "执行任务")

    if not project:
        projects_dir = repo_root / "projects"
        if projects_dir.is_dir():
            candidates = [p.name for p in projects_dir.iterdir() if p.is_dir()]
            if len(candidates) == 1:
                project = candidates[0]
            elif candidates:
                print(f"  ❓ 请指定项目。可用: {', '.join(candidates)}")
                print(f"  💡 例如: add {candidates[0]} {task_text}")
                return True
            else:
                print("  ❌ 没有可用项目。先用 create_project 创建项目。")
                return True

    tasks_file = repo_root / "projects" / project / "TASKS.md"
    if not tasks_file.is_file():
        print(f"  ❌ 项目不存在: {project}")
        return True

    content = tasks_file.read_text(encoding="utf-8")
    new_entry = f"\n- [ ] {task_text} [zero-resource]\n  Done when: TBD\n"
    tasks_file.write_text(content + new_entry, encoding="utf-8")
    print(f"  ✅ 任务已写入 projects/{project}/TASKS.md")

    ready_count = sum(
        1 for line in tasks_file.read_text(encoding="utf-8").splitlines()
        if line.strip().startswith("- [ ]")
    )

    scheduler = get_fleet_scheduler()
    if not scheduler or not scheduler._running:
        from dataclasses import replace
        workers = min(ready_count + 1, config.max_per_project, config.max_workers)
        new_config = replace(
            config,
            max_workers=workers,
            project_filter=frozenset({project}),
            idle_exploration_enabled=False,
        )
        print(f"  🚀 启动舰队: {workers} workers (仅 {project} 项目)")
        start_fleet(repo_root=repo_root, fleet_config=new_config, background=True)
    else:
        scheduler.add_project_filter(project)
        pf = scheduler.config.project_filter
        active = scheduler.metrics.get_active_count()
        print(f"  🚀 舰队运行中 ({active} active)，已加入项目筛选: {', '.join(sorted(pf))}")

    print(f"  💡 输入 status 查看进度，report 查看结果")
    return True


def run_console(
    repo_root: Path | None = None,
    max_workers: int | None = None,
    auto_start: bool = False,
) -> None:
    """Main entry point for the interactive fleet console."""
    if repo_root is None:
        repo_root = Path(os.environ.get("OPENAKARI_HOME", str(Path.cwd())))

    config = FleetConfig.from_env()
    if max_workers is not None:
        from dataclasses import replace
        config = replace(config, max_workers=max_workers)

    bot = None
    try:
        from runner.config import CodexConfig
        from runner.chat import ChatBot
        codex_config = CodexConfig.from_env()
        bot = ChatBot(codex_config)
    except Exception:
        pass

    _print_banner()
    _print_supply_overview(repo_root)
    _print_help()

    if auto_start:
        print(f"  🚀 启动舰队: {config.max_workers} workers — 后台运行中")
        start_fleet(repo_root=repo_root, fleet_config=config, background=True)
        print(f"  💡 输入 status 查看进度，report 查看结果\n")

    while True:
        try:
            scheduler = get_fleet_scheduler()
            if scheduler and scheduler._running:
                active = scheduler.metrics.get_active_count()
                done = scheduler.metrics._total_completed
                pf = scheduler.config.project_filter
                scope = f" ({','.join(sorted(pf))})" if pf else ""
                if scheduler._dashboard and scheduler._dashboard.is_all_done() and done > 0:
                    prompt = f"fleet{scope} [🏁 完成, {done} done]> "
                elif active > 0:
                    prompt = f"fleet{scope} [{active} active, {done} done]> "
                else:
                    prompt = f"fleet{scope} [{done} done]> "
            else:
                prompt = "fleet> "

            user_input = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            scheduler = get_fleet_scheduler()
            if scheduler and scheduler._running:
                print("  ⏳ 正在停止舰队...")
                stop_fleet()
                time.sleep(1)
            print("  👋 再见!")
            break

        if not user_input:
            continue

        should_continue = _handle_command(user_input, repo_root, config, bot)
        if not should_continue:
            break


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(
        description="OpenAkari Fleet Console — 交互式多 Agent 控制台",
    )
    parser.add_argument(
        "--workers", "-w", type=int, default=None,
        help="Worker 数量 (不指定则不自动启动)",
    )
    parser.add_argument(
        "--repo", type=str, default=None,
        help="仓库根目录 (default: OPENAKARI_HOME or cwd)",
    )
    parser.add_argument(
        "--auto-start", action="store_true",
        help="启动后立即开始执行任务",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo) if args.repo else None
    run_console(
        repo_root=repo_root,
        max_workers=args.workers,
        auto_start=args.auto_start or args.workers is not None,
    )


if __name__ == "__main__":
    main()
