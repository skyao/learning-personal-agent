---
title: "Microsoft Autopilot：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 内置的连接面是 Microsoft 365（Teams、Outlook、OneDrive、SharePoint、To Do、Planner），外部扩展靠技能（SKILL.md）和插件（可含连接器），插件经 Microsoft 365 插件市场分发、由 IT 在 Agent 365 集中治理；添加技能或插件不授予额外权限。官方没有给出 Autopilot 可用的第三方插件清单。
---

## 概要

- Autopilot 的首要连接面是 Microsoft 365：通过可用工具使用用户有权访问的 Teams、Outlook、OneDrive、SharePoint；概述页另提到它有自己的邮箱和日历，可用 To Do 和 Planner 跟踪任务（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})）。
- 扩展分两种：技能（任务指令，可在对话中创建，或上传含 SKILL.md 的 ZIP/文件夹）和插件（连接工具与服务，可含技能、连接器或两者），插件经 Microsoft 365 插件市场分发（[自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}})）。
- 「添加技能或插件不会授予数据访问权限或操作权限」；技能可分享给组织内特定人员，但不分享登录、连接或权限（[自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。
- 治理集中在 IT：被策略阻止的插件标「Blocked by policy」，管理员可自动部署插件，部分插件用户不可移除；Agent 365 的插件与技能治理已正式可用（[自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。
- 资料没有列出 Autopilot 可用的第三方插件；Ignite 公布的 Dynamics 365、Salesforce 等插件与技能数是 Copilot 整体的，没有说明是否适用于 Autopilot。Scout 时期的 MCP 服务器与 shell 工具在新文档中没有出现。

## 2026-11：Microsoft 365 加技能与插件

应用卡写明 Autopilot 通过可用工具使用用户有权访问的 Teams、Outlook、OneDrive、SharePoint 信息，不扩大访问范围（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。概述页补充：Autopilot 在用户的邮箱和日历之外有自己的邮箱和日历，可把草稿共享到用户现有 OneDrive 文件夹，用 To Do 和 Planner 共享任务追踪进度（[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})）。场景页提到可请求演示文稿、电子表格或 Loop 内容，产出存 OneDrive（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）。

「自定义 Autopilot 能做什么」一页定义了扩展方式（[自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}})）：

| 类型 | 做法 |
| --- | --- |
| 技能 | 提供任务指令；在对话中创建，或上传含 SKILL.md 的 ZIP/文件夹，输入 / 调用；保存前须用户批准；提醒不要把凭据写进技能 |
| 插件 | 连接工具与服务，可含技能、连接器或两者；从目录添加，经 Microsoft 365 插件市场分发；详情显示创建者、版本、隐私政策与服务条款 |
| 首次登录 | 需要登录的插件在对话中显示连接请求，说明所需访问及原因 |
| 分享 | 技能可分享给组织内特定人员，接收者用自己的访问权限；不分享登录、连接或权限 |

文档反复强调技能和插件不授予权限：「添加技能或插件不会授予数据访问权限或操作权限」（[自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}})）；要求页称「技能与例程不会授予访问权」（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）；应用卡称目录列出不等于已安装或已许可（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

## IT 治理

被组织策略阻止的插件显示「Blocked by policy」，无法添加；由组织管理的插件，连接由管理员处理，用户无需登录或输入密钥；管理员可自动部署插件，部分插件不能移除（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}})）。新闻手册宣布 Agent 365 的「Copilot 和 Cowork 的插件与技能治理」正式可用，MCP 服务器治理（经 Azure AI Gateway 等网关）为预览（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。Copilot 博客介绍了新插件目录与统一插件注册表（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。

Ignite 公布的插件与技能数量——Dynamics 365 插件 100 多项预构建技能、Salesforce in Copilot 38 项以上销售技能，以及销售、客服、财务、法律等角色技能——是 Copilot 整体的，文中没有说 Autopilot 能否使用（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。9 月的消息中心通告称 Work IQ 新增 Dynamics 365 与 Power Platform 数据（公开预览），通过 Work IQ MCP 管理（[消息中心 MC1479277]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-mc1479277-new-copilot-autopilot" >}})）。

## 把 Autopilot 的能力给别的智能体

Tech Community 博文称微软把支撑 Autopilot 的能力开放给产品组合中其他受支持的智能体，如 Sales Development Agent 和 Copilot Studio 智能体，它们也可配备自己的邮箱地址和受保护的 Microsoft 365 资源（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）；TestingCatalog 转述相同（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）。

推断：与 Scout 时期「MCP 服务器 + shell + 浏览器」的开放做法相比，Autopilot 的扩展被收进插件市场和 IT 审批，用户侧只剩技能和已批准插件；这与它改为云端、不碰本机的形态一致。

## 更名前：Scout 的连接方式（2026-06 至 2026-09）

以下为 2026-11-14 分析的内容。Scout 的 Microsoft 365 范围、文件共享限制大体延续；MCP、shell 与组策略开关是桌面版的设计。

### Microsoft 365 范围

「与 Microsoft 365 协作」页（2026-08）列出的能力（[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})）：

| 服务 | 能力 |
| --- | --- |
| Outlook 邮件 | 读取、发送、回复、转发、整理；收件箱规则（8 月） |
| 日历 | 查看、创建、更新、找空闲时间、回复邀请；会议室预订（8 月） |
| Teams | 查看聊天、发消息、频道发帖、查看状态（7 月）；会议转录（8 月） |
| To Do | 7 月加入 |
| OneDrive / SharePoint | 浏览、读取、上传、共享；SharePoint Lists（8 月） |
| 搜索 | 人员与内容搜索 |

各项上线月份见新功能页（[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})）。所有能力以用户现有权限为界，「不会授予你的账户或组织原本不允许的访问权限」（[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})）。

文件共享只面向以自己账号登录的指定人员，可设查看/编辑与到期日，可发共享邀请；可授予、提升、检查访问，但不能移除已有访问（[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})、[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。

### MCP、浏览器与 skill

发布博文称桌面应用把触达扩展到浏览器、本地资源和 MCP 服务器（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）；Computerworld 报道 Scout 通过 MCP 与外部应用交互（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。社区实测中，Scout 遇到无法抓取的网站时发现该站暴露的 MCP 端点并接入，注册为定期来源（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。

skill 方面，内置 Word、Excel、PowerPoint、Web Artifacts Builder 与 Loop（Loop 靠浏览器控制编辑）；用户可自建，「Microsoft 不验证用户创建的自定义 skill」（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。FAQ 还列出开发者工具 git、gh、curl、PowerShell，以及覆盖 Office、PDF、代码、音视频、压缩包的可读写文件类型（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。8 月加入 GitHub Enterprise Cloud 登录（[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})）。

设置里有 Integrations 分组（7 月改版后移入 Settings），但资料没有列出其中可连接的第三方服务（[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})、[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})）。

### 管理员控制

组策略可用 `DisabledServers` 阻止特定 tool server（文档举例 filesystem、playwright、WorkIQ），用 `DisabledPermissions` 禁用 shell、write、mcp、url、custom-tool 等权限类别（[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})）。

### 9 月：插件注册表

新 Copilot 文章介绍插件注册表：把微软、合作伙伴和自定义插件汇集到统一目录，IT 可集中批准和管理，开发者发布一次即可扩展到各支持的体验；Autopilot 界面导航含「插件」（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。iThome 称 Autopilot 深度整合 Teams、Outlook、Microsoft 365，经 Microsoft IQ 了解企业知识（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。

OpenClaw 博客列出的微软上游贡献中有 Teams 表情回应修复、iMessage 批准和 Azure OpenAI 提供方支持，这些是对 OpenClaw 的贡献，不等于 Autopilot 的功能（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。发布前 GeekWire 提到 OpenClaw 已有 Teams 插件（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。

推断：Scout 的连接策略是「Microsoft 365 原生 + MCP 兜底」，没有像消费级产品那样逐个列出第三方应用；插件注册表把第三方扩展纳入 IT 审批，与它面向企业的定位一致。

## 资料缺口

- Autopilot 可用的第三方插件清单；Dynamics 365、Salesforce 插件是否适用。
- 插件市场的审核规则；Autopilot 是否支持用户自行接入 MCP 服务器。
- 授权失效（令牌过期、权限变更）时的处理。

## 主要资料

- 官方：[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})（Microsoft 365 范围与共享限制）；[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})（上线月份）；[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})（skill 与工具）；[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})（管理员控制）；[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（插件注册表）。
- 媒体：[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})、[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})（自动接入 MCP）；[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
- 2026-11 新增官方：[自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}})（技能与插件）；[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})、[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})（Microsoft 365 范围、不授权）；[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})（IT 治理、插件目录）；[消息中心 MC1479277]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-mc1479277-new-copilot-autopilot" >}})（Work IQ）；[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})（能力开放给其他智能体）。
- 2026-11 新增媒体：[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})。
