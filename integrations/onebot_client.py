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
from runner.persona import (
    add_pending_user,
    is_pending_user,
    is_user_ready,
)

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

_owner_last_activity: float = 0.0
_proactive_task: asyncio.Task | None = None  # type: ignore[type-arg]
_proactive_sent_unanswered: bool = False


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
                "请详细描述这张图片的内容。如果有文字请完整识别出来。",
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
            "请详细描述这张图片的内容。如果有文字请完整识别出来。",
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


async def _send_file_via_api(
    ws,
    msg_type: str,
    user_id: int | None,
    group_id: int | None,
    file_path: str,
) -> None:
    """通过 OneBot API 发送文件。支持相对路径自动解析到仓库根目录。"""
    p = _resolve_file_path(file_path)
    if p is None or not p.is_file():
        logger.warning("文件不存在，无法发送: %s（已尝试仓库根目录和递归搜索）", file_path)
        return

    logger.info("准备发送文件: %s (%d bytes)", p, p.stat().st_size)

    if msg_type == "private" and user_id is not None:
        payload = {
            "action": "upload_private_file",
            "params": {
                "user_id": user_id,
                "file": str(p),
                "name": p.name,
            },
        }
    elif msg_type == "group" and group_id is not None:
        payload = {
            "action": "upload_group_file",
            "params": {
                "group_id": group_id,
                "file": str(p),
                "name": p.name,
            },
        }
    else:
        logger.warning("无法确定发送目标 (msg_type=%s, user_id=%s, group_id=%s)",
                        msg_type, user_id, group_id)
        return

    logger.info("发送文件API调用: action=%s, file=%s, name=%s",
                payload["action"], str(p), p.name)
    await ws.send(json.dumps(payload))


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
    for m in reversed(file_matches):
        file_path = m.group(1).strip()
        remaining = remaining[:m.start()] + remaining[m.end():]
        if file_path:
            resolved = _resolve_file_path(file_path)
            if resolved and resolved.is_file():
                logger.info("FILE标签解析: '%s' → %s", file_path, resolved)
                await _send_file_via_api(ws, msg_type, user_id, group_id, str(resolved))
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

    face_matches = list(_MEDIA_TAG_FACE.finditer(remaining))
    for m in reversed(face_matches):
        face_id = m.group(1).strip()
        remaining = remaining[:m.start()] + remaining[m.end():]
        cq = f"[CQ:face,id={face_id}]"
        remaining_before = remaining[:m.start()] if m.start() < len(remaining) else ""
        remaining = remaining  # face 直接内嵌到文字消息

    remaining = remaining.strip()
    if remaining:
        for chunk in _split_message(remaining):
            await _send_raw_cq(ws, msg_type, user_id, group_id, chunk)
            await asyncio.sleep(0.3)


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
        for pat in [_MEDIA_TAG_IMAGE, _MEDIA_TAG_VOICE, _MEDIA_TAG_FILE, _MEDIA_TAG_FACE]
    )

    if has_media_tags:
        await _process_media_tags_and_send(ws, msg_type, user_id, group_id, text)
    else:
        for chunk in _split_message(text):
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
            await asyncio.sleep(0.3)


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

    When humanize_delay is True, adds random delays between messages to simulate
    real typing speed. Used for persona-override conversations.
    """
    if _MULTI_MSG_SEP in text:
        parts = [p.strip() for p in text.split(_MULTI_MSG_SEP) if p.strip()]
    else:
        parts = [text]

    for i, part in enumerate(parts):
        if humanize_delay and i > 0:
            char_count = len(part)
            base_delay = random.uniform(1.5, 4.0)
            typing_delay = min(char_count * 0.08, 3.0)
            await asyncio.sleep(base_delay + typing_delay)
        await _send_single(ws, msg_type, user_id, group_id, part)


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

        add_pending_user(user_id, f"{nickname}({user_id})")

        if config.owner_qq:
            owner_id = int(config.owner_qq)
            notice = (
                f"有新好友 {nickname}({user_id}) 加了小白~\n"
                f"要按什么身份跟ta聊？\n"
                f"（回复「对{user_id}扮演xxx」来设定）"
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
    """Process a single incoming message event, including multimedia."""
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

    if role != "owner" and msg_type == "private":
        if not is_user_ready(user_display):
            if not is_pending_user(uid_str):
                add_pending_user(uid_str, user_display)
                logger.info("新用户 %s 无人设，已通知主人确认", user_display)
                if config.owner_qq:
                    notice = (
                        f"{nickname}({user_id}) 给小白发消息了，但还没设定身份~\n"
                        f"要按什么身份跟ta聊？\n"
                        f"（回复「对{user_id}扮演xxx」来设定）"
                    )
                    await _send_reply(ws, "private", int(config.owner_qq), None, notice)
            else:
                logger.debug("用户 %s 待确认中，静默", uid_str)
            return

    media_context_parts: list[str] = []

    for img in media["images"]:
        url = img.get("url") or img.get("file", "")
        file_id = img.get("file_id", "") or img.get("file", "")
        if url or file_id:
            logger.info("识别图片: url=%s, file=%s, file_id=%s",
                        img.get("url", "")[:120], img.get("file", "")[:60], file_id[:60])
            desc = await _recognize_image(url, ws=ws, file_id=file_id)
            media_context_parts.append(f"[收到图片: {desc}（简短回应即可，不要复述识别内容）]")
        else:
            logger.warning("图片无 URL 也无 file_id: %s", img)

    for rec in media["records"]:
        url = rec.get("url") or rec.get("path", "") or rec.get("file", "")
        if url:
            logger.info("识别语音: url=%s, file=%s", rec.get("url", "")[:120], rec.get("file", "")[:60])
            stt_text = await _recognize_voice(url)
            media_context_parts.append(f"[收到语音: {stt_text}（简短回应即可）]")
        else:
            logger.warning("语音无 URL: %s", rec)

    for f in media["files"]:
        fname = f.get("name") or f.get("file", "")
        media_context_parts.append(f"[收到文件: {fname}]")

    final_text = text_only
    if media_context_parts:
        media_info = "\n".join(media_context_parts)
        final_text = f"{media_info}\n{text_only}".strip() if text_only else media_info

    if not final_text:
        return

    has_persona = role != "owner" and is_user_ready(user_display)

    if has_persona:
        await asyncio.sleep(random.uniform(2.0, 6.0))

    try:
        result = await asyncio.to_thread(
            process_remote_message,
            source="qq-onebot",
            user=user_display,
            text=final_text,
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
    """Wait for idle period, then send one proactive message to owner.

    Only fires once per idle gap — if owner doesn't reply after the proactive
    message, no further proactive messages are sent until owner speaks again.
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
        logger.info("Sent proactive message to owner")


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
            logger.warning("WebSocket 断开: %s — 5 秒后重连...", e)
            await asyncio.sleep(5)
        except Exception as e:
            logger.error("未知错误: %s — 10 秒后重连...", e)
            await asyncio.sleep(10)


def main() -> None:
    config = OneBotConfig.from_env()
    try:
        asyncio.run(_run(config))
    except KeyboardInterrupt:
        logger.info("小白 QQ 端下线了~ 再见！")


if __name__ == "__main__":
    main()
