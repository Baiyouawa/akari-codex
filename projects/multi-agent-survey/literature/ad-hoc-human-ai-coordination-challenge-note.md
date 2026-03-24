# Literature Note — Ad-Hoc Human-AI Coordination Challenge

- Timestamp: 2026-03-23T17:14:00Z
- Category: Evaluation
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-evaluation-application.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 22.
  - Abstract text verified from `https://proceedings.mlr.press/v267/dizdarevic25a.html` via in-session `python3 requests` retrieval.

## Citation

Tin Dizdarević, Ravi Hammond, Tobias Gessler, Anisoara Calinescu, Jonathan Cook, Matteo Gallici, et al. **Ad-Hoc Human-AI Coordination Challenge**. ICML 2025. PMLR page: `https://proceedings.mlr.press/v267/dizdarevic25a.html`. DBLP: `https://dblp.org/rec/conf/icml/DizdarevicHGC0G25`.

## What this paper studies

The paper studies evaluation of coordination between humans and AI agents rather than only coordination among trained artificial teammates. It uses Hanabi as the testbed and proposes a reproducible benchmark based on human proxy agents.

## Key contributions

1. Introduces **AH2AC2**, an evaluation challenge for ad-hoc human-AI coordination.
2. Uses Hanabi because it combines imperfect information, constrained communication, theory of mind, and coordinated action.
3. Replaces expensive human evaluation with proxy agents trained on a large-scale human dataset.
4. Releases a dataset of **3,079** games while intentionally limiting data volume to encourage data-efficient methods.
5. Provides baseline results for both two-player and three-player settings.

## Evidence from source

Abstract excerpt, verified from the PMLR page:
> "We develop human proxy agents on a large-scale human dataset that serve as robust, cheap, and reproducible human-like evaluation partners in AH2AC2. To encourage the development of data-efficient methods, we open-source a dataset of 3,079 games, deliberately limiting the amount of available human gameplay data."

## Why it matters for the survey

- It reframes evaluation around human compatibility, which is a deployment-critical criterion for many real-world multi-agent systems.
- It gives a concrete answer to a recurring survey problem: human studies are expensive and hard to reproduce, so how can we still benchmark human-AI teaming?
- It covers a setting where communication and theory of mind are central, making it more diagnostic than plain task-completion benchmarks.

## Method / benchmark lens

The benchmark contribution is a controlled substitute for direct human trials:
- choose a coordination-rich game,
- model human behavior with proxy agents,
- keep evaluation centralized and controlled rather than fully releasing the proxies.

That design is notable because it treats reproducibility as part of the benchmark specification.

## Limits / caveats

1. Hanabi is a stylized domain, so transfer to open-world agent systems is uncertain.
2. Human proxies are only as good as the data and modeling assumptions used to train them.
3. The benchmark addresses coordination quality, but the current repository evidence does not specify whether it compares multi-agent LLM systems against single-agent baselines.

## Relevance to open questions

- **什么时候值得用多智能体？** If deployment requires cooperating with humans or unknown partners, this benchmark suggests that pure self-play success is not enough.
- **ICLR 2026 是否有关于 multi-agent evaluation benchmark 的新工作？** AH2AC2 is an important benchmark baseline for human-AI coordination that newer papers should be compared against.

## One-sentence takeaway

AH2AC2 is load-bearing because it operationalizes reproducible human-AI coordination evaluation, not just agent-only task success.