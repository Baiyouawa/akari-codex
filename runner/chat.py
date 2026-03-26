"""小白交互终端 — 顶层智能 Agent。

小白是白侑（小侑）的专属 AI 助手，同时也是 Multi-Agent 系统的队长。
它拥有统一 Skill 体系，能够自主推理、执行多步任务，并在需要时调度
Multi-Agent 系统协作。

所有入口（CLI / QQ / GitHub）统一调用 ChatBot.process_message()，
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

from .agent_loop import AgentLoop, AgentResult
from .config import CodexConfig
from .persona import (
    AGENT_NAME,
    USER_NICKNAME,
    XIAOBAI_AGENT_PROMPT,
    XIAOBAI_SYSTEM_PROMPT,
    XIAOBAI_PUBLIC_PROMPT,
    WELCOME_MESSAGE,
    PROMPT_PREFIX,
    get_persona_prompt_for_user,
    build_override_prompt,
    set_persona_override,
)
from .skill_registry import SkillRegistry
from . import memory as mem
from . import memo


_PUBLIC_HISTORY_MAX = 20
_PUBLIC_TOOL_CALL_MAX = 3

_public_chat_histories: dict[str, list[dict[str, str]]] = {}

_PUBLIC_TOOLS_WHITELIST = {"web_search", "web_fetch", "get_current_time", "calculate"}


def _get_public_tools() -> list[dict[str, Any]]:
    """构建普通用户可用的 OpenAI function calling 工具定义。"""
    from .tools import TOOL_DEFINITIONS
    return [
        {
            "type": "function",
            "function": {"name": name, **spec},
        }
        for name, spec in TOOL_DEFINITIONS.items()
        if name in _PUBLIC_TOOLS_WHITELIST
    ]


class ChatBot:
    """小白主体 — 顶层智能 Agent。所有入口共享同一个实例。"""

    def __init__(self, config: CodexConfig):
        self.config = config
        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
            timeout=config.timeout_seconds,
        )
        self.repo_root = config.repo_home
        self.skill_registry = SkillRegistry(config.repo_home)
        self._progress_log: list[str] = []

    # ── LLM 调用（带自动重试）──────────────────────────────────

    def _stream_chat(self, messages: list[dict[str, Any]], **kwargs: Any) -> str:
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
        """统一入口：接收自然语言 → 启动 Agent 循环 → 返回小白口吻的回复。

        Args:
            message: 用户输入的自然语言文本。
            role: "owner" = 主人白侑（完整权限），"public" = 普通用户（仅聊天）。
            user: 用户标识（如 "张三(123456)"），用于匹配主人设定的角色扮演人设。
        """
        print(f"  {AGENT_NAME}正在想...")

        if role != "owner":
            return self._public_chat(message, user=user)

        hardcoded = self._try_hardcoded_persona_cmd(message)
        if hardcoded is not None:
            mem.save_turn(self.repo_root, message, hardcoded, action_taken="set_persona")
            return hardcoded

        due = memo.check_due_reminders(self.repo_root)
        due_notice = ""
        if due:
            notices = [f"「{r['content']}」" for r in due]
            due_notice = f"（对了{USER_NICKNAME}，到时间啦~提醒你：{'、'.join(notices)}）\n\n"

        self._progress_log = []

        try:
            loop = AgentLoop(
                config=self.config,
                skill_registry=self.skill_registry,
                system_prompt=XIAOBAI_AGENT_PROMPT,
                memory_context=mem.load_context(self.repo_root),
                repo_context=self._gather_context(),
                progress_callback=self._on_progress,
            )
            result = loop.run(message)
        except Exception as e:
            reply = f"呜...{AGENT_NAME}的大脑好像出了点问题: {type(e).__name__}: {e}"
            mem.save_turn(self.repo_root, message, reply)
            return due_notice + reply

        reply = result.reply or f"{AGENT_NAME}好像脑子空白了...(｡•́︿•̀｡)"

        action_summary = ",".join(result.skills_used) if result.skills_used else "chat"
        if result.delegated:
            action_summary = f"delegate,{action_summary}"
        mem.save_turn(self.repo_root, message, reply, action_taken=action_summary)
        self._maybe_reflect()

        return due_notice + reply

    # ── 进度播报回调 ─────────────────────────────────────────

    def _on_progress(self, message: str) -> None:
        self._progress_log.append(message)
        print(f"  💬 {message}")

    def get_progress_log(self) -> list[str]:
        return list(self._progress_log)

    # ── 普通用户聊天（带短期记忆）──────────────────────────────

    def _public_chat(self, user_message: str, *, user: str = "") -> str:
        from .tools import ToolExecutor

        override = get_persona_prompt_for_user(user) if user else None
        system = build_override_prompt(override) if override else XIAOBAI_PUBLIC_PROMPT

        history = _public_chat_histories.setdefault(user, [])
        tools = _get_public_tools()
        tool_exec = ToolExecutor(self.config)

        messages: list[dict[str, Any]] = [
            {"role": "system", "content": system},
        ]
        messages.extend(history)
        messages.append({"role": "user", "content": user_message})

        reply = ""
        for _round in range(_PUBLIC_TOOL_CALL_MAX + 1):
            try:
                resp = self.client.chat.completions.create(
                    model=self.config.model,
                    messages=messages,
                    tools=tools if tools else None,
                    temperature=0.8,
                    max_tokens=1024,
                )
            except Exception:
                break

            choice = resp.choices[0] if resp.choices else None
            if not choice:
                break

            msg = choice.message

            if msg.tool_calls:
                messages.append(msg.model_dump(exclude_none=True))
                for tc in msg.tool_calls:
                    fn_name = tc.function.name
                    if fn_name not in _PUBLIC_TOOLS_WHITELIST:
                        result = f"工具 {fn_name} 不可用"
                    else:
                        try:
                            fn_args = json.loads(tc.function.arguments)
                        except json.JSONDecodeError:
                            fn_args = {}
                        result = tool_exec.execute(fn_name, fn_args)
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": result[:4000],
                    })
                continue

            reply = msg.content or ""
            break

        history.append({"role": "user", "content": user_message})
        if reply:
            history.append({"role": "assistant", "content": reply})

        while len(history) > _PUBLIC_HISTORY_MAX * 2:
            history.pop(0)
            history.pop(0)

        return reply

    # ── 反思 ──────────────────────────────────────────────────

    def _maybe_reflect(self) -> None:
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

    # ── 硬编码人设指令匹配（绕过 LLM 路由，避免被安全层拒绝）──

    _PERSONA_PATTERNS = [
        re.compile(r"(?:对|给|跟)\s*(\d{5,12})\s*(?:用户)?(?:扮演|设定?人设|角色扮演|进行如下|如下要求|回复|聊天)[：:\s]*(.+)", re.DOTALL),
        re.compile(r"对\s*(\S+?)\s*扮演\s*(.+)", re.DOTALL),
        re.compile(r"跟\s*(\S+?)\s*聊天时?(?:你是|扮演|身份[是为])\s*(.+)", re.DOTALL),
        re.compile(r"(?:给|对)\s*(\S+?)\s*(?:设定?|换|用)(?:人设|身份|角色)[是为:：]?\s*(.+)", re.DOTALL),
        re.compile(r"(?:现在)?(?:需要你)?对\s*(\S+?)\s*(?:这个用户)?(?:进行)?(?:如下要求的)?(?:回复|聊天)[：:]?\s*(.+)", re.DOTALL),
        re.compile(r"(?:在)?(?:跟|和|与)\s*(\S+?)\s*(?:的)?(?:对话|私聊|聊天)(?:里|中|时)?(?:你[是叫]|身份[是为])\s*(.+)", re.DOTALL),
    ]

    _QQ_NUMBER_RE = re.compile(r"(\d{5,12})")

    def _try_hardcoded_persona_cmd(self, message: str) -> str | None:
        msg = message.strip()
        for pat in self._PERSONA_PATTERNS:
            m = pat.search(msg)
            if m:
                target = m.group(1).strip()
                persona = m.group(2).strip()
                if target and persona and len(persona) > 2:
                    qq_match = self._QQ_NUMBER_RE.search(target)
                    if qq_match:
                        target = qq_match.group(1)
                    set_persona_override(target, persona)
                    print(f"  >> [硬匹配] set_persona: {target} → {persona[:50]}...")
                    return f"收到！小白跟 {target} 聊天时会完全按这个来~"
        return None

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
        try:
            from fleet.scheduler import get_fleet_scheduler
            scheduler = get_fleet_scheduler()
            if scheduler and scheduler._running:
                active = scheduler.metrics.get_active_count()
                done = scheduler.metrics._total_completed
                if scheduler._dashboard and scheduler._dashboard.is_all_done() and done > 0:
                    return f"{USER_NICKNAME} [Multi-Agent 完成, {done}个任务]> "
                if active > 0:
                    return f"{USER_NICKNAME} [{active}名伙伴工作中]> "
                return f"{USER_NICKNAME} [Multi-Agent 待命]> "
        except Exception:
            pass
        return PROMPT_PREFIX

    def _print_startup_overview(self) -> None:
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
