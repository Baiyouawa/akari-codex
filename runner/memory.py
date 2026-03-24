"""小白记忆与反思系统。

三层记忆架构：
- 短期记忆：最近 N 轮对话（自动滚动）
- 长期记忆：从对话中提炼的重要事实
- 反思日志：定期总结与洞察

存储在 logs/xiaobai/ 目录下，JSONL 格式。
"""

from __future__ import annotations

import datetime
import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger("xiaobai.memory")

_BJ_TZ = datetime.timezone(datetime.timedelta(hours=8))

SHORT_TERM_MAX = 50
REFLECT_EVERY_N = 10
LONG_TERM_MAX = 200


def _now_str() -> str:
    return datetime.datetime.now(_BJ_TZ).strftime("%Y-%m-%d %H:%M:%S")


def _memory_dir(repo_root: Path) -> Path:
    d = repo_root / "logs" / "xiaobai"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _read_jsonl(path: Path, max_lines: int = 0) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").strip().splitlines()
    records = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    if max_lines > 0 and len(records) > max_lines:
        records = records[-max_lines:]
    return records


def _append_jsonl(path: Path, record: dict[str, Any]) -> None:
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def _rewrite_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


# ─── 短期记忆 ────────────────────────────────────────────────

def save_turn(
    repo_root: Path,
    user_msg: str,
    bot_reply: str,
    action_taken: str = "",
) -> None:
    """保存一轮对话到短期记忆。"""
    mem_dir = _memory_dir(repo_root)
    path = mem_dir / "short_term.jsonl"

    record = {
        "timestamp": _now_str(),
        "user": user_msg[:500],
        "bot": bot_reply[:500],
        "action": action_taken,
    }
    _append_jsonl(path, record)

    all_records = _read_jsonl(path)
    if len(all_records) > SHORT_TERM_MAX:
        _rewrite_jsonl(path, all_records[-SHORT_TERM_MAX:])


def load_short_term(repo_root: Path, limit: int = 10) -> list[dict[str, Any]]:
    """加载最近 N 轮对话。"""
    path = _memory_dir(repo_root) / "short_term.jsonl"
    records = _read_jsonl(path)
    return records[-limit:]


# ─── 长期记忆 ────────────────────────────────────────────────

def add_fact(repo_root: Path, fact: str, source: str = "reflect") -> None:
    """添加一条长期记忆（重要事实/用户偏好）。"""
    path = _memory_dir(repo_root) / "long_term.jsonl"
    record = {
        "timestamp": _now_str(),
        "fact": fact,
        "source": source,
    }
    _append_jsonl(path, record)

    all_records = _read_jsonl(path)
    if len(all_records) > LONG_TERM_MAX:
        _rewrite_jsonl(path, all_records[-LONG_TERM_MAX:])


def load_long_term(repo_root: Path) -> list[dict[str, Any]]:
    """加载全部长期记忆。"""
    path = _memory_dir(repo_root) / "long_term.jsonl"
    return _read_jsonl(path)


# ─── 反思 ────────────────────────────────────────────────────

def load_turn_count(repo_root: Path) -> int:
    """当前短期记忆中的对话轮次数。"""
    path = _memory_dir(repo_root) / "short_term.jsonl"
    return len(_read_jsonl(path))


def save_reflection(repo_root: Path, summary: str, insights: list[str]) -> None:
    """保存一次反思结果。"""
    path = _memory_dir(repo_root) / "reflections.jsonl"
    record = {
        "timestamp": _now_str(),
        "summary": summary,
        "insights": insights,
    }
    _append_jsonl(path, record)


def should_reflect(repo_root: Path) -> bool:
    """判断是否应该触发反思（每 N 轮对话）。"""
    count = load_turn_count(repo_root)
    if count == 0:
        return False
    return count % REFLECT_EVERY_N == 0


# ─── 构建记忆上下文（注入到 system prompt） ──────────────────

def load_context(repo_root: Path) -> str:
    """构建记忆上下文字符串，注入到 LLM 的 system message 中。"""
    parts: list[str] = []

    long_term = load_long_term(repo_root)
    if long_term:
        facts = [r["fact"] for r in long_term[-20:]]
        parts.append("## 小白记住的事情\n" + "\n".join(f"- {f}" for f in facts))

    short_term = load_short_term(repo_root, limit=8)
    if short_term:
        history_lines = []
        for r in short_term:
            history_lines.append(f"[{r['timestamp']}] 小侑: {r['user'][:100]}")
            history_lines.append(f"[{r['timestamp']}] 小白: {r['bot'][:100]}")
        parts.append("## 最近的对话\n" + "\n".join(history_lines))

    return "\n\n".join(parts) if parts else ""


REFLECT_PROMPT = """\
你是小白的记忆整理模块。请根据最近的对话，完成以下任务：

1. 用 1-2 句话总结最近对话的主题和要点
2. 提取值得长期记住的事实（用户偏好、项目状态、重要决定等），每条一行

输出 JSON 格式：
{"summary": "总结", "facts": ["事实1", "事实2", ...]}

如果没有值得记住的新事实，facts 留空数组。
"""


def build_reflect_messages(repo_root: Path) -> list[dict[str, str]]:
    """构建反思用的 messages。"""
    recent = load_short_term(repo_root, limit=REFLECT_EVERY_N)
    if not recent:
        return []

    history = ""
    for r in recent:
        history += f"小侑: {r['user'][:200]}\n小白: {r['bot'][:200]}\n\n"

    return [
        {"role": "system", "content": REFLECT_PROMPT},
        {"role": "user", "content": f"最近对话记录：\n\n{history}"},
    ]
