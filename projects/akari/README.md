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
4. The stale root README count was identified and documented for correction.
   - Provenance: updated audit record `projects/akari/audits/2026-03-23-conventions-audit.md` and follow-up audit log `projects/akari/logs/2026-03-24T034245Z-akari-conventions-followup-audit.md`.

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

### 2026-03-23T17:20:00Z

Investigated which capability improvements appear to transfer across projects versus which depend on repo-specific history and conventions.

Findings:
1. The most portable improvements are the ones that create more mechanical ground truth for stateless agents: structured records, explicit before/after verification, and machine-countable operational artifacts.
   - Provenance: `projects/akari/diagnosis/self-observation-examples.md`; `projects/akari/patterns/structured-work-records.md`.
2. State-handoff improvements also appear broadly transferable because they address general statelessness problems rather than one project's topic area: repo-as-cognitive-state, inline logging, and explicit task decomposition into usable versus blocked work.
   - Provenance: `projects/akari/patterns/repo-as-cognitive-state.md`; `projects/akari/patterns/inline-logging.md`; `projects/akari/analysis/local-self-improvement-loop-example.md`.
3. Improvements are less transferable when they depend on local semantics: exact file destinations, archival thresholds, task taxonomies, approval conventions, and the contents of a repo's skill library all rely on accumulated repo history and established conventions.
   - Provenance: `projects/akari/patterns/repo-as-cognitive-state.md`; `projects/akari/patterns/skills-architecture.md`.
4. A practical split is: transferable improvements mostly upgrade the form of coordination and evidence; repo-specific improvements mostly encode local judgment about where knowledge belongs and how this repo names, counts, and routes work.
   - Provenance: synthesis from the sources above.

Provisional answer: improvements that reduce ambiguity by adding structure, provenance, and reusable blocked/unblocked workflow patterns are the best cross-project candidates. Improvements that encode a particular repo's vocabulary, thresholds, skills, and counting rules should be treated as fork-local until validated elsewhere.

Further research needed: the repo does not yet contain a controlled comparison across multiple forks using shared counting rules, so transferability is still argued from design-pattern evidence rather than demonstrated by cross-deployment measurement. The next internal step is to compare at least two deployments with the same definitions for intervention events, gap artifacts, and system-level improvements.

### 2026-03-24T03:45:00Z

Investigated the smallest useful amount of operational logging needed for real self-study without overwhelming orient cost.

Findings:
1. The repo already shows that some self-study metrics do not require verbose prose logs: human-intervention rate was computed from only session counts in `logs/sessions/session-*.json` plus explicit escalation records in `APPROVAL_QUEUE.md`.
   - Provenance: `projects/akari/analysis/human-intervention-rate-2026-03-23.md`; `logs/sessions/session-20260323-120013-60cedbe2.json`; `logs/sessions/session-20260323-160117-0eb0dceb.json`; `logs/sessions/session-20260323-161007-0e17eb63.json`; `APPROVAL_QUEUE.md`.
2. The local self-improvement-loop example shows that a second minimal logging requirement is one durable repo-state change that links a detected gap to a changed task/artifact state and a later reuse event.
   - Provenance: `projects/akari/analysis/local-self-improvement-loop-example.md`; `projects/multi-agent-survey/TASKS.md`; `projects/multi-agent-survey/README.md`; `logs/sessions/2026-03-23T161441Z-neurips-2024-harvest.md`.
3. Repo guidance explicitly prefers mechanical ground truth over narrative claims for self-observation.
   - Provenance: `projects/akari/diagnosis/self-observation-examples.md`; `decisions/0004-inline-logging.md`.
4. Orient cost is intentionally bounded by keeping only the 5 most recent README log entries, with older detail archived elsewhere.
   - Provenance: `decisions/0066-log-retention-count-based.md`.

Provisional answer: the smallest useful logging bundle is not a full prose diary. It is:
- one machine-readable per-session record with stable identifiers and timestamps;
- one explicit record of human intervention/escalation events when they occur;
- one durable repo-state record of outcome when a session discovers a gap or changes operating state (for example, task-state updates, a README finding, or a diagnosis artifact);
- provenance strong enough to recompute any numerical claim from files or inline arithmetic.

This appears sufficient to support at least three kinds of self-study already demonstrated in-repo: intervention-rate measurement, gap->change->reuse loop reconstruction, and convention/quality audits. Anything substantially less would lose either the denominator (`sessions`), the explicit intervention signal, or the before/after state change needed to study improvement. Anything substantially more should be treated as optional detail and archived out of the README path to avoid raising orient cost.

Further research needed: this answer is still based on a very small local sample. The next internal test is to check whether the same minimal bundle still supports self-study once session volume is much higher, especially whether session JSON + approval records + task/README deltas remain enough without also logging standardized touched-file lists or explicit outcome tags.

### 2026-03-24T13:18:35Z

Ran a horizon scan for new developments related to studying and improving the autonomous research system itself.

Findings:
1. `projects/akari/literature/` already covered remote-channel observability and scheduler evaluation telemetry, but not fleet-scale benchmark reporting.
   - Provenance: `projects/akari/literature/2026-03-23-remote-channel-observability.md`; `projects/akari/literature/2026-03-23-scheduler-evaluation-telemetry.md`.
2. `docs/fleet-research.md` now exposes a fleet-scale empirical benchmark surface with `5,303` sessions, `91.0% (4,825/5,303)` overall success, and `54.2% (2,876/5,303)` knowledge-producing sessions.
   - Provenance: `docs/fleet-research.md`, section `Evidence: sustained autonomous operation`.
3. The same document reports category-level output counts and an explicit-governance baseline of `12 / 1,529 = 0.0079` approval events per session for the week of `2026-03-02`.
   - Provenance: `docs/fleet-research.md`, sections `Evidence: sustained autonomous operation` and `Evidence: scarce human intervention`; inline arithmetic `12 / 1529 = 0.007848...`, rounded to `0.0079`.
4. The document's reproduction checklist identifies a candidate cross-fork benchmark bundle: success rate, knowledge-producing-session rate, output counts by category, and approval events per session.
   - Provenance: `docs/fleet-research.md`, section `How to reproduce this kind of evidence in your system`.

Interpretation: this is a genuinely new self-study direction for akari because it shifts from isolated telemetry surfaces to a fork-comparison benchmark frame. The main remaining gap is that this public fork still lacks a fully mechanical classifier for `knowledge-producing sessions`, so benchmark portability depends on standardizing those definitions.

### 2026-03-24T13:41:13Z

Re-audited akari conventions and fixed one real stale contradiction.

Findings:
1. `projects/akari/README.md` still follows the expected project README structure and `projects/akari/TASKS.md` open-task formatting remains internally consistent.
   - Provenance: direct reads of `projects/akari/README.md` and `projects/akari/TASKS.md` in this session.
2. Root `README.md` still claimed `decisions/` contained `67 architectural decision records`, but shell count returned `68` files.
   - Provenance: direct read of root `README.md`; `run_shell("find decisions -maxdepth 1 -type f | wc -l")` returned `68`.
3. No additional stale or contradictory information was found in the audited akari project files.
   - Provenance: comparison of `projects/akari/README.md`, `projects/akari/TASKS.md`, and prior akari audit artifacts.
4. The root README decision-count claim was corrected in place from `67` to `68`.
   - Provenance: updated root `README.md` in this session.

## Open questions

- Which self-improvement metrics are robust enough to compare across different forks or deployments of openakari?
- What is the smallest useful amount of operational logging needed to support real self-study without overwhelming orient cost?
- Which kinds of capability improvements transfer across projects, and which depend on the specific repo's history and conventions?
- Should this deployment standardize on `APPROVAL_QUEUE.md` requests, resolved approvals, or both as the canonical intervention-event source for future autonomy comparisons?
