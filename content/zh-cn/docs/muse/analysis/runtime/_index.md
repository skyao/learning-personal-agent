---
title: "Meta Muse：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  每个用户一台云端 Linux 虚拟机，智能体跑在虚拟机内的容器里，凭证、审批、出站检查放在容器之外；计算按需拉起、空闲即回收，状态只靠一块 100 GB 加密卷延续。11 月起多了用户自己的 Chrome 和 Mac 两个本地执行面。
---

## 概要

- **一人一台云端虚拟机，智能体跑在容器里。** 官方称每个用户有一台专用的 Linux 虚拟机 Muse Secure VM，智能体和用户数据都在里面；harness（内部代号 Hatch）运行在虚拟机内的 systemd-nspawn 运行时容器（runtime cell）中，凭证代理、审批、出站检查 Sentinel 等服务放在容器之外。这一层次已有三份独立拆解和用户自己的实测相互印证，是同类产品中公开得最细的运行环境。
- **「常驻」是产品体验，计算并不常驻。** 实测显示虚拟机空闲几分钟到几十分钟就被回收，再次使用时冷启动一台新机器，挂上原来的加密用户卷；两天内换了 9 台、宿主 CPU 在 AMD 与 Intel 之间切换。跨机器延续的只有约 100 GB 的用户卷，配置是 2 vCPU、约 8 GB 内存，空闲内存被气球驱动大量回收。
- **环境对用户高度开放。** 用户可以看到命令、子智能体和浏览器，接管浏览器，安装软件，甚至打包导出整个根文件系统；Meta 称导出是「预期中的行为」。开放带来了可审计性，也让架构细节（以及攻击面）完全公开。
- **网页操作分两条路。** 默认是云端的 Chromium（独立租用的浏览器虚拟机，或回退到本机容器），出口在云与 CDN 网段，常被网站识别和拦截；2026-11-13 上架、11-20 正式宣布的 Chrome 扩展让 Muse 在用户自己的浏览器标签组里操作。Mac 应用则在本机读取文件和 Messages，形成云端为主、本地补充的混合结构。
- **隔离边界有两处公开的弱点。** 容器与虚拟机共享内核，第三方研究称内核逃逸后进程可经虚拟机自己的公网 IPv6 绕过 Sentinel；Meta 也写明当前设计不阻止 Meta 在运营必要时访问数据，承诺的 Confidential VM 截至 2026-11 仍未上线。

## 每个用户一台虚拟机，智能体在容器里

官方的说法从发布起没有变：[发布稿]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})称每位用户有一台专用虚拟机，「同时容纳智能体和个人的数据」，并自带浏览器；[安全架构文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})写明这是一台隔离的 Linux 机器，用于编译智能体写的代码、开发自定义技能、处理并发子智能体和定时任务，是用户放入 Muse 的一切内容的「记录系统」。各地上线稿沿用同一表述（[日本]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})、[澳大利亚]({{< relref "/docs/muse/sources/official/2026-11-17-muse-available-australia" >}})），[英国稿]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})改用更通俗的「就像一台只属于你的笔记本电脑」，并称信息和登录凭证不在 Meta 的其他服务里。Meta 高管 David Singleton 让用户把它看作「云端的免费计算机」（[The Verge]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}})）。

虚拟机内部的分层，官方文章与第三方拆解一致：

| 层 | 内容 | 出处 |
| --- | --- | --- |
| 宿主与虚拟化 | Linux 宿主 → KVM → Cloud Hypervisor（不是 Firecracker） | [Adwankar 拆解]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})、[NebuSec]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-inside-meta-muse" >}})、[用户实测]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}}) |
| 用户虚拟机 | Ubuntu，2 vCPU、约 8 GB 内存，无 GPU，PCI 设备全是 virtio | [用户实测]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})、[NebuSec]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-inside-meta-muse" >}}) |
| 运行时容器 | systemd-nspawn；容器内 root 映射为虚拟机中的非特权 uid 131072；过滤系统调用（无 io_uring）、去掉 CAP_SYS_PTRACE 和 CAP_NET_ADMIN | [安全架构文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})、[用户实测]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}}) |
| 容器内 | harness Hatch（327 MB 的 Rust 二进制，与系统镜像分开以「实时更新包」交付）、工作区文件、工具二进制 | [Adwankar 拆解]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})、[安全架构文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}}) |
| 容器外 | hatch-safety（审查输入输出）、privsep、hatch-authd（代管连接器凭证）、Sentinel（出站检查）、postgres 状态库、推理与遥测代理；容器内外经带对端校验的 Unix 套接字通信 | [安全架构文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})、[NebuSec]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-inside-meta-muse" >}})、[CodePick]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}}) |

模型推理不在虚拟机里，经代理发往外部（[CodePick]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})）；但发给模型的请求在用户虚拟机上本地组装，个人内容来自家目录下的 Markdown 文件（[PersonalAgentBench 拆解]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})）。手机、网页客户端经加密传输直连用户的虚拟机（[安全架构文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）；Adwankar 观察到每台虚拟机都有公开域名，手机经 Noise_XX 会话直连，他认为这是与 Claude Code 云端虚拟机「完全没有入站」相比最大的架构差异（[Adwankar 拆解]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})）。网站、App 和 WhatsApp 连到的是同一个智能体（[NebuSec]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-inside-meta-muse" >}})）。

工作区沿用 OpenClaw 的文件结构（SOUL.md、MEMORY.md、USER.md、IDENTITY.md 等），雷峰网据此称 Muse「就是给普通人用的 OpenClaw」；Nat Friedman 回应代码从零构建、产品上深受 OpenClaw 启发（[雷峰网]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})、[Peter James 导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})）。记忆文件的细节见[记忆与上下文]({{< relref "/docs/muse/analysis/memory" >}})。

## 计算按需拉起，状态靠一块加密卷延续

用户自己的实测（[VM 调研]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})，2026-10 上旬两天的观察）给出了官方没有公开的生命周期：

- **存储：** 四块盘中只有 100 GB、LUKS 加密、btrfs 格式、挂载为 `/home/hatch` 的用户卷是持久的；系统盘、容器镜像盘都是易失的。虚拟机被回收时这块卷摘下、挂到新机器上。Adwankar 与 NebuSec 的拆解给出相同的结构（[Adwankar 拆解]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})、[NebuSec]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-inside-meta-muse" >}})）。
- **回收：** 8 次释放都发生在空闲时，空闲约 3 到 28 分钟不等，没有固定阈值；有每 10 秒一次的写盘心跳时撑到 93 分钟，30 分钟一次的 cron 检查几乎不能续命；空闲 1 小时或隔夜必被回收。
- **拉起：** 两天内换了 9 台虚拟机，CPU 在 AMD EPYC 9D25、Intel Xeon 8321HC、AMD EPYC 9D64 之间无规律切换；新机器的拉起并不严格跟着用户消息。作者据启动记录推断恢复是冷启动，而不是内存快照。
- **内存：** 约 80% 的内存被 virtio-balloon 回收，实际可用约 1.5 GB。Adwankar 也观察到闲置机器只占约 2 GB 工作集，他推断这正是长期在线的按用户虚拟机能负担得起的原因（[Adwankar 拆解]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})）。

Adwankar 记录的另一面是机器池化：虚拟机以「无身份」状态预先启动，用户登录时把用户卷嫁接上去；发布新版本时换一台新机器，中断约 40 秒（13 秒到容器、约 40 秒就绪），家目录文件完好，虚拟机不能原地重启（[Adwankar 拆解]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})）。智能体安装的软件包记成清单，在新机器上重放，所以用户装的工具能跨替换保留。

其他来源的规格说法不一：PC Watch 作者实测为「4 核 EPYC、内存只有 8GB」（[PC Watch]({{< relref "/docs/muse/sources/media/2026-11-19-pc-watch-muse-zaurus-developer" >}})）；ITmedia 称存储官方未公布，有人调查约 100 GB（[ITmedia]({{< relref "/docs/muse/sources/media/2026-11-22-itmedia-muse-explainer" >}})）；Arcjet 从网站一侧看到的 Muse 浏览器报告 6 个逻辑 CPU、约 16 GB（有时 8 GB）内存，作者提醒这些值不稳定（[Arcjet]({{< relref "/docs/muse/sources/community/2026-10-14-detect-muse-ai-agent" >}})）。浏览器可能运行在另一台虚拟机上，这些数字测的不一定是同一台机器。

推断：官方和媒体讲的「7×24 小时在后台工作」，落到实现上是「状态常驻、计算按需」。后台任务由定时器唤醒新机器执行，用户感受不到回收；代价是冷启动延迟和对空闲判定的依赖。这也解释了第三方成本测算的分歧：Z Finance 转述的摩根士丹利模型按 2 vCPU、8GB 沙箱计价，并指出 24/7 常驻与「按需拉起 + 状态快照休眠」相差一个数量级（[Z Finance]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})）；海外独角兽讨论转述的同一机构估算 CPU 沙箱每用户每月 5 至 8 美元（[海外独角兽讨论]({{< relref "/docs/industry/sources/community/2026-10-23-haiwaidujiaoshou-discussion" >}})）。实测的回收行为更接近后一种模式。

## 环境对用户开放：看得见、接管得了、导得出

- **可见：** 用户在 App 里能看到它运行的命令、浏览器和启动的子智能体，Pat Simmons 认为 Dots 和 Grok Bot 展示得远不如它（[Pat Simmons 实测]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）；手机 App 有文件列表，可查看、下载虚拟机里的文件（[聚 AI 讨论]({{< relref "/docs/muse/sources/community/2026-10-04-juai-muse-discussion" >}})）。
- **可装可写：** Muse 有自己的文件系统、终端和完整浏览器，可以写代码构建工具（[设计文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})）；用户实测在里面装了其他 AI 的命令行工具（[Emma 实测]({{< relref "/docs/muse/sources/community/2026-11-25-emma-cli-ai-bridge" >}})），PC Watch 作者在里面搭了编译环境，又经 Tailscale 和 SSH 让它连到家里的机器做真机调试（[PC Watch]({{< relref "/docs/muse/sources/media/2026-11-19-pc-watch-muse-zaurus-developer" >}})）。用户说的 MCP 服务器，Muse 能在虚拟机里现写客户端接上，但只能连公开的 HTTPS 地址，够不到用户本机（[智能体互通]({{< relref "/docs/muse/sources/community/2026-11-17-agent-to-agent-interop" >}})）。
- **可导出：** 2026-09 两名开发者让 Muse 把整个根文件系统打包分享，压缩约 2.7 GB、解压 6.8 GB，含系统文件、内部文档、集成代码和子智能体日志（[Peter James 导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})、[The Verge]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}})）。Meta 称这不带来对 Meta 基础设施或他人数据的访问，Friedman 称是「预期中的行为」（[The Verge]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}})）。凭证文件读不出来，SSH 密钥被排除（[Future Society 自查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。
- **可清空：** 重置 Muse 会永久删除所有信息、聊天、文件和进行中的任务（[帮助：指导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})）。

开放的代价也来自同一处：产品不开源，但拆解者能从导出的文件里还原出几乎全部架构（[是否开源]({{< relref "/docs/muse/sources/community/2026-11-05-is-meta-muse-open-source" >}})）。镜像里的连接器管控配置自称「可见性管控，而不是能力边界」（[Future Society 自查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})），这类细节是安全研究的起点，见[安全]({{< relref "/docs/muse/analysis/security" >}})。

## 网页操作：云端浏览器为主，用户的 Chrome 为补充

**云端浏览器。** 官方称浏览器是真实、保持最新的 Chromium，运行在虚拟化层之后；驱动它的子智能体只看页面的无障碍树快照，不能在页面里运行 JavaScript，DevTools 被禁用；用户接管或凭证库填表时智能体暂停（[安全架构文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。用户可以「打开浏览器」旁观、「接管浏览器」、「停止任务」（[帮助：浏览网页]({{< relref "/docs/muse/sources/official/2026-09-08-help-browse-web" >}})）。拆解显示浏览器通常从专门的浏览器虚拟机池中租用，租期 15 分钟，容器没有直达浏览器代理的路径（[Adwankar 拆解]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})）；NebuSec 列出四种浏览器后端，按任务选择，后三种用 Chromium 155.0.8059.80（[NebuSec]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-inside-meta-muse" >}})）。远程浏览器每个网站都要单独登录，审批卡约 30 分钟后过期，可能让任务中途终止（[两个浏览器]({{< relref "/docs/muse/sources/community/2026-11-25-muse-two-browsers" >}})）。

云端运行的直接后果是出口 IP 在机房。DataDome 统计 99.3% 的 Muse 请求来自云与 CDN 基础设施（Cloudflare 81.2%、Fastly 18.1%），只有 0.6% 来自消费级网络（[DataDome]({{< relref "/docs/muse/sources/media/2026-10-15-datadome-muse-29-million-requests" >}})）；用户实测小红书封禁了 Muse 的机房 IP，视频号登录态只能维持一两天（[村长七天实测]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}})）；Muse 在 FlightHub 被机器人检查拦住后改经 Expedia 订票（[Pat Simmons 实测]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。网站的封堵和 Meta 的应对见[连接器]({{< relref "/docs/muse/analysis/connectors" >}})。另一个副作用是购物者手机上的联盟 cookie 不在 Meta 托管的浏览器里（[Hello Partner]({{< relref "/docs/muse/sources/media/2026-11-12-muse-uk-affiliate-pixels-blind" >}})）。

**Chrome 扩展。** 2026-11-13 扩展被发现上架，11-20 Alexandr Wang 正式宣布，称已有 20 万人使用（[Wang 宣布扩展]({{< relref "/docs/muse/sources/media/2026-11-20-muse-chrome-extension-official-announcement" >}})、[扩展上架]({{< relref "/docs/muse/sources/media/2026-11-13-muse-chrome-extension" >}})）。Muse 在用户自己的 Chrome 侧边栏里工作，只能在专属标签组内操作，网站看到的是已登录的用户本人，所以不用重新登录，也不被当作智能体拦截；把标签拖出标签组即收回控制权（[两个浏览器]({{< relref "/docs/muse/sources/community/2026-11-25-muse-two-browsers" >}})，作者未安装实测）。

推断：扩展把执行从 Meta 的云挪到用户的机器上，绕开了机房 IP 的封堵，也把「隔离的虚拟机」这一卖点在网页操作上部分让渡给了用户的浏览器环境。两条路线的分工（低信任任务用远程浏览器、已登录的常用账户用扩展）目前只是社区建议，缺少实测。

## 本地执行面：Mac 应用与小设备

Mac 应用在用户电脑上查找、整理文件，读取 iMessage、备忘录、提醒事项、邮件和日历，需要 macOS 授予完全磁盘访问、自动化、通知三项权限；官方称完全磁盘访问覆盖所有文件，但智能体只用用户让它处理的部分（[帮助：Mac]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})）。2026-09-23 Connect 大会称 Mac 版可操作 Mac 上的任何应用（[Connect 2026]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})）。不开这些权限时，智能体仍从云端电脑处理邮件、日历和浏览（[Mac 权限提示]({{< relref "/docs/muse/sources/community/2026-11-19-apple-rewrote-mac-permission-screen" >}})）。安卓版沿用 OpenClaw 的说法，把手机称为「节点」，云端下命令、手机执行（[雷峰网]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})）。手表应用相当于云端 Muse 的遥控器（[手表与 Wear OS]({{< relref "/docs/muse/sources/community/2026-11-12-muse-on-apple-watch-wear-os" >}})）；Gadgets SDK 让 Raspberry Pi 等设备上可以部署常驻程序接收事件（[涂鸦技能]({{< relref "/docs/muse/sources/community/2026-11-12-tuya-cloud-devices-skill" >}})）。设备细节见[设备]({{< relref "/docs/muse/analysis/devices" >}})。

## 隔离边界与 Meta 自身的访问

官方的隔离主张有两层：别的用户的智能体碰不到你的虚拟机；容器里的智能体碰不到凭证和出站通道。第三方研究对后一层提出了具体的反例：容器与虚拟机共享内核，内核逃逸后直接运行在虚拟机里的进程不受 cgroup 出站挂钩约束，可经虚拟机自己的公网 IPv6 绕过 Sentinel（[NebuSec]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-inside-meta-muse" >}})）；CSA 据此建议把出口管控放在虚拟机或宿主层（[CSA]({{< relref "/docs/muse/sources/community/2026-11-21-csa-sentinel-bypass-lessons" >}})）。已公开的事件有：漏洞赏金发现可触及用户虚拟机的漏洞，Meta 评为 SEV-2；404 Media 报道上线前（2026-08-27 至 09-18）因 KVM 逃逸报告激增紧急修复（[Secure VM 攻击面]({{< relref "/docs/muse/sources/community/2026-11-05-muse-secure-vm-attack-surface" >}})、[404 Media]({{< relref "/docs/muse/sources/media/2026-10-05-404media-vm-escape-before-launch" >}})）。漏洞赏金把 Linux 内核公开漏洞披露后 30 天内的报告排除在外（[赏金规则]({{< relref "/docs/muse/sources/official/2026-11-04-bug-bounty-payout-guidelines" >}})）。

对 Meta 自身，官方写明当前设计「并不阻止 Meta 在为支持、保护或运营该服务所必需时访问数据」，员工访问靠政策限制（[Secure VM 攻击面]({{< relref "/docs/muse/sources/community/2026-11-05-muse-secure-vm-attack-surface" >}})）。发布时预告的 Muse Confidential VM（用户持钥，Meta 也看不到）定在「今年晚些时候」（[安全架构文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）；10 月有人在网页设置里看到未完成的入口，截至 2026-11 的资料中仍未上线（[iFynx]({{< relref "/docs/muse/sources/community/2026-09-16-ifynx-muse-secure-vm" >}})）。这部分与[安全]({{< relref "/docs/muse/analysis/security" >}})、[隐私]({{< relref "/docs/muse/analysis/privacy" >}})交叉。

## 与其他跟踪产品的差别

| 产品 | 执行环境 | 与 Muse 的主要差别 | 出处 |
| --- | --- | --- | --- |
| Muse | 每用户一台 Linux 虚拟机，智能体在容器内；另有 Chrome 扩展、Mac 应用 | — | 上文 |
| Grok Bot | 每账户一台共享云电脑，所有 Bot 共用文件、浏览器会话和登录 | Muse 是单智能体，不存在多 Bot 共享凭证的问题 | [四款入门成本]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})、[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}}) |
| Dots | 每个 dot 一台云电脑，可选连接用户本机 | 路线最接近；Dots 可借用户 Chrome 绕过拦截，Muse 到 11 月才有扩展 | [四款入门成本]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})、[Pat Simmons 实测]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}}) |
| Claude Duet | 自己的云电脑，用户看不到也不能接管浏览器 | Muse 的可见性和接管能力明显更强 | [四款入门成本]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}}) |
| Gemini Spark | iThome 称每项任务一台临时虚拟机（未注出处） | Muse 的状态跨任务保留在用户卷中 | [iThome]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}}) |

在 2026-11 的四款 20 美元档对比中，作者称 Muse 是唯一自带常驻电脑、不依赖用户笔记本或桌面应用的一款（[20 美元四家]({{< relref "/docs/industry/sources/community/2026-11-22-four-agents-twenty-dollars" >}})，作者未实测）。从上面的实测看，「常驻」指的是状态，不是计算。

## 资料缺口

- 官方规格与运营参数：CPU、内存、存储配额，空闲回收阈值，冷启动延迟，并发子智能体上限，长任务超时。目前全部来自拆解和用户实测，且观测时间集中在 2026-09 至 10 月。
- 浏览器虚拟机池的规模、租用失败时的行为、出口 IP 分配；Chrome 扩展的权限模型与实测（目前只有商店页和帮助中心的转述）。
- Muse Confidential VM 的上线时间与设计；虚拟机隔离的独立审计；Meta 对 NebuSec 内核逃逸与 IPv6 出站研究的回应。
- 长期使用中的环境稳定性：用户卷损坏、软件包重放失败、版本滚动时任务中断的记录。

## 主要资料

官方：
- [How We Built Safety Into Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})：虚拟机、运行时容器、容器外服务、浏览器设计的一手说明。
- [发布稿]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})、[设计文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})：Secure VM 的定位与「自己的计算机」。
- [帮助：浏览网页]({{< relref "/docs/muse/sources/official/2026-09-08-help-browse-web" >}})、[帮助：Mac]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})、[帮助：指导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})：浏览器接管、Mac 权限、重置。
- [英国上线]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})、[赏金规则]({{< relref "/docs/muse/sources/official/2026-11-04-bug-bounty-payout-guidelines" >}})：最新的官方表述与隔离边界的赏金范围。

媒体：
- [The Verge]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}})：根文件系统导出与 Meta 的回应。
- [DataDome]({{< relref "/docs/muse/sources/media/2026-10-15-datadome-muse-29-million-requests" >}})：浏览器流量来源构成。
- [PC Watch]({{< relref "/docs/muse/sources/media/2026-11-19-pc-watch-muse-zaurus-developer" >}})：规格观察与经 SSH 外连家用设备的开发实测。
- [Wang 宣布扩展]({{< relref "/docs/muse/sources/media/2026-11-20-muse-chrome-extension-official-announcement" >}})、[雷峰网]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})：Chrome 扩展；与 OpenClaw 的结构对照。

社区：
- [Adwankar 拆解]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})：Cloud Hypervisor、四块盘、池化与滚动更新、浏览器租用。
- [NebuSec]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-inside-meta-muse" >}})、[CSA]({{< relref "/docs/muse/sources/community/2026-11-21-csa-sentinel-bypass-lessons" >}})：执行层级、四种浏览器后端、出站绕过。
- [Peter James 导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})、[Future Society 自查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})、[PersonalAgentBench 拆解]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})：导出内容、权限边界、请求组装。
- [两个浏览器]({{< relref "/docs/muse/sources/community/2026-11-25-muse-two-browsers" >}})：云端浏览器与 Chrome 扩展对照。
- [Secure VM 攻击面]({{< relref "/docs/muse/sources/community/2026-11-05-muse-secure-vm-attack-surface" >}})：已公开的隔离失效记录与 Meta 自身的访问。

实测：
- [Muse VM 调研]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})：用户 2026-10 上旬的实测，规格、持久卷、9 次替换、回收与拉起规律。
