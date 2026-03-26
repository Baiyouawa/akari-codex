# Rewrite main.tex into more natural academic prose

## Goal Description
Revise the prose in `projects/AI/main.tex` so that it reads more like natural human academic writing while preserving the original meaning, terminology, logical structure, sectioning, and LaTeX structure. The task covers continuous prose, table wording, captions, and reflective narrative text, but must not alter the document's analytical claims, UML logic, bibliography entries, or overall document architecture.

## Acceptance Criteria
- AC-1: `projects/AI/main.tex` remains a valid LaTeX document with the same section/subsection structure, figures, tables, bibliography, and core formatting commands preserved.
  - Positive check: the file still contains the same major LaTeX blocks such as `\section{Introduction}`, `\subsection{The Design of Functional Requirements with Use Case Diagrams}`, `\subsection{The Design of Functional Behaviour with Activity Diagrams}`, the bibliography environment, and the appendix sections.
  - Negative check: no sections, figures, tables, or bibliography blocks are removed or reordered.
- AC-2: The prose is substantively rewritten at sentence and paragraph level to sound more like human academic writing, while preserving original meaning, terminology, and argument flow.
  - Positive check: wording, syntax, transitions, and paragraph rhythm differ from the source across the document.
  - Negative check: no technical meaning is changed; no new claims, citations, or domain scope are introduced.
- AC-3: Key domain terms and UML semantics are preserved exactly where needed for correctness.
  - Positive check: terms such as Amazon enterprise online POS system, OOAD, UML, `\texttt{<<include>>}`, `\texttt{<<extend>>}`, PCI DSS, WCAG~2.1, GDPR, MFA, and actor/use-case names remain consistent with the original model.
  - Negative check: no actor names, use-case names, or cited standards are renamed inconsistently.
- AC-4: The RLCR work products are written under `projects/AI/plans/` and include a progress note, self-review, and final summary with explicit evidence against the ACs.
  - Positive check: `projects/AI/plans/` contains the plan file, at least one progress file, a self-review file, and a summary file.
  - Negative check: work is not left undocumented.
- AC-5: Task state and session record are persisted in-repo.
  - Positive check: a project `TASKS.md` reflects the task completion state, and a session log file records what changed with provenance.
  - Negative check: no completion claim is made only in chat.

## Path Boundaries
### Upper Bound (most complete)
Rewrite the full prose of `main.tex`, including title-page descriptive text, main body paragraphs, table wording, recommendation text, and individual reflections, while preserving all LaTeX scaffolding and factual content.

### Lower Bound (minimum viable)
Rewrite the main report prose in the Introduction, Section 2 subsections, and Conclusions/Recommendations, with all RLCR artifacts and task/session records completed.

## Milestones
1. Establish project records: create plan file, inspect current file set, and create project task tracking if missing.
2. Rewrite `projects/AI/main.tex` while preserving structure and meaning.
3. Write progress note, perform self-review, fix any P0/P1 issues, and write final summary and session log.

## Plan Evolution Log
- 2026-03-24: Initial plan created because no existing plan file was present in `projects/AI/plans/`.