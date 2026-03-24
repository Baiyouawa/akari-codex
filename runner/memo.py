"""小白备忘录与提醒系统。

存储在 logs/xiaobai/ 下：
- memos.jsonl — 备忘录条目
- reminders.jsonl — 定时提醒
"""

from __future__ import annotations

import datetime
import json
import uuid
from pathlib import Path
from typing import Any

_BJ_TZ = datetime.timezone(datetime.timedelta(hours=8))


def _now() -> datetime.datetime:
    return datetime.datetime.now(_BJ_TZ)


def _now_str() -> str:
    return _now().strftime("%Y-%m-%d %H:%M:%S")


def _memo_dir(repo_root: Path) -> Path:
    d = repo_root / "logs" / "xiaobai"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    records = []
    for line in path.read_text(encoding="utf-8", errors="replace").strip().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return records


def _write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


# ─── 备忘录 ──────────────────────────────────────────────────

def add_memo(repo_root: Path, content: str, tags: list[str] | None = None) -> str:
    """添加备忘录，返回 ID。"""
    path = _memo_dir(repo_root) / "memos.jsonl"
    memo_id = uuid.uuid4().hex[:8]
    record = {
        "id": memo_id,
        "timestamp": _now_str(),
        "content": content,
        "tags": tags or [],
        "done": False,
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return memo_id


def list_memos(repo_root: Path, include_done: bool = False) -> list[dict[str, Any]]:
    """列出备忘录。"""
    path = _memo_dir(repo_root) / "memos.jsonl"
    records = _read_jsonl(path)
    if not include_done:
        records = [r for r in records if not r.get("done")]
    return records


def complete_memo(repo_root: Path, memo_id: str) -> bool:
    """标记备忘录为完成。"""
    path = _memo_dir(repo_root) / "memos.jsonl"
    records = _read_jsonl(path)
    found = False
    for r in records:
        if r.get("id") == memo_id:
            r["done"] = True
            found = True
    if found:
        _write_jsonl(path, records)
    return found


# ─── 提醒 ────────────────────────────────────────────────────

def add_reminder(repo_root: Path, content: str, remind_at: str) -> str:
    """添加提醒，remind_at 格式为自然语言描述或 ISO 时间。返回 ID。"""
    path = _memo_dir(repo_root) / "reminders.jsonl"
    reminder_id = uuid.uuid4().hex[:8]

    parsed_time = _parse_time(remind_at)

    record = {
        "id": reminder_id,
        "timestamp": _now_str(),
        "content": content,
        "remind_at": parsed_time,
        "remind_at_raw": remind_at,
        "done": False,
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return reminder_id


def _parse_time(time_str: str) -> str:
    """尝试解析时间描述为标准格式。支持简单模式。"""
    now = _now()

    import re
    m = re.match(r"(\d+)\s*分钟后", time_str)
    if m:
        delta = datetime.timedelta(minutes=int(m.group(1)))
        return (now + delta).strftime("%Y-%m-%d %H:%M:%S")

    m = re.match(r"(\d+)\s*小时后", time_str)
    if m:
        delta = datetime.timedelta(hours=int(m.group(1)))
        return (now + delta).strftime("%Y-%m-%d %H:%M:%S")

    m = re.match(r"(\d+)\s*天后", time_str)
    if m:
        delta = datetime.timedelta(days=int(m.group(1)))
        return (now + delta).strftime("%Y-%m-%d %H:%M:%S")

    m = re.match(r"(今天|明天|后天)\s*(\d{1,2})[:\s点](\d{0,2})", time_str)
    if m:
        day_offset = {"今天": 0, "明天": 1, "后天": 2}[m.group(1)]
        hour = int(m.group(2))
        minute = int(m.group(3)) if m.group(3) else 0
        target = now.replace(hour=hour, minute=minute, second=0)
        target += datetime.timedelta(days=day_offset)
        return target.strftime("%Y-%m-%d %H:%M:%S")

    return time_str


def list_reminders(repo_root: Path, include_done: bool = False) -> list[dict[str, Any]]:
    """列出提醒。"""
    path = _memo_dir(repo_root) / "reminders.jsonl"
    records = _read_jsonl(path)
    if not include_done:
        records = [r for r in records if not r.get("done")]
    return records


def check_due_reminders(repo_root: Path) -> list[dict[str, Any]]:
    """检查到期的提醒并标记为完成。返回到期的提醒列表。"""
    path = _memo_dir(repo_root) / "reminders.jsonl"
    records = _read_jsonl(path)
    now_str = _now_str()

    due: list[dict[str, Any]] = []
    changed = False
    for r in records:
        if r.get("done"):
            continue
        if r.get("remind_at", "") <= now_str:
            r["done"] = True
            due.append(r)
            changed = True

    if changed:
        _write_jsonl(path, records)

    return due


def format_memos(memos: list[dict[str, Any]]) -> str:
    """格式化备忘录列表为可读文本。"""
    if not memos:
        return "目前没有备忘录哦~"
    lines = []
    for i, m in enumerate(memos, 1):
        status = "[完成]" if m.get("done") else ""
        tags = " ".join(f"#{t}" for t in m.get("tags", []))
        lines.append(f"  {i}. {m['content']} {tags} {status}".strip())
    return "\n".join(lines)


def format_reminders(reminders: list[dict[str, Any]]) -> str:
    """格式化提醒列表为可读文本。"""
    if not reminders:
        return "目前没有待提醒事项哦~"
    lines = []
    for i, r in enumerate(reminders, 1):
        status = "[已提醒]" if r.get("done") else ""
        lines.append(f"  {i}. {r['content']} (时间: {r['remind_at']}) {status}".strip())
    return "\n".join(lines)
