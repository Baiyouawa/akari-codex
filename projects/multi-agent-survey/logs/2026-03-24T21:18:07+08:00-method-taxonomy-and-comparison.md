# Session Log — Method taxonomy and comparison table

- Timestamp: 2026-03-24T21:18:07+08:00
- Project: `projects/multi-agent-survey`
- Task: `projects/multi-agent-survey/TASKS.md` — 产出分类体系与方法对比表
- Classification: ROUTINE
- Status: completed

## Summary

Completed the assigned Phase 3 structuring task by producing a repository-backed method taxonomy for recent Multi-Agent research and a comparison table covering representative papers, strengths, weaknesses, and fit-for-use scenarios. The artifact is designed to support the survey draft directly rather than only serve as a note dump.

## Findings

1. The current repository supports a method taxonomy organized by explicit design variable rather than by venue.
   - Provenance: synthesized from `projects/multi-agent-survey/literature/icml-2024-2025.md`, `projects/multi-agent-survey/literature/neurips-2024-2025.md`, `projects/multi-agent-survey/literature/iclr-2025-2026.md`, and `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`.

2. A 6-category taxonomy is supportable from in-repo evidence: role/topology-driven architecture, task decomposition and coordination, communication/shared memory, training/self-improving multi-agent systems, evaluation/benchmark/diagnostic work, and high-value application systems.
   - Provenance: `projects/multi-agent-survey/analysis/2026-03-24-method-taxonomy-and-comparison.md`.
   - Inline arithmetic: 6 categories = 6 named buckets in the analysis artifact.

3. The strongest current trend signal in the repo is not "more agents", but making structure, coordination, communication, and evaluation increasingly explicit.
   - Provenance: topology-focused evidence from `projects/multi-agent-survey/literature/2026-03-23-goagent-communication-topology.md` and `projects/multi-agent-survey/literature/iclr-2025-2026.md` entries 95 and 117; benchmark/safety evidence from `omnibench-note.md`, `windows-agent-arena-note.md`, `agent-smith-note.md`, and `iclr-2025-2026.md` entries 55 and 103.

4. The repo-level boundary answer remains consistent with a single-agent-first default unless coordination, communication, or topology is itself the hard part.
   - Provenance: `projects/multi-agent-survey/logs/2026-03-23T170500Z-single-vs-multi-agent-boundary-synthesis.md` and the practical synthesis section in `projects/multi-agent-survey/analysis/2026-03-24-method-taxonomy-and-comparison.md`.

## Actions taken

1. Wrote `projects/multi-agent-survey/analysis/2026-03-24-method-taxonomy-and-comparison.md`.
2. Updated `projects/multi-agent-survey/TASKS.md` to mark the taxonomy/comparison task complete with evidence.
3. Recorded this session log.

## Verification

Verified that the new analysis artifact includes:
- a stated classification principle,
- a method taxonomy table,
- per-category representative papers,
- strengths/weaknesses/use-case notes,
- a cross-category comparison table,
- and an explicit synthesis on when multi-agent is or is not justified.

## Next step

Use this taxonomy as the structure for the survey draft and for the later trend-analysis document, especially the sections on topology optimization, evaluation benchmarks, and the single-agent vs multi-agent boundary.
