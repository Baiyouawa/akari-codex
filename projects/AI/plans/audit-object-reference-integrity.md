# Audit object/reference integrity around tables, figures, formulas, and surrounding prose

Generated: 2026-03-27

## Goal Description
Audit `projects/AI/main.tex` to verify that all tables, figures, formulas, and their surrounding reference sentences remain intact during prose rewriting. The task focuses on object identity, numbering, surrounding references, captions, labels, refs, and cites. If any wording adjustment is needed, only surrounding prose may be edited; object bodies and LaTeX structural commands must remain untouched.

## Acceptance Criteria
- AC-1: Every table, figure, and other object block in `projects/AI/main.tex` is inventoried with line-level provenance, and the audit confirms whether the object body changed.
  - Positive check: each `table` and `figure` environment is listed with its start line, caption line when present, and nearby prose references.
  - Negative check: any object is omitted or its body is edited without being called out.
- AC-2: Object-body integrity is preserved.
  - Positive check: no edits are made inside `table`, `figure`, `tabular`, `tabularx`, `includegraphics`, or `caption{...}` blocks for this task.
  - Negative check: captions, image paths, table contents, environment types, or internal formatting are modified.
- AC-3: Cross-reference language remains correct.
  - Positive check: surrounding prose still points to the same object type and number (for example, Figure~1 stays Figure~1, Table~1 stays Table~1).
  - Negative check: a sentence changes an object type, number, or conclusion.
- AC-4: The audit explicitly records the current state of `label`, `ref`, `eqref`, `autoref`, and `cite` usage with provenance.
  - Positive check: counts and presence/absence are documented from direct file inspection.
  - Negative check: the summary asserts reference-command integrity without stating whether those commands exist.
- AC-5: RLCR artifacts are written under `projects/AI/plans/`, and task/session state is persisted in-repo.
  - Positive check: progress, self-review, and summary files exist; `projects/AI/TASKS.md` and a session log are updated.
  - Negative check: work is only described in chat.

## Path Boundaries
### Upper Bound (most complete)
Produce a full object inventory, verify all nearby reference sentences, make any needed prose-only corrections outside object bodies, document reference-command usage, and persist progress/self-review/summary/session log updates.

### Lower Bound (minimum viable)
Confirm by direct inspection that all object blocks and nearby prose remain intact, document the findings with provenance, and update task/session records without changing object bodies.

## Milestones
1. Inspect `projects/AI/main.tex` and build an object/reference inventory.
2. Apply any needed prose-only fixes outside object bodies.
3. Write progress note, self-review, final summary, and update project task/session records.

## Plan Evolution Log
- 2026-03-27: Created a dedicated plan file for the object/reference integrity audit because the assignment required a task-specific plan under `projects/AI/plans/`.
