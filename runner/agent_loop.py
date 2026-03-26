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

            action_queue = self._parse_all_actions(raw_text)
            if not action_queue:
                result.reply = self._fallback_reply(raw_text)
                break

            # 整段模型输出只记一次 assistant，避免重复；多段 JSON 在下方队列中顺序执行
            messages.append({"role": "assistant", "content": raw_text})

            while action_queue:
                action = action_queue.pop(0)
                action_type = action.get("action", "")

                if action_type == "reply":
                    result.reply = action.get("message", "")
                    return result

                if action_type == "think":
                    messages.append({
                        "role": "user",
                        "content": f"[系统] 好的，继续。根据你的分析决定下一步行动。",
                    })
                    break

                if action_type == "progress":
                    msg = action.get("message", "")
                    result.progress_log.append(msg)
                    if self.progress_callback:
                        self.progress_callback(msg)
                    messages.append({
                        "role": "user",
                        "content": "[系统] 已播报进展，继续执行。",
                    })
                    continue

                if action_type == "use_skill":
                    skill_name = action.get("skill", "")
                    skill_args = action.get("args", {})
                    result.skills_used.append(skill_name)

                    skill_result = self._execute_skill(skill_name, skill_args, messages)
                    messages.append({
                        "role": "user",
                        "content": f"[Skill 执行结果: {skill_name}]\n\n{skill_result}",
                    })
                    continue

                if action_type == "delegate":
                    result.delegated = True
                    delegate_result = self._execute_delegate(action)
                    messages.append({
                        "role": "user",
                        "content": f"[Multi-Agent 调度结果]\n\n{delegate_result}",
                    })
                    continue

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

    @staticmethod
    def _extract_first_json_object(text: str) -> str | None:
        """从 text 中第一个 `{` 起做括号配平，提取完整 JSON 对象子串。

        处理嵌套对象与字符串内的引号/反斜杠，避免旧正则 `[^{}]*` 无法匹配
        `{"args":{"path":"."}}` 而导致解析失败并把原始 JSON 泄漏给用户回复。
        """
        start = text.find("{")
        if start < 0:
            return None
        depth = 0
        i = start
        in_str = False
        esc = False
        while i < len(text):
            c = text[i]
            if in_str:
                if esc:
                    esc = False
                elif c == "\\":
                    esc = True
                elif c == '"':
                    in_str = False
                i += 1
                continue
            if c == '"':
                in_str = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return text[start : i + 1]
            i += 1
        return None

    def _parse_all_actions(self, text: str) -> list[dict[str, Any]]:
        """解析 LLM 输出中的全部 JSON action（支持多个对象首尾拼接）。

        模型有时会一次输出 `{"action":"use_skill",...}{"action":"use_skill",...}`，
        必须逐个执行，且不能把整段字符串当作最终 reply 发给用户。
        """
        cleaned = text.strip()
        if cleaned.startswith("```"):
            cleaned = re.sub(r"^```\w*\n?", "", cleaned)
            cleaned = re.sub(r"\n?```$", "", cleaned)
            cleaned = cleaned.strip()

        actions: list[dict[str, Any]] = []
        rest = cleaned
        while True:
            i = rest.find("{")
            if i < 0:
                break
            rest = rest[i:]
            chunk = self._extract_first_json_object(rest)
            if not chunk:
                break
            try:
                obj = json.loads(chunk)
            except json.JSONDecodeError:
                break
            if not isinstance(obj, dict) or "action" not in obj:
                break
            actions.append(obj)
            rest = rest[len(chunk) :].lstrip()

        return actions

    def _fallback_reply(self, raw_text: str) -> str:
        """无法解析出任何合法 action 时的用户可见回复（禁止泄漏原始 JSON）。"""
        t = raw_text.strip()
        if not t:
            return "小白脑子短路了一下...(｡•́︿•̀｡)"
        # 明显是结构化输出失败，不要直接把 JSON 发到 QQ
        if '"action"' in t and (t.startswith("{") or "```" in t[:20]):
            return "小白这边解析响应时出了点小问题，麻烦你再说一次或说简单一点～"
        return t

    def _parse_action(self, text: str) -> dict[str, Any] | None:
        """从 LLM 输出中提取第一个 JSON action（兼容单测与外部调用）。"""
        actions = self._parse_all_actions(text)
        return actions[0] if actions else None

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
        if skill_name in ("pack_for_qq_send", "send_project_zip"):
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
            target = (
                args.get("target", "")
                or args.get("target_user", "")
                or args.get("user", "")
                or args.get("qq", "")
            )
            persona = (
                args.get("persona", "")
                or args.get("persona_desc", "")
                or args.get("description", "")
                or args.get("desc", "")
            )
            if not target or not persona:
                return "需要指定目标用户和角色描述"
            import re as _re
            qq_match = _re.search(r"(\d{5,12})", target)
            if qq_match:
                target = qq_match.group(1)
            set_persona_override(target, persona)
            return f"收到！小白跟 {target} 聊天时会扮演: {persona[:80]}"

        if skill_name == "clear_persona":
            target = args.get("target", "") or args.get("target_user", "") or args.get("user", "")
            if not target:
                return "需要指定要取消人设的用户"
            import re as _re
            qq_match = _re.search(r"(\d{5,12})", target)
            if qq_match:
                target = qq_match.group(1)
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

        if skill_name.startswith("media_"):
            return self._sys_media(skill_name, args)

        if skill_name.startswith("sticker_"):
            return self._sys_sticker(skill_name, args)

        if skill_name.startswith("humanize_"):
            return self._sys_humanize(skill_name, args)

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

        if skill_name == "pack_for_qq_send":
            path = args.get("path", "")
            label = str(args.get("label", "") or args.get("name", "") or "")
            if not path:
                return "需要指定 path（目录或文件的绝对路径，或相对仓库根的路径）"
            info = media_tools.pack_path_for_qq_send(path, self.config.repo_home, label=label)
            if not info.get("ok"):
                return str(info.get("error", "打包失败"))
            return (
                f"[发送文件指令] 请在 reply 的 message 中包含: [FILE:{info['path']}]\n"
                f"类型: {info.get('kind', '')}  文件名: {info.get('name', '')}  大小: {info['size']} bytes\n"
                f"{info.get('note', '')}"
            )

        if skill_name == "send_project_zip":
            project = str(args.get("project", "") or args.get("name", "") or "").strip()
            label = str(args.get("label", "") or "")
            if not project:
                return "需要指定 project（projects 下的目录名，例如 zero-basics-plan）"
            info = media_tools.pack_project_for_qq_send(
                project, self.config.repo_home, label=label
            )
            if not info.get("ok"):
                return str(info.get("error", "打包失败"))
            return (
                f"[发送文件指令] 请在 reply 的 message 中包含: [FILE:{info['path']}]\n"
                f"项目: {project}  压缩包: {info.get('name', '')}  大小: {info['size']} bytes\n"
                f"{info.get('note', '')}"
            )

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

    # ── 缓存管理 Skill ─────────────────────────────────────────

    def _sys_media(self, skill_name: str, args: dict[str, Any]) -> str:
        """媒体缓存管理：标记重要文件、查看统计、手动清理。"""
        from runner.media_tools import (
            pin_media_file, unpin_media_file, list_pinned_files,
            get_cache_stats, cleanup_media_cache,
        )

        if skill_name == "media_pin":
            filename = args.get("filename", "")
            if not filename:
                stats = get_cache_stats()
                return (
                    f"请指定要标记的文件名。当前缓存 {stats['file_count']} 个文件，"
                    f"其中 {stats['pinned_count']} 个已标记为重要。"
                )
            return pin_media_file(filename)

        if skill_name == "media_unpin":
            filename = args.get("filename", "")
            if not filename:
                return "请指定要取消标记的文件名"
            return unpin_media_file(filename)

        if skill_name == "media_pinned_list":
            pinned = list_pinned_files()
            if not pinned:
                return "没有文件被标记为重要"
            lines = [f"共 {len(pinned)} 个重要文件："]
            for f in pinned:
                lines.append(f"  {f}")
            return "\n".join(lines)

        if skill_name == "media_cache_stats":
            stats = get_cache_stats()
            ttl_days = stats["ttl_seconds"] / 86400
            return (
                f"缓存目录: {stats['directory']}\n"
                f"文件数: {stats['file_count']}\n"
                f"总大小: {stats['total_size_mb']} MB\n"
                f"重要文件数: {stats['pinned_count']}\n"
                f"自动清理策略: 超过 {ttl_days:.1f} 天的文件自动删除\n"
                f"容量上限: {stats['max_size_mb']} MB\n"
                f"注意: 表情包收藏独立存储，不受清理影响"
            )

        if skill_name == "media_cleanup_now":
            result = cleanup_media_cache(force=True)
            if result.get("skipped"):
                return f"跳过: {result['reason']}"
            return (
                f"清理完成！删除了 {result['deleted_count']} 个文件，"
                f"释放 {result['deleted_mb']} MB 空间。"
                f"保留了 {result['pinned_count']} 个重要文件。"
            )

        return f"未知的缓存管理 Skill: {skill_name}"

    # ── 表情包 Skill ───────────────────────────────────────────

    def _sys_sticker(self, skill_name: str, args: dict[str, Any]) -> str:
        """表情包管理操作。"""
        from runner import sticker_manager as sm

        if skill_name == "sticker_send":
            mood = args.get("mood", "开心")
            entry = sm.pick_sticker_for_mood(mood)
            if not entry:
                return "表情包收藏是空的，需要先从聊天中收集一些~"
            path = sm.get_sticker_path(entry["id"])
            if not path:
                return "表情包文件丢失了"
            return f"[IMG:{path}]"

        if skill_name == "sticker_save":
            url = args.get("url", "")
            if not url:
                recent = self._find_recent_image_url()
                if not recent:
                    return "找不到最近的图片，请指定图片 URL"
                url = recent
            entry = sm.save_sticker_from_url(url, source_user="owner")
            if entry:
                sm.auto_tag_sticker(entry["id"])
                return f"已存为表情包！ID: {entry['id']}"
            return "存储失败（可能是重复的或图片无法下载）"

        if skill_name == "sticker_list":
            stickers = sm.list_stickers()
            if not stickers:
                return "收藏夹是空的~还没有收藏过表情包"
            lines = [f"共收藏 {len(stickers)} 个表情包："]
            for s in stickers[-20:]:
                tags = ", ".join(s.get("tags", [])) or "未标注"
                lines.append(f"  {s['id']} [{tags}] (用了{s.get('use_count', 0)}次)")
            if len(stickers) > 20:
                lines.append(f"  ...还有 {len(stickers) - 20} 个")
            return "\n".join(lines)

        if skill_name == "sticker_tag":
            sid = args.get("id", "")
            tags = args.get("tags", [])
            if not sid or not tags:
                return "需要指定 id 和 tags"
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.replace("，", ",").split(",")]
            ok = sm.tag_sticker(sid, tags, args.get("description", ""))
            return f"已标注！" if ok else f"找不到 id={sid} 的表情包"

        return f"未知的表情包 Skill: {skill_name}"

    def _find_recent_image_url(self) -> str | None:
        """从对话历史中倒查最近的图片 URL 或本地路径。"""
        import re
        img_re = re.compile(r"\[CQ:image,[^\]]*url=([^\],]+)|https?://\S+\.(?:jpg|jpeg|png|gif|webp)\b", re.IGNORECASE)
        cache_dir = self.config.repo_home / "logs" / "media_cache"
        for msg in reversed(self.messages):
            content = msg.get("content", "")
            if isinstance(content, str):
                m = img_re.search(content)
                if m:
                    return m.group(1) or m.group(0)
        if cache_dir.is_dir():
            images = sorted(cache_dir.glob("*.jpg"), key=lambda p: p.stat().st_mtime, reverse=True)
            if not images:
                images = sorted(cache_dir.glob("*.png"), key=lambda p: p.stat().st_mtime, reverse=True)
            if images:
                return str(images[0])
        return None

    # ── Humanize 代码审查 ─────────────────────────────────────

    def _sys_humanize(self, skill_name: str, args: dict[str, Any]) -> str:
        """Humanize 代码审查系统操作。"""
        try:
            from . import humanize_bridge as hb
        except ImportError:
            return "Humanize bridge 模块不可用"

        if not hb.is_humanize_available():
            return "Humanize 未安装（找不到 ~/.cursor/skills/humanize/scripts/）"

        if skill_name == "humanize_review":
            target = args.get("target", "")
            focus = args.get("focus", "")
            if not target:
                return "需要指定审查目标（文件路径或描述）"

            question = f"Review {target}"
            if focus:
                question += f" focusing on: {focus}"

            result = hb.ask_codex(
                question,
                model="gpt-5.4",
                effort="high",
                timeout=600,
                cwd=self.config.repo_home,
            )
            if result.exit_code != 0:
                return f"Codex 审查失败 (exit={result.exit_code}): {result.output[:500]}"
            return f"[Codex 独立审查结果] ({result.duration_seconds:.0f}s)\n\n{result.output}"

        if skill_name == "humanize_rlcr_setup":
            plan_file = args.get("plan_file", "")
            max_iter = int(args.get("max", 10))
            skip_impl = args.get("skip_impl", False)

            result = hb.setup_rlcr_loop(
                plan_file,
                max_iterations=max_iter,
                skip_impl=bool(skip_impl),
                cwd=self.config.repo_home,
            )
            if result.success:
                return f"RLCR 循环已启动！\n目录: {result.loop_dir}\n\n{result.output[:1000]}"
            return f"RLCR 启动失败 (exit={result.exit_code}): {result.output[:500]}"

        if skill_name == "humanize_status":
            available = hb.is_humanize_available()
            root = hb.get_humanize_root()
            lines = [
                f"Humanize 状态: {'✓ 可用' if available else '✗ 不可用'}",
                f"安装路径: {root}",
            ]
            humanize_dir = self.config.repo_home / ".humanize"
            if humanize_dir.is_dir():
                rlcr_dirs = list((humanize_dir / "rlcr").iterdir()) if (humanize_dir / "rlcr").is_dir() else []
                lines.append(f"RLCR 历史会话: {len(rlcr_dirs)} 个")
            else:
                lines.append("尚无 .humanize/ 运行数据")
            return "\n".join(lines)

        return f"未知的 Humanize 操作: {skill_name}"

    # ── Multi-Agent 调度 ──────────────────────────────────────

    _delegate_phase: str = ""

    def _notify(self, msg: str) -> None:
        """向主人推送进度消息（如果有 progress_callback）。"""
        if self.progress_callback:
            self.progress_callback(msg)

    def _execute_delegate(self, action: dict[str, Any]) -> str:
        """处理 delegate action：规划任务 → 生成 plan → 启动 Fleet 分配。

        全程通过 progress_callback 向主人实时汇报每一步，不会静默等待。
        流程：
          1. 汇报：收到任务，开始规划
          2. 创建项目目录和 TASKS.md
          3. 逐个生成 plan 文件，每完成一个汇报一个
          4. 汇报：规划完毕，开始分配
          5. 启动 Fleet，展示分配表
        """
        tasks = action.get("tasks", [])
        max_workers = action.get("max_workers", 4)
        project = action.get("project", "")
        reason = action.get("reason", "")

        deduped = self._deduplicate_tasks(tasks)
        if not deduped or not project:
            return self._sys_multiagent("multiagent_start", {
                "max_workers": max_workers,
                "project": project,
                "tasks": tasks,
                "reason": reason,
            })

        # ── 阶段 1：汇报启动 ──
        self._delegate_phase = "planning"
        assignment_preview = self._format_assignment(deduped, project)
        self._notify(
            f"📋 收到！小白现在开始规划任务，共 {len(deduped)} 个子任务：\n\n"
            f"{assignment_preview}\n\n"
            f"⏳ 正在为每个任务生成执行计划（plan）..."
        )

        # ── 阶段 2：创建项目结构 ──
        repo = self.config.repo_home
        slug = re.sub(r"[^a-z0-9-]", "-", project.lower()).strip("-")
        project_dir = repo / "projects" / slug
        project_dir.mkdir(parents=True, exist_ok=True)
        for sub in ("literature", "analysis", "plans", "logs"):
            (project_dir / sub).mkdir(exist_ok=True)

        if not (project_dir / "README.md").is_file():
            import time as _t
            now = _t.strftime("%Y-%m-%d")
            (project_dir / "README.md").write_text(
                f"# {project}\n\nPriority: high\nStatus: active\n"
                f"Mission: {reason or project}\n\n## Log\n\n### {now}\n\n项目创建。\n",
                encoding="utf-8",
            )

        tasks_file = project_dir / "TASKS.md"
        if not tasks_file.is_file():
            tasks_file.write_text(f"# {project} — 任务列表\n\n", encoding="utf-8")
        existing_content = tasks_file.read_text(encoding="utf-8")

        completed_tasks = {
            m.group(1).strip()
            for m in re.finditer(r"- \[x\]\s*(.+)", existing_content, re.IGNORECASE)
        }
        pending_tasks: list[str] = []
        skipped_done: list[str] = []
        for t in deduped:
            if any(t.lower()[:40] in done.lower() for done in completed_tasks):
                skipped_done.append(t)
            else:
                pending_tasks.append(t)

        if skipped_done:
            self._notify(
                f"♻️ 检测到 {len(skipped_done)} 个已完成任务，自动跳过：\n"
                + "\n".join(f"  ✅ {s[:60]}" for s in skipped_done)
            )

        if not pending_tasks:
            self._delegate_phase = ""
            return (
                f"✅ 所有 {len(deduped)} 个任务已在之前完成，无需重新运行！\n"
                + "\n".join(f"  ✅ {s[:60]}" for s in skipped_done)
            )

        new_entries = ""
        for t in pending_tasks:
            if t not in existing_content:
                new_entries += f"- [ ] {t}\n  Done when: TBD\n\n"
        if new_entries:
            tasks_file.write_text(
                existing_content.rstrip("\n") + "\n\n" + new_entries,
                encoding="utf-8",
            )

        # ── 阶段 3：检查已有 plan，仅为缺失的生成新 plan ──
        plans_dir = project_dir / "plans"
        plan_results: list[str] = []
        for i, t in enumerate(pending_tasks):
            task_slug = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", t.lower())[:60].strip("-")
            existing_plan = plans_dir / f"{task_slug}.md"
            if existing_plan.exists():
                line = f"  [{i+1}/{len(pending_tasks)}] {t[:50]}... ♻️ 已有 Plan（续做）"
                plan_results.append(line)
            else:
                try:
                    self._auto_gen_plan(project_dir, t, reason)
                    status = "✅ 新建"
                except Exception:
                    status = "⚠️ 跳过（Worker 会自行创建）"
                line = f"  [{i+1}/{len(pending_tasks)}] {t[:50]}... {status}"
                plan_results.append(line)
            if (i + 1) % 2 == 0 or i == len(pending_tasks) - 1:
                self._notify(
                    f"📝 Plan 检查/生成进度 ({i+1}/{len(pending_tasks)}):\n"
                    + "\n".join(plan_results[-(min(i+1, 2)):])
                )

        # ── 阶段 4：汇报规划完毕，启动 Fleet ──
        self._delegate_phase = "launching"
        resumed_count = sum(1 for r in plan_results if "已有 Plan" in r)
        new_count = len(pending_tasks) - resumed_count
        self._notify(
            f"✅ {len(pending_tasks)} 个任务的 Plan 已就绪"
            f"（{resumed_count} 个续做, {new_count} 个新建）！\n"
            f"🚀 正在启动 Multi-Agent 系统，分配任务给子 Agent..."
        )

        result = self._sys_multiagent("multiagent_start", {
            "max_workers": max_workers,
            "project": project,
            "tasks": pending_tasks,
            "reason": reason,
            "_skip_plan_gen": True,
        })

        self._delegate_phase = ""

        # ── 阶段 5：最终汇报 ──
        skip_info = ""
        if skipped_done:
            skip_info = f"\n♻️ 已完成（跳过）: {len(skipped_done)} 个\n"
        final_report = (
            f"📝 规划阶段完成（{len(pending_tasks)} 个待执行, "
            f"{resumed_count} 个续做, {new_count} 个新建）:\n"
            + "\n".join(plan_results)
            + skip_info
            + "\n\n" + result
        )
        return final_report

    def _maybe_autostart_fleet_on_status(self, args: dict[str, Any]) -> str:
        """查询状态时：若 Fleet 未运行且有待办任务，则自动启动（可关）。"""
        import os
        import threading
        import time as _time

        if args.get("no_autostart"):
            return ""
        if os.environ.get("MULTIAGENT_STATUS_AUTOSTART", "1").strip() == "0":
            return ""

        from fleet.scheduler import get_fleet_scheduler, start_fleet
        from fleet.config import FleetConfig
        from fleet.task_scanner import scan_available_tasks

        sched = get_fleet_scheduler()
        thread_alive = any(
            t.name == "fleet-scheduler" and t.is_alive()
            for t in threading.enumerate()
        )
        if sched is not None:
            if sched._running:
                return ""
            if thread_alive:
                return ""

        cfg = FleetConfig.from_env()
        if cfg.max_workers <= 0:
            return ""

        eligible = [
            t for t in scan_available_tasks(self.config.repo_home)
            if t.fleet_eligible and not t.blocked
        ]
        if not eligible:
            return ""

        start_fleet(
            repo_root=self.config.repo_home,
            fleet_config=cfg,
            background=True,
            codex_config=self.config,
        )
        _time.sleep(0.6)
        return (
            "\n▶ 检测到有待认领任务且 Fleet 未在运行，**已自动启动调度**。"
            "\n  （若不想自动启动：调用时加 `no_autostart: true` 或设置环境变量 "
            "`MULTIAGENT_STATUS_AUTOSTART=0`）\n"
        )

    def _format_multiagent_fixed_report(self, args: dict[str, Any], autostart_note: str) -> str:
        """固定格式 Multi-Agent 汇报（阶段 / Fleet 事实 / 队列 / Agent / 产出）。"""
        import threading
        from datetime import datetime, timedelta, timezone

        from fleet.scheduler import get_fleet_scheduler

        repo = self.config.repo_home
        bj = timezone(timedelta(hours=8))
        ts = datetime.now(bj).strftime("%Y-%m-%d %H:%M:%S")

        lines: list[str] = [
            "═══════════════════════════════════════════════════════",
            "【小白 · Multi-Agent 固定汇报】",
            f"汇报时间（北京）: {ts}",
            "═══════════════════════════════════════════════════════",
            "",
            "■ 1）小白编排阶段（delegate / Plan）",
        ]
        phase = (self._delegate_phase or "").strip()
        if phase == "planning":
            lines.append(
                "   状态: 📝 **Plan 规划中**"
                "（正在检查或生成各任务的 `plans/*.md`，尚未完成向 Worker 的满载派发）"
            )
        elif phase == "launching":
            lines.append(
                "   状态: 🚀 **Plan 已就绪，正在拉起 Fleet**"
                "（调度器启动或预分配任务入队中）"
            )
        else:
            lines.append(
                "   状态: — **不在 delegate 阻塞阶段**"
                "（若下方 Fleet 判定为运行中，则任务由调度器按 tick 派发）"
            )

        sched = get_fleet_scheduler()
        thread_alive = any(
            t.name == "fleet-scheduler" and t.is_alive()
            for t in threading.enumerate()
        )

        lines.extend(["", "■ 2）Fleet 调度器事实状态（本进程，避免误判）"])
        if sched is None:
            lines.append("   调度器实例: **不存在**")
            lines.append(f"   fleet-scheduler 线程存活: **{'是' if thread_alive else '否'}**")
            lines.append("   **综合判定**: ⛔ Fleet **未运行**")
        else:
            lines.append("   调度器实例: **存在**")
            lines.append(f"   _running: **{bool(sched._running)}**")
            lines.append(f"   _draining: **{bool(sched._draining)}**")
            lines.append(f"   fleet-scheduler 线程存活: **{'是' if thread_alive else '否'}**")
            if sched._running and not sched._draining:
                verdict = "✅ Fleet **运行中**"
            elif thread_alive:
                verdict = "⏳ **收尾中**（调度线程仍在，如刚 stop 或正在排空）"
            else:
                verdict = "⛔ Fleet **已停止**"
            lines.append(f"   **综合判定**: {verdict}")
            pf = sched.config.project_filter
            if pf:
                lines.append(f"   当前 project_filter: `{', '.join(sorted(pf))}`")
            else:
                lines.append("   当前 project_filter: （空，扫描全部项目）")

        snap = sched.metrics.get_snapshot() if sched else None

        lines.extend(
            [
                "",
                "■ 3）仓库与产出格式（按路径找结果）",
                f"   仓库根: `{repo}`",
                "   项目目录: `projects/<项目名>/`",
                "     · `TASKS.md` — 任务 `[ ]` / `[x]`",
                "     · `plans/` — Humanize 风格计划（与任务对应）",
                "     · `logs/` — Worker 会话日志（如 `*fleet*.md`）",
                "     · `analysis/`、`literature/` — 分析与文献笔记",
            ]
        )

        lines.extend(["", "■ 4）预分配队列（小白已指定、尚未派出 Worker）"])
        if sched:
            n_pre, prev = sched.peek_preassigned()
            lines.append(f"   剩余: **{n_pre}** 条")
            if prev:
                for i, ptxt in enumerate(prev[:12], 1):
                    lines.append(f"     {i}. {ptxt}")
            elif n_pre == 0:
                lines.append("     （队列为空）")
        else:
            lines.append("   （无调度器实例）")

        lines.extend(["", "■ 5）当前 Agent 一对一（metrics，可靠）"])
        if snap and snap.active_list:
            lines.append(f"   活跃: **{len(snap.active_list)}** / {snap.max_workers}")
            for i, w in enumerate(snap.active_list, 1):
                idle = w.get("is_idle")
                et = (w.get("exploration_type") or "").strip()
                task = (w.get("task_text") or w.get("task_id") or "?").strip()
                if idle:
                    task = f"[空闲探索·{et or w.get('task_id', '')}] {task}".strip()
                task_short = task[:100] + ("…" if len(task) > 100 else "")
                wid = w.get("worker_id", "?")
                proj = w.get("project", "?")
                el = w.get("elapsed_seconds", 0) or 0
                lines.append(
                    f"   |{i:2d}| `{wid}` | {proj} | 🔄执行中 | {task_short} | {el:.0f}s"
                )
        else:
            if sched and sched._running and not sched._draining:
                lines.append(
                    "   当前 **0** 个活跃 Worker（tick 间隙、或队列空、或即将拉起空闲探索）"
                )
            else:
                lines.append("   无活跃 Worker。")

        lines.extend(["", "■ 6）近期完成与产出（Dashboard）"])
        if sched and sched._dashboard:
            detail = self._render_dashboard_chatter(sched._dashboard)
            lines.append(detail if detail.strip() else "   （暂无最近交付摘要）")
        else:
            lines.append("   （Dashboard 未就绪 — 以 ■7 磁盘日志为准）")

        lines.extend(["", "■ 7）磁盘上最新项目日志（兜底）"])
        try:
            log_files = sorted(
                repo.glob("projects/*/logs/*.md"),
                key=lambda x: x.stat().st_mtime,
                reverse=True,
            )[:8]
            if log_files:
                for lf in log_files:
                    rel = lf.relative_to(repo)
                    try:
                        sz = lf.stat().st_size
                    except OSError:
                        sz = 0
                    lines.append(f"   · `{rel}` ({sz} bytes)")
            else:
                lines.append("   （暂无 `projects/*/logs/*.md`）")
        except OSError as e:
            lines.append(f"   （列举失败: {e}）")

        if snap:
            lines.extend(
                [
                    "",
                    "■ 8）累计统计（本会话调度器生命周期内）",
                    f"   已派发: {snap.total_launched} | 已完成: {snap.total_completed} "
                    f"| ✅{snap.total_ok} ❌{snap.total_failed} | 成功率约 {snap.success_rate:.0%}",
                ]
            )

        blocked_items: list[dict[str, str]] = []
        if sched:
            blocked_items = sched.drain_blocked_notifications()
        lines.extend(["", "■ 9）阻塞项（本汇报会清空阻塞队列缓存）"])
        if blocked_items:
            for b in blocked_items:
                wk = b.get("worker", "?")
                lines.append(f"   ⚠️ `{wk}`: {(b.get('reason') or '')[:220]}")
        else:
            lines.append("   无")

        if autostart_note:
            lines.extend(["", autostart_note.rstrip()])

        lines.extend(["", "═══════════════════════════════════════════════════════"])
        return "\n".join(lines)

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
            skip_plan = args.get("_skip_plan_gen", False)

            if tasks and project and not skip_plan:
                self._ensure_project_tasks(project, tasks, args.get("reason", ""))

            deduped_tasks = self._deduplicate_tasks(tasks)

            existing = get_fleet_scheduler()
            if existing and existing._running and not existing._draining:
                if deduped_tasks and project:
                    fleet_tasks = self._build_fleet_tasks(project, deduped_tasks)
                    added = existing.enqueue_preassigned(fleet_tasks)
                    existing.add_project_filter(project)
                    assignment = self._format_assignment(deduped_tasks, project)
                    return (
                        f"Multi-Agent 系统运行中，已追加 {added} 个任务到 {project}\n\n"
                        f"{assignment}"
                    )
                if project:
                    existing.add_project_filter(project)
                    pf = existing.config.project_filter
                    return f"Multi-Agent 系统运行中，已加入项目: {', '.join(sorted(pf))}"
                snap = existing.metrics.get_snapshot()
                return (
                    f"Multi-Agent 系统已在运行 "
                    f"({snap.active_workers}/{snap.max_workers} 活跃, "
                    f"已完成: {snap.total_completed})"
                )

            fleet_config = FleetConfig.from_env()
            max_workers = args.get("max_workers")
            n = int(max_workers) if max_workers else min(
                max(len(deduped_tasks), 2), fleet_config.max_workers
            )
            proj_filter = frozenset({project}) if project else frozenset()
            fleet_config = dc_replace(
                fleet_config,
                max_workers=n,
                project_filter=proj_filter,
                idle_exploration_enabled=not bool(proj_filter),
                poll_interval_seconds=min(fleet_config.poll_interval_seconds, 10),
            )
            scope = f" (仅 {project})" if project else " (所有项目)"
            scheduler = start_fleet(
                repo_root=self.config.repo_home,
                fleet_config=fleet_config,
                background=True,
                codex_config=self.config,
            )

            if deduped_tasks and project:
                fleet_tasks = self._build_fleet_tasks(project, deduped_tasks)
                scheduler.enqueue_preassigned(fleet_tasks)

            import time as _time
            _time.sleep(1)

            assignment = self._format_assignment(deduped_tasks, project) if deduped_tasks else ""
            return (
                f"Multi-Agent 系统已启动! {n} 个 Agent 出发{scope}\n\n"
                f"{assignment}\n"
                f"{_fleet_status()}"
            )

        if skill_name == "multiagent_status":
            autostart_note = self._maybe_autostart_fleet_on_status(args)
            return self._format_multiagent_fixed_report(args, autostart_note)

        if skill_name == "multiagent_worker_detail":
            scheduler = get_fleet_scheduler()
            if not scheduler or not scheduler._dashboard:
                return "没有运行中的 Dashboard"
            worker_id = args.get("worker_id", "")
            return self._render_single_worker(scheduler._dashboard, worker_id)

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

    # ── Fleet 任务分配辅助 ─────────────────────────────────────

    @staticmethod
    def _deduplicate_tasks(tasks: list[str]) -> list[str]:
        """去重并过滤空任务，保持顺序。"""
        seen: set[str] = set()
        result: list[str] = []
        for t in tasks:
            t = t.strip()
            if not t:
                continue
            key = t.lower()[:60]
            if key in seen:
                continue
            seen.add(key)
            result.append(t)
        return result

    def _build_fleet_tasks(self, project: str, task_texts: list[str]) -> list:
        """将文本任务列表转为 FleetTask 对象，供 scheduler 预分配。"""
        import hashlib
        from fleet.config import FleetTask
        fleet_tasks = []
        for text in task_texts:
            tid = hashlib.sha256(f"{project}:{text}".encode()).hexdigest()[:16]
            fleet_tasks.append(FleetTask(
                task_id=tid,
                project=project,
                text=text,
                fleet_eligible=True,
            ))
        return fleet_tasks

    @staticmethod
    def _format_assignment(tasks: list[str], project: str) -> str:
        """格式化任务分配表，展示小白的分配决策。"""
        if not tasks:
            return ""
        lines = [f"📋 任务分配表 (项目: {project}, 共 {len(tasks)} 个任务):"]
        lines.append("─" * 40)
        for i, t in enumerate(tasks):
            lines.append(f"  W{i}: {t[:80]}")
        lines.append("─" * 40)
        lines.append(f"每个 Agent 负责一个独立任务，互不干扰。")
        return "\n".join(lines)

    # ── Fleet Worker 详情渲染 ─────────────────────────────────

    @staticmethod
    def _render_dashboard_chatter(dashboard: Any) -> str:
        """从 Dashboard 提取最近动态信息（补充 metrics 的静态数据）。"""
        try:
            dashboard._drain_events()
        except Exception:
            return ""

        lines: list[str] = []

        with dashboard._lock:
            finished = [w for w in dashboard._workers.values() if w.finished]
            if finished:
                ok_count = sum(1 for w in finished if w.ok)
                fail_count = len(finished) - ok_count
                lines.append(f"\n🏁 已交付 ({len(finished)} 个, ✅{ok_count} ❌{fail_count}):")
                for ws in finished[-5:]:
                    short_id = ws.worker_id.replace("fleet-worker-", "W")
                    icon = "✅" if ws.ok else "❌"
                    task = ws.task_text[:40] + ("..." if len(ws.task_text) > 40 else "")
                    dur = f"{ws.duration_seconds:.0f}s" if ws.duration_seconds else "?"
                    lines.append(f"  {icon} {short_id}: {task} ({dur})")
                    if ws.deliverables:
                        for d in ws.deliverables[:3]:
                            lines.append(f"     📄 {d}")

            chatter = dashboard._recent_chatter[-6:] if dashboard._recent_chatter else []
            if chatter:
                lines.append(f"\n💬 最近动态:")
                for wid, icon, msg in chatter:
                    short = wid.replace("fleet-worker-", "W")
                    lines.append(f"  {icon} [{short}] {msg[:60]}")

        return "\n".join(lines)

    @staticmethod
    def _render_single_worker(dashboard: Any, worker_id: str) -> str:
        """渲染单个 Worker 的详细信息（先查 metrics，再补充 dashboard）。"""
        from fleet.scheduler import get_fleet_scheduler
        scheduler = get_fleet_scheduler()
        if not scheduler:
            return "Fleet 未运行"

        snap = scheduler.metrics.get_snapshot()
        target = None
        for i, w in enumerate(snap.active_list):
            wid = w["worker_id"]
            if worker_id in (wid, f"W{i}", wid.replace("fleet-worker-", "W")):
                target = w
                break

        if not target:
            return f"找不到 Worker: {worker_id}"

        import time as _time
        task = target.get("task_text", "") or target["task_id"]
        lines = [
            f"Worker {target['worker_id']} 详情:",
            f"  📋 任务: {task}",
            f"  📂 项目: {target['project']}",
            f"  📍 状态: 🔄执行中",
            f"  ⏱️ 已运行: {target['elapsed_seconds']:.0f}s",
        ]

        if dashboard:
            try:
                dashboard._drain_events()
                with dashboard._lock:
                    for ws in dashboard._workers.values():
                        if ws.worker_id == target["worker_id"]:
                            pct = min(ws.turn / max(ws.max_turns, 1) * 100, 99)
                            lines.append(f"  📊 进度: {pct:.0f}% (第{ws.turn}轮/{ws.max_turns}轮)")
                            if ws.phase == "tool_exec" and ws.tool_name:
                                lines.append(f"  🔧 正在使用工具: {ws.tool_name}")
                            if ws.last_message:
                                lines.append(f"  💬 最新状态: {ws.last_message}")
                            if ws.deliverables:
                                lines.append("  📄 产出物:")
                                for d in ws.deliverables:
                                    lines.append(f"    - {d}")
                            break
            except Exception:
                pass

        return "\n".join(lines)

    # ── Fleet 任务落盘 ─────────────────────────────────────────

    def _ensure_project_tasks(
        self,
        project: str,
        tasks: list[str],
        reason: str = "",
    ) -> None:
        """Ensure project dir and TASKS.md exist, then append tasks for fleet scanner.

        Also auto-generates Humanize-style plan files for each task so that
        Fleet Workers can follow the RLCR loop (Plan → Implement → Review → Fix).
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

        plans_dir = project_dir / "plans"
        plans_dir.mkdir(exist_ok=True)

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
            new_entries += f"- [ ] {t}\n  Done when: TBD\n\n"

        if new_entries:
            tasks_file.write_text(
                existing_content.rstrip("\n") + "\n\n" + new_entries,
                encoding="utf-8",
            )

    def _auto_gen_plan(
        self,
        project_dir: Path,
        task_text: str,
        project_reason: str = "",
    ) -> None:
        """Auto-generate a Humanize-style plan file for a task using the LLM.

        Follows the gen-plan skill output format: Goal, Acceptance Criteria,
        Path Boundaries, Milestones.  Falls back to a template if LLM fails.
        """
        task_slug = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", task_text.lower())[:60].strip("-")
        if not task_slug:
            task_slug = "task"
        plan_file = project_dir / "plans" / f"{task_slug}.md"
        if plan_file.exists():
            return

        import time as _t
        now = _t.strftime("%Y-%m-%d")

        gen_prompt = (
            f"你是一个任务规划专家。为以下任务生成一份结构化的实施计划。\n\n"
            f"**任务**: {task_text}\n"
            f"**项目背景**: {project_reason or '无额外背景'}\n\n"
            f"请严格按以下 Markdown 格式输出，不要输出其他内容：\n\n"
            f"# {task_text}\n\n"
            f"Generated: {now}\n\n"
            f"## Goal Description\n（清晰描述任务目标）\n\n"
            f"## Acceptance Criteria\n\n"
            f"- AC-1: （第一个验收标准）\n"
            f"  - Positive Tests: （预期通过的情况）\n"
            f"  - Negative Tests: （预期失败的情况）\n"
            f"- AC-2: ...\n\n"
            f"## Path Boundaries\n\n"
            f"### Upper Bound (Maximum Scope)\n（最完整的方案）\n\n"
            f"### Lower Bound (Minimum Scope)\n（最简可行方案）\n\n"
            f"### Allowed Choices\n- Can use: ...\n- Cannot use: ...\n\n"
            f"## Dependencies and Sequence\n\n"
            f"### Milestones\n1. ...\n\n"
            f"## Implementation Notes\n- 代码中不应包含 AC-、Milestone 等计划术语\n"
        )

        try:
            from openai import OpenAI
            client = OpenAI(
                api_key=self.config.api_key,
                base_url=self.config.base_url,
                timeout=60.0,
            )
            stream = client.chat.completions.create(
                model=self.config.model,
                messages=[{"role": "user", "content": gen_prompt}],
                stream=True,
                temperature=0.4,
                max_tokens=2048,
            )
            parts: list[str] = []
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    parts.append(chunk.choices[0].delta.content)
            plan_content = "".join(parts).strip()
            if len(plan_content) < 50:
                raise ValueError("LLM returned too short a plan")
        except Exception as e:
            import logging as _logging
            _logging.getLogger("runner.agent_loop").warning(
                "Auto gen-plan failed for '%s': %s, using template", task_text, e,
            )
            plan_content = (
                f"# {task_text}\n\n"
                f"Generated: {now}\n\n"
                f"## Goal Description\n{task_text}\n\n"
                f"## Acceptance Criteria\n\n"
                f"- AC-1: 任务核心产出物存在且内容完整\n"
                f"  - Positive Tests: 产出文件存在、内容非空、格式正确\n"
                f"  - Negative Tests: 文件不存在或内容为空\n"
                f"- AC-2: 证据链完整可追溯\n"
                f"  - Positive Tests: 每个结论有来源\n"
                f"  - Negative Tests: 存在无来源的断言\n\n"
                f"## Path Boundaries\n\n"
                f"### Upper Bound\n全面完成所有要求\n\n"
                f"### Lower Bound\n最小可行产出\n\n"
                f"## Dependencies and Sequence\n\n"
                f"### Milestones\n1. 调研与信息收集\n2. 核心内容撰写\n3. 自审与修复\n"
            )

        plan_file.write_text(plan_content, encoding="utf-8")
        import logging as _logging
        _logging.getLogger("runner.agent_loop").info("Auto-generated plan: %s", plan_file)

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
            tasks_content += f"- [ ] {t}\n  Done when: TBD\n\n"
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
            new_tasks += f"\n- [ ] {t}\n  Done when: TBD\n"

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
