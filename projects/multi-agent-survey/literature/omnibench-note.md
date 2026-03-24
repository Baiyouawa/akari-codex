# Literature Note — OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities

- Timestamp: 2026-03-23T17:13:00Z
- Category: Evaluation
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-evaluation-application.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 14.
  - Abstract text verified from `https://proceedings.mlr.press/v267/bu25b.html` via in-session `python3 requests` retrieval.

## Citation

Wendong Bu, Yang Wu, Qifan Yu, Minghe Gao, Bingchen Miao, Zhenkui Zhang, et al. **What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities**. ICML 2025. PMLR page: `https://proceedings.mlr.press/v267/bu25b.html`. DBLP: `https://dblp.org/rec/conf/icml/BuWYGMZPL000TZ25`.

## What this paper studies

The paper argues that existing virtual-agent benchmarks lack controllable task complexity, require too much manual annotation, and do not evaluate agents across multiple capability dimensions. It introduces OmniBench and OmniEval to address those benchmark-design gaps.

## Key contributions

1. Proposes **OmniBench**, a self-generating graph-based benchmark.
2. Uses automated task synthesis through subtask composition, making complexity controllable.
3. Proposes **OmniEval**, a multidimensional evaluation framework with subtask-level and graph-based metrics.
4. Reports a synthesized dataset of **36k** graph-structured tasks across **20** scenarios with **91%** human acceptance rate.
5. Claims training on graph-structured data improves cross-environment generalization.

## Evidence from source

Abstract excerpt, verified from the PMLR page:
> "We introduce OmniBench, a self-generating, graph-based benchmark with an automated pipeline for synthesizing tasks of controllable complexity through subtask composition. To evaluate the diverse capabilities of virtual agents on the graph, we further present OmniEval... Our synthesized dataset contains 36k graph-structured tasks across 20 scenarios, achieving a 91% human acceptance rate."

## Why it matters for the survey

- It represents a move from static benchmark curation to benchmark generation.
- The multidimensional evaluation framing is useful for agent systems where scalar success rate alone hides weaknesses.
- Controllable complexity is especially important for testing whether multi-agent systems help only on hard decomposable tasks or also on simpler ones.

## Method / benchmark lens

The benchmark design appears to be centered on a task graph abstraction:
- synthesize tasks automatically,
- control complexity by subtask composition,
- evaluate both local subtask execution and global graph-level success.

This is survey-relevant because it provides a concrete path toward diagnosing where an agent system fails: planning, decomposition, or capability execution.

## Limits / caveats

1. The paper studies virtual agents broadly; current repository evidence does not prove the benchmark was designed specifically for multi-agent collaboration.
2. Automated synthesis raises the usual question of benchmark realism versus benchmark convenience.
3. Without deeper reading, the repository can verify headline dataset and framework claims but not the exact robustness of the metric design.

## Relevance to open questions

- **ICLR 2026 是否有关于 multi-agent evaluation benchmark 的新工作？** OmniBench is a strong benchmark precursor and a comparison point for newer benchmark papers.
- **Multi-Agent 与 Single-Agent + tools 的性能边界在哪里？** A controllable-complexity benchmark is exactly the kind of instrument needed to answer that question.

## One-sentence takeaway

OmniBench is load-bearing because it turns agent evaluation into a controllable, multidimensional benchmark-generation problem rather than a fixed leaderboard problem.