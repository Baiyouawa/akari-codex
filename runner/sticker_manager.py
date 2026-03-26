"""表情包收藏与管理系统。

小白可以：
  1. 收藏（偷）别人发来的表情包图片
  2. 按场景/情绪从收藏中智能选择表情包
  3. 在对话中自动穿插表情包（每 N 句话发一个）

存储结构：
  logs/xiaobai/stickers/
    ├── index.json      — 索引: [{id, path, tags, source, timestamp}, ...]
    └── *.jpg / *.png    — 表情包图片文件
"""

from __future__ import annotations

import json
import logging
import os
import random
import time
import hashlib
from pathlib import Path
from typing import Any

_log = logging.getLogger("runner.sticker")

STICKERS_PER_REPLY = int(os.environ.get("STICKER_FREQUENCY", "3"))


def _sticker_dir(repo_root: Path | None = None) -> Path:
    root = repo_root or Path(os.environ.get("OPENAKARI_HOME", "."))
    d = root / "logs" / "xiaobai" / "stickers"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _index_path(repo_root: Path | None = None) -> Path:
    return _sticker_dir(repo_root) / "index.json"


def _load_index(repo_root: Path | None = None) -> list[dict[str, Any]]:
    ip = _index_path(repo_root)
    if not ip.is_file():
        return []
    try:
        return json.loads(ip.read_text(encoding="utf-8"))
    except Exception:
        return []


def _save_index(index: list[dict[str, Any]], repo_root: Path | None = None) -> None:
    ip = _index_path(repo_root)
    ip.write_text(
        json.dumps(index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def save_sticker(
    image_data: bytes,
    *,
    tags: list[str] | None = None,
    source_user: str = "",
    source_group: str = "",
    description: str = "",
    repo_root: Path | None = None,
) -> dict[str, Any] | None:
    """保存一张表情包图片到收藏，返回索引条目或 None（重复时）。"""
    content_hash = hashlib.md5(image_data).hexdigest()[:12]

    index = _load_index(repo_root)
    for entry in index:
        if entry.get("hash") == content_hash:
            return None

    ext = ".jpg"
    if image_data[:4] == b"\x89PNG":
        ext = ".png"
    elif image_data[:4] == b"GIF8":
        ext = ".gif"
    elif len(image_data) > 8 and image_data[8:12] == b"WEBP":
        ext = ".webp"

    filename = f"sticker_{int(time.time())}_{content_hash}{ext}"
    save_path = _sticker_dir(repo_root) / filename
    save_path.write_bytes(image_data)

    entry = {
        "id": content_hash,
        "filename": filename,
        "hash": content_hash,
        "tags": tags or [],
        "description": description,
        "source_user": source_user,
        "source_group": source_group,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "use_count": 0,
    }
    index.append(entry)
    _save_index(index, repo_root)
    _log.info("Sticker saved: %s (from user=%s)", filename, source_user)
    return entry


def save_sticker_from_file(
    file_path: str | Path,
    **kwargs: Any,
) -> dict[str, Any] | None:
    """从本地文件保存表情包。"""
    p = Path(file_path)
    if not p.is_file():
        return None
    return save_sticker(p.read_bytes(), **kwargs)


def save_sticker_from_url(
    url: str,
    **kwargs: Any,
) -> dict[str, Any] | None:
    """从 URL 下载并保存表情包。"""
    import html as _html
    import urllib.request

    clean_url = _html.unescape(url)

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; XiaoBai/1.0)",
            "Referer": "https://qq.com",
        }
        if "multimedia.nt.qq.com" in clean_url or "gchat.qpic.cn" in clean_url:
            headers["Accept"] = "image/*"
        req = urllib.request.Request(clean_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        if len(data) < 500:
            return None
        return save_sticker(data, **kwargs)
    except Exception as e:
        _log.warning("Failed to download sticker from %s: %s", clean_url[:80], e)
        return None


def list_stickers(repo_root: Path | None = None) -> list[dict[str, Any]]:
    """列出所有收藏的表情包。"""
    return _load_index(repo_root)


def get_sticker_count(repo_root: Path | None = None) -> int:
    return len(_load_index(repo_root))


def get_sticker_path(sticker_id: str, repo_root: Path | None = None) -> Path | None:
    """根据 ID 获取表情包文件路径。"""
    index = _load_index(repo_root)
    for entry in index:
        if entry["id"] == sticker_id:
            p = _sticker_dir(repo_root) / entry["filename"]
            if p.is_file():
                return p
    return None


def tag_sticker(
    sticker_id: str,
    tags: list[str],
    description: str = "",
    repo_root: Path | None = None,
) -> bool:
    """给表情包添加标签和描述（用于场景匹配）。"""
    index = _load_index(repo_root)
    for entry in index:
        if entry["id"] == sticker_id:
            existing_tags = set(entry.get("tags", []))
            existing_tags.update(tags)
            entry["tags"] = sorted(existing_tags)
            if description:
                entry["description"] = description
            _save_index(index, repo_root)
            return True
    return False


def delete_sticker(sticker_id: str, repo_root: Path | None = None) -> bool:
    """删除一个表情包。"""
    index = _load_index(repo_root)
    for i, entry in enumerate(index):
        if entry["id"] == sticker_id:
            p = _sticker_dir(repo_root) / entry["filename"]
            if p.is_file():
                p.unlink()
            index.pop(i)
            _save_index(index, repo_root)
            return True
    return False


def pick_sticker_for_mood(
    mood: str,
    repo_root: Path | None = None,
) -> dict[str, Any] | None:
    """根据情绪/场景从收藏中选择一个表情包。

    匹配逻辑：
    1. 先找 tags 或 description 包含 mood 关键词的
    2. 没找到就随机选一个
    3. 优先选使用次数少的（均匀分布）
    """
    index = _load_index(repo_root)
    if not index:
        return None

    valid = []
    for entry in index:
        p = _sticker_dir(repo_root) / entry["filename"]
        if p.is_file():
            valid.append(entry)
    if not valid:
        return None

    mood_lower = mood.lower()
    mood_keywords = mood_lower.split()

    matched = []
    for entry in valid:
        tags_text = " ".join(entry.get("tags", [])).lower()
        desc_text = (entry.get("description", "") or "").lower()
        searchable = tags_text + " " + desc_text
        if any(kw in searchable for kw in mood_keywords):
            matched.append(entry)

    candidates = matched if matched else valid

    min_use = min(e.get("use_count", 0) for e in candidates)
    least_used = [e for e in candidates if e.get("use_count", 0) <= min_use + 2]

    chosen = random.choice(least_used)

    for entry in index:
        if entry["id"] == chosen["id"]:
            entry["use_count"] = entry.get("use_count", 0) + 1
            break
    _save_index(index, repo_root)

    return chosen


# ── Auto-tagging via Vision LLM ─────────────────────────────────


def auto_tag_sticker(
    sticker_id: str,
    repo_root: Path | None = None,
) -> list[str]:
    """用 Vision LLM 自动为表情包生成标签和描述。"""
    path = get_sticker_path(sticker_id, repo_root)
    if not path:
        return []

    try:
        from runner.media_tools import recognize_image
        result = recognize_image(
            str(path),
            "这是一张聊天表情包。请用5个以内的中文关键词描述它的情绪和场景，"
            "用逗号分隔。例如：开心,撒娇,可爱,求夸奖,卖萌\n"
            "然后换行写一句简短描述。",
        )
    except Exception:
        return []

    lines = result.strip().split("\n")
    if not lines:
        return []

    tags = [t.strip() for t in lines[0].replace("，", ",").split(",") if t.strip()]
    description = lines[1].strip() if len(lines) > 1 else ""

    tag_sticker(sticker_id, tags, description, repo_root)
    return tags
