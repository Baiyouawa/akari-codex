# Session Log — MoE Horizon Scan: inference systems split evidence

- Timestamp: 2026-03-24T13:42:29Z
- Project: `projects/moe`
- Task: Horizon scan for new MoE developments already not captured in project literature
- Classification: ROUTINE
- Status: complete

## Summary

Performed a horizon scan against the current MoE literature baseline and found one genuinely new direction worth recording: recent inference/serving literature now provides direct evidence that MoE training and inference bottlenecks should be modeled separately rather than only as a shared systems bucket.

## Findings

1. The existing project literature baseline did not yet contain named serving-focused sources such as `Toward Efficient Inference for Mixture of Experts` or `MegaScale-Infer`.
   - Provenance: direct read of `projects/moe/literature/2026-03-24-moe-source-map.md` and search over `projects/moe` for those source names in this session.
2. `Toward Efficient Inference for Mixture of Experts` (NeurIPS 2024) identifies inference inefficiency sources around large model size and complex communication patterns, and proposes dynamic gating, expert buffering, and expert load balancing.
   - Provenance: NeurIPS proceedings abstract page fetched in this session: `https://proceedings.neurips.cc/paper_files/paper/2024/hash/98bf3b8505c611ac21055dd9d355c66e-Abstract-Conference.html`.
3. `MegaScale-Infer` (arXiv 2025) contributes newer serving evidence that MoE FFNs can become memory-intensive during inference, motivating disaggregated attention/FFN deployment, ping-pong pipeline parallelism, and lower-overhead communication support; the abstract reports up to 1.90× higher per-GPU throughput.
   - Provenance: arXiv abstract page fetched in this session: `https://arxiv.org/abs/2504.02263`.
4. Compared with the current repo systems note, the new literature makes three serving-dominant bottlenecks newly explicit in project memory: sparse-FFN memory intensity at inference, expert buffering / residency management, and disaggregated module serving with communication hiding.
   - Provenance: comparison between `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md` and `projects/moe/literature/2026-03-24-inference-systems-split-evidence.md`.

## Actions taken

1. Oriented by reading `AGENTS.md`, root `README.md`, `projects/moe/README.md`, `projects/moe/TASKS.md`, existing MoE literature, and recent project logs.
2. Searched external literature for recent MoE training/inference systems developments and implementation-comparison signals.
3. Fetched abstract-level evidence for one inference-focused 2024 paper and one 2025 serving systems paper.
4. Wrote one new literature note: `projects/moe/literature/2026-03-24-inference-systems-split-evidence.md`.
5. Updated `projects/moe/README.md` with a dated project log entry and narrowed the remaining open question.

## Verification

- Verified absence of the new source names in current project memory using repository text search before writing the note.
- Verified that the new note was written under `projects/moe/literature/` and stayed within the session constraint of maximum one literature note.
- Verified that the project README now records the new finding and preserves provenance links.
- Verified session time using `get_current_time`, which returned Beijing time `2026年03月24日 周二 21:42:29`; converted to UTC timestamp `2026-03-24T13:42:29Z` by subtracting 8 hours inline.

## Notes

I did not create new tasks, per session constraint. I also did not update `projects/moe/TASKS.md` because this scan added evidence but did not change the executable next step definitions already present there.
