"""Codex backend: OpenAI Responses API client with iterative tool-call loop.

This module implements the core agent loop:
  1. Assemble prompt bundle (system + developer + user context)
  2. Call the OpenAI Responses API
  3. Inspect response for tool calls
  4. Execute approved tools locally
  5. Feed tool results back for the next round
  6. Repeat until the model produces a final text response or max turns exhausted
  7. Record token usage and latency
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Protocol

from openai import OpenAI

from .config import CodexConfig


class ProgressCallback(Protocol):
    """Callback invoked after each turn of the tool-call loop."""

    def __call__(
        self,
        turn: int,
        max_turns: int,
        phase: str,
        tool_name: str | None = None,
        tool_args_preview: str | None = None,
    ) -> None: ...


@dataclass
class TokenUsage:
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0

    def accumulate(self, usage: dict[str, int]) -> None:
        self.prompt_tokens += usage.get("prompt_tokens", 0)
        self.completion_tokens += usage.get("completion_tokens", 0)
        self.total_tokens += usage.get("total_tokens", 0)


@dataclass
class SessionResult:
    task_id: str
    model: str
    turns: int = 0
    final_output: str = ""
    tool_calls_log: list[dict[str, Any]] = field(default_factory=list)
    token_usage: TokenUsage = field(default_factory=TokenUsage)
    latency_seconds: float = 0.0
    success: bool = False
    error: str | None = None


def _load_prompt_file(path: Path) -> str:
    if path.is_file():
        return path.read_text(encoding="utf-8").strip()
    return ""


def _build_tool_definitions(tools_registry: dict[str, Any]) -> list[dict]:
    """Convert the tools registry into OpenAI function-calling format."""
    definitions = []
    for name, spec in tools_registry.items():
        definitions.append({
            "type": "function",
            "function": {
                "name": name,
                "description": spec.get("description", ""),
                "parameters": spec.get("parameters", {"type": "object", "properties": {}}),
            },
        })
    return definitions


class CodexBackend:
    """OpenAI Responses API backend with tool-call loop."""

    def __init__(self, config: CodexConfig, tool_executor: Any = None):
        self.config = config
        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
            timeout=config.timeout_seconds,
        )
        self.tool_executor = tool_executor

    def _assemble_messages(
        self,
        task_context: str,
        repo_state: str,
        additional_context: str = "",
    ) -> list[dict[str, str]]:
        system_prompt = _load_prompt_file(
            self.config.repo_home / "prompts" / "system.md"
        )
        developer_prompt = _load_prompt_file(
            self.config.repo_home / "prompts" / "developer.md"
        )

        messages: list[dict[str, str]] = []

        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        if developer_prompt:
            messages.append({"role": "developer", "content": developer_prompt})

        user_content_parts = []
        if repo_state:
            user_content_parts.append(f"## Current repo state\n\n{repo_state}")
        if additional_context:
            user_content_parts.append(f"## Additional context\n\n{additional_context}")
        user_content_parts.append(f"## Task\n\n{task_context}")

        messages.append({"role": "user", "content": "\n\n".join(user_content_parts)})
        return messages

    def _stream_completion(self, **kwargs: Any) -> dict[str, Any]:
        """Call the API with stream=True and reassemble into a complete message.

        Returns a dict with keys: content, tool_calls, usage.
        """
        kwargs["stream"] = True
        kwargs["stream_options"] = {"include_usage": True}

        content_parts: list[str] = []
        tool_calls_by_index: dict[int, dict] = {}
        usage_data: dict[str, int] = {}

        stream = self.client.chat.completions.create(**kwargs)
        for chunk in stream:
            if chunk.usage:
                usage_data = {
                    "prompt_tokens": chunk.usage.prompt_tokens or 0,
                    "completion_tokens": chunk.usage.completion_tokens or 0,
                    "total_tokens": chunk.usage.total_tokens or 0,
                }

            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta

            if delta.content:
                content_parts.append(delta.content)

            if delta.tool_calls:
                for tc_delta in delta.tool_calls:
                    idx = tc_delta.index
                    if idx not in tool_calls_by_index:
                        tool_calls_by_index[idx] = {
                            "id": tc_delta.id or "",
                            "type": "function",
                            "function": {"name": "", "arguments": ""},
                        }
                    entry = tool_calls_by_index[idx]
                    if tc_delta.id:
                        entry["id"] = tc_delta.id
                    if tc_delta.function:
                        if tc_delta.function.name:
                            entry["function"]["name"] += tc_delta.function.name
                        if tc_delta.function.arguments:
                            entry["function"]["arguments"] += tc_delta.function.arguments

        tool_calls_list = [
            tool_calls_by_index[i]
            for i in sorted(tool_calls_by_index)
        ] if tool_calls_by_index else []

        return {
            "content": "".join(content_parts),
            "tool_calls": tool_calls_list,
            "usage": usage_data,
        }

    def run_session(
        self,
        task_id: str,
        task_context: str,
        repo_state: str = "",
        additional_context: str = "",
        tools_registry: dict[str, Any] | None = None,
        progress_callback: ProgressCallback | None = None,
    ) -> SessionResult:
        """Execute a complete agent session with streaming tool-call loop.

        All API calls use stream=True (required by the gateway).
        Streaming chunks are reassembled into complete messages before
        tool dispatch.
        """
        result = SessionResult(task_id=task_id, model=self.config.model)
        start_time = time.time()

        messages = self._assemble_messages(task_context, repo_state, additional_context)

        tool_defs = (
            _build_tool_definitions(tools_registry) if tools_registry else None
        )

        def _notify(turn: int, phase: str, tool_name: str | None = None,
                     tool_args_preview: str | None = None) -> None:
            if progress_callback:
                progress_callback(
                    turn=turn,
                    max_turns=self.config.max_turns,
                    phase=phase,
                    tool_name=tool_name,
                    tool_args_preview=tool_args_preview,
                )

        try:
            for turn in range(self.config.max_turns):
                result.turns = turn + 1

                _notify(turn + 1, "llm_thinking")

                kwargs: dict[str, Any] = {
                    "model": self.config.model,
                    "messages": messages,
                    "temperature": self.config.temperature,
                    "max_tokens": self.config.max_tokens_per_turn,
                }
                if tool_defs:
                    kwargs["tools"] = tool_defs
                    kwargs["tool_choice"] = "auto"

                assembled = self._stream_completion(**kwargs)

                if assembled["usage"]:
                    result.token_usage.accumulate(assembled["usage"])

                if assembled["tool_calls"] and self.tool_executor:
                    messages.append({
                        "role": "assistant",
                        "content": assembled["content"],
                        "tool_calls": assembled["tool_calls"],
                    })

                    for tc in assembled["tool_calls"]:
                        tool_name = tc["function"]["name"]
                        try:
                            tool_args = json.loads(tc["function"]["arguments"])
                        except json.JSONDecodeError:
                            tool_args = {}

                        args_preview = json.dumps(tool_args, ensure_ascii=False)
                        if len(args_preview) > 80:
                            args_preview = args_preview[:77] + "..."
                        _notify(turn + 1, "tool_exec", tool_name, args_preview)

                        tool_result = self.tool_executor.execute(
                            tool_name, tool_args
                        )

                        result.tool_calls_log.append({
                            "turn": turn + 1,
                            "tool": tool_name,
                            "args": tool_args,
                            "result_preview": str(tool_result)[:500],
                        })

                        messages.append({
                            "role": "tool",
                            "tool_call_id": tc["id"],
                            "content": str(tool_result),
                        })

                    continue

                _notify(turn + 1, "finalizing")
                result.final_output = assembled["content"]
                result.success = True
                break
            else:
                result.error = f"Max turns ({self.config.max_turns}) exhausted"

        except Exception as e:
            result.error = f"{type(e).__name__}: {e}"

        result.latency_seconds = time.time() - start_time
        return result
