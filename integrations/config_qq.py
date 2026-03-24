"""OneBot11 QQ 客户端配置（基于 NapCatQQ 协议端）。

Required env vars:
    ONEBOT_SELF_QQ   — 小白登录的 QQ 号（用于判断群里 @ 自己）

Optional env vars:
    ONEBOT_WS_URL    — NapCat 正向 WebSocket 地址 (default: ws://localhost:3001)
    ONEBOT_ADMIN_USERS — 逗号分隔的允许使用的 QQ 号 (empty = allow all)
    ONEBOT_REPLY_PRIVATE — 是否回复私聊 (default: "1")
    ONEBOT_REPLY_GROUP_AT — 是否回复群里 @ (default: "1")
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class OneBotConfig:
    self_qq: str
    ws_url: str = "ws://localhost:3001"
    admin_users: frozenset[str] = field(default_factory=frozenset)
    reply_private: bool = True
    reply_group_at: bool = True

    @classmethod
    def from_env(cls) -> OneBotConfig:
        self_qq = os.environ.get("ONEBOT_SELF_QQ", "")
        if not self_qq:
            raise EnvironmentError(
                "ONEBOT_SELF_QQ is required — set to the QQ number that NapCat logged in with."
            )

        raw_admins = os.environ.get("ONEBOT_ADMIN_USERS", "").strip()
        admins = frozenset(
            u.strip() for u in raw_admins.split(",") if u.strip()
        ) if raw_admins else frozenset()

        return cls(
            self_qq=self_qq,
            ws_url=os.environ.get("ONEBOT_WS_URL", "ws://localhost:3001"),
            admin_users=admins,
            reply_private=os.environ.get("ONEBOT_REPLY_PRIVATE", "1") == "1",
            reply_group_at=os.environ.get("ONEBOT_REPLY_GROUP_AT", "1") == "1",
        )

    def is_user_allowed(self, user_id: str) -> bool:
        if not self.admin_users:
            return True
        return user_id in self.admin_users
