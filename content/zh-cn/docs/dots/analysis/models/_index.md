---
title: "OpenAI Dots：模型"
linkTitle: "模型"
weight: 70
analyzedAt: 2026-11-12
sourcesUntil: 2026-11-11
description: >
  dots 发布时由 GPT-6 Astra 驱动，2026-11-04 起加入 GPT-6.1 Terra；官方只说 dot 会在不同环节调用不同模型，没有公开规则，用户也不能自选。
---

## 概要

- 发布时（2026-09-29）官方称 dots 由 GPT-6 Astra 驱动；2026-11-04 起 GPT-6.1 Terra 成为「驱动 dots 的模型之一」。
- 为 dots 所做的适配，资料中体现在运行框架（harness）、时间预算、dots 专用的确认和审查策略上，没有「为 Personal Agent 单独训练模型」的说法。
- 官方只有一句「你的 dot 可以在工作的不同部分调用不同的模型」，没有公开选择规则；资料中没有用户自选模型的界面。
- 有用户在开发者论坛报告自己的 dot 实际被分配到 GPT-6.1 Sol（低推理强度），怀疑是对 100 美元档的降级测试；这是单个用户的报告，没有官方回应。

## 从 GPT-6 Astra 到「模型家族」

| 时间 | 说法 | 资料 |
| --- | --- | --- |
| 2026-09-29 | dots「由 GPT-6 Astra 驱动」；GPT-6 Astra 系统卡新增「附录：dots」 | [推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}})、[系统卡附录]({{< relref "/docs/dots/sources/official/2026-09-29-gpt-6-astra-system-card-dots" >}}) |
| 2026-10-16 | 有用户称通过浏览器开发者工具看到分配给自己的是 gpt-6.1-sol、推理强度 low | [论坛帖]({{< relref "/docs/dots/sources/community/2026-10-16-rabbitdaisuke-dots-model-ab-test" >}}) |
| 2026-11-04 | 「GPT-6.1 Terra 现在是驱动 dots 的模型之一」 | [11 月 2–6 日更新]({{< relref "/docs/dots/sources/official/2026-11-04-docs-whats-new-november-2-6" >}}) |
| 2026-11-05 | 「我们正在扩大驱动 dots 的前沿模型家族……你的 dot 可以在工作的不同部分调用不同的模型」 | [文档：认识 dots]({{< relref "/docs/dots/sources/official/2026-11-05-docs-meet-dots" >}}) |

安全博客称 Astra 是 OpenAI「能力最强、对齐程度最高的模型」（[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})）。媒体报道基本照引 Astra 的说法。同日收集的帮助中心隐私常见问题仍只提 Astra，未同步 Terra（[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}})）。

## 适配在运行框架上，而不是新模型

系统卡附录的描述是：dots 构建在现有模型和智能体能力之上；评估中把同一个 Astra 分别放在 Codex 和 dots 两种运行框架中比较；新增「时间预算」设置，最终产品结合时间预算与推理强度；dots 有专用的确认策略（优先级高于 Codex 运行框架的策略），自动审查也有 dots 专用指令（[系统卡附录]({{< relref "/docs/dots/sources/official/2026-09-29-gpt-6-astra-system-card-dots" >}})）。附录中的 GPT-6 Sol 只作为对照出现。附录的评估数字（提示注入、越权、未对齐率等）见[安全]({{< relref "/docs/dots/analysis/security" >}})。

推断：从系统卡看，OpenAI 把 dots 定位为「同一前沿模型 + 新的运行框架」，长时间运行的需求通过时间预算和运行框架解决，而不是训练一个专门的 Personal Agent 模型。资料中没有否定这一点的说法，但也没有官方明确表述。

## 模型怎么选：只有一句话

官方只写了 dot 可以在工作的不同部分调用不同模型，没有说明按任务类型、推理强度、订阅档位还是成本来分。企业管理员的模型控制不适用于主 dot 对话；dot 委派出去的 Work 与 Codex 任务遵循各自产品的模型权限（[帮助中心：工作区管理]({{< relref "/docs/dots/sources/official/2026-11-05-help-manage-dots-in-workspaces" >}})）。

用户侧唯一的证据是 2026-10-16 的论坛帖：作者称在开发者工具中看到 `gpt-6.1-sol`、`reasoningEffort: low`，截图中 `originator` 字段为 `codex_cloud`；他据此认为 OpenAI 在对 100 美元档用户做降级 A/B 测试，并描述了低档模型的表现（频繁请求权限、优先与插件交互等）。帖子在 24 小时后自动关闭，没有 OpenAI 回应（[论坛帖]({{< relref "/docs/dots/sources/community/2026-10-16-rabbitdaisuke-dots-model-ab-test" >}})）。「A/B 测试」「降级」是作者的推断。

推断：`originator` 为 `codex_cloud` 说明作者看到的可能是 dot 委派出去的 Codex 云端任务，而不是主 dot 对话；这与官方「委派任务遵循各自产品的模型权限」以及之后「调用不同模型」的说法相容。资料不足以确认。

## 资料缺口

- 不同模型的分工规则：Terra 是否取代 Astra，谁负责主对话、谁负责长任务。
- 时间预算和推理强度是否随订阅档位（Pro 100/200/500 美元）变化，是否向用户公开。
- 语音通话使用的模型。
- OpenAI 对论坛帖中 GPT-6.1 Sol 报告的回应。

## 主要资料

- 官方：[GPT-6 Astra 系统卡：附录 dots]({{< relref "/docs/dots/sources/official/2026-09-29-gpt-6-astra-system-card-dots" >}})（运行框架、时间预算）；[11 月 2–6 日更新]({{< relref "/docs/dots/sources/official/2026-11-04-docs-whats-new-november-2-6" >}})（加入 Terra）；[文档：认识 dots]({{< relref "/docs/dots/sources/official/2026-11-05-docs-meet-dots" >}})（模型家族）；[帮助中心：工作区管理]({{< relref "/docs/dots/sources/official/2026-11-05-help-manage-dots-in-workspaces" >}})（企业模型控制不适用）。
- 社区：[rabbitdaisuke 论坛帖]({{< relref "/docs/dots/sources/community/2026-10-16-rabbitdaisuke-dots-model-ab-test" >}})（GPT-6.1 Sol 报告）。
