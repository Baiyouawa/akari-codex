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
import re
import sys
import traceback
from pathlib import Path

try:
    import websockets
    import websockets.client
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

logger = logging.getLogger("xiaobai.onebot")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
)

QQ_MSG_LIMIT = 4500

_CQ_AT_RE = re.compile(r"\[CQ:at,qq=(\d+)[^\]]*\]")


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


async def _send_reply(
    ws,
    msg_type: str,
    user_id: int | None,
    group_id: int | None,
    text: str,
) -> None:
    """Send a reply message via OneBot11 send_msg API."""
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
        await asyncio.sleep(0.5)


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
        reply = "嗯？小侑你 @ 小白了但没说话呀~ 想让小白做什么呢？"
        await _send_reply(ws, msg_type, user_id, group_id, reply)
        return

    if not config.is_user_allowed(str(user_id)):
        logger.info("Blocked message from user %s (not in admin list)", user_id)
        return

    logger.info(
        "[%s] %s (%s): %s",
        msg_type,
        nickname,
        user_id,
        text[:100],
    )

    try:
        result = await asyncio.to_thread(
            process_remote_message,
            source="qq-onebot",
            user=f"{nickname}({user_id})",
            text=text,
        )
    except Exception:
        tb = traceback.format_exc()
        logger.error("Gateway error: %s", tb)
        result = f"呜...小白出了点问题: {tb[-300:]}"

    await _send_reply(ws, msg_type, user_id, group_id, result)


async def _run(config: OneBotConfig) -> None:
    """Main loop: connect to NapCat WebSocket and listen for messages."""
    logger.info("正在连接 NapCatQQ: %s", config.ws_url)
    logger.info("小白 QQ 号: %s", config.self_qq)
    logger.info("回复私聊: %s, 回复群@: %s", config.reply_private, config.reply_group_at)
    if config.admin_users:
        logger.info("允许用户: %s", ", ".join(config.admin_users))
    else:
        logger.info("允许用户: 所有人")

    while True:
        try:
            async with websockets.client.connect(
                config.ws_url,
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

                    if event.get("post_type") == "meta_event":
                        meta_type = event.get("meta_event_type", "")
                        if meta_type == "lifecycle":
                            logger.info("NapCat lifecycle: %s", event.get("sub_type", ""))
                        continue

                    if event.get("post_type") != "message":
                        continue

                    asyncio.create_task(_handle_message(ws, event, config))

        except (ConnectionError, OSError, websockets.exceptions.ConnectionClosed) as e:
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
