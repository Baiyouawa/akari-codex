# Literature Note — ZSC-Eval: An Evaluation Toolkit and Benchmark for Multi-agent Zero-shot Coordination

- Timestamp: 2026-03-23T17:16:00Z
- Category: Evaluation
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-evaluation-application.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/neurips-2024-2025.md`, entry 19.
  - Title verified by DOI redirect from `https://doi.org/10.52202/079017-1501` to `https://www.proceedings.com/079017-1501.html` during this session.
  - Repository-internal tagging provenance: the NeurIPS artifact labels this paper `Coordination, Evaluation`.

## Citation

Jingxiao Chen, Wentao Dong, Xihuai Wang, Ying Wen, Shao Zhang, Weinan Zhang, Wenhao Zhang. **ZSC-Eval: An Evaluation Toolkit and Benchmark for Multi-agent Zero-shot Coordination**. NeurIPS 2024. DOI: `https://doi.org/10.52202/079017-1501`.

## What this paper studies

From the title and repository classification, the paper proposes an evaluation toolkit and benchmark for zero-shot coordination in multi-agent settings. That makes it a benchmark-centered contribution for measuring whether agents can coordinate with previously unseen partners or under unseen interaction conditions.

## Key contributions we can verify from repository state

1. It is explicitly framed as both an **evaluation toolkit** and a **benchmark**.
2. Its target phenomenon is **multi-agent zero-shot coordination**, which is one of the hardest deployment-relevant coordination problems.
3. It sits at the boundary between evaluation and coordination, making it useful for comparing MARL-style benchmark traditions with newer LLM-agent system benchmarks.

## Evidence from source

Verified title from DOI landing page:
> "ZSC-Eval: An Evaluation Toolkit and Benchmark for Multi-agent Zero-shot Coordination"

Repository metadata from `projects/multi-agent-survey/literature/neurips-2024-2025.md`:
- Tags: `Coordination, Evaluation`
- Query provenance: retrieved via `multi-agent`

## Why it matters for the survey

- Zero-shot coordination is one of the most informative tests for whether a multi-agent method generalizes beyond a fixed team.
- The paper helps anchor the survey's evaluation section in the MARL/coordination literature, so the survey does not over-focus on LLM-agent benchmarks.
- It is directly relevant to the question of when multi-agent systems are worthwhile: if agents cannot coordinate with new partners, practical value is limited.

## Limits / caveats

1. In this session, the repository can verify the title, DOI landing page, tags, and benchmark orientation, but not the full abstract or numeric results.
2. Because the accessible landing page did not expose the abstract text directly, this note should be treated as a provisional literature note pending deeper extraction.
3. The paper likely belongs partly in the Coordination bucket as well; its placement here reflects its benchmark role.

## Relevance to open questions

- **什么时候值得用多智能体？** Only if coordination generalizes beyond the exact teammates seen in development; ZSC-Eval appears designed to test that.
- **ICLR 2026 是否有关于 multi-agent evaluation benchmark 的新工作？** ZSC-Eval is a strong 2024 baseline to compare against any new benchmark claims.

## One-sentence takeaway

ZSC-Eval is load-bearing because zero-shot coordination benchmarking is a core test of whether multi-agent capability survives beyond closed-world training partners.