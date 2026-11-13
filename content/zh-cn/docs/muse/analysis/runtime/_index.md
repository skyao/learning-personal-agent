---
title: "Meta Muse：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  每位 Muse 用户有一台 Meta 云端的专用 Linux 虚拟机（Muse Secure VM），智能体本体 Hatch 跑在其中的 systemd-nspawn 容器里，凭证、审批与出站控制放在容器之外；实测显示虚拟机空闲即回收、按需冷启动，只有 100 GB 的用户盘跨实例保留。
---

## 概要

- 官方称每位用户一台隔离的云端 Linux 虚拟机 Muse Secure VM，带文件系统、终端和真实的 Chromium 浏览器，App 关闭后继续工作；它既是智能体的执行环境，也是用户内容的「记录系统」。
- 虚拟机内部是两层边界：智能体框架 Hatch 和所有工具运行在 systemd-nspawn「运行时单元」（runtime cell）里，凭证服务、安全分类器、Sentinel、数据库、推理代理作为独立服务放在单元之外。官方安全文章、漏洞赏金指南和用户实测三方说法一致。
- 用户实测（2026-10）看到的规格是 2 vCPU、8 GB 内存、100 GB 用户盘、无显卡，但内存气球回收了大部分内存；两天内 VM 被替换 9 次，空闲几分钟到半小时即释放，靠冷启动恢复，只有挂在 `/home/hatch` 的用户盘跨实例保留。官方没有公布这些机制。
- 环境对用户相当透明：用户可以看系统文件、活动日志，打开、接管或停止浏览器；多名用户和记者让 Muse 把整个根文件系统打包导出，Meta 称这不涉及基础设施或他人数据。这也引出了 VM 逃逸、文件导出等安全问题（见[安全]({{< relref "/docs/muse/analysis/security" >}})）。
- 云端运行的代价是机房 IP 被部分网站屏蔽、文件不在用户本机。Meta 宣布过「机密虚拟机」（Muse Confidential VM），截至 2026-11-12 的资料仍是未来时。Mac 应用是另一条在用户本机执行的路径。

## 每个用户一台云端虚拟机

发布稿称 Muse 运行在 Muse Secure VM 上，这是「专用的虚拟机（VM），同时容纳智能体和个人的数据」（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})）。安全工程文章写得更具体：每位用户一台隔离的 Linux 机器，带浏览器，有足够的存储、CPU 和内存来编译智能体写的代码、开发自定义技能、处理并发的子智能体和定时任务；用户与 Muse 共享这台计算机，它是用户内容的记录系统。iOS、Android、网页客户端通过安全传输层直接连到用户的 VM（[我们如何为 Muse 构建安全]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。帮助中心称 Meta 另外维护备份，防止智能体历史丢失（[帮助：隐私、安全与保障]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})）。日本、新加坡上线稿沿用同样说法，并写明 VM 存放所连接服务的数据和认证信息（[日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})、[新加坡上线]({{< relref "/docs/muse/sources/official/2026-10-27-singapore-launch" >}})）。

高管的说法偏向「一台电脑」：据 The Verge，David Singleton 说用户应把 Muse 看作「云端的免费计算机」，能做放在桌下的计算机能做的几乎任何事（[Verge：文件系统下载]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}})）。TOP5 榜单称有高级用户已往 VM 里装了 Claude Code，这是转述，没有逐条出处（[TOP5 榜单]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。

内部名称是 Hatch。官方文章、Verge 和多份文件系统导出都写明 Hatch 是 Muse 在代码库中的名字；用户实测看到的镜像名为 `hatch-image`，版本 0.1.46（[用户实测：Muse VM 调研]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。

## 虚拟机里的两层边界

官方安全文章把一台 VM 描述为「一台机器上的两个隔离的安全域」：

| 层 | 内容 | 资料 |
| --- | --- | --- |
| 运行时单元（runtime cell） | Hatch 框架、工作区文件系统、所有工具二进制；systemd-nspawn 容器，自带 Debian 根文件系统和虚拟网卡；单元内 root 映射为宿主的非特权用户；过滤系统调用（无 io_uring），去掉 CAP_SYS_PTRACE、CAP_NET_ADMIN 等能力 | [安全工程文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}}) |
| 单元之外的系统服务 | hatch-safety（分类器）、privsep、hatch-authd（凭证）、Sentinel、postgres（持久化应用状态）、推理与遥测代理；与单元之间走 Unix 域套接字，用 SO_PEERCRED 和对端 ACL 鉴别 | 同上 |

漏洞赏金指南从攻击者角度重述了这一划分：用户在自己的沙箱内「按照设计」拥有 root；持有凭证、执行批准和出站控制的进程在沙箱之外；整个安全模型依赖 VM 与生产环境和其他用户隔离、凭证保护、出站控制、敏感操作人工批准四项控制（[漏洞赏金指南]({{< relref "/docs/muse/sources/official/2026-11-04-bug-bounty-payout-guidelines" >}})）。

用户实测与官方描述一致：容器内只有 7 个进程，hatch 约占 213 MB 常驻内存；容器内 uid 0 映射到宿主 uid 131072；容器通过 Unix 套接字访问推理代理、postgres 和疑似 gatekeeper 的 `gk-proxy`（[用户实测]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。Peter James 的导出中，`/opt/hatch/runtime-cell/` 有 18 个文件，用 systemd-nspawn 启动根文件系统（[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})）。镜像里带有 Codex CLI，但作者只找到 Muse 借用它捆绑的 bubblewrap 沙箱跑 ffmpeg（无网络、用户 nobody），没有调用 Codex 的证据（同上）。

CodePick 的分析提醒，容器里看不到某个服务不能证明它在另一台机器上，作者没有登录 VM，也没有完整执行日志（[CodePick：架构分析]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})）。Future Society 引用内部注释称，一条 setuid 提权路径靠每次启动打补丁缓解，对容器隐藏某二进制只是「可见性管控而非能力边界」（[Future Society：泄露 VM 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。

推断：两层设计把「用户可完全控制的执行环境」和「持有密钥与审批权的服务」分开，这样即使智能体或用户在单元内拿到 root，也不能直接动用凭证或绕过出站审查。上线前的 VM 逃逸事件说明外层边界同样是攻击目标，详见[安全]({{< relref "/docs/muse/analysis/security" >}})。

## 实测规格：按需拉起，用户盘单独保留

官方只说资源「足够」，具体规格来自一份用户实测（2026-10-12 整理，迁移自旧笔记；[用户实测]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）：

| 项目 | 实测 |
| --- | --- |
| 虚拟化 | Cloud Hypervisor，9 个 PCI 设备全为 virtio |
| CPU / 内存 | 2 vCPU；8 GB（可见约 7.7 GB），但 `/proc/meminfo` 中 Balloon 约 6.2 GB，作者估算宿主回收约 80%，实际可用约 1.5 GB |
| 磁盘 | 系统盘约 7.4 GB、疑似镜像盘约 7.5 GB、用途未知的小盘、100 GB 用户盘（btrfs，挂在 `/home/hatch`） |
| 图形 | 无桌面，只有 Xvfb 供无头 Chromium 渲染 |
| 生命周期 | 两天内 9 次 VM 替换，CPU 在 AMD EPYC 9D25、Intel Xeon 8321HC、AMD EPYC 9D64 之间切换；8 次释放都在空闲时，空闲时长从约 2 分钟到 28 分钟不等，开 10 秒心跳的一台撑了 93 分钟 |

作者据此推断：VM 暂停和恢复是冷启动新实例，不是内存快照（跨 CPU 厂商无法恢复内存快照）；100 GB 用户盘是「唯一跨 VM 替换存活的盘」，即状态与计算分离；释放没有固定阈值，可能与宿主资源紧张有关。这些是单一用户在一个时间段的观察，Meta 未公布回收策略。Future Society 与 Peter James 的导出测到根文件系统约 7–7.9 GB（解压），与实测的系统盘量级一致（[Future Society]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})、[Peter James]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})）。

推断：「App 关了它还在干」与「空闲几分钟就释放」并不矛盾。从实测看，持续存在的是用户盘上的状态和调度，计算实例按需拉起。成本侧的测算也支持这种做法：ZFinance 转引摩根士丹利研报，假设每用户一台 2 vCPU、8 GB 的隔离沙箱，按 AWS 约每小时 0.1217 美元计价；文章另外推演 24/7 常驻与「按需拉起＋状态快照休眠」的成本差距，这是文章作者的推演，不是 Muse 的披露（[ZFinance：齐俊元融资]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})）。单用户成本数字见[商业与规模]({{< relref "/docs/muse/analysis/business" >}})。

## 环境里有什么

**浏览器。** 帮助中心称聊天里有一个「你和 Muse 都可以控制」的浏览器，用户可打开查看、接管（暂停 Muse）或停止任务（[帮助：浏览网页]({{< relref "/docs/muse/sources/official/2026-09-08-help-browse-web" >}})）。安全文章说明这是保持最新的真实 Chromium，由专门的浏览器子智能体通过独立 broker 管理 CDP 连接；子智能体只看无障碍树快照，不能执行 JavaScript，DevTools 禁用；用户接管或凭证库填表时智能体暂停（[安全工程文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。Meta 称没有 API 的服务，智能体「可以像你一样通过浏览器使用」（[GeekWire：亚马逊拦截]({{< relref "/docs/muse/sources/media/2026-09-20-geekwire-amazon-blocks-muse" >}})）。阿里千问算法负责人把这概括为让 AI「像人一样通过 GUI 使用现有互联网服务」，与千问优先走 MCP/API 的路线相对（[InfoQ：千问]({{< relref "/docs/industry/sources/media/2026-11-08-infoq-qwen-personal-agent" >}})）。

**文件、终端与工具。** 设计文章称 Muse 有自己的计算机、文件系统、终端和完整浏览器，可以写代码、填表、预订和购买，产出文档、PDF、网页等 Artifacts（[我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})）。上传与生成的文件存在 VM 的系统文件中，可在资料库管理（[帮助：管理数据]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）。技能由 Meta 内置、自动调用（[帮助：技能]({{< relref "/docs/muse/sources/official/2026-09-08-help-skills" >}})）；Future Society 的引导对话中看到 62 个捆绑技能（[Future Society]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。11 月推出的 Spaces 让 Muse 在 VM 上搭出迷你应用并放进 App 标签栏；导出的文件系统里已有 Spaces 的 TypeScript/React/SQLite/Bun 模板（[Peter James]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})、[TechCrunch：Spaces]({{< relref "/docs/muse/sources/media/2026-11-06-techcrunch-muse-spaces" >}})）。

**主目录。** `/home/hatch` 里有 SOUL.md、IDENTITY.md、USER.md、MEMORY.md 等人格与记忆文件（记忆机制见[记忆与上下文]({{< relref "/docs/muse/analysis/memory" >}})）。雷峰网据此和安卓安装包的静态分析认为 Muse 与 OpenClaw 内核同构；Nat Friedman 回应称代码从零构建、产品上「深受 OpenClaw 启发」（[雷峰网：OpenClaw 血缘]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})）。

## 多任务与子智能体

官方称 VM 能处理并发的子智能体和定时任务，Muse 不是一问一答，用户无需等回复即可追问（[帮助：开始使用]({{< relref "/docs/muse/sources/official/2026-09-08-help-get-started" >}})）。Peter James 的导出中 `agents/` 目录有 113 条带 JSONL 轨迹的子智能体记录；CodePick 据 Muse 自报的 schema 称子任务以父任务对话为起点、之后各自推进（[Peter James]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})、[CodePick]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})）。安卓包和网页的状态栏显示「3 个子智能体工作中」这类提示（[雷峰网]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})）。一档播客的讨论者则称 Muse 内部只有前台沟通与后台执行两个进程、「没有 Subagent 概念」（[聚 AI 播客]({{< relref "/docs/muse/sources/community/2026-10-04-juai-muse-discussion" >}})），与上述导出和官方说法不符，应视为讨论者对界面的理解。

后台执行有用户实测佐证：AI Agents Library 作者 9 月 27 日布置研究任务后立即关掉 App，回来时报告已完成（[AI Agents Library：Duet 对 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）。定时任务和主动行为见[持续执行]({{< relref "/docs/muse/analysis/continuous-execution" >}})。

## 环境的透明度：可看、可导出

官方允许用户浏览系统文件和活动日志，活动日志按时间记录操作、授予的权限和用过的技能（[帮助：引导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})）。Pat Simmons 的对比实测称能看到 Muse 运行的每条命令、浏览器和启动的子智能体，Dots 与 Grok Bot「远不如它」（[Pat Simmons 实测]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。

上线后两周内，多人让 Muse 打包导出自己的 VM：Peter James 拿到压缩约 2.7 GB、解压 6.8 GB 的根文件系统，含内部文档、集成代码和 SSH 密钥文件，未验证密钥是否有效（[Peter James]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})）；The Verge 记者复现，Muse 起初拒绝，出示先例后改口。Meta 发言人称这「就像看笔记本里的文件」，不带来对 Meta 基础设施或他人数据的访问，并称可获取的信息量会随更新变化（[Verge]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}})）。2026-10-12 的用户实测仍能导出系统提示词副本和 29 个技能文档（[用户实测]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。

推断：官方把 VM 定义为「用户与 Muse 共享的计算机」，用户可见全部文件在设计上是一致的；被导出的主要是 Meta 自己的提示词、技能和框架代码，问题落在知识产权与攻击面，而不是用户数据隔离。

## 云端运行的限制

- **IP 与反爬。** 有用户报告 Muse 云电脑是机房动态 IP，小红书封禁该 IP 段，视频号登录态只能维持一两天（[村长：七天自动化]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}})）。Pat Simmons 的订票任务中 Muse 被 FlightHub 机器人检查拦住，改走 Expedia 完成（[Pat Simmons]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。平台层面的拦截见[连接器]({{< relref "/docs/muse/analysis/connectors" >}})。
- **文件不在本机。** 同一用户为把视频传回本地，自建了 Cloudflare 中转存储，并把 API Token 交给 Muse（[村长]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}})）。另有实测称完成的文件难找（[AI Agents Library]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）。
- **不能自托管。** Muse 的智能体、应用和 VM 全部闭源，只在 Meta 基础设施上运行（[Muse 开源吗]({{< relref "/docs/muse/sources/community/2026-11-05-is-meta-muse-open-source" >}})）。社区观点把这概括为「数据和记忆都放在厂商的云上」（[鱼皮：大厂为何做 Personal Agent]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})）。

## 机密虚拟机与 Mac 本地执行

帮助中心称可选的 Muse Confidential VM 仍在设计中，目标是「甚至对 Meta 也保密」（[帮助：隐私、安全与保障]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})）。Zuckerberg 在访谈中称与 Nat Friedman 一起招募了 Moxie Marlinspike 开发这一机密虚拟机（[Sources：Zuckerberg 谈 Muse]({{< relref "/docs/muse/sources/media/2026-09-08-sources-zuckerberg-on-muse" >}})）；Wired 转述 Meta 称将在「今年晚些时候」推出（[Wired：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})）；iThome 写作「用户自带加密金钥」（[iThome：五款主动智能体]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。截至 2026-11-08 的社区资料仍指出发布页用的是未来语气（[阿彦：从产品到架构]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})），资料中没有上线记录。

Mac 应用是云端 VM 之外的执行路径：帮助中心称 Muse 可在用户电脑上查找、整理文件，读取 iMessage、备忘录、提醒事项、邮件、日历等本地应用（[帮助：Mac]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})）。Muse Gadgets 的 Linux Device SDK 也能把树莓派等机器变成执行自定义命令的「小设备」（[Gadget SDK]({{< relref "/docs/muse/sources/official/2026-10-02-muse-gadget-sdk-readme" >}})）。本地设备的分工见[设备]({{< relref "/docs/muse/analysis/devices" >}})。

## 资料缺口

- 官方的 VM 规格、配额、回收与恢复策略；单用户实测之外的独立验证。
- Muse Confidential VM 的上线时间、技术方案和是否默认开启。
- Mac 本地执行与云端 VM 之间如何分工、数据是否回传云端。
- 文件系统导出后 Meta 实际做了哪些限制（Verge 只有「会随更新变化」的表态）。
- 机房 IP 被网站屏蔽的范围，以及 Meta 是否有出口 IP 或身份声明方面的应对。

## 主要资料

- 官方：[我们如何为 Muse 构建安全]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})（两层边界、浏览器 broker）；[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})（Secure VM）；[帮助：隐私、安全与保障]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})（备份、Confidential VM）；[帮助：浏览网页]({{< relref "/docs/muse/sources/official/2026-09-08-help-browse-web" >}})（查看、接管、停止）；[漏洞赏金指南]({{< relref "/docs/muse/sources/official/2026-11-04-bug-bounty-payout-guidelines" >}})（沙箱内 root、四项控制）；[帮助：Mac]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})（本地执行）。
- 媒体：[Verge：文件系统下载]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}})（复现与 Meta 回应）；[雷峰网：OpenClaw 血缘]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})（静态分析）；[ZFinance]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})（沙箱成本假设）。
- 社区：[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})；[Future Society：泄露 VM 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})；[CodePick：架构分析]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})；[村长：七天自动化]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}})（IP 封禁、文件中转）；[Pat Simmons 实测]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})（透明度、反爬）。
- 实测：[Muse VM 调研]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})（规格、VM 替换与释放、用户盘）。
