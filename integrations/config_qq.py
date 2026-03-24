"""OneBot11 QQ 客户端配置（基于 NapCatQQ 协议端）。

所有配置项都有内置默认值，可通过同名环境变量覆盖。
直接 `python3 -m integrations.onebot_client` 即可启动，无需任何 export。
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field

_DEFAULTS = {
    "self_qq": "3759826713",
    "owner_qq": "1094638877",
    "ws_url": "ws://172.28.144.1:3002",
    "token": "AuuTxNtTKV_Jpt2T",
}


@dataclass(frozen=True)
class OneBotConfig:
    self_qq: str
    owner_qq: str = ""
    ws_url: str = "ws://localhost:3001"
    token: str = ""
    admin_users: frozenset[str] = field(default_factory=frozenset)
    reply_private: bool = True
    reply_group_at: bool = True

    @classmethod
    def from_env(cls) -> OneBotConfig:
        raw_admins = os.environ.get("ONEBOT_ADMIN_USERS", "").strip()
        admins = frozenset(
            u.strip() for u in raw_admins.split(",") if u.strip()
        ) if raw_admins else frozenset()

        return cls(
            self_qq=os.environ.get("ONEBOT_SELF_QQ", _DEFAULTS["self_qq"]),
            owner_qq=os.environ.get("ONEBOT_OWNER_QQ", _DEFAULTS["owner_qq"]),
            ws_url=os.environ.get("ONEBOT_WS_URL", _DEFAULTS["ws_url"]),
            token=os.environ.get("ONEBOT_TOKEN", _DEFAULTS["token"]),
            admin_users=admins,
            reply_private=os.environ.get("ONEBOT_REPLY_PRIVATE", "1") == "1",
            reply_group_at=os.environ.get("ONEBOT_REPLY_GROUP_AT", "1") == "1",
        )

    def is_owner(self, user_id: str) -> bool:
        return bool(self.owner_qq) and user_id == self.owner_qq

    def is_user_allowed(self, user_id: str) -> bool:
        if self.is_owner(user_id):
            return True
        if not self.admin_users:
            return True
        return user_id in self.admin_users
