# Session Log — akari minimum operational logging investigation

- Timestamp: 2026-03-23T16:35:41Z
- Task: Investigate smallest useful operational logging for `projects/akari`
- Classification: ROUTINE
- Status: complete

## Summary

Investigated the minimum operational logging needed to support self-study without excessive orient cost, using only repository sources. Wrote the synthesized answer into `projects/akari/README.md` and marked the investigation complete in `projects/akari/TASKS.md`.

## Findings

1. Structured session JSON already carries the minimum machine-countable fields needed for several self-study metrics.
   - Provenance: `logs/sessions/session-20260323-120013-60cedbe2.json`, `logs/sessions/session-20260323-160117-0eb0dceb.json`, `logs/sessions/session-20260323-161007-0e17eb63.json`.

2. Intervention rate can be computed from session counts plus explicit approval records, without verbose prose logs.
   - Provenance: `projects/akari/analysis/human-intervention-rate-example.md`, `APPROVAL_QUEUE.md`.

3. Repo guidance favors mechanical ground truth and immediate provenance, but README retention is intentionally tight to control orient cost.
   - Provenance: `projects/akari/diagnosis/self-observation-examples.md`, `decisions/0004-inline-logging.md`, `decisions/0066-log-retention-count-based.md`.

4. Small-sample session totals already show large growth in token footprint across sessions.
   - Provenance: token totals from the three session JSON files above.
   - Inline arithmetic: 198,073 / 83,638 ≈ 2.37; 407,080 / 83,638 ≈ 4.87.

## Files changed

- `projects/akari/README.md`
- `projects/akari/TASKS.md`
- `projects/akari/logs/2026-03-23T163541Z-minimum-operational-logging.md`

## Note

Git commit could not be performed in this environment because previous sessions established that `git add`/`git commit` are blocked by shell policy (`git_status` shows repo changes remain uncommitted; earlier `run_shell` commit attempts returned shell-policy errors).
