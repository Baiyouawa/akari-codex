"""OneBot11 WebSocket 客户端 — 连接 NapCatQQ，让小白用普通 QQ 号收发消息。

架构：
    NapCatQQ (QQ协议端, 用你的QQ号登录)
        ↕ OneBot11 正向 WebSocket
    onebot_client.py (本模块)
        → runner.gateway.process_remote_message()
        → ChatBot (小白) 生成回复
        → 通过 WebSocket 调用 send_msg 发回 QQ

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

_owner_last_activity: float = 0.0
_proactive_task: asyncio.Task | None = None  # type: ignore[type-arg]
_proactive_sent_unanswered: bool = False


def _strip_cq_codes(text: str) -> str:
    """Remove all CQ codes from message text."""
    return re.sub(r"\[CQ:[^\]]+\]", "", text).strip()


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


async def _send_single(
    ws,
    msg_type: str,
    user_id: int | None,
    group_id: int | None,
    text: str,
) -> None:
    """Send one QQ message (handles long-message chunking internally)."""
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
    """Process a single incoming message event."""
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
        text = _strip_cq_codes(raw_message)

    if not text:
        return

    if not config.is_user_allowed(str(user_id)):
        logger.info("Blocked message from user %s (not in admin list)", user_id)
        return

    is_owner = config.is_owner(str(user_id))
    role = "owner" if is_owner else "public"
    uid_str = str(user_id)
    user_display = f"{nickname}({user_id})"

    logger.info(
        "[%s][%s] %s (%s): %s",
        msg_type,
        role,
        nickname,
        user_id,
        text[:100],
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

    has_persona = role != "owner" and is_user_ready(user_display)

    if has_persona:
        await asyncio.sleep(random.uniform(2.0, 6.0))

    try:
        result = await asyncio.to_thread(
            process_remote_message,
            source="qq-onebot",
            user=user_display,
            text=text,
            role=role,
        )
    except Exception:
        logger.error("Gateway error: %s", traceback.format_exc())
        return

    if not result or not result.strip():
        return

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
