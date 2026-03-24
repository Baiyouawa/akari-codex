# Session Log — akari cross-fork self-improvement metrics investigation

- Timestamp: 2026-03-24T03:41:44Z
- Project: `projects/akari`
- Task: Investigate which self-improvement metrics are robust enough to compare across different forks or deployments of openakari
- Classification: ROUTINE
- Status: complete

## Summary

Reviewed the akari project README, task list, prior akari logs, the local human-intervention analysis, the self-improvement measurement plan, the self-observation diagnosis example, and ADR 0052 on metric comparison standardization. Wrote a provisional answer into `projects/akari/README.md` and updated `projects/akari/TASKS.md` to capture the remaining standardization work.

## Findings

1. The repo already defines five candidate self-improvement metrics: Gap Detection Rate, Closure Rate, Improvement Effectiveness, Human Intervention Rate, and System-Learning Rate.
   - Provenance: `projects/akari/plans/self-improvement-measurement.md`.

2. Human Intervention Rate is the strongest current cross-fork candidate in this deployment because it already has a stable denominator (`sessions`) and a concrete intervention-event source (`APPROVAL_QUEUE.md` requests tied to session evidence).
   - Provenance: `projects/akari/plans/self-improvement-measurement.md`; `projects/akari/analysis/human-intervention-rate-2026-03-23.md`.

3. Gap Detection Rate, Closure Rate, and System-Learning Rate are only robust across forks if counted from explicit artifact classes and links rather than narrative prose.
   - Provenance: `projects/akari/plans/self-improvement-measurement.md`; `projects/akari/diagnosis/self-observation-examples.md`.

4. Improvement Effectiveness is not yet robust for cross-fork comparison here because ADR 0052 requires explicit denominators and filtering conditions, while this project does not yet define a standard before/after schema for self-improvement interventions.
   - Provenance: `decisions/0052-metric-comparison-standardization.md`; `projects/akari/plans/self-improvement-measurement.md`.

5. Findings-per-dollar is not yet operationalized enough for cross-fork comparison in this repo.
   - Provenance: `AGENTS.md` states the principle; repository searches during this session found no file defining a mechanical counting rule for findings-per-dollar.

## Files changed

- `projects/akari/README.md`
- `projects/akari/TASKS.md`
- `projects/akari/logs/2026-03-24T034144Z-cross-fork-metrics.md`

## Notes

External research was not required for this pass because the repository contained enough material for a provisional internal answer. Remaining work is internal standardization: event schema, denominator/filter conventions, and a throughput companion metric.
