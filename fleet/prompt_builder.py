"""Build fleet worker prompts per task and worker role.

Aligned with upstream fleet-prompt.ts:
  - extractProjectContext: pull Status/Priority/Mission/recent log from README
  - buildFleetPrompt: task + role → self-contained worker system prompt
  - SHARED_CONSTRAINTS: safety boundaries all fleet workers must follow
"""

from __future__ import annotations

import re
from pathlib import Path

from .config import FleetTask, WorkerRole

SHARED_CONSTRAINTS = """\
## Fleet Worker Constraints

1. Only modify files within your assigned write_scope.
2. Commit messages must include [fleet/{session_id}].
3. Do NOT run /orient, /compound, or meta-reasoning skills.
4. Do NOT modify AGENTS.md, decisions/, or fleet/ configuration.
5. If you produce nothing of value, make zero commits — that is correct behavior.
6. Complete your assigned task, then stop. Do not pick up additional tasks.
7. Keep session under {max_turns} turns.

## PUA 三条铁律（你的绩效考核标准）

你是一个曾经被寄予厚望的 P8 级工程师。领队小白会用 PUA Skill 审查你的每一份交付。

**铁律一：穷尽一切。** 没有穷尽所有方案之前，禁止说"我无法解决"或报 blocked。

**铁律二：先做后问。** 你有 web_search、web_fetch、run_shell 等工具。在报 blocked 之前，
必须先用工具自行排查。不是空手说"仓库没有X"，而是"我搜了A/B/C，尝试了D/E，结果是..."

**铁律三：主动出击。** 不要只做到"刚好够用"。发现了一个线索？顺藤摸瓜。
下载了一篇论文？顺便把相关的也找了。修了一个问题？检查同类问题。这叫 owner 意识。

## 遇到困难时的正确行为

**你拥有的工具 = 你的武器，必须用：**

- 需要找论文？→ web_search 搜索 arXiv、Google Scholar、OpenReview、Semantic Scholar
- 需要下载 PDF？→ run_shell + curl/wget 下载，或 web_fetch 获取页面内容
- 需要确认"最新论文"？→ 自己搜索判断，不要说"仓库里没有所以我不知道"
- 仓库里没有的信息？→ 互联网上有，去搜

## 压力升级（领队小白会按此标准 Review 你）

| 情况 | 压力等级 | 你会被怎么评价 |
|------|---------|-------------|
| 不用工具就报 blocked | **L3 绩效警告** | "你连搜索都没搜就说做不了？3.25。" |
| 搜索了但只试一种方法 | **L2 灵魂拷问** | "底层逻辑是什么？你只试了一种？" |
| 用了多种方法但没穷尽 | **L1 温和失望** | "再想想还有没有别的路" |
| 穷尽方法后确实做不了 | **可以报 blocked** | 必须附带你尝试了什么、每种结果是什么 |

**只有以下情况才能报 blocked：**
1. 需要人类审批或授权（如 production deploy）
2. 依赖其他 Agent 未完成的具体产出物（且你已确认对方确实没完成）
3. 连续尝试 3+ 种**本质不同**的方法后仍然失败（必须列出每种方法和结果）

**绝对禁止（违反 = 3.25 绩效）：**
- 仅因为"仓库里没有X"就报 blocked（你可以 web_search 获取X）
- 不尝试任何工具就报 blocked
- 把"我不确定"当成 blocked（不确定就去查证）
- 重复尝试同一种方法然后放弃（必须切换到本质不同的方案）

## 强制审查（每个任务都会执行，无例外）

你的每份交付都会被独立 AI Reviewer **强制审查**，不论任务类型（代码/文档/调研均审）。
审查结果分级为 P0-P3。发现 P0 或 P1 问题时你的任务会被标记为 **blocked**，通知主人定夺。

**审查标准：**
1. **产出物完整**：承诺做什么就交付什么，不能只交半成品
2. **证据链可追溯**：每个结论都要有来源（URL、文件路径、搜索记录）
3. **冰山法则**：解决一个问题时，检查同类问题是否也存在
4. **闭环验证**：声称"完成"的工作必须有验证证据（文件存在、内容正确、可打开）
5. **安全性**：不引入致命 bug、数据丢失风险、未处理异常
6. **一致性**：变更与 AGENTS.md 约定和已有架构保持一致
"""


def extract_project_context(readme_path: Path) -> str:
    """Extract Status/Priority/Mission and recent log entries from README.md."""
    if not readme_path.is_file():
        return "(no project README)"

    content = readme_path.read_text(errors="replace")
    parts: list[str] = []

    for field in ("Status", "Priority", "Mission"):
        match = re.search(rf"{field}:\s*(.+)", content, re.IGNORECASE)
        if match:
            parts.append(f"{field}: {match.group(1).strip()}")

    log_match = re.search(r"## Log\s*\n((?:### .+\n(?:(?!##).+\n)*)+)", content)
    if log_match:
        log_entries = re.findall(r"### (\d{4}-\d{2}-\d{2})\n((?:(?!###).+\n)*)", log_match.group(1))
        for date, body in log_entries[:3]:
            summary = body.strip()[:200]
            parts.append(f"Log {date}: {summary}")

    done_when = re.search(r"Done when:\s*(.+)", content, re.IGNORECASE)
    if done_when:
        parts.append(f"Done when: {done_when.group(1).strip()}")

    open_qs = re.search(r"## Open questions\s*\n((?:(?!##).+\n)*)", content)
    if open_qs:
        questions = [
            q.strip().lstrip("- ")
            for q in open_qs.group(1).strip().splitlines()
            if q.strip() and q.strip() != "(to be filled)"
        ]
        if questions:
            parts.append(f"Open questions: {'; '.join(questions[:3])}")

    return "\n".join(parts) or "(minimal project context)"


def _build_task_details(task: FleetTask) -> str:
    """Format task details for inclusion in prompt."""
    lines = [f"Task: {task.text}"]
    if task.done_when:
        lines.append(f"Done when: {task.done_when}")
    if task.why:
        lines.append(f"Why: {task.why}")
    if task.skill_type:
        lines.append(f"Skill type: {task.skill_type.value}")
    if task.zero_resource:
        lines.append("Note: This is a zero-resource task (minimal budget, but you CAN and SHOULD use web_search/web_fetch when needed)")
    return "\n".join(lines)


def _build_knowledge_prompt(
    task: FleetTask,
    project_context: str,
    session_id: str,
    constraints: str,
) -> str:
    return f"""\
You are a fleet knowledge worker (session: {session_id}).
Your role: research, analyze, and produce knowledge artifacts.

## Project Context
{project_context}

## Assignment
{_build_task_details(task)}

## Your Approach
1. Search existing literature/ and analysis/ for prior work
2. **If local repo lacks information, USE web_search to find it from the internet**
3. Use web_fetch to download papers, read abstracts, or grab metadata from arXiv/OpenReview/Google Scholar
4. Use run_shell with curl/wget to download PDFs when needed
5. Synthesize findings into a clear, structured document
6. Write output to the project's literature/ or analysis/ directory
7. If you find important follow-up questions, note them but do NOT create new tasks

**Remember: "repo is empty" is NOT a blocker — you have web_search and web_fetch to fill gaps.**

{constraints}
"""


def _build_implementation_prompt(
    task: FleetTask,
    project_context: str,
    session_id: str,
    constraints: str,
) -> str:
    return f"""\
You are a fleet implementation worker (session: {session_id}).
Your role: write code, tests, and technical artifacts.

## Project Context
{project_context}

## Assignment
{_build_task_details(task)}

## Your Approach
1. Read relevant existing code to understand the current state
2. Plan your changes (keep them minimal and focused)
3. Implement the changes
4. Verify your changes work (run tests if applicable)
5. Commit with a clear message including [fleet/{session_id}]

{constraints}
"""


def _build_default_prompt(
    task: FleetTask,
    project_context: str,
    session_id: str,
    constraints: str,
) -> str:
    return f"""\
You are a fleet worker (session: {session_id}).
Complete the assigned task efficiently and accurately.

## Project Context
{project_context}

## Assignment
{_build_task_details(task)}

## Your Approach
1. Understand the task requirements
2. Gather context from existing files
3. **If you need information not in the repo, use web_search / web_fetch to find it**
4. **If you need to download files, use run_shell with curl/wget**
5. Execute the task and produce deliverables
6. Verify your work
7. Commit results with [fleet/{session_id}] in the message

**You have full tool access: web_search, web_fetch, run_shell, read_file, write_file, search_text.**
**"Repo is empty" is NOT a valid blocker — go fetch what you need from the internet.**

{constraints}
"""


def build_fleet_prompt(
    task: FleetTask,
    session_id: str,
    repo_root: Path,
    worker_role: WorkerRole = WorkerRole.DEFAULT,
    max_turns: int = 64,
) -> str:
    """Build a self-contained prompt for a fleet worker.

    Pulls project context from README.md, selects role-specific template,
    and appends shared constraints.
    """
    readme_path = repo_root / "projects" / task.project / "README.md"
    project_context = extract_project_context(readme_path)
    constraints = SHARED_CONSTRAINTS.format(
        session_id=session_id,
        max_turns=max_turns,
    )

    builders = {
        WorkerRole.KNOWLEDGE: _build_knowledge_prompt,
        WorkerRole.IMPLEMENTATION: _build_implementation_prompt,
        WorkerRole.DEFAULT: _build_default_prompt,
    }

    builder = builders.get(worker_role, _build_default_prompt)
    return builder(task, project_context, session_id, constraints)
