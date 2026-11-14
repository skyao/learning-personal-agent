---
title: "Microsoft Autopilot：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-10
description: >
  Scout 的上下文来自用户已有权限范围内的 Microsoft 365 数据（经 Work IQ），记忆主动形成、标注来源、可查看删除，会话与记忆存在用户的 OneDrive；外部来源的记忆当作数据而非指令。
---

## 概要

- 接入的数据是用户 Microsoft 365 账户本来就能访问的内容：Outlook 邮件与日历、Teams 聊天/频道/会议转录、To Do、OneDrive/SharePoint 文件与 Lists、组织目录；通过设置里的「Sign in to Microsoft 365」授权。
- Work IQ 被官方称为 Scout 的上下文引擎，默认开启，负责跨 Microsoft 365 搜索和复杂查询。
- 记忆由 Scout 在工作中主动保存，每条标注来源（会话推断、导入、外部）；用户可在设置中查看和删除。来自邮件、网页等外部来源的记忆被当作数据而非指令。
- 会话和记忆数据存在用户的 OneDrive（留在租户内），会话历史按设备分开保存；自动化指令和工具输出存在本机。
- 产品负责人在访谈中强调记忆要会「忘」：常用的相关性上升，不用的随时间消退。

## 数据来源：用户已有的 Microsoft 365 权限

入门页说明，在设置中「Sign in to Microsoft 365」后，Scout 可访问邮件、日历、Teams、OneDrive 等，WorkIQ connectivity 默认开启（[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})）。「与 Microsoft 365 协作」页列出完整范围，并说明范围受已连接账户的访问权限限制（[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})）。官方称 Work IQ 是 Scout 的上下文引擎，学习用户工作方式中的人、文件和模式（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[Build 直播]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-build-live-scout" >}})）。9 月更名后的 Autopilot 改称基于 Microsoft IQ，在租户内拥有自己的记忆（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。

社区作者提醒，用户能触及的一切都会被智能体遍历，SharePoint 的过度共享会因此暴露（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。

## 记忆如何形成、存放与删除

使用指南写明（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）：

- 记忆跨会话持久保存，Scout 在工作时主动保存重要信息，「你无需开口要求」。
- 每条记忆记录来源：会话推断、导入或外部；外部来源（邮件、网页消息）的记忆「当作数据而非指令」，据此行动前与用户确认。
- 用户可在设置的记忆部分查看并删除记忆。

会话历史可搜索（如「我上周做了什么」），可恢复旧对话；7 月起会话历史按设备存放在 OneDrive，「每台设备保留自己的对话」（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})）。长对话可按需压缩，上下文窗口大小可选到「Max」，每个自动化可单独设置（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。

负责任 AI FAQ 说明存放位置：会话和记忆数据在用户的 OneDrive，受 Microsoft DPA 与 Purview 下的 OneDrive 控制覆盖；自动化指令和工具输出存在本机，不受该 DPA 覆盖（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})）。

会话还会跟踪 MIP 敏感度标签：读到带标签内容后，会话的敏感度级别升高并在界面显示（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})，见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})）。

## 「也需要忘掉」

Command Line 对谈中，Jakob Werner 描述分层记忆：常用的相关性上升，不用的随时间消退，而不是无限增长的日记；Omar Shahine 以 ChatGPT 记忆里孩子年龄不更新为例，说明事实需随时间变化（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。这是设计理念的表述，文档没有说明消退的具体机制。

Build 时 Nadella 称用户「完全掌控其上下文和记忆」（[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})）。The Neuron 记录的演示中，Scout 识别日历冲突后询问是移动会议还是保护个人时间，并记住该偏好（[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})）。

## 跨设备

工作区 skill 通过云同步跨设备同步，其余 skill 留在本机（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）；会话历史各设备分开。社区作者 6 月（0.22 版）报告个性设置尚不能同步、重装后部分设置不保留（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。

## 资料缺口

- 记忆的数量上限、消退机制是否已实现、是否可导出。
- Autopilot 云端形态下记忆存在哪里，是否仍在用户 OneDrive。
- Work IQ / Microsoft IQ 在 Scout 中索引了哪些数据、刷新频率。

## 主要资料

- 官方：[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})（记忆来源标注、查看删除）；[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})（存放位置）；[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})、[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})（数据范围与授权）；[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})（遗忘的设计理念）；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})。
- 媒体：[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})、[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})、[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})。
