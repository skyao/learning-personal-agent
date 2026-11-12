---
title: "OpenAI Dots：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-12
sourcesUntil: 2026-11-11
description: >
  每个 dot 有一台 OpenAI 托管的持久云端计算机（Linux + Chrome），可选连接用户的一台电脑，并能把任务委派给 Codex 和 ChatGPT Work；规格、并发和超时官方均未公开。
---

## 概要

- 每个 dot「住在云端」，有自己的计算机和浏览器，建立在与 ChatGPT Work 相同的云端计算机基础设施上；用户设备关机时工作可以继续。
- 执行路径有三条：dot 自己的云端计算机、可选连接的一台用户电脑、委派给 Work 和 Codex 的任务；另有不占用计算机、只读的后台研究智能体。社区实测确认这些路径可以并行。
- 云端计算机是持久的：会话之间保留快照，文件和浏览器登录状态可以保留；删除或重置 dot 会删除这台计算机。
- 独立安全研究者 Cyera 的检查显示，环境是 Debian 13 桌面，容器位于 Kata 虚拟机边界内并叠加 bubblewrap 沙箱，出站流量经代理；这些细节没有官方确认。
- 云端环境无法满足需要 Docker、VPN、公司设备或内部服务器的任务，官方和实测都建议这类任务改用已连接的电脑。
- 官方没有公开计算机规格、并发上限和单任务时长；首月之后的用量条款截至 2026-11-11 的资料仍未公布。

## 每个 dot 一台持久的云端计算机

发布当天官方即称「每个 dot 在它自己的云端计算机上工作，而你的计算机及其内容保持独立，除非你选择连接它」（[推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}})）。安全博客补充：环境由 OpenAI 托管，沙箱限制 dot 的代码和工具能访问的内容，各用户的云端环境彼此隔离，OpenAI 维护底层的 Linux 与 Chrome；自动审查的控制放在 dot 能修改的环境之外，dot 无法关闭必需的检查（[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})）。企业安全文档说明 dots 与 ChatGPT Work 使用相同的云端计算机基础设施，已审查过 Work Cloud 的组织可以以此为评估起点（[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})）。

环境里有浏览器、终端和文件。用户可以「打开计算机」查看，「接管」使用鼠标键盘，再「交还控制」（[文档：连接计算机和应用]({{< relref "/docs/dots/sources/official/2026-11-05-docs-computers-and-apps" >}})）。云端浏览器的 cookie 与成员设备分开存储，不继承用户个人浏览器的登录状态，会话在用户退出或网站过期前保持可用。登录可以通过私密登录表单（密码不经过对话、不暴露给模型）或接管后手动完成，凭证细节见[安全]({{< relref "/docs/dots/analysis/security" >}})。

Cyera 对环境的检查（2026-10-14）给出了官方没有的细节：Debian 13、XFCE 桌面、Chrome 与终端；模型以无特权用户 `agent` 运行，系统目录只读，主目录和工作区可写并持久；容器位于 Kata 虚拟机边界内，再叠加 bubblewrap 沙箱；出站经 HTTP 代理，拒绝直连互联网和云元数据服务；dot 自报的工具约 270 项（[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})）。Slide Factory 转述开发者论坛的一次测试：同样是 Debian 13、没有 sudo，Docker 已安装但无法访问宿主机套接字，.NET 项目能编译并跑通 193 个后端测试，完整技术栈无法运行（[Slide Factory 第一天]({{< relref "/docs/dots/sources/community/2026-10-03-slidefactory-dots-first-day" >}})）。有用户报告云端只有 8G 存储空间（[靖轩：深度体验 11 天]({{< relref "/docs/industry/sources/community/2026-10-10-jingxuan-dots-11-days" >}})），官方没有给出容量数字。

## 三条执行路径，可以并行

官方文档列出的执行方式包括 dot 自己的云端计算机、用户连接的电脑、委派给 Work 或 Codex 的任务，以及不占用计算机的后台智能体和新的云端会话线程（[文档：认识 dots]({{< relref "/docs/dots/sources/official/2026-11-05-docs-meet-dots" >}})）。一项任务可以在云端管理，同时使用已连接电脑上的文件和工具；任务编排始终在 OpenAI 云端，对话、工具结果和上下文「不会只留在已连接的计算机上」（[文档：Work Cloud 与本地计算机访问]({{< relref "/docs/dots/sources/official/2026-11-05-docs-cloud-local-access" >}})）。

一位 Reddit 用户在发布后第三天的实测（2026-10-01）把这些路径逐一验证：dot 在自己的云端计算机上连续数天审阅数百份 PDF 并记得进度；委派给 Codex 的任务因「没有可用执行环境」启动失败，连接一台闲置 Linux 电脑后才得以运行；云端计算机任务、已连接电脑任务和只读的后台研究智能体可以同时运行。该用户也指出，dot 只是在「充当队列管理者」：它会记住被阻塞的任务并定期重试，但没有原生队列，看不出已连接电脑是否空闲；并行路径也不等于独立的用量额度（[Reddit：拿棍子戳 Dots]({{< relref "/docs/dots/sources/community/2026-10-01-reddit-poking-dots-with-sticks" >}})）。

任务一旦开始就停留在原来的环境：更改 dot 所选的计算机不会迁移已有任务（[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})）；本地任务不会自动迁移到云端，本地子任务失去访问权后也不能在云端恢复。

## 可选连接一台用户电脑

本地计算机访问可选、默认关闭，须在那台电脑的 ChatGPT 桌面应用中「允许访问」；一次只能连接一台个人电脑，电脑要在线且应用打开（[文档：连接计算机和应用]({{< relref "/docs/dots/sources/official/2026-11-05-docs-computers-and-apps" >}})）。把电脑连接到 Codex 或开启 Work Sync，任一项单独都不会让 dot 获得访问权。电脑离线时授权仍保留，只有状态为「已断开连接」才表示权限已移除。网站屏蔽云端浏览器时，可以让 dot 改用本地浏览器，这会生成单独的本地任务，不转移云端浏览器会话。

云端计算机不继承成员本地的 VPN、浏览器登录或设备策略；企业单点登录若要求公司设备或 VPN，云端浏览器无法满足，官方建议用户在合规设备上自己完成（[帮助中心：工作区管理]({{< relref "/docs/dots/sources/official/2026-11-05-help-manage-dots-in-workspaces" >}})）。实测结论与此一致：Slide Factory 的本地 MCP 进程无法在云端运行，改用托管端点后才成功；作者建议需要 Docker、VPN、内部服务器或本人登录状态的任务放到已连接电脑或自有基础设施上（[Slide Factory 第一天]({{< relref "/docs/dots/sources/community/2026-10-03-slidefactory-dots-first-day" >}})）。

## 持久、暂停、删除

| 操作 | 效果 | 资料 |
| --- | --- | --- |
| 两次使用之间 | 云端计算机保持状态；会话之间保留快照，磁盘保留文件和浏览器状态 | [文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}}) |
| 暂停 | 停止当前主要任务，可恢复；停止任务不撤销已完成的操作 | [文档：认识 dots]({{< relref "/docs/dots/sources/official/2026-11-05-docs-meet-dots" >}}) |
| 删除 | 删除云端浏览器和计算机，不可恢复；dot 创建的文件、Codex 会话线程和 ChatGPT 对话单独存储，不随之删除 | [文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}}) |
| 重置 | 等同删除 dot（含对话、记忆、计划任务），之后新建 | [帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}}) |

快照保留期限：启用数据驻留或 EKM 的合格工作区按五天周期清除、最长不超过七天；其他工作区中活跃 dot 的快照没有最长保留期，客户目前无法要求提前清除；dot 删除后 30 天内删除（[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})）。

## 成本与限制

官方的用量口径是：与 dot 的对话不计入 ChatGPT 使用限额，dot 在 Work 或 Codex 中启动的任务照常计入；发布后第一个月有延长额度（[推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}})）。价格与额度的完整说明见[开放与价格]({{< relref "/docs/dots/analysis/access-pricing" >}})。官方资料没有给出云端计算机的并发数、单任务超时或算力配额。

响应速度方面有一例实测：Slide Factory 在 Slack 中 16:24 发出的请求 17:13 才被接到，17:15 收到回答（[Slide Factory 第一天]({{< relref "/docs/dots/sources/community/2026-10-03-slidefactory-dots-first-day" >}})）。《纽约时报》两周实测中，dot 的网页浏览器不断出故障，批量投递求职申请的任务卡住（[NYT 五个杀手级任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}})）。

成本压力方面，甲子光年转述巴克莱分析师 Ross Sandler 的估算：免费 Personal Agent 的运行成本约为免费 ChatGPT 的 10 倍，原因是全天候云端常驻、独立虚拟机和定时扫描（[甲子光年]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})）。

企业侧的限制：测试期不支持数据驻留和推理驻留，FedRAMP、EKM 工作区不适用；任一云端政策启用 `enforce_residency` 时本地计算机访问不可用；带本地访问时部分本地钩子不受支持，云端编排事件不会进入本地 OpenTelemetry 收集器，需要用 Compliance API（[文档：Work Cloud 与本地计算机访问]({{< relref "/docs/dots/sources/official/2026-11-05-docs-cloud-local-access" >}})）。

推断：dots 的运行环境与 ChatGPT Work、Codex 共用基础设施和执行路径，dot 本身更像一个调度层。好处是能复用已有的云端容器、本地连接和企业管控；代价是用户要理解多个执行目标、各自的额度和失败方式，社区批评 OpenAI 的 Chat、Work、Dots 三者「用起来割裂」（[智消前沿：家谱]({{< relref "/docs/industry/sources/community/2026-11-09-aiwenxiao-personal-agent-family-tree" >}})）也指向这一点。

## 不一致的说法

- 「大语言模型」公众号称 Dots「不走虚拟机路线」（[大语言模型：讲透 Muse、Dots]({{< relref "/docs/industry/sources/community/2026-10-27-dayuyanmoxing-muse-dots-explained" >}})），与官方「拥有自己的计算机和浏览器」不符，应是作者误读。
- 关闭本地访问后，Work 会立即中断正在运行的轮次；官方特意提醒 dots 已授权的本地任务可能仍在完成，不要假定两者行为相同。

## 资料缺口

- 云端计算机的规格（CPU、内存、磁盘）、单任务最长时间、并发上限、休眠与唤醒机制。
- Kata 虚拟机、bubblewrap 等隔离细节的官方确认。
- 多个 dot 并存时环境如何共享或隔离（目前每个账户只有一个主 dot）。
- 桌面应用是否支持 Linux（Reddit 用户连接的是 Linux 电脑，官方未说明）。

## 主要资料

- 官方：[文档：连接计算机和应用]({{< relref "/docs/dots/sources/official/2026-11-05-docs-computers-and-apps" >}})（云端计算机与本地连接）；[文档：Work Cloud 与本地计算机访问]({{< relref "/docs/dots/sources/official/2026-11-05-docs-cloud-local-access" >}})（混合执行、企业限制）；[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})（基础设施、快照、删除）；[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})（沙箱与隔离）。
- 媒体：[NYT 五个杀手级任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}})（浏览器故障）；[甲子光年]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})（运行成本估算）。
- 社区：[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})（环境与隔离的技术细节）；[Reddit：拿棍子戳 Dots]({{< relref "/docs/dots/sources/community/2026-10-01-reddit-poking-dots-with-sticks" >}})（执行路径与并行）；[Slide Factory 第一天]({{< relref "/docs/dots/sources/community/2026-10-03-slidefactory-dots-first-day" >}})（云端环境的限制）。
