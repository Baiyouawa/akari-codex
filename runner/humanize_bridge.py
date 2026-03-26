"""Humanize bridge: integrates RLCR, Ask-Codex, and PR-Loop into the runner.

Provides Python wrappers around the Humanize shell scripts so that
AgentLoop, Fleet executor, and the scheduler can trigger Codex-powered
code review without shelling out manually.
"""

from __future__ import annotations

import logging
import os
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

logger = logging.getLogger("runner.humanize")

_HUMANIZE_ROOT = Path(
    os.environ.get(
        "HUMANIZE_ROOT",
        os.path.expanduser("~/.cursor/skills/humanize"),
    )
)

_SCRIPTS = _HUMANIZE_ROOT / "scripts"


def _humanize_available() -> bool:
    return (_SCRIPTS / "ask-codex.sh").is_file()


def _run_script(
    script_name: str,
    args: list[str],
    *,
    timeout: int = 3600,
    cwd: str | Path | None = None,
) -> subprocess.CompletedProcess[str]:
    cmd = [str(_SCRIPTS / script_name)] + args
    env = {**os.environ, "PATH": os.environ.get("PATH", "")}
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=str(cwd) if cwd else None,
        env=env,
    )


# ── Ask-Codex: one-shot consultation ──────────────────────────────


@dataclass
class AskCodexResult:
    output: str
    exit_code: int
    duration_seconds: float
    timed_out: bool = False


def ask_codex(
    question: str,
    *,
    model: str = "gpt-5.4",
    effort: str = "medium",
    timeout: int = 600,
    cwd: str | Path | None = None,
) -> AskCodexResult:
    """Send a one-shot question to Codex and return the response."""
    if not _humanize_available():
        return AskCodexResult(
            output="Humanize not installed", exit_code=1, duration_seconds=0
        )

    args = ["--codex-model", f"{model}:{effort}", "--codex-timeout", str(timeout)]
    args.append(question)

    start = time.time()
    try:
        proc = _run_script("ask-codex.sh", args, timeout=timeout + 60, cwd=cwd)
        return AskCodexResult(
            output=proc.stdout,
            exit_code=proc.returncode,
            duration_seconds=time.time() - start,
        )
    except subprocess.TimeoutExpired:
        return AskCodexResult(
            output="Codex timed out",
            exit_code=124,
            duration_seconds=time.time() - start,
            timed_out=True,
        )


# ── Code Review: diff-based review against a base branch ─────────


@dataclass
class CodeReviewResult:
    issues: list[dict[str, str]]
    raw_output: str
    exit_code: int
    duration_seconds: float
    has_critical: bool = False


def review_code_diff(
    base_branch: str = "main",
    *,
    model: str = "gpt-5.4",
    effort: str = "high",
    timeout: int = 1800,
    cwd: str | Path | None = None,
) -> CodeReviewResult:
    """Run `codex review --base <branch>` and parse [P0-9] issues."""
    start = time.time()
    try:
        proc = subprocess.run(
            ["codex", "review", "--base", base_branch,
             "-m", model, "-c", f"model_reasoning_effort={effort}"],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(cwd) if cwd else None,
        )
    except FileNotFoundError:
        return CodeReviewResult(
            issues=[], raw_output="codex CLI not found",
            exit_code=1, duration_seconds=time.time() - start,
        )
    except subprocess.TimeoutExpired:
        return CodeReviewResult(
            issues=[], raw_output="codex review timed out",
            exit_code=124, duration_seconds=time.time() - start,
        )

    issues = _parse_review_issues(proc.stdout)
    has_critical = any(i["severity"] in ("P0", "P1") for i in issues)

    return CodeReviewResult(
        issues=issues,
        raw_output=proc.stdout,
        exit_code=proc.returncode,
        duration_seconds=time.time() - start,
        has_critical=has_critical,
    )


def _parse_review_issues(output: str) -> list[dict[str, str]]:
    import re
    issues: list[dict[str, str]] = []
    for match in re.finditer(
        r"-\s*\[(P\d)\]\s*(.+?)(?:\s*-\s*(\S+:\d[\d-]*))?$",
        output,
        re.MULTILINE,
    ):
        issues.append({
            "severity": match.group(1),
            "description": match.group(2).strip(),
            "location": match.group(3) or "",
        })
    return issues


# ── RLCR Loop: setup and gate ────────────────────────────────────


@dataclass
class RLCRSetupResult:
    success: bool
    loop_dir: str
    output: str
    exit_code: int


def setup_rlcr_loop(
    plan_file: str,
    *,
    max_iterations: int = 10,
    codex_model: str = "gpt-5.4:xhigh",
    codex_timeout: int = 3600,
    base_branch: str = "",
    skip_impl: bool = False,
    agent_teams: bool = False,
    cwd: str | Path | None = None,
) -> RLCRSetupResult:
    """Start an RLCR loop by running the setup script."""
    if not _humanize_available():
        return RLCRSetupResult(
            success=False, loop_dir="",
            output="Humanize not installed", exit_code=1,
        )

    args: list[str] = []
    if skip_impl:
        args.append("--skip-impl")
    if plan_file and not skip_impl:
        args.append(plan_file)
    args.extend(["--max", str(max_iterations)])
    args.extend(["--codex-model", codex_model])
    args.extend(["--codex-timeout", str(codex_timeout)])
    if base_branch:
        args.extend(["--base-branch", base_branch])
    if agent_teams:
        args.append("--agent-teams")

    proc = _run_script("setup-rlcr-loop.sh", args, cwd=cwd)

    loop_dir = ""
    for line in proc.stdout.splitlines():
        if "Loop Directory:" in line:
            loop_dir = line.split(":", 1)[1].strip()
            break

    return RLCRSetupResult(
        success=proc.returncode == 0,
        loop_dir=loop_dir,
        output=proc.stdout,
        exit_code=proc.returncode,
    )


def rlcr_stop_gate(*, cwd: str | Path | None = None) -> int:
    """Run the RLCR stop gate. Returns exit code: 0=done, 10=continue, 20=error."""
    if not _humanize_available():
        return 20
    proc = _run_script("rlcr-stop-gate.sh", [], cwd=cwd)
    return proc.returncode


# ── Fleet post-task review ────────────────────────────────────────


@dataclass
class PostTaskReviewResult:
    reviewed: bool
    issues_found: int
    has_critical: bool
    summary: str
    duration_seconds: float


_REVIEW_SYSTEM_PROMPT = """\
你是一位严格的代码审查专家。对给定的文件变更进行审查，找出以下问题：
- [P0] 致命: 数据丢失、安全漏洞、死循环、未处理的异常导致崩溃
- [P1] 严重: 逻辑错误、并发竞态、资源泄漏、违反核心约定
- [P2] 中等: 性能问题、错误处理不完整、命名混乱
- [P3] 轻微: 风格问题、冗余代码、文档不足

输出格式（每个问题一行）:
- [P级别] 问题描述 - 文件:行号

最后用一行总结: VERDICT: PASS 或 VERDICT: FAIL (存在 P0 或 P1 时 FAIL)
如果没有发现问题，输出: VERDICT: PASS — 无问题"""


def _review_via_api(
    written_files: list[str],
    repo_root: Path,
    task_text: str = "",
    *,
    model: str = "",
    timeout: int = 120,
) -> PostTaskReviewResult:
    """Review deliverables using the project's own OpenAI API — no external tools needed."""
    start = time.time()

    try:
        from runner.config import CodexConfig
        cfg = CodexConfig.from_env()
    except Exception:
        return PostTaskReviewResult(
            reviewed=False, issues_found=0, has_critical=False,
            summary="CodexConfig unavailable, review skipped",
            duration_seconds=time.time() - start,
        )

    file_contents: list[str] = []
    for fpath in written_files[:10]:
        full = repo_root / fpath if not Path(fpath).is_absolute() else Path(fpath)
        if not full.is_file():
            continue
        try:
            text = full.read_text(encoding="utf-8", errors="replace")
            if len(text) > 8000:
                text = text[:4000] + "\n... (truncated) ...\n" + text[-2000:]
            file_contents.append(f"=== {fpath} ===\n{text}")
        except Exception:
            continue

    if not file_contents:
        return PostTaskReviewResult(
            reviewed=False, issues_found=0, has_critical=False,
            summary="No readable files to review",
            duration_seconds=time.time() - start,
        )

    user_msg = f"任务: {task_text}\n\n以下是本次变更的文件:\n\n" + "\n\n".join(file_contents)

    try:
        from openai import OpenAI
        client = OpenAI(
            api_key=cfg.api_key,
            base_url=cfg.base_url,
            timeout=timeout,
        )
        resp = client.chat.completions.create(
            model=model or cfg.model,
            messages=[
                {"role": "system", "content": _REVIEW_SYSTEM_PROMPT},
                {"role": "user", "content": user_msg[:30000]},
            ],
            temperature=0.2,
            max_tokens=2048,
        )
        output = resp.choices[0].message.content or ""
    except Exception as e:
        return PostTaskReviewResult(
            reviewed=False, issues_found=0, has_critical=False,
            summary=f"API review failed: {e}",
            duration_seconds=time.time() - start,
        )

    issues = _parse_review_issues(output)
    has_critical = any(i["severity"] in ("P0", "P1") for i in issues)
    verdict_fail = "VERDICT: FAIL" in output.upper()

    return PostTaskReviewResult(
        reviewed=True,
        issues_found=len(issues),
        has_critical=has_critical or verdict_fail,
        summary=output[:2000],
        duration_seconds=time.time() - start,
    )


def fleet_post_task_review(
    repo_root: Path,
    base_branch: str = "main",
    written_files: list[str] | None = None,
    task_text: str = "",
    *,
    model: str = "gpt-5.4",
    effort: str = "medium",
    timeout: int = 600,
) -> PostTaskReviewResult:
    """Review after a Fleet worker completes ANY task (code or docs).

    Strategy:
      1. Try external `codex review` if Humanize CLI is available
      2. Otherwise fall back to direct API review (always available)
    """
    if not written_files:
        return PostTaskReviewResult(
            reviewed=False, issues_found=0, has_critical=False,
            summary="No files written, skipping review",
            duration_seconds=0,
        )

    if _humanize_available():
        try:
            result = review_code_diff(
                base_branch, model=model, effort=effort,
                timeout=timeout, cwd=repo_root,
            )
            if result.exit_code == 0 and result.raw_output.strip():
                return PostTaskReviewResult(
                    reviewed=True,
                    issues_found=len(result.issues),
                    has_critical=result.has_critical,
                    summary=result.raw_output[:2000],
                    duration_seconds=result.duration_seconds,
                )
        except Exception:
            pass

    return _review_via_api(
        written_files, repo_root, task_text,
        model=model, timeout=min(timeout, 120),
    )


# ── Status and availability ───────────────────────────────────────


def is_humanize_available() -> bool:
    return _humanize_available()


def get_humanize_root() -> Path:
    return _HUMANIZE_ROOT
