---
title: "Meta Muse：设备"
linkTitle: "设备"
weight: 60
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Muse 在云端执行，终端只负责对话、确认和提供本地数据。截至 2026-11-12，已有手机、网页、iPad、Mac（可操作电脑）、Apple Watch 和 Wear OS；眼镜处于 Beta，专用硬件 Muse Charm 尚未发货。Meta 还开源了 Muse Gadgets SDK，并随订阅附赠 Home Link，用于连接家中设备。
---

## 概要

- 截至 2026-11-12，Muse 的终端是 iOS、Android、网页（muse.ai）、iPad（10 月）、Mac 测试版、Apple Watch 与 Wear OS（11-09）。手机和手表都只是对话与确认的入口，任务在云端执行；Android 手机和 Mac 还能成为云端可调用的本地执行端。
- Mac 应用支持计算机操作（Computer Use），需要完全磁盘访问、自动化、通知三项 macOS 权限。9 月这个客户端曾被公开过一个本地零日漏洞。
- AI 眼镜是官方最常提的方向（唤醒词、针对眼前所见的东西行动）。官方帮助中心已有「眼镜 Beta」说明，但 2026-11-10 的媒体稿仍称眼镜接入「尚未推出」，各方对上线状态的说法不一致。
- 专用硬件 Muse Charm 在 2026-09-23 Connect 上宣布，官方称「今年晚些时候」再公布细节。媒体称年底前或 12 月发货，价格未公布。
- Meta 在硬件上走了一条开发者路线：Muse Gadgets SDK 以 Apache 2.0 开源，配对需要 Meta 的 SDK 令牌。另有官方的 Muse Home Link，限美国，随有效订阅附赠，用来通过家庭 Wi-Fi 连接家中设备。

## 手机、网页与 Mac：执行在云端，终端负责入口和本地数据

发布时官方列出的客户端是 iOS、Android 和网页（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})）。Connect 时官方的说法是 Muse 目前在「手机、电脑和网页上把事情办成」（[Muse 登陆 AI 眼镜]({{< relref "/docs/muse/sources/official/2026-09-23-muse-on-ai-glasses" >}})）。之后陆续增加了几个终端：

| 时间 | 终端 | 资料 |
| --- | --- | --- |
| 2026-09-23 | Muse for Mac 支持计算机操作 | [Connect 2026 发布汇总]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}}) |
| 2026-10 | iPad 应用（据 TechCrunch，比手机首发晚约一个月） | [TechCrunch：手表]({{< relref "/docs/muse/sources/media/2026-11-10-techcrunch-muse-apple-watch-wear-os" >}}) |
| 2026-11-05 | 美国用户的实时语音与化身视频聊天，覆盖手机、网页与 Mac | [语音模式开启指南]({{< relref "/docs/muse/sources/community/2026-11-06-how-to-turn-on-muse-voice-mode" >}}) |
| 2026-11-09 | Apple Watch 伴侣应用（App Store 15.0 版）；据 Alexandr Wang 在 X 上称，Wear OS 同步上线 | [Muse 登陆 Apple Watch 与 Wear OS]({{< relref "/docs/muse/sources/media/2026-11-09-muse-apple-watch-wear-os" >}}) |

Mac 应用是从 Meta 网站下载的测试版，不在 Mac App Store 上架，没有版本记录（[语音模式开启指南]({{< relref "/docs/muse/sources/community/2026-11-06-how-to-turn-on-muse-voice-mode" >}})）。资料中没有 Windows 客户端，Ars Technica 称「奇怪的是，没有 Windows 版本」（[Ars Technica：零日漏洞]({{< relref "/docs/muse/sources/media/2026-09-21-arstechnica-muse-zero-day" >}})）。

社区资料把手机的角色描述为「接收要求和反馈」，任务在云端执行（[生活有变量：大厂防守]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}})）。在线运行环境的细节见[运行环境]({{< relref "/docs/muse/analysis/runtime" >}})。

### Android 手机作为「节点」

雷峰网对安卓安装包做了静态分析，结论是代码沿用 OpenClaw 的叫法，把手机称作「节点」：云端下命令，手机去执行。发短信时手机会弹窗「Muse 想用你的手机发送一条短信」，点一下即可放行，也可以设为始终允许（[雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})、[Muse 与 OpenClaw 拆解]({{< relref "/docs/muse/sources/community/2026-11-04-muse-openclaw-teardown" >}})）。基于泄露虚拟机文件的社区审查也提到，配对 Android 手机后，智能体可以读发短信、读取通知、搜索通话记录（[Future Society：泄露 VM 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。用户自己的虚拟机探索中，设备数据结构（device schema）包含配对设备同步来的联系人、日历事件、通话记录、上传会话等表（[用户实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。

iOS 方面，Tom's Guide 实测时让 Muse 读取了 iPhone 日历和健康数据（[Tom's Guide：自动化 10 项任务]({{< relref "/docs/muse/sources/media/2026-10-07-tomsguide-automate-10-tasks" >}})）。资料中没有 iOS 端对应「节点」的说明。

### Mac：计算机操作与三项系统权限

帮助中心写明，Mac 应用需要三项 macOS 权限：完全磁盘访问（Full Disk Access）、自动化（Automation）、通知（Notifications）。对消息、备忘录、邮件等在本地存储信息的应用，用户可以分别设为关闭、只读或读取并交互；发送邮件或购买前会先请用户确认，删除的文件移到废纸篓。要完全关闭计算机操作，需要在系统设置中移除这些权限，因为「这些权限由 macOS 设定和控制，而不是由 Meta 控制」（[帮助中心：Mac]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})）。

2026-09-21，安全研究者 Patrick Wardle 公开了 Muse macOS 客户端的本地零日漏洞（[Wardle：Not a Mused]({{< relref "/docs/muse/sources/community/2026-09-21-wardle-not-a-mused" >}})），Ars Technica 跟进报道（[Ars Technica：零日漏洞]({{< relref "/docs/muse/sources/media/2026-09-21-arstechnica-muse-zero-day" >}})）。另一篇分析称，问题出在一个未公开的 macOS 偏好键，它决定了语音听写的端点（[一个配置键就够了]({{< relref "/docs/muse/sources/community/2026-11-02-one-config-key-was-enough" >}})）。漏洞的经过与修补见[安全]({{< relref "/docs/muse/analysis/security" >}})。

推断：Mac 端同时拥有完全磁盘访问和本地漏洞记录，是 Muse 各终端中权限最大、暴露面也最大的一端。Top5Apps 的语音模式指南建议保持「执行前询问」，也说明了这一点（[语音模式开启指南]({{< relref "/docs/muse/sources/community/2026-11-06-how-to-turn-on-muse-voice-mode" >}})）。

### 手表：遥控与确认

Apple Watch 版把 Muse 形象放在全屏中央，提供通话、聊天、麦克风三个入口，另有表盘复杂功能。Meta 分享的截图示例中，Muse 告诉用户关注的影片已开票，给出 4:30、7:30 两个场次，用户确认后预订两张 7:30 的票（[Muse 登陆 Apple Watch 与 Wear OS]({{< relref "/docs/muse/sources/media/2026-11-09-muse-apple-watch-wear-os" >}})、[MacRumors：Apple Watch]({{< relref "/docs/muse/sources/media/2026-11-09-muse-apple-watch" >}})）。媒体指出，手表应用的设计与 Muse Charm 相似。

雷科技的判断是，手表适合承担长时间任务中的零散交互，但 Muse「还远没有获得完整的系统级权限」，对手表市场的短期影响有限（[雷科技]({{< relref "/docs/industry/sources/media/2026-11-10-leikeji-muse-smartwatch" >}})）。

## AI 眼镜：官方主推，上线状态说法不一

发布稿称 Muse「即将登陆 AI 眼镜」（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})）。Connect 上官方给出的时间是「未来几个月内」，设想的用法包括：说出智能体的名字激活，免手持；针对用户正看着的东西行动（货架上的商品、墙上的传单、学习用品清单）；指导锻炼、记录饮食、开车或做饭时预约；Muse 在后台工作，完成后再回来告知（[Connect 2026 发布汇总]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})、[Muse 登陆 AI 眼镜]({{< relref "/docs/muse/sources/official/2026-09-23-muse-on-ai-glasses" >}})）。官方同时提到眼镜上的「私密处理」（Private Processing），称不让包括 Meta 在内的任何人看到数据，但只有一句话。

据 AIVO 转述的 Meta 第三季度财报电话会，扎克伯格称 Muse 将「从 11 月开始登陆 Meta Glasses」（[AIVO：Muse 101]({{< relref "/docs/muse/sources/community/2026-11-04-muse-101-agentic-commerce" >}})）。

帮助中心「如何在你的 AI 眼镜上使用 Muse（Beta）」（页面创建于 2026-10-27）写明了 Beta 的边界（[帮助中心：眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})）：

- 需要同时使用 Meta AI 应用（配对、设置、固件）和 Muse 应用（对话）。
- 眼镜上「一次只有一个助手处于启用状态」，在 Meta AI 应用的设备设置中切换 Muse 和 Meta AI；部分音乐、通话、消息、导航功能暂不支持，需要切回 Meta AI。
- 可以给 Muse 起名并用「Hey 名字」唤醒，也可以说「Hey Meta」或「Hey Muse」；自定义名字和「Hey Muse」不是所有型号都支持。
- 系统检测到的误唤醒语音交互会在检测后 90 天内删除。位置数据的处理见[隐私]({{< relref "/docs/muse/analysis/privacy" >}})。
- Beta 参与者在 Beta 期间获得额外用量。

关于眼镜是否已经上线，资料的说法并不一致：

| 资料 | 说法 |
| --- | --- |
| [帮助中心：眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})（2026-10-27） | 眼镜上的 Muse「目前处于 Beta 阶段」 |
| [The Verge：语音模式上手]({{< relref "/docs/muse/sources/media/2026-11-05-muse-voice-mode-hands-on" >}})（2026-11-05） | 语音与化身将「很快」登陆 AI 眼镜 |
| [Muse 墨西哥上线]({{< relref "/docs/muse/sources/media/2026-11-05-muse-launches-mexico" >}})（2026-11-05） | 墨西哥的「眼镜已经运行由 Muse 驱动的助手」；同一篇又转述当地媒体称 Meta「计划增加」对眼镜的兼容 |
| [Muse Mail 向付费用户开放]({{< relref "/docs/muse/sources/media/2026-11-10-muse-mail-paid-subscribers" >}})（2026-11-10） | Connect 宣布的四项能力中，「眼镜接入尚未推出」 |

推断：比较一致的解释是，眼镜上的 Muse 截至 2026-11-10 只是少量用户参与的 Beta，没有正式上线；墨西哥那篇的「已经运行」可能指 Meta AI 助手，而不是 Muse 本身。资料不足以确认。

## Muse Charm：宣布了专用硬件，但未发货

官方在 Connect 上的描述是：一款可以放进口袋、专为与 Muse 交谈互动打造的趣味设备，搭载最先进的实时语音模型，「今年晚些时候我们将分享更多信息」（[Connect 2026 发布汇总]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})）。其他资料的描述：

- DataCamp 称它是「一款无需手机即可使用 Muse 的小型钥匙扣设备」（[DataCamp：Dots 与 Muse]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})）；Tom's Guide 称它是手掌大小的伴侣设备（[Tom's Guide：Muse 与 Dots]({{< relref "/docs/industry/sources/media/2026-09-30-tomsguide-muse-vs-dots" >}})）。
- 一场播客讨论中，参与者称 Charm 有两英寸屏幕、前后摄像头、语音与视频输入输出、5G 和 eSIM，赶在圣诞节发货（[聚 AI：深入讨论 Muse]({{< relref "/docs/muse/sources/community/2026-10-04-juai-muse-discussion" >}})）。这是讨论者的说法，官方资料中没有这些规格。
- 发货时间：The Verge 称「预计今年出货」（[The Verge：语音模式上手]({{< relref "/docs/muse/sources/media/2026-11-05-muse-voice-mode-hands-on" >}})）；Top5Apps 转述 Android Authority，称预计 12 月发货，尚无价格（[语音模式开启指南]({{< relref "/docs/muse/sources/community/2026-11-06-how-to-turn-on-muse-voice-mode" >}})）。
- 扎克伯格在第三季度财报电话会上把 Charm 与眼镜一起列为 Muse 将接入的设备（[36 氪：Muse 时刻]({{< relref "/docs/muse/sources/media/2026-10-27-36kr-muse-moment" >}})）。

The Verge 的一位作者用 50 美元的 Waveshare ESP32-S3 1.75 英寸触屏开发板（Meta 推荐的 Muse Gadget 方案之一）自制了一个 Charm 平替。初始状态基本不可用：Muse 把语音当成待转录的音频片段而不是指令，回复慢而且不出声，屏幕一次只显示几个词，只有一个 Jolly 形象，也不会自动发现智能家居设备。他认为响应延迟主要来自 Meta 的服务器，专用硬件的意义在于做手机做不到的事，「Muse 本身并不是买一块专用计算怀表的理由」。他不信任 Muse 接触自己的家庭网络，所以把设备放在访客 Wi-Fi 上（[The Verge：50 美元自制 Muse Charm]({{< relref "/docs/muse/sources/media/2026-10-31-verge-diy-muse-charm" >}})）。

播客讨论者也认为 Charm 本身「没有什么值得讲的」，价值在于 Muse、WhatsApp 与用户数据组成的闭环（[聚 AI：深入讨论 Muse]({{< relref "/docs/muse/sources/community/2026-10-04-juai-muse-discussion" >}})）。

## Muse Gadgets 与 Home Link：把家中设备接进来

### 开源的 Gadgets SDK

Muse Gadgets 是官方的自制设备方案：给 ESP32 开发板编程，或用 SDK 配置树莓派，把 Muse 连接到屏幕、按钮和传感器。SDK 和固件以 Apache 2.0 许可证开源，包括 ESP32 Device SDK、Linux Device SDK，以及手机端的 Muse Gadgets Test。配对需要 SDK 令牌，「每个小设备都需要一个令牌才能配对」。仓库还附有面向 Muse Code 等编程智能体的 AGENTS.md（[Gadget SDK README]({{< relref "/docs/muse/sources/official/2026-10-02-muse-gadget-sdk-readme" >}})、[Muse Gadgets 首页]({{< relref "/docs/muse/sources/official/2026-11-04-muse-gadgets-home" >}})）。首页推荐了树莓派、圆形 AMOLED 屏、电子墨水屏等项目，电视棒标为「即将推出」。

一篇社区文章指出，开源的范围有限：设备需要 Meta 的 SDK 令牌并受 Gadget SDK 条款约束，动画化身不在开源许可之内（[Muse 开源吗]({{< relref "/docs/muse/sources/community/2026-11-05-is-meta-muse-open-source" >}})）。

### Home Link：随订阅附赠的家庭网关

Muse Home Link 是 Meta 自己做的 USB-C 小设备，基于 ESP32-C5（RISC-V，240 MHz），配 8 MB PSRAM、8 MB 闪存、Wi-Fi 6，尺寸 35 × 42 × 10 mm，只运行官方固件，不能重新刷写。设置流程是在 Muse 应用中通过低功耗蓝牙配对、选择 Wi-Fi，再添加技能。之后 Muse 可以通过本地 HTTP API 访问家中的兼容设备，社区技能支持 Philips Hue、Sonos、Apple TV、Google Nest 音箱、Samsung 电视等。官方提醒，社区技能可能变化或失效，「不要在家庭安防、紧急情况或医疗需求等安全攸关的事情上依赖它们」。Home Link 仅限美国，随有效的 Muse 订阅附赠，每位订阅用户限领一个，10 月发货（[Muse Home Link]({{< relref "/docs/muse/sources/official/2026-11-04-muse-home-link" >}})、[Muse Gadgets 首页]({{< relref "/docs/muse/sources/official/2026-11-04-muse-gadgets-home" >}})）。

Home Link 的痕迹在正式公布前就出现过：9 月有用户导出的 Muse 文件系统中，有一份 `docs/devices/home_link.md`，描述一项「Meta Home Link 的实验性集成」（[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})）。The Verge 当时报道称 Meta 尚未宣布这项功能（[The Verge：文件系统下载]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}})）。

据 Tuya 新闻稿，Tuya Skill 把 Muse 能控制的范围从自制设备扩展到用户家中已联网的量产设备，但不开放门锁控制、实时视频、固件升级、网络配置和设备移除（[Tuya 云设备技能]({{< relref "/docs/muse/sources/community/2026-11-12-tuya-cloud-devices-skill" >}})）。其他设备接入方式（如 Tessie 控制汽车）属于技能与连接器，见[连接器]({{< relref "/docs/muse/analysis/connectors" >}})。

推断：Meta 在家庭设备上先做开发者与爱好者生态（开源 SDK、社区技能、随订阅送网关），而不是像眼镜那样做成官方整合的消费功能。安防和门锁这类高风险操作被明确排除在外。

## 远期形态与零散线索

- 人形机器人：据 NDTV 转述 The Information，Meta 与 Fourier 用三个月造出人形机器人原型 Max（约 48 公斤、约五英尺，运行 Nvidia Jetson Thor）。Meta 机器人部门把它看作 Muse 的一种可能的实体形态，CTO Andrew Bosworth 在内部也这样描述过。Meta 发言人称合作只用于内部研究，没有销售计划（[Meta 人形机器人 Max]({{< relref "/docs/muse/sources/media/2026-11-02-meta-max-humanoid-robot" >}})）。
- 泄露的界面字符串：社区审查在泄露的虚拟机文件中发现一项「Life Management」捆绑技能的描述，内容是根据用户全天的自言自语（ACS 眼镜转写）整理待办事项、提议需要批准的操作。实时语音配置中还有「Wearables」配置档和带图像拍摄分类器的「Reactive Image Capture Test」配置档。这些文件没有说明转写是否持续录音，也没有说明分类器的作用；Muse 的数据文档称语音输入由用户发起，没有后台监听（[Future Society：泄露 VM 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。这些是未发布功能的痕迹，不能当作计划。
- 家庭安防摄像头：CNBC 在发布日报道中称 Muse 可监控家庭安防摄像头画面（[CNBC：Meta 进军个人智能体]({{< relref "/docs/muse/sources/media/2026-09-08-cnbc-meta-pushes-into-personal-agents" >}})）。官方资料中没有对应说明，Tuya Skill 也不开放实时视频。

## 资料缺口

- 眼镜 Beta 的开放范围（地区、型号、人数），以及是否已经正式上线；眼镜上「私密处理」的技术说明（官方提到另有工程博客，未收）。
- Muse Charm 的官方规格、价格与发货日期；播客中「5G、eSIM、前后摄像头」说法的出处。
- iPad 应用的官方说明（目前只有 TechCrunch 一句话）；Wear OS 版的功能与上线范围（目前只有 Wang 的一句 X 帖转述）。
- iOS 端能否像 Android 那样作为本地执行「节点」；Android 节点的官方帮助文档。
- Windows 客户端的计划。
- Home Link 的实际发货情况与用户使用反馈；Tuya Skill 的官方（Meta 方）说明。

## 主要资料

- 官方：[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})；[Connect 2026 发布汇总]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})、[Muse 登陆 AI 眼镜]({{< relref "/docs/muse/sources/official/2026-09-23-muse-on-ai-glasses" >}})（眼镜、Charm、Mac 计算机操作）；[帮助中心：眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})（眼镜边界）；[帮助中心：Mac]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})（三项权限）；[Gadget SDK README]({{< relref "/docs/muse/sources/official/2026-10-02-muse-gadget-sdk-readme" >}})、[Muse Gadgets 首页]({{< relref "/docs/muse/sources/official/2026-11-04-muse-gadgets-home" >}})、[Muse Home Link]({{< relref "/docs/muse/sources/official/2026-11-04-muse-home-link" >}})（自制设备与家庭网关）。
- 媒体：[Muse 登陆 Apple Watch 与 Wear OS]({{< relref "/docs/muse/sources/media/2026-11-09-muse-apple-watch-wear-os" >}})、[TechCrunch：手表]({{< relref "/docs/muse/sources/media/2026-11-10-techcrunch-muse-apple-watch-wear-os" >}})（手表、iPad）；[The Verge：50 美元自制 Muse Charm]({{< relref "/docs/muse/sources/media/2026-10-31-verge-diy-muse-charm" >}})（Gadget 实测）；[Muse Mail 向付费用户开放]({{< relref "/docs/muse/sources/media/2026-11-10-muse-mail-paid-subscribers" >}})（眼镜未上线的说法）；[雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})（安卓「节点」）。
- 社区：[语音模式开启指南]({{< relref "/docs/muse/sources/community/2026-11-06-how-to-turn-on-muse-voice-mode" >}})；[Future Society：泄露 VM 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})、[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})（配对手机、Home Link 痕迹）；[Muse 开源吗]({{< relref "/docs/muse/sources/community/2026-11-05-is-meta-muse-open-source" >}})；[Tuya 云设备技能]({{< relref "/docs/muse/sources/community/2026-11-12-tuya-cloud-devices-skill" >}})。
- 实测：[VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})（2026-10-12，配对设备同步的数据表）。
