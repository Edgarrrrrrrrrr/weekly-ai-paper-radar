# Weekly Paper Radar | 2026 第 32 周

> 2026 年当前阶段，更值得跟踪的是 Agent 与视觉生成交叉方向的系统化演进。

## 本期总览

这份周报不再只看最近几天的新论文，而是把每个方向的长期基石、近期值得关注的新工作、以及研究趋势放在一起看，帮助你做路线判断。

## 总体趋势

- Agentic AI 持续从单轮推理走向工具调用、规划和恢复能力。
- 纯文生图和纯文生视频方向仍然值得看最新会议论文，因为方法迭代往往先在 CVPR / ICLR 等 venue 集中出现。
- 文生图 + Agent 方向更像在构建可编排的视觉工作流，而不只是单次生成。
- 文生视频 + Agent 方向越来越接近世界模型、交互环境和长期控制。

## 继续关注

- 当前跟踪方向：Agentic AI / 文生图 / 文生视频 / 文生图 + Agentic AI / 文生视频 + Agentic AI
- 关注是否出现真正可执行的多工具生成代理工作流。
- 关注视频世界模型是否开始稳定支撑长时序 Agent 训练与评估。

## Agentic AI

这个方向的核心已经从“会不会推理”转向“能不能在真实任务中规划、调用工具并稳定完成任务”。 本期可以重点留意：AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair；Beyond Component Testing: Validating Agentic AI Systems。

### 长期重要论文

| 排名 | 论文 | 为什么值得长期看 | 原文 | 精读 |
| --- | --- | --- | --- | --- |
| 1 | ReAct: Synergizing Reasoning and Acting in Language Models | 这是 Agentic AI 的长期基石论文之一，适合用来理解“思考 + 行动”范式的原点。 | [Abstract](https://arxiv.org/abs/2210.03629) / [PDF](https://arxiv.org/pdf/2210.03629) | [阅读精读](papers/2210-03629-react-synergizing-reasoning-and-acting-in-language-models.md) |
| 2 | Toolformer: Language Models Can Teach Themselves to Use Tools | 如果你关心 Agent 的工具使用能力，这篇是必须长期放在视野里的代表工作。 | [Abstract](https://arxiv.org/abs/2302.04761) / [PDF](https://arxiv.org/pdf/2302.04761) | [阅读精读](papers/2302-04761-toolformer-language-models-can-teach-themselves-to-use-tools.md) |

### 本期关注的新工作

| 排名 | 论文 | 来源 | 发布时间 | 为什么值得看 | 原文 | 精读 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair | arXiv | 2026-07-31 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 Agentic AI 的关键特征。 | [Abstract](http://arxiv.org/abs/2607.29422v1) / [PDF](https://arxiv.org/pdf/2607.29422v1) | [阅读精读](papers/2607-29422v1-agenticrepair-multi-faceted-program-context-engineering-for-agentic-vuln.md) |
| 2 | Beyond Component Testing: Validating Agentic AI Systems | arXiv | 2026-07-31 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 Agentic AI 的关键特征。 | [Abstract](http://arxiv.org/abs/2607.29405v1) / [PDF](https://arxiv.org/pdf/2607.29405v1) | [阅读精读](papers/2607-29405v1-beyond-component-testing-validating-agentic-ai-systems.md) |
| 3 | SeekBrain: An Autonomous Multi-Agent System for Accelerating Neuroscience Discovery | arXiv | 2026-07-31 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 Agentic AI 的关键特征。 | [Abstract](http://arxiv.org/abs/2607.29347v1) / [PDF](https://arxiv.org/pdf/2607.29347v1) | [阅读精读](papers/2607-29347v1-seekbrain-an-autonomous-multi-agent-system-for-accelerating-neuroscience.md) |

### 趋势判断

- 更强调工具使用与规划，而不只是语言推理。 本期样本数：3。
- 研究目标逐步转向真实环境任务完成度。
- 鲁棒性、恢复能力和可验证性会越来越重要。

## 文生图

纯文生图方向更值得关注模型可控性、编辑能力、效率和数据配方，而最新方法往往会先在顶会和 arXiv 同步冒出来。 本期可以重点留意：SatEdit: Mask-Conditioned Image Editing via VLM-Guided Segment Annotation；Evaluation-Verification Reward for Consistent Multi-Reference Image Editing。

### 长期重要论文

| 排名 | 论文 | 为什么值得长期看 | 原文 | 精读 |
| --- | --- | --- | --- | --- |
| 1 | High-Resolution Image Synthesis with Latent Diffusion Models | 这篇几乎是现代文生图路线的基石论文，长期都值得反复回看。 | [Abstract](https://arxiv.org/abs/2112.10752) / [PDF](https://arxiv.org/pdf/2112.10752) | [阅读精读](papers/2112-10752-high-resolution-image-synthesis-with-latent-diffusion-models.md) |
| 2 | Adding Conditional Control to Text-to-Image Diffusion Models | 如果你关心文生图真正可用性，这篇比很多“更大模型”论文更值得长期看。 | [Abstract](https://arxiv.org/abs/2302.05543) / [PDF](https://arxiv.org/pdf/2302.05543) | [阅读精读](papers/2302-05543-adding-conditional-control-to-text-to-image-diffusion-models.md) |

### 本期关注的新工作

| 排名 | 论文 | 来源 | 发布时间 | 为什么值得看 | 原文 | 精读 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SatEdit: Mask-Conditioned Image Editing via VLM-Guided Segment Annotation | arXiv | 2026-07-31 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 的关键特征。 | [Abstract](http://arxiv.org/abs/2607.29367v1) / [PDF](https://arxiv.org/pdf/2607.29367v1) | [阅读精读](papers/2607-29367v1-satedit-mask-conditioned-image-editing-via-vlm-guided-segment-annotation.md) |
| 2 | Evaluation-Verification Reward for Consistent Multi-Reference Image Editing | arXiv | 2026-07-31 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 的关键特征。 | [Abstract](http://arxiv.org/abs/2607.29025v1) / [PDF](https://arxiv.org/pdf/2607.29025v1) | [阅读精读](papers/2607-29025v1-evaluation-verification-reward-for-consistent-multi-reference-image-edit.md) |
| 3 | DualDiT: A Conditional Dual-Output Diffusion Transformer for Joint OCT Image and Segmentation Mask Generation | arXiv | 2026-07-31 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 的关键特征。 | [Abstract](http://arxiv.org/abs/2607.29337v1) / [PDF](https://arxiv.org/pdf/2607.29337v1) | [阅读精读](papers/2607-29337v1-dualdit-a-conditional-dual-output-diffusion-transformer-for-joint-oct-im.md) |

### 趋势判断

- 图像生成研究继续关注更强可控性和更低推理成本。 本期样本数：3。
- 高质量编辑、局部约束和一致性是更实用的方向。
- CVPR / ICLR 里的方法论文通常比单篇 demo 更值得长期看。

## 文生视频

纯文生视频方向更值得持续看长时序一致性、运动建模、可编辑性和训练效率，这类进展在最新会议论文里通常很集中。 本期可以重点留意：MoRoute: Dynamic Routing for In-Context Multimodal Video Generation。

### 长期重要论文

| 排名 | 论文 | 为什么值得长期看 | 原文 | 精读 |
| --- | --- | --- | --- | --- |
| 1 | Video Diffusion Models | 它非常适合用来理解后续绝大多数文生视频方法的共同技术祖先。 | [Abstract](https://arxiv.org/abs/2204.03458) / [PDF](https://arxiv.org/pdf/2204.03458) | [阅读精读](papers/2204-03458-video-diffusion-models.md) |
| 2 | Imagen Video: High Definition Video Generation with Diffusion Models | 如果你要看文生视频真正迈向高质量的一批代表论文，这篇不能缺。 | [Abstract](https://arxiv.org/abs/2210.02303) / [PDF](https://arxiv.org/pdf/2210.02303) | [阅读精读](papers/2210-02303-imagen-video-high-definition-video-generation-with-diffusion-models.md) |

### 本期关注的新工作

| 排名 | 论文 | 来源 | 发布时间 | 为什么值得看 | 原文 | 精读 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | MoRoute: Dynamic Routing for In-Context Multimodal Video Generation | arXiv | 2026-07-31 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 的关键特征。 | [Abstract](http://arxiv.org/abs/2607.29545v1) / [PDF](https://arxiv.org/pdf/2607.29545v1) | [阅读精读](papers/2607-29545v1-moroute-dynamic-routing-for-in-context-multimodal-video-generation.md) |

### 趋势判断

- 视频生成研究的核心仍是长时序一致性和运动质量。 本期样本数：1。
- 世界模型、压缩表示和效率优化越来越重要。
- 顶会论文更适合用来判断真正的技术方向，而不只是看产品效果。

## 文生图 + Agentic AI

这个方向更值得关注的是：大模型如何成为图像生成与编辑工具链的编排层，让生成流程可拆解、可修正、可多步执行。 本期可以重点留意：Evaluation-Verification Reward for Consistent Multi-Reference Image Editing。

### 长期重要论文

| 排名 | 论文 | 为什么值得长期看 | 原文 | 精读 |
| --- | --- | --- | --- | --- |
| 1 | Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models | 这是图像生成 Agent 化的代表作之一，适合用来理解多工具视觉工作流如何被大模型调度。 | [Abstract](https://arxiv.org/abs/2303.04671) / [PDF](https://arxiv.org/pdf/2303.04671) | [阅读精读](papers/2303-04671-visual-chatgpt-talking-drawing-and-editing-with-visual-foundation-models.md) |
| 2 | MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action | 它是理解“视觉生成或视觉专家能力如何被 Agent 框架统一调度”的关键参考。 | [Abstract](https://arxiv.org/abs/2303.11381) / [PDF](https://arxiv.org/pdf/2303.11381) | [阅读精读](papers/2303-11381-mm-react-prompting-chatgpt-for-multimodal-reasoning-and-action.md) |

### 本期关注的新工作

| 排名 | 论文 | 来源 | 发布时间 | 为什么值得看 | 原文 | 精读 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Evaluation-Verification Reward for Consistent Multi-Reference Image Editing | arXiv | 2026-07-31 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。 | [Abstract](http://arxiv.org/abs/2607.29025v1) / [PDF](https://arxiv.org/pdf/2607.29025v1) | [阅读精读](papers/2607-29025v1-evaluation-verification-reward-for-consistent-multi-reference-image-edit.md) |

### 趋势判断

- 图像生成逐步成为可被 Agent 拆解和调度的工作流。 本期样本数：1。
- 编辑、重绘、局部控制等能力会比单纯画质更重要。
- 多模型协作会比单模型单次输出更值得关注。

## 文生视频 + Agentic AI

这个方向正在从单纯的视频生成走向可交互环境、世界模型和长时序控制，为 Agent 提供训练与模拟空间。 本期可以重点留意：BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning；Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving。

### 长期重要论文

| 排名 | 论文 | 为什么值得长期看 | 原文 | 精读 |
| --- | --- | --- | --- | --- |
| 1 | World Models | 虽然它不是今天意义上的文生视频系统，但它是视频世界模型与 Agent 结合最重要的源头之一。 | [Abstract](https://arxiv.org/abs/1803.10122) / [PDF](https://arxiv.org/pdf/1803.10122) | [阅读精读](papers/1803-10122-world-models.md) |
| 2 | Genie: Generative Interactive Environments | 如果你关心视频生成如何进一步成为 Agent 的训练场和模拟器，这篇很值得长期追踪。 | [Abstract](https://arxiv.org/abs/2402.15391) / [PDF](https://arxiv.org/pdf/2402.15391) | [阅读精读](papers/2402-15391-genie-generative-interactive-environments.md) |

### 本期关注的新工作

| 排名 | 论文 | 来源 | 发布时间 | 为什么值得看 | 原文 | 精读 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning | arXiv | 2026-07-31 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。 | [Abstract](http://arxiv.org/abs/2607.29302v1) / [PDF](https://arxiv.org/pdf/2607.29302v1) | [阅读精读](papers/2607-29302v1-bwm-a-low-cost-high-fidelity-world-simulator-for-robot-learning.md) |
| 2 | Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving | arXiv | 2026-07-31 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。 | [Abstract](http://arxiv.org/abs/2607.29031v1) / [PDF](https://arxiv.org/pdf/2607.29031v1) | [阅读精读](papers/2607-29031v1-auto-jepa-a-latent-world-model-of-continuous-intent-for-end-to-end-auton.md) |
| 3 | Transcript-Managed Transformers: Monotone Multi-Agent Collapse and Universality with Two Pop-Enabled Transcripts | arXiv | 2026-07-31 | 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。 | [Abstract](http://arxiv.org/abs/2607.29496v1) / [PDF](https://arxiv.org/pdf/2607.29496v1) | [阅读精读](papers/2607-29496v1-transcript-managed-transformers-monotone-multi-agent-collapse-and-univer.md) |

### 趋势判断

- 视频生成开始和世界模型、模拟环境概念靠近。 本期样本数：3。
- 长时序一致性和动作反馈是关键难点。
- 这一方向更适合关注“环境可用性”而不是单段视频好不好看。

## 说明

- 现在的周报结构按方向组织，不再只看最近一周发了什么。
- 每个方向都会同时保留长期重要论文、近期关注新工作和趋势判断。
- 权威论文 seed 清单可以直接在 `config/pipeline.json` 里维护。

