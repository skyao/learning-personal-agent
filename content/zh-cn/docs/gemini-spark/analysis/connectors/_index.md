---
title: "Gemini Spark：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Spark 的连接以 Google 自家服务为主，第三方只有少数官方合作和用户自己填的 MCP 服务器；没有连接器的网站靠 Chrome 自动浏览。10 月曾出现表格写入被策略检查拦截的故障。
---

## 概要

- 主力是 Google 自家服务：Workspace 全家、相册、通讯录、搜索、地图、YouTube，默认关闭、在设置中开启。Workspace 操作在 7 月 14 日扩充，能编辑共享的文档、表格、幻灯片。
- 官方第三方连接只有少数几家：I/O 当天的 Canva、OpenTable、Instacart（MCP），7 月 7 日的 Dropbox、Zillow。第三方资料给出的对照是 Dots 经插件连 4,000 多个应用、Claude Duet 6,000 多个连接器和插件。
- 6 月 29 日起支持自定义 MCP：填服务器 URL 即可，须遵循标准 MCP 规范；限美国、18 岁以上、个人账号、英语。Google 明说不控制、不监控第三方服务器，所有写入操作要手动确认。
- 没有连接器的网站，7 月 30 日起交给 Chrome 自动浏览，用用户已登录的账号操作。
- 2026-10-13 起多名用户报告 Spark 能读不能写 Google 表格，报错为「Blocking policy check failed」；楼主 10-16 称后端已修复，Google 官方没有公开说明。

## Google 自家服务

截至 2026-11-10 的帮助页列出的可连接服务：通讯录、Gemini Notebook、Google 相册、Workspace（日历、文档、云端硬盘、Gmail、Keep、表格、幻灯片、Google Tasks）、Google 搜索服务（搜索、财经、航班、酒店、地图）、YouTube，另有「若干第三方应用」，以及经确认的「使用 Google 登录」（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。产品页称这些连接「默认关闭」（[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})）。

Workspace 中能做的操作（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）：

| 应用 | 操作 |
| --- | --- |
| 日历 | 查看、回复邀请、新建、改期、取消 |
| Gmail | 搜索与汇总、起草、转发、回复、贴标签 |
| 云端硬盘 | 搜索、读取、重命名、删除 |
| 文档、表格、幻灯片 | 编辑、读评论；编辑共享文件要用户先审阅计划的修改 |
| Keep、Google Tasks | 查找与创建；Google Tasks 私密任务的批量操作可以不经确认 |

这些能力分批加入：6 月 29 日接入 Google Tasks、Keep 和读取 Docs 评论；7 月 14 日增加编辑私有表格和演示文稿、编辑共享的文档表格幻灯片、向文档和演示文稿加图、用 Canvas 编辑（[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})）。8 月 13 日改用 Gemini 3.7 Flash 时，官方称改进了「对 Google Workspace 应用的工具使用」（[3.7 Flash 发布]({{< relref "/docs/gemini-spark/sources/official/2026-08-13-gemini-3-7-flash-spark" >}})）。

Google 相册约 2026-09 起逐步在任务中可用：搜索挑选、编辑（生成新副本，不覆盖原图）、建相册、通过 Gmail、Docs、Messages 分享相册链接、从图片提取文字；新相册默认私密，共享和发邮件前要许可；美国部分地区不可用，只在移动应用和网页版（[帮助：相册工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-google-photos-workflows" >}})）。

## 少数官方第三方合作

I/O 当天 Google 宣布「今天上线与 Canva、OpenTable 和 Instacart 的新 MCP 连接」，更多伙伴在接入中（[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})）。更新日志的时间是 7 月 1 日推出 Canva、Instacart、OpenTable，7 月 7 日推出 Dropbox、Zillow（[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})）；6 月更新稿写作 Zillow Rentals，并称连接应用先在网页和移动版一周内陆续推出，数周内推到 macOS（[6 月更新]({{< relref "/docs/gemini-spark/sources/official/2026-06-30-spark-updates-june" >}})）。

第三方给出的对照：iThome 称 Dots 「透过外挂可连接 4,000 多个 App」（[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）；Freistyle AI 列出 Muse 连 Meta 系账号和 Figma、Shopify、Slack、Stripe、Zoom 等十多项，Claude Duet 列有 6,000 多个连接器和插件（[Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。

推断：Spark 的第三方连接器数量明显少于 Dots 和 Duet，它的覆盖面主要来自 Google 自家服务加浏览器操作，而不是连接器生态。

## 自定义 MCP 应用

6 月 29 日起可以用 MCP 服务器 URL 把个人或第三方应用接入 Spark（[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})、[6 月更新]({{< relref "/docs/gemini-spark/sources/official/2026-06-30-spark-updates-june" >}})）。帮助页的规则（[帮助：自定义应用]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-custom-apps" >}})）：

- **接入**：在网页版「已连接应用」设置中填 MCP 服务器 URL，服务器须遵循标准 MCP 规范；不支持动态客户端注册的可以手动填凭据。接入后移动应用和网页应用都可用，用 `@` 指定。Google 另提供 Connected Apps Platform 和 Gemini Developer Mode 给开发者调试。
- **准入**：年满 18 岁且身处美国、个人 Google 账号、开启 Keep Activity；目前只有英语，只在移动应用和网页版，Mac 应用没有列入。
- **撤销**：可以断开连接、从 Google 账号解除 MCP 服务器关联并撤销权限，或在 Google 账号的「已关联应用」页面解除。
- **风险**：Google 不控制、不监控、不保护第三方 MCP 服务器；数据发出后受对方隐私做法约束；应用可能过度索取数据；Gemini 对任何写入操作要求手动确认。

## 没有连接器时走浏览器

7 月 30 日起 Spark 可以通过 Chrome 自动浏览，用用户已登录的账号和保存的密码处理网页杂事（[Chrome 集成]({{< relref "/docs/gemini-spark/sources/official/2026-07-30-spark-chrome" >}})）；云端还有一个远程浏览器（详见[运行环境]({{< relref "/docs/gemini-spark/analysis/runtime" >}})）。WIRED 的午餐测试里，Spark 通过 DoorDash 选了一家越南餐厅，却只给老板加了一个 5 美元的卷，是该项「唯一真正失败」的一款，得 1/5（[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。

## 表格写入被策略检查拦截（2026-10）

一则 Google 开发者论坛帖子记录（[开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}})）：

- 2026-10-13 起，楼主的 Spark 可以读取 Google 表格，但写入全部失败，内部工具 `sheets_agent:call` 返回「Failed to verify file permissions: Blocking policy check failed」（PERMISSION_DENIED），所测表格全部失败，包括「知道链接的任何人可编辑」的表；重新连接 Workspace 无效。香港和美国用户都遇到同样错误，都是个人账号。
- 楼主转述另一则社区报告：Spark 无法编辑 Google 幻灯片，「高级 Spark 子智能体」失败而 Drive 访问正常。
- 楼主转述 Google 支持的回复：表格内编辑应使用表格里的 Gemini 侧边栏，而不是独立的 Gemini 应用。
- 2026-10-16 楼主回报「后端回归问题似乎已完全解决」。

Google 支持的回复（换用侧边栏）和楼主的结论（后端回归已修复）不一致；故障原因是楼主的分析，Google 官方没有公开说明。楼主还提到故障开始时正是 Argon 模型推出的时候，这只是时间上的重合。

## Verge 早期实测中的连接限制

2026-06 的 The Verge 实测中，Spark 创建的 Google Doc 只有作者能访问，问它能否给妻子权限，它答称目前做不到；Spark 还请求访问通讯录，被作者拒绝，任务仍然完成（[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})）。这发生在 7 月 14 日扩充 Workspace 操作之前；之后能否修改共享权限，资料没有写。

AI Agents Library 在 2026-08 的测试中，Spark 把带公式、图表和汇总行的表格写进 Drive，得 8.5 分，作者提醒「每个公式仍然需要复核」（[AI Agents Library 三方对照]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})）。

## 资料缺口

- 官方第三方连接器的完整清单和增长情况；是否有面向开发者的连接器上架或审核机制（Connected Apps Platform 的细节）。
- 10 月表格写入故障的官方说明与影响范围。
- 自定义 MCP 应用何时开放到美国以外和 Mac 应用。
- Spark 能否修改 Drive 文件的共享权限。
- 网站方（如 Airbnb、亚马逊）对 Spark 的拦截或合作情况。

## 主要资料

- 官方：[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})（服务清单与操作）；[帮助：自定义应用]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-custom-apps" >}})；[帮助：相册工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-google-photos-workflows" >}})；[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})、[6 月更新]({{< relref "/docs/gemini-spark/sources/official/2026-06-30-spark-updates-june" >}})、[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})、[Chrome 集成]({{< relref "/docs/gemini-spark/sources/official/2026-07-30-spark-chrome" >}})、[3.7 Flash 发布]({{< relref "/docs/gemini-spark/sources/official/2026-08-13-gemini-3-7-flash-spark" >}})；[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})。
- 媒体：[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})；[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})；[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
- 社区：[开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}})；[AI Agents Library 三方对照]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})；[Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})。
