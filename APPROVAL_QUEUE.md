Coordination file for autonomous agent sessions requiring human decisions.

# Approval Queue

Items requiring human decision before autonomous execution can proceed. Agents append to "Pending"; humans resolve by moving items to "Resolved" with a decision.

## Pending

## Resolved

<!--
Schema for pending items:

### YYYY-MM-DD — <title>
Project: <project name>
Type: resource | structural | external | tool-access | burst
Request: <what the agent wants to do>
Context: <why, with links to relevant log entries>
Options: <if applicable, what choices exist>
Estimated cost: <if resource type>

Schema for resolved items:

### YYYY-MM-DD — <title>
Decision: approved | denied | modified
By: <human>
Date: <YYYY-MM-DD>
Notes: <any modifications or context>
-->

---

### [NON-BLOCKING] test-action

**Requested:** 2026-03-23T11:51:33.185911+00:00
**Description:** Smoke test approval queue
**Status:** pending


---

### [BLOCKING] tool-access

**Requested:** 2026-03-23T16:04:42.991412+00:00
**Description:** Example project task 'Run baseline captioning with 3 models on 50-image pilot set' cannot execute in the current repository state. The repo lacks the referenced local assets (`examples/my-research-project/data/captions.csv`, `data/categories.json`, pilot images, and `experiments/baseline-pilot/results/` scaffold) and no Gemini or Claude integrations were found in-repo (`search_text("anthropic|gemini|google.generativeai|vertexai", path=".")` returned no matches; `runner/openai_backend.py` is OpenAI-only). Approval/clarification needed on either: (A) provide the missing dataset + approved runtime path/API access for GPT-4o, Gemini 2.0 Flash, and Claude Sonnet; or (B) reformulate the task to use only currently available assets/providers.
**Status:** pending


---

### [BLOCKING] tool-access

**Requested:** 2026-03-23T16:38:51.175296+00:00
**Description:** Shell allowlist/denylist is blocking `git add` because the command string contains `add`, which appears to trigger a false-positive `dd` denylist match. Approval or policy adjustment is needed to stage and commit the akari horizon-scan files already written under `projects/akari/`.
**Status:** pending


---

### [BLOCKING] tool-access

**Requested:** 2026-03-24T03:50:23.158665+00:00
**Description:** Need approval or tool-policy adjustment to complete required git commit for session work. The allowlisted shell command `git add ... && git commit -m "[fleet/fleet-worker-07-1774323557-291433] ..."` was blocked by the shell denylist with false-positive message `Command blocked by denylist: dd`, apparently triggered by the substring `add`. Without a way to stage the new session log file, I cannot complete the mandated commit for the documented blocker update in `projects/multi-agent-survey/`.
**Status:** pending

