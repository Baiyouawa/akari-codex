# Session Log — Human Intervention Rate Baseline

- Timestamp: 2026-03-23T16:35:35Z
- Project: `projects/akari`
- Task: `projects/akari/TASKS.md` — Measure human intervention rate in your deployment
- Classification: ROUTINE
- Status: complete

## Summary

Computed a local human-intervention baseline for this deployment using approval-queue requests as the intervention signal and session JSON files in `logs/sessions/` as the session denominator.

## Findings

1. Three autonomous session JSON records were available for analysis.
   - Provenance: `logs/sessions/session-20260323-120013-60cedbe2.json`, `logs/sessions/session-20260323-160117-0eb0dceb.json`, `logs/sessions/session-20260323-161007-0e17eb63.json`.

2. Only one approval-queue entry represented a real human-decision escalation during the observed session windows.
   - Provenance: `APPROVAL_QUEUE.md` includes a `tool-access` request at `2026-03-23T16:04:42.991412+00:00`; the `test-action` entry was excluded because its description is `Smoke test approval queue`.

3. Intervention events per session differed across the two analyzed windows.
   - Provenance: `projects/akari/analysis/human-intervention-rate-2026-03-23.md`.
   - Inline arithmetic: `0 / 1 = 0.00` for `2026-03-23 12:00-12:59 UTC`; `1 / 2 = 0.50` for `2026-03-23 16:00-16:59 UTC`.

## Actions taken

1. Wrote `projects/akari/analysis/human-intervention-rate-2026-03-23.md`.
2. Updated `projects/akari/TASKS.md` to mark the task complete with evidence.
3. Appended a project README log entry summarizing the baseline.
4. Wrote this project-scoped session log.

## Notes

This is a bootstrap baseline only. The sample currently covers 3 sessions and 1 included intervention event, so it is useful for future comparison but too small for strong trend claims.
