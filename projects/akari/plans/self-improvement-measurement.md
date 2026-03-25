# Repo-Specific Self-Improvement Measurement Plan

Date: 2026-03-24
Project: akari
Type: measurement plan
Status: active

## Goal

Define a measurement plan for this fork that can be recomputed from repository artifacts already present in the public repo. The plan should prefer mechanical counts over narrative judgment, make denominators explicit, and stay compatible with the minimum-logging bundle already observed in this deployment.

## Scope and constraints

This plan is fork-specific rather than a generic example.

Design constraints already established in-repo:

1. The smallest useful logging bundle in this fork is: per-session JSON records, explicit intervention/escalation records, durable repo-state outcome records, and provenance strong enough to recompute numerical claims.
   - Provenance: `projects/akari/logs/2026-03-23T163541Z-minimum-operational-logging.md`; `projects/akari/README.md` entry at `2026-03-24T03:45:00Z`.

2. The strongest current cross-fork candidates are metrics with stable denominators and explicit artifact classes, especially approval events per session and benchmark-style session outcomes.
   - Provenance: `projects/akari/logs/2026-03-24T034144Z-cross-fork-metrics.md`; `docs/fleet-research.md`.

3. Comparisons must state denominators and filtering conditions explicitly.
   - Provenance: `decisions/0052-metric-comparison-standardization.md`.

4. README orient cost must stay bounded, so the measurement plan should read mostly from dedicated artifacts rather than requiring verbose README logs.
   - Provenance: `decisions/0066-log-retention-count-based.md`.

## Measurement cadence

- **Bootstrap cadence:** recompute after every meaningful increase in local session count.
- **Steady-state cadence:** weekly rolling window once session volume is high enough for windowed comparison.
- **Comparison rule:** do not claim trend improvement from a single tiny sample; use repeated windows with the same denominator/filter definitions.

## Metrics

### M1. Approval-Queue Intervention Rate

**Question:** How often does a session require explicit human governance escalation?

**Formula:**

`included_approval_queue_events / session_json_records`

**Current counting rule in this fork:**
- Count intervention events from `APPROVAL_QUEUE.md` when they correspond to a real session blocker or governance escalation.
- Exclude obvious smoke tests or non-operational entries.
- Count sessions from `logs/sessions/session-*.json`.
- When reporting, state the time window and any exclusions.

**Primary data sources:**
- `APPROVAL_QUEUE.md`
- `logs/sessions/session-*.json`

**Why this metric is included:**
This repo already demonstrated a mechanical baseline for this metric using those exact files.
- Provenance: `projects/akari/analysis/human-intervention-rate-2026-03-23.md`.

**Known failure mode:**
Requests and resolutions are not the same event type; future comparisons must declare whether the metric uses pending requests, resolved decisions, or both.
- Provenance: `projects/akari/README.md` open question on canonical intervention-event source.

### M2. Knowledge-Producing Session Rate

**Question:** What fraction of sessions leave behind durable knowledge artifacts rather than only attempted work?

**Formula:**

`knowledge_producing_sessions / session_json_records`

**Provisional counting rule for this fork:**
A session counts as knowledge-producing if it produces at least one durable artifact that adds reusable repo knowledge, such as:
- a project analysis file;
- a diagnosis file;
- a literature note;
- a decision record;
- a README log entry that records a new finding with provenance;
- a task-state change that isolates blocked vs usable work and is later reusable.

**Primary data sources:**
- `logs/sessions/session-*.json`
- project-local artifacts under `projects/*/analysis/`, `projects/*/diagnosis/`, `projects/*/literature/`, `decisions/`
- project `README.md` log entries and `TASKS.md` state changes when they encode the durable result

**Why this metric is included:**
Fleet benchmark documentation now treats knowledge-producing-session rate as a core autonomy measure, and this fork already has at least one local example of durable reuse after a task-state change.
- Provenance: `docs/fleet-research.md`; `projects/akari/analysis/local-self-improvement-loop-example.md`.

**Known failure mode:**
This fork does not yet have a fully mechanical classifier script for the `knowledge-producing` label, so every report must state the artifact classes used.
- Provenance: `projects/akari/literature/2026-03-24-fleet-scale-autonomy-benchmarks.md`.

### M3. Gap-to-Action Closure Rate

**Question:** When the system detects a self-observation gap, how often does that gap lead to a concrete fix or follow-up task?

**Formula:**

`gap_artifacts_with_linked_fix_or_followup / total_gap_artifacts`

**Counting rule for this fork:**
Count a gap artifact when a diagnosis, audit, blocker log, or self-observation note identifies a concrete operational failure, contradiction, or missing prerequisite. Count it as closed when the artifact is linked to at least one of:
- an implemented file change,
- a completed follow-up task,
- a newly created blocked/unblocked task split,
- or an approval request that cleanly externalizes the blocker.

**Primary data sources:**
- `projects/akari/diagnosis/`
- `projects/akari/audits/`
- `logs/sessions/*.md`
- project `TASKS.md`
- `APPROVAL_QUEUE.md`

**Why this metric is included:**
The local repo already contains concrete cases where an identified operational gap changed task structure or created an approval escalation instead of being left implicit.
- Provenance: `projects/akari/analysis/local-self-improvement-loop-example.md`; `logs/sessions/2026-03-23T160340Z-caption-pilot-blocked.md`.

**Known failure mode:**
Narrative prose can overstate linkage. Reports must cite the exact downstream task/file proving closure.
- Provenance: `projects/akari/diagnosis/self-observation-examples.md`.

### M4. Measured Improvement Effectiveness

**Question:** When this fork implements a self-improvement change, how often is a before/after effect actually measured rather than merely asserted?

**Formula:**

`self_improvement_changes_with_explicit_before_after_measurement / total_self_improvement_changes_claimed`

**Counting rule for this fork:**
A claimed self-improvement change enters the denominator when a session asserts that a convention, infrastructure change, task decomposition, or measurement update improved the system itself. It enters the numerator only when the artifact also cites:
- a before state,
- an after state,
- and a metric or count proving the delta.

**Primary data sources:**
- `projects/akari/analysis/`
- `projects/akari/logs/`
- `projects/akari/README.md`
- relevant project `TASKS.md` / README files that provide before/after evidence

**Why this metric is included:**
This directly measures whether the meta-project is doing real empirical self-improvement rather than producing unverified anecdotes.
- Provenance: `projects/akari/plans/self-improvement-measurement.md` (prior example metric); `decisions/0052-metric-comparison-standardization.md`.

**Known failure mode:**
This metric is stricter than ordinary success reporting, so early values may be low until the repo standardizes before/after schemas.
- Provenance: `projects/akari/logs/2026-03-24T034144Z-cross-fork-metrics.md`.

### M5. System-Learning Embed Rate

**Question:** How often do sessions push operational learning back into durable system structure?

**Formula:**

`system_level_learning_artifacts / session_json_records`

**Counted artifact classes in this fork:**
- new or updated decision records in `decisions/`
- updates to `AGENTS.md`
- updates to `skills/`
- akari diagnosis/pattern/plan artifacts that change how future sessions should reason
- task decompositions or convention fixes that explicitly alter future routing or evidence practices

**Primary data sources:**
- `decisions/`
- `AGENTS.md`
- `skills/`
- `projects/akari/patterns/`
- `projects/akari/diagnosis/`
- `projects/akari/plans/`
- `projects/*/TASKS.md` when task-state changes encode a reusable operating rule

**Why this metric is included:**
The meta-project is about whether operations get embedded into the system. This metric captures that directly.
- Provenance: `projects/akari/patterns/repo-as-cognitive-state.md`; `projects/akari/patterns/inline-logging.md`.

**Known failure mode:**
Some file changes are structural but not genuinely learning-related, so reports must specify which artifact classes are included.

## Metrics intentionally deferred

### Findings per dollar

This remains a core design principle, but it is not yet included as a measured repo-specific metric because this fork does not yet define a mechanical counting rule for `findings` or a stable cost ledger that covers all session work.
- Provenance: `AGENTS.md`; `projects/akari/logs/2026-03-24T034144Z-cross-fork-metrics.md`.

### Raw task completion rate

This is useful operationally but not sufficient for the meta-project because a session can complete mechanical work without producing reusable system learning.
- Provenance: synthesis from `projects/akari/plans/self-improvement-measurement.md` and `docs/fleet-research.md`.

## Reporting template

Every future metric report in this project should include:

1. time window;
2. exact denominator source;
3. inclusion/exclusion rules;
4. any artifact classes used as proxies;
5. inline arithmetic or script path for each numerical claim;
6. caveats when sample size is too small for trend claims.

## Immediate next implementation needs

1. Define a mechanical classifier for `knowledge-producing sessions` in this fork.
2. Standardize whether intervention rate uses approval requests, resolved approvals, or both.
3. Add a lightweight schema for before/after self-improvement claims so M4 can be counted consistently.
4. Once session volume increases, recompute M1-M5 on a fixed weekly window rather than ad hoc snapshots.
