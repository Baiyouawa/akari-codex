"""Unified remote gateway for OpenAkari-Codex.

Bridges external channels (GitHub, QQ, etc.) to the existing ChatBot
without modifying any core runner code.

Usage:
    python -m runner.gateway --source github    --user "alice" --message "调研 multi-agent"
    python -m runner.gateway --source qq-onebot --user "12345" --message "查看状态"
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path
from typing import Any

from .chat import ChatBot
from .config import CodexConfig

MAX_RESULT_LENGTH = 4000

SENSITIVE_PATTERNS = [
    re.compile(r"(sk-[a-zA-Z0-9]{8,})"),
    re.compile(r"(OPENAI_API_KEY\s*=\s*\S+)"),
    re.compile(r"(/home/[^\s]+)"),
]

ALLOWED_USERS_ENV = "AKARI_ALLOWED_USERS"

BLOCKED_ACTIONS = frozenset()


def _sanitize_output(text: str) -> str:
    """Strip sensitive information from output before sending externally."""
    for pat in SENSITIVE_PATTERNS:
        text = pat.sub("[REDACTED]", text)
    return text


def _truncate(text: str, limit: int = MAX_RESULT_LENGTH) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 40] + "\n\n... (结果过长，已截断)"


def _check_user_allowed(source: str, user: str) -> bool:
    """Return True if user is allowed. If no allowlist is configured, allow all."""
    import os

    raw = os.environ.get(ALLOWED_USERS_ENV, "").strip()
    if not raw:
        return True
    entries = {e.strip().lower() for e in raw.split(",") if e.strip()}
    key = f"{source}:{user}".lower()
    return key in entries or user.lower() in entries


def _log_invocation(
    repo_root: Path,
    source: str,
    user: str,
    message: str,
    result: str,
) -> None:
    """Append a JSON-lines record to logs/remote-invocations.jsonl."""
    log_dir = repo_root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "remote-invocations.jsonl"

    record = {
        "timestamp": datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=8))
        ).strftime("%Y-%m-%d %H:%M:%S"),
        "source": source,
        "user": user,
        "message": message,
        "result_preview": result[:500],
        "result_length": len(result),
    }
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def process_remote_message(
    source: str,
    user: str,
    text: str,
    config: CodexConfig | None = None,
    *,
    role: str = "owner",
) -> str:
    """Primary entry point for all remote channels.

    Args:
        source: Channel identifier ("github", "qq", etc.)
        user: Sender identifier (GitHub username, QQ user id, etc.)
        text: The natural language command.
        config: Optional config override; defaults to CodexConfig.from_env().
        role: "owner" for the master user (full access), "public" for others
              (chat-only, no actions/tools).

    Returns:
        Sanitized, truncated result string suitable for posting back.
    """
    if not _check_user_allowed(source, user):
        return f"[{source}] 用户 {user} 不在允许列表中。请联系管理员。"

    if config is None:
        config = CodexConfig.from_env()

    cleaned = re.sub(r'^[/@]?[Aa][Kk][Aa][Rr][Ii][:\s]*', '', text.strip())
    cleaned = re.sub(r'^阿卡丽[:\s，,]*', '', cleaned).strip()
    cleaned = re.sub(r'^小白[:\s，,]*', '', cleaned).strip()
    cleaned = re.sub(r'^[Xx]iao\s*[Bb]ai[:\s]*', '', cleaned).strip()
    if not cleaned:
        cleaned = text.strip()

    bot = ChatBot(config)
    raw_result = bot.process_message(cleaned, role=role, user=user)
    safe_result = _sanitize_output(raw_result)
    final_result = _truncate(safe_result)

    _log_invocation(config.repo_home, source, user, text, final_result)
    return final_result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="OpenAkari-Codex remote gateway",
    )
    parser.add_argument("--source", required=True, help="Channel: github, qq, ...")
    parser.add_argument("--user", default="anonymous", help="Sender identifier")
    parser.add_argument("--message", required=True, help="Natural language command")
    args = parser.parse_args()

    try:
        result = process_remote_message(
            source=args.source,
            user=args.user,
            text=args.message,
        )
    except EnvironmentError as e:
        print(f"配置错误: {e}", file=sys.stderr)
        sys.exit(1)

    print(result)


if __name__ == "__main__":
    main()
