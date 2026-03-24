# Literature Note — DIG to Heal: Scaling General-purpose Agent Collaboration via Explainable Dynamic Decision Paths

- Timestamp: 2026-03-23T17:19:00Z
- Category: Evaluation / Application-enabling systems
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-evaluation-application.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`, 2026-02 entry 3.
  - Abstract snippet provenance from the same arXiv harvest artifact.
  - Title verified from `https://arxiv.org/abs/2603.00309v1` during this session.

## Citation

Hanqing Yang, Hyungwoo Lee, Yuhang Yao, Zhiwei Liu, Kay Liu, Jingdi Chen, Carlee Joe-Wong. **DIG to Heal: Scaling General-purpose Agent Collaboration via Explainable Dynamic Decision Paths**. arXiv preprint `http://arxiv.org/abs/2603.00309v1`, published 2026-02-27T20:59:37Z.

## What this paper studies

The paper studies how to scale collaboration among general-purpose LLM agents. The title foregrounds two ideas especially relevant to practical deployment: dynamic decision paths and explainability.

## Key contributions we can verify from repository state

1. The work is about **scaling general-purpose agent collaboration**.
2. It introduces or centers **explainable dynamic decision paths**.
3. The arXiv harvest classifies it as `Architecture, Coordination, Communication, Evaluation`.
4. The stored abstract snippet states that many agentic systems rely on predefined workflows and positions this paper against that limitation.

## Evidence from source

Verified title from arXiv abstract page:
> "DIG to Heal: Scaling General-purpose Agent Collaboration via Explainable Dynamic Decision Paths"

Repository abstract snippet from `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`:
> "The increasingly popular agentic AI paradigm promises to harness the power of multiple, general-purpose large language model (LLM) agents to collaboratively complete complex tasks. While many agentic AI systems utilize predefined..."

## Why it matters for the survey

- It is a recent paper that directly addresses scalability of agent collaboration, which is central to practical value.
- Explainability is crucial for real deployments because debugging and trust become harder as more agents interact.
- It helps connect evaluation and application: a collaboration system that cannot explain decision paths is hard to validate in practice.

## System lens

The paper appears to push beyond fixed workflows by making coordination paths dynamic and interpretable. That is notable because many multi-agent systems succeed only under handcrafted protocols; a move toward dynamic collaboration could be a meaningful 2026 trend.

## Limits / caveats

1. This note is based on title verification and repository-preserved abstract snippet, not full-paper extraction.
2. Exact evaluation metrics and baselines are not yet verified from repository state.
3. The paper may belong partly in the Architecture or Coordination bucket; it is included here because scaling and explainability strongly affect application viability.

## Relevance to open questions

- **最近三个月 arXiv 上的 multi-agent 论文主要集中在哪些子方向？** This paper supports the view that scalable collaboration control and interpretability are active subdirections.
- **什么时候值得用多智能体？** Dynamic decision-path control may be one condition under which multi-agent systems become practical rather than brittle.

## One-sentence takeaway

DIG to Heal is load-bearing because it targets the practical bottleneck of general-purpose multi-agent deployment: scalable collaboration needs decision paths that are both dynamic and interpretable.