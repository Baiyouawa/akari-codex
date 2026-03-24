# Human intervention rate in this deployment

Date: 2026-03-23
Project: akari
Type: local analysis

## Metric definition

For this deployment snapshot, an **intervention event** is an entry in `APPROVAL_QUEUE.md` that requests human decision-making for a session. This is slightly broader than a resolved approval/denial, but it is the cleanest intervention signal currently logged in-repo because the queue records when agent work had to escalate to a human.

Excluded from the metric:
- `test-action` requested at `2026-03-23T11:51:33.185911+00:00`, because its description is `Smoke test approval queue` and it is not tied to a research session or operational blocker.
  - Provenance: `APPROVAL_QUEUE.md`.

Included in the metric:
- `tool-access` requested at `2026-03-23T16:04:42.991412+00:00`, because it records a real task escalation caused by missing tool/data access.
  - Provenance: `APPROVAL_QUEUE.md`; supporting session log `logs/sessions/2026-03-23T160340Z-caption-pilot-blocked.md`.

## Session evidence used

Observed autonomous session records in `logs/sessions/`:

1. `logs/sessions/session-20260323-120013-60cedbe2.json`
   - `timestamp`: `2026-03-23T12:03:20Z`
2. `logs/sessions/session-20260323-160117-0eb0dceb.json`
   - `timestamp`: `2026-03-23T16:04:55Z`
3. `logs/sessions/session-20260323-161007-0e17eb63.json`
   - `timestamp`: `2026-03-23T16:17:10Z`

## Windowed calculation

I used two hourly windows that cover all three recorded session JSON files.

| Window (UTC) | Sessions | Intervention events | Rate |
|---|---:|---:|---:|
| 2026-03-23 12:00-12:59 | 1 | 0 | 0.00 |
| 2026-03-23 16:00-16:59 | 2 | 1 | 0.50 |

Inline arithmetic:
- Window 1 session count = 1 (`12:03:20Z` only).
- Window 1 intervention count = 0 (no included approval-queue requests in that hour).
- Window 1 rate = `0 / 1 = 0.00`.
- Window 2 session count = 2 (`16:04:55Z`, `16:17:10Z`).
- Window 2 intervention count = 1 (`tool-access` requested at `16:04:42.991412+00:00`).
- Window 2 rate = `1 / 2 = 0.50`.

## Interpretation

In the currently logged sample, the earlier hour had no recorded human-escalation events per session, while the later hour had one intervention event across two sessions. That means the observed intervention rate increased from `0.00` to `0.50` interventions/session across these two windows.

This should be treated as a bootstrap baseline, not a trend claim, because the deployment currently has only three recorded session JSON files and one real intervention event in scope.

## Caveats

- The metric is based on **approval-queue requests**, not resolved approvals/denials, because no resolved human decisions are present in `APPROVAL_QUEUE.md` during this snapshot.
- The sample is very small: 3 sessions and 1 included intervention event.
- A low rate is only good if useful work is still being produced; this metric should later be paired with throughput or completed-task measures.
