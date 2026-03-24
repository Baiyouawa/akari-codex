# OpenAkari-Codex

**Autonomous Knowledge Acquisition and Research Intelligence — powered by Codex/OpenAI**

This is a local reproduction of the [OpenAkari](https://github.com/victoriacity/openakari) research operating system, with the agent runtime rebuilt around the OpenAI Responses API (Codex models).

## What this is

A repository-as-memory system where LLM agents operate as persistent researchers — selecting tasks, running experiments, recording findings, and building institutional knowledge across stateless sessions.

## Architecture

```
┌─────────────────────────────────────────────┐
│              Repo Memory Layer              │
│  tasks/ logs/ decisions/ approvals/ skills/ │
├─────────────────────────────────────────────┤
│            Agent Policy Layer               │
│     AGENTS.md  prompts/  project rules      │
├─────────────────────────────────────────────┤
│           Codex Backend Layer               │
│  OpenAI Responses API  tool-call loop       │
│  token/cost logging  model selection        │
├─────────────────────────────────────────────┤
│           Execution Layer                   │
│  shell executor  file I/O  git ops          │
│  search  approval gates                     │
├─────────────────────────────────────────────┤
│      Scheduler & Governance Layer           │
│  cron jobs  approval queue  provenance      │
│  failure replay  budget enforcement         │
└─────────────────────────────────────────────┘
```

## Quick start

```bash
# Set environment
export OPENAI_API_KEY="your_key"
export OPENAI_BASE_URL="https://code.vangularcode.asia/v1"
export OPENAI_MODEL="gpt-5.4"
export OPENAKARI_HOME="$(pwd)"

# Install dependencies
pip install -r requirements.txt

# Run a single session
python runner/codex_session_runner.py --task tasks/demo_task.md

# Run with scheduler
python runner/codex_session_runner.py --scheduler
```

## Key files

| File | Purpose |
|---|---|
| `AGENTS.md` | Agent operating manual |
| `runner/openai_backend.py` | Codex/OpenAI Responses API client |
| `runner/codex_session_runner.py` | Session runner with orient→execute→commit |
| `runner/tools.py` | Local tool execution layer |
| `runner/config.py` | Configuration and environment handling |
| `skills/` | 25 encoded judgment procedures |
| `decisions/` | 67 architectural decision records |

## Remote channels

In addition to the local CLI (`python -m runner.chat`), two remote channels allow you to issue natural language commands from anywhere:

| Channel | Trigger | Docs |
|---|---|---|
| **GitHub Issue/Discussion** | Comment `/akari <command>` on any Issue or Discussion | [docs/remote-channels.md](docs/remote-channels.md#github) |
| **QQ Official Bot** | @-mention the bot in a QQ guild/group channel | [docs/remote-channels.md](docs/remote-channels.md#qq-bot) |

Both channels route through `runner/gateway.py` which handles auth, logging, and output sanitization without touching core runner code.

## Design philosophy

- **The repo is the brain.** Agents have no memory between sessions.
- **Provenance over assertion.** Every claim leashed to a source.
- **Convention over configuration.** Schemas and SOPs reduce drift.
- **Knowledge output over task completion.** Findings per dollar is the metric.

## Recent updates

- 2026-03-23T12:01:14Z — Completed initial repository health check. Verified readable `AGENTS.md` and `README.md`, confirmed root structure (`approvals/`, `artifacts/`, `decisions/`, `docs/`, `examples/`, `infra/`, `jobs/`, `logs/`, `projects/`, `prompts/`, `runner/`, `skills/`, `tasks/`), and recorded open-task inventory in `logs/sessions/2026-03-23T120114Z-repo-health-check.md`.

## Origin

Migrated from [OpenAkari](https://github.com/victoriacity/openakari) (MIT License).
Backend replaced from Claude Code to Codex/OpenAI Responses API.
See `MIGRATION_MAP.md` for the full migration record.
