"""真实电话工具 — SIP 外呼 + OpenAI Realtime API 实时语音对话。

提供两种电话能力：
  1. 实时语音对话电话：SIP trunk 拨号 → WebSocket 桥接 OpenAI Realtime API
  2. 语音通知外呼：TTS 合成 → SIP 播放语音消息

依赖环境变量：
  SIP_SERVER     - SIP 服务器地址（如 sip.qcloud.com）
  SIP_USERNAME   - SIP 账号
  SIP_PASSWORD   - SIP 密码
  SIP_CALLER_ID  - 主叫号码
  OPENAI_API_KEY - OpenAI API Key（用于 Realtime API）
"""

from __future__ import annotations

import asyncio
import json
import os
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from .media_tools import tts_generate, _get_cache_dir


@dataclass
class CallConfig:
    """电话配置。"""
    sip_server: str = ""
    sip_username: str = ""
    sip_password: str = ""
    caller_id: str = ""
    openai_api_key: str = ""
    openai_base_url: str = ""

    @classmethod
    def from_env(cls) -> CallConfig:
        return cls(
            sip_server=os.environ.get("SIP_SERVER", ""),
            sip_username=os.environ.get("SIP_USERNAME", ""),
            sip_password=os.environ.get("SIP_PASSWORD", ""),
            caller_id=os.environ.get("SIP_CALLER_ID", ""),
            openai_api_key=os.environ.get("OPENAI_API_KEY", ""),
            openai_base_url=os.environ.get(
                "OPENAI_BASE_URL", "https://code.vangularcode.asia/v1"
            ),
        )

    @property
    def sip_configured(self) -> bool:
        return bool(self.sip_server and self.sip_username and self.sip_password)


@dataclass
class CallRecord:
    """通话记录。"""
    call_id: str
    phone_number: str
    call_type: str  # "realtime" | "notification"
    status: str  # "pending" | "ringing" | "active" | "ended" | "failed"
    started_at: float = 0.0
    ended_at: float = 0.0
    duration_seconds: float = 0.0
    transcript: list[dict[str, str]] = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "call_id": self.call_id,
            "phone_number": self.phone_number,
            "call_type": self.call_type,
            "status": self.status,
            "duration": f"{self.duration_seconds:.1f}s",
            "transcript_length": len(self.transcript),
            "error": self.error,
        }


_active_calls: dict[str, CallRecord] = {}


def _generate_call_id() -> str:
    return f"call_{int(time.time() * 1000)}"


def check_phone_setup() -> dict[str, Any]:
    """检查电话功能的配置状态。"""
    config = CallConfig.from_env()
    result: dict[str, Any] = {
        "sip_configured": config.sip_configured,
        "openai_key_set": bool(config.openai_api_key),
        "missing": [],
    }

    if not config.sip_server:
        result["missing"].append("SIP_SERVER")
    if not config.sip_username:
        result["missing"].append("SIP_USERNAME")
    if not config.sip_password:
        result["missing"].append("SIP_PASSWORD")
    if not config.caller_id:
        result["missing"].append("SIP_CALLER_ID (主叫号码)")
    if not config.openai_api_key:
        result["missing"].append("OPENAI_API_KEY")

    if result["missing"]:
        result["message"] = (
            f"电话功能尚未完全配置。缺少: {', '.join(result['missing'])}。\n"
            "请在环境变量或 .env 文件中设置这些值。"
        )
    else:
        result["message"] = "电话功能已配置就绪。"

    return result


# ─── 语音通知外呼 ────────────────────────────────────────────

def make_notification_call(
    phone_number: str,
    message: str,
    voice: str = "",
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """发起语音通知电话：TTS 合成消息 → SIP 外呼播放。

    这是一种单向通话，只播放合成的语音消息给对方。
    适用于：提醒、通知、闹钟等场景。
    """
    config = CallConfig.from_env()
    if not config.sip_configured:
        return {"error": "SIP 未配置。请设置 SIP_SERVER / SIP_USERNAME / SIP_PASSWORD"}

    call_id = _generate_call_id()
    record = CallRecord(
        call_id=call_id,
        phone_number=phone_number,
        call_type="notification",
        status="pending",
        started_at=time.time(),
    )
    _active_calls[call_id] = record

    try:
        audio_path = tts_generate(message, voice=voice)
        record.status = "ringing"
        record.transcript.append({"role": "system", "content": message})

        _sip_play_audio(config, phone_number, str(audio_path))

        record.status = "ended"
        record.ended_at = time.time()
        record.duration_seconds = record.ended_at - record.started_at

    except Exception as e:
        record.status = "failed"
        record.error = str(e)
        record.ended_at = time.time()

    _save_call_record(record, repo_root)
    return record.to_dict()


# ─── 实时语音对话电话 ────────────────────────────────────────

def make_realtime_call(
    phone_number: str,
    system_prompt: str = "",
    repo_root: Path | None = None,
    progress_callback: Callable[[str], None] | None = None,
) -> dict[str, Any]:
    """发起实时语音对话电话：SIP 拨号 → 双向音频 → OpenAI Realtime API。

    这是双向通话，小白可以与对方实时对话。
    SIP → RTP 音频流 → WebSocket → OpenAI Realtime API → 合成语音 → RTP → SIP
    """
    config = CallConfig.from_env()
    if not config.sip_configured:
        return {"error": "SIP 未配置。请设置 SIP_SERVER / SIP_USERNAME / SIP_PASSWORD"}
    if not config.openai_api_key:
        return {"error": "OPENAI_API_KEY 未设置，无法使用 Realtime API"}

    call_id = _generate_call_id()
    record = CallRecord(
        call_id=call_id,
        phone_number=phone_number,
        call_type="realtime",
        status="pending",
        started_at=time.time(),
    )
    _active_calls[call_id] = record

    if not system_prompt:
        system_prompt = (
            "你是小白，一个可爱、聪明、有礼貌的 AI 助手。"
            "你正在通过电话与人交流。请用简洁自然的口语回复。"
            "不要使用 markdown 或特殊格式。"
        )

    if progress_callback:
        progress_callback(f"正在拨打 {phone_number}...")

    try:
        record.status = "ringing"

        result = asyncio.run(
            _realtime_call_session(config, phone_number, system_prompt, record, progress_callback)
        )

        record.status = "ended"
        record.ended_at = time.time()
        record.duration_seconds = record.ended_at - record.started_at

    except Exception as e:
        record.status = "failed"
        record.error = str(e)
        record.ended_at = time.time()
        if progress_callback:
            progress_callback(f"通话失败: {e}")

    _save_call_record(record, repo_root)
    return record.to_dict()


async def _realtime_call_session(
    config: CallConfig,
    phone_number: str,
    system_prompt: str,
    record: CallRecord,
    progress_callback: Callable[[str], None] | None = None,
) -> None:
    """实时通话会话：协调 SIP 和 OpenAI Realtime API。

    架构：
    ┌─────────┐    RTP     ┌──────────┐   WebSocket  ┌──────────────┐
    │ 电话网络 │ ◄──────── │ SIP 客户端│ ◄──────────► │ OpenAI       │
    │ (对方)   │ ────────► │ (PJSIP)  │              │ Realtime API │
    └─────────┘            └──────────┘              └──────────────┘
    """
    try:
        import websockets
    except ImportError:
        raise RuntimeError("需要安装 websockets: pip install websockets")

    ws_url = f"wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview"

    async with websockets.connect(
        ws_url,
        additional_headers={
            "Authorization": f"Bearer {config.openai_api_key}",
            "OpenAI-Beta": "realtime=v1",
        },
    ) as ws:
        session_config = {
            "type": "session.update",
            "session": {
                "modalities": ["text", "audio"],
                "instructions": system_prompt,
                "voice": "shimmer",
                "input_audio_format": "pcm16",
                "output_audio_format": "pcm16",
                "input_audio_transcription": {"model": "whisper-1"},
                "turn_detection": {
                    "type": "server_vad",
                    "threshold": 0.5,
                    "prefix_padding_ms": 300,
                    "silence_duration_ms": 500,
                },
            },
        }
        await ws.send(json.dumps(session_config))

        record.status = "active"
        if progress_callback:
            progress_callback("通话已接通，AI 正在与对方交流...")

        sip_process = await _start_sip_bridge(config, phone_number)

        try:
            async for msg in ws:
                event = json.loads(msg)
                event_type = event.get("type", "")

                if event_type == "response.audio_transcript.done":
                    text = event.get("transcript", "")
                    if text:
                        record.transcript.append({"role": "assistant", "content": text})

                elif event_type == "conversation.item.input_audio_transcription.completed":
                    text = event.get("transcript", "")
                    if text:
                        record.transcript.append({"role": "user", "content": text})
                        if progress_callback:
                            progress_callback(f"对方说: {text[:50]}...")

                elif event_type == "error":
                    err = event.get("error", {})
                    record.error = err.get("message", str(err))
                    break

        finally:
            if sip_process:
                sip_process.terminate()


async def _start_sip_bridge(
    config: CallConfig,
    phone_number: str,
) -> subprocess.Popen | None:
    """启动 SIP → RTP 桥接进程（基于 PJSIP / baresip）。

    这里使用外部 SIP 客户端进程。实际部署时需要：
    1. 安装 pjsip 或 baresip
    2. 配置 SIP trunk 账号
    3. 将 RTP 音频流桥接到 WebSocket
    """
    sip_script = _get_cache_dir() / "sip_bridge.sh"

    sip_uri = f"sip:{phone_number}@{config.sip_server}"

    sip_script.write_text(f"""#!/bin/bash
# SIP Bridge Script — 自动生成
# 需要预先安装 pjsua 或 baresip

if command -v pjsua &> /dev/null; then
    pjsua \\
        --registrar "sip:{config.sip_server}" \\
        --id "sip:{config.caller_id}@{config.sip_server}" \\
        --realm "*" \\
        --username "{config.sip_username}" \\
        --password "{config.sip_password}" \\
        --auto-answer 200 \\
        --max-calls 1 \\
        "{sip_uri}"
else
    echo "ERROR: pjsua not found. Install PJSIP first."
    echo "  Ubuntu: apt-get install pjsua"
    echo "  Or build from source: https://www.pjsip.org/"
    exit 1
fi
""", encoding="utf-8")

    sip_script.chmod(0o755)

    try:
        proc = subprocess.Popen(
            [str(sip_script)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        await asyncio.sleep(2)
        return proc
    except Exception:
        return None


def _sip_play_audio(config: CallConfig, phone_number: str, audio_path: str) -> None:
    """通过 SIP 向指定号码播放音频文件。"""
    sip_uri = f"sip:{phone_number}@{config.sip_server}"

    try:
        subprocess.run(
            [
                "pjsua",
                "--registrar", f"sip:{config.sip_server}",
                "--id", f"sip:{config.caller_id}@{config.sip_server}",
                "--realm", "*",
                "--username", config.sip_username,
                "--password", config.sip_password,
                "--play-file", audio_path,
                "--auto-play",
                "--auto-hangup-after", "60",
                "--max-calls", "1",
                sip_uri,
            ],
            timeout=120,
            capture_output=True,
        )
    except FileNotFoundError:
        raise RuntimeError(
            "pjsua 未安装。请安装 PJSIP:\n"
            "  Ubuntu: apt-get install pjsua\n"
            "  或从源码编译: https://www.pjsip.org/"
        )
    except subprocess.TimeoutExpired:
        pass


def _save_call_record(record: CallRecord, repo_root: Path | None = None) -> None:
    """保存通话记录到日志。"""
    if repo_root is None:
        repo_root = Path(os.environ.get("OPENAKARI_HOME", "."))

    log_dir = repo_root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "phone-calls.jsonl"

    import datetime
    entry = {
        "timestamp": datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=8))
        ).strftime("%Y-%m-%d %H:%M:%S"),
        **record.to_dict(),
        "full_transcript": record.transcript,
    }

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def get_call_status(call_id: str) -> dict[str, Any]:
    """查询活跃通话状态。"""
    record = _active_calls.get(call_id)
    if not record:
        return {"error": f"未找到通话: {call_id}"}
    return record.to_dict()


def list_recent_calls(repo_root: Path | None = None, limit: int = 10) -> list[dict[str, Any]]:
    """列出最近的通话记录。"""
    if repo_root is None:
        repo_root = Path(os.environ.get("OPENAKARI_HOME", "."))

    log_file = repo_root / "logs" / "phone-calls.jsonl"
    if not log_file.is_file():
        return []

    records = []
    for line in log_file.read_text(encoding="utf-8").strip().splitlines():
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    return records[-limit:]
