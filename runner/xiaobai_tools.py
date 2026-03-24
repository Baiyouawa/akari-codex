"""小白专属轻量工具集。

在 chat 模式下通过 OpenAI function calling 调用，
用于回答需要实时信息的问题（天气、搜索、时间、计算等）。
与 runner/tools.py（Agent session 工具）分离，保持各自职责清晰。
"""

from __future__ import annotations

import datetime
import json
import re
import urllib.parse
import urllib.request
from typing import Any

_BJ_TZ = datetime.timezone(datetime.timedelta(hours=8))
_UA = "Mozilla/5.0 (compatible; XiaoBai/1.0)"
_TIMEOUT = 15

# ─── 工具定义（OpenAI function calling schema） ──────────────

XIAOBAI_TOOL_DEFINITIONS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "搜索互联网获取实时信息（天气、新闻、知识等）。使用 DuckDuckGo。",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜索关键词",
                    },
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "web_fetch",
            "description": "抓取指定 URL 的网页内容（返回纯文本摘要）。",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "要抓取的 URL",
                    },
                },
                "required": ["url"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "获取当前时间（北京时间）。",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "计算数学表达式。",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "数学表达式，如 '2**10' 或 'sqrt(144)'",
                    },
                },
                "required": ["expression"],
            },
        },
    },
]

# ─── 工具实现 ────────────────────────────────────────────────


def web_search(query: str) -> str:
    """通过 DuckDuckGo Lite 搜索。"""
    try:
        encoded = urllib.parse.urlencode({"q": query, "kl": "cn-zh"})
        url = f"https://lite.duckduckgo.com/lite/?{encoded}"
        req = urllib.request.Request(url, headers={"User-Agent": _UA})
        with urllib.request.urlopen(req, timeout=_TIMEOUT) as resp:
            html = resp.read().decode("utf-8", errors="replace")

        results = _extract_ddg_results(html)
        if not results:
            return f"搜索「{query}」没有找到结果。"
        return f"搜索「{query}」的结果:\n\n" + "\n".join(results[:5])
    except Exception as e:
        return f"搜索失败: {type(e).__name__}: {e}"


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


def web_fetch(url: str) -> str:
    """抓取 URL 并返回纯文本内容摘要。"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": _UA})
        with urllib.request.urlopen(req, timeout=_TIMEOUT) as resp:
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


def get_current_time() -> str:
    """返回当前北京时间。"""
    now = datetime.datetime.now(_BJ_TZ)
    weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    wd = weekdays[now.weekday()]
    return f"现在是北京时间 {now.strftime('%Y年%m月%d日')} {wd} {now.strftime('%H:%M:%S')}"


def calculate(expression: str) -> str:
    """安全计算数学表达式。"""
    import math
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


# ─── 分发 ────────────────────────────────────────────────────

_TOOL_DISPATCH: dict[str, Any] = {
    "web_search": web_search,
    "web_fetch": web_fetch,
    "get_current_time": get_current_time,
    "calculate": calculate,
}


def execute_tool(name: str, arguments: dict[str, Any]) -> str:
    """执行小白工具，返回结果文本。"""
    handler = _TOOL_DISPATCH.get(name)
    if not handler:
        return f"未知工具: {name}"
    try:
        return handler(**arguments)
    except Exception as e:
        return f"工具执行失败: {type(e).__name__}: {e}"
