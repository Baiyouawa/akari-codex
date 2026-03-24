# Fleet-scale autonomy benchmarks as a new self-improvement comparison surface

Date: 2026-03-24
Project: akari
Type: internal-development note
Verified: 2026-03-24

## Why this is new

Existing akari literature notes already capture two new self-study surfaces in this repo: remote-channel observability and scheduler evaluation telemetry. They do not yet capture that the repo now publishes a fleet-scale empirical benchmark surface for autonomy claims: aggregate success, knowledge-production, and explicit-approval rates over thousands of sessions.

## Verified developments

1. The repo now includes a dedicated document describing fleet operation as an empirical research system rather than only an architectural pattern.
   - Provenance: `docs/fleet-research.md`.

2. That document reports an operational record excerpt covering `5,303` fleet sessions from `2026-02-25` through `2026-03-07`.
   - Provenance: `docs/fleet-research.md`, section `Evidence: sustained autonomous operation`.

3. The same excerpt reports an overall success rate of `91.0% (4,825/5,303)` and a knowledge-producing-session rate of `54.2% (2,876/5,303)`.
   - Provenance: `docs/fleet-research.md`, section `Evidence: sustained autonomous operation`.

4. The document also reports category-level output counts from those sessions: `7,026` structural changes, `1,647` new literature notes, `1,465` new experiment findings, `185` experiments completed, `494` infra code changes, and `48` decision records created.
   - Provenance: `docs/fleet-research.md`, section `Evidence: sustained autonomous operation`.

5. For explicit human governance, the document reports `12` approval events over `1,529` sessions in the week of `2026-03-02`, which it states as `0.0079` approval events per session.
   - Provenance: `docs/fleet-research.md`, section `Evidence: scarce human intervention`; inline arithmetic check `12 / 1529 = 0.007848...`, which rounds to `0.0079`.

6. The same document explicitly recommends four reproducible operational measures for forks that want to substantiate autonomy claims: success rate, knowledge-producing-session rate, output counts by category, and approval events per session.
   - Provenance: `docs/fleet-research.md`, section `How to reproduce this kind of evidence in your system`.

## Why it matters for self-improvement

This is a distinct development from the previously noted telemetry surfaces. Remote-invocation logs and scheduler metrics define what can be measured. `docs/fleet-research.md` adds a published benchmark frame for what forks should compare: not only intervention rate, but also durable knowledge yield and output composition at operational scale.

That creates at least three new directions for the akari meta-project:

- **Cross-fork benchmark portability**: whether success rate, knowledge-producing-session rate, and approval-events-per-session remain comparable when forks share session and approval schemas.
- **Knowledge-yield evaluation**: whether `knowledge-producing sessions / total sessions` is a more stable autonomy metric across deployments than task-completion counts alone.
- **Output-mix diagnostics**: whether changes in the distribution of literature notes, findings, infra changes, and decision records reveal capability drift or self-improvement trade-offs over time.

## Limits

The published evidence is aggregated rather than raw, and the document does not specify a fully mechanical schema for classifying a session as `knowledge-producing` inside this public fork.
- Provenance: `docs/fleet-research.md` presents aggregate counts and a reproduction checklist but no public classifier definition or script path for the `knowledge-producing sessions` label.

## Implication

For akari's open question about robust self-improvement metrics across forks, the strongest newly surfaced candidates are now a small benchmark bundle: success rate, knowledge-producing-session rate, output counts by category, and approval events per session. But portability still depends on standardizing the event definitions and classifiers behind those counts.