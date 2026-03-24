# Session Log — akari capability-improvement transferability investigation

- Timestamp: 2026-03-23T17:20:00Z
- Task: Investigate which kinds of capability improvements transfer across projects, and which depend on repo history and conventions
- Classification: ROUTINE
- Status: complete

## Summary

Reviewed existing akari project artifacts and design-pattern documents to separate capability improvements that appear portable across projects from those that are strongly repo-specific. Wrote a synthesized provisional answer into `projects/akari/README.md` and updated `projects/akari/TASKS.md` to reflect that the measurement-plan work is now informed by a transferability split.

## Findings

1. Improvements that create more mechanical ground truth are the strongest candidates to transfer across projects.
   - Provenance: `projects/akari/diagnosis/self-observation-examples.md`
   - Provenance: `projects/akari/patterns/structured-work-records.md`

2. Improvements that standardize state handoff structure also look portable: repo-as-memory, inline logging, and structured work records all address stateless-session failure modes that are described as general rather than project-domain-specific.
   - Provenance: `projects/akari/patterns/repo-as-cognitive-state.md`
   - Provenance: `projects/akari/patterns/inline-logging.md`
   - Provenance: `projects/akari/patterns/structured-work-records.md`

3. The local self-improvement-loop example suggests that decomposition of coupled work into usable and blocked subtasks transfers as a general operational tactic.
   - Provenance: `projects/akari/analysis/local-self-improvement-loop-example.md`

4. Improvements encoded as specific skills, file destinations, thresholds, and counting rules are much more repo-specific because they depend on local conventions, schemas, and accumulated history.
   - Provenance: `projects/akari/patterns/skills-architecture.md`
   - Provenance: `projects/akari/patterns/repo-as-cognitive-state.md`

5. Cross-project validation is still missing: the repo contains conceptual evidence for portability but not a controlled comparison across multiple forks using the same counting rules.
   - Provenance: direct review of `projects/akari/README.md`, `projects/akari/analysis/`, and `projects/akari/patterns/` during this session; no multi-fork comparison artifact was found.

## Notes

No external research was required for this provisional internal answer. The next research need is internal cross-fork measurement using at least two deployments with shared definitions for intervention events, gap artifacts, and system-level improvements.
