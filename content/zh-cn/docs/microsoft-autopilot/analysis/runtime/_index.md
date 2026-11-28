---
title: "Microsoft Autopilot：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，2026-11-17 起以 Frontier 预览推出的 Autopilot 是运行在微软托管云环境中的智能体，有自己的远程计算机和工作区，与用户设备分离、不能访问本地文件夹或应用，只在启用后借用户 Edge 浏览器触达已登录站点；此前 Scout 是用户 Windows/Mac 上的桌面应用，更名后的文档明确两者不同。
---

## 概要

- 2026-11-17 起的 Learn 文档把 Autopilot 写成 Microsoft Copilot 中的常驻云端智能体：有自己的身份、记忆、远程计算机和工作区，在微软管理的云环境运行，用户关掉应用、合上笔记本或关机后仍继续工作；无需在设备上安装代理（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。
- 云端计算机与本地设备分离，「无法访问本地文件夹或应用」；要求页明说不要把早期桌面预览的说明当作云端体验的设置要求。这与 Scout 桌面应用直接操作用户机器的形态相反（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）。
- 唯一触及用户设备的是 Edge 浏览器模式：组织启用后，只在所有者的私人对话中、只在相关标签页内操作已登录站点，例程不用浏览器；读到的页面内容送到云端模型处理（[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})）。
- 每人只能有一个 Autopilot，创建后自动预配 10 到 30 分钟；工作区跨会话保留上下文，任务的临时文件完成后不保留（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。
- 规格、并发、持久化之外的细节仍没有：云端计算机的配置、与 Windows 365 for Agents 或 Copilot Managed Runtime 的关系都没有文档。Scout 桌面版的形态见下文「更名前」。

## 2026-11：微软托管的云端计算机

Ignite 当天的消息中心通告把 Autopilot 定义为「常驻的、基于云的个人智能体」，有自己的账户与身份、存储和邮箱，「以及自己的远程计算机」（[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})）。FAQ 补充：Autopilot 在微软管理的云环境中运行，关闭 Copilot 应用、笔记本合上或关机后仍继续；工作区跨会话保留上下文，任务期间的临时文件完成后不保留（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。概述页写明设备关机时也能运行计划中的工作，前提是访问权限、审批和服务可用（[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})）。Tech Community 博文、TestingCatalog、Redmondmag 所引 Microsoft Mechanics 演示都用「合上笔记本也继续工作」来描述（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。

管理员文档称 Autopilot「作为 Microsoft Copilot 的一部分在云端运行」，管理员可在 Agents > Autopilot (Frontier) > Instances 查看组织内的实例（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。应用卡把 Workspace 定义为可跨会话保留上下文的云端工作环境，独立于本地设备和交付物的发布位置（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。用户在设置标签页能看到 Autopilot 的名称、外观、记忆和「计算机」（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})）。

创建流程：选名称和外观，审阅建议的起始例程，随后自动预配，需要 10 到 30 分钟，就绪时发邮件和 Teams 通知；就绪后审阅它从近期工作推断出的人员、职责和周期性承诺（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})）。每个启用的用户只能创建一个（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）。

## 本地文件与 Edge 浏览器

应用卡、要求页、FAQ 和 Edge 页都写明 Autopilot 无法访问用户设备上的本地文件夹或应用（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})）。十月新功能汇总则称它能「跨用户的本地文件和它自己的远程计算机运行」（[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})），与 11-17 之后的文档不一致。该汇总页为第 5 版（11-13 修改），资料没有说明这句是否是更名前的旧口径。

Edge 模式是唯一的本机触点（[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})）：

| 项目 | 说明 |
| --- | --- |
| 前提 | 组织启用；Edge 已打开、以工作账户登录并连接 Autopilot；逐步推出 |
| 范围 | 只限所有者的私人对话（Copilot 或一对一 Teams 聊天）；只在对话涉及的标签页内操作，看不到其他标签页 |
| 不用浏览器的情形 | 例程（定时工作）、共享对话（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}}) 同说） |
| 数据 | 密码和 cookie 留在 Edge，读到的页面内容送云端模型处理 |

Redmondmag 报道管理员可选择智能体会话「仅限于云端，还是允许在受管设备上本地运行」（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})），Learn 文档没有这一设置。要求页把「隔离执行环境 Microsoft local (MXC)」（需 Intune Plan 1 或 Microsoft 365 E3）列为必需的安全能力（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})），新闻手册与 Copilot 博客把 MXC 描述为隔离设备上本地智能体的机制（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。

推断：从 MXC 被列为必需能力和 Redmondmag 的说法看，Autopilot 可能保留了某种受管设备上的本地执行选项；但用户文档一致写「无法访问本地文件夹或应用」，两者如何对应，资料没有说明。

## 相关的托管基础设施

新闻手册宣布 Copilot Managed Runtime 正式可用，托管 Copilot Code、Cowork、Copilot Studio 中创建的应用，列举对象中没有 Autopilot；Windows 365 for Agents 将在 Frontier 支持持久云 PC，用于「始终在线的个人智能体」，也没有点名 Autopilot（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。管理员文档的导出排障提到脚本会临时修改 hosts 文件中的 `cowork.local.microsoft.com` 条目（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})）。

推断：`cowork.local` 域名提示 Autopilot 与 Cowork 可能共用部分底层服务；Managed Runtime、Windows 365 for Agents 是否就是 Autopilot 的「远程计算机」，资料没有说明，不能据此认定。

## 更名前：Scout 桌面应用（2026-06 至 2026-09）

以下为 2026-11-14 分析的内容，描述 Scout 时期的 Learn 文档与报道。要求页称不应把早期桌面预览的说明当作云端体验的要求（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})），桌面应用是否仍在提供，资料没有说明。

### 桌面应用：用户的机器、用户的身份

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

### 托管设备上的部署细节

受管环境排障文档透露了桌面应用的构成（[托管设备排障]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-01-scout-managed-troubleshoot" >}})）：Scout 应用之外捆绑 GitHub Copilot 组件 `copilot.exe`，AppLocker/WDAC 还需放行 `node-runner.exe`、`node.exe`，可选 `workiq.exe`；数据和日志目录是 `~/.copilot`；渲染器日志靠 `ELECTRON_ENABLE_LOGGING=1` 打开。Copilot 组件连 `githubcopilot.com`，对它做 TLS 检查会导致登录失败；应用必须以正常登录用户运行，不能以 SYSTEM 运行；VDI 中需加 `--disable-gpu`，非持久 VDI 每次会话丢失登录状态。文档列出的多项「变通办法」称未来版本会自动处理。预发布界面仍显示内部名 Clawpilot（协议 `ms-clawpilot://`）。

推断：从 `copilot.exe` 与 Electron 日志开关看，桌面版 Scout 可能是 Electron 外壳加 GitHub Copilot 的智能体组件，模型调用因此经 GitHub 处理（见[模型]({{< relref "/docs/microsoft-autopilot/analysis/models" >}})、[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})）。

组织可用 Intune 策略把文件系统和 shell 限制在工作区（`RestrictToWorkspace`）、阻止浏览器访问指定来源（[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})）。

### 企业化：容器不受信任

Command Line 对谈中，官方称智能体容器被视为不受信任，每次工具调用、模型请求和网络跳转都由零信任运行时中介，身份、令牌和策略由微软控制并放在容器之外；所有软件包经过策管、签名的微软供应链引入（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。OpenClaw 博客列出的上游贡献中有 MXC 沙箱后端，用 Microsoft 执行容器技术约束 Windows 上的智能体命令执行（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。

### 6 月说「跨云、桌面和网页」，9 月说「自己的计算机」

发布博文称 Scout「跨云、桌面和网页运行」，通过桌面应用把触达扩展到浏览器、本地资源和 MCP 服务器（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）；Computerworld 照此报道（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。同期的 Learn 文档只写桌面应用。社区作者 6 月称云端版仍是有限访问，可不依赖设备完全自主运行（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。

2026-09-25 的更名文章写 Autopilot 由云端托管，在租户内拥有自己的身份、记忆、计算机和工作区，用户睡觉时仍在工作（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。同文介绍的 Microsoft Copilot Managed Runtime 是「让代码在你公司的 Microsoft 365 环境内安全运行的托管基础设施」，支撑 Cowork、Code 等，文中没有说它与 Autopilot 的关系。iThome 的比较表采用云端说法（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。社区作者指出更名不只是改名：Scout 是桌面应用，Autopilot 是云端托管，桌面应用是否保留没有文档说明（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})、[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。

推断：9 月之后的 Autopilot 很可能从「用户机器上的桌面应用」转向「租户内托管的云端计算机」，这与 6 月社区作者所说的「云端版」衔接；但截至 11-10 资料库里没有云端版的文档，规格、持久化、并发等都无从判断。

### 与 OpenClaw 的关系

发布前，ClawPilot 是基于 OpenClaw 的桌面环境（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）；6 月的官方对谈与博文都把 Scout 写成 OpenClaw 之上加企业身份、治理和安全（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})、[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）。9 月 OpenClaw 博客称 Autopilot 的基础是 OpenClaw，并列出可靠性类上游修复（排队的用户请求优先于后台任务、修复可能挂起 Gateway 的调度器等）（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。社区作者指出微软 9 月文章和 Learn 文档完全没提 OpenClaw，这一说法是单方面的（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

## 资料缺口

- 云端计算机的规格、持久化、休眠与回收、并发上限、超时；它是否基于 Windows 365 for Agents 或 Copilot Managed Runtime。
- MXC 在 Autopilot 中隔离的是什么；Redmondmag 所说「受管设备本地运行」的设置是否存在。
- 十月汇总「跨本地文件运行」与 11 月文档「无法访问本地文件夹」的关系。
- Scout 桌面应用在 Autopilot 推出后是否继续提供、是否迁移。
- 云端算力如何计入 Copilot Credits。

## 主要资料

- 官方：[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})（本地运行、用户身份）；[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[Scout 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-overview" >}})（桌面能力）；[托管设备排障]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-01-scout-managed-troubleshoot" >}})（部署构成）；[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})（零信任运行时）；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（云端托管说法）。
- 媒体：[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})、[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})、[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})（桌面版与云端版的区别）；[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})（上游贡献）；[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})（更名前后形态的差异）。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
- 2026-11 新增官方：[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})（云端计算机、无本地访问）；[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})（浏览器模式）；[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})（创建与预配）；[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})（「跨本地文件」的旧说法）；[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})（MXC、Managed Runtime、Windows 365 for Agents）；[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})。
- 2026-11 新增媒体：[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})（本地运行设置的说法）。
