# 5. Reasoning over Video: Evaluating How MLLMs Extract, Integrate, and Reconstruct Spatiotemporal Evidence

> 中文标题：Reasoning over Video: Evaluating How MLLMs Extract, Integrate, and Reconstruct Spatiotemporal Evidence

> 这篇论文同时命中了 Agentic AI 方向的关键词，而且发布时间很近，适合作为本周优先跟踪对象。

| 字段 | 内容 |
| --- | --- |
| 方向 | Agentic AI |
| 来源 | arXiv |
| 发布时间 | 2026-03-13 |
| 作者 | Seunghwan Bang, Hwanjun Song |
| 原文入口 | [Abstract](http://arxiv.org/abs/2603.13091v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2603.13091v1) |

## 为什么值得看

从关键词覆盖、发布时间和主题贴合度来看，这篇论文值得进入本周跟踪列表。

## 核心方法

The growing interest in embodied agents increases the demand for spatiotemporal video understanding, yet existing benchmarks largely emphasize extractive reasoning, where answers can be explicitly presented within spatiotemporal events

## 技术要点

- 论文摘要显示其核心贡献和当前关注方向高度相关。
- 如果你在做路线判断，这篇更适合拿来快速理解最新思路。
- 建议结合原文的实验部分进一步确认真实增益。

## 应用价值

- 可作为相关方向的技术情报输入。
- 可辅助判断近期研究热点是否发生迁移。

## 风险与局限

- 当前分析基于摘要，不等价于完整精读。
- 真正的工程可用性还需要看实验设计和复现实验。

## 推荐谁读

- 做多模态生成研究的人
- 做视频生成或 Agent 产品判断的人
- 需要跟踪前沿技术路线的团队负责人

## 建议继续追问的问题

- 阅读原文方法部分与实验设置。
- 对比最近 4 到 6 周同方向论文的变化。

## 摘要摘录

> The growing interest in embodied agents increases the demand for spatiotemporal video understanding, yet existing benchmarks largely emphasize extractive reasoning, where answers can be explicitly presented within spatiotemporal events. It remains unclear whether multimodal large language models can instead perform abstractive spatiotemporal reasoning, which requires integrating observations over time, combining dispersed cues, and inferring implicit spatial and contextual structure. To address this gap, we formalize abstractive spatiotemporal reasoning from videos by introducing a structured evaluation taxonomy that systematically targets its core dimensions and construct a controllable, scenario-driven synthetic egocentric video dataset tailored to evaluate abstractive spatiotemporal reasoning capabilities, spanning object-, room-, and floor-plan-level scenarios. Based on this framework, we present VAEX-BENCH, a benchmark comprising five abstractive reasoning tasks together with their extractive counterparts. Our extensive experiments compare the performance of state-of-the-art MLLMs under extractive and abstractive settings, exposing their limitations on abstractive tasks and providing a fine-grained analysis of the underlying bottlenecks. The dataset will be released soon.

## 一句话结论

这篇论文同时命中了 Agentic AI 方向的关键词，而且发布时间很近，适合作为本周优先跟踪对象。
