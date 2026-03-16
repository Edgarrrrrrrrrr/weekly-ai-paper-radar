# 2. SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation

> 中文标题：SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation

> 这篇论文同时命中了 Text-to-Image / Text-to-Video 方向的关键词，而且发布时间很近，适合作为本周优先跟踪对象。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Image / Text-to-Video |
| 来源 | arXiv |
| 发布时间 | 2026-03-13 |
| 作者 | Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding |
| 原文入口 | [Abstract](http://arxiv.org/abs/2603.13024v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2603.13024v1) |

## 为什么值得看

从关键词覆盖、发布时间和主题贴合度来看，这篇论文值得进入本周跟踪列表。

## 核心方法

A surgical world model capable of generating realistic surgical action videos with precise control over tool-tissue interactions can address fundamental challenges in surgical AI and simulation -- from data scarcity and rare event synthesis to bridging the sim-to-real gap for surgical automation

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

> A surgical world model capable of generating realistic surgical action videos with precise control over tool-tissue interactions can address fundamental challenges in surgical AI and simulation -- from data scarcity and rare event synthesis to bridging the sim-to-real gap for surgical automation. However, current video generation methods, the very core of such surgical world models, require expensive annotations or complex structured intermediates as conditioning signals at inference, limiting their scalability. Other approaches exhibit limited temporal consistency across complex laparoscopic scenes and do not possess sufficient realism. We propose Surgical Action World (SAW) -- a step toward surgical action world modeling through video diffusion conditioned on four lightweight signals: language prompts encoding tool-action context, a reference surgical scene, tissue affordance mask, and 2D tool-tip trajectories. We design a conditional video diffusion approach that reformulates video-to-video diffusion into trajectory-conditioned surgical action synthesis. The backbone diffusion model is fine-tuned on a custom-curated dataset of 12,044 laparoscopic clips with lightweight spatiotemporal conditioning signals, leveraging a depth consistency loss to enforce geometric plausibility without requiring depth at inference. SAW achieves state-of-the-art temporal consistency (CD-FVD: 199.19 vs. 546.82) and strong visual quality on held-out test data. Furthermore, we demonstrate its downstream utility for (a) surgical AI, where augmenting rare actions with SAW-generated videos improves action recognition (clipping F1-score: 20.93% to 43.14%; cutting: 0.00% to 8.33%) on real test data, and (b) surgical simulation, where rendering tool-tissue interaction videos from simulator-derived trajectory points toward a visually faithful simulation engine.

## 一句话结论

这篇论文同时命中了 Text-to-Image / Text-to-Video 方向的关键词，而且发布时间很近，适合作为本周优先跟踪对象。
