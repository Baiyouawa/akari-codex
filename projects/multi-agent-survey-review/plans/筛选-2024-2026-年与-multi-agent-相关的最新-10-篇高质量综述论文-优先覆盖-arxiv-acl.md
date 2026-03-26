# 筛选 2024-2026 年与 multi-agent 相关的最新 10 篇高质量综述论文，优先覆盖 arXiv、ACL Anthology、OpenReview、期刊与顶会教程/综述

Generated: 2026-03-26

## Goal Description
围绕“multi-agent”主题，快速恢复并并行推进综述调研工作，在 2024-2026 时间范围内筛选出最新且高质量的 10 篇综述类论文。候选来源优先覆盖 arXiv、ACL Anthology、OpenReview，以及期刊论文、顶会 tutorial / survey / overview 类文章。最终产出应包含一份可复核的候选池、明确的筛选标准、去重与质量评估结果，以及最终入选的 10 篇论文清单与简要说明，确保结果具备时效性、代表性、质量可靠性与来源多样性，便于后续继续开展深入综述写作或研究跟踪。

## Acceptance Criteria

- AC-1: 检索范围覆盖 2024-2026 年，并以 multi-agent 为核心主题
  - Positive Tests: 候选论文发表或公开时间在 2024-01-01 至 2026-12-31 之间；标题、摘要或关键词明确涉及 multi-agent / multi-agent systems / LLM-based multi-agent / agent collaboration / agent society 等相关主题
  - Negative Tests: 纳入 2023 年及以前论文；仅涉及单智能体而无明确多智能体内容；主题偏离 multi-agent 协作、系统、框架或综述方向

- AC-2: 最终结果为“10 篇综述类论文”，且每篇都具备综述属性
  - Positive Tests: 论文标题或正文明确为 survey / review / overview / tutorial / taxonomy / systematic review；内容以总结、归纳、分类、比较、挑战与趋势分析为主
  - Negative Tests: 纳入原始研究论文、benchmark 论文、方法论文、系统演示论文；仅有少量 related work 但并非综述性质的文章

- AC-3: 来源优先覆盖 arXiv、ACL Anthology、OpenReview、期刊与顶会教程/综述，且具备来源多样性
  - Positive Tests: 候选池包含上述多个来源；最终 10 篇中至少体现不同类型来源的代表性文章，如预印本、会议平台、期刊或教程文章
  - Negative Tests: 结果全部来自单一平台；完全忽略 ACL Anthology、OpenReview 或期刊/教程类来源

- AC-4: 建立明确、可复核的筛选标准，并完成去重
  - Positive Tests: 输出中包含检索关键词、来源平台、纳入/排除规则、排序依据；同一论文的 arXiv 与会议版本完成合并去重并保留最佳版本
  - Negative Tests: 未说明筛选逻辑；同一论文重复计入；无法解释为何某篇被保留或剔除

- AC-5: 每篇入选论文都附带必要元信息与入选理由
  - Positive Tests: 每条记录至少包含标题、作者、年份、来源平台、链接、综述类型、主题覆盖范围、入选理由；可快速支撑后续阅读
  - Negative Tests: 只给标题列表；缺少链接或来源信息；没有说明其高质量或代表性的依据

- AC-6: “高质量”判定有一致标准，而非仅凭主观印象
  - Positive Tests: 采用综合评价维度，如来源可信度、内容完整性、引用/讨论热度、作者与机构背景、是否被社区广泛传播、是否为教程或领域性综述；对每篇给出简要质量判断
  - Negative Tests: 仅以“感觉重要”筛选；无质量评分或质量说明；把低相关度但高热度论文误判为高质量综述

- AC-7: 支持并行执行与快速恢复
  - Positive Tests: 将任务拆分为并行子流，如来源分工、初筛、复筛、去重、质量评估、终选；每个子流有清晰输入输出
  - Negative Tests: 计划完全串行；无法在中途中断后恢复；没有统一表结构导致多人结果难以汇总

- AC-8: 输出结果应适合后续继续扩展为系统调研
  - Positive Tests: 保留候选池与备选论文；记录排除原因；可按子主题扩展，如 LLM-based multi-agent、coordination、communication、planning、agent society
  - Negative Tests: 只输出最终 10 篇，无过程记录；无法复用到下一轮调研

## Path Boundaries

### Upper Bound (Maximum Scope)
最完整方案包括：
1. 同步检索 arXiv、ACL Anthology、OpenReview、Google Scholar、DBLP、Semantic Scholar、Web of Science / Scopus、主要期刊官网、顶会 tutorial 页面。
2. 使用多组关键词组合，覆盖“multi-agent + survey/review/tutorial/overview/taxonomy/systematic review + LLM/coordination/collaboration/planning/communication/society”等细分方向。
3. 建立候选池不少于 40-80 篇记录，并保留检索日志。
4. 对候选论文进行两轮筛选：题名摘要初筛 + 全文/结构复筛。
5. 对重复版本进行规范化合并，优先保留正式出版版本；若正式版本不可得则保留 arXiv 版本。
6. 对每篇候选论文进行统一质量评分，并输出排序结果。
7. 最终给出 10 篇主清单 + 5-10 篇备选清单，并按子主题分组说明。
8. 产出可直接交付的 Markdown/表格结果，支持继续写综述。

### Lower Bound (Minimum Scope)
最简可行方案包括：
1. 至少检索 arXiv、ACL Anthology、OpenReview 三类核心来源，并补充期刊或顶会教程类来源至少一种。
2. 建立不少于 20 篇候选论文的初始池。
3. 完成基本去重与综述属性判断。
4. 从中筛选出 10 篇 2024-2026 年的高相关综述论文。
5. 为每篇提供标题、年份、来源、链接、简要入选理由。
6. 保留至少一份简单的排除规则说明，确保结果可复核。

### Allowed Choices
- Can use: arXiv、ACL Anthology、OpenReview、DBLP、Google Scholar、Semantic Scholar、Crossref、期刊官网、会议官网、教程页面、论文 PDF 标题/摘要/章节结构、引用信息、作者主页、机构主页、公开元数据、表格化候选池、人工复核
- Cannot use: 不可验证的二手转述、无出处的社交媒体结论、仅凭标题猜测的纳入判断、超出 2024-2026 时间范围的最终入选论文、非综述性质论文替代综述论文、重复版本重复计数、无链接或无来源记录的条目

## Dependencies and Sequence

### Milestones
1. 明确任务定义与统一筛选口径
   - 统一“multi-agent”主题边界
   - 统一“综述类论文”定义
   - 统一时间范围、来源优先级与质量判断维度
   - 输出字段模板，便于并行汇总

2. 建立并行检索子任务
   - 子流 A：arXiv 检索
   - 子流 B：ACL Anthology 检索
   - 子流 C：OpenReview 检索
   - 子流 D：期刊与顶会 tutorial / survey 页面检索
   - 每个子流独立产出候选条目与原始证据

3. 汇总候选池并标准化字段
   - 合并各来源结果
   - 统一标题、作者、年份、venue、链接、版本信息、摘要、关键词
   - 标记来源类型与子主题标签

4. 执行第一轮筛选
   - 按时间范围、主题相关性、综述属性进行题名摘要初筛
   - 删除明显不相关、非综述、时间不符条目
   - 保留初筛通过与待人工判断条目

5. 执行去重与版本合并
   - 识别同名或近似标题论文
   - 合并 arXiv 与会议/期刊正式版本
   - 确定主记录与备用链接

6. 执行第二轮质量评估
   - 依据来源可信度、内容结构完整性、覆盖广度、社区影响信号、作者背景进行评分
   - 标记高优先级、边界案例、备选项
   - 对有争议条目做人工复核

7. 形成最终 10 篇清单
   - 检查来源多样性与主题覆盖
   - 若同类论文过多，优先保留代表性更强、更新、更系统的综述
   - 补足教程类或期刊类高质量综述，避免来源失衡

8. 生成可交付结果
   - 输出最终 10 篇清单
   - 附每篇的元信息与入选理由
   - 附候选池、排除原因、备选论文与后续扩展方向

## Implementation Notes
- 建议先建立统一表头：标题、作者、年份、来源平台、venue、版本、链接、是否综述、主题标签、质量评分、纳入状态、排除原因、备注
- 检索关键词建议采用核心词与扩展词组合：
  - 核心主题词：multi-agent, multi-agent systems, multiple agents, agent collaboration, agent society
  - 大模型相关词：LLM-based multi-agent, language agents, AI agents, autonomous agents
  - 综述词：survey, review, overview, tutorial, taxonomy, systematic review
- 检索表达可按来源微调，例如：
  - arXiv：ti/abs 包含 “multi-agent” AND “survey|review|overview|tutorial”
  - ACL Anthology：multi-agent + survey/review/tutorial
  - OpenReview：multi-agent + survey/review/overview
- 对“高质量”的建议评分维度：
  - 来源可信度
  - 是否正式发表或被顶会/期刊/教程采纳
  - 是否具备完整综述结构：定义、分类、比较、挑战、未来方向
  - 是否覆盖 2024-2026 前沿，如 LLM multi-agent、协作规划、工具使用、通信与博弈等
  - 是否有较强社区传播信号，如引用增长、作者团队影响力、教程属性
- 版本选择原则：
  - 优先正式出版版本
  - 若正式版本为短摘要而 arXiv 为完整长文，可保留完整长文并备注正式关联版本
- 对 tutorial/overview 类内容要谨慎判断：
  - 必须具备论文或正式可引用文档形态
  - 仅有幻灯片而无论文正文时，不纳入最终 10 篇
- 对边界案例做显式标注，例如：
  - “agentic workflow” 但无多智能体内容，不纳入
  - “multi-robot systems” 若文章核心为多智能体综述，可纳入；若仅工程控制而与目标语境差异过大，可降优先级
  - “game theory / MARL” 综述若未覆盖更广义 multi-agent 系统，可作为备选而非优先主清单
- 并行执行建议：
  - 每个来源独立负责人先完成候选池建设
  - 由一名汇总负责人统一去重与终选
  - 所有条目使用统一 ID，便于恢复和追踪
- 恢复机制建议：
  - 先从上次已有候选池继续，而不是重头检索
  - 新增字段“本轮更新时间”“复核状态”“证据链接”
  - 对已确认条目标记锁定，避免重复劳动
- 最终交付建议包含两层结果：
  - 主结果：10 篇最终入选综述
  - 附录：备选论文、排除论文及原因
- 代码中不应包含 AC-、Milestone 等计划术语