---
title: "Microsoft Autopilot：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 在 Copilot 网页/桌面应用的 Home 导航中管理，日常沟通走 Teams 一对一私聊和邮件，同事可在 Teams 群聊、频道中 @提及它；它有自己的名称、头像、邮箱和日历，以自己的身份发消息；移动端借 Microsoft 365 Copilot、Teams、Outlook 应用。Scout 时期「自己的 Entra 身份」与「用户身份」的说法分歧，新文档以「两种身份按操作分工」解决。
---

## 概要

- 管理入口在 Copilot 网页（copilot.cloud.microsoft）或桌面应用 Home 左侧导航，以 Autopilot 的名字出现，面板含 Overview、Activity、Routines、Settings（[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})）。
- 日常沟通走 Teams 一对一私聊（更新、提问、审批）和邮件：它有自己的邮箱，可以发邮件让用户直接回复（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）。
- 对同事：Autopilot 有自己的名称、头像和邮箱，在 Copilot、Teams、Outlook 中与用户并列出现；同事可在 Teams 频道或群聊中 @提及它询问或请求受支持的操作，也可通过它约用户的时间（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）。
- 身份问题有了文档答案：有些操作用 Autopilot 自己的 Entra Agent ID（如以自己的名义发 Teams 消息），有些用代表用户的授权访问（如读日历）（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。
- 移动端没有独立 App，用 iOS/Android 上的 Microsoft 365 Copilot、Teams、Outlook；仍没有短信、iMessage 等消费级渠道（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

## 2026-11：Copilot 应用、Teams 与邮件

| 入口 | 用途 | 来源 |
| --- | --- | --- |
| Copilot 网页或桌面应用 Home 导航 | 创建、配置、查看活动；面板含 Overview、Activity、Routines、Settings | [Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| Teams 一对一私聊 | Autopilot 主动联系用户：更新、提问、需批准的决定；审批卡也出现在这里 | [Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}}) |
| 邮件 | 有自己的邮箱，可把简报等用邮件发给用户，用户回复即继续对话 | [Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}}) |
| Teams 群聊、频道、会议 | 同事 @提及；用户把工作委派给它；产品页称可带进 Teams 的聊天和会议 | [Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}}) |
| 移动端 | iOS/Android 上的 Microsoft 365 Copilot、Teams、Outlook 应用 | [Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}}) |

场景页举例：把简报投递到 Teams、在 Teams 讨论串中跟进负责人、起草并发布回复；已发布的回复对能看到讨论串的人可见（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）。TestingCatalog 转述 Omar Shahine 的推文：他用 iPhone 的 Action Button 录语音备忘，转写后发给 Teams 里的 Autopilot 记录费用（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）。新闻手册称团队「即将」可以把个人 Autopilot 带入 Copilot Workspaces（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）；Copilot 博客称 Workspaces 中 Autopilot 可领任务（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。

## 自己的名字、头像、邮箱

应用卡写明 Autopilot「有自己的名称、头像和电子邮件地址」，在 Copilot、Teams、Outlook 中与用户并列出现，让同事区分它的工作（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）；概述页称它另有自己的日历（[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})）。用户可在 Microsoft 365 个人资料的「联系人 > 助手」字段把它设为助手，由管理员控制该字段，设置本身不授予权限（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。审批卡把组织外的收件人标为「外部」（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})）。

博文作者举例：别人可以在 Teams 里和他的 Autopilot（名为 Sebastian）说话来约他的时间，它知道他的日程偏好（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）。场景页写明 Autopilot 以自己的身份发送跟进消息，收件人能看出来自谁的 Autopilot（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）。

## 两种身份按操作分工

Scout 时期官方博文说「自己的 Entra 身份」、消息中心通告说「使用用户身份」，11 月的文档把两者合在一起：FAQ 称身份与操作账户「相关但不同」，有些操作用 Autopilot 自己的身份，有些用代表用户获得的授权访问，例如用用户的权限读日历、以自己的身份与同事沟通；独立身份不意味着不受限的访问（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。管理员文档举例以自身身份发 Teams 消息，并说明执行访问由实际执行的账户、资源和策略决定（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。审计日志中两类操作分别记在 Autopilot 名下和所有者名下，见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})。

UC Today 认为 Ignite 上「每个智能体都进了 Teams」，在频道里出现已不特殊，区别在于智能体向谁负责，Autopilot 是唯一有独立目录身份和具名管理者的（[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})）。

## 更名前：Scout 的入口（2026-06 至 2026-09）

以下为 2026-11-14 分析的内容。桌面聊天界面属于 Scout 桌面应用；身份口径的分歧已由 11 月文档的「两种身份按操作分工」说明。

### 桌面应用的聊天界面

使用指南描述：富 Markdown 流式回复（表格、代码块、Mermaid、图片）；Scout 工作时可继续发消息，消息排队按序处理；需要信息时给出选项，可自由文本回答或跳过；对话与自动化在左侧导航，可筛选、固定（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。入门页提到个性预设，默认「有帮助且专业」（[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})）。社区作者称个性可从专业调到「勉强愿意帮忙」，TestingCatalog 视为轻量点缀（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})、[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})）。另有始终置顶的迷你模式（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。

### Teams 与 Outlook

发布博文称用户在 Teams 中与 Scout 交互，工作发生在 Teams、Outlook、OneDrive、SharePoint 和本机（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[Build 直播]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-build-live-scout" >}})）。Scout 能在 Teams 发消息、在频道发帖、发邮件，这些对外动作都先请求批准（[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})）。iThome 列出的入口是 Teams、Outlook 和 Microsoft 365 Copilot 界面（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。

9 月的更名文章称 Autopilot 出现在 Teams、Outlook、聊天、频道和文档中，「你可以像同事一样 @提及它」（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）；社区综述补充它有头像和用户选的名字（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

### 以谁的名义

| 说法 | 来源 |
| --- | --- |
| 每个智能体在自己受治理的 Entra 身份下运行，而非共享匿名服务账户 | [Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})；媒体转述见 [Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})、[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}}) |
| 应用在用户设备本地运行，并使用用户身份进行操作 | [消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}}) |
| 发布前原型有自己的 Entra ID、Exchange 邮箱与 Teams 在线状态 | [GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}}) |
| Autopilot 在租户内拥有自己的身份 | [新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}}) |

推断：桌面版 Scout 的 Microsoft 365 操作按文档是以用户账号进行（权限以用户为界）；「自己的 Entra 身份」更像是对智能体可归因、可治理的描述，或是云端 Autopilot 的形态。两者如何并存，资料没有说明，见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})。

### 消费级渠道

Shahine 的个人版 Lobster 有自己的 Apple ID，可从任何有 iMessage 的设备给它发消息（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})），这是个人项目，Scout 产品资料没有 iMessage 等渠道。OpenClaw 博客列出的 iMessage 批准等贡献针对 OpenClaw 本身（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。

## 资料缺口

- Teams 会议中 Autopilot 能做什么（产品页首次提到「会议」）。
- 带入 Workspaces 的上线时间。
- 外部（组织外）联系人与它往来邮件的限制。

## 主要资料

- 官方：[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})（聊天界面）；[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})（对外动作的批准）；[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})（身份说法）；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（@提及）。
- 媒体：[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})、[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})、[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})、[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
- 2026-11 新增官方：[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})（入口与移动端）；[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 审查操作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-approval" >}})（名称、邮箱、身份分工）；[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})（Teams 与邮件用例、Workspaces）。
- 2026-11 新增媒体：[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})。
- industry：[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})（Teams 中各家智能体的身份对比）。
