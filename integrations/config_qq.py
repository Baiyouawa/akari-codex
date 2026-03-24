"""QQ Bot configuration loaded from environment variables.

Required env vars:
    QQ_BOT_APPID  — Bot application ID from q.qq.com
    QQ_BOT_TOKEN  — Bot token from q.qq.com

Optional env vars:
    QQ_BOT_SECRET    — (Optional) Bot secret for webhook verification
    QQ_BOT_SANDBOX   — Set to "1" to use sandbox environment (default: "0")
    QQ_ADMIN_USERS   — Comma-separated list of allowed QQ user IDs (empty = allow all)
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class QQBotConfig:
    appid: str
    token: str
    secret: str = ""
    sandbox: bool = False
    admin_users: frozenset[str] = field(default_factory=frozenset)

    @classmethod
    def from_env(cls) -> QQBotConfig:
        appid = os.environ.get("QQ_BOT_APPID", "")
        if not appid:
            raise EnvironmentError(
                "QQ_BOT_APPID is required. Register at https://q.qq.com"
            )
        token = os.environ.get("QQ_BOT_TOKEN", "")
        if not token:
            raise EnvironmentError(
                "QQ_BOT_TOKEN is required. Get it from the QQ Bot dashboard."
            )

        raw_admins = os.environ.get("QQ_ADMIN_USERS", "").strip()
        admins = frozenset(
            u.strip() for u in raw_admins.split(",") if u.strip()
        ) if raw_admins else frozenset()

        return cls(
            appid=appid,
            token=token,
            secret=os.environ.get("QQ_BOT_SECRET", ""),
            sandbox=os.environ.get("QQ_BOT_SANDBOX", "0") == "1",
            admin_users=admins,
        )

    def is_user_allowed(self, user_id: str) -> bool:
        if not self.admin_users:
            return True
        return user_id in self.admin_users
