# Remote-channel observability as a new self-study surface

Date: 2026-03-23
Project: akari
Type: internal-development note
Verified: 2026-03-23

## Why this is new

The akari meta-project artifacts currently focus on session-level self-improvement metrics such as intervention rate, gap detection, and self-observation failures. They do not yet describe the new remote command channels or the telemetry surface those channels create.

## Verified developments

1. The repository now documents two remote command channels: GitHub Issue/Discussion comments and a QQ bot.
   - Provenance: `README.md` section "Remote channels" and `docs/remote-channels.md`.

2. Both channels converge on a unified gateway that logs every remote invocation to a structured JSONL file.
   - Provenance: `docs/remote-channels.md` section "Unified Gateway"; `runner/gateway.py` function `_log_invocation(...)` writes to `logs/remote-invocations.jsonl`.

3. The logged record includes `timestamp`, `source`, `user`, `message`, `result_preview`, and `result_length`.
   - Provenance: `runner/gateway.py`, `_log_invocation(...)` record literal.

4. The gateway applies auth checks plus output sanitization and truncation before returning results externally.
   - Provenance: `runner/gateway.py` functions `_check_user_allowed(...)`, `_sanitize_output(...)`, and `_truncate(...)`; `docs/remote-channels.md` security sections.

## Why it matters for self-improvement

This adds a new operational data source for studying the autonomous research system itself. Session logs and approval events show what the system did after work began. Remote invocation logs add observability one step earlier in the loop: how work enters the system, which channels are used, and how often external-interface safeguards modify results.

That creates at least three measurement directions not captured in the current akari examples:

- **Channel mix and demand shape**: share of work entering through GitHub vs. QQ vs. local CLI.
- **Remote friction metrics**: rate of auth rejection, truncation, or sanitization events per remote invocation.
- **Input-to-session yield**: how often a remote request produces durable repo state such as logs, tasks, or project artifacts.

## Limits

The current implementation logs only a preview of the result and its length; it does not explicitly label whether sanitization or truncation occurred, nor whether a remote invocation led to a committed artifact.
- Provenance: `runner/gateway.py` stores `result_preview` and `result_length` but no explicit `sanitized`, `truncated`, or downstream artifact fields.

## Implication

The smallest useful logging question for akari should now include remote-interface events, not just internal sessions. Otherwise the system may miss failure modes introduced by the growing gap between command intake and durable knowledge production.
