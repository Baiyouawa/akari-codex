# AGENTS.md

This file provides guidance to the autonomous agent (powered by Codex/OpenAI Responses API) when working in this repository.

## What this repo is

This is a research group monorepo operated autonomously by LLM agents. The repo serves as both artifact storage and cognitive state — it is the agents' persistent memory between sessions. See [docs/design.md](docs/design.md) for rationale.

## Work cycle

The conversation is ephemeral; the repo is permanent. Record as you go, not at the end.

- **Finding → file, immediately.** When you discover a fact (data path, schema, limitation, dependency), update the relevant project file in the same turn. Do not defer.
- **Decision → log or decision record.** When you make a choice or resolve an open question, write a log entry or decision record before moving on.
- **Plan → plans/ directory.** When you produce a non-trivial plan, write it to `plans/<name>.md` in the project directory.
- **Session summary → log entry.** Before ending a session, add a dated log entry to every project README you touched.
- **Open questions → README.** When you identify something you can't resolve, add it to the project's `## Open questions` section.

The test: if you started a fresh session and read only the repo, would you know everything the previous session learned?

### Knowledge output

This system is a research institute, not a task runner. Every plan, experiment, and session should be evaluated by the knowledge it produces — findings, decisions, hypotheses tested, questions resolved. The fundamental efficiency metric is **findings per dollar**.

Before any implementation plan, ask: "What knowledge does this produce?"

**Inline logging checklist** (see `decisions/0004-inline-logging.md`):

1. Discovery of a non-obvious fact → write to project file **in the same turn**.
2. Config/env change → log entry with before/after and rationale.
3. Successful verification → log the exact command and output.
4. Log incrementally throughout the session.
5. **Findings provenance:** Every numerical claim must include either (a) the script + data file that produces it, or (b) inline arithmetic from referenced data.

## Autonomous execution

This repo runs autonomous agent sessions via the scheduler infrastructure.
Each session follows the standard operating procedure:

1. **Orient** — Read repo state, identify current project priorities and open tasks.
2. **Select** — Pick one task based on priority, budget, and dependency state.
3. **Classify** — Determine scope: ROUTINE / RESOURCE / STRUCTURAL.
4. **Execute** — Perform the task using available tools.
5. **Commit** — Write findings, update task state, commit to repo.

### Approval gates

Autonomous sessions MUST NOT proceed with:
- **Resource decisions**: Increasing budget limits or extending deadlines
- **Governance changes**: Changes to approval workflow, budget rules, or governance mechanisms in AGENTS.md
- **Tool access**: Requests for tools or APIs not currently configured
- **Production PRs**: Opening pull requests to production modules

Write to `APPROVAL_QUEUE.md` and end the session for blocking items.

Everything else does **not** need approval, including: infrastructure fixes, new files, new decision records, schema changes, refactors — as long as correctness is verifiable by code.

### Session discipline

- Every session begins with orient (reading repo state)
- Every session ends with a git commit and log entry
- If a session produces no useful work, log that fact and end cleanly
- Do not re-litigate decisions recorded in `decisions/`
- Sessions submit experiments, they do not supervise — use fire-and-forget for long-running compute
- Never sleep more than 30 seconds in a session
- Commit incrementally during sessions
- Batch archival commits per project

### Task lifecycle tags

Use these tags in `TASKS.md` to coordinate across sessions:

- `[in-progress: YYYY-MM-DD]` — being worked on
- `[blocked-by: <description>]` — cannot proceed until condition is met
- `[approval-needed]` — requires human sign-off
- `[approved: YYYY-MM-DD]` — human approved, ready to execute
- `[zero-resource]` — consumes no budget resources
- `[skill: <type>]` — skill-typed routing tag

Skill types:
- `record` → documentation, status updates, archival
- `persist` → state management, cross-references
- `govern` → convention compliance, self-audits
- `execute` → code changes, scripts, bug fixes
- `diagnose` → root cause analysis, debugging
- `analyze` → experiment results interpretation
- `orient` → strategic task selection and planning
- `multi` → requires reasoning + implementation + knowledge

### Task decomposition

Decompose a task when:
- It has more than 2 independent steps
- It touches more than 3 files
- It combines blocked and unblocked work
- It mixes mechanical work with judgment-requiring work

### Partial completion

Never mark a task `[x]` with a "(partial)" annotation. If work is partially done, keep the task `[ ]` and update the description, or split into subtasks.

## Conventions

| Convention | Description |
|---|---|
| File conventions | Naming, organization, archival rules |
| Provenance | Every claim leashed to a source |
| Temporal reasoning | Claims about duration, age, timelines require evidence |
| Decisions | Significant choices → ADR in `decisions/` |
| Structured work records | YAML frontmatter, type-specific sections |

## Schemas

| Schema | Purpose |
|---|---|
| Log entry | Session log format |
| Task | Task description format in TASKS.md |
| Decision record | ADR format in decisions/ |
| Experiment | EXPERIMENT.md structure |
| Budget & ledger | budget.yaml / ledger.yaml |

## Infrastructure

`infra/` holds shared tooling — experiment harnesses, scheduling, budget verification. Each tool gets its own subdirectory with a README.

## Model configuration

The default model is configured via environment variables:
- `OPENAI_API_KEY` — API authentication
- `OPENAI_BASE_URL` — API endpoint (default: `https://code.vangularcode.asia/v1`)
- `OPENAI_MODEL` — Model identifier (default: `gpt-5.4`)
- `OPENAKARI_HOME` — Root path of this repository
