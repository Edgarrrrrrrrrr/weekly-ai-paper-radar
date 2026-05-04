# PhysEdit: Physically-Consistent Region-Aware Image Editing via Adaptive Spatio-Temporal Reasoning

> 中文标题：PhysEdit: Physically-Consistent Region-Aware Image Editing via Adaptive Spatio-Temporal Reasoning

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Image / Text-to-Image + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-05-01 |
| 作者 | Guandong Li, Mengxia Ye |
| 原文入口 | [Abstract](http://arxiv.org/abs/2605.00707v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2605.00707v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Image editing instructions are heterogeneous: a color swap, an object insertion, and a physical-action edit all demand different spatial coverage and different reasoning depth, yet existing reasoning-based editors apply a single fixed inference recipe to every instruction. We argue that adaptivity along both the spatial and temporal axes is the missing degree of freedom, and we present PhysEdit, an editing framework built around this principle. PhysEdit introduces two inference-time modules that compose without retraining the backbone. At its core, (1) Complexity-Adaptive Reasoning Depth (CARD) predicts edit complexity directly from the instruction and reference image and allocates the reasoning step count N_r and reasoning-token length r per sample -- turning a previously fixed inference schedule into a conditional-computation problem. CARD is supported by (2) a Spatial Reasoning Mask (SRM) that extracts an instruction-conditioned spatial prior from cross-attention to confine reasoning to regions that semantically require it. On the full 737-case ImgEdit Basic-Edit Suite, PhysEdit delivers a 1.18x wall-clock speedup (64.3s vs. 76.1s per sample) over a strong reasoning baseline while slightly improving instruction adherence (CLIP-T 0.2283 vs. 0.2266, +0.7%) and matching identity preservation within noise (CLIP-I 0.8246 vs. 0.8280). The speedup is category-dependent and reaches 1.52x on appearance-level edits, validating CARD's adaptive allocation as the principal source of efficiency gain. A 30-sample pilot with full ablations isolates the contribution of each module.

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

Image editing instructions are heterogeneous: a color swap, an object insertion, and a physical-action edit all demand different spatial coverage and different reasoning depth, yet existing reasoning-based editors apply a single fixed inference recipe to every instruction. We argue that adaptivity along both the spatial and temporal axes is the missing degree of freedom, and we present PhysEdit, an editing framework built around this principle. PhysEdit introduces two inference-time modules that compose without retraining the backbone. At its core, (1) Complexity-Adaptive Reasoning Depth (CARD) predicts edit complexity directly from the instruction and reference image and allocates the reasoning step count N_r and reasoning-token length r per sample -- turning a previously fixed inference schedule into a conditional-computation problem. CARD is supported by (2) a Spatial Reasoning Mask (SRM) that extracts an instruction-conditioned spatial prior from cross-attention to confine reasoning to regions that semantically require it. On the full 737-case ImgEdit Basic-Edit Suite, PhysEdit delivers a 1.18x wall-clock speedup (64.3s vs. 76.1s per sample) over a strong reasoning baseline while slightly improving instruction adherence (CLIP-T 0.2283 vs. 0.2266, +0.7%) and matching identity preservation within noise (CLIP-I 0.8246 vs. 0.8280). The speedup is category-dependent and reaches 1.52x on appearance-level edits, validating CARD's adaptive allocation as the principal source of efficiency gain. A 30-sample pilot with full ablations isolates the contribution of each module.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。
