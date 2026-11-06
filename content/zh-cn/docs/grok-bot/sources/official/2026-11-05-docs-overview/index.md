---
title: "文档：Grok Bot 概览"
linkTitle: "文档：概览"
date: 2026-11-05
originalTitle: "Grok Bot"
sourceUrl: "https://cursor.com/docs/grok-bot"
altUrls: ["https://docs.x.ai/grok-bot/overview"]
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [运行环境, 记忆与上下文, 开放与价格]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Grok Bot 提供可长期保留的 Bot，每个 Bot 在持久的云端计算机上工作，有浏览器、文件系统和终端，任务在真实工具中完成而不是停在聊天草稿。用户通过发消息交办任务，Bot 跨应用和网站完成多步工作，需要审批时回来找人；设置只是发一条消息，不需要搭建工作流。同一用户的所有 Bot 共用一台云端计算机，共享文件、浏览器会话和应用登录，用户之间则严格隔离；每个 Bot 在共享计算机上有自己的屏幕，一个 Bot 一次只能在其屏幕上运行一个计算机使用任务。Bot 的记忆是稳定偏好、角色上下文和过往工作摘要，对重要决策应让 Bot 查看当前来源而不是依赖记忆。支持 macOS、Windows、Linux、iOS、Android，访问权包含在每个付费个人 Cursor 套餐和 Teams 中，用量每周重置。

**保留理由**：这是官方文档的总览，把计算机共享模型、记忆范围和访问权来源集中说了一遍，是读其他文档前的框架。

---

Grok Bot 为你提供可以长期保留的 Bot：有名字、有职责、上下文会随时间不断累积的 AI 队友（AI teammates）。每个 Bot 都在一台持久的云端计算机（cloud computer）上工作，配有浏览器、文件系统和终端，因此任务会在你实际使用的工具中完成，而不是停留为聊天草稿。从你的第一个 Bot [开始使用](https://cursor.com/docs/grok-bot/get-started)，或阅读[团队如何推广使用](https://cursor.com/docs/grok-bot/teams)。

你通过与 Bot 发消息来协作。给它一项任务、相关上下文，以及它所需工具的访问权。它会跨应用和网站承担多步工作，在对话中持续向你更新进展，并在某件事需要你批准时回来找你。

Grok Bot 可在 macOS、Windows、Linux、iOS 和 Android 上运行，并包含在每个付费个人 Cursor 套餐和 Cursor Teams 套餐中。你也可以关联个人 SuperGrok、SuperGrok Plus 或 SuperGrok Heavy 订阅，或以自助式 Grok Business 套餐中的一个席位登录。完整对照表见[套餐与计费](https://cursor.com/help/grok-bot/plans)。

## Grok Bot 有何不同

- **每个 Bot 都有一台计算机。** 你的 Bot 运行在一台持久的云端计算机上，配有浏览器、文件系统和终端。它们在有可用[已连接应用（connected apps）](https://cursor.com/docs/grok-bot/work#connect-apps)时使用这些应用，其余一切则使用计算机使用（computer use），并且在你合上笔记本电脑时工作仍会继续。
- **设置是一条消息，不是工作流搭建器。** 创建一个 Bot，描述工作，并在它请求时授予访问权。同一个 Bot 可以从桌面应用以及 iPhone 和 Android 应用访问。
- **Bot 之间会互相协调。** 你的 Bot 可以并行运行、互相发消息、在[群聊（group chats）](https://cursor.com/docs/grok-bot/work#group-chats)中共享上下文，并转移任务的所有权，因此你不必充当工具之间的路由器。
- **Bot 通过示范学习工作流。** 带一个 Bot 走一遍多步路径，它就能把这条路径保存为[技能（skill）](https://cursor.com/docs/grok-bot/work#skills-and-routines)，并按计划重新运行。
- **上下文会累积。** 一个有名字的 Bot 会在不同会话之间保留其记忆、文件、浏览器会话和偏好，而不是每项任务都重置。

## 你的 Bot 共用一台计算机

你所有的 Bot 共用同一台云端计算机，共享其文件、浏览器会话和应用登录，这让交接无需重复设置即可进行。这台计算机属于你的账号，而不属于某个单独的 Bot，因此凡放在它上面的内容，都应视为你运行的每个 Bot 都能使用；用户之间则严格隔离。[计算机与应用](https://cursor.com/docs/grok-bot/work#the-computer-and-apps)介绍了完整模型。当你与队友的[共享 Bot（shared Bot）](https://cursor.com/help/grok-bot/shared-bots)聊天时，它通常也在你的计算机上工作。

## 一次好的首次交办

从一项跨几个工具、且有清晰终点的真实任务开始：

> 从我们的 CRM 中拉取本周的销售管道复盘名单。跳过任何已处于活跃序列（active sequence）中的人。在网上和 Slack 上调研排名前五的客户，找到合适的联系人，用我的语气起草外联内容，并在明天早上之前把草稿留给我审批。

这告诉 Bot 要做什么、在哪里工作、要拉取哪些上下文，以及完成的工作是什么样子。审阅结果、纠正它，再把稳定的流程变成[技能或例程（skill or routine）](https://cursor.com/docs/grok-bot/work#skills-and-routines)。

## 常见问题

### 合上笔记本电脑后，Grok Bot 还会继续工作吗？

会。工作在云端计算机上运行。关闭应用、笔记本电脑或手机，都不会停止一个后台回合（background turn）或一个例程。

### 多个 Bot 可以同时工作吗？

可以。Bot 可以推理、使用已连接应用、处理文件并并行协调。每个 Bot 在共享计算机上有自己的屏幕，一个 Bot 一次只能在其屏幕上运行一个计算机使用任务。

### Bot 会记住什么？

稳定的偏好、角色上下文，以及过往工作的摘要。对话和学到的上下文按 Bot 分开保留，而共享文件、浏览器会话和直接交接会在它们之间传递上下文。对于有后果的决策，应让 Bot 查看当前来源，而不是依赖记忆。

### Bot 可以使用任何网站吗？

Bot 可以使用许多基于浏览器的工具，包括没有已连接应用的服务。网站仍可能阻止自动化、让会话过期，或要求人工步骤。Bot 会把这些步骤交给你，而不是绕过它们。

### 支持哪些平台？

桌面应用可在 macOS（Apple 芯片与 Intel）、Windows（x64 与 Arm64）和 Linux（x64 与 Arm64）上运行，移动应用可在 iPhone 和 Android 上运行。Bot 工作所用的计算机运行在 Cursor 的云中。

### Grok Bot 的费用是多少？

访问权包含在每个付费个人 Cursor 套餐和 Cursor Teams 套餐中，也可通过关联个人 SuperGrok 账号，或以自助式 Grok Business 套餐中的一个席位获得。用量每周重置。见[套餐与计费](https://cursor.com/help/grok-bot/plans)。

## 下一步

[开始使用

安装应用，创建你的第一个 Bot，并交给它一项有用的任务。](https://cursor.com/docs/grok-bot/get-started)[使用场景

适合的岗位，附带可自行调整的起始提示。](https://cursor.com/docs/grok-bot/use-cases)[使用 Grok Bot

Bot、消息、共享计算机，以及技能和例程，都在一处。](https://cursor.com/docs/grok-bot/work)[团队与企业

管理控制、身份、私有网络，以及推荐的推广基线。](https://cursor.com/docs/grok-bot/teams)[安全

网络策略、审批与自动审阅（Auto Review）、日志，以及数据处理。](https://cursor.com/docs/grok-bot/security)[部署

将桌面应用推送到受管设备，选择版本，并规划更新。](https://cursor.com/docs/grok-bot/deployment)
