---
title: "Microsoft Scout：基于 OpenClaw 的全新常驻工作个人智能体（Build 直播条目）"
linkTitle: "Build 直播条目"
date: 2026-06-02
originalTitle: "Microsoft Scout, the new always-on personal agent for work built on OpenClaw"
sourceUrl: "https://news.microsoft.com/build-2026-live-blog/live-entry/microsoft-build-2026-live/microsoft-scout-the-new-always-on-personal-agent-for-work-built-on-openclaw/"
author: "Nick（条目署名）"
publisher: "Microsoft（Build 2026 直播博客）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [发布, 持续执行]
products: [microsoft-autopilot]
dateNote: "日期取条目数据中的发布时间 2026-06-02T11:17:16（PDT）"
---

{{< source-info >}}

**收录说明**：Microsoft Build 2026 直播博客中关于 Scout 的条目，文末署名「Nick」，未写全名。条目页直接访问返回 404，正文取自直播页 news.microsoft.com/build-2026-live-blog/ 内嵌的条目数据（WordPress 接口格式），抽取为 Markdown。已翻译。

**内容摘要**：Build 2026 直播博客条目介绍 Autopilot：常驻后台、自主运行、拥有自己的身份。Microsoft Scout 是微软的首个 Autopilot 智能体，采用企业级安全，由开源 OpenClaw 技术驱动，以 Work IQ 为上下文引擎，工作入口为 Teams 和 Outlook（对话）、OneDrive 和 SharePoint（文件）以及本机上的设备本地操作。每个智能体在自己受治理的 Entra 身份下运行；管理员将能设置策略规则，用户可以看到智能体在后台做什么。署名作者称自己在发布前测试了数周早期本地版本，例如让它每天早上监控一个 GitHub 讨论、找出各 Microsoft 365 应用的功能负责人并开启 Teams 聊天跟进状态，也让它设置 Build 之后一周的外出回复，它自行推算日期、检查日历冲突并创建了时间块。Scout 通过 Frontier 以早期实验版提供，需要 Frontier 注册、Intune 策略配置和 opt-in 声明。

**保留理由**：条目里有发布方一线人员在发布前数周的实际使用叙述，给出了两个具体的日常用例，补充了官方产品描述中缺少的使用场景。

---

## 基于 OpenClaw 打造的全新常驻工作个人智能体 Microsoft Scout

今天我们所称的「AI at work」大多仍在等待提示。借助 Autopilot 智能体，这项工作正变得更连续。Autopilots 是常驻运行的智能体，以自己的身份自主工作，代你行事。它们在后台保持活跃，了解工作如何跨你的应用和系统完成，并无需每次都被提示即可采取行动。

**Microsoft Scout** 是 Microsoft 的第一个 Autopilot 智能体。它以企业级安全构建，由开源 OpenClaw 技术驱动，以 Work IQ 作为其上下文引擎。它存在于工作已经发生的地方：用于对话的 Teams 和 Outlook、用于文件的 OneDrive 和 SharePoint，以及你机器上的设备本地操作。

Microsoft Scout 的信任层是内建的，而不是外挂的。每个智能体都在自己受治理的 Entra 身份下运行，而不是共享的匿名服务账户，因此它完成的工作始终可归因于你的目录已认识的已知行为者。管理员将能够设置策略规则，你可以在工作推进时看到智能体在后台做什么。

在今天之前，我已经测试了数周 Microsoft Scout 的早期本地版本。我最喜欢的事情之一：我让它每天早上监控一个 GitHub 讨论，在各 Microsoft 365 应用中找出正确的功能负责人，并开启 Teams 聊天跟踪状态——我一根手指都不用动。而在数周「tokenmaxxing」把所有那些公告准备好之后，我需要休息一下——所以我让 Microsoft Scout 设置我在 Build 之后那一周的外出回复。它算出了日期，检查了日历冲突并创建了时间块。Work IQ 正是让它有用而不嘈杂的原因——它学习你所特有的工作方式中的人、文件和模式。

Microsoft Scout 通过早期实验版向 Frontier 组织提供，让客户有机会探索 Autopilots 如何融入他们自己的工作流。访问需要 Frontier 注册、Intune 策略配置和一份 opt-in 声明（attestation）。拥有 GitHub Copilot 账户/许可证的用户随后可以下载并安装该体验。

*——Nick*

[阅读关于此消息的更多内容](https://aka.ms/ProjectLobster-Blog)
