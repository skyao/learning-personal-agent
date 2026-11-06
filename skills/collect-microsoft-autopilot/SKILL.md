---
name: collect-microsoft-autopilot
description: 收集 Microsoft Autopilot（原 Microsoft Scout，微软）的资料时使用：Microsoft Autopilot 的官方渠道、抓取方法、收录范围与已知问题。与 collect-sources 配合使用，通用流程与页面规则见 collect-sources。
---

# 收集 Microsoft Autopilot 资料

通用流程、页面模板与翻译规则见 `skills/collect-sources/SKILL.md`。本文件只记录 Microsoft Autopilot 特有的内容；与通用规则冲突时，以本文件为准。

## 状态

| 项目 | 值 |
| --- | --- |
| 产品目录 | `content/zh-cn/docs/microsoft-autopilot/`（尚未建立，第一轮收集时按 section-templates.md 建） |
| 时间线 | 2026-06-02 Build 2026 以 Microsoft Scout 之名发布，是微软首个「Autopilot」类智能体，经 Frontier 计划实验性提供；2026-09-25 微软博客称其为 Autopilot（formerly Scout），同月底扩大私有预览 |
| 最后收集日期 | —（2026-11-06 用户同意纳入，尚未收集） |

## 背景

- 面向 Microsoft 365 企业用户的常驻个人智能体，运行在企业租户内，由 IT 管理；没有面向消费者的版本。
- 基于开源的 OpenClaw，上下文来自 Work IQ（后称 Microsoft IQ）；覆盖 Teams、Outlook、OneDrive、SharePoint，桌面应用（Windows、macOS）可访问浏览器、本地文件与 MCP 服务器。
- 每个智能体有独立的 Entra 身份；凭证按任务限定并在日志中脱敏；敏感操作可要求人工签核；Purview 敏感度标签与数据防泄漏在发送或写入前生效。
- 开通条件：加入 Frontier、配置 Intune 策略、签署 opt-in 声明，有 GitHub Copilot 许可证的用户才能安装。按用量计费（usage-based billing），具体价格未公布（2026-11-06）。

## 收录范围

- 收：Autopilot / Scout 的官方博客、Microsoft Learn 文档、Microsoft 365 消息中心公告（如 MC1332811）、Tech Community 官方帖，以及专门写它的报道和实测。
- 2026-09-25 的博客同时介绍新版 Copilot 的 Home、Code 等功能，收录时按全文存档，摘要只写 Autopilot 相关部分。
- 只讲 Microsoft 365 Copilot、Copilot Cowork 等其他功能、未涉及 Autopilot 的资料不收。
- **Windows Autopilot**（设备部署服务）与本产品无关，一律不收。

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| Microsoft Copilot 博客 | `microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/` | 发布文章，页顶有改名横幅 | 2026-11-06 用 WebFetch 可读，下载方法待第一轮确认 |
| The Official Microsoft Blog | `blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/` | 改名后的介绍与私有预览扩大 | 同上 |
| Microsoft Learn | `learn.microsoft.com/en-us/microsoft-scout/`（如 `use-microsoft-scout`） | 产品文档 | 待确认；Learn 文档一般可直接下载，并有 GitHub 源 |
| Microsoft 365 消息中心 | MC1332811「Introducing Microsoft Scout, an always-on personal agent」 | 管理员公告 | 需要登录；只能经第三方镜像（m365admin.handsontek.net、cloudscout.one 等）读取，第一轮判断是否收 |
| Tech Community | `techcommunity.microsoft.com`（Microsoft 365 Copilot 讨论区、Partner News 博客） | 官方帖与合作伙伴文章 | 待确认 |
| Build 2026 | `news.microsoft.com/build-2026-live-blog/` | 发布现场 | 待确认是否有 Scout 相关段落；视频只在有文字稿时收 |

## 媒体与社区检索

- 英文检索词：`Microsoft Autopilot agent`、`Microsoft Scout agent`、`Microsoft 365 Autopilot always-on agent`、`Scout OpenClaw Microsoft`
- 中文检索词：`微软 Scout 智能体`、`微软 Autopilot 智能体`、`Microsoft Scout 个人智能体`
- 「Autopilot」「Scout」都是常见词，检索时要带 Microsoft 和 agent，并排除 Windows Autopilot。
- 检索结果中有大量咨询公司与合作伙伴博客（bismart、powerapps911、innfactory、digitalapplied、robquickenden 等），第一轮逐个判断，只转述官方内容的不收。

## 已知问题

- 改名：2026-06 的资料称 Scout，2026-09 起称 Autopilot。资料页标题按原文，摘要中注明是同一产品。

## 命名约定

- 目录名用 `microsoft-autopilot`，不用 `autopilot`，避免与 Windows Autopilot 混淆。
