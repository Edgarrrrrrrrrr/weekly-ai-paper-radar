# Agentic Physics-Grounded Video Generation via Memory-Augmented In-Context Reasoning

> 中文标题：Agentic Physics-Grounded Video Generation via Memory-Augmented In-Context Reasoning

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Agentic AI / Text-to-Video / Text-to-Video + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-10-16 |
| 作者 | Xikang Guan, Shaocong Yang, Yanqi Bao, Can Wang, Zheng Gu, Zhengqing Chen |
| 原文入口 | [Abstract](http://arxiv.org/abs/2610.23677v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2610.23677v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Physical plausibility is essential for realistic video generation. Existing methods impose physical guidance before synthesis via simulations or refined prompts, but this can limit dynamic diversity, miss errors that emerge only after generation, and require repeated regeneration when inconsistencies remain. We therefore study a generate-diagnose-repair paradigm that preserves the original generation capability and selectively repairs physical inconsistencies afterward, raising two key questions: what to repair and how to repair? To address them, we introduce PhysRepair, an agentic video generation framework that combines causal reasoning over the observed physical failure with prior repair experience to enable localized and adaptive correction. Specifically, Spatiotemporal Causal Constraints identify the first invalid physical state and its causally affected states, producing a repair specification that guides physically plausible local regeneration while preserving unaffected content. Experience-augmented In-context Learning combines the ongoing repair context with relevant experience from previous repairs, allowing the agent to adapt its repair decisions across diverse physical failures and accumulate completed trajectories for future cases. Experiments on Physics-IQ Verified across solid mechanics, fluid dynamics, optics, thermodynamics, and magnetism demonstrate that PhysRepair consistently improves the physical plausibility of generated videos over existing methods. Our project page is available at https://xxkkxxx.github.io/PhysRepair-Website/.

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

Physical plausibility is essential for realistic video generation. Existing methods impose physical guidance before synthesis via simulations or refined prompts, but this can limit dynamic diversity, miss errors that emerge only after generation, and require repeated regeneration when inconsistencies remain. We therefore study a generate-diagnose-repair paradigm that preserves the original generation capability and selectively repairs physical inconsistencies afterward, raising two key questions: what to repair and how to repair? To address them, we introduce PhysRepair, an agentic video generation framework that combines causal reasoning over the observed physical failure with prior repair experience to enable localized and adaptive correction. Specifically, Spatiotemporal Causal Constraints identify the first invalid physical state and its causally affected states, producing a repair specification that guides physically plausible local regeneration while preserving unaffected content. Experience-augmented In-context Learning combines the ongoing repair context with relevant experience from previous repairs, allowing the agent to adapt its repair decisions across diverse physical failures and accumulate completed trajectories for future cases. Experiments on Physics-IQ Verified across solid mechanics, fluid dynamics, optics, thermodynamics, and magnetism demonstrate that PhysRepair consistently improves the physical plausibility of generated videos over existing methods. Our project page is available at https://xxkkxxx.github.io/PhysRepair-Website/.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。
