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


---

### [BLOCKING] tool-access

**Requested:** 2026-03-24T03:57:10.678063+00:00
**Description:** Need shell access to `git add` and `git commit` to complete the required session commit for task `继续推进 MoE 任务`. Work artifacts have been written under `projects/moe/`, but the current allowlist permits `git status`/`git diff` only, so the required commit with message containing `[fleet/fleet-worker-03-1774323557-89bc3c]` cannot be executed from this session.
**Status:** pending


---

### [BLOCKING] tool-access

**Requested:** 2026-03-24T04:04:40.731642+00:00
**Description:** Need permission or alternative mechanism to stage and commit project-local changes for task completion. Current shell policy blocks `git add`/commit path with denylist match (`Command blocked by denylist: dd `), preventing required final commit for files under `projects/multi-agent-survey/` despite non-destructive repo-local changes.
**Status:** pending


---

### [BLOCKING] tool-access

**Requested:** 2026-03-24T04:17:01.617991+00:00
**Description:** Need permission/tool access to run `git add` and `git commit` for only the MoE task files (`projects/moe/README.md`, `projects/moe/TASKS.md`, `projects/moe/literature/2026-03-24-moe-source-map.md`, `projects/moe/logs/2026-03-24T035630Z-source-map-first-pass.md`). Current shell allowlist exposes `git status/log/diff/branch` but not `git add/commit`, and the repo has unrelated dirty files from other sessions, so I cannot safely create the required isolated commit with message containing [fleet/fleet-worker-21-1774324248-f85493] without expanded git access.
**Status:** pending


---

### [BLOCKING] tool-access

**Requested:** 2026-03-24T13:22:38.045759+00:00
**Description:** Need approval or alternate tool access to run git staging/commit for this completed MoE task. Repository policy requires ending session with a git commit, but `run_shell` blocks `git add`/`git commit` (current denylist reports `Command blocked by denylist: dd`). Work is already written under `projects/moe/` and verified; only staging/commit remains.
**Status:** pending


---

### [BLOCKING] tool-access

**Requested:** 2026-03-24T13:29:56.880615+00:00
**Description:** Need approval or alternative tooling to stage files for commit. Standard `git add ... && git commit ...` was blocked by the shell denylist (`Command blocked by denylist: dd `), apparently because `git add` matches the denylist substring. The task is otherwise complete under `projects/moe/`, but I cannot create the required commit without a staging-capable path.
**Status:** pending


---

### [BLOCKING] tool-access

**Requested:** 2026-03-24T13:31:06.477403+00:00
**Description:** Need approval or tool-access extension to run git staging/commit commands for completed task output. Work is finished in repo files (`projects/multi-agent-survey/plans/survey-draft.md`, README/TASKS/log updated), but current allowlist blocks `git add`/`git commit`, preventing required session finalization with commit message `[fleet/花阳-06-1774358212-01557e] ...`.
**Status:** pending

