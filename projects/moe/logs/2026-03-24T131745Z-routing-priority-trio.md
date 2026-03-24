# Session Log — MoE Routing Priority Trio

- Timestamp: 2026-03-24T13:17:45Z
- Project: `projects/moe`
- Task: Investigate which three papers in the current source map should be prioritized for a routing / load-balancing comparison table
- Classification: ROUTINE
- Status: complete

## Summary

Answered the first open routing question using only repository-internal evidence and recorded the result in the project README and task state so later sessions can move directly to row-level extraction instead of re-deciding source priority.

## Findings

1. The best first extraction trio is `Switch Transformers`, `BASE Layers`, and `ST-MoE`.
   - Provenance: `projects/moe/TASKS.md` names these three in the routing task’s next-step instruction; `projects/moe/literature/2026-03-24-moe-source-map.md` assigns them complementary roles of routing simplification, balancing alternative, and stability-oriented refinement.
2. This trio gives the cleanest comparison frame inside the current repo because each source emphasizes a different primary design axis: top-1 simplified routing (`Switch Transformers`), balancing-by-assignment (`BASE Layers`), and stability intervention on sparse routing (`ST-MoE`).
   - Provenance: `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` sections for Switch-style routing, BASE-style balanced assignment, and ST-MoE-style stability refinements.
3. The repository’s survey draft had already partially resolved this question before this session by stating that these three are the strongest immediate trio for a first routing table.
   - Provenance: `projects/moe/plans/moe-survey-draft.md`, section `2.3 Routing implications for this project`.
4. The unresolved work after this session is not source prioritization but field extraction: the table still needs explicit row values for experts-per-token, balancing method, capacity/overflow handling, and stability intervention.
   - Provenance: updated `projects/moe/TASKS.md` in this session.

## Actions taken

1. Read `AGENTS.md`, repository `README.md`, `projects/moe/README.md`, `projects/moe/TASKS.md`, the MoE source map, the routing analysis, the survey draft, and recent MoE logs to orient.
2. Synthesized the repo-internal evidence for the first routing-table source trio.
3. Updated `projects/moe/README.md` with one dated log entry that resolves open question 1.
4. Updated `projects/moe/TASKS.md` so the remaining routing task now points to the concrete row-level extraction step.

## Verification

- Verified that `projects/moe/README.md` now records the resolved source-priority answer and removes that item from `## Open questions`.
- Verified that `projects/moe/TASKS.md` now contains a more concrete next step for the routing task.

## Notes

No external research was needed for this question because the repository already contained a source map, routing analysis, and survey draft that converged on the same three-paper priority set.
