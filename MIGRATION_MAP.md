# OpenAkari → Codex Migration Map

> Generated: 2026-03-23
> Source: https://github.com/victoriacity/openakari/tree/main
> Target: Codex/OpenAI Responses API local reproduction

## Component Classification

| Source Path | Purpose | Action | Codex Replacement | Risk |
|---|---|---|---|---|
| `CLAUDE.md` | Agent operating manual — work cycle, conventions, schemas | **RENAME** → `AGENTS.md` | Rewrite vendor-specific language to neutral; keep all operational rules | Low |
| `README.md` | Human-facing repo description | **RENAME** | Rewrite for Codex context; keep philosophy | Low |
| `.claude/skills/` (25 skills) | Encoded judgment procedures | **RENAME** → `skills/` | Move to top-level; strip Claude-specific frontmatter | Low |
| `.cursor/rules/claude-skills.mdc` | Cursor IDE bridge rule | **DROP** | Not needed for Codex workflow | None |
| `decisions/` (67 ADRs) | Architectural decision records | **KEEP** | Text-replace "CLAUDE.md" → "AGENTS.md", ".claude/skills" → "skills" | Low |
| `docs/design.md` | Core design philosophy | **KEEP** | Minor reference updates | Low |
| `docs/repo-as-interface.md` | Repo-as-interface rationale | **KEEP** | No change needed | None |
| `docs/fleet-research.md` | Fleet autonomy evidence | **KEEP** | Phase 2 reference | None |
| `docs/sops/*.md` (9 SOPs) | Standard operating procedures | **RENAME** | Replace `claude -p`, slash-commands with neutral wording | Low |
| `docs/skill-classifications.md` | Skill taxonomy | **KEEP** | Path updates only | Low |
| `docs/getting-started.md` | Onboarding guide | **REWRITE** | Rewrite for Codex CLI/API context | Medium |
| `docs/conventions/*.md` | Referenced in CLAUDE.md but not in open-source snapshot | **STUB** | Create stubs or inline into AGENTS.md | Medium |
| `docs/schemas/*.md` | Referenced in CLAUDE.md but not in open-source snapshot | **STUB** | Create stubs or inline | Medium |
| `projects/akari/` | Meta-project studying the system | **KEEP** | Reference updates | Low |
| `projects/akari/patterns/` (7 patterns) | Evidence-backed design patterns | **KEEP** | Reference path updates | Low |
| `examples/my-research-project/` | Example project scaffold | **KEEP** | No change needed | None |
| `infra/scheduler/` (TypeScript) | Session orchestrator + cron + API | **REWRITE** | Replace Claude Agent SDK with Codex backend; rewrite `backend.ts`, `agent.ts`, `sdk.ts`, `executor.ts` | **High** |
| `infra/scheduler/package.json` | Dependencies incl. `@anthropic-ai/claude-agent-sdk` | **REWRITE** | Remove Claude SDK; add `openai` package | High |
| `infra/scheduler/reference-implementations/` | Slack + fleet references | **PHASE2** | Not needed for MVP | None |
| `infra/experiment-runner/` | Fire-and-forget experiment submission | **KEEP** | Vendor-independent Python | Low |
| `infra/experiment-validator/` | Experiment validation | **KEEP** | Vendor-independent Python | Low |
| `infra/budget-verify/` | Budget enforcement + CF Gateway audit | **KEEP** | May need adapter for OpenAI billing | Low |
| `APPROVAL_QUEUE.md` | Human approval queue | **KEEP** | No change | None |
| `LICENSE` | MIT license | **KEEP** | No change | None |

## New Components Required

| Target Path | Purpose | Priority |
|---|---|---|
| `runner/config.py` | Model config, API keys, environment | P0 |
| `runner/openai_backend.py` | OpenAI Responses API client with tool-call loop | P0 |
| `runner/tools.py` | Local tool execution (read/write/shell/git/approval) | P0 |
| `runner/codex_session_runner.py` | End-to-end session runner with orient→execute→commit cycle | P0 |
| `prompts/system.md` | System prompt for Codex sessions | P0 |
| `prompts/developer.md` | Developer prompt with repo conventions | P0 |
| `requirements.txt` | Python dependencies | P0 |
| `tasks/demo_task.md` | Smoke test task | P1 |

## Known Risks

1. **Scheduler rewrite complexity**: The TypeScript scheduler is ~40+ files deeply integrated with Claude Agent SDK. Full rewrite deferred; Python minimal scheduler built first.
2. **Missing upstream docs**: `docs/conventions/` and `docs/schemas/` are referenced in CLAUDE.md but absent from the open-source snapshot. Must stub or inline.
3. **Skill capability mapping**: Skills reference Claude-specific model tiers (Opus/Sonnet). Need mapping to Codex model capabilities.
4. **API differences**: OpenAI Responses API vs Claude's conversational API have structural differences in tool-call handling.
