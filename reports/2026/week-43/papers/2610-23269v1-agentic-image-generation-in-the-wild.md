# Agentic Image Generation in the Wild

> 中文标题：Agentic Image Generation in the Wild

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Agentic AI / Text-to-Image / Text-to-Image + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-10-16 |
| 作者 | Yifan Li, Bowen Qin, Kun Zhou, Haochen Zhao, Zikang Liu, Zheng Li |
| 原文入口 | [Abstract](http://arxiv.org/abs/2610.23269v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2610.23269v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Agentic image generation pairs an image generator with a search agent that retrieves references from the web, extending generation beyond the generator's training data. Real-world requests, however, often concern entities that appeared only days ago. We call this setting Image Generation in the Wild. In this setting, the web offers limited visual evidence, search results are crowded with easily confused entities, and the target is rarely shown on its own. To study this setting, we build an automated pipeline that synthesizes prompts from recent headlines and keeps only those whose real search results are highly confusing, yielding requests that are hard to solve yet natural to ask. With it, we construct Savanna, a benchmark of 500 prompts across 16 subcategories. On Savanna, even harness frameworks built on the frontier models retrieve a correct reference for only about half of the prompts. We then propose Locate-Corroborate-Isolate, a paradigm in which the agent first pins down the target's identity through text search, then verifies candidate images against multiple sources, and finally crops a clean reference for the generator. Trained on 15K trajectories that follow this paradigm, Ranger-8B achieves a search score of 67.2, outperforming harnesses equipped with frontier models. It also achieves the best generation quality with every generator we test, and surpasses prior agentic methods on other image generation benchmarks. We release the pipeline, benchmark, training data and model at https://github.com/RUCAIBox/Agentic-ImageGen-Wild.

## 技术要点

- 建议先把这篇放回整个方向脉络里看，而不是孤立地看一篇论文。
- 如果你在做路线判断，比起单个指标，更要看它重新定义了什么任务边界。
- 真正的价值通常体现在是否改变了后续研究的默认范式。

## 应用价值

- 适合作为近期方向判断和技术情报输入。
- 适合帮助你发现哪些问题开始被研究社区反复强调。

## 风险与局限

- 当前分析基于论文摘要或配置中的方向摘记，不等价于完整精读。
- 真正的工程价值仍然需要结合实验设计、复现难度和系统成本来判断。

## 推荐谁读

- 需要做方向判断的研究负责人
- 在做生成式产品或 Agent 产品路线规划的人
- 需要追踪交叉方向机会的多模态团队

## 建议继续追问的问题

- 和同方向过去 4 到 8 周的工作做横向比较。
- 重点看实验设置、任务定义和是否真的解决了生产可用性问题。

## 摘要 / 内容摘记

Agentic image generation pairs an image generator with a search agent that retrieves references from the web, extending generation beyond the generator's training data. Real-world requests, however, often concern entities that appeared only days ago. We call this setting Image Generation in the Wild. In this setting, the web offers limited visual evidence, search results are crowded with easily confused entities, and the target is rarely shown on its own. To study this setting, we build an automated pipeline that synthesizes prompts from recent headlines and keeps only those whose real search results are highly confusing, yielding requests that are hard to solve yet natural to ask. With it, we construct Savanna, a benchmark of 500 prompts across 16 subcategories. On Savanna, even harness frameworks built on the frontier models retrieve a correct reference for only about half of the prompts. We then propose Locate-Corroborate-Isolate, a paradigm in which the agent first pins down the target's identity through text search, then verifies candidate images against multiple sources, and finally crops a clean reference for the generator. Trained on 15K trajectories that follow this paradigm, Ranger-8B achieves a search score of 67.2, outperforming harnesses equipped with frontier models. It also achieves the best generation quality with every generator we test, and surpasses prior agentic methods on other image generation benchmarks. We release the pipeline, benchmark, training data and model at https://github.com/RUCAIBox/Agentic-ImageGen-Wild.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。
