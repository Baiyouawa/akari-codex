"""Local tool execution layer for the Codex agent.

Implements the tools the agent can call during a session:
  - read_file       Read a file from the repo
  - write_file      Write/overwrite a file in the repo
  - list_files      List files in a directory
  - search_text     Search for text patterns (ripgrep)
  - run_shell       Execute an allowlisted shell command
  - git_status      Get current git status
  - log_decision    Write a decision record to decisions/
  - request_approval Queue an approval request
  - web_search      Search the internet (DuckDuckGo)
  - web_fetch       Fetch and extract text from a URL
  - get_current_time Return current Beijing time
  - calculate       Evaluate a math expression safely
"""

from __future__ import annotations

import datetime
import json
import math
import os
import re
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from .config import CodexConfig

_BJ_TZ = datetime.timezone(datetime.timedelta(hours=8))
_UA = "Mozilla/5.0 (compatible; XiaoBai/1.0)"
_WEB_TIMEOUT = 15

TOOL_DEFINITIONS: dict[str, dict[str, Any]] = {
    "read_file": {
        "description": "Read the contents of a file at the given path (relative to repo root).",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Relative file path"},
            },
            "required": ["path"],
        },
    },
    "write_file": {
        "description": "Write content to a file (creates or overwrites). Path is relative to repo root.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Relative file path"},
                "content": {"type": "string", "description": "File content to write"},
            },
            "required": ["path", "content"],
        },
    },
    "list_files": {
        "description": "List files and directories at the given path (relative to repo root).",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Relative directory path (default: root)",
                    "default": ".",
                },
                "recursive": {
                    "type": "boolean",
                    "description": "List recursively",
                    "default": False,
                },
            },
        },
    },
    "search_text": {
        "description": "Search for a text pattern in the repo using ripgrep.",
        "parameters": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string", "description": "Search pattern (regex)"},
                "path": {
                    "type": "string",
                    "description": "Directory to search in (default: repo root)",
                    "default": ".",
                },
                "max_results": {
                    "type": "integer",
                    "description": "Maximum results to return",
                    "default": 50,
                },
            },
            "required": ["pattern"],
        },
    },
    "run_shell": {
        "description": "Execute a shell command (subject to allowlist policy).",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "Shell command to execute"},
                "working_dir": {
                    "type": "string",
                    "description": "Working directory (relative to repo root)",
                    "default": ".",
                },
            },
            "required": ["command"],
        },
    },
    "git_status": {
        "description": "Get the current git status of the repository.",
        "parameters": {"type": "object", "properties": {}},
    },
    "log_decision": {
        "description": "Write a decision record (ADR) to the decisions/ directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "Decision title"},
                "context": {"type": "string", "description": "Why this decision was needed"},
                "decision": {"type": "string", "description": "What was decided"},
                "consequences": {"type": "string", "description": "Expected consequences"},
            },
            "required": ["title", "context", "decision"],
        },
    },
    "request_approval": {
        "description": "Queue an approval request in APPROVAL_QUEUE.md. Blocks the current action.",
        "parameters": {
            "type": "object",
            "properties": {
                "action_type": {
                    "type": "string",
                    "description": "Type: resource-decision, governance-change, tool-access, production-pr",
                },
                "description": {"type": "string", "description": "What needs approval and why"},
                "urgency": {
                    "type": "string",
                    "enum": ["blocking", "non-blocking"],
                    "default": "blocking",
                },
            },
            "required": ["action_type", "description"],
        },
    },
    "web_search": {
        "description": "Search the internet via DuckDuckGo. Returns top results with titles and URLs.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search keywords"},
            },
            "required": ["query"],
        },
    },
    "web_fetch": {
        "description": "Fetch a URL and return its text content (HTML tags stripped).",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "URL to fetch"},
            },
            "required": ["url"],
        },
    },
    "get_current_time": {
        "description": "Get the current date and time in Beijing timezone (UTC+8).",
        "parameters": {"type": "object", "properties": {}},
    },
    "calculate": {
        "description": "Safely evaluate a mathematical expression (supports math module functions).",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Math expression, e.g. '2**10', 'sqrt(144)', 'log(100)'",
                },
            },
            "required": ["expression"],
        },
    },
}


class ToolExecutor:
    """Executes tools within the safety boundaries of the Codex config."""

    def __init__(self, config: CodexConfig):
        self.config = config
        self.repo_root = config.repo_home
        self._dispatch = {
            "read_file": self._read_file,
            "write_file": self._write_file,
            "list_files": self._list_files,
            "search_text": self._search_text,
            "run_shell": self._run_shell,
            "git_status": self._git_status,
            "log_decision": self._log_decision,
            "request_approval": self._request_approval,
            "web_search": self._web_search,
            "web_fetch": self._web_fetch,
            "get_current_time": self._get_current_time,
            "calculate": self._calculate,
        }

    def execute(self, tool_name: str, args: dict[str, Any]) -> str:
        handler = self._dispatch.get(tool_name)
        if not handler:
            return json.dumps({"error": f"Unknown tool: {tool_name}"})
        try:
            return handler(**args)
        except Exception as e:
            return json.dumps({"error": f"{type(e).__name__}: {e}"})

    def _resolve_path(self, rel_path: str) -> Path:
        resolved = (self.repo_root / rel_path).resolve()
        if not str(resolved).startswith(str(self.repo_root.resolve())):
            raise PermissionError(f"Path escapes repo root: {rel_path}")
        return resolved

    def _check_write_allowed(self, rel_path: str) -> None:
        """Enforce write_scope partition for fleet workers."""
        scope = self.config.write_scope
        if scope is None:
            return
        normalized = Path(rel_path).as_posix()
        allowed = [scope, "artifacts/", ".fleet/"]
        if not any(normalized.startswith(a) or normalized == a.rstrip("/") for a in allowed):
            raise PermissionError(
                f"Fleet write_scope violation: {rel_path} not under {scope}"
            )

    def _read_file(self, path: str) -> str:
        target = self._resolve_path(path)
        if not target.is_file():
            return json.dumps({"error": f"File not found: {path}"})
        content = target.read_text(encoding="utf-8", errors="replace")
        if len(content) > 100_000:
            content = content[:100_000] + "\n\n... [truncated at 100k chars]"
        return content

    def _write_file(self, path: str, content: str) -> str:
        self._check_write_allowed(path)
        target = self._resolve_path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return json.dumps({"status": "ok", "path": str(path), "bytes": len(content)})

    def _list_files(self, path: str = ".", recursive: bool = False) -> str:
        target = self._resolve_path(path)
        if not target.is_dir():
            return json.dumps({"error": f"Not a directory: {path}"})

        entries = []
        if recursive:
            for p in sorted(target.rglob("*")):
                if ".git" in p.parts:
                    continue
                rel = p.relative_to(self.repo_root)
                entries.append({
                    "path": str(rel),
                    "type": "dir" if p.is_dir() else "file",
                })
                if len(entries) >= 500:
                    break
        else:
            for p in sorted(target.iterdir()):
                if p.name.startswith(".git"):
                    continue
                rel = p.relative_to(self.repo_root)
                entries.append({
                    "path": str(rel),
                    "type": "dir" if p.is_dir() else "file",
                })
        return json.dumps(entries, indent=2)

    def _search_text(
        self, pattern: str, path: str = ".", max_results: int = 50
    ) -> str:
        target = self._resolve_path(path)
        try:
            proc = subprocess.run(
                ["rg", "--json", "-m", str(max_results), pattern, str(target)],
                capture_output=True,
                text=True,
                timeout=30,
                cwd=str(self.repo_root),
            )
        except FileNotFoundError:
            proc = subprocess.run(
                ["grep", "-rn", "--include=*.md", "--include=*.py",
                 "--include=*.ts", "--include=*.js", "--include=*.yaml",
                 pattern, str(target)],
                capture_output=True,
                text=True,
                timeout=30,
                cwd=str(self.repo_root),
            )
        output = proc.stdout
        if len(output) > 50_000:
            output = output[:50_000] + "\n... [truncated]"
        return output or "(no matches)"

    def _run_shell(self, command: str, working_dir: str = ".") -> str:
        cmd_lower = command.strip().lower()

        for denied in self.config.shell_denylist:
            if denied in cmd_lower:
                return json.dumps({
                    "error": f"Command blocked by denylist: {denied}",
                    "action": "request_approval",
                })

        is_allowed = any(
            cmd_lower.startswith(allowed) for allowed in self.config.shell_allowlist
        )
        if not is_allowed:
            return json.dumps({
                "error": f"Command not on allowlist. Use request_approval for: {command}",
                "allowlist": list(self.config.shell_allowlist),
            })

        cwd = self._resolve_path(working_dir)
        try:
            proc = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=60,
                cwd=str(cwd),
                env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
            )
            output = proc.stdout + proc.stderr
            if len(output) > 50_000:
                output = output[:50_000] + "\n... [truncated]"
            return json.dumps({
                "exit_code": proc.returncode,
                "output": output,
            })
        except subprocess.TimeoutExpired:
            return json.dumps({"error": "Command timed out after 60 seconds"})

    def _git_status(self) -> str:
        try:
            proc = subprocess.run(
                ["git", "status", "--porcelain", "--branch"],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=str(self.repo_root),
            )
            return proc.stdout or "(clean working tree)"
        except Exception as e:
            return json.dumps({"error": str(e)})

    def _log_decision(
        self,
        title: str,
        context: str,
        decision: str,
        consequences: str = "",
    ) -> str:
        decisions_dir = self.repo_root / "decisions"
        decisions_dir.mkdir(exist_ok=True)

        existing = list(decisions_dir.glob("*.md"))
        numbers = []
        for f in existing:
            try:
                numbers.append(int(f.stem.split("-")[0]))
            except (ValueError, IndexError):
                pass
        next_num = max(numbers, default=0) + 1

        slug = title.lower().replace(" ", "-")[:50]
        filename = f"{next_num:04d}-{slug}.md"
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()

        content = f"""# ADR {next_num:04d}: {title}

**Date:** {now}
**Status:** Accepted

## Context

{context}

## Decision

{decision}

## Consequences

{consequences or "To be observed."}
"""
        self._check_write_allowed(f"decisions/{filename}")
        target = decisions_dir / filename
        target.write_text(content, encoding="utf-8")
        return json.dumps({"status": "ok", "path": f"decisions/{filename}"})

    def _request_approval(
        self,
        action_type: str,
        description: str,
        urgency: str = "blocking",
    ) -> str:
        queue_file = self.repo_root / "APPROVAL_QUEUE.md"
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()

        entry = f"""
---

### [{urgency.upper()}] {action_type}

**Requested:** {now}
**Description:** {description}
**Status:** pending

"""
        if queue_file.is_file():
            existing = queue_file.read_text(encoding="utf-8")
        else:
            existing = "# Approval Queue\n\nItems requiring human review.\n"

        queue_file.write_text(existing + entry, encoding="utf-8")
        return json.dumps({
            "status": "queued",
            "type": action_type,
            "urgency": urgency,
            "message": "Action blocked pending approval" if urgency == "blocking" else "Queued for review",
        })

    # ── Web / utility tools ──────────────────────────────────

    def _web_search(self, query: str) -> str:
        try:
            encoded = urllib.parse.urlencode({"q": query, "kl": "cn-zh"})
            url = f"https://lite.duckduckgo.com/lite/?{encoded}"
            req = urllib.request.Request(url, headers={"User-Agent": _UA})
            with urllib.request.urlopen(req, timeout=_WEB_TIMEOUT) as resp:
                html = resp.read().decode("utf-8", errors="replace")

            results = _extract_ddg_results(html)
            if not results:
                return f"搜索「{query}」没有找到结果。"
            return f"搜索「{query}」的结果:\n\n" + "\n".join(results[:5])
        except Exception as e:
            return f"搜索失败: {type(e).__name__}: {e}"

    def _web_fetch(self, url: str) -> str:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": _UA})
            with urllib.request.urlopen(req, timeout=_WEB_TIMEOUT) as resp:
                ctype = resp.headers.get("Content-Type", "")
                if "text" not in ctype and "json" not in ctype:
                    return f"URL 返回的不是文本内容 (Content-Type: {ctype})"
                raw = resp.read()
                encoding = "utf-8"
                m = re.search(r"charset=([^\s;]+)", ctype)
                if m:
                    encoding = m.group(1)
                text = raw.decode(encoding, errors="replace")

            text = re.sub(r"<script[^>]*>.*?</script>", "", text, flags=re.DOTALL)
            text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL)
            text = re.sub(r"<[^>]+>", " ", text)
            text = re.sub(r"\s+", " ", text).strip()

            if len(text) > 3000:
                text = text[:3000] + "... (已截断)"
            return text or "(页面内容为空)"
        except Exception as e:
            return f"抓取失败: {type(e).__name__}: {e}"

    def _get_current_time(self) -> str:
        now = datetime.datetime.now(_BJ_TZ)
        weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        wd = weekdays[now.weekday()]
        return f"现在是北京时间 {now.strftime('%Y年%m月%d日')} {wd} {now.strftime('%H:%M:%S')}"

    def _calculate(self, expression: str) -> str:
        allowed_names = {
            k: v for k, v in math.__dict__.items()
            if not k.startswith("_")
        }
        allowed_names.update({"abs": abs, "round": round, "min": min, "max": max})
        try:
            result = eval(expression, {"__builtins__": {}}, allowed_names)  # noqa: S307
            return f"{expression} = {result}"
        except Exception as e:
            return f"计算错误: {e}"


def _extract_ddg_results(html: str) -> list[str]:
    """从 DuckDuckGo Lite HTML 中提取搜索结果。"""
    results: list[str] = []

    links = re.findall(
        r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',
        html, re.DOTALL,
    )
    for href, title in links:
        clean_title = re.sub(r"<[^>]+>", "", title).strip()
        if not clean_title:
            continue
        if "duckduckgo.com/l/" in href:
            m = re.search(r"uddg=([^&]+)", href)
            real_url = urllib.parse.unquote(m.group(1)) if m else href
            results.append(f"- {clean_title}\n  {real_url}")
        elif href.startswith("http") and "duckduckgo" not in href:
            results.append(f"- {clean_title}\n  {href}")
        if len(results) >= 8:
            break

    if not results:
        text_blocks = re.findall(r"<td[^>]*>(.*?)</td>", html, re.DOTALL)
        for block in text_blocks:
            clean = re.sub(r"<[^>]+>", "", block).strip()
            if len(clean) > 30:
                results.append(f"- {clean[:200]}")
                if len(results) >= 5:
                    break

    return results
