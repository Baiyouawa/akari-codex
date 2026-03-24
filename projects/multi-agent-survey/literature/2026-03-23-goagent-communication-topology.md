# Literature Note — GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems

- Note date: 2026-03-23T16:35:00Z
- Project: `projects/multi-agent-survey`
- Status: new horizon-scan note

## Bibliographic stub

- Title: **GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems**
- Venue: arXiv preprint
- Published: 2026-03-20T06:21:32Z
- Link: https://arxiv.org/abs/2603.19677v1

## Provenance

This note is based on the arXiv Atom API response retrieved in-session via:

```bash
python3 - <<'PY'
import urllib.request, xml.etree.ElementTree as ET
url='https://export.arxiv.org/api/query?search_query=all:%22multi-agent%22+OR+all:%22multiagent%22+OR+all:%22agent+collaboration%22&sortBy=submittedDate&sortOrder=descending&start=0&max_results=20'
...
PY
```

The returned entry included:
- published: `2026-03-20T06:21:32Z`
- title: `GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems`
- link: `https://arxiv.org/abs/2603.19677v1`
- abstract lead: `Large language model (LLM)-based multi-agent systems (MAS) have demonstrated exceptional capabilities in solving complex tasks, yet their effectiveness depends heavily on the underlying communication topology ...`

## Why this looks genuinely new relative to current repo state

Current project artifacts include only a broad NeurIPS 2024 candidate pool in `projects/multi-agent-survey/literature/neurips-2024-2025.md`; there was no existing note or mention of communication-topology generation for LLM-based MAS in `projects/multi-agent-survey/literature/` at scan time.

## Load-bearing takeaway

This paper appears to target a concrete gap in current LLM multi-agent research: **the communication graph itself becomes a learned/generated object**, rather than a fixed design choice such as all-to-all chat, manager-worker, or debate.

That matters for one of the project's explicit open questions:
- `Agent-to-agent communication 的最新范式是什么？shared memory vs message passing vs tool use?`

GoAgent suggests a fourth framing worth tracking in the survey:
- **topology generation / communication structure search**

## Provisional classification

- Primary: Communication
- Secondary: Architecture
- Tertiary: Coordination

## Survey implication

If later verified by full-paper reading, this work may support a 2026 trend claim that the field is moving from:
1. hand-authored multi-agent roles,
2. to role + tool orchestration,
3. to **adaptive communication topology design**.

This would sharpen the survey's comparison between multi-agent systems and strong single-agent + tools baselines: one plausible advantage of multi-agent systems is not just parallel role specialization, but the ability to induce sparse or hierarchical information-routing structures.

## Follow-up questions for future sessions

1. Does GoAgent optimize topology offline, online, or per task instance?
2. What baselines are used: all-to-all, star, tree, debate, or memory-sharing?
3. Does the paper show quality/cost wins over single-agent + tools?
4. Is there an associated benchmark for communication-topology evaluation?
