# Literature Note — MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making

- Timestamp: 2026-03-23T17:17:00Z
- Category: Application
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-evaluation-application.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/neurips-2024-2025.md`, entry 9.
  - Title verified by DOI redirect from `https://doi.org/10.52202/079017-2522` to `https://www.proceedings.com/079017-2522.html` during this session.
  - Repository-internal tagging provenance: the NeurIPS artifact labels this paper `Architecture`.

## Citation

Cynthia Breazeal, Yik Chan, Marzyeh Ghassemi, Hyewon Jeong, Yubin Kim, Hyeonhoon Lee, Daniel McDuff, Chanwoo Park, Hae Park, Xuhai Xu. **MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making**. NeurIPS 2024. DOI: `https://doi.org/10.52202/079017-2522`.

## What this paper studies

From the verified title, this paper applies collaborative LLM agents to medical decision-making. The key survey value is not only that it is an application paper, but that it targets a high-stakes domain where accuracy, robustness, and interpretability matter more than demo-style task completion.

## Key contributions we can verify from repository state

1. The paper is about **adaptive collaboration** among LLMs.
2. The application domain is **medical decision-making**.
3. It provides a representative example of multi-agent systems being positioned as practical decision-support tools rather than generic chat orchestration.

## Evidence from source

Verified title from DOI landing page:
> "MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making"

Repository metadata from `projects/multi-agent-survey/literature/neurips-2024-2025.md`:
- Tags: `Architecture`
- Query provenance: retrieved via `collaboration`

## Why it matters for the survey

- Medical decision-making is a demanding application setting where claims about multi-agent value must be scrutinized carefully.
- The paper is useful as a representative case for whether role-specialized or collaborative agent systems outperform a single strong model in high-stakes workflows.
- It helps the survey cover application value, not just benchmark construction.

## Application lens

This paper should be read as an example of domain-specialized multi-agent deployment logic:
- decompose a complex decision task,
- assign or induce complementary LLM roles,
- aggregate or adapt collaboration for better decisions.

That pattern recurs across many practical multi-agent system papers.

## Limits / caveats

1. In this session, the repository verifies the title and application framing but not the abstract details or outcome metrics.
2. Because the accessible DOI landing page did not expose the abstract cleanly, this note remains provisional with respect to exact claimed gains.
3. High-stakes domain papers often need stronger evidence than benchmark wins, including clinician comparison and error analysis, which are not yet verified here.

## Relevance to open questions

- **什么时候值得用多智能体？** A domain like medicine is one of the strongest candidate settings, but only if collaboration yields verifiable gains beyond a single model plus tools.
- **Multi-Agent 与 Single-Agent + tools 的性能边界在哪里？** MDAgents is a good case study for that boundary because the task is knowledge-intensive and potentially decomposable.

## One-sentence takeaway

MDAgents is load-bearing because it tests whether multi-agent collaboration can justify itself in a high-stakes medical decision setting rather than only in synthetic benchmarks.