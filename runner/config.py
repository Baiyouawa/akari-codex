"""Configuration and environment handling for the Codex backend."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class CodexConfig:
    api_key: str
    base_url: str = "https://code.vangularcode.asia/v1"
    model: str = "gpt-5.4"
    repo_home: Path = field(default_factory=lambda: Path.cwd()) #仓库根目录
    max_turns: int = 20 #每个Session最多跑几轮tool-call
    max_tokens_per_turn: int = 16384
    temperature: float = 0.0
    timeout_seconds: int = 120
    shell_allowlist: tuple[str, ...] = (
        "pwd", "ls", "find", "rg", "grep", "cat", "head", "tail", "wc",
        "git status", "git log", "git diff", "git branch",
        "python", "python3", "node", "npm", "pip",
        "echo", "date", "which", "env",
    )
    shell_denylist: tuple[str, ...] = (
        "rm -rf /", "mkfs", "dd ", "shutdown", "reboot",
        "curl", "wget",  # network access needs explicit approval
    )
    write_scope: str | None = None  # fleet path partition (e.g. "projects/my-project")

    def with_write_scope(self, scope: str) -> CodexConfig:
        """Return a copy with write_scope set (for fleet path partitioning)."""
        from dataclasses import replace
        return replace(self, write_scope=scope)

    @classmethod
    def from_env(cls) -> CodexConfig:
        api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            raise EnvironmentError(
                "OPENAI_API_KEY is required. Set it before running the session."
            )
        return cls(
            api_key=api_key,
            base_url=os.environ.get("OPENAI_BASE_URL", cls.base_url),
            model=os.environ.get("OPENAI_MODEL", cls.model),
            repo_home=Path(
                os.environ.get("OPENAKARI_HOME", str(Path.cwd()))
            ),
            max_turns=int(os.environ.get("CODEX_MAX_TURNS", str(cls.max_turns))),
            temperature=float(
                os.environ.get("CODEX_TEMPERATURE", str(cls.temperature))
            ),
        )

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.api_key:
            errors.append("OPENAI_API_KEY is empty")
        if not self.repo_home.is_dir():
            errors.append(f"OPENAKARI_HOME does not exist: {self.repo_home}")
        return errors
