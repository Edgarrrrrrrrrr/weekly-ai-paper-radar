# Weekly Paper Radar

每周自动更新五个方向的长期重要论文、近期新工作、原文链接和中文精读：Agentic AI、文生图、文生视频、文生图 + Agentic AI、文生视频 + Agentic AI。

- 最新周报：[查看 2026 第 32 周](reports/2026/week-32/README.md)
- 自动更新：每周一 09:00（北京时间）
- 来源：arXiv + ICLR + CVPR
- 结构：长期重要论文 + 本期关注 + 趋势判断

> 2026 年当前阶段，更值得跟踪的是 Agent 与视觉生成交叉方向的系统化演进。

## Agentic AI

这个方向的核心已经从“会不会推理”转向“能不能在真实任务中规划、调用工具并稳定完成任务”。 本期可以重点留意：AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair；Beyond Component Testing: Validating Agentic AI Systems。

### 长期重要论文

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | [PDF](https://arxiv.org/pdf/2210.03629) | arXiv | [精读](reports/2026/week-32/papers/2210-03629-react-synergizing-reasoning-and-acting-in-language-models.md)
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | [PDF](https://arxiv.org/pdf/2302.04761) | arXiv | [精读](reports/2026/week-32/papers/2302-04761-toolformer-language-models-can-teach-themselves-to-use-tools.md)

### 本期关注

- [AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair](http://arxiv.org/abs/2607.29422v1) | [PDF](https://arxiv.org/pdf/2607.29422v1) | arXiv | [精读](reports/2026/week-32/papers/2607-29422v1-agenticrepair-multi-faceted-program-context-engineering-for-agentic-vuln.md)
- [Beyond Component Testing: Validating Agentic AI Systems](http://arxiv.org/abs/2607.29405v1) | [PDF](https://arxiv.org/pdf/2607.29405v1) | arXiv | [精读](reports/2026/week-32/papers/2607-29405v1-beyond-component-testing-validating-agentic-ai-systems.md)
- [SeekBrain: An Autonomous Multi-Agent System for Accelerating Neuroscience Discovery](http://arxiv.org/abs/2607.29347v1) | [PDF](https://arxiv.org/pdf/2607.29347v1) | arXiv | [精读](reports/2026/week-32/papers/2607-29347v1-seekbrain-an-autonomous-multi-agent-system-for-accelerating-neuroscience.md)

## 文生图

纯文生图方向更值得关注模型可控性、编辑能力、效率和数据配方，而最新方法往往会先在顶会和 arXiv 同步冒出来。 本期可以重点留意：SatEdit: Mask-Conditioned Image Editing via VLM-Guided Segment Annotation；Evaluation-Verification Reward for Consistent Multi-Reference Image Editing。

### 长期重要论文

- [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752) | [PDF](https://arxiv.org/pdf/2112.10752) | arXiv | [精读](reports/2026/week-32/papers/2112-10752-high-resolution-image-synthesis-with-latent-diffusion-models.md)
- [Adding Conditional Control to Text-to-Image Diffusion Models](https://arxiv.org/abs/2302.05543) | [PDF](https://arxiv.org/pdf/2302.05543) | arXiv | [精读](reports/2026/week-32/papers/2302-05543-adding-conditional-control-to-text-to-image-diffusion-models.md)

### 本期关注

- [SatEdit: Mask-Conditioned Image Editing via VLM-Guided Segment Annotation](http://arxiv.org/abs/2607.29367v1) | [PDF](https://arxiv.org/pdf/2607.29367v1) | arXiv | [精读](reports/2026/week-32/papers/2607-29367v1-satedit-mask-conditioned-image-editing-via-vlm-guided-segment-annotation.md)
- [Evaluation-Verification Reward for Consistent Multi-Reference Image Editing](http://arxiv.org/abs/2607.29025v1) | [PDF](https://arxiv.org/pdf/2607.29025v1) | arXiv | [精读](reports/2026/week-32/papers/2607-29025v1-evaluation-verification-reward-for-consistent-multi-reference-image-edit.md)
- [DualDiT: A Conditional Dual-Output Diffusion Transformer for Joint OCT Image and Segmentation Mask Generation](http://arxiv.org/abs/2607.29337v1) | [PDF](https://arxiv.org/pdf/2607.29337v1) | arXiv | [精读](reports/2026/week-32/papers/2607-29337v1-dualdit-a-conditional-dual-output-diffusion-transformer-for-joint-oct-im.md)

## 文生视频

纯文生视频方向更值得持续看长时序一致性、运动建模、可编辑性和训练效率，这类进展在最新会议论文里通常很集中。 本期可以重点留意：MoRoute: Dynamic Routing for In-Context Multimodal Video Generation。

### 长期重要论文

- [Video Diffusion Models](https://arxiv.org/abs/2204.03458) | [PDF](https://arxiv.org/pdf/2204.03458) | arXiv | [精读](reports/2026/week-32/papers/2204-03458-video-diffusion-models.md)
- [Imagen Video: High Definition Video Generation with Diffusion Models](https://arxiv.org/abs/2210.02303) | [PDF](https://arxiv.org/pdf/2210.02303) | arXiv | [精读](reports/2026/week-32/papers/2210-02303-imagen-video-high-definition-video-generation-with-diffusion-models.md)

### 本期关注

- [MoRoute: Dynamic Routing for In-Context Multimodal Video Generation](http://arxiv.org/abs/2607.29545v1) | [PDF](https://arxiv.org/pdf/2607.29545v1) | arXiv | [精读](reports/2026/week-32/papers/2607-29545v1-moroute-dynamic-routing-for-in-context-multimodal-video-generation.md)

## 文生图 + Agentic AI

这个方向更值得关注的是：大模型如何成为图像生成与编辑工具链的编排层，让生成流程可拆解、可修正、可多步执行。 本期可以重点留意：Evaluation-Verification Reward for Consistent Multi-Reference Image Editing。

### 长期重要论文

- [Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models](https://arxiv.org/abs/2303.04671) | [PDF](https://arxiv.org/pdf/2303.04671) | arXiv | [精读](reports/2026/week-32/papers/2303-04671-visual-chatgpt-talking-drawing-and-editing-with-visual-foundation-models.md)
- [MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action](https://arxiv.org/abs/2303.11381) | [PDF](https://arxiv.org/pdf/2303.11381) | arXiv | [精读](reports/2026/week-32/papers/2303-11381-mm-react-prompting-chatgpt-for-multimodal-reasoning-and-action.md)

### 本期关注

- [Evaluation-Verification Reward for Consistent Multi-Reference Image Editing](http://arxiv.org/abs/2607.29025v1) | [PDF](https://arxiv.org/pdf/2607.29025v1) | arXiv | [精读](reports/2026/week-32/papers/2607-29025v1-evaluation-verification-reward-for-consistent-multi-reference-image-edit.md)

## 文生视频 + Agentic AI

这个方向正在从单纯的视频生成走向可交互环境、世界模型和长时序控制，为 Agent 提供训练与模拟空间。 本期可以重点留意：BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning；Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving。

### 长期重要论文

- [World Models](https://arxiv.org/abs/1803.10122) | [PDF](https://arxiv.org/pdf/1803.10122) | arXiv | [精读](reports/2026/week-32/papers/1803-10122-world-models.md)
- [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) | [PDF](https://arxiv.org/pdf/2402.15391) | arXiv | [精读](reports/2026/week-32/papers/2402-15391-genie-generative-interactive-environments.md)

### 本期关注

- [BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning](http://arxiv.org/abs/2607.29302v1) | [PDF](https://arxiv.org/pdf/2607.29302v1) | arXiv | [精读](reports/2026/week-32/papers/2607-29302v1-bwm-a-low-cost-high-fidelity-world-simulator-for-robot-learning.md)
- [Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving](http://arxiv.org/abs/2607.29031v1) | [PDF](https://arxiv.org/pdf/2607.29031v1) | arXiv | [精读](reports/2026/week-32/papers/2607-29031v1-auto-jepa-a-latent-world-model-of-continuous-intent-for-end-to-end-auton.md)
- [Transcript-Managed Transformers: Monotone Multi-Agent Collapse and Universality with Two Pop-Enabled Transcripts](http://arxiv.org/abs/2607.29496v1) | [PDF](https://arxiv.org/pdf/2607.29496v1) | arXiv | [精读](reports/2026/week-32/papers/2607-29496v1-transcript-managed-transformers-monotone-multi-agent-collapse-and-univer.md)

## 历史周报

- [2026 第 32 周](reports/2026/week-32/README.md)
- [2026 第 30 周](reports/2026/week-30/README.md)
- [2026 第 29 周](reports/2026/week-29/README.md)
- [2026 第 28 周](reports/2026/week-28/README.md)
- [2026 第 27 周](reports/2026/week-27/README.md)
- [2026 第 26 周](reports/2026/week-26/README.md)
- [2026 第 25 周](reports/2026/week-25/README.md)
- [2026 第 24 周](reports/2026/week-24/README.md)

## 说明

- 仓库首页只展示论文入口和方向导航。
- 运行与配置说明已移到 [docs/SETUP.md](docs/SETUP.md)。
