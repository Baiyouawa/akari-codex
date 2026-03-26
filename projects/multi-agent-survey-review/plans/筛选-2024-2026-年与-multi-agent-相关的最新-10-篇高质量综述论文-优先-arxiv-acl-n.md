# 筛选 2024-2026 年与 multi-agent 相关的最新 10 篇高质量综述论文，优先 arXiv/ACL/NeurIPS/ICML/ICLR/IEEE/ACM 等可信来源，并记录题目、年份、链接与筛选理由

Generated: 2026-03-26

## Goal Description
围绕“multi-agent”主题，面向 2024-2026 时间范围，快速建立一套可并行执行的高质量综述论文筛选与研读流程，从可信来源中筛选出最新 10 篇高质量综述类论文，并为每篇论文记录题目、年份、链接与筛选理由。  
该任务需支持 Agent 集群并行执行，覆盖检索、去重、质量评估、下载、初读、精读、中文总结与最终清单汇总，确保结果可追溯、可复核、可继续扩展。

## Acceptance Criteria

- AC-1: 明确完成 2024-2026 年范围内与 multi-agent 主题相关的综述论文检索与初筛
  - Positive Tests: 检索结果明确限定在 2024、2025、2026；主题与 multi-agent、multi-agent systems、LLM-based multi-agent、agent society、coordination、collaboration、survey/review/tutorial 等关键词强相关；来源优先覆盖 arXiv、ACL Anthology、OpenReview、IEEE、ACM、NeurIPS、ICML、ICLR 等
  - Negative Tests: 纳入 2023 及以前论文；纳入与 multi-agent 无明显关联的单智能体论文；纳入原始研究论文而非综述/系统性综述/教程类论文；纳入来源不明或不可验证链接

- AC-2: 最终输出恰好 10 篇高质量综述论文，并保留候选池与淘汰依据
  - Positive Tests: 最终表格中恰有 10 篇；每篇均有题目、年份、链接、来源类型、筛选理由；存在候选池与去重/淘汰记录
  - Negative Tests: 少于或多于 10 篇；缺失基本字段；无法解释为何入选；重复论文或同一论文多个版本重复计入

- AC-3: 建立清晰、可执行的质量评估标准并用于筛选
  - Positive Tests: 评估维度至少包括来源可信度、论文类型是否为综述、时间新近性、主题相关性、覆盖面、引用/传播信号、结构完整性；每篇入选论文有对应评分或定性说明
  - Negative Tests: 仅凭单一关键词命中即入选；没有统一标准；评估逻辑前后不一致

- AC-4: 支持 Agent 集群并行执行，并有明确的角色分工与合并机制
  - Positive Tests: 至少拆分为检索 Agent、去重 Agent、质量评估 Agent、下载 Agent、精读 Agent、中文总结 Agent、汇总校验 Agent；定义输入输出与交接顺序
  - Negative Tests: 所有工作混在单线程流程中；无角色边界；并行结果无法汇总或互相覆盖

- AC-5: 每篇入选论文都完成基础下载核验与内容可读性确认
  - Positive Tests: 每篇均能访问论文主页或 PDF；能确认其摘要、目录或正文中具有综述属性；记录可访问链接
  - Negative Tests: 链接失效；仅有二手转载；无法确认论文真实存在；下载后发现并非综述类论文

- AC-6: 形成中文总结产出框架，满足后续精读沉淀
  - Positive Tests: 每篇论文至少有中文摘要式总结模板，包含研究范围、问题划分、方法分类、关键结论、适用场景、局限性；可供后续扩写
  - Negative Tests: 仅保留标题列表；无中文信息沉淀；无法支撑后续综述写作或组内汇报

- AC-7: 保证结果可追溯、可复现、可复核
  - Positive Tests: 记录检索关键词、数据源、检索日期、筛选标准、版本信息、入选/淘汰原因；如有 arXiv 与正式出版版本，能说明选择哪个版本
  - Negative Tests: 无检索日志；无版本说明；无法复现相同筛选结果；后续复核时无法解释决策过程

## Path Boundaries

### Upper Bound (Maximum Scope)
构建完整的多 Agent 文献调研流水线：  
1. 同时在 arXiv、ACL Anthology、OpenReview、IEEE Xplore、ACM Digital Library、Google Scholar、Semantic Scholar 等多源并行检索；  
2. 自动识别 survey/review/tutorial 类论文，建立 2024-2026 multi-agent 综述候选池；  
3. 对候选论文进行跨源去重、版本合并、元数据补全；  
4. 基于统一评分规则筛选最新 10 篇高质量综述；  
5. 下载论文全文并完成摘要级、结构级、结论级三层精读；  
6. 产出中文总结、分类标签、比较表和推荐阅读顺序；  
7. 输出可复用的数据表、筛选日志、失败样本清单与后续扩展建议。

### Lower Bound (Minimum Scope)
完成一个最简可用版本：  
1. 在 2-3 个可信来源中检索 2024-2026 年 multi-agent 综述论文；  
2. 收集不少于 15 篇候选；  
3. 去重后筛出 10 篇；  
4. 为每篇记录题目、年份、链接、筛选理由；  
5. 提供简要中文摘要模板，供后续精读补充。

### Allowed Choices
- Can use: arXiv、ACL Anthology、OpenReview、IEEE Xplore、ACM Digital Library、DBLP、Semantic Scholar、Google Scholar 作为辅助检索入口；关键词布尔检索；人工复核；多 Agent 并行分工；表格化管理；版本优先策略（正式发表版优先，若无则 arXiv）
- Cannot use: 不可验证的聚合转载站作为唯一来源；仅凭博客/社媒推荐直接入选；将普通研究论文误标为综述论文；混入 2023 及以前论文；以 citation 数作为唯一质量标准；遗漏链接或筛选理由

## Dependencies and Sequence

### Milestones
1. 明确任务口径与筛选规则  
   - 确认时间范围为 2024-2026  
   - 明确“multi-agent”主题边界  
   - 明确“综述论文”包含 survey、review、tutorial、systematization 等可接受类型  
   - 定义来源优先级与版本优先级

2. 搭建 Agent 集群角色与工作流  
   - 检索 Agent：多源并行搜索候选论文  
   - 元数据 Agent：统一字段并补全年份、作者、来源、链接  
   - 去重 Agent：合并同题不同版本、预印本与正式版  
   - 质量评估 Agent：依据评分标准打分与排序  
   - 下载核验 Agent：检查 PDF/主页可访问性与真实性  
   - 精读 Agent：提取论文核心综述范围与贡献  
   - 中文总结 Agent：形成标准化摘要  
   - 审核汇总 Agent：整合最终 10 篇结果

3. 设计检索策略并发起第一轮候选收集  
   - 核心关键词：multi-agent survey、multi-agent review、multi-agent systems survey、LLM multi-agent survey、large language model multi-agent review、autonomous agents survey、agent collaboration survey、agent society survey  
   - 来源分桶检索：预印本源、会议源、出版社源  
   - 记录检索式、日期、命中数、初步判断

4. 构建候选池并完成去重  
   - 目标候选数量不少于 15-25 篇  
   - 合并 arXiv 与正式版  
   - 去除非综述、非 2024-2026、非 multi-agent 强相关项  
   - 保留淘汰原因

5. 建立质量评估矩阵并排序  
   - 维度包括：主题相关性、综述属性强度、来源可信度、时间新近性、覆盖面、结构完整性、社区影响信号  
   - 输出候选排序表  
   - 标记边界案例供人工复核

6. 确定最终 10 篇入选论文  
   - 优先最新年份  
   - 在同等质量下优先可信来源与正式出版版  
   - 保证主题覆盖面不过度集中于单一子方向  
   - 检查是否存在重复主题或低质量补位

7. 执行下载与真实性核验  
   - 确认每篇链接可访问  
   - 确认标题、年份、版本一致  
   - 下载 PDF 或保存稳定主页链接  
   - 标记访问异常项并补充替代链接

8. 完成精读信息抽取  
   - 提取综述范围  
   - 提取问题分类框架  
   - 提取方法脉络  
   - 提取代表性结论与局限  
   - 提取适用对象与读者价值

9. 输出中文总结与最终交付清单  
   - 形成 10 篇论文的中文摘要卡片  
   - 形成总表：题目、年份、链接、来源、筛选理由、关键词、备注  
   - 附候选池、淘汰表、检索日志

10. 完成最终审核与交付前校验  
   - 核对数量是否为 10  
   - 核对时间范围是否正确  
   - 核对每篇是否为综述类  
   - 核对链接是否可用  
   - 核对中文总结是否齐全

## Implementation Notes
- 先定义“综述论文”的可接受范围，避免把 benchmark、position paper、framework paper、original research paper 误纳入
- 检索时采用“主题词 + survey/review/tutorial/systematic review”双重约束，必要时补充“literature review”与“overview”
- 对 LLM-based multi-agent 方向应纳入，但需确保仍属于 multi-agent 主体，而非纯单智能体工具调用
- 对 multi-agent systems 传统方向与 LLM multi-agent 新方向应平衡覆盖，避免结果全落在某一热点子域
- 来源优先顺序建议为：正式出版数据库/官方会议页面 > OpenReview/ACL Anthology > arXiv 预印本 > 学术搜索辅助页
- 若同一论文同时存在 arXiv 与 IEEE/ACM/会议正式版，最终记录应优先保留正式版链接，并可附 arXiv 作为备选
- 对“最新”应以年份优先，再结合版本发布日期；若 2026 年候选不足，可由 2025-2024 高质量综述补足，但必须说明原因
- 质量筛选建议采用“硬性门槛 + 相对排序”两阶段：先按年份/主题/综述属性/来源过滤，再按综合质量排序
- 下载环节需验证链接稳定性，优先保存 DOI、官方主页或可长期访问的 arXiv 链接
- 中文总结模板建议统一为：研究对象、综述范围、分类方法、核心结论、亮点、局限、适合阅读人群
- 最终结果中除入选 10 篇外，建议保留“候补 3-5 篇”，用于应对链接失效、误判类型或质量复核后替换
- 对所有 Agent 输出采用统一字段：title、year、venue/source、url、paper_type、topic_fit、quality_notes、selection_reason、status
- 合并结果时必须保留证据链，包括摘要摘录、目录判断或论文自述中表明其为 survey/review/tutorial 的句段
- 若检索工具或接口存在速率限制，应采用分批并发、缓存结果、失败重试与人工补录机制
- 输出的最终文档应可直接用于后续“下载、精读、中文总结产出”的流水线衔接
- 代码中不应包含 AC-、Milestone 等计划术语