# NeurIPS multi-agent inventory recovery and gap assessment

- Timestamp: 2026-03-25T13:44:06Z
- Project: `projects/multi-agent-survey`
- Scope: assess what the repository can already support for the NeurIPS multi-agent retrieval task without new external calls
- Provenance boundary: this note uses only in-repo artifacts recovered in this session

## Sources used

1. `projects/multi-agent-survey/literature/neurips-2024-2025.md`
2. `projects/multi-agent-survey/scripts/harvest_neurips_crossref.py`
3. `projects/multi-agent-survey/logs/2026-03-23T161441Z-neurips-2024-harvest.md`
4. Inline arithmetic from the recovered literature file via `python3` regex counting in this session

## What was recovered

This session recovered three previously deleted but still HEAD-addressable project artifacts:

1. `projects/multi-agent-survey/literature/neurips-2024-2025.md`
2. `projects/multi-agent-survey/scripts/harvest_neurips_crossref.py`
3. `projects/multi-agent-survey/logs/2026-03-23T161441Z-neurips-2024-harvest.md`

Provenance: `python3` + `git show HEAD:<path>` restored each file byte-for-byte into the working tree during this session.

## Current in-repo answer for the NeurIPS task

The repository already contains a venue-constrained NeurIPS candidate inventory generated from Crossref.

### Coverage currently supported by repo evidence

- The recovered artifact contains **138** numbered candidates under `## 2024`.
  - Provenance: `projects/multi-agent-survey/literature/neurips-2024-2025.md`; independently re-counted in this session with `python3` regex over numbered entries, which printed `count_2024 138`.
- The recovered artifact contains **0** harvested candidates under `## 2025` in the Crossref snapshot used at the time.
  - Provenance: the `## 2025` section says `No candidates harvested for this year in the current Crossref snapshot.`; the same session regex check printed `count_2025 0`.
- The recovered task log explicitly states that the NeurIPS inventory was only a **partial** completion because 2025 was missing from the source snapshot.
  - Provenance: `projects/multi-agent-survey/logs/2026-03-23T161441Z-neurips-2024-harvest.md`.

### Topic mix in the recovered 2024 candidate pool

Using the lightweight title-tagging already stored in `neurips-2024-2025.md`, the 138 recovered 2024 candidates include:

- `Theory/MARL`: 76 tagged entries
- `Communication`: 22 tagged entries
- `Architecture`: 20 tagged entries
- `Evaluation`: 4 tagged entries
- `Coordination`: 3 tagged entries
- `Application`: 3 tagged entries

Provenance: inline `python3` regex counting over tag lines in `projects/multi-agent-survey/literature/neurips-2024-2025.md` during this session printed exactly:
- `Architecture 20`
- `Coordination 3`
- `Communication 22`
- `Evaluation 4`
- `Application 3`
- `Theory/MARL 76`

Caveat: these counts are tag incidences from the artifact’s heuristic labels, not mutually exclusive paper counts by category.

## What is still missing relative to the current assignment

The current assignment asks for the **recent three years** of NeurIPS multi-agent papers plus high-relevance filtering and the fields `title / authors / year / link / PDF / OpenReview or conference page`.

The recovered in-repo artifacts do **not** yet satisfy that request fully:

1. **2023 coverage is absent.**
   - Provenance: `projects/multi-agent-survey/literature/neurips-2024-2025.md` only contains sections `## 2024` and `## 2025`.
2. **2025 coverage is absent in the stored Crossref snapshot.**
   - Provenance: the 2025 section explicitly reports zero harvested candidates.
3. **High-relevance screening is not finalized.**
   - Provenance: the artifact is titled `candidate list`, and the method says `Relevance heuristic: keep titles containing at least one agent/MAS-related keyword`; it does not mark a final high-relevance subset.
4. **PDF download addresses are not stored.**
   - Provenance: each entry in `neurips-2024-2025.md` has `Authors`, `Link`, `Tags`, and `Retrieved via query`, but no `PDF` field.
5. **OpenReview or conference-page URLs are not stored.**
   - Provenance: same file structure; no `OpenReview` or `conference page` fields appear in entries.

## Practical conclusion

Within the repository’s current no-new-external-call boundary, the best verified NeurIPS result is:

- a recovered **NeurIPS 2024 candidate inventory with 138 venue-constrained Crossref hits**, and
- a verified statement that the prior retrieval pipeline produced **no NeurIPS 2025 records** in that snapshot.

This is valuable prior work and should be preserved, but it is **insufficient to close** the current task as written because the repository still lacks:

- NeurIPS 2023 coverage,
- actual NeurIPS 2025 paper records,
- final high-relevance subset selection, and
- per-paper PDF / OpenReview / conference-page links.

## Follow-up questions noted

- Which authoritative in-repo or already-cached source can supply NeurIPS 2023 and NeurIPS 2025 proceedings metadata without introducing fresh external retrieval?
- Should the final NeurIPS deliverable preserve the broad candidate pool and add a second section for a manually screened high-relevance subset?
