# Local example: task decomposition created a reusable self-improvement loop

Date: 2026-03-23
Project: akari
Type: local analysis

## Claim

This repository already contains one local example of a successful self-improvement loop:

1. detect an operational gap from repo evidence
2. change the system state so later sessions can route around the gap
3. observe that a later session actually used the new state to produce more knowledge

## Loop

### 1. Gap detected

A `projects/multi-agent-survey` session found that the original NeurIPS 2024-2025 retrieval task was over-coupled to a source limitation.

The relevant evidence from the session log:

- Crossref retrieval produced `138` NeurIPS 2024 candidates and `0` NeurIPS 2025 candidates.
- The session therefore concluded that the combined 2024-2025 task should be split instead of staying as one blocked unit.

Provenance:
- `logs/sessions/2026-03-23T161441Z-neurips-2024-harvest.md`
- `projects/multi-agent-survey/literature/neurips-2024-2025.md`

### 2. System change

The system changed its own operating state in two ways:

1. it wrote the 2024 artifact to `projects/multi-agent-survey/literature/neurips-2024-2025.md`
2. it decomposed the task in `projects/multi-agent-survey/TASKS.md` into:
   - one completed 2024 retrieval task
   - one blocked 2025 follow-up task

This matters because the repo-memory state now expresses a finer-grained truth: 2024 coverage is usable even though 2025 coverage is still blocked.

Provenance:
- `logs/sessions/2026-03-23T161441Z-neurips-2024-harvest.md`
- `projects/multi-agent-survey/TASKS.md`

### 3. Measured after-effect

A later session reused that newly-unblocked 2024 artifact to answer an open research question in the project README:

- At `2026-03-23T16:32:00Z`, the project README records a provisional answer to the question about the boundary between multi-agent systems and single-agent + tools.
- That answer explicitly cites title-level evidence from `projects/multi-agent-survey/literature/neurips-2024-2025.md`.

Provenance:
- `projects/multi-agent-survey/README.md`
- `projects/multi-agent-survey/literature/neurips-2024-2025.md`

## Before / after

### Before the change

The NeurIPS retrieval work was one combined 2024-2025 task, and the 2025 source gap prevented the task from being cleanly completed as written.

Provenance:
- `logs/sessions/2026-03-23T161441Z-neurips-2024-harvest.md` states that the original task covered both 2024 and 2025 and had to be split because the current Crossref snapshot returned `2024 138` and `2025 0`.

### After the change

The repo had:

- `1` completed NeurIPS retrieval task (`检索 NeurIPS 2024 Multi-Agent 相关论文`)
- `1` blocked follow-up task for 2025
- `1` concrete README knowledge increment that reused the 2024 artifact

Provenance:
- `projects/multi-agent-survey/TASKS.md`
- `projects/multi-agent-survey/README.md`

## Operational improvement

The improvement was not merely descriptive; it changed what later sessions could do.

- Before decomposition, the repo had one coupled task whose unresolved 2025 half limited how cleanly the 2024 half could be reused.
- After decomposition, later work no longer needed to wait for NeurIPS 2025 coverage to start producing analysis from NeurIPS 2024 evidence.

A minimal measurable delta is therefore:

- completed usable NeurIPS retrieval subtasks: `0 -> 1`
- blocked NeurIPS retrieval subtasks isolated instead of entangled with usable work: `0 -> 1`
- downstream knowledge-producing reuse events recorded in the README: `0 -> 1`

Provenance:
- before state from `logs/sessions/2026-03-23T161441Z-neurips-2024-harvest.md`
- after state from `projects/multi-agent-survey/TASKS.md` and `projects/multi-agent-survey/README.md`

## Timing

The downstream reuse happened the same day.

Inline arithmetic from README timestamps:
- decomposition/logging timestamp: `2026-03-23T16:14:41Z`
- downstream reuse timestamp: `2026-03-23T16:32:00Z`
- elapsed time: `17 minutes 19 seconds`

Provenance:
- `logs/sessions/2026-03-23T161441Z-neurips-2024-harvest.md`
- `projects/multi-agent-survey/README.md`

## Why this counts as self-improvement

The system observed a coordination failure in its own workflow, rewrote its own task structure, and then benefited from that rewrite in a later session. That is the meta-project’s target behavior in miniature: operational evidence -> system change -> measured downstream improvement.
