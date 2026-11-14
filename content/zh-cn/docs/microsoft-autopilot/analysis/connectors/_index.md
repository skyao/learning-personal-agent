---
title: "Microsoft Autopilot：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-10
description: >
  Scout 的连接以 Microsoft 365 为主（Outlook、Teams、OneDrive/SharePoint、To Do），外部服务靠 MCP 服务器、浏览器操作和自定义 skill；官方没有给出第三方连接器清单，9 月的 Copilot 改为统一的插件注册表。
---

## 概要

- Microsoft 365 是核心：邮件、日历、Teams、To Do、文件、SharePoint Lists、会议转录、会议室、收件箱规则，7、8 月陆续扩充。
- 外部服务靠三条路：MCP 服务器、浏览器自动化、用户自建的 skill（SKILL.md）；微软不验证用户自建的 skill。
- 文件共享有硬性限制：只共享给登录的指定人员，不建匿名或公开链接，不能移除已有访问权限。
- 管理员可阻止指定的 tool server，禁用 MCP、shell 等权限类别。
- 9 月的新 Copilot 引入插件注册表，汇集微软、合作伙伴和自定义插件，由 IT 集中批准；Autopilot 界面有「插件」入口。

## Microsoft 365 范围

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

## MCP、浏览器与 skill

发布博文称桌面应用把触达扩展到浏览器、本地资源和 MCP 服务器（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）；Computerworld 报道 Scout 通过 MCP 与外部应用交互（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。社区实测中，Scout 遇到无法抓取的网站时发现该站暴露的 MCP 端点并接入，注册为定期来源（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。

skill 方面，内置 Word、Excel、PowerPoint、Web Artifacts Builder 与 Loop（Loop 靠浏览器控制编辑）；用户可自建，「Microsoft 不验证用户创建的自定义 skill」（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。FAQ 还列出开发者工具 git、gh、curl、PowerShell，以及覆盖 Office、PDF、代码、音视频、压缩包的可读写文件类型（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。8 月加入 GitHub Enterprise Cloud 登录（[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})）。

设置里有 Integrations 分组（7 月改版后移入 Settings），但资料没有列出其中可连接的第三方服务（[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})、[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})）。

## 管理员控制

组策略可用 `DisabledServers` 阻止特定 tool server（文档举例 filesystem、playwright、WorkIQ），用 `DisabledPermissions` 禁用 shell、write、mcp、url、custom-tool 等权限类别（[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})）。

## 9 月：插件注册表

新 Copilot 文章介绍插件注册表：把微软、合作伙伴和自定义插件汇集到统一目录，IT 可集中批准和管理，开发者发布一次即可扩展到各支持的体验；Autopilot 界面导航含「插件」（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。iThome 称 Autopilot 深度整合 Teams、Outlook、Microsoft 365，经 Microsoft IQ 了解企业知识（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。

OpenClaw 博客列出的微软上游贡献中有 Teams 表情回应修复、iMessage 批准和 Azure OpenAI 提供方支持，这些是对 OpenClaw 的贡献，不等于 Autopilot 的功能（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。发布前 GeekWire 提到 OpenClaw 已有 Teams 插件（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。

推断：Scout 的连接策略是「Microsoft 365 原生 + MCP 兜底」，没有像消费级产品那样逐个列出第三方应用；插件注册表把第三方扩展纳入 IT 审批，与它面向企业的定位一致。

## 资料缺口

- Integrations 中实际可用的第三方服务清单。
- 插件注册表的开放时间、审核规则，与 MCP 服务器的关系。
- 授权失效（令牌过期、权限变更）时的处理。

## 主要资料

- 官方：[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})（Microsoft 365 范围与共享限制）；[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})（上线月份）；[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})（skill 与工具）；[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})（管理员控制）；[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（插件注册表）。
- 媒体：[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})、[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})（自动接入 MCP）；[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
