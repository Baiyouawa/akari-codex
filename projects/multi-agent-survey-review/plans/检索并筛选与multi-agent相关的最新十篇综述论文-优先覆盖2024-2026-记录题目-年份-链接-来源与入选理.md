# 检索并筛选与multi-agent相关的最新十篇综述论文，优先覆盖2024-2026，记录题目、年份、链接、来源与入选理由

Generated: 2026-03-26

## Goal Description
围绕“multi-agent”主题，开展一次面向最新研究进展的综述论文检索与筛选工作，优先覆盖 2024-2026 年，输出十篇高相关、高可信、可获取的综述类论文清单。每篇论文需记录题目、年份、链接、来源与入选理由，并为后续“下载、精读、中文 Markdown 总结与 idea 设计”提供可直接衔接的高质量输入。实施过程中需兼顾检索广度、来源权威性、主题覆盖度、时间新近性与结果可复核性。

## Acceptance Criteria

- AC-1: 完成面向 multi-agent 综述论文的系统检索，覆盖至少 3 类权威来源
  - Positive Tests: 检索来源包含 arXiv、Google Scholar、DBLP、OpenReview、IEEE/ACM/Springer/Elsevier/ACL Anthology 中至少 3 类；保留检索关键词、检索日期与筛选路径
  - Negative Tests: 仅从单一来源抓取结果；无法说明检索关键词；结果无法复现

- AC-2: 最终入选论文数量为 10 篇，且优先覆盖 2024-2026 年
  - Positive Tests: 入选清单正好 10 篇；其中大多数论文发表于 2024-2026；若 2026 年论文较少，明确说明以 2024-2025 补足
  - Negative Tests: 少于或多于 10 篇；大部分论文来自 2023 年及更早；未说明时间覆盖不足的原因

- AC-3: 入选论文必须为“综述/Survey/Review/Tutorial/Taxonomy/Overview”类文献，而非普通研究论文
  - Positive Tests: 标题、摘要或来源中能明确识别为 survey/review/tutorial/taxonomy/overview；必要时通过摘要确认其综述属性
  - Negative Tests: 选入普通算法论文、benchmark 论文、单一方法论文；仅因标题包含 multi-agent 而误判为综述

- AC-4: 每篇入选论文均完整记录题目、年份、链接、来源与入选理由
  - Positive Tests: 每条记录均具备 5 项信息；链接可访问到论文主页、PDF 或正式出版页面；来源标注明确
  - Negative Tests: 缺少年份或链接；来源写成模糊描述；入选理由仅有“相关”这类无信息量表述

- AC-5: 入选结果需体现主题覆盖，而非同质化堆叠
  - Positive Tests: 十篇论文覆盖多个子方向，如 LLM-based multi-agent、协作/通信、规划与决策、博弈/强化学习、多智能体系统架构、评测与安全、应用综述等
  - Negative Tests: 十篇几乎都集中在同一窄方向；无法说明覆盖结构；遗漏当前热门方向

- AC-6: 对候选论文执行明确筛选规则，并记录淘汰原因
  - Positive Tests: 存在候选池；有纳入标准与排除标准；可说明某些论文因非综述、时间过旧、质量不足或重复而被淘汰
  - Negative Tests: 直接给出最终十篇而无筛选逻辑；不能解释为何某些热门论文未入选

- AC-7: 结果格式可直接用于后续下载与精读任务
  - Positive Tests: 清单结构清晰，便于后续批量下载、分工阅读与中文总结；链接优先选择稳定入口
  - Negative Tests: 链接混乱、记录不标准；无法据此进行后续执行

- AC-8: 输出内容应避免虚构文献信息，并对不确定项进行显式标记与复核
  - Positive Tests: 对年份、正式发表状态、版本信息进行核实；对 arXiv 预印本与正式出版物做区分；不确定时标注“待复核”
  - Negative Tests: 编造不存在的论文；混淆预印本与期刊版本；错误标注来源与年份

## Path Boundaries

### Upper Bound (Maximum Scope)
执行一套完整的“检索—去重—筛选—校验—结构化整理”流程：  
1. 建立检索词矩阵，覆盖 multi-agent、multi-agent systems、multi-agent collaboration、LLM multi-agent、survey、review、taxonomy、tutorial、overview 等组合；  
2. 在多个学术平台交叉检索并汇总候选文献；  
3. 去重并建立候选池（建议 20-40 篇）；  
4. 基于时间、综述属性、来源可信度、主题覆盖度、可访问性进行多轮筛选；  
5. 对最终十篇逐篇核实元数据；  
6. 输出标准化表格，并附简明筛选依据、淘汰原因、主题标签与后续阅读优先级建议；  
7. 为后续下载、精读、中文 Markdown 总结和 idea 设计预留字段，如“推荐阅读顺序”“适合分配给哪个 Agent”“是否值得重点精读”。

### Lower Bound (Minimum Scope)
完成最小可行版调研：  
1. 至少使用 3 个可信来源检索；  
2. 形成不少于 15 篇候选综述论文；  
3. 筛选出 10 篇较新的 multi-agent 综述；  
4. 为每篇记录题目、年份、链接、来源与一句话入选理由；  
5. 明确说明筛选依据与时间优先原则。

### Allowed Choices
- Can use: 学术搜索引擎、论文数据库、出版社官网、预印本平台、参考文献追踪、标题/摘要级人工筛选、去重表格、主题标签法、时间优先排序法
- Cannot use: 非学术博客作为主要来源、未核实的二手搬运链接、将普通研究论文冒充综述、省略来源与链接、仅凭单平台单次检索直接定稿、编造文献元数据

## Dependencies and Sequence

### Milestones
1. 明确任务定义与筛选口径
   - 统一“multi-agent”范围：可包含 multi-agent systems、multi-agent collaboration、LLM-based multi-agent、multi-agent reinforcement learning 中的综述文献
   - 统一“综述论文”判定标准：Survey、Review、Tutorial、Taxonomy、Overview 等
   - 统一时间优先级：2026 > 2025 > 2024 > 必要时少量 2023 补充

2. 设计检索策略
   - 生成核心关键词与扩展关键词组合
   - 设定检索平台优先级与补充平台
   - 约定记录字段：题目、年份、作者、来源、链接、摘要片段、是否综述、主题标签、初筛结论

3. 多源检索并构建候选池
   - 在权威平台执行检索
   - 汇总候选论文到统一表格
   - 初步去重，保留不同版本信息以便核验

4. 执行第一轮筛选：综述属性与时间过滤
   - 删除非综述类论文
   - 删除明显过旧且缺乏代表性的论文
   - 保留 2024-2026 的高相关候选，必要时保留少量高价值补充项

5. 执行第二轮筛选：质量与相关性评估
   - 评估来源可信度、引用潜力、主题相关性、覆盖价值
   - 识别同质化论文，避免最终清单过于集中
   - 为候选论文打标签，如“LLM Agent”“MARL”“规划协作”“系统架构”“评测安全”“行业应用”

6. 确定最终十篇与备选清单
   - 从候选池中选出 10 篇
   - 同时保留 3-5 篇备选，以防链接失效或元数据冲突
   - 逐篇确认题目、年份、链接、来源、入选理由

7. 生成结构化输出
   - 形成标准化结果表
   - 附带简要筛选说明与边界说明
   - 保证结果可直接交给后续下载与精读流程

8. 质量复核
   - 检查数量是否正好为 10
   - 检查每条记录是否字段齐全
   - 检查链接可用性、来源正确性、是否存在重复或误分类
   - 检查是否满足“优先覆盖 2024-2026”的要求

## Implementation Notes
- 先定义“综述论文”识别规则，再开始检索，避免后期混入普通研究论文
- 检索词建议分层设计：核心词（multi-agent / multi-agent systems）+ 方法词（survey / review / tutorial / taxonomy / overview）+ 热点词（LLM / collaboration / planning / reinforcement learning / communication / safety / evaluation）
- 同一篇论文若同时存在 arXiv 版本与正式出版版本，优先记录正式出版入口，并补充预印本链接作为备选
- 对“multi-agent”边界要保持一致：若论文主题偏 distributed systems、swarm intelligence 或 agentic workflow，但与 multi-agent 关联较弱，应谨慎纳入
- 入选理由应具体，可从“时间新、覆盖面广、主题代表性强、适合作为入门主线、对后续 idea 启发大、来源可信”等角度描述
- 应显式记录淘汰原因，如“非综述”“年份偏旧”“与 multi-agent 关联弱”“内容与已入选论文高度重复”
- 若 2026 年公开综述数量不足，应在结果说明中明确采用 2025 和 2024 论文补足，而非降低文献类型标准
- 输出结果建议采用表格结构，便于后续 Agent 集群执行下载、分配阅读与中文总结
- 可为每篇论文附加“优先阅读级别”与“主题标签”，但不得替代题目、年份、链接、来源与入选理由这五项核心字段
- 链接优先级建议为：官方出版页 > OpenReview/ACL Anthology 等正式会议页 > arXiv PDF/abs 页
- 对于标题中未直接出现 Survey/Review 的候选项，必须通过摘要或正文简介确认其综述属性后再纳入
- 结果应保持可复核，便于后续人员依据同样方法再次检索得到近似结论
- 代码中不应包含 AC-、Milestone 等计划术语