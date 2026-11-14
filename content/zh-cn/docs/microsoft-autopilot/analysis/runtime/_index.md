---
title: "Microsoft Autopilot：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-10
description: >
  截至 2026-11-10 的资料，产品文档描述的 Scout 是运行在用户 Windows 或 Mac 上的桌面应用，以用户身份读写工作区、跑 shell、控制浏览器；2026-09-25 更名 Autopilot 时官方改称它在租户内拥有自己的计算机，但云端形态没有文档。
---

## 概要

- Learn 文档（2026-08 版）中的 Scout 是 Windows 11 / macOS 12 以上的桌面应用，在用户设备本地运行、使用用户身份，能读写工作区目录、执行 shell 命令、控制浏览器、调用 Microsoft 365 数据；不支持移动设备。
- 2026-09-25 的更名文章改称 Autopilot 由云端托管，在租户内「拥有自己的身份、记忆、计算机和工作区」。桌面应用在新名字下是否保留、云端环境的规格，资料都没有说明。
- 发布时官方称 Scout「跨云、桌面和网页运行」，但当时的文档只描述桌面应用；社区作者称 6 月的云端版仍是有限访问。
- 企业化层面，官方称智能体容器被视为不受信任，每次工具调用、模型请求和网络跳转由零信任运行时中介，软件包经签名的微软供应链引入。
- 底层是开源 OpenClaw，这一点只有 OpenClaw 博客和微软 6 月的文章明说，9 月文章与 Learn 文档没有提。

## 桌面应用：用户的机器、用户的身份

消息中心通告写明 Scout 应用「在用户设备本地运行，并使用用户身份进行操作」（[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})）。概览与入门页给出平台要求：Windows 11 或 macOS 12（Monterey）及以上，Windows 还需 Visual C++ 可再发行组件（[Scout 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-overview" >}})、[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})）。FAQ 用一张表对照 Copilot Chat 与 Scout：前者在云端，没有本地文件、shell、浏览器和自主模式；后者是桌面应用，有完整的工作区访问、三级权限的 shell、浏览器自动化、Heartbeat 和自动化。它不支持移动设备，理由是需要本地文件系统、shell 和浏览器控制（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。

环境里有什么，使用指南写得比较完整（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）：

| 能力 | 说明 |
| --- | --- |
| 工作区目录 | 首次登录时设定，默认只在其中读写；7 月起首次访问工作区外的文件夹（如下载、文档）会请求授权，批准一次后续可用（[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})） |
| shell | 在用户机器上执行命令，分自动批准、提示、拒绝三级（见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})） |
| 浏览器 | 导航、点击、填表、上传、截图、读控制台日志与网络请求；捆绑的 Loop skill 用浏览器控制编辑 Loop 文档 |
| 子 agent | Explore、Task、Code review、Research、General-purpose 五类，后台运行，完成后并回对话 |
| skill | 捆绑、工作区（云同步跨设备）、全局用户三层，自定义 skill 是带 SKILL.md 的文件夹 |
| Co-Create 工作区 | 可存本地，8 月起也可由 OneDrive 或 SharePoint 作后端；人与智能体同时编辑时自动合并 |

TestingCatalog 另提到无头浏览器模式，让部分任务在后台更快执行（[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})）。社区作者称 Scout 缺少能力时会自己写 Python 或 HTML 工具（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。

连接中断时进行中的工作暂停，恢复后自动继续（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。社区实测称桌面版要求机器保持运行，设备休眠时自动化暂停（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。

## 托管设备上的部署细节

受管环境排障文档透露了桌面应用的构成（[托管设备排障]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-01-scout-managed-troubleshoot" >}})）：Scout 应用之外捆绑 GitHub Copilot 组件 `copilot.exe`，AppLocker/WDAC 还需放行 `node-runner.exe`、`node.exe`，可选 `workiq.exe`；数据和日志目录是 `~/.copilot`；渲染器日志靠 `ELECTRON_ENABLE_LOGGING=1` 打开。Copilot 组件连 `githubcopilot.com`，对它做 TLS 检查会导致登录失败；应用必须以正常登录用户运行，不能以 SYSTEM 运行；VDI 中需加 `--disable-gpu`，非持久 VDI 每次会话丢失登录状态。文档列出的多项「变通办法」称未来版本会自动处理。预发布界面仍显示内部名 Clawpilot（协议 `ms-clawpilot://`）。

推断：从 `copilot.exe` 与 Electron 日志开关看，桌面版 Scout 可能是 Electron 外壳加 GitHub Copilot 的智能体组件，模型调用因此经 GitHub 处理（见[模型]({{< relref "/docs/microsoft-autopilot/analysis/models" >}})、[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})）。

组织可用 Intune 策略把文件系统和 shell 限制在工作区（`RestrictToWorkspace`）、阻止浏览器访问指定来源（[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})）。

## 企业化：容器不受信任

Command Line 对谈中，官方称智能体容器被视为不受信任，每次工具调用、模型请求和网络跳转都由零信任运行时中介，身份、令牌和策略由微软控制并放在容器之外；所有软件包经过策管、签名的微软供应链引入（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。OpenClaw 博客列出的上游贡献中有 MXC 沙箱后端，用 Microsoft 执行容器技术约束 Windows 上的智能体命令执行（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。

## 6 月说「跨云、桌面和网页」，9 月说「自己的计算机」

发布博文称 Scout「跨云、桌面和网页运行」，通过桌面应用把触达扩展到浏览器、本地资源和 MCP 服务器（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）；Computerworld 照此报道（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。同期的 Learn 文档只写桌面应用。社区作者 6 月称云端版仍是有限访问，可不依赖设备完全自主运行（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。

2026-09-25 的更名文章写 Autopilot 由云端托管，在租户内拥有自己的身份、记忆、计算机和工作区，用户睡觉时仍在工作（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。同文介绍的 Microsoft Copilot Managed Runtime 是「让代码在你公司的 Microsoft 365 环境内安全运行的托管基础设施」，支撑 Cowork、Code 等，文中没有说它与 Autopilot 的关系。iThome 的比较表采用云端说法（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。社区作者指出更名不只是改名：Scout 是桌面应用，Autopilot 是云端托管，桌面应用是否保留没有文档说明（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})、[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。

推断：9 月之后的 Autopilot 很可能从「用户机器上的桌面应用」转向「租户内托管的云端计算机」，这与 6 月社区作者所说的「云端版」衔接；但截至 11-10 资料库里没有云端版的文档，规格、持久化、并发等都无从判断。

## 与 OpenClaw 的关系

发布前，ClawPilot 是基于 OpenClaw 的桌面环境（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）；6 月的官方对谈与博文都把 Scout 写成 OpenClaw 之上加企业身份、治理和安全（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})、[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）。9 月 OpenClaw 博客称 Autopilot 的基础是 OpenClaw，并列出可靠性类上游修复（排队的用户请求优先于后台任务、修复可能挂起 Gateway 的调度器等）（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。社区作者指出微软 9 月文章和 Learn 文档完全没提 OpenClaw，这一说法是单方面的（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

## 资料缺口

- Autopilot 云端计算机的规格、持久化、休眠与回收、并发上限、超时；Managed Runtime 是否就是它的运行环境。
- 桌面应用在更名后是否继续提供，与云端版如何分工。
- 运行环境的算力额度如何计入按用量计费。

## 主要资料

- 官方：[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})（本地运行、用户身份）；[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[Scout 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-overview" >}})（桌面能力）；[托管设备排障]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-01-scout-managed-troubleshoot" >}})（部署构成）；[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})（零信任运行时）；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（云端托管说法）。
- 媒体：[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})、[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})、[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})（桌面版与云端版的区别）；[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})（上游贡献）；[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})（更名前后形态的差异）。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
