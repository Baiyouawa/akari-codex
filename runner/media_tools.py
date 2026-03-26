"""多媒体工具层 — 图片/语音/文件/表情包的生成、下载、转换。

为小白提供 QQ 多媒体交互能力：
  - TTS 语音合成（edge-tts）
  - 图片识别（Vision LLM）
  - 语音识别（Whisper / 在线 STT）
  - 文件操作（全系统只读 + 删除审批）
  - 表情包发送
  - 媒体缓存自动清理（TTL + 容量上限 + 白名单保护）
"""

from __future__ import annotations

import asyncio
import base64
import json
import logging
import mimetypes
import os
import re
import time
import urllib.request
from pathlib import Path
from typing import Any

_UA = "Mozilla/5.0 (compatible; XiaoBai/1.0)"
_DOWNLOAD_TIMEOUT = 30

_MEDIA_CACHE_DIR: Path | None = None
_LAST_CLEANUP_TS: float = 0.0

CACHE_TTL_SECONDS = int(os.environ.get("MEDIA_CACHE_TTL", 3600))
CACHE_MAX_SIZE_MB = int(os.environ.get("MEDIA_CACHE_MAX_MB", 500))
CACHE_CLEANUP_INTERVAL = 300  # 两次清理之间最少间隔 5 分钟

_log = logging.getLogger(__name__)


def _get_cache_dir() -> Path:
    """获取/创建多媒体缓存目录。"""
    global _MEDIA_CACHE_DIR
    if _MEDIA_CACHE_DIR is None:
        repo = Path(os.environ.get("OPENAKARI_HOME", "."))
        _MEDIA_CACHE_DIR = repo / "logs" / "media_cache"
        _MEDIA_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    return _MEDIA_CACHE_DIR


# ─── 缓存清理机制 ─────────────────────────────────────────────

def _pinned_file() -> Path:
    """长期存储白名单文件路径。"""
    return _get_cache_dir() / "_pinned.json"


def _load_pinned() -> set[str]:
    """读取被主人标记为"长期保留"的文件名集合。"""
    pf = _pinned_file()
    if not pf.is_file():
        return set()
    try:
        data = json.loads(pf.read_text(encoding="utf-8"))
        return set(data) if isinstance(data, list) else set()
    except Exception:
        return set()


def _save_pinned(pinned: set[str]) -> None:
    pf = _pinned_file()
    pf.write_text(json.dumps(sorted(pinned), ensure_ascii=False, indent=2), encoding="utf-8")


def pin_media_file(filename: str) -> str:
    """将文件标记为长期保留，不会被自动清理。

    由主人通过指令触发，例如"保存这张图片"。
    """
    cache = _get_cache_dir()
    target = cache / filename
    if not target.is_file():
        return f"文件不存在: {filename}"
    pinned = _load_pinned()
    pinned.add(filename)
    _save_pinned(pinned)
    return f"已标记为长期保留: {filename}"


def unpin_media_file(filename: str) -> str:
    """取消文件的长期保留标记。"""
    pinned = _load_pinned()
    pinned.discard(filename)
    _save_pinned(pinned)
    return f"已取消长期保留: {filename}"


def list_pinned_files() -> list[str]:
    """列出所有被标记为长期保留的文件。"""
    return sorted(_load_pinned())


def cleanup_media_cache(force: bool = False) -> dict[str, Any]:
    """清理过期或超出容量限制的缓存文件。

    清理策略：
    1. 删除超过 TTL（默认1小时）的非白名单文件
    2. 若总大小仍超过上限（默认500MB），从最旧开始删除直到低于阈值

    Args:
        force: 为 True 时忽略清理间隔限制，立即执行

    Returns:
        清理统计信息字典
    """
    global _LAST_CLEANUP_TS
    now = time.time()

    if not force and (now - _LAST_CLEANUP_TS) < CACHE_CLEANUP_INTERVAL:
        return {"skipped": True, "reason": "cleanup interval not reached"}

    _LAST_CLEANUP_TS = now
    cache = _get_cache_dir()
    pinned = _load_pinned()
    protected = {"_pinned.json"}

    deleted_count = 0
    deleted_bytes = 0
    kept_count = 0

    cache_files: list[tuple[Path, float, int]] = []
    for f in cache.iterdir():
        if not f.is_file() or f.name in protected:
            continue
        try:
            stat = f.stat()
            cache_files.append((f, stat.st_mtime, stat.st_size))
        except OSError:
            continue

    # 第一轮：TTL 过期清理
    for fpath, mtime, size in cache_files:
        if fpath.name in pinned:
            kept_count += 1
            continue
        age = now - mtime
        if age > CACHE_TTL_SECONDS:
            try:
                fpath.unlink()
                deleted_count += 1
                deleted_bytes += size
                _log.debug("cache cleanup: deleted %s (age=%.0fs)", fpath.name, age)
            except OSError as e:
                _log.warning("cache cleanup: failed to delete %s: %s", fpath.name, e)

    # 第二轮：容量上限清理（从最旧到最新）
    max_bytes = CACHE_MAX_SIZE_MB * 1024 * 1024
    remaining: list[tuple[Path, float, int]] = []
    for fpath, mtime, size in cache_files:
        if fpath.is_file():
            remaining.append((fpath, mtime, size))

    total_size = sum(s for _, _, s in remaining)
    if total_size > max_bytes:
        remaining.sort(key=lambda x: x[1])  # oldest first
        for fpath, mtime, size in remaining:
            if total_size <= max_bytes:
                break
            if fpath.name in pinned or fpath.name in protected:
                continue
            try:
                fpath.unlink()
                total_size -= size
                deleted_count += 1
                deleted_bytes += size
                _log.debug("cache cleanup (size): deleted %s", fpath.name)
            except OSError:
                pass

    result = {
        "deleted_count": deleted_count,
        "deleted_bytes": deleted_bytes,
        "deleted_mb": round(deleted_bytes / 1024 / 1024, 2),
        "pinned_count": kept_count,
    }
    if deleted_count > 0:
        _log.info("media cache cleanup: %s", result)
    return result


def _maybe_cleanup() -> None:
    """每次缓存操作后调用，按间隔自动触发清理。"""
    try:
        cleanup_media_cache(force=False)
    except Exception as e:
        _log.warning("auto cache cleanup failed: %s", e)


def get_cache_stats() -> dict[str, Any]:
    """获取缓存目录统计信息。"""
    cache = _get_cache_dir()
    pinned = _load_pinned()
    total_size = 0
    file_count = 0
    for f in cache.iterdir():
        if f.is_file() and f.name != "_pinned.json":
            total_size += f.stat().st_size
            file_count += 1
    return {
        "directory": str(cache),
        "file_count": file_count,
        "total_size_mb": round(total_size / 1024 / 1024, 2),
        "pinned_count": len(pinned),
        "ttl_seconds": CACHE_TTL_SECONDS,
        "max_size_mb": CACHE_MAX_SIZE_MB,
    }


def download_file(url: str, suffix: str = "", headers: dict[str, str] | None = None) -> Path:
    """下载 URL 到本地临时文件，返回路径。

    自动处理 QQ multimedia URL（添加必要的请求头）。
    下载完成后自动触发过期缓存清理。
    """
    import html as _html
    clean_url = _html.unescape(url)

    req_headers = {"User-Agent": _UA}
    if "multimedia.nt.qq.com" in clean_url or "gchat.qpic.cn" in clean_url:
        req_headers["Referer"] = "https://qq.com"
    if headers:
        req_headers.update(headers)

    req = urllib.request.Request(clean_url, headers=req_headers)
    with urllib.request.urlopen(req, timeout=_DOWNLOAD_TIMEOUT) as resp:
        data = resp.read()

    if not suffix:
        ctype = resp.headers.get("Content-Type", "")
        ext = mimetypes.guess_extension(ctype.split(";")[0].strip()) or ""
        suffix = ext or ".bin"

    cache = _get_cache_dir()
    fname = f"{int(time.time() * 1000)}{suffix}"
    path = cache / fname
    path.write_bytes(data)
    _maybe_cleanup()
    return path


def file_to_base64(path: Path | str) -> str:
    """读取文件并返回 base64 编码字符串。"""
    p = Path(path)
    data = p.read_bytes()
    return base64.b64encode(data).decode("ascii")


def _detect_image_mime(path: Path | str) -> str:
    """基于文件头魔数检测图片 MIME 类型（不依赖扩展名）。"""
    p = Path(path)
    try:
        header = p.read_bytes()[:12]
    except Exception:
        return "image/png"

    if header[:4] == b"\x89PNG":
        return "image/png"
    if header[:2] == b"\xff\xd8":
        return "image/jpeg"
    if header[:4] == b"RIFF" and header[8:12] == b"WEBP":
        return "image/webp"
    if header[:4] == b"GIF8":
        return "image/gif"
    if header[:4] == b"\x00\x00\x01\x00":
        return "image/x-icon"

    guessed = mimetypes.guess_type(str(p))[0]
    return guessed or "image/png"


# ─── TTS 语音合成（edge-tts）─────────────────────────────────

_DEFAULT_VOICE = "zh-CN-XiaoxiaoNeural"

_VOICE_MAP = {
    "女声": "zh-CN-XiaoxiaoNeural",
    "男声": "zh-CN-YunxiNeural",
    "温柔": "zh-CN-XiaoyiNeural",
    "播音": "zh-CN-YunyangNeural",
    "活泼": "zh-CN-XiaoxiaoNeural",
    "default": "zh-CN-XiaoxiaoNeural",
}


async def _tts_async(text: str, voice: str, output_path: Path) -> None:
    """异步调用 edge-tts 生成语音文件。"""
    try:
        import edge_tts
    except ImportError:
        raise RuntimeError("edge-tts 未安装，请运行: pip install edge-tts")

    communicate = edge_tts.Communicate(
        text=text, voice=voice,
        connect_timeout=30, receive_timeout=60,
    )
    await communicate.save(str(output_path))


_TTS_MAX_RETRIES = 3


def tts_generate(text: str, voice: str = "", rate: str = "") -> Path:
    """文字转语音，返回 mp3 文件路径。

    Args:
        text: 要合成的文字
        voice: 语音名称/别名（如"女声"、"男声"、或完整 voice ID）
        rate: 语速调整（如 "-20%"、"+10%"）
    """
    resolved_voice = _VOICE_MAP.get(voice, voice) if voice else _DEFAULT_VOICE
    if not resolved_voice.endswith("Neural"):
        resolved_voice = _DEFAULT_VOICE

    cache = _get_cache_dir()
    output = cache / f"tts_{int(time.time() * 1000)}.mp3"

    last_err: Exception | None = None
    for attempt in range(1, _TTS_MAX_RETRIES + 1):
        try:
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
                fut = pool.submit(asyncio.run, _tts_async(text, resolved_voice, output))
                fut.result(timeout=60)
            break
        except Exception as e:
            last_err = e
            if attempt < _TTS_MAX_RETRIES:
                _log.warning("TTS 第 %d 次失败 (%s)，重试...", attempt, e)
                time.sleep(1)
    else:
        raise RuntimeError(f"TTS 合成失败（{_TTS_MAX_RETRIES}次重试后）: {last_err}")

    if not output.is_file() or output.stat().st_size == 0:
        raise RuntimeError(f"TTS 合成失败: 输出文件为空 {output}")
    _maybe_cleanup()
    return output


# ─── 图片识别（Vision LLM）───────────────────────────────────

def recognize_image(
    image_path_or_url: str,
    prompt: str = "用一两句话简短描述这张图片的主要内容",
    api_key: str = "",
    base_url: str = "",
    model: str = "",
) -> str:
    """使用 Vision LLM 识别图片内容。

    支持本地文件路径或 URL。对于远程 URL，先下载再转 base64，
    避免 API 无法直接访问 QQ 图片服务器的问题。
    """
    import html as _html

    if not api_key:
        api_key = os.environ.get("OPENAI_API_KEY", "")
    if not base_url:
        base_url = os.environ.get("OPENAI_BASE_URL", "https://code.vangularcode.asia/v1")
    if not model:
        model = os.environ.get("OPENAI_MODEL", "gpt-5.4")

    if image_path_or_url.startswith(("http://", "https://")):
        clean_url = _html.unescape(image_path_or_url)
        try:
            local_path = download_file(clean_url)
            b64 = file_to_base64(local_path)
            mime = _detect_image_mime(local_path)
            image_url = f"data:{mime};base64,{b64}"
        except Exception as e:
            return f"图片下载失败: {type(e).__name__}: {e}"
    else:
        p = Path(image_path_or_url)
        if not p.is_file():
            return f"图片文件不存在: {image_path_or_url}"
        b64 = file_to_base64(p)
        mime = _detect_image_mime(p)
        image_url = f"data:{mime};base64,{b64}"

    from openai import OpenAI
    client = OpenAI(api_key=api_key, base_url=base_url)

    try:
        stream = client.chat.completions.create(
            model=model,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            }],
            max_tokens=1024,
            stream=True,
        )
        parts: list[str] = []
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                parts.append(chunk.choices[0].delta.content)
        return "".join(parts) or "(无识别结果)"
    except Exception as e:
        return f"图片识别失败: {type(e).__name__}: {e}"


# ─── 语音识别（STT）──────────────────────────────────────────

def recognize_speech(
    audio_path: str,
    api_key: str = "",
    base_url: str = "",
) -> str:
    """语音转文字。

    优先使用独立的 WHISPER_API_KEY / WHISPER_BASE_URL 配置，
    回退到通用 OPENAI_API_KEY / OPENAI_BASE_URL。
    """
    if not api_key:
        api_key = (
            os.environ.get("WHISPER_API_KEY")
            or os.environ.get("OPENAI_API_KEY", "")
        )
    if not base_url:
        base_url = (
            os.environ.get("WHISPER_BASE_URL")
            or os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
        )
    whisper_model = os.environ.get("WHISPER_MODEL", "whisper-1")

    p = Path(audio_path)
    if not p.is_file():
        return f"音频文件不存在: {audio_path}"

    from openai import OpenAI
    client = OpenAI(api_key=api_key, base_url=base_url)

    try:
        with open(p, "rb") as f:
            transcript = client.audio.transcriptions.create(
                model=whisper_model,
                file=f,
                language="zh",
            )
        return transcript.text or "(无识别结果)"
    except Exception as e:
        return f"语音识别失败: {type(e).__name__}: {e}"


# ─── 全系统文件访问（只读 + 删除审批）────────────────────────

_DANGEROUS_PATHS = frozenset({
    "/", "/bin", "/sbin", "/usr", "/boot", "/dev", "/proc", "/sys",
    "/etc/passwd", "/etc/shadow",
})


def read_system_file(path: str) -> str:
    """读取本机任意位置的文件（只读）。"""
    p = Path(path).resolve()

    if str(p) in _DANGEROUS_PATHS or any(
        str(p).startswith(d + "/") for d in ["/proc", "/sys", "/dev"]
    ):
        return f"安全限制：不允许读取系统关键路径 {path}"

    if not p.is_file():
        return f"文件不存在: {path}"

    try:
        if p.stat().st_size > 10 * 1024 * 1024:
            return f"文件过大 ({p.stat().st_size / 1024 / 1024:.1f} MB)，超出 10MB 限制"

        if _is_binary(p):
            return f"二进制文件: {path} ({p.stat().st_size} bytes) — 无法显示内容，但可以发送"

        content = p.read_text(encoding="utf-8", errors="replace")
        if len(content) > 100_000:
            content = content[:100_000] + "\n\n... [截断于 100K 字符]"
        return content
    except PermissionError:
        return f"无权限读取: {path}"
    except Exception as e:
        return f"读取失败: {type(e).__name__}: {e}"


def list_system_dir(path: str, max_items: int = 100) -> str:
    """列出本机任意目录的内容。"""
    p = Path(path).resolve()
    if not p.is_dir():
        return f"目录不存在: {path}"

    try:
        items = []
        for entry in sorted(p.iterdir()):
            kind = "dir" if entry.is_dir() else "file"
            size = ""
            if entry.is_file():
                try:
                    s = entry.stat().st_size
                    if s > 1024 * 1024:
                        size = f" ({s / 1024 / 1024:.1f} MB)"
                    elif s > 1024:
                        size = f" ({s / 1024:.0f} KB)"
                    else:
                        size = f" ({s} B)"
                except OSError:
                    pass
            items.append(f"  [{kind}] {entry.name}{size}")
            if len(items) >= max_items:
                items.append(f"  ... 还有更多文件")
                break
        return f"{path} ({len(items)} 项):\n" + "\n".join(items)
    except PermissionError:
        return f"无权限访问: {path}"
    except Exception as e:
        return f"列出目录失败: {type(e).__name__}: {e}"


def request_file_delete(path: str, repo_root: Path) -> str:
    """提交文件删除请求到审批队列，不立即执行。"""
    p = Path(path).resolve()
    if not p.exists():
        return f"文件/目录不存在: {path}"

    queue_file = repo_root / "APPROVAL_QUEUE.md"
    import datetime
    now = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=8))
    ).strftime("%Y-%m-%d %H:%M:%S")

    size_info = ""
    if p.is_file():
        size_info = f" ({p.stat().st_size} bytes)"
    elif p.is_dir():
        try:
            count = sum(1 for _ in p.rglob("*"))
            size_info = f" (目录，{count} 个文件)"
        except Exception:
            size_info = " (目录)"

    entry = f"""
---

### [BLOCKING] file-delete

**Requested:** {now}
**Path:** `{path}`{size_info}
**Description:** 请求删除文件/目录。需要主人确认后才会执行。
**Status:** pending

"""
    if queue_file.is_file():
        existing = queue_file.read_text(encoding="utf-8")
    else:
        existing = "# Approval Queue\n\nItems requiring human review.\n"

    queue_file.write_text(existing + entry, encoding="utf-8")
    return f"删除请求已提交审批队列，等待小侑确认: {path}{size_info}"


def get_file_for_send(path: str) -> dict[str, Any]:
    """获取要发送的文件信息。返回包含路径、名称、大小的字典。"""
    p = Path(path).resolve()
    if not p.is_file():
        return {"error": f"文件不存在: {path}"}

    return {
        "path": str(p),
        "name": p.name,
        "size": p.stat().st_size,
        "mime": mimetypes.guess_type(str(p))[0] or "application/octet-stream",
    }


def _is_binary(path: Path) -> bool:
    """简单检测文件是否为二进制。"""
    try:
        with open(path, "rb") as f:
            chunk = f.read(1024)
        null_count = chunk.count(b"\x00")
        return null_count > 5
    except Exception:
        return True


# ─── QQ CQ 码构建工具 ────────────────────────────────────────

def build_image_cq(path_or_url: str) -> str:
    """构建发送图片的 CQ 码。"""
    if path_or_url.startswith(("http://", "https://")):
        return f"[CQ:image,file={path_or_url}]"

    p = Path(path_or_url).resolve()
    if p.is_file():
        return f"[CQ:image,file=file:///{p}]"

    return f"[CQ:image,file={path_or_url}]"


def build_record_cq(audio_path: str) -> str:
    """构建发送语音的 CQ 码。"""
    p = Path(audio_path).resolve()
    if p.is_file():
        return f"[CQ:record,file=file:///{p}]"
    return f"[CQ:record,file={audio_path}]"


def build_face_cq(face_id: int) -> str:
    """构建 QQ 标准表情的 CQ 码。"""
    return f"[CQ:face,id={face_id}]"


# ─── CQ 码解析工具（从收到的消息中提取媒体）──────────────────

_CQ_IMAGE_RE = re.compile(r"\[CQ:image,([^\]]+)\]")
_CQ_RECORD_RE = re.compile(r"\[CQ:record,([^\]]+)\]")
_CQ_FILE_RE = re.compile(r"\[CQ:file,([^\]]+)\]")


def _parse_cq_params(params_str: str) -> dict[str, str]:
    """解析 CQ 码参数字符串为字典。"""
    result = {}
    for part in params_str.split(","):
        if "=" in part:
            k, v = part.split("=", 1)
            result[k.strip()] = v.strip()
    return result


def extract_images(raw_message: str) -> list[dict[str, str]]:
    """从 raw_message 中提取所有图片信息。"""
    images = []
    for m in _CQ_IMAGE_RE.finditer(raw_message):
        params = _parse_cq_params(m.group(1))
        images.append({
            "file": params.get("file", ""),
            "url": params.get("url", ""),
            "type": params.get("type", ""),
        })
    return images


def extract_records(raw_message: str) -> list[dict[str, str]]:
    """从 raw_message 中提取所有语音信息。"""
    records = []
    for m in _CQ_RECORD_RE.finditer(raw_message):
        params = _parse_cq_params(m.group(1))
        records.append({
            "file": params.get("file", ""),
            "url": params.get("url", ""),
        })
    return records


def extract_files(raw_message: str) -> list[dict[str, str]]:
    """从 raw_message 中提取所有文件信息。"""
    files = []
    for m in _CQ_FILE_RE.finditer(raw_message):
        params = _parse_cq_params(m.group(1))
        files.append({
            "file": params.get("file", ""),
            "name": params.get("name", ""),
            "url": params.get("url", ""),
        })
    return files
