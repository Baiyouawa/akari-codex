# Session Log — akari metric comparison investigation

- Timestamp: 2026-03-23T17:00:00Z
- Project: `projects/akari`
- Task: Investigate which self-improvement metrics are robust enough to compare across different forks or deployments of openakari
- Classification: ROUTINE
- Status: complete

## Summary

Reviewed the akari project artifacts and relevant decision records, then wrote a synthesized answer into `projects/akari/README.md`.

## Findings

1. The existing measurement plan already proposes five candidate self-improvement metrics: Gap Detection Rate, Closure Rate, Improvement Effectiveness, Human Intervention Rate, and System-Learning Rate.
   - Provenance: `projects/akari/plans/self-improvement-measurement.md`

2. Human Intervention Rate is the strongest current cross-fork candidate because it has a stable session-level denominator and can be grounded in explicit intervention events such as approvals or recovery actions.
   - Provenance: `projects/akari/plans/self-improvement-measurement.md`
   - Provenance: `projects/akari/analysis/human-intervention-rate-example.md`

3. Gap Detection Rate and Closure Rate are also plausible cross-fork metrics, but only if gap artifacts and gap→fix links are defined mechanically rather than narratively.
   - Provenance: `projects/akari/plans/self-improvement-measurement.md`
   - Provenance: `projects/akari/diagnosis/self-observation-examples.md`

4. Cross-fork comparisons are fragile unless denominators and filtering conditions are made explicit.
   - Provenance: `decisions/0052-metric-comparison-standardization.md`

5. This fork does not yet define a standardized counting rule for findings or cost, so findings-per-dollar is not yet a robust cross-fork comparison metric even though it is a core design principle.
   - Provenance: `AGENTS.md`
   - Provenance: search for metric operationalizations of findings-per-dollar and related terms returned no matches in repository files during this session.

## Changes made

- Updated `projects/akari/README.md` with a synthesized answer and concrete next research needs.
- Updated `projects/akari/TASKS.md` to mark the measurement-plan task as in progress and record the specific standardization gaps revealed by this investigation.

## Notes

No external research was required for this pass because the repo contained enough material to provide a provisional internal answer. Remaining work is specification and standardization inside this fork, not literature review.
