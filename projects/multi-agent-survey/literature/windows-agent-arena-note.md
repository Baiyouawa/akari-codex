# Literature Note — Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale

- Timestamp: 2026-03-23T17:12:00Z
- Category: Evaluation
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-evaluation-application.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 13.
  - Abstract text verified from `https://proceedings.mlr.press/v267/bonatti25a.html` via in-session `python3 requests` retrieval.

## Citation

Rogerio Bonatti, Dan Zhao, Francesco Bonacci, Dillon Dupont, Sara Abdali, Yinheng Li, et al. **Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale**. ICML 2025. PMLR page: `https://proceedings.mlr.press/v267/bonatti25a.html`. DBLP: `https://dblp.org/rec/conf/icml/BonattiZBDALLWK25`.

## What this paper studies

The paper proposes a benchmark for computer-use agents in the Windows operating system. Its core claim is that existing agent benchmarks are too narrow or too slow, so realistic evaluation should happen in a real OS environment with diverse tasks involving planning, screen understanding, and tool usage.

## Key contributions

1. Introduces a Windows-specific benchmark environment where agents operate in a real OS.
2. Builds **150+** tasks across representative domains.
3. Emphasizes evaluation scalability: the abstract states the benchmark can be parallelized so a full evaluation finishes in as little as **20 minutes**.
4. Reports a large agent-human gap: the best tested model reaches **19.5%** success rate versus **74.5%** human success rate.

## Evidence from source

Abstract excerpt, verified from the PMLR page:
> "We create 150+ diverse tasks across representative domains that require agentic abilities in planning, screen understanding, and tool usage. Our benchmark is scalable and can be seamlessly parallelized for a full benchmark evaluation in as little as 20 minutes... with the best achieving only a 19.5% success rate compared to a human success rate of 74.5%."

## Why it matters for the survey

- This is direct evidence that evaluation is shifting from toy text tasks to realistic computer-use settings.
- The reported human-agent gap suggests current multi-modal agents remain far from reliable deployment in OS environments.
- Because the benchmark measures planning, perception, and tool use together, it is useful when comparing multi-agent systems against single-agent-plus-tools baselines.

## Method / benchmark lens

The paper is best read as an infrastructure contribution rather than a new multi-agent coordination algorithm. Its survey value comes from benchmark design:
- real operating system environment,
- diverse long-horizon tasks,
- parallelized evaluation to control runtime cost,
- human comparison baseline.

## Limits / caveats

1. The artifact title and abstract emphasize OS agents broadly, not necessarily exclusively multi-agent systems.
2. From current repository evidence, we can verify the benchmark framing and headline metrics, but not the full ablation matrix without deeper paper extraction.
3. Windows-only evaluation may not generalize to web, mobile, or embodied agent settings.

## Relevance to open questions

- **ICLR 2026 是否有关于 multi-agent evaluation benchmark 的新工作？** This paper is an important pre-ICLR benchmark anchor from ICML 2025.
- **什么时候值得用多智能体？** A strong benchmark like this is necessary before any credible answer can be given.

## One-sentence takeaway

Windows Agent Arena is load-bearing because it reframes agent evaluation around realistic OS tasks and quantifies a still-large human-agent capability gap in scalable form.