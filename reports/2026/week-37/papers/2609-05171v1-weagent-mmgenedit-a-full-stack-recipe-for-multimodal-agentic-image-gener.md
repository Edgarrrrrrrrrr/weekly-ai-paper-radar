# WeAgent-MMGenEdit: A Full-Stack Recipe for Multimodal Agentic Image Generation and Editing

> 中文标题：WeAgent-MMGenEdit: A Full-Stack Recipe for Multimodal Agentic Image Generation and Editing

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Agentic AI / Text-to-Image / Text-to-Image + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-09-04 |
| 作者 | Hui Zhang, Zongkai Liu, Liqiang Niu, Juntao Liu, Han Li, Zhen Cao |
| 原文入口 | [Abstract](http://arxiv.org/abs/2609.05171v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2609.05171v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Image generation and editing models have advanced rapidly, yet remain unreliable when prompts require external world knowledge. Bounded and long-tail parametric knowledge prevents direct or reason-then-generate approaches from recovering the required facts and visual appearances. Existing agentic generation and editing methods mitigate this limitation with retrieval tools, yet remain constrained by insufficient visual verification, overloaded policy models, and weak integration of retrieved textual and visual evidence. To address these limitations, we present WeAgent-MMGenEdit, a full-stack recipe including a multimodal harness, a scalable data construction pipeline, a comprehensive benchmark, and post-training methods for the agent policy and image backend. We first introduce WeAgent-Harness, a multimodal runtime with persistent evidence management and dedicated verification and integration tools that organize retrieved multimodal evidence into a dense carrier. Upon this, we develop a scalable pipeline for prompt synthesis and agentic trajectory collection, yielding 23K supervised trajectories and 14.7K RL tasks with three-layer verifiable checklists. We further introduce WeBench-MMGenEdit, a bilingual benchmark covering both knowledge-intensive image generation and multi-image editing. Finally, a two-sided post-training recipe based on SFT and RL improves the agent policy and image backend. Together, WeAgent-MMGenEdit enables a 30B-total/3B-active policy to outperform similarly sized policy models and approach the performance of a 1T-parameter agent.

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

Image generation and editing models have advanced rapidly, yet remain unreliable when prompts require external world knowledge. Bounded and long-tail parametric knowledge prevents direct or reason-then-generate approaches from recovering the required facts and visual appearances. Existing agentic generation and editing methods mitigate this limitation with retrieval tools, yet remain constrained by insufficient visual verification, overloaded policy models, and weak integration of retrieved textual and visual evidence. To address these limitations, we present WeAgent-MMGenEdit, a full-stack recipe including a multimodal harness, a scalable data construction pipeline, a comprehensive benchmark, and post-training methods for the agent policy and image backend. We first introduce WeAgent-Harness, a multimodal runtime with persistent evidence management and dedicated verification and integration tools that organize retrieved multimodal evidence into a dense carrier. Upon this, we develop a scalable pipeline for prompt synthesis and agentic trajectory collection, yielding 23K supervised trajectories and 14.7K RL tasks with three-layer verifiable checklists. We further introduce WeBench-MMGenEdit, a bilingual benchmark covering both knowledge-intensive image generation and multi-image editing. Finally, a two-sided post-training recipe based on SFT and RL improves the agent policy and image backend. Together, WeAgent-MMGenEdit enables a 30B-total/3B-active policy to outperform similarly sized policy models and approach the performance of a 1T-parameter agent.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。
