# Scheduler evaluation telemetry as a new self-study surface

Date: 2026-03-23
Project: akari
Type: internal-development note
Verified: 2026-03-23

## Why this is new

Existing akari self-study artifacts emphasize examples of intervention rate, self-observation failures, and a local self-improvement loop. They do not yet capture that the current repo now specifies a structured scheduler-metrics surface for ongoing evaluation of session efficiency and fleet output quality.

## Verified developments

1. The current `orient` skill instructs sessions to read `.scheduler/metrics/sessions.jsonl` and compute concrete efficiency metrics over recent sessions.
   - Provenance: `skills/orient/SKILL.md` sections `Fast orient` step 4 and `Full orient` step 10.

2. Those metrics include findings per dollar, genuine waste rate, orient overhead, average cost per session, and average turns.
   - Provenance: `skills/orient/SKILL.md` metric lists under `Fast orient` and `Full orient`.

3. The same skill now defines fleet-specific evaluation metrics when cost-based measures do not apply: task completion rate, verification pass rate, log entry rate, and knowledge production rate.
   - Provenance: `skills/orient/SKILL.md` fleet-worker metric lists under `Fast orient` and `Full orient`.

4. The current `compound` skill adds a fleet-output audit that checks recent fleet sessions for verification properties such as `hasCommit`, `hasLogEntry`, `ledgerConsistent`, and L2-violation counts, with pass-rate thresholds and follow-up recommendations.
   - Provenance: `skills/compound/SKILL.md` section `Step 9: Fleet output audit (full/deep only)`.

5. The akari skills-architecture pattern still states that L4 evaluation is underrepresented and that there is no systematic measurement of skill effectiveness or usage.
   - Provenance: `projects/akari/patterns/skills-architecture.md` section `CI layer analysis`, paragraph beginning `A notable gap: L4 (Evaluation) is underrepresented.`

## Why it matters for self-improvement

This means the repo has moved beyond a purely conceptual evaluation gap. It now contains explicit instructions for collecting comparable session-level and fleet-level operational metrics from one shared telemetry file.

That creates at least three research directions not yet captured in akari literature notes:

- **Metric operationalization drift**: whether different forks actually compute the same efficiency metrics from `.scheduler/metrics/sessions.jsonl` the same way.
- **Fleet-quality comparability**: whether verification pass rate and knowledge-production rate are better cross-deployment autonomy metrics than raw cost-based measures.
- **Evaluation-surface completeness**: whether the current scheduler metrics are enough to close the L4 evaluation gap, or whether skill-invocation and skill-effectiveness telemetry is still missing.

## Limits

The documented telemetry focuses on session and fleet outcomes, not direct skill-usage measurement.
- Provenance: `skills/orient/SKILL.md` and `skills/compound/SKILL.md` define session/fleet metrics, while `projects/akari/patterns/skills-architecture.md` explicitly says there is no tracking of which skills are invoked, how often, or whether skill outputs are acted upon.

## Implication

For akari's open question about robust self-improvement metrics across forks, the most immediate new comparison target may be the scheduler-metrics schema plus fleet verification fields, not only README-level narrative artifacts. But the system still lacks direct telemetry for measuring whether skills themselves improve outcomes.