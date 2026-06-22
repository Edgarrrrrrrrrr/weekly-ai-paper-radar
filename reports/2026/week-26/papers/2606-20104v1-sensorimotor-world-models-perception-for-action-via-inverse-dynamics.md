# Sensorimotor World Models: Perception for Action via Inverse Dynamics

> 中文标题：Sensorimotor World Models: Perception for Action via Inverse Dynamics

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Video + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-06-18 |
| 作者 | Petr Ivashkov, Randall Balestriero, Bernhard Schölkopf |
| 原文入口 | [Abstract](http://arxiv.org/abs/2606.20104v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2606.20104v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Perception for action suggests that representations of the world should be shaped not by visual fidelity alone, but by their relevance for actions. At the same time, latent JEPA-style world models advocate learning compact predictive states from high-dimensional observations to facilitate the prediction of future states, but end-to-end training of these models is nontrivial because representations may collapse if our only goal is to construct a latent state that is easy to predict. We introduce a sensorimotor world model (SMWM): a latent world model trained end-to-end with inverse dynamics regularization. This single regularizer addresses both issues: it prevents representation collapse and induces action-aligned representations. By forcing latent states to preserve information about the action underlying a transition, it biases the model toward the controllable degrees of freedom of the environment while discarding uncontrollable distractors. This yields stable latent world models trained from offline, reward-free trajectories, without frozen encoders, exponential moving averages, or complex latent regularizers. Empirically, SMWM learns compact, interpretable latent spaces and enables competitive planning performance across simple 2D and 3D control tasks.

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

Perception for action suggests that representations of the world should be shaped not by visual fidelity alone, but by their relevance for actions. At the same time, latent JEPA-style world models advocate learning compact predictive states from high-dimensional observations to facilitate the prediction of future states, but end-to-end training of these models is nontrivial because representations may collapse if our only goal is to construct a latent state that is easy to predict. We introduce a sensorimotor world model (SMWM): a latent world model trained end-to-end with inverse dynamics regularization. This single regularizer addresses both issues: it prevents representation collapse and induces action-aligned representations. By forcing latent states to preserve information about the action underlying a transition, it biases the model toward the controllable degrees of freedom of the environment while discarding uncontrollable distractors. This yields stable latent world models trained from offline, reward-free trajectories, without frozen encoders, exponential moving averages, or complex latent regularizers. Empirically, SMWM learns compact, interpretable latent spaces and enables competitive planning performance across simple 2D and 3D control tasks.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。
