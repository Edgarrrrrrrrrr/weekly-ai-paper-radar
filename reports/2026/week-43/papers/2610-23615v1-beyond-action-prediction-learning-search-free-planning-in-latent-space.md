# Beyond Action Prediction: Learning Search-Free Planning in Latent Space

> 中文标题：Beyond Action Prediction: Learning Search-Free Planning in Latent Space

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Video + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-10-16 |
| 作者 | Guanchen Du, Jinhao Du, Yanpeng Sun, Shan Zhang, Na Zhao, Zechao Li |
| 原文入口 | [Abstract](http://arxiv.org/abs/2610.23615v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2610.23615v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Latent world models learn action-conditioned state transitions in a compact representation space, providing a predictive model for visual planning and control. However, planning with these models typically requires costly test-time optimization over action sequences. We propose to replace this online search with a goal-conditioned inverse model that directly predicts actions from current and goal observations. A key challenge is that action prediction alone neither ensures that goal representations encode action-relevant information nor that predicted actions are consistent with the learned latent prediction model. We introduce Hindsight Inverse JEPA Planning (HIJP), a search-free framework that addresses both aspects during training. HIJP relabels future observations along offline trajectories as goals, providing action supervision across multiple temporal horizons. By retaining gradients through the goal representations, this supervision directly shapes the visual representation. HIJP further feeds predicted actions into the latent predictor model and aligns the resulting next-state representations with encoded successor observations, enforcing action-transition consistency. At inference time, the inverse dynamics model and latent predictor models are applied alternately to generate multi-step action sequences without online search. Across four visual control tasks, HIJP achieves 86.8% overall success and a 1.9-16.5x planning speedup over search-based planning.

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

Latent world models learn action-conditioned state transitions in a compact representation space, providing a predictive model for visual planning and control. However, planning with these models typically requires costly test-time optimization over action sequences. We propose to replace this online search with a goal-conditioned inverse model that directly predicts actions from current and goal observations. A key challenge is that action prediction alone neither ensures that goal representations encode action-relevant information nor that predicted actions are consistent with the learned latent prediction model. We introduce Hindsight Inverse JEPA Planning (HIJP), a search-free framework that addresses both aspects during training. HIJP relabels future observations along offline trajectories as goals, providing action supervision across multiple temporal horizons. By retaining gradients through the goal representations, this supervision directly shapes the visual representation. HIJP further feeds predicted actions into the latent predictor model and aligns the resulting next-state representations with encoded successor observations, enforcing action-transition consistency. At inference time, the inverse dynamics model and latent predictor models are applied alternately to generate multi-step action sequences without online search. Across four visual control tasks, HIJP achieves 86.8% overall success and a 1.9-16.5x planning speedup over search-based planning.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。
