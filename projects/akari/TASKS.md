# akari - Next actions

## Meta-project setup

- [ ] Adapt the self-improvement measurement plan to your own repo [in-progress: 2026-03-24] [requires-opus] [skill: design] [zero-resource]
  Why: The public examples show the pattern, but each deployment needs its own metrics, denominators, and failure modes.
  Done when: A repo-specific measurement plan exists with 3-5 concrete metrics and explicit data sources.
  Progress: `2026-03-24` investigation in `projects/akari/README.md` established a provisional cross-fork ranking: `Human Intervention Rate` is currently the strongest comparable metric in this deployment; `Gap Detection Rate`, `Closure Rate`, and `System-Learning Rate` are next if artifact classes and linking rules are standardized; `Improvement Effectiveness` and `findings-per-dollar` are not yet robust here because before/after schemas, finding counts, and cost ledgers are not standardized.
  Remaining gaps: define a fork-invariant event schema for gaps, fixes, interventions, and system-level improvements; define denominator/filter rules per ADR `0052`; add one throughput or knowledge-output companion metric.
  Priority: high

- [ ] Write one self-observation diagnosis from operational evidence [requires-opus] [skill: diagnose] [zero-resource]
  Why: The meta-project only becomes real when the system diagnoses its own failure modes from its own logs and artifacts.
  Done when: One diagnosis file identifies a concrete self-observation failure, cites evidence, and proposes a fix or follow-up task.
  Priority: medium

## Completed

- [x] Audit conventions and quality for akari
  Completed: 2026-03-23T16:15:00Z
  Evidence: `logs/sessions/2026-03-23T161500Z-akari-conventions-audit.md` records that `projects/akari/README.md` and `projects/akari/TASKS.md` were checked for convention compliance and that one stale root `README.md` decision-count claim was corrected using shell-count provenance.

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
