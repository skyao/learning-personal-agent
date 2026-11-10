---
title: "MC1332811：Microsoft 365 Copilot 推出常驻个人智能体 Microsoft Scout"
linkTitle: "消息中心 MC1332811"
date: 2026-06-02
originalTitle: "MC1332811 - Microsoft 365 Copilot: Introducing Microsoft Scout, an always-on personal agent"
sourceUrl: "https://admin.microsoft.com/#/MessageCenter/:/messages/MC1332811"
altUrls: ["https://m365admin.handsontek.net/microsoft-365-copilot-introducing-microsoft-scout-always-personal-agent/", "https://app.cloudscout.one/evergreen-item/mc1332811/"]
author: "未署名"
publisher: "Microsoft 365 消息中心"
language: en
fidelity: 转载全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [发布, 开放与价格, 隐私]
products: [microsoft-autopilot]
reprintUrl: "https://mc.merill.net/message/MC1332811"
updatedAt: "2026-08-21"
dateNote: "存档站显示 Published Jun 2, 2026、Last Updated Aug 21, 2026；该公告已于 2026-10-30 过期"
---

{{< source-info >}}

**收录说明**：Microsoft 365 管理中心的消息中心公告，原文需管理员登录，依据第三方存档站 mc.merill.net 的完整转录存档（另有 handsontek、cloudscout 等镜像，记入 altUrls）。删去了存档站的导航与讨论区。已翻译。

**内容摘要**：Message Center 通告 MC1332811 发布于 2026 年 6 月 2 日，最后更新为 2026 年 8 月 21 日，标签为新功能，面向管理员。通告称 Scout 是首个 Autopilot，在 Frontier 预览中面向已注册客户提供 Windows 和 macOS 桌面应用，正式可用的时间将另行通知。该功能默认关闭，需管理员启用；管理员须在 Intune 中配置策略、完成 opt-in 与声明，并确保用户有 GitHub Copilot 许可（用于 AI 额度计费），否则用户无法登录。应用在用户设备本地运行并使用用户身份；合规问答称，预览体验包含 Microsoft 365 之外的数据路径（例如基于 GitHub 的推理），因此需要管理员明确声明。

**保留理由**：这是面向租户管理员的通告，列出了启用步骤、默认关闭、受影响角色以及合规问答，说明数据流出 Microsoft 365 的管理员声明为何必需，博客类材料没有这些细节。

---

MC1332811 - Microsoft 365 Copilot：推出常驻个人智能体 Microsoft Scout

消息中心

此公告已于 **2026 年 10 月 30 日** 过期，不再在消息中心显示。

### 摘要

Microsoft Scout 是一个常驻的个人 Autopilot 智能体，集成于各 Microsoft 365 应用，在组织策略范围内自主行事。现已在 Windows 和 macOS 上以 Frontier 预览版提供，需要管理员启用、Intune 策略配置和 GitHub Copilot 许可。它遵守安全与合规护栏。

[讨论](#discussion)由 zap.ms 提供支持

[### 消息 ID

MC1332811

在消息中心查看](https://admin.microsoft.com/#/MessageCenter/:/messages/MC1332811)

### 最后更新

2026 年 8 月 21 日

发布于 2026 年 6 月 2 日

### 服务

Microsoft Copilot (Microsoft 365)

### 标签

新功能

用户影响

管理员影响

### 更多信息

****是什么以及为什么****

我们推出一类新的智能体，称为 Autopilots——常驻运行的智能体，自主工作，拥有自己的身份，并在你设定的权限与策略范围内代你行事。**Microsoft Scout** 是我们的第一个 Autopilot。它集成于你的用户每天依赖的各 Microsoft 365 应用，由 Work IQ 驱动，始终与用户的优先事项保持连接、监控重要事项，并跨 Teams、Outlook、OneDrive 和 SharePoint 推动工作向前——同时遵守你的组织所定义的安全、身份和治理护栏。

Microsoft Scout 基于 OpenClaw 开源技术和企业级控制构建，今天即可通过 Frontier 以 Windows 和 macOS 上的早期桌面体验获得——也就是 Microsoft 员工一直在使用的同一体验——让已注册的客户有机会探索 Autopilots 如何融入他们的工作流。

了解更多，请访问 [推出 Microsoft Scout：你的常驻个人智能体 | Microsoft 365 博客](https://aka.ms/microsoftscout) 和 [Microsoft Scout（Frontier）文档 | Microsoft Learn](https://aka.ms/MicrosoftScout-Learn-docs)

****推出时间表****

- **Frontier（预览版）：** 现已在 Windows 和 macOS 上面向已注册客户提供
- **正式可用（General availability）**：更大范围的推出时间将另行通知

****对你组织的影响****

*受影响对象*

- 已注册 Frontier 的组织
- 管理 Intune、身份和访问控制的 IT 管理员
- Microsoft 365 管理员
- 满足许可和管理员配置前提条件的最终用户

*平台 / 服务*

- Microsoft 365
- Microsoft Scout 桌面应用（Windows、macOS）
- Microsoft Intune（策略配置）
- GitHub Copilot（AI 额度计费所需）

*将会发生什么*

- 已注册 *Frontier* 的租户将可使用 Microsoft Scout 桌面应用。
- 该功能**默认关闭**，需要管理员启用。
- 在所有必需的管理员前提条件完成之前，用户无法登录。
- Scout 应用在用户设备本地运行，并使用用户身份进行操作。
- 访问受管理员配置、注册和声明（attestation）限制。

****所需操作 / 建议****

管理员操作（必需）

- 在 [Intune](https://intune.microsoft.com/#home) 中配置所需的设备和访问策略。
- 在启用 Microsoft Scout 之前，完成必需的管理员 opt-in 和声明（attestation）（将在设置过程中提供）。由于数据会流出 Microsoft 365，此步骤为必需。
- 确保符合条件的用户拥有相应的 [GitHub Copilot 许可](https://docs.github.com/billing/get-started/introduction-to-billing)。

用户操作

- 下载并安装 Microsoft Scout 应用（Frontier）。
- 下载 Microsoft Scout：<https://aka.ms/msscout>
- 使用工作账户登录（在管理员启用之后）。
- 使用 GitHub 账户登录。

建议

- 在启用前与安全与合规相关方一起审查此功能。
- 告知服务台团队，登录失败通常意味着缺少前提条件。
- 与试点用户分享启用指南，为 Frontier 体验设定预期。

了解更多：

- [计费与许可简介 | 入门 | 账单与付款 | GitHub 文档](https://docs.github.com/billing/get-started/introduction-to-billing)
- [推出 Microsoft Scout：你的常驻个人智能体 | Microsoft 365 博客](https://aka.ms/microsoftscout)
- [Microsoft Scout（Frontier）文档 | Microsoft Learn](https://learn.microsoft.com/microsoft-scout/)
- [第 1 步：设置 Microsoft Intune | Microsoft Intune | Microsoft Learn](https://learn.microsoft.com/intune/fundamentals/deploy-setup-step-1)

****合规考量****

|  |  |
| --- | --- |
| **问题** | **回答** |
| 该更改是否存储新的客户数据？如果是，存储在哪里，数据是缓存还是永久存储？ | 是。预览体验包含 Microsoft 365 之外的数据路径（例如基于 GitHub 的推理），这可能涉及对客户数据的额外处理，并要求管理员明确声明（attestation）。 |
| 该更改是否引入或大幅修改与客户数据交互或提供客户数据访问权限的 AI 或智能体能力？ | 是。此更改引入一种主动的智能体体验，可在既定的组织护栏内代表用户对内容和任务采取行动。 |
| 该更改是否增加与第三方软件产品的任何集成？ | 是。Microsoft Scout 需要与 GitHub Copilot 集成以进行 AI 额度消耗和计费。 |
| 该更改是否包含管理员控制，能否通过 Entra ID 组成员身份进行控制？ | 是。访问通过管理控制进行限制，包括 Intune 配置、Frontier 注册以及必需的管理员 opt-in 和声明。 |
| 该更改是否允许用户自行启用和禁用该功能？ | 是。用户可以安装该应用，但除非管理员完成必需的启用和声明步骤，否则他们无法成功使用。 |
