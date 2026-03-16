# Weekly Paper Radar | 2026 第 12 周

> 2026 年当前阶段，更值得跟踪的是 Agent 与视觉生成交叉方向的系统化演进。

## 本期总览

这份周报不再只看最近几天的新论文，而是把每个方向的长期基石、近期值得关注的新工作、以及研究趋势放在一起看，帮助你做路线判断。

## 总体趋势

- Agentic AI 持续从单轮推理走向工具调用、规划和恢复能力。
- 文生图 + Agent 方向更像在构建可编排的视觉工作流，而不只是单次生成。
- 文生视频 + Agent 方向越来越接近世界模型、交互环境和长期控制。

## 继续关注

- 当前跟踪方向：Agentic AI / 文生图 + Agentic AI / 文生视频 + Agentic AI
- 关注是否出现真正可执行的多工具生成代理工作流。
- 关注视频世界模型是否开始稳定支撑长时序 Agent 训练与评估。

## Agentic AI

这个方向的核心已经从“会不会推理”转向“能不能在真实任务中规划、调用工具并稳定完成任务”。 本期可以重点留意：Recoverable Tool-Using Agents with Deliberate Planning；Planning-Guided Interactive World Models for Video Agents。

### 长期重要论文

| 排名 | 论文 | 为什么值得长期看 | 原文 | 精读 |
| --- | --- | --- | --- | --- |
| 1 | ReAct: Synergizing Reasoning and Acting in Language Models | 这是 Agentic AI 的长期基石论文之一，适合用来理解“思考 + 行动”范式的原点。 | [Abstract](https://arxiv.org/abs/2210.03629) / [PDF](https://arxiv.org/pdf/2210.03629) | [阅读精读](papers/2210-03629-react-synergizing-reasoning-and-acting-in-language-models.md) |
| 2 | Toolformer: Language Models Can Teach Themselves to Use Tools | 如果你关心 Agent 的工具使用能力，这篇是必须长期放在视野里的代表工作。 | [Abstract](https://arxiv.org/abs/2302.04761) / [PDF](https://arxiv.org/pdf/2302.04761) | [阅读精读](papers/2302-04761-toolformer-language-models-can-teach-themselves-to-use-tools.md) |

### 本期关注的新工作

| 排名 | 论文 | 发布时间 | 为什么值得看 | 原文 | 精读 |
| --- | --- | --- | --- | --- | --- |
| 1 | Recoverable Tool-Using Agents with Deliberate Planning | 2026-03-12 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 Agentic AI 的关键特征。 | [Abstract](http://arxiv.org/abs/2603.00013v1) / [PDF](http://arxiv.org/pdf/2603.00013v1) | [阅读精读](papers/2603-00013v1-recoverable-tool-using-agents-with-deliberate-planning.md) |
| 2 | Planning-Guided Interactive World Models for Video Agents | 2026-03-13 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 Agentic AI 的关键特征。 | [Abstract](http://arxiv.org/abs/2603.00012v1) / [PDF](http://arxiv.org/pdf/2603.00012v1) | [阅读精读](papers/2603-00012v1-planning-guided-interactive-world-models-for-video-agents.md) |

### 趋势判断

- 更强调工具使用与规划，而不只是语言推理。 本期样本数：2。
- 研究目标逐步转向真实环境任务完成度。
- 鲁棒性、恢复能力和可验证性会越来越重要。

## 文生图 + Agentic AI

这个方向更值得关注的是：大模型如何成为图像生成与编辑工具链的编排层，让生成流程可拆解、可修正、可多步执行。 本期可以重点留意：Autonomous Canvas Agents for Text-to-Image Editing Workflows。

### 长期重要论文

| 排名 | 论文 | 为什么值得长期看 | 原文 | 精读 |
| --- | --- | --- | --- | --- |
| 1 | Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models | 这是图像生成 Agent 化的代表作之一，适合用来理解多工具视觉工作流如何被大模型调度。 | [Abstract](https://arxiv.org/abs/2303.04671) / [PDF](https://arxiv.org/pdf/2303.04671) | [阅读精读](papers/2303-04671-visual-chatgpt-talking-drawing-and-editing-with-visual-foundation-models.md) |
| 2 | MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action | 它是理解“视觉生成或视觉专家能力如何被 Agent 框架统一调度”的关键参考。 | [Abstract](https://arxiv.org/abs/2303.11381) / [PDF](https://arxiv.org/pdf/2303.11381) | [阅读精读](papers/2303-11381-mm-react-prompting-chatgpt-for-multimodal-reasoning-and-action.md) |

### 本期关注的新工作

| 排名 | 论文 | 发布时间 | 为什么值得看 | 原文 | 精读 |
| --- | --- | --- | --- | --- | --- |
| 1 | Autonomous Canvas Agents for Text-to-Image Editing Workflows | 2026-03-14 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。 | [Abstract](http://arxiv.org/abs/2603.00011v1) / [PDF](http://arxiv.org/pdf/2603.00011v1) | [阅读精读](papers/2603-00011v1-autonomous-canvas-agents-for-text-to-image-editing-workflows.md) |

### 趋势判断

- 图像生成逐步成为可被 Agent 拆解和调度的工作流。 本期样本数：1。
- 编辑、重绘、局部控制等能力会比单纯画质更重要。
- 多模型协作会比单模型单次输出更值得关注。

## 文生视频 + Agentic AI

这个方向正在从单纯的视频生成走向可交互环境、世界模型和长时序控制，为 Agent 提供训练与模拟空间。 本期可以重点留意：Planning-Guided Interactive World Models for Video Agents。

### 长期重要论文

| 排名 | 论文 | 为什么值得长期看 | 原文 | 精读 |
| --- | --- | --- | --- | --- |
| 1 | World Models | 虽然它不是今天意义上的文生视频系统，但它是视频世界模型与 Agent 结合最重要的源头之一。 | [Abstract](https://arxiv.org/abs/1803.10122) / [PDF](https://arxiv.org/pdf/1803.10122) | [阅读精读](papers/1803-10122-world-models.md) |
| 2 | Genie: Generative Interactive Environments | 如果你关心视频生成如何进一步成为 Agent 的训练场和模拟器，这篇很值得长期追踪。 | [Abstract](https://arxiv.org/abs/2402.15391) / [PDF](https://arxiv.org/pdf/2402.15391) | [阅读精读](papers/2402-15391-genie-generative-interactive-environments.md) |

### 本期关注的新工作

| 排名 | 论文 | 发布时间 | 为什么值得看 | 原文 | 精读 |
| --- | --- | --- | --- | --- | --- |
| 1 | Planning-Guided Interactive World Models for Video Agents | 2026-03-13 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。 | [Abstract](http://arxiv.org/abs/2603.00012v1) / [PDF](http://arxiv.org/pdf/2603.00012v1) | [阅读精读](papers/2603-00012v1-planning-guided-interactive-world-models-for-video-agents.md) |

### 趋势判断

- 视频生成开始和世界模型、模拟环境概念靠近。 本期样本数：1。
- 长时序一致性和动作反馈是关键难点。
- 这一方向更适合关注“环境可用性”而不是单段视频好不好看。

## 说明

- 现在的周报结构按方向组织，不再只看最近一周发了什么。
- 每个方向都会同时保留长期重要论文、近期关注新工作和趋势判断。
- 权威论文 seed 清单可以直接在 `config/pipeline.json` 里维护。

