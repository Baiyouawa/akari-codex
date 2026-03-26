# zero-basics-plan 重启现状说明

- 项目：`projects/zero-basics-plan`
- 日期：2026-03-26
- 会话：`侑-00-1774525428-74a7b7`
- 状态：restart note / current-state snapshot

## 1. 一句话结论

`zero-basics-plan` 已经完成了 **课程框架 + 6 份专题调研 + 1 份完整教程草案** 的第一轮搭建，当前并不是“从零开始”，而是进入了 **收口、审查、补齐缺口、从草案转正式文档** 的阶段。

## 2. 当前项目状态

### 2.1 已有核心交付物

截至本次梳理，项目内已落盘的核心 Markdown 交付物共 `8 + 1 = 9` 份：

- 课程框架：`1` 份
- 专题调研：`6` 份
- 重启现状说明：`1` 份（本文）
- 完整教程草案：`1` 份

内联算术：`1 + 6 + 1 + 1 = 9`。

对应文件：

1. `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`
2. `projects/zero-basics-plan/analysis/2026-03-26-linux-beginner-resource-survey.md`
3. `projects/zero-basics-plan/analysis/git-github-beginners-research.md`
4. `projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`
5. `projects/zero-basics-plan/analysis/2026-03-26-vibecoding-ai-assisted-programming-research.md`
6. `projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md`
7. `projects/zero-basics-plan/analysis/2026-03-26-deep-learning-beginner-resource-survey.md`
8. `projects/zero-basics-plan/analysis/2026-03-26-practice-project-cases.md`
9. `projects/zero-basics-plan/zero-basics-plan-course-draft.md`

### 2.2 当前最重要的事实

1. **28 天四周课程骨架已经存在。**
   - 来源：`projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`
2. **Linux / Git-GitHub / 工具链 / VibeCoding / Python / 深度学习 6 条专题线都已有独立调研。**
   - 来源：上文列出的 6 份专题调研文件
3. **完整教程草案已经存在，不需要再从空白文档起草。**
   - 来源：`projects/zero-basics-plan/zero-basics-plan-course-draft.md`
4. **项目真正缺的不是“有没有内容”，而是“状态一致性、资料审查、正式执行方案、Humanize 审查、草案转正式教程拆分”。**
   - 来源：`projects/zero-basics-plan/TASKS.md` 中未完成任务；本文第 5 节汇总

## 3. 已有文档盘点

### 3.1 课程主文档

#### A. 课程框架总表
- 文件：`projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`
- 作用：冻结 4 周 / 28 天结构、每日目标、实操任务、配套资料、周复盘设计。
- 当前价值：是后续所有正式教程拆分的结构母版。
- 证据：已有验证日志记录该文件包含 `28` 个 `### Day` 小节。
  - 来源：`projects/zero-basics-plan/logs/2026-03-26T19:29:10+08:00-fleet-结衣-03-1774524471-df6c5a-course-framework-verification.md`

#### B. 完整教程草案
- 文件：`projects/zero-basics-plan/zero-basics-plan-course-draft.md`
- 作用：将课程说明、四周目标、28 天安排、周末系统课程、产出要求、AI 使用约束、后续拆分建议整合到单文档。
- 当前价值：可直接作为后续“正式版教程”的底稿。
- 证据：已有验证日志记录该文件 `wc -l` 输出为 `751`。
  - 来源：`projects/zero-basics-plan/logs/2026-03-26T19:34:36+08:00-fleet-智乃-02-1774524802-39277a-course-draft.md`

### 3.2 专题调研文档

#### Linux
- 文件：`projects/zero-basics-plan/analysis/2026-03-26-linux-beginner-resource-survey.md`
- 覆盖：文件系统、常用命令、权限、软件安装、Shell、实战练习。
- 当前价值：可直接支撑 Week 1 详细讲义。

#### Git / GitHub
- 文件：`projects/zero-basics-plan/analysis/git-github-beginners-research.md`
- 覆盖：版本控制概念、仓库初始化、commit、branch、merge、rebase、remote、Issue、PR、协作流程。
- 当前价值：可直接支撑 Week 2 详细讲义。

#### 开发工具链
- 文件：`projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`
- 覆盖：Cursor、VS Code、终端、包管理、环境配置、调试、VibeCoding 实践。
- 当前价值：是 Week 3 工具层设计依据。

#### VibeCoding / AI 辅助编程
- 文件：`projects/zero-basics-plan/analysis/2026-03-26-vibecoding-ai-assisted-programming-research.md`
- 覆盖：概念、工作流、提示词基础、Cursor 配合小项目、误区、安全风险。
- 当前价值：可以单独拆成“AI 协作规则附录”。

#### Python 与编程基础
- 文件：`projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md`
- 覆盖：语法、数据结构、函数、模块、文件读写、虚拟环境。
- 当前价值：Week 3 编程基本功主支撑。

#### 基础深度学习
- 文件：`projects/zero-basics-plan/analysis/2026-03-26-deep-learning-beginner-resource-survey.md`
- 覆盖：Python 科学计算、NumPy、PyTorch、张量、自动求导、简单神经网络、训练与推理。
- 当前价值：Week 4 主支撑。

#### 实践项目案例
- 文件：`projects/zero-basics-plan/analysis/2026-03-26-practice-project-cases.md`
- 覆盖：20 个练习 / 小项目 + 28 天练习映射表。
- 当前价值：弥补“课程有知识点但缺练习映射”的问题。

### 3.3 辅助文件

- 计划文件：`projects/zero-basics-plan/plans/2026-03-26-course-framework.md`
- 项目状态文件：`projects/zero-basics-plan/README.md`
- 任务文件：`projects/zero-basics-plan/TASKS.md`
- 历史会话日志：`projects/zero-basics-plan/logs/*.md`
- 原始资料审查数据：
  - `projects/zero-basics-plan/analysis/2026-03-26-resource-audit-raw.json`
  - `projects/zero-basics-plan/analysis/audit-dev-toolchain.json`
  - `projects/zero-basics-plan/analysis/audit-git-github.json`
  - `projects/zero-basics-plan/analysis/audit-linux.json`

## 4. 当前待办梳理

### 4.1 已完成但之前在 TASKS 中状态不一致的事项

本次梳理发现，以下 2 个任务已经有实际交付物和会话日志，但 `TASKS.md` 中此前仍显示未完成：

1. `调研 VibeCoding / AI 辅助编程资料`
   - 已有交付：`projects/zero-basics-plan/analysis/2026-03-26-vibecoding-ai-assisted-programming-research.md`
   - 来源：`projects/zero-basics-plan/logs/2026-03-26T19:29:39+08:00-fleet-岛村-01-1774524411-7e6a52-vibecoding-research.md`
2. `调研实践项目案例`
   - 已有交付：`projects/zero-basics-plan/analysis/2026-03-26-practice-project-cases.md`
   - 来源：`projects/zero-basics-plan/logs/2026-03-26T19:34:13+08:00-fleet-岛村-01-1774524772-3cf537-practice-project-cases.md`

本次已同步修正 `projects/zero-basics-plan/TASKS.md` 状态，避免后续重复认领。

### 4.2 当前真正未完成的任务

按 `projects/zero-basics-plan/TASKS.md`，当前仍未完成的主任务有 `9` 项：

1. 对所有收集到的资料进行可追溯性审查
2. 梳理 zero-basics-plan 当前项目状态、现有待办、已有文档与缺口
3. 制定《零基础计划》顶层执行方案
4. 基于顶层方案拆解为周计划与每日计划，并标记 Humanize review 检查点
5. 调用 Humanize 流程对顶层计划进行独立审查
6. 若 Humanize 审查发现问题，迭代修订计划并再次审查
7. 在计划通过后，为各模块收集高质量资料与练习资源，并建立可追溯来源
8. 汇总为 Markdown 主文档骨架
9. 对最终文档骨架执行 Humanize 审查

内联算术：当前未完成主任务数 `= 9`，以本次更新后的 `TASKS.md` 为准。

## 5. 项目缺口分析

### 5.1 已补上的部分

以下工作已经不再是主要缺口：

- 课程有没有 28 天结构：**已补上**
- Linux / Git / Python / 深度学习有没有调研：**已补上**
- VibeCoding / Cursor 有没有系统材料：**已补上**
- 是否有练习 / 小项目映射：**已补上**
- 是否有完整教程草案：**已补上**

### 5.2 仍然存在的缺口

#### 缺口 1：资料审查没有收口成正式结论文档
虽然项目目录下已经有原始审查 JSON，但还没有一份面向人的正式总结文档，把“哪些链接可访问、哪些页面异常、哪些适合初学者、哪些需要替代”收口成稳定结论。

- 来源：
  - `projects/zero-basics-plan/analysis/2026-03-26-resource-audit-raw.json`
  - `projects/zero-basics-plan/analysis/audit-dev-toolchain.json`
  - `projects/zero-basics-plan/analysis/audit-git-github.json`
  - `projects/zero-basics-plan/analysis/audit-linux.json`
  - `projects/zero-basics-plan/TASKS.md`

#### 缺口 2：课程草案尚未升级为“顶层执行方案 + 分层计划”
目前已有“课程怎么学”的草案，但还缺“项目如何组织生产”的执行层文档，包括：目标人群、交付标准、阶段里程碑、审批点、拆分方式、review 节点。

- 来源：`projects/zero-basics-plan/TASKS.md`

#### 缺口 3：还没有 Humanize 独立审查闭环
任务列表里已经明确要求对顶层计划和最终文档骨架做 Humanize 审查，但目前项目日志中尚未看到对应审查通过记录。

- 来源：`projects/zero-basics-plan/TASKS.md`
- 补充观察：现有 `projects/zero-basics-plan/logs/` 文件主要是 worker 产出日志，未见 Humanize 审查结果文件。

#### 缺口 4：正式教程仍是单大文件，尚未拆章
当前 `zero-basics-plan-course-draft.md` 已能阅读，但对最终交付而言，仍偏“大草案”，还没有拆成按周、按模块、按附录组织的正式结构。

- 来源：
  - `projects/zero-basics-plan/zero-basics-plan-course-draft.md`
  - 其中 `## 8. 后续可拆分的正式文档结构`

#### 缺口 5：开放问题还未决
以下 3 个开放问题仍会影响最终教程形态：

1. 是否分别制作 Windows / macOS / Linux 三套安装截图教程
2. 第 3 周统一使用 VS Code，还是允许 Cursor 作为升级路线
3. 是否补充中文视频教程以降低英文门槛

- 来源：`projects/zero-basics-plan/README.md` 的 `## Open questions`

## 6. 建议的重启切入顺序

如果下一位 agent 继续推进，建议按下面顺序接手：

### Step 1：先做资料审查收口
把现有 JSON 审查结果整理成 1 份人类可读的 `resource-audit-summary.md`，把坏链、弱链接、强推荐、备选资源全部写清楚。

原因：这一步能把“资料是否可用”这件事先钉住，避免后续正式写教程时反复返工。

### Step 2：把课程草案上升为顶层执行方案
新增一份顶层方案文档，明确：
- 目标读者
- 每周成果要求
- 教程拆分结构
- 每个模块的审查点
- 哪些地方必须 Humanize

原因：当前内容够多，但生产流程还没固定。

### Step 3：做 Humanize 审查
先审顶层方案，再审最终文档骨架。

原因：项目已经从“收集资料”进入“保证可落地与适合零基础”的阶段，独立审查的收益变高。

### Step 4：拆正文
把单文件草案拆成：
- `01-course-overview.md`
- `02-week1-linux.md`
- `03-week2-git-github.md`
- `04-week3-python-cursor-vibecoding.md`
- `05-week4-deep-learning.md`
- `06-resource-audit.md`

原因：方便后续并行维护、插图、审查与迭代。

## 7. 本次梳理后的结论

`zero-basics-plan` 当前最适合被理解为：

> **已经完成第一轮课程研发，尚未完成第二轮治理与成稿。**

更具体地说：

- **内容底座已成型**：课程框架、专题调研、练习案例、完整草案都已具备。
- **状态治理刚补齐一部分**：本次修正了 `TASKS.md` 中已完成任务的状态漂移。
- **后续重点不再是盲目补资料，而是审查、定稿、拆章、评审闭环。**

## 8. Provenance

### 项目内文件
- `projects/zero-basics-plan/README.md`
- `projects/zero-basics-plan/TASKS.md`
- `projects/zero-basics-plan/plans/2026-03-26-course-framework.md`
- `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`
- `projects/zero-basics-plan/analysis/2026-03-26-linux-beginner-resource-survey.md`
- `projects/zero-basics-plan/analysis/git-github-beginners-research.md`
- `projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`
- `projects/zero-basics-plan/analysis/2026-03-26-vibecoding-ai-assisted-programming-research.md`
- `projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md`
- `projects/zero-basics-plan/analysis/2026-03-26-deep-learning-beginner-resource-survey.md`
- `projects/zero-basics-plan/analysis/2026-03-26-practice-project-cases.md`
- `projects/zero-basics-plan/analysis/2026-03-26-resource-audit-raw.json`
- `projects/zero-basics-plan/analysis/audit-dev-toolchain.json`
- `projects/zero-basics-plan/analysis/audit-git-github.json`
- `projects/zero-basics-plan/analysis/audit-linux.json`
- `projects/zero-basics-plan/zero-basics-plan-course-draft.md`

### 会话日志
- `projects/zero-basics-plan/logs/2026-03-26T19:29:39+08:00-fleet-岛村-01-1774524411-7e6a52-vibecoding-research.md`
- `projects/zero-basics-plan/logs/2026-03-26T19:34:13+08:00-fleet-岛村-01-1774524772-3cf537-practice-project-cases.md`
- `projects/zero-basics-plan/logs/2026-03-26T19:34:36+08:00-fleet-智乃-02-1774524802-39277a-course-draft.md`
- `projects/zero-basics-plan/logs/2026-03-26T19:29:10+08:00-fleet-结衣-03-1774524471-df6c5a-course-framework-verification.md`

### 验证命令
- `wc -l projects/zero-basics-plan/analysis/*.md projects/zero-basics-plan/zero-basics-plan-course-draft.md`
- `find projects/zero-basics-plan/logs -maxdepth 1 -type f | sort`
- `python3 - <<'PY' ... print(task lines from projects/zero-basics-plan/TASKS.md) ... PY`
