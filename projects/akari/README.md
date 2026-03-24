# akari: Meta-Project for Self-Improvement

Status: active
Mission: Study and improve the autonomous research system itself.
Done when: The system demonstrates self-directed capability improvement by identifying gaps from operational data, implementing changes, and measuring whether autonomy and knowledge output improve over time.

## Context

Akari's core idea is that the research system should study itself.

This project is the meta-project for openakari. Its subject is not an external benchmark or domain problem. Its subject is the behavior of the autonomous system itself: how sessions coordinate, where they fail, how human intervention changes over time, and which infrastructure or convention changes actually improve performance.

The artifacts here are adapted from the original private akari repo's operational history. They are included as examples of what it looks like when an AI-native software system treats its own operations as a research object.

## Log

### 2026-03-08

Created the public meta-project scaffold for openakari. Added a project README, task list, and three example artifacts adapted from the original akari repo: a self-improvement measurement plan, a human-intervention trend analysis, and a self-observation diagnosis. These examples show how the system studies its own behavior rather than only external tasks.

### 2026-03-23T16:15:00Z

Ran a convention/quality audit for the akari project.

Findings:
1. `projects/akari/README.md` follows the expected project README structure (`Status`, `Mission`, `Done when`, `## Context`, `## Log`, `## Open questions`).
   - Provenance: direct read of `projects/akari/README.md` during this session.
2. `projects/akari/TASKS.md` task entries are internally consistent: each open item includes a checkbox line plus `Why`, `Done when`, and `Priority` fields.
   - Provenance: direct read of `projects/akari/TASKS.md` during this session.
3. One stale repository-level contradiction was found outside the project directory: root `README.md` claimed `decisions/` contained 67 records, but shell count returned 68 files.
   - Provenance: `run_shell("find decisions -maxdepth 1 -type f | wc -l")` returned `68`; root `README.md` previously said `67 architectural decision records`.
4. The stale root README count was corrected in place.
   - Provenance: updated `README.md` in this session.

### 2026-03-23T16:35:35Z

Measured a local human-intervention baseline for this deployment in `projects/akari/analysis/human-intervention-rate-2026-03-23.md`.

Findings:
1. The current deployment snapshot contains 3 session JSON records in `logs/sessions/`.
   - Provenance: `logs/sessions/session-20260323-120013-60cedbe2.json`, `logs/sessions/session-20260323-160117-0eb0dceb.json`, `logs/sessions/session-20260323-161007-0e17eb63.json`.
2. Only 1 approval-queue event was included as a real human-decision escalation in the observed windows.
   - Provenance: `APPROVAL_QUEUE.md` includes a real `tool-access` escalation at `2026-03-23T16:04:42.991412+00:00`; the `test-action` smoke-test entry was excluded from the metric.
3. Intervention events per session were `0.00` in the `12:00-12:59 UTC` window and `0.50` in the `16:00-16:59 UTC` window.
   - Provenance: inline arithmetic from the timestamps above and the analysis file.

Interpretation: this is a bootstrap baseline rather than a trend conclusion, because the sample size is only 3 sessions and 1 included intervention event.

### 2026-03-23T16:35:30Z

Recorded a local successful self-improvement loop in `projects/akari/analysis/local-self-improvement-loop-example.md`.

Findings:
1. A `projects/multi-agent-survey` session detected that the original combined NeurIPS 2024-2025 retrieval task was blocked by a source gap on the 2025 half: Crossref retrieval returned `138` NeurIPS 2024 candidates and `0` NeurIPS 2025 candidates.
   - Provenance: `logs/sessions/2026-03-23T161441Z-neurips-2024-harvest.md`; `projects/multi-agent-survey/literature/neurips-2024-2025.md`.
2. The system changed its own operating state by splitting the coupled task into one completed 2024 retrieval task and one blocked 2025 follow-up task.
   - Provenance: `projects/multi-agent-survey/TASKS.md`; `logs/sessions/2026-03-23T161441Z-neurips-2024-harvest.md`.
3. After that change, a later README update reused the new 2024 artifact to answer the open question about the boundary between multi-agent systems and single-agent + tools.
   - Provenance: `projects/multi-agent-survey/README.md` cites `projects/multi-agent-survey/literature/neurips-2024-2025.md` in the `2026-03-23T16:32:00Z` log entry.
4. The minimal before/after operational delta for that loop was: completed usable NeurIPS retrieval subtasks `0 -> 1`, isolated blocked follow-up subtasks `0 -> 1`, and recorded downstream reuse events `0 -> 1`.
   - Provenance: before-state description in `logs/sessions/2026-03-23T161441Z-neurips-2024-harvest.md`; after-state in `projects/multi-agent-survey/TASKS.md` and `projects/multi-agent-survey/README.md`.
5. The downstream reuse happened `17 minutes 19 seconds` after the decomposition was logged.
   - Provenance: inline arithmetic from `2026-03-23T16:14:41Z` in `logs/sessions/2026-03-23T161441Z-neurips-2024-harvest.md` and `2026-03-23T16:32:00Z` in `projects/multi-agent-survey/README.md`.

Interpretation: this is a local miniature of the target meta-loop — operational evidence identified a workflow coupling problem, the repo-memory state was changed to isolate usable work from blocked work, and a later session produced new knowledge without waiting for the blocked half to clear.

### 2026-03-24T03:41:44Z

Investigated which self-improvement metrics are robust enough to compare across different forks or deployments of openakari, using only repository sources.

Findings:
1. The current measurement plan already names five candidate self-improvement metrics: Gap Detection Rate, Closure Rate, Improvement Effectiveness, Human Intervention Rate, and System-Learning Rate.
   - Provenance: `projects/akari/plans/self-improvement-measurement.md`.
2. Human Intervention Rate is the strongest current cross-fork metric because this fork already defines both a machine-countable denominator (`sessions`) and a concrete intervention-event source (`APPROVAL_QUEUE.md` requests tied to session evidence).
   - Provenance: `projects/akari/plans/self-improvement-measurement.md`; `projects/akari/analysis/human-intervention-rate-2026-03-23.md`.
3. Gap Detection Rate, Closure Rate, and System-Learning Rate are potentially comparable across forks if they are counted from explicit artifact classes such as diagnosis files, linked fixes/tasks, decision records, skill updates, or infrastructure changes, rather than narrative descriptions.
   - Provenance: `projects/akari/plans/self-improvement-measurement.md`; `projects/akari/diagnosis/self-observation-examples.md`.
4. Improvement Effectiveness is only weakly comparable today because ADR 0052 requires explicit denominators and filtering conditions for cross-context metric comparison, but this project does not yet define a standard before/after schema for self-improvement interventions.
   - Provenance: `decisions/0052-metric-comparison-standardization.md`; `projects/akari/plans/self-improvement-measurement.md`.
5. Findings-per-dollar is not yet a robust cross-fork metric in this repo even though it is a design principle, because the principle is stated normatively but this fork does not yet define a mechanical counting rule for `findings` or a standardized cost ledger for all sessions.
   - Provenance: `AGENTS.md`; absence of any repository files operationalizing `findings per dollar` or related counting rules in this session's repository searches.

Provisional answer: the most robust cross-fork comparison set is a normalized event metric family grounded in mechanical repo artifacts — first `Human Intervention Rate`, then `Gap Detection Rate`, `Closure Rate`, and `System-Learning Rate` once artifact classes and linking rules are standardized. `Improvement Effectiveness` and `findings-per-dollar` are important, but they are not yet robust for cross-fork comparison in this deployment.

More research needed: define a fork-invariant event schema for gaps, fixes, interventions, and system-level improvements; define required denominators and filters for each metric; and add one throughput/knowledge-output companion metric so forks cannot appear better merely by escalating less.

## Open questions

- What is the smallest useful amount of operational logging needed to support real self-study without overwhelming orient cost?
- Which kinds of capability improvements transfer across projects, and which depend on the specific repo's history and conventions?
- Should this deployment standardize on `APPROVAL_QUEUE.md` requests, resolved approvals, or both as the canonical intervention-event source for future autonomy comparisons?
- What is the smallest fork-invariant event schema that would let `Human Intervention Rate`, `Gap Detection Rate`, `Closure Rate`, and `System-Learning Rate` be recomputed mechanically across deployments?
