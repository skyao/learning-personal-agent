---
title: "推出 Microsoft Scout：你的常驻个人智能体"
linkTitle: "Scout 发布博文"
date: 2026-06-02
originalTitle: "Introducing Microsoft Scout: Your always-on personal agent"
sourceUrl: "https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/"
altUrls: ["https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout/"]
author: "Omar Shahine"
publisher: "Microsoft（Microsoft Copilot 博客）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [发布, 运行环境, 安全]
products: [microsoft-autopilot]
updatedAt: "2026-09-25"
dateNote: "页面结构化数据 dateModified 为 2026-09-25，当天页顶加了改名横幅"
---

{{< source-info >}}

**收录说明**：Microsoft Scout 的发布文章，作者 Omar Shahine 是负责 Microsoft Scout 的公司副总裁。直接下载；原 Microsoft 365 博客地址重定向到此页，记入 altUrls。页顶保留了 2026-09-25 加入的「Microsoft Scout is now Autopilot」横幅；删去了站点标志与文末标签。题图是约 1 MB 的动图，未下载，改为指向原图的链接；作者头像收入 images/。已翻译。

**内容摘要**：微软宣布一类名为 Autopilots 的新智能体：常驻后台、自主运行、拥有自己的身份并代用户行事；Microsoft Scout 是其中第一个 Autopilot 智能体。Scout 跨云、桌面和网页运行，连接 Teams、Outlook、OneDrive 和 SharePoint，用户在 Teams 中与它交互，并通过桌面应用把能力延伸到浏览器、本地资源和 MCP 服务器；它基于 OpenClaw 开源技术，由 Work IQ 提供上下文。每个智能体在自己受治理的 Entra 身份下运行，敏感操作可要求人工批准，Microsoft Purview 的敏感度标签和防泄漏策略会在发送或写入之前生效；微软还将策略合规（policy conformance）直接贡献回 OpenClaw 上游。微软员工已在使用早期桌面版，现将其以实验版形式经 Frontier 提供给 Frontier 组织和一批私有预览客户，需要 Frontier 注册、Intune 策略配置和 opt-in 声明，持 GitHub Copilot 许可证的用户可下载安装。

**保留理由**：这是 Scout 发布时的官方原始表述，其他材料大多以它为依据；它给出了 Autopilot 类别的定义、企业身份与访问控制的官方说法以及上游贡献承诺。

---

[动图：发布 Microsoft Scout](https://www.microsoft.com/en-us/copilot/blog/wp-content/uploads/sites/2/2026/06/Scout-GIF.gif)
Microsoft Scout 现已更名为 Autopilot。[了解更多](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)。

工作正以新的方式向前推进，节奏从单次交互转向更连续的状态。大多数系统仍止步于回答问题。真正的突破在于后续执行——系统掌握你的优先事项，并在你的掌控下代你采取行动。

## 一类新的智能体

今天我们推出一类新的智能体，称为 Autopilots。Autopilots 是常驻运行的智能体，自主工作，拥有自己的身份，并代你行事。

Autopilots 在后台保持活跃，了解工作如何跨你的应用和系统完成，并无需每次都被提示即可采取行动。由于它们以自己的身份运行，因此能在你和组织设定的权限与策略范围内执行任务。这创造了一种更持久的方式让工作持续进行，即使你的注意力在别处。

## 推出 Microsoft Scout

我们同时推出 Microsoft Scout，我们的第一个 Autopilot 智能体。

Microsoft Scout 集成到你每天使用的 Microsoft 365 应用中，让你始终处于工作流之中。它跨云、桌面和网页运行，连接 Teams、Outlook、OneDrive 和 SharePoint，以及支撑你日常工作的数据，包括聊天、电子邮件、日历和联系人。你在 Teams 中与它交互，并通过桌面应用把它的触达范围扩展到你的浏览器、本地资源和模型上下文协议（Model Context Protocol）服务器。

Microsoft Scout 以企业级安全与控制构建，因此从第一天起就能在你的组织中获得信任。它由 OpenClaw 开源技术驱动，体现了我们与社区共同构建的承诺，同时扩展能力以满足企业需求。

Microsoft Scout 减少一天中不断累积的协调工作。它可以主动跨时区安排和协调会议时间、标记重要会议，并生成你准备所需的材料，同时让你随时了解进展。它会识别即将到来的交付物，然后自动在你的日历上预留时间，帮助你保持进度。它还可以发现风险，例如停滞不前的决策，让你在它们成为阻碍之前加以处理。

随着时间推移，Microsoft Scout 会基于 Work IQ 构建上下文，了解你如何工作、你在意什么，以及接下来需要发生什么。Work IQ 推动工作向前，使其更有用、更相关，并与你的优先事项保持一致。

## 回馈开源社区

我们正在直接把策略合规（policy conformance）贡献回 OpenClaw 上游。

运行 OpenClaw 的组织将能够验证其环境是否在安全与合规要求范围内配置、是否安全运行，并获得可验证、可用于审计的答案。

## 让 Microsoft Scout 为企业就绪

Microsoft Scout 增加了构建于 Microsoft 365 之上的企业级解决方案：身份、凭据和访问控制，把开源能力转变为可以在整个组织中安全运行的东西。每个智能体都在自己受治理的 Entra 身份下运行，而不是共享的匿名服务账户，因此它完成的工作可归因于你的目录已认识的已知行为者。

该身份背后的凭据受到端到端保护：范围限定于当前任务，在日志或诊断中被隐去，并以你对任何 Microsoft 第一方服务所期望的同等严谨程度管理。当 Microsoft Scout 代你行事时，你确切知道它承载了谁的授权，以及过程中没有泄露任何敏感信息。

身份告诉你谁在行事；访问控制决定他们能做什么。使用 Microsoft Scout 时，智能体只能访问你已批准的资源与目标。敏感操作可要求人工在继续之前签字批准，来自 Microsoft Purview 的数据保护策略（包括敏感度标签和防泄漏）会在发送或写入任何内容之前即时执行。Microsoft Scout 不会绕过这些控制；它在这些控制内运行，遵守你的组织已配置的保护措施。

## 开始使用 Microsoft Scout

Microsoft 员工已经在使用早期版本的 Microsoft Scout 桌面体验。我们构建它是为了了解常驻智能体在真实工作中如何呈现，我们看到它承担协调工作、更早发现风险，并在无需不断提示的情况下保持工作推进。

我们现在正把这一早期体验扩展到一小批私有预览客户和 Frontier 组织。Microsoft Scout 通过 Frontier 以实验版形式提供，让客户有机会探索 Microsoft Scout 如何融入他们自己的工作流。

访问需要 Frontier 注册、Intune 策略配置和一份 opt-in 声明（attestation）。拥有 GitHub Copilot 许可证的用户随后可以下载并安装该体验。**[完整设置说明可在此获取](https://learn.microsoft.com/microsoft-scout)**。

---

Microsoft Build 汇集了我们各平台的创新，其中许多正出现在 Microsoft 365 Copilot 中：

- [推出新的 Work IQ API](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/announcing-the-new-work-iq-apis/)

- [Work IQ：面向每个智能体的生产就绪智能](https://aka.ms/WorkIQAPI_GA)

- [在工作发生的地方构建协作智能体](http://aka.ms/TeamsPlatform-Build)

- [Frontier Tuning：教 AI 按你的方式工作](https://aka.ms/frontiertuningblog)

![Omar Shahine 头像](images/omar-shahine.png)

## Omar Shahine

Microsoft Scout 公司副总裁

Omar Shahine 是 Microsoft 的公司副总裁，领导 Microsoft Scout，这项工作的重点是开发面向 Microsoft 365 的下一代常驻个人智能体。Omar 在 Microsoft 工作超过 25 年，担任过多个产品领导职务。在 Microsoft Scout 之前，他作为 Copilot 产品家族的一部分领导 Microsoft Word 团队。
