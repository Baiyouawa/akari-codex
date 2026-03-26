# 将这 10 篇综述论文下载到本地，按统一目录结构整理 PDF 与元数据，确保文件可追溯到原始来源

Generated: 2026-03-26

## Goal Description
建立一套可立即执行的论文获取与归档流程，用于并行完成“最新 10 篇 multi-agent 相关综述论文”的筛选、下载、本地整理与来源留痕。实施结果应包括：  
1. 已确认属于“综述论文”的目标论文清单；  
2. 每篇论文的本地 PDF 文件；  
3. 与 PDF 一一对应的结构化元数据文件；  
4. 统一且可扩展的目录结构；  
5. 可回溯到原始来源页面、DOI、出版社或开放获取地址的证据链；  
6. 为后续 Agent 集群执行精读、中文总结与知识抽取提供稳定输入。

## Acceptance Criteria

- AC-1: 已完成 10 篇“最新”的 multi-agent 相关综述论文筛选，并形成唯一确定的目标列表
  - Positive Tests: 列表恰好包含 10 篇论文；每篇论文均有标题、作者、年份、来源、综述属性判断依据；按明确时间规则排序（如 online date / publication date）；主题与 multi-agent 综述直接相关
  - Negative Tests: 数量不是 10；混入非综述论文、教程、观点文章或原始研究论文；缺失年份或来源信息；“最新”标准不明确导致结果不可复现

- AC-2: 10 篇目标论文均已下载到本地，且文件可正常打开
  - Positive Tests: 每篇论文对应 1 个可打开的 PDF；文件大小大于 0；随机抽检可阅读正文；下载日志可定位到获取时间与下载链接
  - Negative Tests: 文件损坏、空文件、HTML 页面误保存为 PDF、重复下载同一论文替代其他论文、仅保存截图或网页快照而无正式 PDF

- AC-3: 本地目录结构统一，能够稳定支持后续自动化处理
  - Positive Tests: 所有论文均按统一路径规范存放；PDF、元数据、日志、校验信息位置固定；任意一篇论文都能通过目录规则快速定位
  - Negative Tests: 不同论文使用不同命名方式；文件散落在多个无规则目录；人工难以判断哪份元数据对应哪份 PDF

- AC-4: 每篇论文都具有完整且结构化的元数据
  - Positive Tests: 每篇至少包含 paper_id、title、authors、year、venue/publisher、doi、source_url、pdf_url、access_date、review_type、language、open_access_status、license（如可得）、local_pdf_path、checksum；字段格式一致
  - Negative Tests: 元数据缺字段；字段命名不统一；将来源描述写成自由文本无法机读；本地路径与真实文件不一致

- AC-5: 每篇论文都可追溯到原始来源
  - Positive Tests: 元数据中包含原始落地页 URL、PDF 直链或 DOI 解析链接；可从本地记录反查至出版社、arXiv、OpenReview、ACL Anthology、IEEE、ACM、Springer 等原始页面；保存访问时间与来源类型
  - Negative Tests: 仅记录“来自搜索引擎”；只有第三方转载链接；无法确认 PDF 是否为正式版本；来源页面失效且无 DOI/归档信息

- AC-6: 文件命名与唯一标识规则可避免冲突和歧义
  - Positive Tests: 每篇论文具有稳定唯一 ID；同标题不同版本可区分；文件名不含高风险非法字符；跨平台兼容
  - Negative Tests: 直接用长标题命名导致路径过长；同名文件相互覆盖；使用空格、特殊字符或中文全角符号导致脚本处理失败

- AC-7: 下载与整理过程具备可审计性
  - Positive Tests: 保留抓取/下载日志、时间戳、状态码或错误原因；失败论文有重试记录；最终清单可复现
  - Negative Tests: 无任何日志；无法区分“未找到”和“下载失败”；人工修改后无记录

- AC-8: 结果可直接供后续 Agent 集群使用
  - Positive Tests: 存在机器可读索引文件（如 papers_index.jsonl / csv）；下游 Agent 可批量读取 PDF 路径与元数据；字段满足精读、总结、引用管理需求
  - Negative Tests: 仅有人工整理的文件夹；下游流程还需手工补全路径、标题或来源信息

## Path Boundaries

### Upper Bound (Maximum Scope)
最完整的方案包括：  
- 通过多源检索策略筛选 multi-agent 领域最新综述论文，来源覆盖 Crossref、Semantic Scholar、OpenAlex、Google Scholar 辅助核验、arXiv、DBLP、出版社官网等；  
- 对“综述”属性进行二次验证，结合标题关键词、摘要、出版类型、正文结构和来源标签确认；  
- 建立标准化目录，例如按 `paper_id` 分层，分别保存 PDF、元数据 JSON、原始页面快照、下载日志、校验和、许可信息；  
- 为每篇论文记录 DOI、原始落地页、PDF 直链、访问时间、下载工具、HTTP 状态、文件哈希值；  
- 对付费/受限论文仅保存合法可访问的元数据与来源链接，不绕过权限控制；  
- 产出统一索引文件，供后续多个 Agent 并行执行精读、段落抽取、中文总结、参考文献分析；  
- 增加重复检测、版本识别（preprint vs published）、缺失字段回填、失败重试与异常报告；  
- 保证流程可复用到后续批次论文获取任务。

### Lower Bound (Minimum Scope)
最简可行方案包括：  
- 确认 10 篇最新且确属综述的目标论文；  
- 为每篇下载 1 份可读 PDF 到本地；  
- 为每篇保存 1 份基础元数据文件，至少含标题、作者、年份、来源、DOI/来源链接、PDF 路径、访问日期；  
- 使用统一目录结构和统一命名规则；  
- 保存一份总索引文件，能让后续流程直接读取。  

### Allowed Choices
- Can use: 合法公开来源或机构授权可访问来源；Crossref/OpenAlex/Semantic Scholar/DBLP/arXiv/出版社官网/API；Python、Shell、下载器、PDF 校验工具、哈希计算工具；JSON、JSONL、CSV、Markdown 作为元数据或索引载体；并行 Agent 执行筛选、下载、校验、整理
- Cannot use: 绕过付费墙、破解登录、抓取受版权限制且无授权的 PDF；仅依赖不可信第三方搬运站作为唯一来源；手工随意命名导致不可复现；在无来源留痕的情况下保存论文；将非综述论文冒充综述纳入结果

## Dependencies and Sequence

### Milestones
1. 明确筛选范围与“最新”判定规则
   - 定义主题边界：multi-agent systems、multi-agent collaboration、LLM-based multi-agent、agentic systems 等是否纳入
   - 定义文献类型边界：survey、review、overview、systematic review、literature review
   - 定义时间排序字段优先级：online date > publication date > preprint date
   - 确认目标数量固定为 10

2. 搭建检索与候选池汇总机制
   - 从多个可信来源拉取候选论文
   - 去重并合并 DOI、标题、作者、年份等字段
   - 初步按时间倒序排列，形成候选池

3. 执行综述属性与主题相关性核验
   - 基于标题、摘要、来源类型和必要时正文目录判断是否为综述
   - 剔除非综述、非 multi-agent 主题或信息不完整的条目
   - 固化最终 10 篇目标列表

4. 设计并创建统一目录结构
   - 建议结构：
     - `papers/`
       - `{paper_id}/`
         - `paper.pdf`
         - `metadata.json`
         - `source.txt`
         - `download.log`
         - `checksums.txt`
     - `indexes/`
       - `papers_index.jsonl`
       - `papers_index.csv`
     - `logs/`
       - `run_2026-03-26.log`
   - 确定 `paper_id` 规则，如 `year_firstauthor_keyword_hash`

5. 执行 PDF 下载与本地落盘
   - 优先从 DOI 落地页或出版社/开放仓库原始页面获取
   - 记录下载 URL、访问时间、响应状态、保存路径
   - 对失败条目执行重试与备用来源查找

6. 生成并补全结构化元数据
   - 为每篇论文生成标准 JSON 元数据
   - 回填 DOI、来源站点、许可状态、摘要、关键词等可得信息
   - 写入本地路径与哈希值，形成文件级映射

7. 执行一致性校验与可追溯性验证
   - 校验 PDF 是否可打开、元数据是否齐全、路径是否存在
   - 校验每篇是否具备原始来源 URL 或 DOI
   - 检查是否恰好 10 篇且无重复

8. 产出总索引并交付给下游 Agent
   - 汇总所有论文信息到统一索引文件
   - 确保下游可按索引读取 PDF 与元数据
   - 输出异常清单与未满足项（如合法不可下载但元数据完整的情况）

## Implementation Notes
- 建议优先以 DOI 作为跨平台主键，若无 DOI，再使用稳定组合键生成本地 `paper_id`
- PDF 文件建议统一命名为 `paper.pdf`，通过目录名而非文件名承载唯一性，减少跨平台兼容问题
- 元数据文件建议使用 UTF-8 编码 JSON，字段保持固定顺序与命名
- `metadata.json` 建议至少包含：
  - `paper_id`
  - `title`
  - `authors`
  - `year`
  - `abstract`
  - `keywords`
  - `review_type`
  - `topic_tags`
  - `venue`
  - `publisher`
  - `doi`
  - `source_url`
  - `pdf_url`
  - `access_date`
  - `open_access_status`
  - `license`
  - `local_pdf_path`
  - `file_checksum_sha256`
  - `notes`
- `source.txt` 可保存人工可读的来源说明，例如原始落地页、检索入口、是否 OA、是否出版版/预印本
- 对同一论文的 preprint 与 publisher version，应只保留 1 个主版本作为下游默认输入，并在元数据中记录版本说明
- 若目标论文因版权限制无法合法下载正式 PDF，可保留完整元数据与来源留痕，并在异常报告中标记，不得以非授权版本替代
- 为支持并行 Agent，索引文件中应包含绝对路径或相对根路径，避免运行环境切换后失效
- 应增加去重规则：优先 DOI 去重，其次标题归一化 + 第一作者 + 年份
- 应增加校验规则：PDF 魔数检测、文件大小阈值、页数读取、哈希值生成
- 可设置失败重试策略：网络失败重试 3 次，来源切换不超过 2 个候选
- 中文总结与精读不是本任务交付物，但目录和索引应为后续步骤预留扩展字段
- 代码中不应包含 AC-、Milestone 等计划术语