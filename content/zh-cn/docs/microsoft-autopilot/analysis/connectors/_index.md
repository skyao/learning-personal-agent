---
title: "Microsoft Autopilot：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 内置的连接面是 Microsoft 365（Teams、Outlook、OneDrive、SharePoint，另有自己的邮箱、日历，可用 To Do 和 Planner），外部扩展靠技能（SKILL.md）和插件（可含连接器），插件经 Microsoft 365 插件市场分发、由 IT 集中治理；添加技能或插件不授予额外权限。官方没有给出 Autopilot 可用的第三方插件清单。
---

## 概要

- 首要连接面是 Microsoft 365：通过可用工具使用用户有权访问的 Teams、Outlook、OneDrive、SharePoint；Autopilot 另有自己的邮箱和日历，可用 To Do 和 Planner 跟踪任务。
- 扩展分两种：技能（任务指令，可在对话中创建或上传含 SKILL.md 的文件夹）和插件（连接工具与服务，可含技能、连接器或两者），插件经 Microsoft 365 插件市场分发。
- 「添加技能或插件不会授予数据访问权限或操作权限」；技能可分享给组织内的人，但不分享登录、连接或权限。
- 治理集中在 IT：被策略阻止的插件标「Blocked by policy」，管理员可自动部署插件；Agent 365 的插件与技能治理已正式可用。
- 资料没有列出 Autopilot 可用的第三方插件；Ignite 公布的 Dynamics 365、Salesforce 等插件与技能数是 Copilot 整体的。

## Microsoft 365 范围

应用卡写明 Autopilot 通过可用工具使用用户有权访问的 Teams、Outlook、OneDrive、SharePoint 信息，不扩大访问范围（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。概述页补充：Autopilot 在用户的邮箱和日历之外有自己的邮箱和日历，可把草稿共享到用户现有 OneDrive 文件夹，用 To Do 和 Planner 共享任务追踪进度（[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})）。场景页提到可请求演示文稿、电子表格或 Loop 内容，产出存 OneDrive（[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})）。FAQ 称它可处理已授权的 Teams、邮件、日历和 OneDrive/SharePoint 文件（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。

9 月的消息中心通告称 Work IQ 新增 Dynamics 365 Sales、Customer Service 和 Power Platform 数据（公开预览），管理员经 Agents > Tools 下的 Work IQ MCP 管理访问（[消息中心 MC1479277]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-mc1479277-new-copilot-autopilot" >}})）；资料没有说 Autopilot 是否使用这些数据。

## 技能与插件

「自定义 Autopilot 能做什么」一页的定义（[自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}})）：

| 类型 | 做法 |
| --- | --- |
| 技能 | 提供任务指令；在对话中创建，或上传含 SKILL.md 的 ZIP/文件夹，输入 / 调用；保存前须用户批准；提醒不要把凭据写进技能 |
| 插件 | 连接工具与服务，可含技能、连接器或两者；从目录添加，经 Microsoft 365 插件市场分发；详情显示创建者、版本、隐私政策与服务条款 |
| 首次登录 | 需要登录的插件在对话中显示连接请求，说明所需访问及原因 |
| 分享 | 技能可分享给组织内特定人员，接收者用自己的访问权限；不分享登录、连接或权限 |

文档反复强调技能和插件不授予权限：「添加技能或插件不会授予数据访问权限或操作权限」（[自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}})）；「技能与例程不会授予访问权」（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）；目录中列出不等于已安装或已许可（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。Redmondmag 称它可用 IT 批准的插件扩展能力（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。

## IT 治理

被组织策略阻止的插件显示「Blocked by policy」，无法添加；由组织管理的插件，连接由管理员处理，用户无需登录或输入密钥；管理员可自动部署插件，部分插件用户不能移除（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}})）。新闻手册宣布 Agent 365 的「Copilot 和 Cowork 的插件与技能治理」正式可用，MCP 服务器治理（经 Azure AI Gateway 等网关）为预览（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。插件注册表在 9 月更名时已宣布，汇集微软、合作伙伴和自定义插件，由 IT 集中批准（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）；Ignite 上推出新的插件目录（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。

Ignite 公布的插件与技能数量——Dynamics 365 插件 100 多项预构建技能、Salesforce in Copilot 38 项以上销售技能，以及销售、客服、财务、法律等角色技能——是 Copilot 整体的，没有说 Autopilot 能否使用（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。

## 把 Autopilot 的能力给其他智能体

Tech Community 博文称微软把支撑 Autopilot 的能力开放给产品组合中其他受支持的智能体，如 Sales Development Agent 和 Copilot Studio 智能体，它们也可配备自己的邮箱地址和受保护的 Microsoft 365 资源（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）；TestingCatalog 转述相同（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）。

推断：Autopilot 的扩展被收进插件市场和 IT 审批，用户侧只有技能和已批准的插件；文档没有提用户自行接入 MCP 服务器、shell 或开发者工具（这些曾出现在 Scout 桌面预览中，见 [Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})），与它改为云端、不碰本机的形态一致。

## 资料缺口

- Autopilot 可用的第三方插件清单；Dynamics 365、Salesforce 插件是否适用。
- 插件市场的审核规则；是否支持用户自行接入 MCP 服务器。
- 授权失效（令牌过期、权限变更）时的处理。

## 主要资料

- 官方：[自定义 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-20-autopilot-plugins" >}})（技能与插件）；[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})、[Autopilot 场景]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-scenarios" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})（Microsoft 365 范围、不授权）；[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（IT 治理、插件目录）；[消息中心 MC1479277]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-mc1479277-new-copilot-autopilot" >}})（Work IQ）；[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})（能力开放给其他智能体）；[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})。
- 媒体：[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})。
