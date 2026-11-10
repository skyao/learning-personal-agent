---
name: collect-microsoft-autopilot
description: 收集 Microsoft Autopilot（原 Microsoft Scout，微软）的资料时使用：Microsoft Autopilot 的官方渠道、抓取方法、收录范围与已知问题。与 collect-sources 配合使用，通用流程与页面规则见 collect-sources。
---

# 收集 Microsoft Autopilot 资料

通用流程、页面模板与翻译规则见 `skills/collect-sources/SKILL.md`。本文件只记录 Microsoft Autopilot 特有的内容；与通用规则冲突时，以本文件为准。

## 状态

| 项目 | 值 |
| --- | --- |
| 产品目录 | `content/zh-cn/docs/microsoft-autopilot/`（2026-11-10 建立） |
| 时间线 | 2026-06-02 Build 2026 以 Microsoft Scout 之名发布，是微软首个「Autopilot」类智能体，经 Frontier 计划实验性提供；2026-09-25 微软博客称其为 Autopilot（formerly Scout），同月底扩大私有预览 |
| 最后收集日期 | 2026-11-10（增量复查：无新资料；Ignite 2026-11-17 至 20 举行，下一轮重点看 Autopilot 公告）；2026-11-10（美东；第一轮：官方 17 篇、媒体 6 篇、社区 4 篇；Learn 文档 12 篇全收，旧笔记 learning-ai-agent 的 copilot-autopilot 引用来源已逐条对照） |

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
| Microsoft Copilot 博客 | `microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/` | 发布文章，页顶有改名横幅 | curl 加浏览器标识可直接下载；`microsoft-365/blog/2026/06/02/introducing-microsoft-scout/` 重定向到此（记 altUrls）。博客图片对 curl 返回 403，要带浏览器标识单独下载；题图是约 1 MB 的动图，改为链接 |
| The Official Microsoft Blog | `blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/` | 改名后的介绍与私有预览扩大 | 直接下载；`extract.py` 把内嵌视频抽成「YouTube Video」，按 HTML 中 `youtube-nocookie.com/embed/<id>` 的顺序换成占位行。微软亚洲新闻中心 2026-09-29 的简体中文版是同文译本，记 altUrls |
| Microsoft Learn | `learn.microsoft.com/en-us/microsoft-scout/`（目录见 `toc.json`） | 产品文档，12 篇（另有一个只有链接的首页，不收） | 直接下载；`extract.py <html> main`，从 `# 标题` 起到 `## Feedback` 前止。日期取 `updated_at`（页面显示的 Last updated），`ms.date` 写进 dateNote。源仓库 `MicrosoftDocs/microsoft-scout-pr` 是私有仓库，读不到。增量收集时比对 toc.json 与各页 `updated_at`，有更新按「原文更新」覆盖 |
| Microsoft 365 消息中心 | MC1332811「Introducing Microsoft Scout, an always-on personal agent」 | 管理员公告 | 需要登录；已依据 `mc.merill.net/message/MC1332811` 收为「转载全文」（handsontek 返回 Cloudflare 验证页）。该公告 2026-10-30 过期。以后的新 MC 公告同样到 mc.merill.net 按编号查 |
| Tech Community | `techcommunity.microsoft.com`（Microsoft 365 Copilot 讨论区、Partner News 博客） | 官方帖与合作伙伴文章 | 待确认 |
| Build 2026 | `news.microsoft.com/build-2026-live-blog/` | 发布现场 | 有一条 Scout 条目（已收）。条目页直接访问返回 404，正文在直播页 HTML 内嵌的 WordPress 条目 JSON 里（按 `link` 定位，`content.rendered`） |
| Command Line | `commandline.microsoft.com` | 微软官方的人物与工程故事博客 | 直接下载；Project Lobster 一文已收（aka.ms/ProjectLobster-Blog） |

## 媒体与社区检索

- 英文检索词：`Microsoft Autopilot agent`、`Microsoft Scout agent`、`Microsoft 365 Autopilot always-on agent`、`Scout OpenClaw Microsoft`
- 中文检索词：`微软 Scout 智能体`、`微软 Autopilot 智能体`、`Microsoft Scout 个人智能体`
- 「Autopilot」「Scout」都是常见词，检索时要带 Microsoft 和 agent，并排除 Windows Autopilot。
- 检索结果中有大量咨询公司与合作伙伴博客（bismart、powerapps911、innfactory、digitalapplied、robquickenden 等），第一轮逐个判断，只转述官方内容的不收。

## 第一轮判断记录（2026-11-10）

- 已收媒体：GeekWire（Mary Jo Foley，2026-05-04，发布前的 ClawPilot 报道）、Computerworld（Forrester 分析师评论）、Semafor（Shahine 采访，预览期计费）、TechRadar Pro（Nadella 主题演讲引语）、TestingCatalog（桌面客户端界面观察）、The Neuron（Shahine 采访与演示）。
- 已收社区：copilotatwork（Danny de Vries，上手使用）、OpenClaw 博客（微软上游贡献清单）、CIAOPS（模型调用经 GitHub Copilot 的数据边界分析）、dsebastien（时间线与参考来源汇总）。
- 放弃（只复述公告或文档、无新信息）：Decrypt、Help Net Security、The Register、PCWorld、Neowin、Gigazine、Office Watch、Redmond Magazine（9-25 改名稿）、IT之家（转述 TestingCatalog，经凤凰网转载）、The New Stack（6-07 评论，无一手来源；原站 403，Wayback 快照 20260608170812 可读）、Futurum、aicybr（SEO）、hubsite365（Shane Young 视频的 AI 摘要；原视频无文字稿）。
- 未收、可再看：Shane Young 的 YouTube 上手视频（有字幕时可按「字幕整理」收）；cgtech-au 的个人体验文章（站点返回「Web App - Unavailable」，Wayback 无快照）；Omar Shahine 个人的 Lobster 项目站 lobster.shahine.com（家用 OpenClaw 智能体，是 Scout 的前身而非产品本身，暂不收）。

## 已知问题

- 改名：2026-06 的资料称 Scout，2026-09 起称 Autopilot。资料页标题按原文，摘要中注明是同一产品。
- 截至 2026-11-10，Learn 文档与 MC 公告仍用 Scout 之名、仍描述桌面应用；9-25 起的 Autopilot 是云端托管，文档尚未跟上。增量收集时留意 Learn 是否出现 Autopilot 文档集或改名。
- 行业综合中有两篇比较涉及本产品（ithome 五款主动型 Agent、ai-agents-compared-small-business），已在 `products` 补上 `microsoft-autopilot`。

## 命名约定

- 目录名用 `microsoft-autopilot`，不用 `autopilot`，避免与 Windows Autopilot 混淆。
