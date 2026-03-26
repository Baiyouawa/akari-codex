"""OneBot11 WebSocket 客户端 — 连接 NapCatQQ，让小白用普通 QQ 号收发消息。

架构：
    NapCatQQ (QQ协议端, 用你的QQ号登录)
        ↕ OneBot11 正向 WebSocket
    onebot_client.py (本模块)
        → runner.gateway.process_remote_message()
        → ChatBot (小白) 生成回复
        → 通过 WebSocket 调用 send_msg 发回 QQ

支持多媒体消息：
    - 接收/识别图片（Vision LLM）
    - 接收/识别语音（Whisper STT）
    - 发送图片、语音、文件、表情包
    - 回复中嵌入 CQ 码（[IMG:path]、[VOICE:text]、[FILE:path]、[FACE:id]）

发文件（[FILE:…]）说明：
    NapCat 若在 Windows、小白在 WSL，协议端无法读取 Linux 路径，会导致 upload 静默失败。
    默认用 base64 内联（与图片/语音一致）。若 NapCat 与仓库同机可读路径，可设
    ``ONEBOT_FILE_SEND_MODE=path``。超大文件超过 ``ONEBOT_FILE_BASE64_MAX_MB`` 时自动改回路径模式。
    若 ``upload_private_file`` 仍异常，可试 ``ONEBOT_FILE_API=send_msg``（走 send_msg 的 file 消息段）。

Usage:
    export ONEBOT_SELF_QQ="123456789"
    export ONEBOT_WS_URL="ws://localhost:3001"   # optional
    python3 -m integrations.onebot_client
"""

from __future__ import annotations

import asyncio
import json
import logging
import random
import re
import sys
import traceback
from pathlib import Path

try:
    from websockets.asyncio.client import connect as ws_connect
    from websockets.exceptions import ConnectionClosed
except ImportError:
    print(
        "websockets is not installed. Run: pip install websockets",
        file=sys.stderr,
    )
    sys.exit(1)

_project_root = Path(__file__).resolve().parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from integrations.config_qq import OneBotConfig
from runner.gateway import process_remote_message
from runner.persona import is_user_ready

logger = logging.getLogger("xiaobai.onebot")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
)

QQ_MSG_LIMIT = 4500
PROACTIVE_IDLE_MIN = 120
PROACTIVE_IDLE_MAX = 360

_CQ_AT_RE = re.compile(r"\[CQ:at,qq=(\d+)[^\]]*\]")
_CQ_IMAGE_RE = re.compile(r"\[CQ:image,([^\]]+)\]")
_CQ_RECORD_RE = re.compile(r"\[CQ:record,([^\]]+)\]")
_CQ_FILE_RE = re.compile(r"\[CQ:file,([^\]]+)\]")

_MEDIA_TAG_IMAGE = re.compile(r"\[IMG:([^\]]+)\]")
_MEDIA_TAG_VOICE = re.compile(r"\[VOICE:([^\]]+)\]")
_MEDIA_TAG_FILE = re.compile(r"\[FILE:([^\]]+)\]")
_MEDIA_TAG_FACE = re.compile(r"\[FACE:(\d+)\]")
_MEDIA_TAG_STICKER = re.compile(r"\[STICKER:([^\]]+)\]")

_owner_last_activity: float = 0.0
_proactive_task: asyncio.Task | None = None  # type: ignore[type-arg]
_proactive_sent_unanswered: bool = False

MSG_AGGREGATE_WINDOW = 10.0
_msg_buffers: dict[str, list[dict]] = {}
_msg_timers: dict[str, asyncio.Task] = {}
_msg_locks: dict[str, asyncio.Lock] = {}


def _parse_cq_params(params_str: str) -> dict[str, str]:
    result = {}
    for part in params_str.split(","):
        if "=" in part:
            k, v = part.split("=", 1)
            result[k.strip()] = v.strip()
    return result


def _strip_cq_codes(text: str) -> str:
    """Remove all CQ codes from message text."""
    return re.sub(r"\[CQ:[^\]]+\]", "", text).strip()


def _extract_media_from_event(event: dict) -> dict:
    """从 OneBot 事件中提取多媒体内容。

    优先从 message 数组（JSON segment）中提取完整数据，
    这比 raw_message 的 CQ 码更可靠——CQ 码中 URL 的 & 会被截断。
    """
    media: dict = {"images": [], "records": [], "files": []}

    message = event.get("message")
    if isinstance(message, list):
        for seg in message:
            seg_type = seg.get("type", "")
            data = seg.get("data", {})
            if seg_type == "image":
                media["images"].append({
                    "file": data.get("file", ""),
                    "url": data.get("url", ""),
                    "file_id": data.get("file_id", ""),
                })
            elif seg_type == "record":
                media["records"].append({
                    "file": data.get("file", ""),
                    "url": data.get("url", ""),
                    "path": data.get("path", ""),
                    "file_id": data.get("file_id", ""),
                })
            elif seg_type == "file":
                media["files"].append({
                    "file": data.get("file", ""),
                    "name": data.get("name", data.get("file", "")),
                    "url": data.get("url", ""),
                    "file_id": data.get("file_id", ""),
                })
        return media

    raw_message = event.get("raw_message", "") or ""
    for m in _CQ_IMAGE_RE.finditer(raw_message):
        params = _parse_cq_params(m.group(1))
        media["images"].append({
            "file": params.get("file", ""),
            "url": params.get("url", ""),
        })
    for m in _CQ_RECORD_RE.finditer(raw_message):
        params = _parse_cq_params(m.group(1))
        media["records"].append({
            "file": params.get("file", ""),
            "url": params.get("url", ""),
        })
    for m in _CQ_FILE_RE.finditer(raw_message):
        params = _parse_cq_params(m.group(1))
        media["files"].append({
            "file": params.get("file", ""),
            "name": params.get("name", ""),
            "url": params.get("url", ""),
        })

    return media


async def _recognize_image(url: str, ws=None, file_id: str = "") -> str:
    """下载图片并用 Vision LLM 识别。

    策略：
    1. 先尝试直接 HTTP 下载 URL
    2. 失败则通过 OneBot get_image API 获取本地缓存路径
    3. 都失败则返回错误
    """
    import html as _html
    from runner.media_tools import recognize_image, download_file

    clean_url = _html.unescape(url) if url else ""

    local_path = None

    if clean_url:
        try:
            local_path = await asyncio.to_thread(download_file, clean_url, ".jpg")
            logger.info("图片直接下载成功: %s (%d bytes)", local_path, local_path.stat().st_size)
        except Exception as e:
            logger.warning("图片直接下载失败 (%s), 尝试 get_image API...", e)

    if local_path is None and ws is not None and file_id:
        try:
            import uuid
            echo_id = str(uuid.uuid4())[:8]
            await ws.send(json.dumps({
                "action": "get_image",
                "params": {"file": file_id},
                "echo": echo_id,
            }))
            for _ in range(20):
                try:
                    raw_resp = await asyncio.wait_for(ws.recv(), timeout=3.0)
                    resp = json.loads(raw_resp)
                    if resp.get("echo") == echo_id:
                        data = resp.get("data", {})
                        img_file = data.get("file", "") or data.get("filename", "")
                        img_url = data.get("url", "")
                        if img_file and Path(img_file).is_file():
                            local_path = Path(img_file)
                            logger.info("通过 get_image 获取本地路径: %s", local_path)
                        elif img_url:
                            local_path = await asyncio.to_thread(download_file, img_url, ".jpg")
                            logger.info("通过 get_image URL 下载: %s", local_path)
                        break
                except asyncio.TimeoutError:
                    break
                except Exception:
                    continue
        except Exception as e:
            logger.warning("get_image API 失败: %s", e)

    if local_path is None and clean_url:
        try:
            result = await asyncio.to_thread(
                recognize_image, clean_url,
                "用一句话简短描述这张图片是什么。",
            )
            return result
        except Exception as e:
            logger.error("直接 URL 识别也失败: %s", e)
            return f"(图片识别失败，无法下载或访问图片: {e})"

    if local_path is None:
        return "(图片识别失败: 无法获取图片文件)"

    try:
        result = await asyncio.to_thread(
            recognize_image, str(local_path),
            "用一句话简短描述这张图片是什么。",
        )
        return result
    except Exception as e:
        logger.error("图片识别失败: %s", e)
        return f"(图片识别失败: {e})"


async def _recognize_voice(url: str) -> str:
    """下载语音并转文字。"""
    try:
        from runner.media_tools import download_file, recognize_speech
        audio_path = await asyncio.to_thread(download_file, url, ".amr")
        text = await asyncio.to_thread(recognize_speech, str(audio_path))
        return text
    except Exception as e:
        logger.error("语音识别失败: %s", e)
        return f"(语音识别失败: {e})"


def _split_message(text: str, limit: int = QQ_MSG_LIMIT) -> list[str]:
    if len(text) <= limit:
        return [text]
    chunks: list[str] = []
    while text:
        if len(text) <= limit:
            chunks.append(text)
            break
        split_at = text.rfind("\n", 0, limit)
        if split_at == -1:
            split_at = limit
        chunks.append(text[:split_at])
        text = text[split_at:].lstrip("\n")
    return chunks


_MULTI_MSG_SEP = "|||"


async def _send_raw_cq(
    ws,
    msg_type: str,
    user_id: int | None,
    group_id: int | None,
    message: str,
) -> None:
    """发送包含 CQ 码的原始消息。"""
    payload: dict = {
        "action": "send_msg",
        "params": {
            "message_type": msg_type,
            "message": message,
        },
    }
    if msg_type == "private" and user_id is not None:
        payload["params"]["user_id"] = user_id
    elif msg_type == "group" and group_id is not None:
        payload["params"]["group_id"] = group_id
    await ws.send(json.dumps(payload))


async def _send_voice_base64(
    ws,
    msg_type: str,
    user_id: int | None,
    group_id: int | None,
    b64_data: str,
) -> None:
    """用 base64 编码的音频数据发送语音消息。

    NapCat 运行在 Windows 端，无法访问 WSL 文件路径，
    所以用 base64:// 协议将音频数据内联传递。
    """
    message = [{"type": "record", "data": {"file": f"base64://{b64_data}"}}]
    payload: dict = {
        "action": "send_msg",
        "params": {
            "message_type": msg_type,
            "message": message,
        },
    }
    if msg_type == "private" and user_id is not None:
        payload["params"]["user_id"] = user_id
    elif msg_type == "group" and group_id is not None:
        payload["params"]["group_id"] = group_id
    await ws.send(json.dumps(payload))


def _resolve_file_path(file_path: str) -> Path | None:
    """智能解析文件路径，按优先级尝试多种方式定位文件。

    1. 绝对路径直接使用
    2. 相对于 OPENAKARI_HOME 仓库根目录
    3. 相对于进程当前工作目录
    4. 在仓库根目录下递归搜索同名文件（限第一层项目目录）
    """
    import os

    p = Path(file_path)

    if p.is_absolute():
        return p if p.is_file() else None

    repo = Path(os.environ.get("OPENAKARI_HOME", ".")).resolve()

    candidate = repo / file_path
    if candidate.is_file():
        return candidate

    candidate = Path.cwd() / file_path
    if candidate.is_file():
        return candidate

    fname = p.name
    for match in repo.rglob(fname):
        if match.is_file():
            return match

    return None


def _file_payload_for_napcat(p: Path) -> tuple[str, str]:
    """NapCat 读取 file 字段的方式：默认 base64（解决 WSL 路径 Windows 端不可读）。

    环境变量：
    - ONEBOT_FILE_SEND_MODE: ``base64``（默认）| ``path`` — 强制只用本地路径
    - ONEBOT_FILE_BASE64_MAX_MB: 超过此大小的文件仍用路径并打警告（默认 80）

    Returns:
        (file_field, log_hint) — file_field 传给 API 的 ``file`` 参数
    """
    import os

    size = p.stat().st_size
    mode = os.environ.get("ONEBOT_FILE_SEND_MODE", "base64").strip().lower()
    max_b64 = int(os.environ.get("ONEBOT_FILE_BASE64_MAX_MB", "80")) * 1024 * 1024

    if mode == "path":
        return str(p), f"path:{p}"

    if size > max_b64:
        logger.warning(
            "文件 %s (%d bytes) 超过 ONEBOT_FILE_BASE64_MAX_MB，改用路径发送；"
            "若对方仍收不到，请把 NapCat 与仓库放在同一可访问路径或调大该环境变量",
            p.name,
            size,
        )
        return str(p), f"path>{max_b64}:{p}"

    from runner.media_tools import file_to_base64

    b64 = file_to_base64(p)
    return f"base64://{b64}", f"base64:{size}B"


async def _send_file_via_api(
    ws,
    msg_type: str,
    user_id: int | None,
    group_id: int | None,
    file_path: str,
) -> None:
    """通过 OneBot API 发送文件。支持相对路径自动解析到仓库根目录。

    默认使用 ``base64://`` 传递内容（与图片/语音一致），避免 NapCat 在 Windows、
    小白在 WSL 时无法读取 Linux 绝对路径而导致静默失败。
    """
    p = _resolve_file_path(file_path)
    if p is None or not p.is_file():
        logger.warning("文件不存在，无法发送: %s（已尝试仓库根目录和递归搜索）", file_path)
        return

    size = p.stat().st_size
    try:
        file_param, hint = await asyncio.to_thread(_file_payload_for_napcat, p)
    except Exception as e:
        logger.error("准备文件数据失败 %s: %s", p, e)
        return

    logger.info("准备发送文件: %s (%d bytes) [%s]", p, size, hint)

    if msg_type == "private" and user_id is not None:
        payload = {
            "action": "upload_private_file",
            "params": {
                "user_id": user_id,
                "file": file_param,
                "name": p.name,
            },
        }
    elif msg_type == "group" and group_id is not None:
        payload = {
            "action": "upload_group_file",
            "params": {
                "group_id": group_id,
                "file": file_param,
                "name": p.name,
            },
        }
    else:
        logger.warning("无法确定发送目标 (msg_type=%s, user_id=%s, group_id=%s)",
                        msg_type, user_id, group_id)
        return

    import os as _os

    api = _os.environ.get("ONEBOT_FILE_API", "upload").strip().lower()
    if api in ("send_msg", "msg", "segment"):
        message = [{"type": "file", "data": {"name": p.name, "file": file_param}}]
        sm: dict = {
            "action": "send_msg",
            "params": {"message_type": msg_type, "message": message},
        }
        if msg_type == "private" and user_id is not None:
            sm["params"]["user_id"] = user_id
        elif msg_type == "group" and group_id is not None:
            sm["params"]["group_id"] = group_id
        logger.info("发送文件API: send_msg(file) name=%s [%s]", p.name, hint.split(":", 1)[0])
        await ws.send(json.dumps(sm))
        return

    logger.info(
        "发送文件API: action=%s name=%s mode=%s",
        payload["action"],
        p.name,
        hint.split(":", 1)[0],
    )
    await ws.send(json.dumps(payload))


async def _steal_sticker(url: str, user_id: str, group_id: str) -> None:
    """后台下载别人发的图片并存入表情包收藏（偷表情包）。"""
    try:
        from runner.sticker_manager import save_sticker_from_url, auto_tag_sticker
        entry = await asyncio.to_thread(
            save_sticker_from_url, url,
            source_user=user_id, source_group=group_id,
        )
        if entry:
            logger.info("偷到表情包: %s (from user=%s)", entry["id"], user_id)
            await asyncio.to_thread(auto_tag_sticker, entry["id"])
    except Exception as e:
        logger.debug("偷表情包失败: %s", e)


async def _send_sticker_image(
    ws,
    msg_type: str,
    user_id: int | None,
    group_id: int | None,
    sticker_path: Path,
) -> bool:
    """用 base64 将表情包图片作为图片消息发出。

    NapCat 在 Windows 端无法访问 WSL 路径，所以和语音一样必须用 base64://。
    """
    try:
        from runner.media_tools import file_to_base64
        b64 = await asyncio.to_thread(file_to_base64, sticker_path)
    except Exception as e:
        logger.warning("表情包 base64 编码失败 (%s): %s", sticker_path, e)
        return False

    message = [{"type": "image", "data": {"file": f"base64://{b64}"}}]
    payload: dict = {
        "action": "send_msg",
        "params": {"message_type": msg_type, "message": message},
    }
    if msg_type == "private" and user_id is not None:
        payload["params"]["user_id"] = user_id
    elif msg_type == "group" and group_id is not None:
        payload["params"]["group_id"] = group_id
    await ws.send(json.dumps(payload))
    return True


async def _send_sticker(
    ws,
    msg_type: str,
    user_id: int | None,
    group_id: int | None,
    mood: str,
) -> bool:
    """根据 mood 从收藏中选一张表情包并发送。返回是否成功。"""
    try:
        from runner.sticker_manager import pick_sticker_for_mood, get_sticker_path

        entry = await asyncio.to_thread(pick_sticker_for_mood, mood)
        if not entry:
            return False

        sticker_path = await asyncio.to_thread(get_sticker_path, entry["id"])
        if not sticker_path:
            return False

        ok = await _send_sticker_image(ws, msg_type, user_id, group_id, sticker_path)
        if ok:
            logger.info("发送表情包: %s (mood=%s, tags=%s)", entry["id"], mood,
                        ",".join(entry.get("tags", [])))
        return ok
    except Exception as e:
        logger.debug("发送表情包失败: %s", e)
        return False


async def _send_random_sticker(
    ws,
    msg_type: str,
    user_id: int | None,
    group_id: int | None,
) -> bool:
    """从收藏中随机选一张表情包发送（用于强制插入）。"""
    try:
        from runner.sticker_manager import pick_sticker_for_mood, get_sticker_path
        moods = ["开心", "卖萌", "可爱", "有趣", "嘿嘿", ""]
        entry = await asyncio.to_thread(pick_sticker_for_mood, random.choice(moods))
        if not entry:
            return False
        sticker_path = await asyncio.to_thread(get_sticker_path, entry["id"])
        if not sticker_path:
            return False
        ok = await _send_sticker_image(ws, msg_type, user_id, group_id, sticker_path)
        if ok:
            logger.info("强制插入表情包: %s (tags=%s)", entry["id"],
                        ",".join(entry.get("tags", [])))
        return ok
    except Exception:
        return False


async def _process_media_tags_and_send(
    ws,
    msg_type: str,
    user_id: int | None,
    group_id: int | None,
    text: str,
) -> None:
    """解析回复中的媒体标签，拆分为文字和多媒体分别发送。

    媒体标签格式：
      [IMG:path_or_url]    — 发送图片
      [VOICE:要说的文字]   — TTS 合成后发送语音条
      [FILE:本地文件路径]  — 发送文件
      [FACE:表情ID]        — 发送 QQ 表情
      [STICKER:情绪关键词]  — 从收藏中选择匹配的表情包发送
    """
    remaining = text

    voice_matches = list(_MEDIA_TAG_VOICE.finditer(remaining))
    for m in reversed(voice_matches):
        tts_text = m.group(1).strip()
        remaining = remaining[:m.start()] + remaining[m.end():]
        if tts_text:
            try:
                from runner.media_tools import tts_generate, file_to_base64
                audio_path = await asyncio.to_thread(tts_generate, tts_text)
                b64 = await asyncio.to_thread(file_to_base64, audio_path)
                await _send_voice_base64(ws, msg_type, user_id, group_id, b64)
            except Exception as e:
                logger.error("TTS 发送失败: %s", e)

    file_matches = list(_MEDIA_TAG_FILE.finditer(remaining))
    for i, m in enumerate(reversed(file_matches)):
        file_path = m.group(1).strip()
        remaining = remaining[:m.start()] + remaining[m.end():]
        if file_path:
            resolved = _resolve_file_path(file_path)
            if resolved and resolved.is_file():
                logger.info("FILE标签解析: '%s' → %s", file_path, resolved)
                await _send_file_via_api(ws, msg_type, user_id, group_id, str(resolved))
                # 多个 [FILE:] 连发时稍间隔，降低 NapCat / 风控失败率
                if i < len(file_matches) - 1:
                    await asyncio.sleep(0.4)
            else:
                logger.warning("FILE标签路径无法解析: '%s'", file_path)
                fallback = f"抱歉，小白找不到文件 \"{file_path}\"，可以告诉小白完整路径吗？"
                await _send_raw_cq(ws, msg_type, user_id, group_id, fallback)

    img_matches = list(_MEDIA_TAG_IMAGE.finditer(remaining))
    for m in reversed(img_matches):
        img_src = m.group(1).strip()
        remaining = remaining[:m.start()] + remaining[m.end():]
        if img_src:
            from runner.media_tools import build_image_cq
            cq = build_image_cq(img_src)
            await _send_raw_cq(ws, msg_type, user_id, group_id, cq)

    sticker_matches = list(_MEDIA_TAG_STICKER.finditer(remaining))
    for m in reversed(sticker_matches):
        sticker_mood = m.group(1).strip()
        remaining = remaining[:m.start()] + remaining[m.end():]
        if sticker_mood:
            await _send_sticker(ws, msg_type, user_id, group_id, sticker_mood)

    face_matches = list(_MEDIA_TAG_FACE.finditer(remaining))
    for m in reversed(face_matches):
        face_id = m.group(1).strip()
        remaining = remaining[:m.start()] + remaining[m.end():]
        cq = f"[CQ:face,id={face_id}]"
        remaining_before = remaining[:m.start()] if m.start() < len(remaining) else ""
        remaining = remaining  # face 直接内嵌到文字消息

    remaining = remaining.strip()
    if remaining:
        chunks = _split_message(remaining)
        for i, chunk in enumerate(chunks):
            if i > 0:
                await asyncio.sleep(random.uniform(0.8, 1.8))
            await _send_raw_cq(ws, msg_type, user_id, group_id, chunk)


async def _send_single(
    ws,
    msg_type: str,
    user_id: int | None,
    group_id: int | None,
    text: str,
) -> None:
    """Send one QQ message, detecting and handling media tags."""
    has_media_tags = any(
        pat.search(text)
        for pat in [_MEDIA_TAG_IMAGE, _MEDIA_TAG_VOICE, _MEDIA_TAG_FILE, _MEDIA_TAG_FACE, _MEDIA_TAG_STICKER]
    )

    if has_media_tags:
        await _process_media_tags_and_send(ws, msg_type, user_id, group_id, text)
    else:
        chunks = _split_message(text)
        for i, chunk in enumerate(chunks):
            if i > 0:
                await asyncio.sleep(random.uniform(0.8, 1.8))
            payload: dict = {
                "action": "send_msg",
                "params": {
                    "message_type": msg_type,
                    "message": chunk,
                },
            }
            if msg_type == "private" and user_id is not None:
                payload["params"]["user_id"] = user_id
            elif msg_type == "group" and group_id is not None:
                payload["params"]["group_id"] = group_id
            await ws.send(json.dumps(payload))


_reply_counters: dict[str, int] = {}


async def _send_reply(
    ws,
    msg_type: str,
    user_id: int | None,
    group_id: int | None,
    text: str,
    *,
    humanize_delay: bool = False,
) -> None:
    """Send a reply, splitting on ||| into separate messages with human-like delays.

    强制表情包：每 2 次回复（不是每 2 条消息），在回复发完后追加一张表情包。
    """
    if _MULTI_MSG_SEP in text:
        parts = [p.strip() for p in text.split(_MULTI_MSG_SEP) if p.strip()]
    else:
        parts = [text]

    for i, part in enumerate(parts):
        if i > 0:
            char_count = len(part)
            if humanize_delay:
                base_delay = random.uniform(2.0, 5.0)
                typing_delay = min(char_count * 0.1, 4.0)
            else:
                base_delay = random.uniform(1.0, 2.5)
                typing_delay = min(char_count * 0.05, 2.0)
            await asyncio.sleep(base_delay + typing_delay)
        await _send_single(ws, msg_type, user_id, group_id, part)

    counter_key = f"{msg_type}:{user_id}:{group_id or ''}"
    _reply_counters[counter_key] = _reply_counters.get(counter_key, 0) + 1
    if _reply_counters[counter_key] >= 2:
        _reply_counters[counter_key] = 0
        await asyncio.sleep(random.uniform(0.5, 1.5))
        ok = await _send_random_sticker(ws, msg_type, user_id, group_id)
        if not ok:
            logger.debug("表情包收藏为空或发送失败，跳过本次强制插入")


async def _handle_request(ws, event: dict, config: OneBotConfig) -> None:
    """处理好友/群请求事件：自动同意 + 通知主人确认人设。"""
    request_type = event.get("request_type", "")

    if request_type == "friend":
        flag = event.get("flag", "")
        user_id = str(event.get("user_id", ""))
        comment = event.get("comment", "")
        nickname = comment or user_id

        await ws.send(json.dumps({
            "action": "set_friend_add_request",
            "params": {"flag": flag, "approve": True},
        }))
        logger.info("自动同意好友请求: %s (%s)", nickname, user_id)

        if config.owner_qq:
            owner_id = int(config.owner_qq)
            notice = (
                f"有新好友 {nickname}({user_id}) 加了小白~\n"
                f"小白会先用默认身份跟ta聊天\n"
                f"如果需要特殊人设，回复「对{user_id}扮演xxx」"
            )
            await _send_reply(ws, "private", owner_id, None, notice)

    elif request_type == "group":
        flag = event.get("flag", "")
        sub_type = event.get("sub_type", "")
        if sub_type == "invite":
            await ws.send(json.dumps({
                "action": "set_group_add_request",
                "params": {"flag": flag, "sub_type": "invite", "approve": True},
            }))
            group_id = event.get("group_id", "")
            logger.info("自动同意入群邀请: group %s", group_id)


async def _handle_message(ws, event: dict, config: OneBotConfig) -> None:
    """Buffer incoming messages and process them after a quiet window."""
    msg_type = event.get("message_type", "")
    raw_message = event.get("raw_message", "") or ""
    user_id = event.get("user_id")
    group_id = event.get("group_id")
    sender = event.get("sender", {})
    nickname = sender.get("nickname", str(user_id))

    if msg_type == "private" and not config.reply_private:
        return
    if msg_type == "group" and not config.reply_group_at:
        return

    if msg_type == "group":
        at_matches = _CQ_AT_RE.findall(raw_message)
        if config.self_qq not in at_matches:
            return
        text = _CQ_AT_RE.sub("", raw_message).strip()
    else:
        text = raw_message

    media = _extract_media_from_event(event)
    has_media = any(media[k] for k in ("images", "records", "files"))

    text_only = _strip_cq_codes(text)

    if not text_only and not has_media:
        return

    if not config.is_user_allowed(str(user_id)):
        logger.info("Blocked message from user %s (not in admin list)", user_id)
        return

    is_owner = config.is_owner(str(user_id))
    role = "owner" if is_owner else "public"
    uid_str = str(user_id)
    user_display = f"{nickname}({user_id})"

    logger.info(
        "[%s][%s] %s (%s): %s (media: images=%d, records=%d, files=%d)",
        msg_type,
        role,
        nickname,
        user_id,
        text_only[:80],
        len(media["images"]),
        len(media["records"]),
        len(media["files"]),
    )

    media_context_parts: list[str] = []
    for img in media["images"]:
        url = img.get("url") or img.get("file", "")
        file_id = img.get("file_id", "") or img.get("file", "")
        if url or file_id:
            logger.info("识别图片: url=%s, file=%s, file_id=%s",
                        img.get("url", "")[:120], img.get("file", "")[:60], file_id[:60])
            desc = await _recognize_image(url, ws=ws, file_id=file_id)
            media_context_parts.append(f"[收到图片: {desc}]")

    for rec in media["records"]:
        url = rec.get("url") or rec.get("path", "") or rec.get("file", "")
        if url:
            stt_text = await _recognize_voice(url)
            media_context_parts.append(f"[收到语音: {stt_text}]")

    for f in media["files"]:
        fname = f.get("name") or f.get("file", "")
        media_context_parts.append(f"[收到文件: {fname}]")

    final_text = text_only
    if media_context_parts:
        media_info = "\n".join(media_context_parts)
        final_text = f"{media_info}\n{text_only}".strip() if text_only else media_info

    if not final_text:
        return

    buf_key = f"{msg_type}:{user_id}:{group_id or ''}"

    if buf_key not in _msg_locks:
        _msg_locks[buf_key] = asyncio.Lock()

    async with _msg_locks[buf_key]:
        if buf_key not in _msg_buffers:
            _msg_buffers[buf_key] = []

        _msg_buffers[buf_key].append({
            "text": final_text,
            "msg_type": msg_type,
            "user_id": user_id,
            "group_id": group_id,
            "user_display": user_display,
            "role": role,
            "is_owner": is_owner,
        })

        if buf_key in _msg_timers and not _msg_timers[buf_key].done():
            _msg_timers[buf_key].cancel()

        _msg_timers[buf_key] = asyncio.create_task(
            _flush_after_window(ws, config, buf_key)
        )


async def _flush_after_window(ws, config: OneBotConfig, buf_key: str) -> None:
    """Wait for the aggregation window, then process all buffered messages."""
    await asyncio.sleep(MSG_AGGREGATE_WINDOW)

    async with _msg_locks[buf_key]:
        messages = _msg_buffers.pop(buf_key, [])
        _msg_timers.pop(buf_key, None)

    if not messages:
        return

    first = messages[0]
    msg_type = first["msg_type"]
    user_id = first["user_id"]
    group_id = first["group_id"]
    user_display = first["user_display"]
    role = first["role"]
    is_owner = first["is_owner"]

    if len(messages) == 1:
        combined_text = messages[0]["text"]
    else:
        parts = [m["text"] for m in messages]
        combined_text = "\n".join(parts)
        logger.info("聚合 %d 条消息来自 %s", len(messages), user_display)

    has_persona = role != "owner" and is_user_ready(user_display)

    if has_persona:
        await asyncio.sleep(random.uniform(2.0, 5.0))

    try:
        result = await asyncio.to_thread(
            process_remote_message,
            source="qq-onebot",
            user=user_display,
            text=combined_text,
            role=role,
        )
    except Exception:
        logger.error("Gateway error: %s", traceback.format_exc())
        return

    if not result or not result.strip():
        logger.warning("Gateway 返回空结果，不发送")
        return

    logger.info("回复内容 (%d chars): %s", len(result), result[:150].replace('\n', '\\n'))
    await _send_reply(
        ws, msg_type, user_id, group_id, result,
        humanize_delay=has_persona,
    )

    if is_owner and msg_type == "private":
        import time as _time
        global _owner_last_activity, _proactive_sent_unanswered
        _owner_last_activity = _time.time()
        _proactive_sent_unanswered = False
        _schedule_proactive(ws, config)


def _schedule_proactive(ws, config: OneBotConfig) -> None:
    """Cancel any existing proactive timer for owner and start a new one."""
    global _proactive_task
    if _proactive_task and not _proactive_task.done():
        _proactive_task.cancel()
    _proactive_task = asyncio.create_task(_proactive_followup(ws, config))


async def _proactive_followup(ws, config: OneBotConfig) -> None:
    """Wait for idle period, then check fleet status or send casual message.

    Priority: fleet completion > fleet blocked > casual chat.
    Only fires once per idle gap.
    """
    global _proactive_sent_unanswered
    import time as _time

    if not config.owner_qq:
        return

    wait = random.uniform(PROACTIVE_IDLE_MIN, PROACTIVE_IDLE_MAX)
    await asyncio.sleep(wait)

    if _proactive_sent_unanswered:
        return

    if _time.time() - _owner_last_activity < wait * 0.9:
        return

    fleet_hint = _check_fleet_for_proactive()

    if fleet_hint:
        proactive_hint = fleet_hint
    else:
        proactive_hint = (
            "[系统提示：小侑已经有一段时间没说话了。"
            "你可以主动发一条消息，比如汇报一下刚才做了什么、"
            "分享一个发现、或者随口聊点什么。"
            "像朋友之间自然地找话题。"
            "不要说'你还在吗'这种话。简短一句就好。]"
        )

    try:
        result = await asyncio.to_thread(
            process_remote_message,
            source="qq-onebot",
            user=f"owner({config.owner_qq})",
            text=proactive_hint,
            role="owner",
        )
    except Exception:
        logger.error("Proactive message error: %s", traceback.format_exc())
        return

    if result and result.strip():
        _proactive_sent_unanswered = True
        await _send_reply(ws, "private", int(config.owner_qq), None, result)
        logger.info("Sent proactive message to owner (fleet=%s)", bool(fleet_hint))


def _check_fleet_for_proactive() -> str | None:
    """Check if fleet has completed tasks or blocked agents to report."""
    try:
        from fleet.scheduler import get_fleet_scheduler
        scheduler = get_fleet_scheduler()
        if not scheduler or not scheduler._running:
            return None

        snap = scheduler.metrics.get_snapshot()

        if scheduler._dashboard and scheduler._dashboard.is_all_done() and snap.total_completed > 0:
            return (
                f"[系统提示：Multi-Agent 所有任务已完成！"
                f"共完成 {snap.total_completed} 个任务"
                f"（成功 {snap.total_ok}，失败 {snap.total_failed}）。"
                f"请向小侑汇报任务完成情况，简洁说明完成了什么、"
                f"有没有失败的。用小白的口吻，像朋友间汇报工作。]"
            )

        blocked = scheduler.drain_blocked_notifications()
        if blocked:
            details = []
            for b in blocked[:3]:
                w = b.get("worker", "?")
                short_w = w.rsplit("-", 2)[0] if "-" in w else w
                details.append(f"{short_w}: {b.get('reason', '未知')[:100]}")
            block_info = "\n".join(details)
            return (
                f"[系统提示：有 {len(blocked)} 个 Agent 遇到阻塞，需要小侑定夺。"
                f"阻塞详情：\n{block_info}\n"
                f"请向小侑汇报这些阻塞情况，说清楚是谁被卡住了、原因是什么，"
                f"然后问小侑怎么处理。用小白的口吻。]"
            )

        if snap.active_workers > 0:
            return None

    except Exception:
        pass
    return None


_BLOCKED_POLL_INTERVAL = 30  # seconds


async def _poll_blocked_notifications(ws, config: OneBotConfig) -> None:
    """Periodically check for blocked workers and notify the owner via QQ.

    Runs as a background task alongside the main WebSocket listener.
    When a fleet worker reports a blocked state, the scheduler collects it.
    This function drains those notifications and sends them to the owner.
    """
    if not config.owner_qq:
        return

    while True:
        await asyncio.sleep(_BLOCKED_POLL_INTERVAL)
        try:
            from fleet.scheduler import get_fleet_scheduler
            scheduler = get_fleet_scheduler()
            if not scheduler:
                continue

            items = scheduler.drain_blocked_notifications()
            if not items:
                continue

            for item in items:
                worker = item.get("worker", "?")
                short_worker = worker.rsplit("-", 2)[0] if "-" in worker else worker
                project = item.get("project", "?")
                task_id = item.get("task_id", "?")[:12]
                reason = item.get("reason", "未说明原因")

                notice = (
                    f"⚠️ Agent 遇到阻塞，需要你定夺！\n\n"
                    f"Agent: {short_worker}\n"
                    f"项目: {project}\n"
                    f"任务: {task_id}\n"
                    f"阻塞原因:\n{reason[:500]}\n\n"
                    f"请告诉小白怎么处理~"
                )
                await _send_reply(
                    ws, "private", int(config.owner_qq), None, notice
                )
                logger.info(
                    "Sent blocked notification to owner: worker=%s task=%s",
                    short_worker, task_id,
                )
        except asyncio.CancelledError:
            return
        except Exception:
            logger.debug("Blocked poll error", exc_info=True)


async def _run(config: OneBotConfig) -> None:
    """Main loop: connect to NapCat WebSocket and listen for messages."""
    logger.info("正在连接 NapCatQQ: %s", config.ws_url)
    logger.info("小白 QQ 号: %s", config.self_qq)
    if config.owner_qq:
        logger.info("主人 QQ 号: %s", config.owner_qq)
    else:
        logger.warning("未配置 ONEBOT_OWNER_QQ! 所有用户都会被视为普通用户!")
    logger.info("回复私聊: %s, 回复群@: %s", config.reply_private, config.reply_group_at)
    if config.token:
        logger.info("Token: 已配置")
    if config.admin_users:
        logger.info("允许用户: %s", ", ".join(config.admin_users))
    else:
        logger.info("允许用户: 所有人")

    ws_url = config.ws_url
    headers: dict[str, str] = {}
    if config.token:
        sep = "&" if "?" in ws_url else "?"
        ws_url = f"{ws_url}{sep}access_token={config.token}"
        headers["Authorization"] = f"Bearer {config.token}"

    logger.info("连接地址: %s", ws_url)

    blocked_poller: asyncio.Task | None = None

    while True:
        try:
            async with ws_connect(
                ws_url,
                additional_headers=headers if headers else None,
                ping_interval=20,
                ping_timeout=20,
                close_timeout=10,
            ) as ws:
                logger.info("已连接到 NapCatQQ! 小白 QQ 端上线~")

                blocked_poller = asyncio.create_task(
                    _poll_blocked_notifications(ws, config)
                )

                async for raw in ws:
                    try:
                        event = json.loads(raw)
                    except json.JSONDecodeError:
                        continue

                    post_type = event.get("post_type", "")

                    if post_type == "meta_event":
                        meta_type = event.get("meta_event_type", "")
                        if meta_type == "lifecycle":
                            logger.info("NapCat lifecycle: %s", event.get("sub_type", ""))
                        continue

                    if post_type == "request":
                        asyncio.create_task(_handle_request(ws, event, config))
                        continue

                    if post_type == "message":
                        asyncio.create_task(_handle_message(ws, event, config))
                        continue

        except (ConnectionError, OSError, ConnectionClosed) as e:
            if blocked_poller and not blocked_poller.done():
                blocked_poller.cancel()
            logger.warning("WebSocket 断开: %s — 5 秒后重连...", e)
            await asyncio.sleep(5)
        except Exception as e:
            if blocked_poller and not blocked_poller.done():
                blocked_poller.cancel()
            logger.error("未知错误: %s — 10 秒后重连...", e)
            await asyncio.sleep(10)


def main() -> None:
    from runner.media_tools import start_cleanup_daemon
    start_cleanup_daemon()

    config = OneBotConfig.from_env()
    try:
        asyncio.run(_run(config))
    except KeyboardInterrupt:
        logger.info("小白 QQ 端下线了~ 再见！")


if __name__ == "__main__":
    main()
