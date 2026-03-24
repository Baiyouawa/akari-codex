# Remote Channels — Configuration & Usage

OpenAkari-Codex supports two remote channels for natural language command execution. Both channels converge on `runner/gateway.py`, which bridges external protocols to the existing `ChatBot.process_message()` without modifying any core runner code.

```
GitHub Issue Comment ─┐
                      ├──▶ runner/gateway.py ──▶ ChatBot ──▶ SessionRunner
QQ @-mention ─────────┘
```

---

## GitHub Issue / Discussion Commands {#github}

### How it works

1. You write a comment on any Issue or Discussion starting with `/akari`
2. `akari-command.yml` picks it up and dispatches a `repository_dispatch` event
3. `akari-execute.yml` runs the gateway in a fresh Actions runner
4. The result is posted back as a comment on the same Issue/Discussion

### Setup

**Step 1: Add repository secrets**

Go to **Settings > Secrets and variables > Actions** and add:

| Secret | Description |
|---|---|
| `OPENAI_API_KEY` | Your OpenAI-compatible API key |
| `OPENAI_BASE_URL` | API base URL (e.g. `https://code.vangularcode.asia/v1`) |
| `OPENAI_MODEL` | Model to use (e.g. `gpt-5.4`) |

**Step 2: Enable workflows**

The two workflow files are already in `.github/workflows/`:
- `akari-command.yml` — Listens for comments, parses `/akari` commands
- `akari-execute.yml` — Executes the command and posts results

Push the repo to GitHub and workflows are automatically enabled.

**Step 3 (optional): Enable Discussions**

If you want Discussion-based commands, enable Discussions in **Settings > General > Features**.

### Usage

In any Issue or Discussion comment, write:

```
/akari 调研近三个月 arxiv 上 multi-agent 论文
```

```
/akari 查看状态
```

```
/akari 创建一个关于 LLM 安全的调研项目
```

The bot will:
1. React with "eyes" emoji to acknowledge
2. Execute the command
3. Post the result as a reply comment
4. React with "rocket" (success) or "confused" (failure)

### Security

- Only users with `OWNER`, `MEMBER`, or `COLLABORATOR` association can trigger commands
- All invocations are logged to `logs/remote-invocations.jsonl`
- Output is sanitized to remove API keys, absolute paths, and other sensitive data
- Results are truncated to 3500 characters (full output available in Actions logs)

### Customizing allowed users

Set the `AKARI_ALLOWED_USERS` secret (comma-separated) to restrict which GitHub users can trigger commands:

```
alice,bob,carol
```

If not set, all repo members can use `/akari`.

---

## QQ Official Bot {#qq-bot}

### Prerequisites

1. Register a bot at [QQ Bot Open Platform](https://q.qq.com)
2. Get your `AppID` and `Token` from the bot dashboard
3. Add the bot to a QQ guild (server)

### Setup

**Step 1: Install dependency**

```bash
pip install qq-botpy
```

(Already included in `requirements.txt`)

**Step 2: Set environment variables**

```bash
export QQ_BOT_APPID="your_appid"
export QQ_BOT_TOKEN="your_token"

# Optional: sandbox mode for testing
export QQ_BOT_SANDBOX="1"

# Optional: restrict to specific QQ user IDs
export QQ_ADMIN_USERS="user_id_1,user_id_2"

# Required: OpenAI API config (same as core system)
export OPENAI_API_KEY="your_key"
export OPENAI_BASE_URL="https://code.vangularcode.asia/v1"
export OPENAI_MODEL="gpt-5.4"
```

**Step 3: Run the bot**

```bash
cd /path/to/openakari-codex
python -m integrations.qq_bot
```

### Usage

In a QQ guild channel, @-mention the bot followed by your command:

```
@Akari 调研 multi-agent 论文
```

```
@Akari 查看状态
```

```
@Akari 帮助
```

The bot will:
1. Acknowledge with "收到指令，正在执行..."
2. Run the command through the gateway
3. Post the result back in the same channel

### Group messages

The bot also supports QQ group (@-mention) messages. The handler works the same way but uses the group message API.

### Long messages

QQ has a 2000-character message limit. Long results are automatically split into multiple messages.

### Security

- Set `QQ_ADMIN_USERS` to restrict which QQ users can issue commands
- If empty, all users in the guild/group can use the bot
- All invocations are logged to `logs/remote-invocations.jsonl`
- Output is sanitized before sending

---

## Unified Gateway

Both channels use `runner/gateway.py` as the single entry point:

```python
from runner.gateway import process_remote_message

result = process_remote_message(
    source="github",       # or "qq", "qq-group"
    user="alice",
    text="调研 multi-agent 论文",
)
```

### Features

- **Auth checking**: Optional user allowlist via `AKARI_ALLOWED_USERS` env var
- **Output sanitization**: Strips API keys, absolute paths, and other sensitive data
- **Truncation**: Results capped at 4000 characters for external channels
- **Logging**: All invocations recorded in `logs/remote-invocations.jsonl` as JSON lines

### CLI usage

The gateway can also be invoked directly:

```bash
python -m runner.gateway --source test --user dev --message "查看状态"
```

---

## Architecture Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                     External Channels                        │
│                                                              │
│  ┌─────────────────────┐    ┌─────────────────────────┐     │
│  │  GitHub Issue/Disc.  │    │  QQ Guild/Group         │     │
│  │  /akari <command>    │    │  @Akari <command>       │     │
│  └──────────┬──────────┘    └───────────┬─────────────┘     │
│             │                           │                    │
│  ┌──────────▼──────────┐    ┌───────────▼─────────────┐     │
│  │ akari-command.yml    │    │ integrations/qq_bot.py  │     │
│  │ akari-execute.yml    │    │ (qq-botpy long-running) │     │
│  │ (GitHub Actions)     │    │                         │     │
│  └──────────┬──────────┘    └───────────┬─────────────┘     │
└─────────────┼───────────────────────────┼────────────────────┘
              │                           │
              ▼                           ▼
      ┌───────────────────────────────────────────┐
      │          runner/gateway.py                 │
      │  process_remote_message(source, user, txt) │
      │  - auth check                              │
      │  - sanitize output                         │
      │  - log invocation                          │
      └─────────────────┬─────────────────────────┘
                        │
                        ▼
      ┌───────────────────────────────────────────┐
      │          runner/chat.py (unchanged)        │
      │  ChatBot.process_message(text)             │
      │  - LLM intent parsing                      │
      │  - Action dispatch                         │
      └─────────────────┬─────────────────────────┘
                        │
                        ▼
      ┌───────────────────────────────────────────┐
      │     Core Runner (all unchanged)            │
      │  SessionRunner → CodexBackend → Tools      │
      └───────────────────────────────────────────┘
```
