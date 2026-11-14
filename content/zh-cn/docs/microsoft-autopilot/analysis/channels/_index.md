---
title: "Microsoft Autopilot：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-10
description: >
  Scout 的主入口是桌面应用内的聊天界面，对外沟通通过用户账号在 Teams 与 Outlook 中进行；9 月的 Autopilot 改为出现在 Teams、Outlook、频道和文档中、可被 @提及 的「同事」。智能体自己的 Entra 身份与「以用户身份操作」两种说法并存。
---

## 概要

- Learn 文档中的主入口是桌面应用的聊天界面：流式回复、消息排队、给出选项供选择或自由回答。
- 发布博文与 Build 条目称用户「在 Teams 中与它交互」，对话入口是 Teams 和 Outlook。
- 9 月的 Autopilot 出现在 Teams、Outlook、聊天、频道和文档中，可像同事一样被 @提及，有名字与头像。
- 身份口径不一：官方博文称每个智能体有自己受治理的 Entra 身份；消息中心通告和文档称应用使用用户身份操作。是否有独立邮箱或号码，产品资料没有写。
- 不支持移动端，也没有短信、iMessage、WhatsApp 等消费级渠道。

## 桌面应用的聊天界面

使用指南描述：富 Markdown 流式回复（表格、代码块、Mermaid、图片）；Scout 工作时可继续发消息，消息排队按序处理；需要信息时给出选项，可自由文本回答或跳过；对话与自动化在左侧导航，可筛选、固定（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。入门页提到个性预设，默认「有帮助且专业」（[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})）。社区作者称个性可从专业调到「勉强愿意帮忙」，TestingCatalog 视为轻量点缀（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})、[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})）。另有始终置顶的迷你模式（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。

## Teams 与 Outlook

发布博文称用户在 Teams 中与 Scout 交互，工作发生在 Teams、Outlook、OneDrive、SharePoint 和本机（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[Build 直播]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-build-live-scout" >}})）。Scout 能在 Teams 发消息、在频道发帖、发邮件，这些对外动作都先请求批准（[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})）。iThome 列出的入口是 Teams、Outlook 和 Microsoft 365 Copilot 界面（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。

9 月的更名文章称 Autopilot 出现在 Teams、Outlook、聊天、频道和文档中，「你可以像同事一样 @提及它」（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）；社区综述补充它有头像和用户选的名字（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

## 以谁的名义

| 说法 | 来源 |
| --- | --- |
| 每个智能体在自己受治理的 Entra 身份下运行，而非共享匿名服务账户 | [Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})；媒体转述见 [Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})、[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}}) |
| 应用在用户设备本地运行，并使用用户身份进行操作 | [消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}}) |
| 发布前原型有自己的 Entra ID、Exchange 邮箱与 Teams 在线状态 | [GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}}) |
| Autopilot 在租户内拥有自己的身份 | [新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}}) |

推断：桌面版 Scout 的 Microsoft 365 操作按文档是以用户账号进行（权限以用户为界）；「自己的 Entra 身份」更像是对智能体可归因、可治理的描述，或是云端 Autopilot 的形态。两者如何并存，资料没有说明，见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})。

## 消费级渠道

Shahine 的个人版 Lobster 有自己的 Apple ID，可从任何有 iMessage 的设备给它发消息（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})），这是个人项目，Scout 产品资料没有 iMessage 等渠道。OpenClaw 博客列出的 iMessage 批准等贡献针对 OpenClaw 本身（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。

## 资料缺口

- Autopilot 是否有独立邮箱、Teams 账号，对外消息的署名方式。
- Teams/Outlook 内对话与桌面应用对话是否互通。

## 主要资料

- 官方：[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})（聊天界面）；[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})（对外动作的批准）；[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})（身份说法）；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（@提及）。
- 媒体：[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})、[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})、[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})、[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
