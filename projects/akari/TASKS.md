# akari - Next actions

## Meta-project setup

- [x] Adapt the self-improvement measurement plan to your own repo [requires-opus] [skill: design] [zero-resource]
  Why: The public examples show the pattern, but each deployment needs its own metrics, denominators, and failure modes.
  Completed: 2026-03-24T16:28:35Z
  Evidence: `projects/akari/plans/self-improvement-measurement.md` now defines five repo-specific metrics — Approval-Queue Intervention Rate, Knowledge-Producing Session Rate, Gap-to-Action Closure Rate, Measured Improvement Effectiveness, and System-Learning Embed Rate — with explicit formulas, artifact-class counting rules, and primary data sources (`APPROVAL_QUEUE.md`, `logs/sessions/session-*.json`, and durable project artifacts). The plan also records one deferred metric, findings-per-dollar, because this fork still lacks a mechanical counting rule for findings and a stable cost ledger.

- [ ] Write one self-observation diagnosis from operational evidence [requires-opus] [skill: diagnose] [zero-resource]
  Why: The meta-project only becomes real when the system diagnoses its own failure modes from its own logs and artifacts.
  Done when: One diagnosis file identifies a concrete self-observation failure, cites evidence, and proposes a fix or follow-up task.
  Priority: medium

## Completed

- [x] Audit conventions and quality for akari
  Completed: 2026-03-23T16:15:00Z
  Evidence: `projects/akari/audits/2026-03-23-conventions-audit.md` records that `projects/akari/README.md` and `projects/akari/TASKS.md` were checked for convention compliance and that the root `README.md` decision-count claim was identified as stale via `run_shell("find decisions -maxdepth 1 -type f | wc -l") = 68`; the repository summary count was corrected in `README.md` on 2026-03-24.

- [x] Measure human intervention rate in your deployment [fleet-eligible] [skill: analyze] [zero-resource]
  Why: A decreasing intervention rate is one of the clearest signals that the system is becoming more autonomous.
  Completed: 2026-03-23T16:35:35Z
  Evidence: `projects/akari/analysis/human-intervention-rate-2026-03-23.md` computes intervention events per session across two UTC windows using `APPROVAL_QUEUE.md` and the three `logs/sessions/session-*.json` records; rates are `0 / 1 = 0.00` for `2026-03-23 12:00-12:59` and `1 / 2 = 0.50` for `2026-03-23 16:00-16:59`.
  Priority: medium

- [x] Add one local example of a successful self-improvement loop [fleet-eligible] [skill: record] [zero-resource]
  Why: The strongest evidence for the meta-project is a full loop: detect a gap, change the system, then measure improvement.
  Completed: 2026-03-23T16:35:30Z
  Evidence: `projects/akari/analysis/local-self-improvement-loop-example.md` records a local before/after loop where the multi-agent survey project split a coupled NeurIPS 2024-2025 retrieval task after observing `138` 2024 candidates and `0` 2025 candidates, then reused the unblocked 2024 artifact in a later README knowledge increment `17 minutes 19 seconds` later.
  Priority: medium
