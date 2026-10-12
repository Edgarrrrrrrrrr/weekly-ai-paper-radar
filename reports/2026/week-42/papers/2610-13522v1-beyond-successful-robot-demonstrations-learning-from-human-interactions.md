# Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics

> 中文标题：Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Video / Text-to-Video + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-10-09 |
| 作者 | Peiyan Tu, Cong Wang, Hanxin Zhu, Xin Jin, Zhibo Chen |
| 原文入口 | [Abstract](http://arxiv.org/abs/2610.13522v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2610.13522v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Action-conditioned world models offer a promising foundation for generalist robotic intelligence by predicting the consequences of actions. However, existing robotic datasets provide limited coverage of the diverse interaction dynamics required for generalizable world modeling. Large-scale egocentric human videos offer complementary interaction experience, yet the embodiment gap between human hands and robotic manipulators hinders effective cross-embodiment learning. Meanwhile, the predominance of successful demonstrations leaves failure dynamics substantially underrepresented, limiting the ability of world models to anticipate unsuccessful executions. To address these limitations, we introduce HF-WM, an action-conditioned world model that combines Human interaction learning with Failure-aware post-training. To bridge the embodiment gap, we develop a dual-branch framework that couples video generation with auxiliary pointflow prediction, using stabilized pointflow as a unified motion representation across human and robot interactions while suppressing egocentric camera motion. To improve failure modeling, we further perform Group Relative Policy Optimization (GRPO) post-training on perturbed actions derived from successful demonstrations, guided by action alignment and physical plausibility rewards, enabling the model to learn plausible failure dynamics without paired ground-truth videos. Extensive experiments demonstrate that HF-WM achieves state-of-the-art performance in action-conditioned video generation and exhibits strong utility for policy evaluation in downstream robotic tasks.

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

Action-conditioned world models offer a promising foundation for generalist robotic intelligence by predicting the consequences of actions. However, existing robotic datasets provide limited coverage of the diverse interaction dynamics required for generalizable world modeling. Large-scale egocentric human videos offer complementary interaction experience, yet the embodiment gap between human hands and robotic manipulators hinders effective cross-embodiment learning. Meanwhile, the predominance of successful demonstrations leaves failure dynamics substantially underrepresented, limiting the ability of world models to anticipate unsuccessful executions. To address these limitations, we introduce HF-WM, an action-conditioned world model that combines Human interaction learning with Failure-aware post-training. To bridge the embodiment gap, we develop a dual-branch framework that couples video generation with auxiliary pointflow prediction, using stabilized pointflow as a unified motion representation across human and robot interactions while suppressing egocentric camera motion. To improve failure modeling, we further perform Group Relative Policy Optimization (GRPO) post-training on perturbed actions derived from successful demonstrations, guided by action alignment and physical plausibility rewards, enabling the model to learn plausible failure dynamics without paired ground-truth videos. Extensive experiments demonstrate that HF-WM achieves state-of-the-art performance in action-conditioned video generation and exhibits strong utility for policy evaluation in downstream robotic tasks.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。
