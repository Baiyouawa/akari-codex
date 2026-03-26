# Review each agent output with PUA + Humanize

Generated: 2026-03-27T00:13:43+08:00

## Goal Description
Audit each agent output related to the `projects/AI` rewrite effort using PUA + Humanize criteria. For any output that only performs superficial synonym replacement, lacks substantial rewriting, or fails to provide traceable evidence, require a strategy switch and redo. The review must include an evidence chain and modification notes for each assessed agent artifact.

## Acceptance Criteria
- AC-1: Every identifiable agent output for the `projects/AI` rewrite effort is enumerated and assessed with provenance.
  - Positive Tests: each reviewed item cites a concrete repository source such as `git log`, file path, or diff-derived evidence.
  - Negative Tests: any reviewed conclusion without a path, commit hash, or file evidence.
- AC-2: The review explicitly determines whether each output passes or fails the PUA + Humanize bar.
  - Positive Tests: each item has a pass/fail judgment tied to evidence about rewrite depth, traceability, and RLCR completeness.
  - Negative Tests: vague statements such as "needs work" without a criterion-linked reason.
- AC-3: Any failing output includes a required redo direction that changes strategy rather than asking for more of the same.
  - Positive Tests: failure notes specify what to redo, what evidence to add, and what method to change.
  - Negative Tests: a failure only says "rewrite more" or "humanize further" without method change.
- AC-4: RLCR work products for this review are written under `projects/AI/plans/`, including a progress note, self-review, and final summary.
  - Positive Tests: plan, progress, self-review, and summary files exist in `projects/AI/plans/`.
  - Negative Tests: the task is claimed complete without RLCR records.
- AC-5: Project task state and session record are updated in-repo.
  - Positive Tests: `projects/AI/TASKS.md` and `projects/AI/README.md` reflect the review work, and a dated session log file exists under `projects/AI/logs/`.
  - Negative Tests: completion exists only in chat.

## Path Boundaries
### Upper Bound (most complete)
Review every AI-project-related worker artifact, including commits, files, plan coverage, and task tracking drift across `projects/AI` and `projects/ai`, and produce a structured remediation brief.

### Lower Bound (minimum viable)
Review the agent outputs directly evidenced in git history for `projects/AI` / `projects/ai`, record pass/fail with evidence, and write RLCR artifacts plus task/session updates.

## Milestones
1. Gather evidence from project files, task files, and git history for AI-project agent outputs.
2. Write the PUA + Humanize review with pass/fail judgments and redo directions.
3. Write progress note, self-review, summary, and update project records.

## Plan Evolution Log
- 2026-03-27T00:13:43+08:00: Created because `projects/AI/plans/` had no task-specific plan for agent-output review.
