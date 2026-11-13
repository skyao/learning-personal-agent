---
title: "Grok Bot：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Grok Bot 给每个用户一台位于美国的 Cursor 云端 Firecracker 微虚拟机，同一用户的所有 Bot 共用这台计算机，共享文件、浏览器会话和登录状态，各 Bot 只有各自的屏幕；空闲休眠、按需唤醒，持久磁盘跨重建保留，装过的软件包不保留。
---

## 概要

- 计算机按用户分配，不按 Bot 分配。发布稿和设计文章写的是「Bot 有自己的计算机」；10 月以后的官方文档写明「这台电脑分配给你的用户账户，而不是某个 Bot」。同一用户的 Bot 共享文件、浏览器 Cookie 和命令行凭据，每个 Bot 只有一块自己的屏幕，屏幕「不是安全边界」（见[一台计算机，多个 Bot](#一台计算机多个-bot屏幕不是安全边界)）。
- 用户之间的隔离靠硬件虚拟化：官方称每个用户一台专用的 Firecracker 微虚拟机，运行在 Cursor 托管的云上，位于美国，不支持本地部署和自带镜像（见[每个用户一台 Cursor 云上的微虚拟机](#每个用户一台-cursor-云上的微虚拟机)）。
- 计算机不常驻运行。它空闲时休眠，用户打开预览、来电或有新任务时唤醒。磁盘上的文件、浏览器会话和登录状态跨更新与重建保留；用户自己装的应用、软件包、`node_modules` 和 Python 虚拟环境不保留。对话历史存放在计算机之外（见[休眠、更新与重建](#休眠更新与重建持久磁盘保留装过的东西不保留)）。
- 企业版把这台计算机变成可管理的资产：可以统一安装脚本和网络客户端、注入团队机密、批量重建或终止计算机、设置不活跃计算机的保留期。默认出口是 Cursor 的共享静态 IP，可以改为经成员自己的桌面出网（见[企业对计算机的管理](#企业对计算机的管理)）。
- 社区报告的问题集中在共享与并行两处：Bot 多了会变慢，6 个 Bot 并行时浏览器配置文件重置、崩溃。另有一位开发者指出，云端浏览器的指纹补丁不足，遇到托管式 Cloudflare 挑战时会陷入循环。这些都是个案，没有官方数据（见[实测中的表现与问题](#实测中的表现与问题)）。

## 每个用户一台 Cursor 云上的微虚拟机

Grok Bot 由 SpaceXAI（xAI）在 2026-08-11 发布。产品文档和帮助页由 Cursor 托管，资料页收录说明写明 Cursor 于 2026-08-14 并入 SpaceXSI，见[文档：Grok Bot 概览]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-overview" >}})。

官方安全 FAQ 写明，每个用户获得「一台专用的 Firecracker 微虚拟机（microVM），拥有自己的内核、内存和虚拟设备」，一个用户无法访问另一个用户的计算机，见[安全 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security-faq" >}})。其他官方文档的说法与此一致：

- [文档（docs.x.ai）：电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})称「每个用户的电脑都是专用且硬件隔离的」。
- [文档：Grok Bot 安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})的架构图把托管计算机画在「Cursor 云」里，标注「每位成员一个 microVM，位于美国」。
- 同一安全文档写明，Grok Bot 也受 Cursor 仅限美国的数据驻留计划覆盖。

官方称「Grok Bot 只在 Cursor 托管的云计算机上运行」，本地部署、在客户自己的边界内部署和自带镜像都不支持，见[安全 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security-faq" >}})。

计算机内有桌面、浏览器（Chrome）、文件系统和终端。用户可以在对话右侧面板观看 Bot 的点击和输入，也可以接管，见[指南：Grok Bot 入门 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})和[文档：使用 Grok Bot 工作]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})。接管的设计用途是只完成被卡住的那一步，例如单点登录、通行密钥、CAPTCHA、二维码、银行卡验证，然后交还给 Bot。桌面端和手机端都是同一台云端计算机的「瘦客户端」，关闭应用或合上笔记本不会停止云端工作。

计算机能运行的东西逐步增加。据[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})：

| 版本 | 日期 | 变化 |
| --- | --- | --- |
| v0.68.1 | 2026-10-07 | 屏幕从 1280×800 提高到 1920×1200；浏览器页面卡住 25 秒后放弃 |
| v0.79.2 | 2026-11-05 | 可以运行 `ssh` 和 `psql` |

企业版的「Allow Sudo on Bot Computers」默认开启，允许 Bot 在自己的计算机上以 root 身份运行命令，见[文档：面向 Teams 和 Enterprise 的 Grok Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})。

社区实测与官方描述一致。程序员鱼皮在 Bot 详情页的「电脑」标签打开云电脑，先显示「正在唤醒」，「稍等十几秒就能进入桌面」，桌面上有 Chrome、文件管理器和终端，见[鱼皮：大厂为什么都在做 Personal Agent]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})。Claire Vo 在 8 月的试用中把它描述为 OpenClaw 的轻量版，「自带一台虚拟计算机，配有 Chrome、终端和文件系统」，见[ChatPRD：Claire Vo 试用 Grok Bot]({{< relref "/docs/grok-bot/sources/community/2026-08-18-chatprd-claire-vo-grokbot" >}})。

## 一台计算机，多个 Bot：屏幕不是安全边界

早期官方资料把计算机写成每个 Bot 各有一台：

- [发布稿]({{< relref "/docs/grok-bot/sources/official/2026-08-11-introducing-grok-bot" >}})（08-11）称 Bot「有自己的计算机」。
- [扩大到更多套餐]({{< relref "/docs/grok-bot/sources/official/2026-08-26-grok-bot-more-plans" >}})（08-26）称「它们在云端有自己的计算机」。
- [我们如何设计 Grok Bot]({{< relref "/docs/grok-bot/sources/official/2026-09-03-designing-grok-bot" >}})（09-03）称 Bot「有自己的计算机和工具」。

10 月以后的官方文档写得明确：「这台电脑分配给你的用户账户，而不是某个 Bot。如果账户上的另一个 Bot 不应能使用某项凭据或文件，就不要把它放在上面。」见[文档（docs.x.ai）：电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})和[文档（docs.x.ai）：常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})。

[面向 Teams 和 Enterprise 的文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})的表述是：同一用户内部，「Bot 隔离的是人格和工作区，而不是计算资源」。Cybernews 在报道 Bot 把 CEO 银行数据发到公司 Slack 的事件时，引用的也是这段说明，见[Cybernews]({{< relref "/docs/grok-bot/sources/media/2026-10-07-cybernews-bank-data-slack" >}})。

共享的范围包括：

- 文件：共享工作区在 `/workspace`，一个 Bot 可以接着另一个 Bot 保存的工作继续。
- 浏览器 Cookie 和登录状态：用一个 Bot 登录过的网站，其他 Bot 也能访问。
- 命令行凭据。

删除 Bot 不会移除计算机上的文件和浏览器会话，见[文档：Grok Bot 安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})。

能分开的只有屏幕。每个 Bot 在共享计算机上有自己的屏幕，多个 Bot 可以并行使用浏览器和桌面工具，但每块屏幕同一时间只能运行一个计算机使用（computer use）任务，官方称「这些屏幕是工作界面，不是安全边界」，见[文档：使用 Grok Bot 工作]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})。屏幕数量有上限。[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})中有一条修复写道：已删除的 Bot 会释放它在共享计算机上的屏幕，「其他 Bot 的浏览器操作不再因所有屏幕都被占用而失败」。

与此相配的数量限制，见[我们如何设计 Grok Bot]({{< relref "/docs/grok-bot/sources/official/2026-09-03-designing-grok-bot" >}})：

- 每个账户「大约 50 个 Bot」。
- 每个群聊最多 6 个 Bot。

与队友的共享 Bot 聊天时，Bot「通常也在你的计算机上工作」，见[文档：Grok Bot 概览]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-overview" >}})。

多篇第三方资料把这一点列为 Grok Bot 的主要风险或摩擦，依据都是官方说明，没有独立测试：

- [iThome 五款主动式智能体]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})
- [Datawhale 个人智能体综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})
- [AI 应用：Grok、Muse、Dots 对比]({{< relref "/docs/industry/sources/community/2026-11-01-aiyingyong-grok-muse-dots" >}})，原话是「多个 Bot，不等于多套隔离的电脑」

有一组社区资料仍写「每个 Bot 配一台云主机」，与官方文档不符：

- [小企业 AI 智能体对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})
- [Archie Li：Grok Bot 工作模式]({{< relref "/docs/industry/sources/community/2026-11-11-archieli-grok-bot-work-mode" >}})

推断：早期发布稿和设计文章说的「自己的计算机」，指的是相对用户本机而言 Bot 在云端有一台计算机，不是在描述隔离粒度。10 月的官方文档和 11 月 Cursor 托管的文档都按用户分配计算机，应以文档为准。引用早期说法的二手资料会把这一点写错。

## 后端：持久化工作流与按需唤醒的计算机

官方没有发布后端架构说明。目前最具体的描述来自开发者 Peter Piekarczyk 的博客[给 Grok Bot 发消息时实际发生了什么]({{< relref "/docs/grok-bot/sources/community/2026-10-14-peterp-what-happens-when-you-message" >}})（10-14）。作者说明，文章大部分内容来自 Cursor 的 Lee Robinson 关于 Grok Bot 实现方式的演讲，演讲没有讲到的部分是作者根据经验补充的推测。据该文：

- **主循环是持久化工作流。** 主智能体循环是「运行在服务器上、使用 Temporal 的持久化工作流」，每次模型调用和工具调用都作为一步保存，被打断或服务器崩溃时不重做已完成的步骤。回合结束后，工作流停在「等待信号」，不占内存。作者写道「据说智能体会在空闲约两分钟后休眠」，并猜测这是为了在用户很快回复时保持 worker 热状态。
- **小任务和长任务分开处理。** 小任务留在主循环里，长任务交给四类辅助工作流：通用、计算机使用、视频、云端编码。辅助工作流完成后以不打断的消息回报。
- **计算机休眠时做快照。** 智能体的计算机是 Firecracker 微虚拟机，休眠时内存和磁盘做快照，登录状态因此保留。文件、记忆和技能备份到对象存储；作者猜测存储是 S3 或 R2。
- **每个对话有一个队列。** 用户直接发的消息会打断进行中的回合；辅助智能体回报、Slack 提及、计划触发则排队等待。

官方文档对消息优先级的描述与此一致：「你发来的直接消息优先于后台工作」，「立即停止」不会撤销已完成的动作，见[文档（docs.x.ai）：对话与协作]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})。

推断：「始终开机」的说法与按需休眠并不矛盾。从 Piekarczyk 转述的演讲和官方「空闲计算机会自动休眠」的说明看，常驻的是工作流状态和持久磁盘，计算机本身在空闲时休眠、按需唤醒，以此控制每个用户一台虚拟机的成本。资料中没有官方的休眠阈值、唤醒时间或单机规格。

## 休眠、更新与重建：持久磁盘保留，装过的东西不保留

### 休眠与唤醒

官方称「空闲计算机会自动休眠。休眠不是删除」，见[文档：Grok Bot 安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})。据[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})：

- 计算机休眠时，聊天界面保留已加载的内容，并显示计算机正在休眠。
- 点开预览可以原处唤醒计算机；手机的语音通话也会唤醒休眠的计算机。
- 用户本机休眠时，Bot 会在两分钟内把它视为已断开，并立即说明。

### 什么保留，什么不保留

[文档（docs.x.ai）：电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})写明：

- **保留：** 文件、浏览器状态和受支持的登录信息，在计算机更新和恢复后保留。系统会保留已同步数据的持久副本。
- **不保留：** `node_modules`、Python 虚拟环境和手动安装的软件包。
- **存放在计算机之外：** 对话历史，因此在计算机里执行 `rm -rf` 不会删掉聊天。
- **磁盘快满时：** Bot 在聊天中告知一次，列出最大的文件并提议删除，「除非你同意，否则不会删除任何内容」。

### 三种维护操作

设置中提供三种操作，见同一文档和[文档：使用 Grok Bot 工作]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})：

| 操作 | 做什么 | 代价 |
| --- | --- | --- |
| 更新（Update） | 软件更新保留一切；计算机更新会重建机器 | 计算机更新时文件和登录保留，已装应用和软件包被移除 |
| 恢复（Recover） | 尽可能保存后，用已存数据在最新版本上重建 | 中断进行中的工作 |
| 重置（Reset） | 用上次保存的数据重建 | 无法连上时，近期改动会丢失；官方列为最后手段 |

官方建议的排障顺序是：重试 → 重启应用 → 恢复 → 更新 Bot 的计算机 → 重置。

### 更新日志中的可靠性改进

[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})中与持久性有关的条目：

- v0.77.0（10-26）：计算机在内存不足时保持运行，崩溃后恢复更快。
- 系统密钥环中的应用密钥（如 Okta Verify）在计算机重建后保留。
- 浏览器在最后一个窗口关闭后保留网站登录状态。
- 重置或恢复遇到持续拒绝保存时，保留当前磁盘，而不是恢复较旧的备份。

官方不提供客户自行操作的单台计算机时间点还原。Cursor 的生产控制平面每天做加密备份，并复制到单独的恢复设施，见[文档：Grok Bot 安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})。

## 云端计算机与用户本机

用户的 Mac 或 Windows 本机与云端计算机是分开的两台机器，见[文档（docs.x.ai）：电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})和[文档：Grok Bot 安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})。只有开启这项能力并经用户批准，Bot 才会通过桌面应用在本机运行命令、读取文件，或在两台机器之间搬运文件。

本机执行有三档策略：「每次询问」（默认，审批卡显示确切的命令）、「始终允许」和「从不允许」。这套策略与云端工作的审批分开设置。团队管理员只能设上限。

鱼皮的实测展示了这个分工，见[鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})。作者经权限确认后，让 Bot 把本地的选题抓取脚本和规则文档复制到云电脑，做出新版每日热点，从 14 个数据源抓取 347 条内容。

## 企业对计算机的管理

11 月 5 日的 Cursor 文档面向 Teams 和 Enterprise，把每位成员的计算机作为可管理对象。

### 批量重建与终止

管理员可以在 Cursor 控制台或通过组织 API 批量操作成员的计算机，见[文档：管理成员的计算机与数据]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-computers" >}})：

- **重建（Recreate）：** 用最新镜像和团队设置脚本构建替换机。运行中的 Bot 在安全点暂停，在新机上继续。
- **终止（Terminate）：** 删除计算机，运行中的工作停止，成员的下一条消息会在同一块持久磁盘上启动新机。重新连接可能要几分钟，「正在运行的回合会丢失」。

两种操作都保留持久磁盘，移除成员自己装的应用和软件包；终止不会撤销成员的访问权限。一台计算机服务成员所在的每个团队，从任一团队发起的操作都作用于同一台。

### 不活跃计算机与保留期

「已休眠的计算机一直存在，直到有人删除它」，即使成员已经离开，见[文档：管理成员的计算机与数据]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-computers" >}})。为此，[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})陆续加入了两项设置：

- Enterprise：开启「终止不活跃计算机」后，30 天没有消息的计算机视为不活跃并被终止。
- Teams（v0.79.2）：管理员可以设置 Bot 计算机保留期。

### 镜像与团队设置脚本

托管计算机的镜像由 Cursor 维护，客户不能固定版本。新镜像出现时，后台逐步重建空闲计算机，没有固定时间表；运行中的计算机大约每天一次获取团队设置清单的变更，见[文档：向组织部署 Grok Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-deployment" >}})。

Enterprise 的 Team Setup Scripts 可以在每台团队计算机上安装组织自己的工具或网络客户端，见[文档：连接私有网络]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-private-networks" >}})：

- 要求基于 Debian 的 Linux，脚本以计算机用户身份运行。
- 条目按顺序执行，每个脚本 30 分钟超时；失败不阻塞计算机，在之后的刷新中重试。

团队机密（Team Secrets）以环境变量形式传给脚本，见[面向 Teams 和 Enterprise 的文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})。限制是每个团队最多 100 个，每个值最多 32 KB，总计最多 96 KB。同时应用两个及以上团队设置的计算机，不获取任何团队的机密。

### 网络出口

计算机默认经 Cursor 的共享静态出口 IP 访问互联网，官方不提供每客户专用的出口 IP，见[文档：连接私有网络]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-private-networks" >}})和[文档：配置 TLS 检查代理]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-proxies" >}})。

访问私有网络有两种办法：

- **成员桌面转出：** 成员在设置中开启「通过这台计算机路由流量」，计算机的流量改走该成员桌面的网络。据更新日志，此功能在 v0.50.0（09-11）加入，管理员可以关闭。目标站点看到的是设备 IP，私有和 VPN 地址仍默认阻止。
- **团队网络客户端：** Enterprise 用 Team Setup Scripts 在每台计算机上安装组织自己的网络客户端。文档以 Tailscale 为已验证的配置。

Cursor 不安装、不运营也不监控客户的网络客户端。

### 身份与代理的兼容问题

- **设备信任规则：** 计算机是未加入 MDM 的 Linux 机，不运行 Okta FastPass 等设备信任代理，要求受管设备的身份提供方规则会在计算机的浏览器中失败。官方建议加一条只针对非受管 Linux 会话的规则，见[文档：配置身份与访问]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-identity" >}})。
- **TLS 检查网关：** 桌面应用同时连接 `*.cursor.sh` 和计算机的嵌套主机名 `*.*.cursorvm.com`。只放行前者的网关会让「计算机设置挂起，聊天有时仍可用」，见[文档：配置 TLS 检查代理]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-proxies" >}})。

推断：这些限制说明计算机的形态是 Cursor 统一维护的云端 Linux 机，企业能做的是在其上叠加脚本和网络配置，不能把它纳入自己的设备管理体系。对要求设备合规或数据不出境的组织，这是部署前要先评估的条件。

## 实测中的表现与问题

社区资料中与运行环境有关的观察都是个案，没有官方的可用性或并发数据。

- **可以通过部分网站的机器人检查。** Pat Simmons 用同一个订机票任务测试三款产品，Muse 和 Dots 被 FlightHub 的机器人检查拦住，「Grok Bot 直接通过，就像它在另外两个被拦时进入 Amazon 那样」，见[Pat Simmons：Grok、Muse、Dots 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})。
- **托管式 Cloudflare 挑战会卡住。** 一位开发者分析 Grok Bot 的 Web Bot Auth 签名机制时写道，云端浏览器环境「补丁打得不够」，遇到托管式 Cloudflare 挑战时「往往」陷入无限循环，见[冒充 Grok Bot]({{< relref "/docs/grok-bot/sources/community/2026-10-07-nightd-impersonating-grok-bot" >}})。同文披露，签名进程的凭证可以从进程环境变量中读出，详见安全主题。
- **Bot 多了会变慢。** 一位投资人用户的分享中提到，Bot 市场里的 Bot「没有各自独立的电脑，数量一多就会变慢」，见[特工宇宙：投资人的日常]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})。
- **6 个 Bot 并行时不稳定。** 一篇汇总海外案例的文章转述一位 Reddit 用户部署 6 个 Bot 的经历：浏览器配置文件会重置，账户需要重新登录，有时浏览器崩溃、运行中的任务中断，多个 Bot 没有按预期稳定并行，第一天就用掉约 42% 的每周额度，见[十个海外案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})。该文是对 Reddit 截图的二手转述，没有原帖链接。
- **计算机操作环节失败过。** Claire Vo 的四款智能体对比中，「操作员层（operator layer）则没那么可靠：计算机操作功能坏了」，作者需要介入，见[ChatPRD：四款智能体九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})。这里的计算机操作指测试框架驱动各产品的方式，不是 Grok Bot 自身的计算机。
- **配置被认为较高。** Datawhale 的作者称「这台电脑的配置确实也非常高」，并把这一点与较高的价格联系起来，见[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})。资料中没有具体规格。

推断：浏览器配置文件重置、并行变慢、屏幕被占满导致操作失败（更新日志中的那条修复），都指向同一个设计取舍：一个用户的所有 Bot 挤在一台计算机上。官方后续的修复集中在登录状态保留、屏幕释放和崩溃恢复，与这些报告的问题对得上，但资料不足以判断问题是否已经解决。

## 资料缺口

- 计算机的规格：CPU、内存、磁盘容量、屏幕数上限；官方没有公布，社区只有「配置很高」的评价。
- 官方的休眠阈值和唤醒时间；目前只有 Piekarczyk 转述的「约两分钟」和鱼皮实测的「十几秒」。
- 后端架构的一手资料：Lee Robinson 演讲的原始视频或文字稿；目前只有 Piekarczyk 的转述加推测。
- 早期「每个 Bot 有自己的计算机」到「计算机按用户分配」，是表述变化还是架构变化；资料中没有官方说明。
- 多 Bot 并行的官方并发上限，以及 6 个 Bot 并行不稳定的一手报告（Reddit 原帖）。
- 云端浏览器被网站拦截的系统性测试；目前只有 FlightHub、Amazon 和 Cloudflare 的个案。

## 主要资料

**官方**

- [发布稿]({{< relref "/docs/grok-bot/sources/official/2026-08-11-introducing-grok-bot" >}})、[扩大到更多套餐]({{< relref "/docs/grok-bot/sources/official/2026-08-26-grok-bot-more-plans" >}})、[我们如何设计 Grok Bot]({{< relref "/docs/grok-bot/sources/official/2026-09-03-designing-grok-bot" >}})：早期「Bot 有自己的计算机」的说法，以及每账户约 50 个 Bot、每群 6 个的限制。
- [文档（docs.x.ai）：电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})、[常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})：计算机按用户分配、共享范围、持久化规则、三种维护操作。
- [文档（docs.x.ai）：对话与协作]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})：消息优先级。
- [文档：Grok Bot 概览]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-overview" >}})、[使用 Grok Bot 工作]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})：屏幕与并行、接管、恢复顺序。
- [文档：Grok Bot 安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})、[安全 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security-faq" >}})：Firecracker 微虚拟机、位于美国、不支持本地部署、休眠与备份。
- [面向 Teams 和 Enterprise 的 Grok Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})、[管理成员的计算机与数据]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-computers" >}})、[向组织部署]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-deployment" >}})：企业管理、Sudo、机密限制、镜像更新。
- [连接私有网络]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-private-networks" >}})、[配置 TLS 检查代理]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-proxies" >}})、[配置身份与访问]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-identity" >}})：出口 IP、私有网络、网关与设备信任的兼容问题。
- [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})：屏幕分辨率、休眠唤醒、持久性修复、保留期设置的时间线。
- [指南：Grok Bot 入门 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})：远程桌面式的接管。

**媒体**

- [Cybernews：Bot 把 CEO 银行数据泄露到 Slack]({{< relref "/docs/grok-bot/sources/media/2026-10-07-cybernews-bank-data-slack" >}})：引用官方「计算机分配给用户账号」的说明。
- [iThome 五款主动式智能体]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})：共享计算机的第三方概述。

**社区**

- [给 Grok Bot 发消息时实际发生了什么]({{< relref "/docs/grok-bot/sources/community/2026-10-14-peterp-what-happens-when-you-message" >}})：后端架构，转述 Lee Robinson 演讲并加作者推测。
- [冒充 Grok Bot]({{< relref "/docs/grok-bot/sources/community/2026-10-07-nightd-impersonating-grok-bot" >}})：云端浏览器环境与 Cloudflare 挑战。
- [ChatPRD：Claire Vo 试用 Grok Bot]({{< relref "/docs/grok-bot/sources/community/2026-08-18-chatprd-claire-vo-grokbot" >}})、[鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})：计算机的实际界面、唤醒、本机与云端的分工。
- [Pat Simmons]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})、[ChatPRD：四款智能体九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})、[特工宇宙]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})、[十个海外案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})：网站拦截、并行与稳定性的个案。
- [Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[AI 应用：Grok、Muse、Dots 对比]({{< relref "/docs/industry/sources/community/2026-11-01-aiyingyong-grok-muse-dots" >}})、[小企业 AI 智能体对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})、[Archie Li]({{< relref "/docs/industry/sources/community/2026-11-11-archieli-grok-bot-work-mode" >}})：第三方对共享计算机的理解，以及「每个 Bot 一台云主机」的误读。
