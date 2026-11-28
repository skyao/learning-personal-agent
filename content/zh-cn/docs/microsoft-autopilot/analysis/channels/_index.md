---
title: "Microsoft Autopilot：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 在 Copilot 网页或桌面应用的 Home 导航中配置，日常沟通走 Teams 一对一私聊和邮件，同事可在 Teams 群聊、频道中 @提及它；它有自己的名称、头像、邮箱、日历和 Entra Agent ID，部分操作以自己的身份进行。移动端借 Microsoft 365 Copilot、Teams、Outlook 应用，没有消费级渠道。
---

## 概要

- 配置入口是 Copilot 网页（copilot.cloud.microsoft）或桌面应用的 Home 左侧导航，以 Autopilot 的名字出现，面板含 Overview、Activity、Routines、Settings。
- 日常沟通走 Teams 一对一私聊（更新、提问、审批卡）和邮件：它有自己的邮箱，可把简报发给用户，用户回复邮件即可继续对话。
- 对同事：它有自己的名称、头像和邮箱，在 Copilot、Teams、Outlook 中与用户并列出现；同事可在 Teams 频道或群聊中 @提及它，也可通过它约用户的时间。
- 身份按操作分工：有些操作用 Autopilot 自己的 Entra Agent ID（如以自己的名义发 Teams 消息），有些用代表用户的授权访问（如读日历）。
- 移动端没有独立 App，用 iOS/Android 上的 Microsoft 365 Copilot、Teams、Outlook；没有短信、iMessage、WhatsApp 等消费级渠道。

## 入口一览

| 入口 | 用途 | 来源 |
| --- | --- | --- |
| Copilot 网页或桌面应用 Home 导航 | 创建、配置、查看活动；面板含 Overview、Activity、Routines、Settings | [Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| Teams 一对一私聊 | Autopilot 主动联系用户：更新、提问、需批准的决定；审批卡也出现在这里 | [Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}}) |
| 邮件 | 有自己的邮箱，可把简报等用邮件发给用户，回复即继续对话 | [Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}}) |
| Teams 群聊、频道、会议 | 同事 @提及；用户把工作委派给它；产品页称可把它带进 Teams 的聊天和会议 | [Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}}) |
| 移动端 | iOS/Android 上的 Microsoft 365 Copilot、Teams、Outlook 应用 | [Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}}) |

场景页举例：把简报投递到 Teams、在 Teams 讨论串中跟进负责人、起草并发布回复，已发布的回复对能看到讨论串的人可见（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）。TestingCatalog 转述 Omar Shahine 的推文：他用 iPhone 的 Action Button 录语音备忘，转写后发给 Teams 里的 Autopilot 记录费用（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）。新闻手册称团队「即将」可以把个人 Autopilot 带入 Copilot Workspaces，与人在同一空间协作（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）；Copilot 博客称 Workspaces 中 Autopilot 可领任务（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。

## 自己的名字、头像、邮箱

应用卡写明 Autopilot「有自己的名称、头像和电子邮件地址」，在 Copilot、Teams、Outlook 中与用户并列出现，让同事区分它的工作（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）；概述页称它另有自己的日历（[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})）。用户可在 Microsoft 365 个人资料的「联系人 > 助手」字段把它设为助手，该字段由管理员控制，设置本身不授予权限（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。审批卡把组织外的收件人标为「外部」（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。

博文作者举例：别人可以在 Teams 里和他的 Autopilot（名为 Sebastian）说话来约他的时间，它知道他的日程偏好；他也在群聊和频道中把工作委派给它（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）。场景页写明 Autopilot 以自己的身份发送跟进消息，收件人能看出来自谁的 Autopilot（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）。

## 以谁的名义

FAQ 称身份与操作账户「相关但不同」：有些操作用 Autopilot 自己的身份，有些用代表用户获得的授权访问，例如用用户的权限读日历、以自己的身份与同事沟通；独立身份不意味着不受限的访问（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。管理员文档举例以自身身份发 Teams 消息，并说明执行访问由实际执行的账户、资源、操作和策略决定，专用身份不绕过检查（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。两类操作在审计日志中分别记在 Autopilot 名下和所有者名下，见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})。

发布前原型就有自己的 Entra ID、Exchange 邮箱与 Teams 在线状态（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）；6 月 Scout 预览的消息中心通告则写「使用用户身份进行操作」（[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})）。

UC Today 认为 Ignite 上「每个智能体都进了 Teams」，在频道里出现已不特殊，区别在于智能体向谁负责，而 Autopilot 是唯一有独立目录身份和具名管理者的（[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})）。

## 资料缺口

- Teams 会议中 Autopilot 能做什么（产品页首次提到「会议」，没有细节）。
- 带入 Workspaces 的上线时间。
- 与组织外联系人往来邮件的限制。

## 主要资料

- 官方：[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})（入口与移动端）；[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})（名称、邮箱、身份分工）；[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})（Teams 与邮件用例、Workspaces）；[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})。
- 媒体：[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})。
- industry：[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})（Teams 中各家智能体的身份对比）。
