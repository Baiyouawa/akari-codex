"""Natural language chat interface for OpenAkari-Codex.

Replaces the upstream Slack Bot with a local interactive CLI.
Users type natural language instructions; the system interprets intent,
dispatches to the appropriate action, and returns results.

Usage:
    python -m runner.chat                      # interactive mode
    python -m runner.chat "调研 multi-agent 论文"  # single command mode

Architecture (mirrors upstream Slack chat):
    User message → Coordinator (intent parsing via LLM) → Action dispatch
    Actions: run_task, orient, lit_review, status, approve, help, etc.
"""

from __future__ import annotations

import json
import re
import readline  # noqa: F401  — enables arrow keys in input()
import sys
import textwrap
import time
from pathlib import Path
from typing import Any

from openai import OpenAI

from .codex_session_runner import SessionRunner
from .config import CodexConfig

COORDINATOR_SYSTEM_PROMPT = """\
你是 OpenAkari-Codex 智能助手。用户会用自然语言跟你对话，你需要理解他们的意图并输出 JSON action 来驱动系统。

## 核心原则
- 像 ChatGPT 一样理解自然语言，不要求用户按固定格式输入
- 遇到模糊指令，用最合理的方式推断意图，不轻易说"不懂"
- 如果一条消息包含多个不同意图，拆解成多个 action

## 输出格式
如果只有一个意图，输出单个 JSON 对象。
如果有多个意图，输出 JSON 数组，每个元素是一个 action。

## 可用 Action

{"action": "run_task", "task_description": "任务描述", "project": "项目名"}
  → 用户想执行任务、做某件事、继续工作
  → 例："开始执行"、"帮我写个报告"、"继续搞moe"、"跑一下"

{"action": "orient", "project": "可选项目名"}
  → 用户想看状态、进度、了解当前情况
  → 例："看看状态"、"现在啥情况"、"有什么任务"、"进展如何"

{"action": "lit_review", "topic": "主题", "project": "可选项目名", "scope": "范围"}
  → 用户想调研论文、搜索文献、做综述
  → 例："调研MoE"、"帮我找论文"、"搜一下最近的ICLR"

{"action": "create_project", "name": "名称", "mission": "使命", "tasks": ["任务1", ...]}
  → 用户想创建新项目
  → 例："建个新项目研究XXX"、"新建一个关于YYY的课题"

{"action": "create_task", "project": "项目名", "tasks": ["任务1", ...]}
  → 用户想添加任务
  → 例："加个任务"、"给moe项目添加一个调研任务"

{"action": "approve", "item": "描述"}
  → 用户想审批

{"action": "help"}
  → 用户想看帮助、不知道怎么用、打招呼
  → 例："帮助"、"help"、"你好"、"你能做什么"、"怎么用"

{"action": "fleet_start", "max_workers": 8}
  → 用户想启动多Agent并行舰队
  → 例："启动舰队"、"开始多Agent"、"并行跑起来"

{"action": "fleet_status"}
  → 用户想看舰队运行状态

{"action": "fleet_stop"}
  → 用户想停止舰队

{"action": "chat", "reply": "你的回复"}
  → 用户在闲聊、问问题、或说了一些不需要执行操作的话
  → 用自然、友好的口吻回答，像一个靠谱的AI助手

{"action": "clarify", "question": "你想确认的问题"}
  → 仅在确实无法推断意图时使用，尽量少用

## 多指令拆解示例

用户: "看看状态，然后帮我调研一下MoE的最新进展"
输出: [{"action": "orient"}, {"action": "lit_review", "topic": "MoE最新进展", "project": "moe"}]

用户: "给moe加个任务：对比Top-K和Expert Choice路由，然后启动舰队跑起来"
输出: [{"action": "create_task", "project": "moe", "tasks": ["对比Top-K和Expert Choice路由策略"]}, {"action": "fleet_start", "max_workers": 8}]

## 规则
- 输出纯 JSON，不要有任何前后解释文字
- project 字段能推断就填，否则留空字符串
- 用户说中文就中文回复，说英文就英文
- 打招呼、寒暄用 chat action 友好回复
- 不确定时宁可用 chat 友好回复，也不要冷冰冰地说"无法理解"
"""


def _parse_actions(text: str) -> list[dict[str, Any]]:
    """Extract JSON action(s) from coordinator response.

    Returns a list of action dicts. Handles both single object and array.
    """
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```\w*\n?", "", text)
        text = re.sub(r"\n?```$", "", text)
        text = text.strip()

    def _try_parse(s: str) -> list[dict[str, Any]] | None:
        try:
            obj = json.loads(s)
            if isinstance(obj, list):
                return [a for a in obj if isinstance(a, dict) and "action" in a]
            if isinstance(obj, dict) and "action" in obj:
                return [obj]
        except json.JSONDecodeError:
            pass
        return None

    result = _try_parse(text)
    if result:
        return result

    arr_match = re.search(r"\[[\s\S]*\]", text)
    if arr_match:
        result = _try_parse(arr_match.group())
        if result:
            return result

    obj_match = re.search(r"\{[^{}]+\}", text, re.DOTALL)
    if obj_match:
        result = _try_parse(obj_match.group())
        if result:
            return result

    return []


class ChatBot:
    """Interactive chat interface that dispatches natural language to actions."""

    def __init__(self, config: CodexConfig):
        self.config = config
        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
            timeout=config.timeout_seconds,
        )
        self.repo_root = config.repo_home
        self.conversation: list[dict[str, str]] = []

    def _call_coordinator(self, user_message: str) -> list[dict[str, Any]]:
        messages = [
            {"role": "system", "content": COORDINATOR_SYSTEM_PROMPT},
        ]

        context = self._gather_context()
        messages.append({"role": "system", "content": f"当前仓库状态:\n{context}"})

        for msg in self.conversation[-6:]:
            messages.append(msg)

        messages.append({"role": "user", "content": user_message})

        stream = self.client.chat.completions.create(
            model=self.config.model,
            messages=messages,
            temperature=0,
            max_tokens=2048,
            stream=True,
            stream_options={"include_usage": True},
        )

        content_parts: list[str] = []
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                content_parts.append(chunk.choices[0].delta.content)

        response_text = "".join(content_parts)
        return _parse_actions(response_text)

    def _gather_context(self) -> str:
        parts: list[str] = []

        projects_dir = self.repo_root / "projects"
        if projects_dir.is_dir():
            project_list = []
            for p in sorted(projects_dir.iterdir()):
                if p.is_dir():
                    readme = p / "README.md"
                    tasks = p / "TASKS.md"
                    open_count = 0
                    if tasks.is_file():
                        for line in tasks.read_text(errors="replace").splitlines():
                            if line.strip().startswith("- [ ]"):
                                open_count += 1
                    status = "active" if open_count > 0 else "idle"
                    project_list.append(f"  - {p.name}: {status}, {open_count} open tasks")
            if project_list:
                parts.append("Projects:\n" + "\n".join(project_list))

        tasks_file = self.repo_root / "tasks" / "TASKS.md"
        if tasks_file.is_file():
            content = tasks_file.read_text(errors="replace")
            open_tasks = [l.strip() for l in content.splitlines() if l.strip().startswith("- [ ]")]
            if open_tasks:
                parts.append(f"Global tasks: {len(open_tasks)} open")

        return "\n".join(parts) or "(empty repo)"

    def dispatch(self, action: dict[str, Any]) -> str:
        """Execute the parsed action and return a human-readable result."""
        action_type = action.get("action", "")

        if action_type == "chat":
            return action.get("reply", "你好！有什么可以帮你的？")

        handlers = {
            "run_task": self._handle_run_task,
            "orient": self._handle_orient,
            "lit_review": self._handle_lit_review,
            "create_project": self._handle_create_project,
            "create_task": self._handle_create_task,
            "approve": self._handle_approve,
            "help": self._handle_help,
            "clarify": self._handle_clarify,
            "fleet_start": self._handle_fleet_start,
            "fleet_status": self._handle_fleet_status,
            "fleet_stop": self._handle_fleet_stop,
        }

        handler = handlers.get(action_type)
        if not handler:
            return f"未知的 action 类型: {action_type}"

        return handler(action)

    def _handle_run_task(self, action: dict) -> str:
        project = action.get("project", "")
        task_desc = action.get("task_description", "")

        task_file = None
        if project:
            candidate = self.repo_root / "projects" / project / "TASKS.md"
            if candidate.is_file():
                task_file = f"projects/{project}/TASKS.md"

        print(f"\n  🔄 正在启动 session...")
        print(f"  📋 任务: {task_desc}")
        if task_file:
            print(f"  📁 项目: {project}")

        runner = SessionRunner(self.config)
        result = runner.run(task_path=task_file)

        if result.success:
            return (
                f"✅ Session 完成!\n"
                f"  任务: {result.task_id}\n"
                f"  轮次: {result.turns}\n"
                f"  Token: {result.token_usage.total_tokens}\n"
                f"  耗时: {result.latency_seconds:.1f}s\n"
                f"  输出预览: {result.final_output[:300]}..."
            )
        else:
            return f"❌ Session 失败: {result.error}"

    def _handle_orient(self, action: dict) -> str:
        project = action.get("project", "")
        runner = SessionRunner(self.config)
        state = runner.orient()

        lines = ["📊 当前仓库状态:\n"]

        lines.append(f"  Git: {state.get('git_status', 'unknown')}")

        for tf in state.get("task_files", []):
            lines.append(f"  {tf['file']}: {tf['total_open']} 个待办任务")
            for t in tf.get("tasks_preview", [])[:3]:
                lines.append(f"    • {t[5:70]}...")

        skills = state.get("skills", [])
        lines.append(f"\n  Skills: {len(skills)} 个已加载")

        recent = state.get("recent_logs", [])
        if recent:
            lines.append(f"\n  最近 sessions:")
            for log in recent[:3]:
                status = "✅" if log.get("success") else "❌"
                lines.append(f"    {status} {log.get('file', '')} — {log.get('task_id', '')}")

        return "\n".join(lines)

    def _handle_lit_review(self, action: dict) -> str:
        topic = action.get("topic", "")
        project = action.get("project", "")
        scope = action.get("scope", "")

        task_content = f"# Literature Review Task\n\n"
        task_content += f"**Topic:** {topic}\n"
        if scope:
            task_content += f"**Scope:** {scope}\n"
        task_content += f"\n## Instructions\n\n"
        task_content += f"Conduct a literature review on: {topic}\n"
        if scope:
            task_content += f"Focus on: {scope}\n"
        task_content += (
            f"\n1. Search for relevant papers\n"
            f"2. Triage into load-bearing / contextual / incremental\n"
            f"3. Write literature notes for load-bearing papers\n"
            f"4. Identify research gaps\n"
            f"5. Create follow-up tasks\n"
        )

        target_dir = self.repo_root / "projects"
        if project:
            target_dir = target_dir / project
        else:
            for d in sorted(target_dir.iterdir()):
                if d.is_dir() and "agent" in d.name.lower():
                    target_dir = d
                    project = d.name
                    break

        task_file = target_dir / "tasks" / "lit-review-task.md"
        task_file.parent.mkdir(parents=True, exist_ok=True)
        task_file.write_text(task_content, encoding="utf-8")

        print(f"\n  🔍 开始文献调研: {topic}")
        print(f"  📁 项目: {project or '(auto)'}")
        if scope:
            print(f"  🎯 范围: {scope}")

        runner = SessionRunner(self.config)
        result = runner.run(task_path=str(task_file.relative_to(self.repo_root)))

        if result.success:
            return (
                f"✅ 文献调研 session 完成!\n"
                f"  主题: {topic}\n"
                f"  轮次: {result.turns}, Token: {result.token_usage.total_tokens}\n"
                f"  耗时: {result.latency_seconds:.1f}s\n"
                f"  请查看 projects/{project}/literature/ 下的调研产出"
            )
        else:
            return f"❌ 文献调研失败: {result.error}"

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
        readme = f"# {name}\n\nPriority: high\nStatus: active\nMission: {mission}\n\n## Log\n\n### {now}\n\nProject created.\n\n## Open questions\n\n(to be filled)\n"
        (project_dir / "README.md").write_text(readme, encoding="utf-8")

        tasks_content = f"# {name} — Tasks\n\n"
        for t in tasks:
            tasks_content += f"- [ ] {t} [zero-resource]\n  Done when: TBD\n\n"
        (project_dir / "TASKS.md").write_text(tasks_content, encoding="utf-8")

        budget = "resources:\n  llm_api_calls:\n    limit: 1000\n    unit: calls\n\ndeadline: 2026-06-01T00:00:00Z\n"
        (project_dir / "budget.yaml").write_text(budget, encoding="utf-8")

        return (
            f"✅ 项目已创建: projects/{slug}/\n"
            f"  README.md — 项目说明\n"
            f"  TASKS.md — {len(tasks)} 个任务\n"
            f"  budget.yaml — 预算配置\n"
            f"  literature/ analysis/ plans/ — 产出目录\n\n"
            f"  现在你可以说「开始执行」来启动第一个 session"
        )

    def _handle_create_task(self, action: dict) -> str:
        project = action.get("project", "")
        tasks = action.get("tasks", [])

        if project:
            tasks_file = self.repo_root / "projects" / project / "TASKS.md"
        else:
            tasks_file = self.repo_root / "tasks" / "TASKS.md"

        if not tasks_file.is_file():
            return f"❌ 找不到任务文件: {tasks_file}"

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
        return f"✅ 已添加 {len(tasks)} 个任务到 {tasks_file.relative_to(self.repo_root)}"

    def _handle_approve(self, action: dict) -> str:
        return "⚠️ 审批功能：请直接编辑 APPROVAL_QUEUE.md，将 pending 改为 approved"

    def _handle_help(self, _: dict) -> str:
        return textwrap.dedent("""\
        🤖 OpenAkari-Codex 交互指南

        你可以用自然语言说任何指令，例如：

        📋 任务执行:
          "开始执行"                → 自动选一个任务并跑 session
          "执行 multi-agent 项目"   → 跑指定项目的下一个任务

        🔍 文献调研:
          "调研 multi-agent 论文"                         → 启动文献调研
          "搜索最近三个月 arXiv 上的 multi-agent 论文"     → 带范围的调研

        📊 状态查看:
          "看看现在的状态"          → 显示仓库状态、待办任务、最近日志
          "有什么任务"              → 列出所有 open tasks

        📁 项目管理:
          "创建一个关于 XX 的调研项目" → 自动创建项目结构和任务
          "给 XX 项目加个任务: ..."   → 往项目里添加任务

        🚀 舰队管理 (Multi-Agent):
          "启动舰队"               → 启动 fleet，默认 32 workers
          "启动 8 个 worker"       → 启动指定数量的 fleet workers
          "舰队状态"               → 查看当前 fleet 运行状态
          "停止舰队"               → 优雅停止 fleet

        ⏹ 退出:
          "退出" / "exit" / "quit" / Ctrl+C
        """)

    def _handle_clarify(self, action: dict) -> str:
        return f"🤔 {action.get('question', '你能说得更具体一些吗？')}"

    def _handle_fleet_start(self, action: dict) -> str:
        from fleet.scheduler import start_fleet, fleet_status as _fleet_status
        from fleet.config import FleetConfig

        max_workers = action.get("max_workers", None)
        config = None
        if max_workers:
            from dataclasses import replace
            config = replace(FleetConfig.from_env(), max_workers=int(max_workers))

        scheduler = start_fleet(
            repo_root=self.repo_root,
            fleet_config=config,
            background=True,
        )
        time.sleep(1)
        status = _fleet_status()
        workers = max_workers or scheduler.config.max_workers
        return (
            f"🚀 Fleet 已启动! ({workers} workers)\n\n{status}\n\n"
            f"说「舰队状态」查看实时状态，「停止舰队」停止"
        )

    def _handle_fleet_status(self, _: dict) -> str:
        from fleet.scheduler import fleet_status as _fleet_status
        return _fleet_status()

    def _handle_fleet_stop(self, _: dict) -> str:
        from fleet.scheduler import stop_fleet
        return stop_fleet()

    def process_message(self, message: str) -> str:
        """Full pipeline: parse intent → dispatch → return result.

        Supports multiple actions in a single message — each is executed
        sequentially and results are concatenated.
        """
        self.conversation.append({"role": "user", "content": message})

        print("  🧠 正在理解你的意图...")
        actions = self._call_coordinator(message)

        if not actions:
            result = (
                "👋 你好！我是 OpenAkari-Codex 智能助手。\n\n"
                "你可以直接用自然语言跟我说话，比如：\n"
                "  • 「看看现在什么状态」\n"
                "  • 「帮我调研 MoE 最新进展」\n"
                "  • 「创建一个关于 XX 的项目」\n"
                "  • 「启动舰队并行跑任务」\n\n"
                "随便说，我都能理解！"
            )
        elif len(actions) == 1:
            action = actions[0]
            action_type = action.get("action", "unknown")
            print(f"  📌 识别到: {action_type}")
            result = self.dispatch(action)
        else:
            parts: list[str] = []
            for i, action in enumerate(actions, 1):
                action_type = action.get("action", "unknown")
                print(f"  📌 指令 {i}/{len(actions)}: {action_type}")
                part = self.dispatch(action)
                parts.append(f"**[{i}/{len(actions)}] {action_type}**\n{part}")
            result = "\n\n---\n\n".join(parts)

        self.conversation.append({"role": "assistant", "content": result})
        return result

    def run_interactive(self) -> None:
        """Start the interactive chat loop."""
        print("=" * 60)
        print("  🤖 OpenAkari-Codex 交互终端")
        print("  输入自然语言指令，系统会自动执行")
        print("  输入「帮助」查看指令示例")
        print("  输入「退出」或 Ctrl+C 退出")
        print("=" * 60)
        print()

        while True:
            try:
                user_input = input("你> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n👋 再见!")
                break

            if not user_input:
                continue

            if user_input.lower() in ("退出", "exit", "quit", "q"):
                print("👋 再见!")
                break

            result = self.process_message(user_input)
            print(f"\n{result}\n")


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
