# VibeCoding / AI 辅助编程调研

- 项目：`projects/zero-basics-plan`
- 任务：调研 VibeCoding / AI 辅助编程资料：说明概念、工作流、提示词基础、如何与 Cursor 配合完成小项目、常见误区与安全注意事项。
- 产出人：Fleet Worker `岛村-01-1774524411-7e6a52`
- 日期：2026-03-26

## 结论摘要

1. **VibeCoding 可以理解为“用自然语言驱动 AI 生成、修改、调试代码”的开发方式，但专业场景不能停留在“凭感觉生成代码”。** Google Cloud 将其概括为从逐行写代码转向通过对话式流程引导 AI 生成、优化、调试应用；IBM 将其描述为用户用自然语言表达意图，再由 AI 转成可执行代码。来源：
   - https://cloud.google.com/discover/what-is-vibe-coding
   - https://www.ibm.com/think/topics/vibe-coding
2. **最适合零基础学习者的 VibeCoding 不是“纯放手”，而是“负责任的 AI 辅助开发”。** Google Cloud 明确区分了 “Pure vibe coding” 与 “Responsible AI-assisted development”；后者要求用户对 AI 生成代码进行 review、test、understand，并对最终结果负责。来源：
   - https://cloud.google.com/discover/what-is-vibe-coding
3. **对零基础更稳妥的工作流是：明确目标 → 给上下文 → 让 AI 先产出最小版本 → 立刻运行验证 → 根据报错继续迭代。** Google Cloud 给出了 “Describe the goal → AI generates code → Execute and observe → Provide feedback and refine → Repeat” 的循环。来源：
   - https://cloud.google.com/discover/what-is-vibe-coding
4. **提示词基础不等于“玄学咒语”，而是把任务说清楚。** OpenAI 文档强调 GPT 模型通常受益于更明确的 instructions；Anthropic 文档把 clarity、examples、XML structuring、agentic systems 列为提示工程最佳实践核心。来源：
   - https://developers.openai.com/api/docs/guides/prompt-engineering
   - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
5. **Cursor 特别适合作为课程里的 VibeCoding 工具，但前提是先建立规则、终端与验证习惯。** Cursor 官方资料显示其可通过 Rules/AGENTS.md 提供持续指令、通过 Terminal 执行命令且支持 sandboxing、通过 Developing Features 强调 plan features、test-driven development、working code you can trust。来源：
   - https://cursor.com/docs/rules
   - https://cursor.com/docs/agent/tools/terminal
   - https://cursor.com/learn/creating-features
6. **初学者最大的风险不是 prompt 写得不够高级，而是没有验证、一次改太多、没看终端输出、把 AI 当权威。** 这和现有开发工具链调研的结论一致：AI 协作必须与运行、调试、复盘绑定。来源：
   - `projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`
   - https://cloud.google.com/discover/what-is-vibe-coding
   - https://cursor.com/docs/agent/debug-mode

## 1. 什么是 VibeCoding

## 1.1 概念解释

Google Cloud 将 vibe coding 定义为一种软件开发实践：开发者的主要角色从逐行写代码，转向通过对话式方式引导 AI assistant 生成、完善与调试应用。IBM 则将其描述为：用户用 plain speech 表达意图，AI 把这种 thinking 转换为 executable code，并在开发环境中充当实时给建议的 coding assistant。来源：

- https://cloud.google.com/discover/what-is-vibe-coding
- https://www.ibm.com/think/topics/vibe-coding

对《零基础计划》来说，可以把它翻译成更容易教学的说法：

> **VibeCoding = 你先说清楚想做什么，由 AI 帮你搭脚手架、改代码、解释报错；但你必须亲手运行、检查和确认。**

## 1.2 为什么它适合零基础者入门

它适合零基础，不是因为“可以不学编程”，而是因为它把最开始的门槛从“自己从空白页写代码”降成了“先把需求说清楚，再观察程序是否真的跑起来”。

对新手尤其有帮助的地方：

1. 能更快得到第一个可运行结果。
2. 能把“报错”从纯挫败变成可对话的学习材料。
3. 能更快接触项目结构、函数、文件、依赖这些真实开发对象。
4. 能把“提需求—看结果—改需求”的迭代习惯提前建立起来。

## 1.3 它不是什么

VibeCoding **不是**：

1. 不用理解代码。
2. AI 保证正确。
3. 可以跳过测试。
4. 可以直接把生成结果当生产代码。
5. 只靠一条神奇提示词就能自动完成复杂项目。

Google Cloud 对此给出了重要区分：

- **Pure vibe coding**：更偏探索式，甚至接近“忘记代码存在”，适合 throwaway weekend projects。
- **Responsible AI-assisted development**：AI 像 pair programmer，但用户仍需 review、test、understand、own 最终结果。

来源：
- https://cloud.google.com/discover/what-is-vibe-coding

对零基础课程，应该明确采用第二种。

## 2. 适合零基础的 AI 辅助编程工作流

## 2.1 官方材料可提炼出的最小闭环

Google Cloud 页面直接给出了一套代码级工作流：

1. Describe the goal
2. AI generates code
3. Execute and observe
4. Provide feedback and refine
5. Repeat

来源：
- https://cloud.google.com/discover/what-is-vibe-coding

把它翻译成教学可执行版，可以写成 6 步：

### 第一步：先说目标，不先说实现

先描述“我要做什么”，而不是上来就说“给我写一堆复杂代码”。

例子：
- 不好：`帮我写一个很厉害的网站。`
- 更好：`请帮我做一个命令行记账工具，支持新增一条收支记录、查看所有记录，并把数据保存到本地 JSON 文件。先给最小可运行版本。`

### 第二步：补上下文和约束

让 AI 知道：
- 你使用什么语言
- 你现在在哪个目录
- 你是新手还是已有基础
- 你希望它一次改几个文件
- 你希望它给出运行命令还是只给代码

### 第三步：先要最小可运行版本

不要一开始让 AI 实现“登录、数据库、图表、部署、UI 美化”全套。先要一个能运行的最小版本。

### 第四步：立刻运行，不靠脑补验收

运行命令、看终端输出、看报错、看生成文件，是 AI 编程中最重要的事实来源。

### 第五步：把反馈具体化

反馈不要说“还是不对”。要说：
- 实际运行了什么命令
- 出现了什么报错
- 期望结果是什么
- 哪一步与期望不符

### 第六步：每轮只改一个主要问题

如果同一轮同时让 AI 改功能、重构结构、换依赖、修 bug，初学者几乎无法定位问题来源。

## 2.2 零基础课程适用的工作流模板

推荐固定模板：

1. **目标**：我要做什么小功能？
2. **上下文**：我在用什么语言/工具？当前文件有哪些？
3. **约束**：先只做最小版本；尽量只改 1~2 个文件；给出运行命令。
4. **产出要求**：给完整代码、文件路径、运行命令、预期输出。
5. **验证**：我实际运行，记录结果。
6. **下一轮修正**：告诉 AI 哪一步失败。

## 2.3 为什么这套流程比“直接让 AI 全做”更稳

因为新手最缺的不是生成代码的速度，而是：

1. 识别当前问题在哪。
2. 知道结果是否真实可运行。
3. 知道哪个改动引入了 bug。
4. 知道下一轮应该如何描述问题。

这和 Cursor Learn 中 “Developing Features” 强调的内容一致：**plan features、use test-driven development with agents、build working code you can trust**。来源：
- https://cursor.com/learn/creating-features

## 3. 提示词基础：给零基础者的最小规则

## 3.1 提示词基础原则

OpenAI 文档指出，GPT 模型通常受益于更明确的 instructions；Anthropic 文档则把 clarity、examples、XML structuring、thinking、agentic systems 作为最佳实践的一部分。来源：

- https://developers.openai.com/api/docs/guides/prompt-engineering
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

因此，零基础者的提示词原则可以简化为 5 条：

1. **先说目标**：你想得到什么。
2. **再说上下文**：你现在有什么文件、用什么语言、做到了哪一步。
3. **再说约束**：只能改哪些文件、先别做哪些功能。
4. **再说输出格式**：要代码、要步骤、要解释、还是要运行命令。
5. **如果有报错，贴完整报错。**

## 3.2 新手最实用的提示词骨架

### 骨架 A：从零生成功能

```text
你是我的编程助手。请帮我做一个最小可运行的 Python 小项目。

目标：做一个命令行待办事项工具，支持新增任务和查看任务列表。
上下文：我是零基础学习者；当前目录是一个空文件夹；我使用 Python 3。
约束：
1. 先只做最小版本
2. 最多创建 2 个文件
3. 不要引入第三方库
4. 代码后给出运行命令
5. 用注释解释关键代码

请按以下格式回答：
1. 将创建哪些文件
2. 每个文件的完整代码
3. 如何运行
4. 预期输出是什么
```

### 骨架 B：报错修复

```text
我运行了下面的命令：python todo.py
出现了这个报错：
Traceback ...

请你：
1. 用简单语言解释报错原因
2. 只做最小修复，不要重写整个项目
3. 告诉我需要修改哪一行或哪一段
4. 修改后给我重新运行的命令
```

### 骨架 C：让 AI 解释代码

```text
请你逐段解释下面这段 Python 代码。
要求：
1. 用零基础能理解的语言
2. 每段先说“它在做什么”
3. 再说“为什么这样写”
4. 最后告诉我如果改错最可能报什么错
```

### 骨架 D：让 AI 协助重构

```text
下面这段代码已经能运行，但太乱了。
请你：
1. 不改变功能
2. 只做小规模重构
3. 优先提升变量名、函数拆分和注释
4. 修改后告诉我如何验证功能没有变
```

## 3.3 提示词写法中的常见有效元素

结合 OpenAI / Anthropic 官方文档，可以总结出对初学者最有帮助的元素：

1. **明确 instructions**：把要求写清楚。
2. **给 examples**：需要输出格式时给一个小例子。
3. **结构化表达**：用编号、标题、代码块，而不是一大段话。
4. **指定边界**：例如“不要引入新依赖”“只改一个文件”。
5. **要求验证方式**：例如“给出运行命令和预期输出”。

来源：
- https://developers.openai.com/api/docs/guides/prompt-engineering
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

## 4. 如何与 Cursor 配合完成一个小项目

## 4.1 为什么 Cursor 适合这类课程

Cursor 官方文档中，与本任务最相关的能力包括：

1. **Rules**：可设置 Project / Team / User Rules，并支持 `AGENTS.md` 作为持续指令来源。来源：
   - https://cursor.com/docs/rules
2. **Terminal**：Agent 可执行命令，并带 sandboxing、preserved history、native terminal integration，可配置 `sandbox.json` 控制 network 和 filesystem policies。来源：
   - https://cursor.com/docs/agent/tools/terminal
3. **Developing Features**：强调 plan features、test-driven development、working code you can trust。来源：
   - https://cursor.com/learn/creating-features
4. **Debug Mode**：强调 hypothesis generation、log instrumentation、runtime analysis。来源：
   - https://cursor.com/docs/agent/debug-mode

这些点非常适合教学，因为它们天然对应：规则、执行、验证、调试。

## 4.2 推荐的小项目类型

适合零基础的项目应满足：

1. 30~90 分钟内能完成最小版本。
2. 文件数少，最好 1~3 个文件。
3. 不依赖复杂前端或数据库。
4. 运行结果一眼可见。
5. 容易引出“报错—修复—再验证”的循环。

推荐题目：

1. 命令行待办事项工具
2. 单词统计器
3. 文本记账工具
4. 猜数字游戏
5. 批量重命名脚本
6. 简单 Markdown 日记整理器

## 4.3 与 Cursor 配合的标准流程

下面给出适合放入教程的 Cursor 小项目流程。

### 阶段 1：先建立项目规则

在项目根目录先写一份简短规则，约束 AI 行为。可写进 `AGENTS.md` 或项目规则文档。

示例：

```markdown
# Project Rules

1. 我是零基础学习者，请优先解释，再改代码。
2. 每次尽量只改一个文件。
3. 先做最小可运行版本，不要过度设计。
4. 回答时必须给运行命令。
5. 如果修改了逻辑，请说明如何验证。
6. 如果不确定，请明确写出假设。
```

这样做的依据是 Cursor Rules 文档明确支持 Project / Team / User Rules 以及 `AGENTS.md`。来源：
- https://cursor.com/docs/rules

### 阶段 2：让 Cursor 先搭最小版本

示例 prompt：

```text
请帮我做一个最小可运行的 Python 命令行待办事项工具。
要求：
1. 只用标准库
2. 先支持 add 和 list 两个命令
3. 数据保存在 tasks.json
4. 最多创建 2 个文件
5. 给出完整代码和运行命令
```

### 阶段 3：人工运行

在 Cursor Terminal 或系统终端里实际执行，例如：

```bash
python todo.py add "买牛奶"
python todo.py list
```

关键不是“AI 说应该能跑”，而是你真的跑了。

### 阶段 4：遇到报错就贴回去

示例 prompt：

```text
我运行了 `python todo.py list`，报错如下：
...
请你只做最小修复，不要重写项目。
修复后告诉我改了什么，以及我应该重新运行什么命令。
```

### 阶段 5：让 Cursor 帮你做小幅扩展

例如新增：
- `done` 命令
- 删除任务
- 按编号显示
- 更清晰的输出格式

但每次只加一项。

### 阶段 6：让 Cursor 帮你解释与重构

功能跑通之后，再问：

```text
请解释这份代码每个函数的作用，并给出一个小幅重构版本。
要求：
1. 不改变功能
2. 优先改善命名与结构
3. 给出回归验证步骤
```

## 4.4 一个完整的小项目教学脚本

可以直接纳入课程：

### 目标
做一个命令行待办事项工具。

### 课堂步骤

1. 新建空目录并打开 Cursor。
2. 写 Project Rules。
3. 让 Cursor 生成最小版 `todo.py`。
4. 在终端运行 add/list。
5. 故意制造一个小错误，例如删掉某个 import。
6. 用 Cursor 解释报错并修复。
7. 增加 `done` 功能。
8. 让 Cursor 帮忙重构函数。
9. 用 Git 提交一次版本。

### 课堂产出

1. `todo.py`
2. `tasks.json`
3. `README.md`
4. 一份 `ai-collaboration-notes.md`，记录：
   - 我给了哪些 prompt
   - 哪些修改是 AI 建议的
   - 我做了哪些验证
   - 出过什么错

## 5. 常见误区

## 5.1 把 AI 当成权威答案机

误区：AI 给出代码就默认正确。

风险：
- 逻辑错但不报错
- 看起来能跑，边界条件全坏
- 引入不必要依赖
- 偷偷改掉原本正确逻辑

改法：
- 必跑命令
- 必看输出
- 必写预期结果
- 必做最小回归验证

## 5.2 一次让 AI 改太多

误区：一轮里同时要求“修 bug + 加新功能 + 重构 + 美化输出”。

风险：
- 不知道哪一步引入新问题
- 回滚困难
- 新手无法理解改动

改法：
- 一轮只解决一个主问题
- 功能新增与 bug 修复分开做
- 每轮保存一个可运行版本

## 5.3 不给上下文，只给命令式要求

误区：`帮我修一下。`

风险：
- AI 不知道项目结构
- AI 猜错语言/框架/文件
- 容易给出错误补丁

改法：
- 说明文件名、运行命令、报错文本、目标行为

## 5.4 不保留验证证据

误区：只记得“好像修好了”。

风险：
- 过几天无法复现
- 不知道为什么好
- 无法写学习总结

改法：
- 记录 prompt
- 记录命令
- 记录终端输出
- 记录最终改动

## 5.5 只会“生成”，不会“解释”和“审查”

误区：把 AI 只当代码喷涌器。

更好的用法：
- 解释报错
- 解释已有代码
- 提出测试点
- 进行小幅重构
- 给出验证清单

## 6. 安全与风险注意事项

## 6.1 代码安全边界

对零基础者，最需要先建立的安全边界是：

1. **不要直接运行自己看不懂的危险命令。**
2. **不要把 API Key、密码、Token 直接贴进 prompt 或仓库。**
3. **不要让 AI 在未知项目里批量删除或覆盖文件。**
4. **不要让 AI 未经检查地安装一堆依赖。**
5. **不要把 AI 生成代码直接用于生产或真实敏感数据。**

## 6.2 使用 Cursor Terminal 时的注意事项

Cursor Terminal 文档明确提到 sandboxing、history、以及可配置 network / filesystem policies 的 `sandbox.json`。这意味着：

1. 终端是强能力工具。
2. 应让学习者知道“AI 能执行命令”不等于“命令天然安全”。
3. 教学中应优先使用受控目录、小项目、可回滚仓库。

来源：
- https://cursor.com/docs/agent/tools/terminal

## 6.3 隐私与密钥管理

教学中应明确禁止：

1. 把 `.env` 全文贴给 AI。
2. 把个人账号密码写进代码。
3. 直接公开推送带密钥的仓库。
4. 把公司代码或敏感业务数据直接喂给第三方模型。

建议最低配置：

1. 使用示例数据。
2. 把敏感信息写进 `.env`，不提交到 Git。
3. 用 `example.env` 或文档说明需要哪些变量。
4. 提交前检查 Git diff。

## 6.4 结果可靠性风险

AI 编程常见风险包括：

1. 幻觉出不存在的库 API。
2. 使用过时写法。
3. 生成不一致的文件结构。
4. 漏掉异常处理。
5. 在“看起来合理”的情况下埋入逻辑错误。

因此，课程里应固定要求至少做以下验证：

1. 能否运行。
2. 预期输入下是否正确。
3. 错误输入下是否可解释。
4. 修改后旧功能是否仍正常。

## 7. 可直接放进课程的教学建议

## 7.1 建议纳入 28 天课程的位置

结合现有框架，最适合把本主题放在 Week 3：

- Day 19：认识 Cursor 与规则
- Day 20：VibeCoding / AI 辅助编程入门
- Day 21：做一个整合小项目并复盘

对应关系与 `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md` 中的 Week 3 设计一致。来源：
- `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`

## 7.2 建议保留的主资料包

如果本主题只保留最重要的资料，建议优先使用：

1. Google Cloud: What is vibe coding  
   https://cloud.google.com/discover/what-is-vibe-coding
2. IBM: What is Vibe Coding  
   https://www.ibm.com/think/topics/vibe-coding
3. Cursor Docs: Rules  
   https://cursor.com/docs/rules
4. Cursor Docs: Terminal  
   https://cursor.com/docs/agent/tools/terminal
5. Cursor Learn: Developing Features  
   https://cursor.com/learn/creating-features
6. Cursor Docs: Debug Mode  
   https://cursor.com/docs/agent/debug-mode
7. OpenAI API Docs: Prompt engineering  
   https://developers.openai.com/api/docs/guides/prompt-engineering
8. Anthropic Docs: Prompting best practices  
   https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

## 7.3 零基础课程里应强调的底层习惯

1. **AI 生成前先写目标。**
2. **AI 生成后先运行。**
3. **报错后贴证据，不贴情绪。**
4. **每轮只改一个主要问题。**
5. **提交前复查代码、输出和 Git diff。**
6. **任何自动化能力都要配套边界与回滚意识。**

## 8. Open questions

1. 是否需要补一份“面向中文零基础学习者的 VibeCoding 常见 prompt 模板速查表”？
2. 是否要为 Cursor 之外补一个“通用 AI 编程工作流”，以兼容 ChatGPT / Claude / Gemini / Copilot？
3. 是否在最终教程中单独加入“AI 生成代码审查清单”，作为每次实操后的固定作业？

## Provenance

本文件结论来自以下实际检索、抓取与命令验证：

### 直接来源 URL

- https://cloud.google.com/discover/what-is-vibe-coding
- https://www.ibm.com/think/topics/vibe-coding
- https://cursor.com/docs/rules
- https://cursor.com/docs/agent/tools/terminal
- https://cursor.com/learn/creating-features
- https://cursor.com/docs/agent/debug-mode
- https://developers.openai.com/api/docs/guides/prompt-engineering
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- `projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`
- `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`

### 抓取与提取命令

1. 页面标题与描述抽取：

```bash
python3 - <<'PY'
import urllib.request, re
urls = [
 ('cursor_rules','https://cursor.com/docs/rules'),
 ('cursor_terminal','https://cursor.com/docs/agent/tools/terminal'),
 ('cursor_features','https://cursor.com/learn/creating-features'),
 ('cursor_agents','https://cursor.com/learn/agents'),
 ('cursor_customizing','https://cursor.com/learn/customizing-agents'),
 ('cursor_debug','https://cursor.com/docs/agent/debug-mode'),
 ('google_vibe','https://cloud.google.com/discover/what-is-vibe-coding'),
 ('ibm_vibe','https://www.ibm.com/think/topics/vibe-coding'),
]
...
PY
```

2. Google Cloud vibe coding 页面关键句提取：

```bash
python3 - <<'PY'
import urllib.request,re
url='https://cloud.google.com/discover/what-is-vibe-coding'
...
for phrase in ['Pure vibe coding','Responsible AI-assisted development','Describe the goal','Execute and observe','Provide feedback and refine']:
    ...
PY
```

3. IBM vibe coding 页面关键句提取：

```bash
python3 - <<'PY'
import urllib.request,re
url='https://www.ibm.com/think/topics/vibe-coding'
...
for phrase in ['Vibe coding is a fresh take in coding where users express their intention using plain speech', 'AI transforms that thinking into executable code']:
    ...
PY
```

4. OpenAI 提示工程页面关键词提取：

```bash
python3 - <<'PY'
import urllib.request,re
url='https://developers.openai.com/api/docs/guides/prompt-engineering'
...
for phrase in ['few-shot', 'explicit instructions', 'consistent behavior']:
    ...
PY
```

5. Anthropic 提示最佳实践页面关键句提取：

```bash
python3 - <<'PY'
import urllib.request,re
url='https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices'
req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
...
for phrase in ['Comprehensive guide to prompt engineering techniques', 'clarity', 'examples', 'XML structuring', 'agentic systems']:
    ...
PY
```
