# multi-agent-review-survey — 任务列表

- [x] 检索 2024-2026 年 multi-agent 相关综述/survey 论文，自主筛选最相关的 10 篇（使用 web_search 搜索 arXiv、Google Scholar、OpenReview、Semantic Scholar）
  Done when: 确认 10 篇综述的题目、年份、来源链接，写入项目文档
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md`

- [x] 为每篇入选综述确认可访问的 PDF 直链，并用 curl/wget 下载到 literature 文件夹中
  Done when: literature/ 中有 10 个可打开的 PDF 文件，命名规范
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md`

- [x] 验证 literature 文件夹中的 10 个 PDF 是否可正常打开、文件不为空、命名无冲突
  Completed: 2026-03-26T00:56:42+08:00
  Done when: 每个文件验证通过并记录验证结果
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-literature-pdf-verification.md`; `projects/multi-agent-review-survey/logs/2026-03-26T00:56:42+08:00-fleet-千早-05-1774457762-a2bc7b-literature-pdf-verification-recheck.md`

- [x] 记录每篇论文的元数据（题目、作者、年份、来源、PDF 路径）并汇总到项目文档中
  Completed: 2026-03-26T00:52:11+08:00
  Done when: 元数据清单完整且与实际文件一致
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-literature-metadata-inventory.md`; `projects/multi-agent-review-survey/logs/2026-03-26T00:52:11+08:00-fleet-智乃-02-1774457492-d9ccb6-metadata-refresh.md`

- [x] 对全部 10 篇综述逐篇精读，提取研究问题、分类框架、核心方法、数据集/基准、优缺点与未来方向
  Completed: 2026-03-26T00:16:17+08:00
  Done when: 10 篇结构化中文笔记完成
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`; `projects/multi-agent-review-survey/logs/2026-03-26T00:16:17+08:00-fleet-结衣-03-1774454544-65f537-ten-survey-deep-reading.md`

- [x] 综合 10 篇综述撰写中文 Markdown 报告，包含横向比较与研究空白总结
  Completed: 2026-03-26T00:52:23+08:00
  Done when: 报告文件完成，包含逐篇详述和横向分析
  Evidence: `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`; `projects/multi-agent-review-survey/logs/2026-03-26T00:52:23+08:00-fleet-结衣-03-1774457492-789106-survey-report.md`

- [x] 旧口径归档：基于 10 篇综述提出 5 个可做的研究 idea，每个 idea 包含问题动机、核心假设、方法设计、评测方案
  Completed: 2026-03-26T02:08:58+08:00
  Done when: 旧“5 ideas”口径被明确降级为历史中间产物，不再作为最终交付标准
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-research-ideas.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-detailed-ideas.md`; `projects/multi-agent-review-survey/logs/2026-03-26T02:08:58+08:00-fleet-智乃-10-1774462090-e5577c-scope-correction.md`

- [x] 对已下载论文进行交叉 review：至少一名 Agent 初审，另一名 Agent 复核质量
  Completed: 2026-03-26T00:40:55+08:00
  Done when: review 记录完成，质量问题已修正
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-cross-review-record.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`

- [x] 检索并筛选最新的 multi-agent 相关综述/survey 论文，优先近年高相关结果，初步候选不少于15篇
  Completed: 2026-03-26T01:06:05+08:00
  Done when: 初步候选不少于 15 篇，并写入项目文档
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`; `projects/multi-agent-review-survey/logs/2026-03-26T01:06:05+08:00-fleet-沙弥香-09-1774458273-48dea2-latest-survey-candidates-closeout.md`

- [x] 对候选论文逐篇判断是否属于真正的综述/survey，并按新近程度与相关性筛到10篇
  Completed: 2026-03-26T01:00:51+08:00
  Done when: 逐篇给出 survey 判定依据，并形成按新近程度与相关性排序的 top 10
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`

- [x] 为最终确定的10篇论文查找可下载的 PDF 链接，并下载保存到 multi-agent-review-survey/literature 文件夹
  Completed: 2026-03-26T01:36:07+08:00
  Done when: canonical 10 篇均具备可追溯 PDF 链接记录，且对应 PDF 已落盘到 `projects/multi-agent-review-survey/literature/`
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`; `projects/multi-agent-review-survey/logs/2026-03-26T01:36:07+08:00-fleet-柑奈-02-1774460107-7cb095-download-task-revalidation.md`

- [x] 对已下载论文进行交叉复核：检查题目、年份、survey属性、PDF可读性与文件是否落盘完整
  Completed: 2026-03-26T01:10:24+08:00
  Done when: canonical 10 篇论文均完成题目、年份、survey 属性、PDF 可读性与落盘完整性复核，并写入项目文档
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-canonical-ten-cross-verification.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-literature-pdf-verification.md`

- [x] 汇总10篇论文的基础信息，准备后续中文解读整理
  Completed: 2026-03-26T01:11:19+08:00
  Done when: `projects/multi-agent-review-survey/analysis/2026-03-26-basic-info-for-10-papers.md` 完成 10 篇 canonical reading set 的基础信息汇总
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-basic-info-for-10-papers.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-literature-pdf-verification.md`

- [x] 使用 web_search/web_fetch 检索 2024-2026 年 multi-agent systems / LLM agents / cooperative agents 相关综述或 survey，整理不少于 15 篇候选，附标题、年份、来源 URL
  Completed: 2026-03-26T01:24:26+08:00
  Done when: 至少 15 篇候选以标题、年份、来源 URL 形式落盘到项目文档，并具备 web_search/web_fetch 证据链
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-web-search-15-survey-candidates-refresh.md`; `projects/multi-agent-review-survey/logs/2026-03-26T01:24:26+08:00-fleet-千早-05-1774459025-ee93cb-web-search-15-survey-candidates.md`

- [x] 从候选中筛出最新且真正属于综述/survey 的 10 篇，给出判断依据，并为每篇确认主页与 PDF 直链；必要时交叉检查 arXiv、OpenReview、出版社页面
  Completed: 2026-03-26T01:21:48+08:00
  Done when: 10 篇论文均有逐篇 survey 判定依据、主页/来源页与 PDF 直链，并在项目文档中可追溯
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-canonical-ten-cross-verification.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-top10-survey-selection-closeout.md`

- [x] 检索 2024-2026 年最新的 multi-agent 相关综述/survey 论文，初筛候选论文并记录来源链接、年份、标题与摘要
  Completed: 2026-03-26T01:23:42+08:00
  Done when: 候选清单记录来源链接、年份、标题与摘要并落盘到项目文档
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-2024-2026-multi-agent-survey-candidate-screening-with-abstracts.md`; `projects/multi-agent-review-survey/logs/2026-03-26T01:23:42+08:00-fleet-沙弥香-09-1774459295-5067c4-candidate-screening-with-abstracts.md`; `projects/multi-agent-review-survey/logs/2026-03-26T01:36:46+08:00-fleet-日向-03-1774460167-0e2817-candidate-screening-task-closeout.md`

- [x] 核验候选论文是否真正属于综述/survey，判断是否足够新，并去重后确定 10 篇最终名单
  Completed: 2026-03-26T01:29:07+08:00
  Done when: 候选逐篇完成 survey 属性、时间窗与去重审计，并锁定 canonical 10 篇最终名单
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-verification-audit.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`

- [x] 为最终确定的 10 篇论文查找可下载 PDF 链接，下载到项目目录 multi-agent-review-survey/literature 文件夹
  Completed: 2026-03-26T01:36:07+08:00
  Done when: canonical 10 篇均具备可追溯 PDF 链接记录，且对应 PDF 已落盘到 `projects/multi-agent-review-survey/literature/`
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`; `projects/multi-agent-review-survey/logs/2026-03-26T01:36:07+08:00-fleet-柑奈-02-1774460107-7cb095-download-task-revalidation.md`

- [x] 对已下载文件进行互相 review：检查 PDF 是否可打开、标题是否匹配、是否为目标论文，并整理每篇论文的基础信息供后续中文解读使用
  Completed: 2026-03-26T01:58:40+08:00
  Done when: canonical 10 篇论文均完成 PDF 可读性、标题匹配、目标论文身份与基础信息可用性复核，并写入项目文档
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-downloaded-files-cross-review-task-closeout.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-basic-info-for-10-papers.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-canonical-ten-cross-verification.md`; `projects/multi-agent-review-survey/logs/2026-03-26T01:58:40+08:00-fleet-文乃-04-1774461459-998a50-downloaded-files-cross-review-task-closeout.md`

- [x] 为当前已下载并核验通过的 5 篇 multi-agent 相关综述/综述型论文记录元数据（题目、作者、年份、来源、PDF 路径）并汇总到项目文档中
  Done when: `analysis/2026-03-26-five-paper-metadata.md` 包含 5 篇论文元数据，且每个 `PDF 路径` 均与 `literature/` 中实际文件一致

- [x] 检索近年最新的 multi-agent 相关综述/survey 候选论文，优先 2024-2026，给出题目、年份、链接与入选理由
  Completed: 2026-03-26T01:39:54+08:00
  Done when: 候选短名单以题目、年份、链接与入选理由形式落盘到项目文档
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates-shortlist.md`

- [x] 对候选论文逐篇核验是否属于真正的综述/survey，而不是普通方法论文；若不合格则替换，直到凑齐 10 篇
  Completed: 2026-03-26T01:42:08+08:00
  Done when: 候选逐篇完成 survey 属性核验，并在不合格时用合格候选替换，最终形成 canonical 10 篇名单
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-verification-audit.md`; `projects/multi-agent-review-survey/logs/2026-03-26T01:42:08+08:00-fleet-灯里-08-1774460467-e28c8e-candidate-survey-verification-closeout.md`

- [x] 为每篇入选论文查找可下载 PDF，并将 PDF 保存到 projects/multi-agent-review-survey/literature/
  Completed: 2026-03-26T01:44:55+08:00
  Done when: canonical 10 篇均具备可追溯 PDF 链接记录，且对应 PDF 已保存到 `projects/multi-agent-review-survey/literature/`
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`; `projects/multi-agent-review-survey/logs/2026-03-26T01:44:55+08:00-fleet-沙弥香-09-1774460647-ec3ac4-download-task-closeout.md`

- [x] 对已下载文件做交叉 review：检查文件是否可打开、标题是否匹配、是否重复、总数是否达到 10 篇；不达标就继续补齐
  Completed: 2026-03-26T01:52:17+08:00
  Done when: 已下载文件的交叉 review 结果落盘，确认 canonical 10 篇可打开、标题匹配、无重复，且目录总数达到 10 篇
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-downloaded-files-cross-review-revalidation.md`; `projects/multi-agent-review-survey/logs/2026-03-26T01:52:17+08:00-fleet-柑奈-10-1774460858-1973c8-downloaded-files-cross-review.md`

- [x] 核查 projects/multi-agent-review-survey/literature/ 中现有 PDF，补齐到 10 篇“最新且明确属于 multi-agent 综述/survey”的论文，并记录每篇的题目、年份、链接、是否正式综述、PDF 路径
  Completed: 2026-03-26T01:49:08+08:00
  Done when: canonical 10 篇均在 `literature/` 中落盘，且题目、年份、来源链接、正式综述判定、PDF 路径已统一写入项目文档
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-literature-top10-inventory-closeout.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-verification-audit.md`

- [x] 对 10 篇综述逐篇精读，抽取统一结构信息：研究问题、分类框架、核心观点、方法谱系、数据集/benchmark、评测维度、主要结论、局限性、未来方向
  Completed: 2026-03-26T00:16:17+08:00
  Done when: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 完成 10 篇统一模板笔记
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`; `projects/multi-agent-review-survey/logs/2026-03-26T00:16:17+08:00-fleet-结衣-03-1774454544-65f537-ten-survey-deep-reading.md`

- [x] 对每篇论文做证据链核验：至少核对摘要、引言、结论与 survey/review 定位表述，避免把普通论文误判为综述；如遇边界论文，写明保留或剔除理由
  Completed: 2026-03-26T01:57:28+08:00
  Done when: 每篇目标论文都有摘要、引言、结论与 survey/review/SoK 定位证据，并对边界论文给出保留或剔除理由
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-survey-identity-evidence-chain-audit.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-latest-five-review-evidence-verification.md`; `projects/multi-agent-review-survey/logs/2026-03-26T01:57:28+08:00-fleet-日向-03-1774461369-d0939c-latest-five-review-evidence-verification.md`

- [x] 对 10 篇综述做横向对比，整理共识、分歧、重复主题、空白问题、时间演化趋势，形成适合快速浏览的中文总览
  Completed: 2026-03-26T01:55:48+08:00
  Done when: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md` 形成适合快速浏览的中文横向总览
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

- [x] 撰写一个中文 Markdown 文档，帮助人快速了解这 10 篇综述；文档需包含：执行摘要、10 篇逐篇精读卡片、横向对比表、关键趋势、局限与机会
  Completed: 2026-03-26T01:59:33+08:00
  Done when: 文档落盘并覆盖执行摘要、10 篇逐篇精读卡片、横向对比表、关键趋势、局限与机会
  Evidence: `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md`; `projects/multi-agent-review-survey/logs/2026-03-26T01:59:33+08:00-fleet-枫-05-1774461549-e6b16c-fast-survey-handbook.md`

- [x] 基于 10 篇综述的空白点与未来方向，提出 10 个后续可做的详细 idea；每个 idea 需包含：问题定义、为什么值得做、与现有综述的关系、可行方法、数据/benchmark、评测指标、预期难点、最小可执行原型
  Completed: 2026-03-26T02:01:50+08:00
  Done when: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-detailed-ideas.md` 完成 10 个结构完整、可追溯的 detailed ideas
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-detailed-ideas.md`

- [x] 对生成的 10 个 idea 做去重与优先级排序，标注短期可做/中期可做/高风险高收益，并给出推荐的前 3 个起步方向
  Completed: 2026-03-26T02:03:11+08:00
  Done when: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-idea-dedup-and-priority.md` 完成 10 个 idea 的去重、优先级排序、短中期/高风险分类与 Top 3 起步建议
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-idea-dedup-and-priority.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-detailed-ideas.md`

- [x] 对最终 Markdown 文档做互相 review，检查完整性、中文表达质量、事实一致性、可追溯引用与 PDF 对应关系；若发现偷懒式 blocked 或只尝试单一路径，按 PUA 标准打回重做
  Completed: 2026-03-26T02:07:07+08:00
  Done when: 最终 Markdown 文档通过结构完整性、事实一致性、可追溯引用与 PDF 对应关系复核，并写入项目文档
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-final-markdown-cross-review.md`; `projects/multi-agent-review-survey/logs/2026-03-26T02:07:07+08:00-fleet-灯里-08-1774461940-b59ce3-final-markdown-cross-review.md`

- [x] 把最终文档保存到项目内，文件名明确，例如 projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md，并在文档开头给出论文清单与 PDF 对应关系
  Completed: 2026-03-26T02:07:07+08:00
  Done when: 最终文档已落盘到项目内，且文档开头给出论文清单与 PDF 对应关系
  Evidence: `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-final-markdown-cross-review.md`; `projects/multi-agent-review-survey/logs/2026-03-26T02:07:07+08:00-fleet-灯里-08-1774461940-b59ce3-final-markdown-cross-review.md`

- [x] 纠正任务口径：废弃或降级所有仅要求‘5个idea’的旧任务，统一以‘10篇综述精读 + 10个详细idea’为最终目标继续执行
  Completed: 2026-03-26T02:08:58+08:00
  Done when: README / TASKS / session log 明确旧“5 ideas”口径已降级为历史中间产物，项目最终目标统一为“10 篇综述精读 + 10 个详细 idea”
  Evidence: `projects/multi-agent-review-survey/README.md`; `projects/multi-agent-review-survey/TASKS.md`; `projects/multi-agent-review-survey/logs/2026-03-26T02:08:58+08:00-fleet-智乃-10-1774462090-e5577c-scope-correction.md`

- [x] 盘点并核验 literature 文件夹现有 PDF：确认每篇是否为 2024-2026 年、是否明确属于综述/survey、是否与 multi-agent 高相关；不足则继续补齐到准确 10 篇
  Completed: 2026-03-26T02:10:57+08:00
  Done when: 项目内已有 closeout 工件明确给出 canonical 10 篇的年份、survey 身份、相关性判定与 PDF 路径，并确认无需继续补齐
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-literature-pdf-audit-task-closeout.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-literature-top10-inventory-closeout.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-verification-audit.md`; `projects/multi-agent-review-survey/logs/2026-03-26T02:10:57+08:00-fleet-日向-11-1774462120-ac611f-literature-pdf-audit-closeout.md`

- [x] 对最终 10 篇论文逐篇精读，按统一模板抽取：研究问题、分类框架、关键方法脉络、涉及数据集/benchmark、评测维度、主要结论、局限性、作者给出的未来方向
  Completed: 2026-03-26T02:12:23+08:00
  Done when: canonical 10 篇均已按统一模板完成结构化精读，并与主报告和元数据清单保持一致
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-structured-reading-task-closeout.md`; `projects/multi-agent-review-survey/logs/2026-03-26T02:12:23+08:00-fleet-灯里-00-1774462300-c5384e-structured-reading-task-closeout.md`

- [x] 产出中文 Markdown 主报告，文件保存为 projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md；内容必须包含：执行摘要、10篇逐篇解读、横向对比表、趋势总结、研究空白
  Completed: 2026-03-26T02:16:43+08:00
  Done when: `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 已存在，且文档中可检出 `## 1. 执行摘要`、`## 2. 十篇逐篇精读卡片`、`## 3. 横向对比表`、`## 4. 关键趋势`、`## 5. 局限与机会` 等对应章节
  Evidence: `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-final-markdown-cross-review.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-final-markdown-review.md`

- [x] 基于 10 篇综述的共同空白与差异，提出 10 个详细 research idea；每个 idea 必须包含：题目、背景动机、核心问题、创新点、方法设计、实验方案、数据/benchmark、评价指标、风险点、最小可行原型
  Completed: 2026-03-26T02:20:47+08:00
  Done when: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-detailed-ideas.md` 明确覆盖 10 个 idea，且每个条目包含问题定义/价值/与综述关系/可行方法/数据与 benchmark/评测指标/预期难点/最小原型等结构字段
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-detailed-ideas.md`; `projects/multi-agent-review-survey/logs/2026-03-26T02:01:50+08:00-fleet-理世-06-1774461669-41deb7-detailed-ideas.md`

- [x] 安排交叉 review：一名 Agent 写逐篇解读，另一名 Agent 复核事实与引用；再由第三名 Agent 专门检查 10 个 idea 是否重复、是否真的来源于综述中的空白与未来方向
  Completed: 2026-03-26T02:20:47+08:00
  Done when: 仓库内同时存在逐篇精读、事实/PDF 交叉复核、以及 10 个 idea 去重与优先级审计三类工件
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-final-markdown-cross-review.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-idea-dedup-and-priority.md`

- [x] 若任何 Agent 报 blocked，先审查其是否使用 web_search/web_fetch/本地文件核验等手段；未穷尽方法即 blocked 的视为伪阻塞，直接按 PUA 标准打回重做并要求切换方案
  Completed: 2026-03-26T02:20:47+08:00
  Done when: 已形成 blocked 审查记录，逐条说明哪些会话属于伪阻塞、哪些属于阶段性真实阻塞，并给出重做要求
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-blocked-agent-audit-and-pua-disposition.md`

- [ ] 完成后整理最终清单：10篇论文题目、年份、PDF文件名/路径、入选理由、中文摘要入口，确保文档与 literature 文件夹一一对应
  Done when: TBD

- [ ] 重做 2024-2026 年 multi-agent 相关综述/survey 检索任务：必须先使用 web_search 检索候选论文不少于15篇，覆盖 multi-agent systems、LLM-based multi-agent systems、communication/collaboration/coordination surveys 等子方向
  Done when: TBD

- [ ] 对每个候选用 web_fetch 抓取摘要页、arXiv页、期刊页或PDF首页信息，核验其是否明确自称 survey/review、年份是否在 2024-2026、主题是否与 multi-agent 直接相关
  Done when: TBD

- [ ] 输出最终入选10篇与剔除名单，给出每篇入选/剔除理由，并标注来源链接、PDF链接、年份、survey证据句
  Done when: TBD

- [ ] 若再次报 blocked，必须写明至少3种已尝试方法及各自结果；未使用 web_search/web_fetch 不得报 blocked
  Done when: TBD

- [ ] 安排另一名 Agent 复核沙弥香-01 的新结果，检查是否存在把普通论文误当综述、把旧论文误当最新、或证据链不完整的问题
  Done when: TBD

- [ ] 盘点 projects/multi-agent-review-survey/literature/ 现有 PDF，核对哪些是真正的 multi-agent 综述/survey、哪些重复或不合格，形成缺口清单
  Done when: TBD

- [ ] 从互联网系统检索 2023-2026 年优先的 multi-agent 相关正式综述/survey 论文，候选需包含题目、年份、来源、是否 survey/review 的证据
  Done when: TBD

- [ ] 对候选综述做交叉 review，剔除伪综述、教程、观点文、单篇方法总结和重复主题，最终确定 10 篇高质量综述清单
  Done when: TBD

- [ ] 下载最终确认的综述 PDF 到 projects/multi-agent-review-survey/literature/，保证文件可打开、命名规范且总数达到 10 篇
  Done when: TBD

- [ ] 为每篇已确认综述提取摘要、研究问题、分类框架、核心结论、局限性和可延展方向，整理成后续中文 Markdown 精读的结构化笔记
  Done when: TBD

- [ ] 基于这 10 篇综述归纳 10 个后续可开展的详细 research/execution ideas，记录每个 idea 的动机、切入点、预期产出和依赖条件
  Done when: TBD

- [ ] 盘点并确认项目中目标 10 篇 multi-agent 相关综述论文的最终清单，补齐题目、年份、链接与引用信息，若缺失则联网检索验证。
  Done when: TBD

- [ ] 对这 10 篇综述逐篇精读，提炼中文总结：研究问题、分类框架、核心观点、代表方法、数据集/benchmark、优缺点、局限与启发。
  Done when: TBD

- [ ] 交叉比对 10 篇综述之间的重合点与差异点，整理统一的 multi-agent survey 总体脉络，包括任务分类、协作机制、通信方式、评测维度与应用方向。
  Done when: TBD

- [ ] 产出最终中文 Markdown 文档，内容包含：10 篇综述精读、横向对比表、统一知识框架、关键结论。
  Done when: TBD

- [ ] 在综述总结之外，额外提出 10 个后续可做的详细 research ideas，每个 idea 说明动机、切入点、可能方法、预期贡献与风险。
  Done when: TBD

- [ ] 对所有引用与事实进行复核，检查证据链、链接可追溯性和表述准确性，不足处重新检索补证。
  Done when: TBD

- [ ] 检查现有 Agent 历史产出，若有 blocked 或质量不足，按要求重派并穷尽搜索，不允许未检索就放弃。
  Done when: TBD

- [ ] 将最终交付物落盘到项目目录中的 Markdown 文件，并给出可直接汇报给小侑的完成版摘要。
  Done when: TBD
