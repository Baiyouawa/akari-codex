# multi-agent-review-survey — 任务列表

- [ ] 检索近年与 multi-agent 相关的最新综述论文，优先覆盖 2024-2026，筛选最相关且具有代表性的 5 篇综述，记录来源链接（arXiv/OpenReview/出版社页面）与入选理由。 [zero-resource] [blocked-by: 当前项目 `literature/`、`analysis/`、`logs/` 在会话开始时为空，且仓库检索未发现可验证的 2024-2026 multi-agent 综述候选元数据/来源链接；在仅允许 `read_file` + `search_text` 的本地证据约束下，无法判定“最新五篇”及入选理由。详见 `projects/multi-agent-review-survey/analysis/2026-03-25-latest-review-selection-blocker-assessment.md`]
  Done when: 仓库内补齐可追溯的候选综述元数据或来源页面快照，并据此完成 5 篇综述的筛选、来源记录与入选理由说明。

- [ ] 将筛选出的 5 篇综述论文下载到本地 paper 目录，优先保存 PDF，并整理文件名、元数据与下载来源；若下载受阻，立即报告具体阻塞论文、来源与缺失资料。 [zero-resource] [blocked-by: 上游“5 篇综述筛选”任务未完成，当前仓库内不存在已确认的目标论文清单与来源页面。]
  Done when: 仓库内存在已确认的 5 篇目标综述及其来源页面，并将 PDF/元数据保存到本地 `paper/` 目录。

- [ ] 对第 1 篇综述进行详读，提炼研究背景、问题定义、分类体系、核心方法脉络、实验/benchmark、局限性与未来方向，输出中文详细笔记。 [zero-resource] [blocked-by: 目标综述尚未筛定，且仓库内没有该论文的 PDF、摘要摘录或已验证笔记。]
  Done when: 第 1 篇综述已在仓库内具备可追溯全文或已验证阅读材料，并形成中文详细笔记。

- [ ] 对第 2 篇综述进行详读，提炼研究背景、问题定义、分类体系、核心方法脉络、实验/benchmark、局限性与未来方向，输出中文详细笔记。 [zero-resource] [blocked-by: 目标综述尚未筛定，且仓库内没有该论文的 PDF、摘要摘录或已验证笔记。]
  Done when: 第 2 篇综述已在仓库内具备可追溯全文或已验证阅读材料，并形成中文详细笔记。

- [ ] 对第 3 篇综述进行详读，提炼研究背景、问题定义、分类体系、核心方法脉络、实验/benchmark、局限性与未来方向，输出中文详细笔记。 [zero-resource] [blocked-by: 目标综述尚未筛定，且仓库内没有该论文的 PDF、摘要摘录或已验证笔记。]
  Done when: 第 3 篇综述已在仓库内具备可追溯全文或已验证阅读材料，并形成中文详细笔记。

- [ ] 对第 4 篇综述进行详读，提炼研究背景、问题定义、分类体系、核心方法脉络、实验/benchmark、局限性与未来方向，输出中文详细笔记。 [zero-resource] [blocked-by: 目标综述尚未筛定，且仓库内没有该论文的 PDF、摘要摘录或已验证笔记。]
  Done when: 第 4 篇综述已在仓库内具备可追溯全文或已验证阅读材料，并形成中文详细笔记。

- [ ] 对第 5 篇综述进行详读，提炼研究背景、问题定义、分类体系、核心方法脉络、实验/benchmark、局限性与未来方向，输出中文详细笔记。 [zero-resource] [blocked-by: 目标综述尚未筛定，且仓库内没有该论文的 PDF、摘要摘录或已验证笔记。]
  Done when: 第 5 篇综述已在仓库内具备可追溯全文或已验证阅读材料，并形成中文详细笔记。

- [ ] 综合 5 篇综述，撰写一份中文 markdown 报告，包含：五篇综述分别的详细解读、横向比较、研究空白总结。 [zero-resource] [blocked-by: 前置的 5 篇综述筛选、下载与逐篇详读任务均未完成。]
  Done when: 5 篇综述的中文详细笔记全部完成，并整合为横向综述报告。

- [ ] 基于 5 篇综述的共同空白与趋势，提出 5 个可做的研究 idea；每个 idea 需要写清问题动机、核心假设、方法设计、数据/benchmark、评测指标、潜在风险与预期贡献。 [zero-resource] [blocked-by: 缺少前置的 5 篇综述比较与研究空白总结。]
  Done when: 基于已完成的 5 篇综述比较，产出 5 个结构完整的研究 idea。

- [ ] 检索 multi-agent 相关最新5篇综述论文，优先覆盖 arXiv 与 OpenReview，可补充可信学术来源 [zero-resource] [blocked-by: 仓库内仍无可验证的本地候选综述清单、来源页面快照、PDF、摘要摘录或已验证笔记；`search_text(pattern="multi-agent|survey|综述|review|arXiv|OpenReview", path="projects/multi-agent-review-survey", max_results=200)` 在本会话返回 no matches，因此在零外部检索约束下无法确认“最新5篇”。详见 `projects/multi-agent-review-survey/logs/2026-03-25T23:27:42+08:00-fleet-沙弥香-01-1774452423-4754bc-latest-five-surveys-blocked.md`]
  Done when: 仓库内补齐候选综述的可追溯元数据或来源页面快照，并据此确认5篇目标综述。

- [ ] 将确认后的5篇综述下载到本地 paper 目录，并记录来源链接与文件名映射 [zero-resource] [blocked-by: 上游“确认5篇综述”任务未完成；当前仓库内没有已确认论文标题、来源链接或 PDF 地址，无法生成可追溯下载与文件名映射。]
  Done when: 仓库内已有确认后的5篇综述及其来源链接，并已将对应文件保存到 `projects/multi-agent-review-survey/paper/`，同时记录来源链接与文件名映射。

- [ ] 逐篇精读5篇综述，提取研究问题、分类框架、核心方法、数据集/基准、优缺点与未来方向 [zero-resource] [blocked-by: 缺少已确认并下载到仓库内的5篇综述全文或等效可追溯阅读材料。]
  Done when: 5篇综述均具备本地全文或可追溯阅读材料，并完成逐篇结构化笔记。

- [ ] 汇总生成中文 Markdown 文档，分别详述5篇综述的内容与价值 [zero-resource] [blocked-by: 前置逐篇精读任务尚未完成。]
  Done when: 基于5篇综述的结构化笔记生成中文 Markdown 汇总文档。

- [ ] 基于5篇综述提出5个可做的研究 idea，并为每个 idea 写出具体方法设计、可行性与潜在贡献 [zero-resource] [blocked-by: 缺少前置综述比较与研究空白综合。]
  Done when: 形成5个结构完整、来源可追溯的研究 idea。

- [ ] 若任一论文缺失、下载失败或信息不全，立即报告阻塞详情：哪个Agent卡住、卡点与缺失资料 [zero-resource]
  Done when: TBD
