You are working in the OpenAkari-Codex research repository.

## Repository structure

- `AGENTS.md` — Operating manual for agent sessions
- `skills/` — 25 encoded judgment procedures (orient, design, diagnose, critique, etc.)
- `decisions/` — Architectural decision records (ADRs)
- `tasks/` — Task definitions with lifecycle tags
- `logs/` — Session logs and failure records
- `approvals/` — Approval queue and records
- `projects/` — Research project directories
- `infra/` — Shared tooling (scheduler, experiment-runner, budget-verify)
- `prompts/` — System and developer prompts

## Current task

Read the task provided and execute it following the session protocol in AGENTS.md.
Before acting, orient yourself by reading the project README and recent logs.
After completing work, write a session log and update the task state.

## Conventions

- Every session log uses ISO 8601 timestamps
- Decision records follow the ADR format in `decisions/`
- Task state changes must be committed to `TASKS.md`
- Findings require provenance (script path or inline arithmetic)
- Never mark a task complete with "(partial)" — split instead
