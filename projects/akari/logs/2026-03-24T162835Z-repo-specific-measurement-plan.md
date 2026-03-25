# Session Log — akari repo-specific measurement plan

- Timestamp: 2026-03-24T16:28:35Z
- Project: `projects/akari`
- Task: `projects/akari/TASKS.md` — Adapt the self-improvement measurement plan to your own repo
- Classification: ROUTINE
- Status: complete

## Summary

Converted the example self-improvement measurement plan into a repo-specific plan for this public fork. The updated plan now names five concrete metrics, binds each to explicit formulas and artifact classes, and records which metrics remain deferred because the current repo still lacks standardized counting rules.

## Findings

1. This fork already had enough durable evidence to define a repo-specific measurement plan without external research: per-session JSON records, approval-queue events, local self-improvement examples, and fleet benchmark documentation are all present in-repo.
   - Provenance: `logs/sessions/session-20260323-120013-60cedbe2.json`; `logs/sessions/session-20260323-160117-0eb0dceb.json`; `logs/sessions/session-20260323-161007-0e17eb63.json`; `APPROVAL_QUEUE.md`; `projects/akari/analysis/local-self-improvement-loop-example.md`; `docs/fleet-research.md`.

2. The strongest immediately measurable metric in this fork remains Approval-Queue Intervention Rate because it already has a stable denominator (`logs/sessions/session-*.json`) and an explicit intervention-event source (`APPROVAL_QUEUE.md`).
   - Provenance: `projects/akari/plans/self-improvement-measurement.md`; `projects/akari/analysis/human-intervention-rate-2026-03-23.md`.

3. The new repo-specific plan defines five metrics for this fork: Approval-Queue Intervention Rate, Knowledge-Producing Session Rate, Gap-to-Action Closure Rate, Measured Improvement Effectiveness, and System-Learning Embed Rate.
   - Provenance: `projects/akari/plans/self-improvement-measurement.md`.

4. Findings-per-dollar is still deferred rather than operationalized because the repo has not yet defined a mechanical counting rule for `findings` or a stable cost ledger that covers session work.
   - Provenance: `AGENTS.md`; `projects/akari/plans/self-improvement-measurement.md`; `projects/akari/logs/2026-03-24T034144Z-cross-fork-metrics.md`.

5. Three immediate standardization gaps remain before these metrics can be recomputed consistently at larger scale: a mechanical classifier for `knowledge-producing sessions`, a canonical intervention-event source definition, and a lightweight before/after schema for self-improvement claims.
   - Provenance: `projects/akari/plans/self-improvement-measurement.md`.

## Files changed

- `projects/akari/plans/self-improvement-measurement.md`
- `projects/akari/TASKS.md`
- `projects/akari/README.md`
- `projects/akari/logs/2026-03-24T162835Z-repo-specific-measurement-plan.md`

## Notes

Attempting the required git commit remains blocked by current shell policy. Prior approval-queue records show repeated `git add` / `git commit` attempts are denied by the shell denylist with a false-positive `dd` match, so this session recorded the completed work in repo files but could not finalize it as a commit.
