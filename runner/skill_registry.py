"""统一 Skill 注册表。

三类 Skill 共存于同一个 Registry：
- atomic:   对应 tools.py 中的原子操作（web_search、read_file 等），一步执行
- compound: 对应 skills/*.md 的多步流程（lit-review、orient 等），读取 SKILL.md 作为执行指南
- system:   Python 直接执行的内部操作（备忘/提醒/项目管理/人设/Multi-Agent 调度）

小白 Agent 和 Multi-Agent Worker 共享同一个 Registry。
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable


@dataclass
class SkillDescriptor:
    """单个 Skill 的元信息。"""

    name: str
    category: str  # "atomic" | "compound" | "system"
    description: str
    complexity: str = "low"  # "low" | "medium" | "high" | "opus-only"
    allowed_tools: list[str] = field(default_factory=list)
    skill_md_path: str | None = None
    handler: Callable[..., str] | None = None

    def summary_line(self) -> str:
        """一行摘要，用于注入 Agent prompt。"""
        tag = {"atomic": "工具", "compound": "技能", "system": "系统"}
        return f"[{tag.get(self.category, '?')}] {self.name} — {self.description}"


def _parse_frontmatter(text: str) -> dict[str, Any]:
    """解析 SKILL.md 开头的 YAML frontmatter（轻量实现，不依赖 PyYAML）。"""
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    result: dict[str, Any] = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(":", 1)
        if len(parts) != 2:
            continue
        key = parts[0].strip()
        val = parts[1].strip().strip('"').strip("'")
        if val.startswith("[") and val.endswith("]"):
            items = [
                v.strip().strip('"').strip("'")
                for v in val[1:-1].split(",")
                if v.strip()
            ]
            result[key] = items
        else:
            result[key] = val
    return result


class SkillRegistry:
    """统一 Skill 注册表。启动时扫描 + 注册所有 Skill。"""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self._skills: dict[str, SkillDescriptor] = {}
        self._scan_compound_skills()
        self._register_atomic_skills()
        self._register_system_skills()

    def _scan_compound_skills(self) -> None:
        """扫描 skills/*/SKILL.md 注册复合 Skill。"""
        skills_dir = self.repo_root / "skills"
        if not skills_dir.is_dir():
            return
        for skill_dir in sorted(skills_dir.iterdir()):
            md_path = skill_dir / "SKILL.md"
            if not md_path.is_file():
                continue
            text = md_path.read_text(encoding="utf-8", errors="replace")
            fm = _parse_frontmatter(text)
            name = fm.get("name", skill_dir.name)
            self._skills[name] = SkillDescriptor(
                name=name,
                category="compound",
                description=fm.get("description", ""),
                complexity=fm.get("complexity", "medium"),
                allowed_tools=fm.get("allowed-tools", []),
                skill_md_path=str(md_path.relative_to(self.repo_root)),
            )

    def _register_atomic_skills(self) -> None:
        """注册 tools.py 中的原子工具为 Skill。"""
        from .tools import TOOL_DEFINITIONS

        for name, spec in TOOL_DEFINITIONS.items():
            self._skills[name] = SkillDescriptor(
                name=name,
                category="atomic",
                description=spec.get("description", ""),
                complexity="low",
                allowed_tools=[name],
            )

    def _register_system_skills(self) -> None:
        """注册系统操作为 Skill（备忘/提醒/项目管理/人设/Multi-Agent/多媒体/电话）。"""
        system_skills = [
            ("memo_add", "记录备忘事项"),
            ("memo_list", "列出所有备忘"),
            ("memo_complete", "完成一条备忘"),
            ("reminder_add", "设置定时提醒"),
            ("reminder_list", "列出所有提醒"),
            ("create_project", "创建新研究项目（自动生成 README/TASKS/目录结构）"),
            ("create_task", "向指定项目添加任务"),
            ("orient", "查看仓库和项目当前状态"),
            ("set_persona", "为指定 QQ 用户设定角色扮演人设"),
            ("clear_persona", "清除指定用户的角色扮演人设"),
            ("list_personas", "列出当前所有角色扮演设定"),
            ("multiagent_start", "启动 Multi-Agent 系统并行执行任务。参数: project(项目名), tasks(任务文本列表), max_workers(Agent数量,可选), reason(启动原因,可选)"),
            ("multiagent_status", "查看 Multi-Agent 系统运行状态"),
            ("multiagent_stop", "停止 Multi-Agent 系统"),
            ("multiagent_report", "查看 Multi-Agent 任务执行报告"),
            ("multiagent_scale", "调整 Multi-Agent Worker 数量"),
            ("multiagent_tasks", "列出所有可执行任务"),
            # ── 多媒体 Skill ─────────────────────────────
            ("send_image", "发送图片到 QQ（支持本地路径或 URL）。在回复中用 [IMG:路径] 标签"),
            ("recognize_image", "识别图片内容（Vision LLM）。参数: path_or_url, prompt"),
            ("send_voice", "发送语音消息到 QQ（TTS 合成）。在回复中用 [VOICE:要说的话] 标签"),
            ("recognize_speech", "语音转文字（Whisper STT）。参数: audio_path"),
            ("send_file", "发送本地文件到 QQ。在回复中用 [FILE:文件路径] 标签"),
            ("send_emoji", "发送 QQ 表情。在回复中用 [FACE:表情ID] 标签"),
            ("tts_generate", "文字转语音，生成 mp3 文件。参数: text, voice(可选)"),
            # ── 文件系统访问 Skill ────────────────────────
            ("read_system_file", "读取本机任意位置的文件（只读）。参数: path"),
            ("list_system_dir", "列出本机任意目录内容。参数: path"),
            ("request_file_delete", "提交文件删除审批请求（不立即执行）。参数: path"),
            ("get_file_for_send", "获取文件信息（准备发送）。参数: path"),
            # ── 表情包 Skill ─────────────────────────────
            ("sticker_send", "从收藏中选择匹配情绪的表情包发送。参数: mood(情绪关键词,如'开心/卖萌/无语')"),
            ("sticker_list", "列出当前收藏的表情包（数量和标签）"),
            ("sticker_tag", "给表情包添加标签。参数: id(表情包ID), tags(标签列表)"),
            # ── Humanize 代码审查 Skill ────────────────────
            ("humanize_review", "请求 Codex 独立审查指定文件或代码变更。参数: target(文件路径或描述), focus(审查重点,可选)"),
            ("humanize_rlcr_setup", "启动 RLCR 迭代开发循环（需要 plan 文件）。参数: plan_file, max(最大迭代,可选), skip_impl(跳过实现直接审查,可选)"),
            ("humanize_status", "查看 Humanize/RLCR 系统状态和可用性"),
            # ── 电话 Skill ───────────────────────────────
            ("phone_check_setup", "检查电话功能配置状态"),
            ("phone_call_notification", "拨打语音通知电话（单向，播放 TTS 消息）。参数: phone_number, message"),
            ("phone_call_realtime", "拨打实时语音对话电话（双向，AI 与对方实时通话）。参数: phone_number, system_prompt(可选)"),
            ("phone_call_status", "查询通话状态。参数: call_id"),
            ("phone_recent_calls", "列出最近通话记录"),
        ]
        for name, desc in system_skills:
            self._skills[name] = SkillDescriptor(
                name=name,
                category="system",
                description=desc,
                complexity="low",
            )

    # ── 查询接口 ──────────────────────────────────────────────

    def get(self, name: str) -> SkillDescriptor | None:
        return self._skills.get(name)

    def list_all(self) -> list[SkillDescriptor]:
        return list(self._skills.values())

    def list_by_category(self, category: str) -> list[SkillDescriptor]:
        return [s for s in self._skills.values() if s.category == category]

    def build_skill_catalog(self) -> str:
        """构建供 Agent prompt 注入的 Skill 目录文本。"""
        sections: list[str] = []

        atomic = self.list_by_category("atomic")
        if atomic:
            lines = [s.summary_line() for s in atomic]
            sections.append("### 原子 Skill（直接执行的工具）\n" + "\n".join(lines))

        compound = self.list_by_category("compound")
        if compound:
            lines = [s.summary_line() for s in compound]
            sections.append("### 复合 Skill（多步流程技能）\n" + "\n".join(lines))

        system = self.list_by_category("system")
        if system:
            humanize_skills = [s for s in system if s.name.startswith("humanize_")]
            media_skills = [s for s in system if s.name.startswith(("send_", "recognize_", "tts_"))]
            file_skills = [s for s in system if s.name.startswith(("read_system", "list_system", "request_file", "get_file_for"))]
            phone_skills = [s for s in system if s.name.startswith("phone_")]
            other_system = [
                s for s in system
                if s not in media_skills and s not in file_skills
                and s not in phone_skills and s not in humanize_skills
            ]

            if other_system:
                lines = [s.summary_line() for s in other_system]
                sections.append("### 系统 Skill（内部操作）\n" + "\n".join(lines))
            if media_skills:
                lines = [s.summary_line() for s in media_skills]
                sections.append("### 多媒体 Skill（QQ 图片/语音/文件/表情）\n" + "\n".join(lines))
            if file_skills:
                lines = [s.summary_line() for s in file_skills]
                sections.append("### 文件系统 Skill（本机全文件访问）\n" + "\n".join(lines))
            if phone_skills:
                lines = [s.summary_line() for s in phone_skills]
                sections.append("### 电话 Skill（真实电话外呼）\n" + "\n".join(lines))
            if humanize_skills:
                lines = [s.summary_line() for s in humanize_skills]
                sections.append("### 代码审查 Skill（Humanize / Codex Review）\n" + "\n".join(lines))

        return "\n\n".join(sections)

    def load_skill_guide(self, name: str) -> str | None:
        """读取复合 Skill 的 SKILL.md 全文，用于注入 Agent 上下文。"""
        skill = self._skills.get(name)
        if not skill or not skill.skill_md_path:
            return None
        full_path = self.repo_root / skill.skill_md_path
        if not full_path.is_file():
            return None
        return full_path.read_text(encoding="utf-8", errors="replace")
