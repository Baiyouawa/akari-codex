"""小白交互终端 — 常驻角色 Agent。

小白是白侑（小侑）的专属 AI 助手，具有完整的记忆/反思体系、
自然语言理解、多指令拆解和智能任务分发能力。

所有入口（CLI / fleet console / GitHub / QQ）统一调用 ChatBot.process_message()，
返回值始终是小白口吻的自然语言。

Usage:
    python -m runner.chat                          # 交互模式
    python -m runner.chat "看看现在什么状态"          # 单条命令模式
"""

from __future__ import annotations

import json
import re
import readline  # noqa: F401
import sys
import time
from pathlib import Path
from typing import Any

from openai import OpenAI

_API_MAX_RETRIES = 3
_API_RETRY_DELAY = 3

from .codex_session_runner import SessionRunner
from .config import CodexConfig
from .persona import (
    AGENT_NAME,
    USER_NICKNAME,
    XIAOBAI_ROUTER_PROMPT,
    XIAOBAI_SYSTEM_PROMPT,
    XIAOBAI_PUBLIC_PROMPT,
    XIAOBAI_WRAP_PROMPT,
    WELCOME_MESSAGE,
    PROMPT_PREFIX,
    get_persona_prompt_for_user,
    build_override_prompt,
    set_persona_override,
    clear_persona_override,
    list_persona_overrides,
)
from . import memory as mem
from . import memo
from .tools import ToolExecutor


# ─── JSON 解析 ───────────────────────────────────────────────

def _parse_router_response(text: str) -> dict[str, Any] | None:
    """解析路由模块的 JSON 输出。"""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```\w*\n?", "", text)
        text = re.sub(r"\n?```$", "", text)
        text = text.strip()

    try:
        obj = json.loads(text)
        if isinstance(obj, dict) and "route" in obj:
            return obj
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        try:
            obj = json.loads(match.group())
            if isinstance(obj, dict) and "route" in obj:
                return obj
        except json.JSONDecodeError:
            pass

    return None


# ─── ChatBot ─────────────────────────────────────────────────

class ChatBot:
    """小白主体。所有入口共享同一个实例。"""

    def __init__(self, config: CodexConfig):
        self.config = config
        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
            timeout=config.timeout_seconds,
        )
        self.repo_root = config.repo_home
        self.tool_executor = ToolExecutor(config)

    # ── LLM 调用（带自动重试）──────────────────────────────────

    def _stream_chat(self, messages: list[dict[str, Any]], **kwargs: Any) -> str:
        """带自动重试的流式 LLM 调用，返回拼接后的文本。"""
        last_err = None
        for attempt in range(1, _API_MAX_RETRIES + 1):
            try:
                stream = self.client.chat.completions.create(
                    model=self.config.model,
                    messages=messages,
                    stream=True,
                    **kwargs,
                )
                parts: list[str] = []
                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta.content:
                        parts.append(chunk.choices[0].delta.content)
                return "".join(parts)
            except Exception as e:
                last_err = e
                if attempt < _API_MAX_RETRIES:
                    print(f"  [重试 {attempt}/{_API_MAX_RETRIES}] API 连接问题: {e}")
                    time.sleep(_API_RETRY_DELAY * attempt)
        raise last_err  # type: ignore[misc]

    # ── 核心入口 ──────────────────────────────────────────────

    def process_message(
        self, message: str, *, role: str = "owner", user: str = "",
    ) -> str:
        """统一入口：接收自然语言 → 返回小白口吻的回复。

        Args:
            message: 用户输入的自然语言文本。
            role: "owner" = 主人白侑（完整权限），"public" = 普通用户（仅聊天）。
            user: 用户标识（如 "张三(123456)"），用于匹配主人设定的角色扮演人设。
        """
        print(f"  {AGENT_NAME}正在想...")

        if role != "owner":
            reply = self._public_chat(message, user=user)
            return reply

        hardcoded = self._try_hardcoded_persona_cmd(message)
        if hardcoded is not None:
            mem.save_turn(self.repo_root, message, hardcoded, action_taken="set_persona")
            return hardcoded

        due = memo.check_due_reminders(self.repo_root)
        due_notice = ""
        if due:
            notices = [f"「{r['content']}」" for r in due]
            due_notice = f"（对了{USER_NICKNAME}，到时间啦~提醒你：{'、'.join(notices)}）\n\n"

        try:
            router_result = self._call_router(message)
        except Exception as e:
            reply = f"呜...{AGENT_NAME}的大脑好像出了点问题: {type(e).__name__}: {e}"
            mem.save_turn(self.repo_root, message, reply)
            return due_notice + reply

        if not router_result:
            reply = self._plain_chat(message)
            mem.save_turn(self.repo_root, message, reply)
            self._maybe_reflect()
            return due_notice + reply

        route = router_result.get("route", "chat")

        if route == "chat":
            reply = self._plain_chat(message)
            mem.save_turn(self.repo_root, message, reply)
            self._maybe_reflect()
            return due_notice + reply

        if route == "tool_use":
            reply = self._handle_tool_use(message, router_result)
            mem.save_turn(self.repo_root, message, reply, action_taken="tool_use")
            self._maybe_reflect()
            return due_notice + reply

        if route == "action":
            actions = router_result.get("actions", [])
            if not actions:
                reply = f"欸？{AGENT_NAME}理解了你的意思，但好像没有具体要做的事情呢~"
                mem.save_turn(self.repo_root, message, reply)
                return due_notice + reply

            raw_results: list[str] = []
            action_names: list[str] = []
            for action in actions:
                action_type = action.get("action", "")
                action_names.append(action_type)
                print(f"  >> 执行: {action_type}")
                result = self._dispatch(action)
                raw_results.append(result)

            combined = "\n\n---\n\n".join(raw_results)
            reply = self._wrap_result(message, combined)
            mem.save_turn(self.repo_root, message, reply, action_taken=",".join(action_names))
            self._maybe_reflect()
            return due_notice + reply

        reply = router_result.get("reply", f"{AGENT_NAME}有点迷糊了~")
        mem.save_turn(self.repo_root, message, reply)
        return due_notice + reply

    # ── 阶段一：意图路由 ──────────────────────────────────────

    def _call_router(self, user_message: str) -> dict[str, Any] | None:
        memory_context = mem.load_context(self.repo_root)
        repo_context = self._gather_context()

        system_parts = [XIAOBAI_ROUTER_PROMPT]
        if memory_context:
            system_parts.append(f"\n\n{memory_context}")
        if repo_context:
            system_parts.append(f"\n\n## 当前仓库状态\n{repo_context}")

        messages = [
            {"role": "system", "content": "\n".join(system_parts)},
            {"role": "user", "content": user_message},
        ]

        try:
            response_text = self._stream_chat(messages, temperature=0, max_tokens=2048)
        except Exception as e:
            return {"route": "chat", "reply": f"呜...API出了点问题: {e}"}

        return _parse_router_response(response_text)

    # ── 纯文本聊天（不依赖 function calling）──────────────────

    def _plain_chat(self, user_message: str) -> str:
        """小白纯文本聊天：system prompt + memory → 直接让 LLM 回答。"""
        memory_context = mem.load_context(self.repo_root)
        system = XIAOBAI_SYSTEM_PROMPT
        if memory_context:
            system += f"\n\n{memory_context}"

        messages: list[dict[str, Any]] = [
            {"role": "system", "content": system},
            {"role": "user", "content": user_message},
        ]
        try:
            text = self._stream_chat(messages, temperature=0.7, max_tokens=2048)
            return text or f"{AGENT_NAME}好像脑子空白了...(｡•́︿•̀｡)"
        except Exception as e:
            return f"呜...{AGENT_NAME}连不上大脑了: {e}"

    # ── 普通用户聊天（无工具、无 action、无记忆）─────────────

    def _public_chat(self, user_message: str, *, user: str = "") -> str:
        """普通用户模式：查是否有主人设定的角色扮演人设，有则用，否则用默认公共人设。"""
        override = get_persona_prompt_for_user(user) if user else None
        system = build_override_prompt(override) if override else XIAOBAI_PUBLIC_PROMPT

        messages: list[dict[str, Any]] = [
            {"role": "system", "content": system},
            {"role": "user", "content": user_message},
        ]
        try:
            text = self._stream_chat(messages, temperature=0.8, max_tokens=1024)
            return text or ""
        except Exception:
            return ""

    # ── Skill 工具分发（替代 function calling）────────────────

    def _handle_tool_use(self, user_message: str, router_result: dict[str, Any]) -> str:
        """路由器识别到需要工具 → 直接 Python 执行 → 结果喂回 LLM 生成自然语言回答。

        不依赖 API 的 function calling 能力，仅需两轮纯文本调用。
        """
        tools = router_result.get("tools", [])
        if not tools:
            return self._plain_chat(user_message)

        tool_results: list[str] = []
        for tool_spec in tools:
            tool_name = tool_spec.get("tool", "")
            tool_args = {k: v for k, v in tool_spec.items() if k != "tool"}
            print(f"  >> 执行工具: {tool_name}({tool_args})")
            result = self.tool_executor.execute(tool_name, tool_args)
            tool_results.append(f"[{tool_name}] {result}")

        combined_data = "\n\n".join(tool_results)

        memory_context = mem.load_context(self.repo_root)
        system = XIAOBAI_SYSTEM_PROMPT
        if memory_context:
            system += f"\n\n{memory_context}"

        messages: list[dict[str, Any]] = [
            {"role": "system", "content": system},
            {"role": "user", "content": (
                f"{user_message}\n\n"
                f"---\n以下是小白帮你查到的实时信息，请根据这些信息回答{USER_NICKNAME}的问题：\n\n"
                f"{combined_data}"
            )},
        ]
        try:
            text = self._stream_chat(messages, temperature=0.7, max_tokens=2048)
            return text or combined_data
        except Exception as e:
            return f"小白查到了信息但脑子转不过来了...\n\n{combined_data}\n\n(错误: {e})"

    # ── 阶段二：结果润色 ──────────────────────────────────────

    def _wrap_result(self, user_message: str, raw_result: str) -> str:
        """把系统执行结果用小白的口吻重新包装。"""
        if len(raw_result) < 50:
            return raw_result

        messages = [
            {"role": "system", "content": XIAOBAI_WRAP_PROMPT},
            {"role": "user", "content": f"{USER_NICKNAME}的原始请求: {user_message}\n\n系统执行结果:\n{raw_result[:3000]}"},
        ]

        try:
            wrapped = self._stream_chat(messages, temperature=0.5, max_tokens=2048)
            return wrapped if wrapped else raw_result
        except Exception:
            return raw_result

    # ── 反思 ──────────────────────────────────────────────────

    def _maybe_reflect(self) -> None:
        """条件触发记忆反思。"""
        if not mem.should_reflect(self.repo_root):
            return

        messages = mem.build_reflect_messages(self.repo_root)
        if not messages:
            return

        try:
            text = self._stream_chat(messages, temperature=0, max_tokens=1024)
            result = json.loads(text)
            summary = result.get("summary", "")
            facts = result.get("facts", [])

            if summary:
                mem.save_reflection(self.repo_root, summary, facts)
            for fact in facts:
                mem.add_fact(self.repo_root, fact, source="reflect")
        except Exception:
            pass

    # ── Action 分发 ───────────────────────────────────────────

    def _dispatch(self, action: dict[str, Any]) -> str:
        action_type = action.get("action", "")

        handlers = {
            "run_task": self._handle_run_task,
            "orient": self._handle_orient,
            "lit_review": self._handle_lit_review,
            "create_project": self._handle_create_project,
            "create_task": self._handle_create_task,
            "approve": self._handle_approve,
            "help": self._handle_help,
            "fleet_start": self._handle_fleet_start,
            "fleet_status": self._handle_fleet_status,
            "fleet_stop": self._handle_fleet_stop,
            "fleet_report": self._handle_fleet_report,
            "fleet_scale": self._handle_fleet_scale,
            "fleet_tasks": self._handle_fleet_tasks,
            "memo_add": self._handle_memo_add,
            "memo_list": self._handle_memo_list,
            "reminder_add": self._handle_reminder_add,
            "reminder_list": self._handle_reminder_list,
            "set_persona": self._handle_set_persona,
            "clear_persona": self._handle_clear_persona,
            "list_personas": self._handle_list_personas,
        }

        handler = handlers.get(action_type)
        if not handler:
            return f"未知操作: {action_type}"
        return handler(action)

    # ── Handlers ──────────────────────────────────────────────

    def _handle_run_task(self, action: dict) -> str:
        project = action.get("project", "")
        task_desc = action.get("task_description", "")

        task_file = None
        if project:
            candidate = self.repo_root / "projects" / project / "TASKS.md"
            if candidate.is_file():
                task_file = f"projects/{project}/TASKS.md"

        runner = SessionRunner(self.config)
        result = runner.run(task_path=task_file)

        if result.success:
            return (
                f"任务完成!\n"
                f"  任务: {result.task_id}\n"
                f"  轮次: {result.turns}\n"
                f"  Token: {result.token_usage.total_tokens}\n"
                f"  耗时: {result.latency_seconds:.1f}s\n"
                f"  输出: {result.final_output[:300]}..."
            )
        return f"任务失败: {result.error}"

    def _handle_orient(self, action: dict) -> str:
        runner = SessionRunner(self.config)
        state = runner.orient()

        lines = ["当前仓库状态:\n"]
        lines.append(f"  Git: {state.get('git_status', '未知')}")

        for tf in state.get("task_files", []):
            lines.append(f"  {tf['file']}: {tf['total_open']} 个待办任务")
            for t in tf.get("tasks_preview", [])[:3]:
                lines.append(f"    - {t[5:70]}...")

        skills = state.get("skills", [])
        lines.append(f"\n  技能: {len(skills)} 个已加载")

        recent = state.get("recent_logs", [])
        if recent:
            lines.append(f"\n  最近会话:")
            for log in recent[:3]:
                status = "成功" if log.get("success") else "失败"
                lines.append(f"    [{status}] {log.get('file', '')} — {log.get('task_id', '')}")

        return "\n".join(lines)

    def _handle_lit_review(self, action: dict) -> str:
        topic = action.get("topic", "")
        project = action.get("project", "")
        scope = action.get("scope", "")

        task_content = f"# 文献调研任务\n\n"
        task_content += f"**主题:** {topic}\n"
        if scope:
            task_content += f"**范围:** {scope}\n"
        task_content += (
            f"\n## 要求\n\n"
            f"1. 搜索相关论文\n"
            f"2. 按 load-bearing / contextual / incremental 分类\n"
            f"3. 对重要论文写文献笔记\n"
            f"4. 识别研究空白\n"
            f"5. 创建后续任务\n"
        )

        target_dir = self.repo_root / "projects"
        if project:
            target_dir = target_dir / project
        else:
            for d in sorted(target_dir.iterdir()):
                if d.is_dir():
                    target_dir = d
                    project = d.name
                    break

        task_file = target_dir / "tasks" / "lit-review-task.md"
        task_file.parent.mkdir(parents=True, exist_ok=True)
        task_file.write_text(task_content, encoding="utf-8")

        runner = SessionRunner(self.config)
        result = runner.run(task_path=str(task_file.relative_to(self.repo_root)))

        if result.success:
            return (
                f"文献调研完成!\n"
                f"  主题: {topic}\n"
                f"  轮次: {result.turns}, Token: {result.token_usage.total_tokens}\n"
                f"  耗时: {result.latency_seconds:.1f}s\n"
                f"  产出在 projects/{project}/literature/ 目录下"
            )
        return f"文献调研失败: {result.error}"

    def _handle_create_project(self, action: dict) -> str:
        name = action.get("name", "new-project")
        mission = action.get("mission", "")
        tasks = action.get("tasks", [])

        slug = re.sub(r"[^a-z0-9-]", "-", name.lower()).strip("-")
        project_dir = self.repo_root / "projects" / slug
        project_dir.mkdir(parents=True, exist_ok=True)
        (project_dir / "literature").mkdir(exist_ok=True)
        (project_dir / "analysis").mkdir(exist_ok=True)
        (project_dir / "plans").mkdir(exist_ok=True)

        now = time.strftime("%Y-%m-%d")
        readme = f"# {name}\n\nPriority: high\nStatus: active\nMission: {mission}\n\n## Log\n\n### {now}\n\n项目创建。\n"
        (project_dir / "README.md").write_text(readme, encoding="utf-8")

        tasks_content = f"# {name} — 任务列表\n\n"
        for t in tasks:
            tasks_content += f"- [ ] {t} [zero-resource]\n  Done when: TBD\n\n"
        (project_dir / "TASKS.md").write_text(tasks_content, encoding="utf-8")

        return (
            f"项目已创建: projects/{slug}/\n"
            f"  README.md — 项目说明\n"
            f"  TASKS.md — {len(tasks)} 个任务\n"
            f"  literature/ analysis/ plans/ — 产出目录"
        )

    def _handle_create_task(self, action: dict) -> str:
        project = action.get("project", "")
        tasks = action.get("tasks", [])

        if project:
            tasks_file = self.repo_root / "projects" / project / "TASKS.md"
        else:
            tasks_file = self.repo_root / "tasks" / "TASKS.md"

        if not tasks_file.is_file():
            return f"找不到任务文件: {tasks_file}"

        content = tasks_file.read_text(encoding="utf-8")
        new_tasks = ""
        for t in tasks:
            new_tasks += f"\n- [ ] {t} [zero-resource]\n  Done when: TBD\n"

        insert_point = content.find("## Completed")
        if insert_point == -1:
            content += new_tasks
        else:
            content = content[:insert_point] + new_tasks + "\n" + content[insert_point:]

        tasks_file.write_text(content, encoding="utf-8")
        return f"已添加 {len(tasks)} 个任务到 {tasks_file.relative_to(self.repo_root)}"

    def _handle_approve(self, action: dict) -> str:
        return "审批功能：请直接编辑 APPROVAL_QUEUE.md"

    def _handle_help(self, _: dict) -> str:
        return (
            f"小白能帮{USER_NICKNAME}做这些事:\n\n"
            f"  聊天 — 直接跟小白说话就好\n"
            f"  看状态 — \"看看现在什么状态\"\n"
            f"  调研 — \"帮我调研 MoE 最新进展\"\n"
            f"  建项目 — \"创建一个关于XX的项目\"\n"
            f"  加任务 — \"给moe项目加个任务\"\n"
            f"  备忘 — \"记住：明天要交报告\"\n"
            f"  提醒 — \"明天下午3点提醒我开会\"\n"
            f"  舰队 — \"启动4个Agent跑任务\"\n"
            f"  退出 — \"退出\" 或 Ctrl+C"
        )

    def _handle_fleet_start(self, action: dict) -> str:
        from fleet.scheduler import start_fleet, fleet_status as _fleet_status, get_fleet_scheduler
        from fleet.config import FleetConfig
        from dataclasses import replace as dc_replace

        max_workers = action.get("max_workers", None)
        project = action.get("project", "")

        existing = get_fleet_scheduler()
        if existing and existing._running:
            if project:
                existing.add_project_filter(project)
                pf = existing.config.project_filter
                return f"舰队运行中，已加入项目筛选: {', '.join(sorted(pf))}"
            active = existing.metrics.get_active_count()
            done = existing.metrics._total_completed
            return f"舰队已在运行 (正在工作: {active}, 已完成: {done})\n用「调整到N个Agent」调整数量，或「停止舰队」后重新启动"

        fleet_config = FleetConfig.from_env()
        n = int(max_workers) if max_workers else min(4, fleet_config.max_workers)
        proj_filter = frozenset({project}) if project else frozenset()
        fleet_config = dc_replace(
            fleet_config,
            max_workers=n,
            project_filter=proj_filter,
            idle_exploration_enabled=not bool(proj_filter),
        )

        scope = f" (仅 {project})" if project else " (所有项目)"
        start_fleet(repo_root=self.repo_root, fleet_config=fleet_config, background=True)
        time.sleep(1)
        return f"舰队已启动! {n} 个伙伴出发{scope}\n\n{_fleet_status()}"

    def _handle_fleet_status(self, _: dict) -> str:
        from fleet.scheduler import get_fleet_scheduler, fleet_status as _fleet_status
        scheduler = get_fleet_scheduler()
        if not scheduler or not scheduler._running:
            return "舰队目前没有运行哦~ 说「启动舰队」就可以让伙伴们出发!"
        if scheduler._dashboard:
            return scheduler._dashboard.render_snapshot()
        return _fleet_status()

    def _handle_fleet_stop(self, _: dict) -> str:
        from fleet.scheduler import get_fleet_scheduler, stop_fleet
        scheduler = get_fleet_scheduler()
        if not scheduler or not scheduler._running:
            return "舰队没有在运行哦~"
        return stop_fleet()

    def _handle_fleet_report(self, _: dict) -> str:
        from fleet.scheduler import get_fleet_scheduler
        scheduler = get_fleet_scheduler()
        if not scheduler or not scheduler._dashboard:
            return "目前没有执行记录，先启动舰队跑任务吧~"
        return scheduler._dashboard.render_report()

    def _handle_fleet_scale(self, action: dict) -> str:
        from fleet.scheduler import get_fleet_scheduler
        from dataclasses import replace as dc_replace
        count = action.get("count", 0)
        if not count:
            return "请告诉小白要调整到几个Agent~"
        n = int(count)
        scheduler = get_fleet_scheduler()
        if scheduler and scheduler._running:
            scheduler.config = dc_replace(scheduler.config, max_workers=n)
            scheduler.metrics._max_workers = n
            return f"Worker 上限已调整为 {n} 个，下一轮 refill 生效~"
        return f"舰队没有在运行。说「启动{n}个Agent」来启动吧~"

    def _handle_fleet_tasks(self, _: dict) -> str:
        from fleet.task_scanner import scan_available_tasks
        tasks = scan_available_tasks(self.repo_root)
        fleet_tasks = [t for t in tasks if t.fleet_eligible and not t.blocked]
        if not fleet_tasks:
            return "目前没有可执行的任务哦~"
        lines = [f"可执行任务 ({len(fleet_tasks)} 个):\n"]
        for i, t in enumerate(fleet_tasks[:15], 1):
            skill = f"[{t.skill_type.value}]" if t.skill_type else ""
            lines.append(f"  {i:2d}. [{t.project}] {t.text[:60]} {skill}")
        if len(fleet_tasks) > 15:
            lines.append(f"  ... 还有 {len(fleet_tasks) - 15} 个")
        return "\n".join(lines)

    def _handle_memo_add(self, action: dict) -> str:
        content = action.get("content", "")
        if not content:
            return "备忘内容不能为空哦~"
        memo_id = memo.add_memo(self.repo_root, content)
        return f"已记录备忘 (ID: {memo_id}): {content}"

    def _handle_memo_list(self, _: dict) -> str:
        memos = memo.list_memos(self.repo_root)
        return memo.format_memos(memos)

    def _handle_reminder_add(self, action: dict) -> str:
        content = action.get("content", "")
        remind_time = action.get("time", "")
        if not content:
            return "提醒内容不能为空哦~"
        reminder_id = memo.add_reminder(self.repo_root, content, remind_time)
        return f"已设置提醒 (ID: {reminder_id}): {content} — {remind_time}"

    def _handle_reminder_list(self, _: dict) -> str:
        reminders = memo.list_reminders(self.repo_root)
        return memo.format_reminders(reminders)

    # ── 硬编码人设指令匹配（绕过 LLM 路由，避免被安全层拒绝）──

    _PERSONA_PATTERNS = [
        re.compile(r"对\s*(\S+?)\s*扮演\s*(.+)", re.DOTALL),
        re.compile(r"跟\s*(\S+?)\s*聊天时?(?:你是|扮演|身份[是为])\s*(.+)", re.DOTALL),
        re.compile(r"(?:给|对)\s*(\S+?)\s*(?:设定?|换|用)(?:人设|身份|角色)[是为:：]?\s*(.+)", re.DOTALL),
        re.compile(r"(?:现在)?(?:需要你)?对\s*(\S+?)\s*(?:这个用户)?(?:进行)?(?:如下要求的)?(?:回复|聊天)[：:]?\s*(.+)", re.DOTALL),
        re.compile(r"(?:在)?(?:跟|和|与)\s*(\S+?)\s*(?:的)?(?:对话|私聊|聊天)(?:里|中|时)?(?:你[是叫]|身份[是为])\s*(.+)", re.DOTALL),
    ]

    def _try_hardcoded_persona_cmd(self, message: str) -> str | None:
        """尝试用正则直接匹配人设指令，命中则立即执行，不走 LLM 路由。"""
        msg = message.strip()
        for pat in self._PERSONA_PATTERNS:
            m = pat.search(msg)
            if m:
                target = m.group(1).strip()
                persona = m.group(2).strip()
                if target and persona and len(persona) > 2:
                    set_persona_override(target, persona)
                    print(f"  >> [硬匹配] set_persona: {target} → {persona[:50]}...")
                    return f"收到！小白跟 {target} 聊天时会完全按这个来~"
        return None

    def _handle_set_persona(self, action: dict) -> str:
        target = action.get("target", "")
        persona = action.get("persona", "")
        if not target or not persona:
            return "需要指定目标用户和角色描述哦~"
        set_persona_override(target, persona)
        return f"收到！小白跟 {target} 聊天时会扮演: {persona}"

    def _handle_clear_persona(self, action: dict) -> str:
        target = action.get("target", "")
        if not target:
            return "需要指定要取消人设的用户~"
        if clear_persona_override(target):
            return f"已取消对 {target} 的角色扮演，恢复默认"
        return f"没有找到对 {target} 的角色扮演设定"

    def _handle_list_personas(self, _: dict) -> str:
        overrides = list_persona_overrides()
        if not overrides:
            return "目前没有设定任何角色扮演哦~"
        lines = ["当前角色扮演列表:\n"]
        for target, desc in overrides.items():
            lines.append(f"  {target} → {desc[:60]}")
        return "\n".join(lines)

    def _handle_clarify(self, action: dict) -> str:
        return action.get("question", f"{USER_NICKNAME}能再说具体一点吗？")

    # ── 上下文收集 ────────────────────────────────────────────

    def _gather_context(self) -> str:
        parts: list[str] = []

        projects_dir = self.repo_root / "projects"
        if projects_dir.is_dir():
            project_list = []
            for p in sorted(projects_dir.iterdir()):
                if p.is_dir():
                    tasks = p / "TASKS.md"
                    open_count = 0
                    if tasks.is_file():
                        for line in tasks.read_text(errors="replace").splitlines():
                            if line.strip().startswith("- [ ]"):
                                open_count += 1
                    status = "进行中" if open_count > 0 else "空闲"
                    project_list.append(f"  - {p.name}: {status}, {open_count} 个待办")
            if project_list:
                parts.append("项目:\n" + "\n".join(project_list))

        tasks_file = self.repo_root / "tasks" / "TASKS.md"
        if tasks_file.is_file():
            content = tasks_file.read_text(errors="replace")
            open_tasks = [l.strip() for l in content.splitlines() if l.strip().startswith("- [ ]")]
            if open_tasks:
                parts.append(f"全局任务: {len(open_tasks)} 个待办")

        return "\n".join(parts) or "(空仓库)"

    # ── 动态 prompt ─────────────────────────────────────────────

    def _build_prompt(self) -> str:
        """根据舰队状态动态构建 prompt。"""
        try:
            from fleet.scheduler import get_fleet_scheduler
            scheduler = get_fleet_scheduler()
            if scheduler and scheduler._running:
                active = scheduler.metrics.get_active_count()
                done = scheduler.metrics._total_completed
                if scheduler._dashboard and scheduler._dashboard.is_all_done() and done > 0:
                    return f"{USER_NICKNAME} [舰队完成, {done}个任务]> "
                if active > 0:
                    return f"{USER_NICKNAME} [{active}名伙伴工作中]> "
                return f"{USER_NICKNAME} [舰队待命]> "
        except Exception:
            pass
        return PROMPT_PREFIX

    def _print_startup_overview(self) -> None:
        """启动时显示简要任务概览。"""
        projects_dir = self.repo_root / "projects"
        if not projects_dir.is_dir():
            return
        overview: list[str] = []
        for p in sorted(projects_dir.iterdir()):
            if not p.is_dir():
                continue
            tasks = p / "TASKS.md"
            if not tasks.is_file():
                continue
            open_count = sum(
                1 for line in tasks.read_text(errors="replace").splitlines()
                if line.strip().startswith("- [ ]")
            )
            if open_count > 0:
                overview.append(f"  {p.name}: {open_count} 个待办")
        if overview:
            print(f"\n  当前项目任务:")
            for line in overview:
                print(line)
            print()

    # ── 交互循环 ──────────────────────────────────────────────

    def run_interactive(self) -> None:
        print(WELCOME_MESSAGE)
        self._print_startup_overview()

        while True:
            try:
                prompt = self._build_prompt()
                user_input = input(prompt).strip()
            except (EOFError, KeyboardInterrupt):
                self._shutdown()
                break

            if not user_input:
                continue

            if user_input.lower() in ("退出", "exit", "quit", "q"):
                self._shutdown()
                break

            result = self.process_message(user_input)
            print(f"\n{result}\n")

    def _shutdown(self) -> None:
        """优雅退出：停止舰队并告别。"""
        try:
            from fleet.scheduler import get_fleet_scheduler, stop_fleet
            scheduler = get_fleet_scheduler()
            if scheduler and scheduler._running:
                print(f"\n  {AGENT_NAME}正在让伙伴们收工...")
                stop_fleet()
                time.sleep(1)
        except Exception:
            pass
        print(f"\n{AGENT_NAME}下线啦~ {USER_NICKNAME}再见! (≧▽≦)/")


def main() -> None:
    try:
        config = CodexConfig.from_env()
    except EnvironmentError as e:
        print(f"配置错误: {e}", file=sys.stderr)
        sys.exit(1)

    bot = ChatBot(config)

    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
        result = bot.process_message(message)
        print(f"\n{result}")
    else:
        bot.run_interactive()


if __name__ == "__main__":
    main()
