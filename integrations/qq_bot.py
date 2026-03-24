"""QQ Official Bot integration for OpenAkari-Codex.

Listens for @-mentions in QQ guilds/groups and dispatches commands
through the unified gateway.

Prerequisites:
    pip install qq-botpy

Usage:
    export QQ_BOT_APPID="your_appid"
    export QQ_BOT_TOKEN="your_token"
    python -m integrations.qq_bot

Architecture:
    QQ @message -> AkariQQBot.on_at_message_create()
                -> runner.gateway.process_remote_message()
                -> ChatBot.process_message()
                -> result posted back to QQ channel
"""

from __future__ import annotations

import asyncio
import logging
import sys
import traceback
from pathlib import Path

try:
    import botpy
    from botpy import logging as botpy_logging
    from botpy.message import GroupMessage, Message
except ImportError:
    print(
        "qq-botpy is not installed. Run: pip install qq-botpy",
        file=sys.stderr,
    )
    sys.exit(1)

# Ensure project root is on sys.path so runner.* imports work
_project_root = Path(__file__).resolve().parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from integrations.config_qq import QQBotConfig
from runner.gateway import process_remote_message

logger = logging.getLogger("akari.qq")

QQ_MESSAGE_LIMIT = 2000


def _split_message(text: str, limit: int = QQ_MESSAGE_LIMIT) -> list[str]:
    """Split long text into chunks that fit QQ message limits."""
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


class AkariQQBot(botpy.Client):
    """QQ Bot client that forwards messages to OpenAkari-Codex gateway."""

    def __init__(self, qq_config: QQBotConfig, **kwargs):
        super().__init__(**kwargs)
        self.qq_config = qq_config

    async def on_ready(self):
        logger.info("Akari QQ Bot is ready! (appid=%s)", self.qq_config.appid)

    async def on_at_message_create(self, message: Message):
        """Handle @-mention messages in guild channels."""
        user_id = str(message.author.id)
        username = message.author.username or user_id
        text = (message.content or "").strip()

        # Remove the @bot mention prefix that QQ prepends
        if text.startswith("<@"):
            # Format: <@!botid> actual message
            parts = text.split(">", 1)
            if len(parts) > 1:
                text = parts[1].strip()

        if not text:
            await self.api.post_message(
                channel_id=message.channel_id,
                content="请在 @ 后面写上指令哦~ 例如: @Akari 调研 multi-agent 论文",
                msg_id=message.id,
            )
            return

        if not self.qq_config.is_user_allowed(user_id):
            await self.api.post_message(
                channel_id=message.channel_id,
                content=f"用户 {username} 不在允许列表中，请联系管理员。",
                msg_id=message.id,
            )
            return

        logger.info("Command from %s (%s): %s", username, user_id, text)

        await self.api.post_message(
            channel_id=message.channel_id,
            content=f"收到指令，正在执行...\n> {text[:100]}",
            msg_id=message.id,
        )

        try:
            result = await asyncio.to_thread(
                process_remote_message,
                source="qq",
                user=f"{username}({user_id})",
                text=text,
            )
        except Exception:
            tb = traceback.format_exc()
            logger.error("Gateway error: %s", tb)
            result = f"执行出错:\n{tb[-500:]}"

        chunks = _split_message(result)
        for chunk in chunks:
            await self.api.post_message(
                channel_id=message.channel_id,
                content=chunk,
                msg_id=message.id,
            )

    async def on_group_at_message_create(self, message: GroupMessage):
        """Handle @-mention messages in QQ groups (if enabled)."""
        user_id = str(message.author.member_openid)
        text = (message.content or "").strip()

        if text.startswith("<@"):
            parts = text.split(">", 1)
            if len(parts) > 1:
                text = parts[1].strip()

        if not text:
            await message._api.post_group_message(
                group_openid=message.group_openid,
                content="请在 @ 后面写上指令~ 例如: @Akari 查看状态",
                msg_id=message.id,
            )
            return

        logger.info("Group command from %s: %s", user_id, text)

        await message._api.post_group_message(
            group_openid=message.group_openid,
            content=f"收到指令，正在执行...\n> {text[:100]}",
            msg_id=message.id,
        )

        try:
            result = await asyncio.to_thread(
                process_remote_message,
                source="qq-group",
                user=user_id,
                text=text,
            )
        except Exception:
            tb = traceback.format_exc()
            logger.error("Gateway error: %s", tb)
            result = f"执行出错:\n{tb[-500:]}"

        chunks = _split_message(result)
        for chunk in chunks:
            await message._api.post_group_message(
                group_openid=message.group_openid,
                content=chunk,
                msg_id=message.id,
            )


def main() -> None:
    qq_config = QQBotConfig.from_env()

    intents = botpy.Intents(
        public_guild_messages=True,
        guild_messages=True,
    )

    bot = AkariQQBot(qq_config=qq_config, intents=intents)

    logger.info(
        "Starting Akari QQ Bot (appid=%s, sandbox=%s)",
        qq_config.appid,
        qq_config.sandbox,
    )

    bot.run(
        appid=qq_config.appid,
        secret=qq_config.secret or qq_config.token,
    )


if __name__ == "__main__":
    main()
