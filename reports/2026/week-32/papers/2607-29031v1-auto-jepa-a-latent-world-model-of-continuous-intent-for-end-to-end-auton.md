# Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving

> 中文标题：Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Video + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-07-31 |
| 作者 | Jiwei Yang, Zhengxian Chen, Chaosheng Huang, Jun Li |
| 原文入口 | [Abstract](http://arxiv.org/abs/2607.29031v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2607.29031v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Existing autonomous-driving world models typically perform dense prediction of future videos, occupancy states, BEV representations, or agent motion. We argue that planning need not reconstruct the complete future world, but only focus on scene features that affect future ego action. Based on this perspective, we propose Auto-JEPA, an action-oriented latent world model that learns continuous future driving intent through joint-embedding prediction. Given visual observations, egomotion history, and navigation commands, Auto-JEPA predicts an intent embedding aligned with the latent representation of the future ego trajectory. The predicted intent retrieves executable trajectories from a fixed trajectory memory, which are then ranked by a scene-conditioned candidate selection module. Auto-JEPA keeps the visual encoder frozen, requires no explicit perception annotations, and uses no learned trajectory generator. By optimizing only task-specific modules for trajectory representation, intent prediction, and candidate selection, Auto-JEPA achieves 91.3 PDMS on NAVSIM v1 and 89.1 EPDMS on NAVSIM v2. Semantic occlusion experiments show that masking dynamic-agent regions induces an average intent change 2.97x that of equal-area random masking. Moreover, occluding vehicles that affect future driving substantially changes the predicted intent and selected trajectory, whereas both remain essentially unchanged when non-influential vehicles are occluded. These results show that future-intent prediction encourages the model to focus on planning-relevant visual features and supports high-quality planning without dense future-world modeling.

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

Existing autonomous-driving world models typically perform dense prediction of future videos, occupancy states, BEV representations, or agent motion. We argue that planning need not reconstruct the complete future world, but only focus on scene features that affect future ego action. Based on this perspective, we propose Auto-JEPA, an action-oriented latent world model that learns continuous future driving intent through joint-embedding prediction. Given visual observations, egomotion history, and navigation commands, Auto-JEPA predicts an intent embedding aligned with the latent representation of the future ego trajectory. The predicted intent retrieves executable trajectories from a fixed trajectory memory, which are then ranked by a scene-conditioned candidate selection module. Auto-JEPA keeps the visual encoder frozen, requires no explicit perception annotations, and uses no learned trajectory generator. By optimizing only task-specific modules for trajectory representation, intent prediction, and candidate selection, Auto-JEPA achieves 91.3 PDMS on NAVSIM v1 and 89.1 EPDMS on NAVSIM v2. Semantic occlusion experiments show that masking dynamic-agent regions induces an average intent change 2.97x that of equal-area random masking. Moreover, occluding vehicles that affect future driving substantially changes the predicted intent and selected trajectory, whereas both remain essentially unchanged when non-influential vehicles are occluded. These results show that future-intent prediction encourages the model to focus on planning-relevant visual features and supports high-quality planning without dense future-world modeling.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。
