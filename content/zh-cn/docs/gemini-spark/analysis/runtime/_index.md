---
title: "Gemini Spark：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Spark 在 Google 云端运行，设备关机后继续工作；上网有本地 Chrome 和云端远程浏览器两条路径，另有一台保存数据的远程计算机。环境规格官方没有公开。
---

## 概要

- 官方称 Spark 在云端运行，合上笔记本、锁上手机、设备关机后都继续工作；发布时运行在 Gemini 3.5 上，使用 Antigravity harness。虚拟机规格、隔离方式官方没有写，「Google Cloud 专用虚拟机」「每项任务一台全新的临时虚拟机」只出自第三方综述，未注出处。
- 上网有两条路径：桌面上用户自己的 Chrome（Chrome 自动浏览），可用已登录账号和密码管理器，但设备和 Chrome 必须开着；或云端的远程浏览器，关掉设备也能继续，遇到登录就停下来等用户接管。帮助页写明远程浏览器「仅在移动设备上使用」。
- 任务还能用一台远程计算机运行代码、生成文档和媒体文件，远程浏览器的 Cookie 和代码执行数据都留着供后续会话使用；关闭任务模式时这两类数据被删除。
- Mac 应用让 Spark 处理本机文件，只能碰用户加入「已连接的文件夹」的文件，改动前做临时备份，24 小时后删除；7 月 14 日起可从另一台设备远程控制 Mac 上的 Gemini。
- 硬性限制：同一时刻最多 15 个任务运行，用量按计算量计、随订阅档位提高。

## 云端运行，设备关机后继续

I/O 发布稿称 Spark 是「运行在 Gemini 3.5 上，并使用 Antigravity harness」的云端智能体，「即使你合上笔记本电脑或锁上手机，Spark 仍会在后台继续工作」（[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})）。产品页和计划帮助页说法相同：即使手机和笔记本都关着也在后台工作，计划在云端而不是用户的手机或电脑上运行（[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})、[帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}})）。

运行环境的规格、隔离方式、休眠与回收，官方资料都没有写。第三方的说法有两种：Datawhale 综述与鸿煊的文章称 Spark「在 Google Cloud 专用虚拟机中执行」（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）；iThome 的比较表称每项任务进入「全新、严格隔离的暂时性 VM」（[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。三篇都没有注明出处，鸿煊一文又几乎逐句沿用 Datawhale，不能算两个独立来源。

## 本地 Chrome 与云端远程浏览器

7 月 30 日起 Spark 与 Chrome 集成，经许可使用用户「已登录的账号和保存的密码」处理网页杂事，如安排看房、查航班并开始预订流程（[Chrome 集成]({{< relref "/docs/gemini-spark/sources/official/2026-07-30-spark-chrome" >}})）。截至 2026-11-10 的帮助页把网页浏览分成两条路径（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）：

| 路径 | 在哪里运行 | 能用什么 | 设备要求 | 限制 |
| --- | --- | --- | --- | --- |
| Chrome 自动浏览（Chrome auto browse） | 用户桌面上的本地 Chrome | 与用户相同的网站，包括已登录网站；经许可可用密码管理器中的登录信息 | 设备和 Chrome 保持唤醒并运行；任务完成前设备不可用时，可能改用远程浏览器 | 目前仅桌面端；首次使用要授权 Chrome 连接 Gemini，此后每项涉及浏览的任务都先确认 |
| 远程浏览器 | 云端单独的浏览器 | 一般网站；Cookie 等登录信息保存供后续会话使用 | 关闭设备也继续 | 登录网站等步骤会暂停，等用户接管；帮助页称「远程浏览器仅在移动设备上使用」 |

用户阻止网页浏览后，Gemini 可能改用远程浏览器、其他工具，或放弃任务（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。

推断：官方各页对设备依赖的说法看似矛盾（计划页称「即使你的设备关机，它也会继续工作」，任务页称用本地浏览器时要让设备保持唤醒），按任务页的说明，两者分别对应云端执行与本地浏览器两条路径，并不冲突；但何时选哪条路径、移动端发起的任务能否用桌面 Chrome，帮助页没有写清。

## 远程计算机：运行代码、生成文件、保留数据

帮助页称任务可以「使用远程计算机运行代码或执行复杂任务」，数据保存在远程计算机上供后续会话使用；可生成 .pdf、.docx、.xlsx、.pptx、代码、.html、图像、.mp3、.mp4、.zip 等文件（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。

数据的保留与删除：

- 远程浏览器的 Cookie 等登录信息「为你方便而保存」，Gemini 可能代用户自动删除，用户也可以在设置的「浏览器」里删除；代码执行数据可在任务设置里删除（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。
- 删除某个任务线程不会删除关联的远程浏览器数据和远程代码执行数据（[帮助：查找与管理任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-find-and-manage-tasks" >}})）。
- 关闭任务模式会删除远程浏览器数据和远程代码执行数据，不清除本地 Chrome 的浏览数据，已有任务、线程、计划和文件保留（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。

技能可以带脚本，但不支持需要联网的脚本，脚本不能对外部网站执行操作或发请求；一个技能连同参考文件不超过 100 MB（[帮助：技能]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-skills" >}})）。

另外，任务运行中用户可以补充说明，Gemini「在不丢失进度的情况下」更新工作；7 月 13 日起复杂任务可以并行检索、审查多个来源（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})、[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})）。一则开发者论坛帖子中，写入表格失败时报错的内部工具名为 `sheets_agent:call`，楼主提到另有报告称「高级 Spark 子智能体」编辑幻灯片失败（[开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}})）。

推断：从工具名和「子智能体」的说法看，Spark 内部可能按应用拆成若干子智能体或工具层；这只是用户从报错信息看到的痕迹，官方没有说明架构。

## Mac 应用：本机文件与远程控制

Spark 进入 Gemini 的 macOS 应用是为了「处理涉及本地文件的任务」，如把「下载」里的 PDF 分类归档、用本机发票做预算表并设定期更新（[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})、[6 月更新]({{< relref "/docs/gemini-spark/sources/official/2026-06-30-spark-updates-june" >}})）。帮助页的规则（[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})）：

- 只能看到用户加入「已连接的文件夹」的文件；授权后可查看、编辑「下载」「桌面」「文稿」「照片」等大多数文件夹。
- 处理文件时创建临时备份，进入下一项任务前可恢复；备份在开始新查询或任务时，或 24 小时后删除。任务完成或用户要求删除后，文件「可能无法恢复」。
- 公共云盘的文件夹加入后，Gemini 可访问、编辑、共享、删除其中文件，并可能把用户数据共享给该云盘。

7 月 14 日起，可以从另一台设备让 Gemini 在用户的 Mac 上执行操作；两台设备需登录同一账号，处于同一 Wi-Fi 或打开蓝牙（[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})、[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})）。

## 并发与用量上限

- 同一时刻最多 15 个任务运行，达到上限要等任务完成才能发新请求；已有 15 个任务运行时计划也不会运行（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})、[帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}})）。
- 用量按计算量计，随更高的 Google AI 订阅提高，接近上限时 Gemini 会提示；达到上限时计划不运行（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})、[帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}})）。具体额度没有公开。
- 计划的运行时间是大致的，高流量期可能延迟（[帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}})）。

Top5Apps 称 Spark「最多 15 个定时或事件触发的任务」，与官方口径（同时运行 15 个任务，活跃计划另有 50 个上限）不同（[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。

## 网站拦截与验证

实测中卡住 Spark 的往往不是运行环境本身，而是目标网站：

- WIRED 让 Spark 用远程浏览器订一家寿司店的晚餐，触发了发到作者手机的六位验证码，仍没订成，作者最后打电话订位（[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})，2026-05 Beta 首周）。
- The Verge 让 Spark 预订 Airbnb，Spark 称因 Airbnb 的安全和认证政策无法登录、付款、预订；作者认为「是 Airbnb 封了这次操作，不是 Google」（[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})，2026-06）。

这两次测试都在 7 月 30 日 Chrome 自动浏览上线之前，此后用本地已登录浏览器的效果，资料中没有实测。

## 资料缺口

- 云端环境的规格、隔离方式（每用户还是每任务）、休眠与回收；第三方「专用虚拟机」「临时 VM」说法的一手出处。
- 本地 Chrome 与远程浏览器之间如何选择、何时切换；移动端发起的任务能否使用桌面 Chrome。
- 计算量用量的具体额度，各档位差别。
- Chrome 自动浏览上线后的网页任务实测。

## 主要资料

- 官方：[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})（云端、Gemini 3.5、Antigravity）；[6 月更新]({{< relref "/docs/gemini-spark/sources/official/2026-06-30-spark-updates-june" >}})（Mac 本机文件）；[Chrome 集成]({{< relref "/docs/gemini-spark/sources/official/2026-07-30-spark-chrome" >}})；[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})（远程控制 Mac、并行检索）；[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})；[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})（两种浏览器、远程计算机、并发与用量）；[帮助：计划]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-schedules" >}})；[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})；[帮助：查找与管理任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-find-and-manage-tasks" >}})；[帮助：技能]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-skills" >}})（脚本限制）。
- 媒体：[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})、[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})（网站拦截）；[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})（临时 VM 说法）。
- 社区：[开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}})（内部工具名）；[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})（专用虚拟机说法）；[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})（15 个任务的另一口径）。
