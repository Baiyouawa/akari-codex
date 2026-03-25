"""小白顶层 Agent 多轮推理循环。

小白不是路由器，而是一个真正的顶层智能 Agent。
每轮循环：思考 → 选择 Skill → 执行 → 观察结果 → 再思考 → …… → 最终回复

支持五种 action:
  think       — 显式推理（分析任务、选择策略）
  use_skill   — 调用一个 Skill（原子/复合/系统）
  delegate    — 将任务分配给 Multi-Agent 系统
  progress    — 向用户播报当前进展
  reply       — 最终回复，结束循环
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from openai import OpenAI

from .config import CodexConfig
from .skill_registry import SkillRegistry
from .tools import ToolExecutor


@dataclass
class AgentResult:
    """Agent 循环的最终结果。"""

    reply: str
    turns: int = 0
    skills_used: list[str] = field(default_factory=list)
    delegated: bool = False
    progress_log: list[str] = field(default_factory=list)
    error: str | None = None


ProgressCallback = Callable[[str], None]

_API_MAX_RETRIES = 3
_API_RETRY_DELAY = 3


class AgentLoop:
    """小白的多轮推理循环。

    每一轮，LLM 输出一个 JSON action，AgentLoop 执行后把结果
    反馈到 messages 中继续下一轮，直到 LLM 输出 reply 或达到最大轮次。
    """

    def __init__(
        self,
        config: CodexConfig,
        skill_registry: SkillRegistry,
        system_prompt: str,
        memory_context: str = "",
        repo_context: str = "",
        progress_callback: ProgressCallback | None = None,
        max_turns: int = 0,
    ):
        self.config = config
        self.registry = skill_registry
        self.tool_executor = ToolExecutor(config)
        self.progress_callback = progress_callback
        self.max_turns = max_turns or config.max_turns

        self._system_prompt = system_prompt
        self._memory_context = memory_context
        self._repo_context = repo_context

        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
            timeout=config.timeout_seconds,
        )

        self._active_skill_guide: str | None = None

    # ── 主循环 ────────────────────────────────────────────────

    def run(self, user_message: str) -> AgentResult:
        """运行多轮 Agent 循环，返回最终结果。"""
        result = AgentResult(reply="")
        messages = self._build_initial_messages(user_message)

        for turn in range(self.max_turns):
            result.turns = turn + 1

            raw_text = self._call_llm(messages)
            if not raw_text:
                result.reply = "小白脑子空白了...(｡•́︿•̀｡)"
                result.error = "LLM returned empty response"
                break

            action = self._parse_action(raw_text)
            if not action:
                result.reply = raw_text
                break

            action_type = action.get("action", "")

            if action_type == "reply":
                result.reply = action.get("message", raw_text)
                break

            if action_type == "think":
                thought = action.get("thought", "")
                messages.append({"role": "assistant", "content": raw_text})
                messages.append({
                    "role": "user",
                    "content": f"[系统] 好的，继续。根据你的分析决定下一步行动。",
                })
                continue

            if action_type == "progress":
                msg = action.get("message", "")
                result.progress_log.append(msg)
                if self.progress_callback:
                    self.progress_callback(msg)
                messages.append({"role": "assistant", "content": raw_text})
                messages.append({
                    "role": "user",
                    "content": "[系统] 已播报进展，继续执行。",
                })
                continue

            if action_type == "use_skill":
                skill_name = action.get("skill", "")
                skill_args = action.get("args", {})
                result.skills_used.append(skill_name)

                messages.append({"role": "assistant", "content": raw_text})
                skill_result = self._execute_skill(skill_name, skill_args, messages)
                messages.append({
                    "role": "user",
                    "content": f"[Skill 执行结果: {skill_name}]\n\n{skill_result}",
                })
                continue

            if action_type == "delegate":
                result.delegated = True
                messages.append({"role": "assistant", "content": raw_text})
                delegate_result = self._execute_delegate(action)
                messages.append({
                    "role": "user",
                    "content": f"[Multi-Agent 调度结果]\n\n{delegate_result}",
                })
                continue

            messages.append({"role": "assistant", "content": raw_text})
            messages.append({
                "role": "user",
                "content": f"[系统] 未知的 action: {action_type}，请输出有效的 action。",
            })
        else:
            if not result.reply:
                result.reply = "小白想了太久了，先把目前的结果告诉你~"
                result.error = f"达到最大轮次 ({self.max_turns})"

        return result

    # ── 消息构建 ──────────────────────────────────────────────

    def _build_initial_messages(self, user_message: str) -> list[dict[str, str]]:
        system_parts = [self._system_prompt]

        skill_catalog = self.registry.build_skill_catalog()
        system_parts.append(f"\n\n## 你的 Skill 清单\n\n{skill_catalog}")

        if self._memory_context:
            system_parts.append(f"\n\n{self._memory_context}")
        if self._repo_context:
            system_parts.append(f"\n\n## 当前仓库状态\n{self._repo_context}")

        return [
            {"role": "system", "content": "\n".join(system_parts)},
            {"role": "user", "content": user_message},
        ]

    # ── LLM 调用 ─────────────────────────────────────────────

    def _call_llm(self, messages: list[dict[str, Any]]) -> str:
        last_err = None
        for attempt in range(1, _API_MAX_RETRIES + 1):
            try:
                stream = self.client.chat.completions.create(
                    model=self.config.model,
                    messages=messages,
                    stream=True,
                    temperature=0.3,
                    max_tokens=4096,
                )
                parts: list[str] = []
                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta.content:
                        parts.append(chunk.choices[0].delta.content)
                return "".join(parts)
            except Exception as e:
                last_err = e
                if attempt < _API_MAX_RETRIES:
                    time.sleep(_API_RETRY_DELAY * attempt)
        return f"[API 错误: {last_err}]"

    # ── Action 解析 ───────────────────────────────────────────

    def _parse_action(self, text: str) -> dict[str, Any] | None:
        """从 LLM 输出中提取 JSON action。

        支持多种格式：纯 JSON、markdown code block 包裹、或混合文本中的 JSON。
        如果完全没有 JSON，视为直接 reply。
        """
        cleaned = text.strip()

        if cleaned.startswith("```"):
            cleaned = re.sub(r"^```\w*\n?", "", cleaned)
            cleaned = re.sub(r"\n?```$", "", cleaned)
            cleaned = cleaned.strip()

        try:
            obj = json.loads(cleaned)
            if isinstance(obj, dict) and "action" in obj:
                return obj
        except json.JSONDecodeError:
            pass

        match = re.search(r"\{[^{}]*\"action\"\s*:[^{}]*\}", text)
        if match:
            try:
                obj = json.loads(match.group())
                if isinstance(obj, dict) and "action" in obj:
                    return obj
            except json.JSONDecodeError:
                pass

        match = re.search(r"\{[\s\S]*\"action\"\s*:[\s\S]*\}", text)
        if match:
            try:
                obj = json.loads(match.group())
                if isinstance(obj, dict) and "action" in obj:
                    return obj
            except json.JSONDecodeError:
                pass

        return None

    # ── Skill 执行 ───────────────────────────────────────────

    def _execute_skill(
        self,
        skill_name: str,
        args: dict[str, Any],
        messages: list[dict[str, str]],
    ) -> str:
        skill = self.registry.get(skill_name)
        if not skill:
            return f"未知的 Skill: {skill_name}"

        if skill.category == "atomic":
            return self._execute_atomic(skill_name, args)

        if skill.category == "compound":
            return self._execute_compound(skill_name, args, messages)

        if skill.category == "system":
            return self._execute_system(skill_name, args)

        return f"不支持的 Skill 类型: {skill.category}"

    def _execute_atomic(self, skill_name: str, args: dict[str, Any]) -> str:
        """执行原子 Skill（tools.py 工具）。"""
        return self.tool_executor.execute(skill_name, args)

    def _execute_compound(
        self,
        skill_name: str,
        args: dict[str, Any],
        messages: list[dict[str, str]],
    ) -> str:
        """执行复合 Skill：读取 SKILL.md 注入为指导，由 Agent 后续轮次按步骤执行。

        复合 Skill 不在此处一次性完成，而是将 SKILL.md 内容注入到对话中，
        让 Agent 在后续轮次中按步骤调用原子 Skill 完成。
        """
        guide = self.registry.load_skill_guide(skill_name)
        if not guide:
            return f"找不到 Skill 指南: {skill_name}"

        self._active_skill_guide = skill_name
        args_desc = json.dumps(args, ensure_ascii=False) if args else "无额外参数"

        return (
            f"[已加载复合 Skill: {skill_name}]\n\n"
            f"参数: {args_desc}\n\n"
            f"以下是该 Skill 的完整执行指南，请按步骤执行：\n\n"
            f"---\n{guide}\n---\n\n"
            f"现在请按照上述指南的步骤，依次使用 use_skill 调用需要的原子工具完成任务。"
            f"每完成一步，用 progress 播报进展。全部完成后用 reply 汇报最终结果。"
        )

    def _execute_system(self, skill_name: str, args: dict[str, Any]) -> str:
        """执行系统 Skill（备忘/提醒/项目管理/人设/Multi-Agent/多媒体/电话）。"""
        repo = self.config.repo_home

        if skill_name.startswith(("send_", "recognize_", "tts_")):
            return self._execute_media_skill(skill_name, args)
        if skill_name.startswith(("read_system", "list_system", "request_file", "get_file_for")):
            return self._execute_file_skill(skill_name, args)
        if skill_name.startswith("phone_"):
            return self._execute_phone_skill(skill_name, args)

        from . import memo
        from .persona import (
            set_persona_override,
            clear_persona_override,
            list_persona_overrides,
        )

        if skill_name == "memo_add":
            content = args.get("content", "")
            if not content:
                return "备忘内容不能为空"
            memo_id = memo.add_memo(repo, content)
            return f"已记录备忘 (ID: {memo_id}): {content}"

        if skill_name == "memo_list":
            memos = memo.list_memos(repo)
            return memo.format_memos(memos)

        if skill_name == "memo_complete":
            memo_id = args.get("id", "")
            if memo.complete_memo(repo, memo_id):
                return f"备忘 {memo_id} 已完成"
            return f"找不到备忘: {memo_id}"

        if skill_name == "reminder_add":
            content = args.get("content", "")
            remind_time = args.get("time", "")
            if not content:
                return "提醒内容不能为空"
            rid = memo.add_reminder(repo, content, remind_time)
            return f"已设置提醒 (ID: {rid}): {content} — {remind_time}"

        if skill_name == "reminder_list":
            reminders = memo.list_reminders(repo)
            return memo.format_reminders(reminders)

        if skill_name == "create_project":
            return self._sys_create_project(args)

        if skill_name == "create_task":
            return self._sys_create_task(args)

        if skill_name == "orient":
            return self._sys_orient(args)

        if skill_name == "set_persona":
            target = args.get("target", "")
            persona = args.get("persona", "")
            if not target or not persona:
                return "需要指定目标用户和角色描述"
            set_persona_override(target, persona)
            return f"收到！小白跟 {target} 聊天时会扮演: {persona}"

        if skill_name == "clear_persona":
            target = args.get("target", "")
            if not target:
                return "需要指定要取消人设的用户"
            if clear_persona_override(target):
                return f"已取消对 {target} 的角色扮演，恢复默认"
            return f"没有找到对 {target} 的角色扮演设定"

        if skill_name == "list_personas":
            overrides = list_persona_overrides()
            if not overrides:
                return "目前没有设定任何角色扮演"
            lines = ["当前角色扮演列表:"]
            for target, desc in overrides.items():
                lines.append(f"  {target} → {desc[:60]}")
            return "\n".join(lines)

        if skill_name.startswith("multiagent_"):
            return self._sys_multiagent(skill_name, args)

        return f"未实现的系统 Skill: {skill_name}"

    # ── 多媒体 Skill 执行 ─────────────────────────────────────

    def _execute_media_skill(self, skill_name: str, args: dict[str, Any]) -> str:
        """执行多媒体相关 Skill。"""
        from . import media_tools

        if skill_name == "send_image":
            path_or_url = args.get("path", "") or args.get("url", "")
            if not path_or_url:
                return "需要指定图片路径或 URL"
            cq = media_tools.build_image_cq(path_or_url)
            return f"[发送图片指令] 请在回复中包含: [IMG:{path_or_url}]\n(CQ码: {cq})"

        if skill_name == "recognize_image":
            source = args.get("path_or_url", "") or args.get("url", "") or args.get("path", "")
            prompt = args.get("prompt", "用一两句话简短描述这张图片的主要内容")
            if not source:
                return "需要指定图片路径或 URL"
            return media_tools.recognize_image(source, prompt)

        if skill_name == "send_voice":
            text = args.get("text", "")
            if not text:
                return "需要指定要说的文字内容"
            return f"[发送语音指令] 请在回复中包含: [VOICE:{text}]"

        if skill_name == "recognize_speech":
            audio_path = args.get("audio_path", "") or args.get("path", "")
            if not audio_path:
                return "需要指定音频文件路径"
            return media_tools.recognize_speech(audio_path)

        if skill_name == "send_file":
            path = args.get("path", "")
            if not path:
                return "需要指定文件路径"
            info = media_tools.get_file_for_send(path)
            if "error" in info:
                return info["error"]
            return (
                f"[发送文件指令] 请在回复中包含: [FILE:{info['path']}]\n"
                f"文件: {info['name']} ({info['size']} bytes, {info['mime']})"
            )

        if skill_name == "send_emoji":
            face_id = args.get("id", args.get("face_id", 0))
            return f"[发送表情指令] 请在回复中包含: [FACE:{face_id}]"

        if skill_name == "tts_generate":
            text = args.get("text", "")
            voice = args.get("voice", "")
            if not text:
                return "需要指定要合成的文字"
            try:
                audio_path = media_tools.tts_generate(text, voice=voice)
                return f"语音已合成: {audio_path} ({audio_path.stat().st_size} bytes)"
            except Exception as e:
                return f"TTS 合成失败: {e}"

        return f"未知的多媒体 Skill: {skill_name}"

    # ── 文件系统 Skill 执行 ───────────────────────────────────

    def _execute_file_skill(self, skill_name: str, args: dict[str, Any]) -> str:
        """执行文件系统访问 Skill。"""
        from . import media_tools

        if skill_name == "read_system_file":
            path = args.get("path", "")
            if not path:
                return "需要指定文件路径"
            return media_tools.read_system_file(path)

        if skill_name == "list_system_dir":
            path = args.get("path", "")
            if not path:
                return "需要指定目录路径"
            return media_tools.list_system_dir(path)

        if skill_name == "request_file_delete":
            path = args.get("path", "")
            if not path:
                return "需要指定要删除的路径"
            return media_tools.request_file_delete(path, self.config.repo_home)

        if skill_name == "get_file_for_send":
            path = args.get("path", "")
            if not path:
                return "需要指定文件路径"
            import json as _json
            return _json.dumps(media_tools.get_file_for_send(path), ensure_ascii=False)

        return f"未知的文件 Skill: {skill_name}"

    # ── 电话 Skill 执行 ──────────────────────────────────────

    def _execute_phone_skill(self, skill_name: str, args: dict[str, Any]) -> str:
        """执行电话相关 Skill。"""
        from . import phone_tools

        if skill_name == "phone_check_setup":
            import json as _json
            return _json.dumps(phone_tools.check_phone_setup(), ensure_ascii=False, indent=2)

        if skill_name == "phone_call_notification":
            phone_number = args.get("phone_number", "")
            message = args.get("message", "")
            if not phone_number or not message:
                return "需要指定电话号码和消息内容"
            result = phone_tools.make_notification_call(
                phone_number, message,
                voice=args.get("voice", ""),
                repo_root=self.config.repo_home,
            )
            import json as _json
            return _json.dumps(result, ensure_ascii=False, indent=2)

        if skill_name == "phone_call_realtime":
            phone_number = args.get("phone_number", "")
            if not phone_number:
                return "需要指定电话号码"
            result = phone_tools.make_realtime_call(
                phone_number,
                system_prompt=args.get("system_prompt", ""),
                repo_root=self.config.repo_home,
                progress_callback=self.progress_callback,
            )
            import json as _json
            return _json.dumps(result, ensure_ascii=False, indent=2)

        if skill_name == "phone_call_status":
            call_id = args.get("call_id", "")
            if not call_id:
                return "需要指定通话 ID"
            import json as _json
            return _json.dumps(phone_tools.get_call_status(call_id), ensure_ascii=False, indent=2)

        if skill_name == "phone_recent_calls":
            import json as _json
            calls = phone_tools.list_recent_calls(self.config.repo_home)
            if not calls:
                return "暂无通话记录"
            return _json.dumps(calls, ensure_ascii=False, indent=2)

        return f"未知的电话 Skill: {skill_name}"

    # ── Multi-Agent 调度 ──────────────────────────────────────

    def _execute_delegate(self, action: dict[str, Any]) -> str:
        """处理 delegate action：启动 Multi-Agent 系统执行任务。"""
        tasks = action.get("tasks", [])
        max_workers = action.get("max_workers", 4)
        project = action.get("project", "")
        reason = action.get("reason", "")

        return self._sys_multiagent("multiagent_start", {
            "max_workers": max_workers,
            "project": project,
            "tasks": tasks,
            "reason": reason,
        })

    def _sys_multiagent(self, skill_name: str, args: dict[str, Any]) -> str:
        """Multi-Agent 系统操作。"""
        try:
            from fleet.scheduler import (
                start_fleet, stop_fleet, fleet_status as _fleet_status,
                get_fleet_scheduler,
            )
            from fleet.config import FleetConfig
            from dataclasses import replace as dc_replace
        except ImportError:
            return "Multi-Agent 系统模块不可用"

        if skill_name == "multiagent_start":
            project = args.get("project", "")
            tasks = args.get("tasks", [])

            if tasks and project:
                self._ensure_project_tasks(project, tasks, args.get("reason", ""))

            existing = get_fleet_scheduler()
            if existing and existing._running:
                if project:
                    existing.add_project_filter(project)
                    pf = existing.config.project_filter
                    return f"Multi-Agent 系统运行中，已加入项目: {', '.join(sorted(pf))}"
                active = existing.metrics.get_active_count()
                done = existing.metrics._total_completed
                return f"Multi-Agent 系统已在运行 (工作中: {active}, 已完成: {done})"

            fleet_config = FleetConfig.from_env()
            max_workers = args.get("max_workers")
            n = int(max_workers) if max_workers else min(4, fleet_config.max_workers)
            proj_filter = frozenset({project}) if project else frozenset()
            fleet_config = dc_replace(
                fleet_config,
                max_workers=n,
                project_filter=proj_filter,
                idle_exploration_enabled=not bool(proj_filter),
            )
            scope = f" (仅 {project})" if project else " (所有项目)"
            start_fleet(
                repo_root=self.config.repo_home,
                fleet_config=fleet_config,
                background=True,
            )
            import time as _time
            _time.sleep(1)
            return f"Multi-Agent 系统已启动! {n} 个 Agent 出发{scope}\n\n{_fleet_status()}"

        if skill_name == "multiagent_status":
            scheduler = get_fleet_scheduler()
            if not scheduler or not scheduler._running:
                return "Multi-Agent 系统目前没有运行"
            if scheduler._dashboard:
                return scheduler._dashboard.render_snapshot()
            return _fleet_status()

        if skill_name == "multiagent_stop":
            scheduler = get_fleet_scheduler()
            if not scheduler or not scheduler._running:
                return "Multi-Agent 系统没有在运行"
            return stop_fleet()

        if skill_name == "multiagent_report":
            scheduler = get_fleet_scheduler()
            if not scheduler or not scheduler._dashboard:
                return "目前没有执行记录"
            return scheduler._dashboard.render_report()

        if skill_name == "multiagent_scale":
            count = args.get("count", 0)
            if not count:
                return "请指定要调整到几个 Agent"
            n = int(count)
            scheduler = get_fleet_scheduler()
            if scheduler and scheduler._running:
                scheduler.config = dc_replace(scheduler.config, max_workers=n)
                scheduler.metrics._max_workers = n
                return f"Worker 上限已调整为 {n} 个"
            return f"Multi-Agent 系统没有在运行"

        if skill_name == "multiagent_tasks":
            from fleet.task_scanner import scan_available_tasks
            tasks = scan_available_tasks(self.config.repo_home)
            eligible = [t for t in tasks if t.fleet_eligible and not t.blocked]
            if not eligible:
                return "目前没有可执行的任务"
            lines = [f"可执行任务 ({len(eligible)} 个):"]
            for i, t in enumerate(eligible[:15], 1):
                skill = f"[{t.skill_type.value}]" if t.skill_type else ""
                lines.append(f"  {i:2d}. [{t.project}] {t.text[:60]} {skill}")
            if len(eligible) > 15:
                lines.append(f"  ... 还有 {len(eligible) - 15} 个")
            return "\n".join(lines)

        return f"未知的 Multi-Agent 操作: {skill_name}"

    # ── Fleet 任务落盘 ─────────────────────────────────────────

    def _ensure_project_tasks(
        self,
        project: str,
        tasks: list[str],
        reason: str = "",
    ) -> None:
        """Ensure project dir and TASKS.md exist, then append tasks for fleet scanner.

        This bridges the gap between the delegate/multiagent_start action
        (which carries a tasks list) and the fleet scheduler (which reads
        TASKS.md on disk).  Without this, the scheduler starts but finds
        0 ready tasks and never spawns workers.
        """
        repo = self.config.repo_home
        slug = re.sub(r"[^a-z0-9-]", "-", project.lower()).strip("-")
        project_dir = repo / "projects" / slug
        tasks_file = project_dir / "TASKS.md"

        if not project_dir.is_dir():
            project_dir.mkdir(parents=True, exist_ok=True)
            for sub in ("literature", "analysis", "plans", "logs"):
                (project_dir / sub).mkdir(exist_ok=True)
            import time as _t
            now = _t.strftime("%Y-%m-%d")
            readme = (
                f"# {project}\n\nPriority: high\nStatus: active\n"
                f"Mission: {reason or project}\n\n## Log\n\n### {now}\n\n项目创建。\n"
            )
            (project_dir / "README.md").write_text(readme, encoding="utf-8")

        if not tasks_file.is_file():
            tasks_file.write_text(
                f"# {project} — 任务列表\n\n", encoding="utf-8"
            )

        existing_content = tasks_file.read_text(encoding="utf-8")
        new_entries = ""
        for t in tasks:
            t = t.strip()
            if not t or t in existing_content:
                continue
            new_entries += f"- [ ] {t} [zero-resource]\n  Done when: TBD\n\n"

        if new_entries:
            tasks_file.write_text(
                existing_content.rstrip("\n") + "\n\n" + new_entries,
                encoding="utf-8",
            )

    # ── 系统操作辅助 ──────────────────────────────────────────

    def _sys_create_project(self, args: dict[str, Any]) -> str:
        name = args.get("name", "new-project")
        mission = args.get("mission", "")
        tasks = args.get("tasks", [])
        repo = self.config.repo_home

        slug = re.sub(r"[^a-z0-9-]", "-", name.lower()).strip("-")
        project_dir = repo / "projects" / slug
        project_dir.mkdir(parents=True, exist_ok=True)
        (project_dir / "literature").mkdir(exist_ok=True)
        (project_dir / "analysis").mkdir(exist_ok=True)
        (project_dir / "plans").mkdir(exist_ok=True)

        import time as _time
        now = _time.strftime("%Y-%m-%d")
        readme = (
            f"# {name}\n\nPriority: high\nStatus: active\n"
            f"Mission: {mission}\n\n## Log\n\n### {now}\n\n项目创建。\n"
        )
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

    def _sys_create_task(self, args: dict[str, Any]) -> str:
        project = args.get("project", "")
        tasks = args.get("tasks", [])
        repo = self.config.repo_home

        if project:
            tasks_file = repo / "projects" / project / "TASKS.md"
        else:
            tasks_file = repo / "tasks" / "TASKS.md"

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
        return f"已添加 {len(tasks)} 个任务到 {tasks_file.relative_to(repo)}"

    def _sys_orient(self, args: dict[str, Any]) -> str:
        from .codex_session_runner import SessionRunner
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
                lines.append(
                    f"    [{status}] {log.get('file', '')} — {log.get('task_id', '')}"
                )

        return "\n".join(lines)
