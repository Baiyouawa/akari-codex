# Session Log — MoE Training vs Inference Modeling

- Timestamp: 2026-03-24T13:43:44Z
- Session: 花阳-06-1774359774-423cd9
- Project: `projects/moe`
- Task: 验证训练与推理场景是否应分开建模，并确定是否需要统一指标桥接二者
- Classification: ROUTINE
- Status: complete

## Summary

Completed the assigned zero-resource analysis task using only repository-internal sources. Wrote a new note that separates currently supported evidence from still-open hypotheses, then synced the conclusion back to `projects/moe/README.md` and `projects/moe/TASKS.md`.

## Findings

1. Current repo evidence is stronger for training-time systems concerns than for inference-time serving concerns because the registered implementation entries emphasize training configuration, expert parallelism, and distributed execution, while inference-side evidence is mostly limited to configuration and usage documentation.
   - Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`; `projects/moe/analysis/2026-03-24-training-vs-inference-modeling.md`.
2. The current evidence base supports splitting training and inference into separate comparison axes, but not treating them as completely unrelated systems, because both still share the same MoE structure-induced costs: dispatch, communication, utilization, and capacity handling.
   - Provenance: `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`; `projects/moe/analysis/2026-03-24-training-vs-inference-modeling.md`.
3. A safer project-level evaluation frame is “separate top-level metrics plus shared bridge fields” rather than either a single mixed score or two fully disconnected scorecards.
   - Provenance: `projects/moe/analysis/2026-03-24-training-vs-inference-modeling.md`, section `Decision for current project state`.
4. The strongest bridge-metric candidates currently visible in repo evidence are dispatch complexity, expert utilization/load skew, overflow or unused-capacity rate, and communication-to-compute exposure.
   - Provenance: `projects/moe/analysis/2026-03-24-training-vs-inference-modeling.md`, section `Bridge metric candidates`.

## Actions taken

1. Read `AGENTS.md`, root `README.md`, `projects/moe/README.md`, `projects/moe/TASKS.md`, the MoE source map, the existing systems analysis, and recent MoE logs to orient.
2. Wrote `projects/moe/analysis/2026-03-24-training-vs-inference-modeling.md` with source inventory, evidence vs hypothesis split, recommended modeling split, and bridge-metric candidates.
3. Updated `projects/moe/README.md` with a dated log entry and removed the resolved training-vs-inference item from `## Open questions`.
4. Updated `projects/moe/TASKS.md` to mark the assigned task complete with explicit evidence.

## Verification

- Verified the new analysis artifact exists at `projects/moe/analysis/2026-03-24-training-vs-inference-modeling.md`.
- Verified `projects/moe/README.md` now records the conclusion that training and inference should be modeled separately but compared through shared bridge fields.
- Verified `projects/moe/TASKS.md` now marks the training-vs-inference modeling task complete.

## Notes

This session intentionally did not claim that the repository has already proven a serving-specific bottleneck ranking. The note preserves that distinction as an open evidence gap while still resolving the project’s immediate modeling decision.
