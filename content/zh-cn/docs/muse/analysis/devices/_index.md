---
title: "Meta Muse：设备"
linkTitle: "设备"
weight: 60
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  Muse 的智能体始终在云端虚拟机里运行，终端只是入口和本地数据的来源。截至 2026-11-28，手机、网页、Mac、iPad、手表和眼镜 Beta 已经可用；专用硬件 Muse Charm 只有官方发布和媒体报道，价格和发货日期都来自未证实的报道。
---

## 概要

- **执行在云端，终端负责三件事：入口、本地数据、本地动作。** 手机、Mac 把联系人、日历、通话记录、健康数据同步进云端虚拟机；Android 手机和 Mac 还能替智能体在本机执行动作。专用硬件 Muse Charm 带 5G，也只是连回云端的入口（[拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})的推断）。
- **Mac 和 Android 的本地权限最宽，事故也出在这两端。** Mac 应用要完全磁盘访问、自动化、通知三项权限，可以操作桌面应用。路透社复现，Muse 能在 Android 上借通知权限、在 macOS 上借辅助功能和截图读取 Signal 消息，同样的请求在 iPhone 上被拦住。之后 Apple 在 macOS 27.3 beta 2 改写了 Mac 的权限授予界面。
- **终端扩展很快，但都是「轻入口」。** 时间线：
  - 9-08 推出手机和网页，9-17 推出 Mac；
  - 约 10 月上旬推出 iPad 专用应用，10-27 起有眼镜 Beta 的帮助页，11-09 登陆 Apple Watch 和 Wear OS。
  
  手表和眼镜要依赖配对的手机，眼镜端还要切掉 Meta AI，而且音乐、通话、消息、导航都只部分支持。
- **专用硬件仍停在宣布阶段。** Muse Charm 由 Meta 在 2026-09-23 的 Connect 上发布；12 月发货、定价 300 美元、附赠 12 个月 5G，都出自媒体转述的未具名消息，Meta 没有证实。家庭网关 Home Link 随订阅附赠，仅限美国，The Verge 报道只做了 5,000 台。
- **Meta 也向开发者开放了设备一侧。** Muse Gadgets SDK 开源，每台小设备要凭 Meta 发的令牌配对。社区和涂鸦（Tuya）在这基础上把 Muse 接到量产的智能家居设备。官方没有开放智能体本身。

## 智能体在云端，终端是入口和数据源

官方称 Muse 帮用户「在手机、电脑和网页上把事情办成」（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})、[个人智能体登陆 AI 眼镜]({{< relref "/docs/muse/sources/official/2026-09-23-muse-on-ai-glasses" >}})）。几份拆解对分工的描述一致：智能体跑在 Meta 为每个用户配置的云端 Linux 虚拟机上，手机、网页、Mac 应用都是连到这台虚拟机的入口（[拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})，见 [运行环境]({{< relref "/docs/muse/analysis/runtime" >}})）。

终端的数据会进到虚拟机里。沙箱剖析和用户实测都看到了这些数据：
- 数据库的 `device` schema 存着配对设备同步来的通讯录、日历、通话记录和媒体上传（[Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})、[我的实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）；
- Tom's Guide 的实测读到了 iPhone 上的日历和健康数据，包括步数、锻炼、睡眠（[Tom's Guide：自动化实测]({{< relref "/docs/muse/sources/media/2026-10-07-tomsguide-automate-10-tasks" >}})）；
- 健康数据在 iPhone 上来自 Apple Health，在 Android 上来自 Health Connect（[健康数据连接细则]({{< relref "/docs/muse/sources/community/2026-11-15-health-data-permission-chain" >}})）。

终端也能替云端执行动作。雷峰网和社区拆解都发现，Android 版沿用 OpenClaw 的叫法，把手机叫作「节点」：云端下命令，手机执行（[OpenClaw 同源拆解]({{< relref "/docs/muse/sources/community/2026-11-04-muse-openclaw-teardown" >}})、[雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})）。Muse 自己文件系统里的文档写明，Android 配对后可以设闹钟、用用户自己的号码打电话、读发短信、读手机通知、搜索通话历史（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。

AIX财经的受访者称，Muse 目前主要靠云端，端云协同（轻量任务放在本地处理）是一种可能的方向，但受发热、内存和本地模型能力的限制（[AIX财经：共识还是泡沫]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})）。

推断：从上面几点看，终端在 Muse 里的价值主要是数据和权限，不是算力。所以本地权限的宽窄，决定了各端能做的事和风险有多大（见下一节）。

## Mac：计算机操作与宽本地权限

据社区整理，Mac 应用 2026-09-17 上线（[拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})、[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。Connect（9-23）上，Wang 介绍了 Mac 上的计算机操作：「你可以离开你的电脑，它会继续为你处理你排好的所有工作」（[TechCrunch：Connect 上的 Muse]({{< relref "/docs/muse/sources/media/2026-09-23-techcrunch-everything-new-muse" >}})）。资料里没有 Windows 版，Ars Technica 特意提了一句（[Ars Technica：Muse 零日漏洞]({{< relref "/docs/muse/sources/media/2026-09-21-arstechnica-muse-zero-day" >}})）。

帮助文档写明：
- 计算机操作需要 macOS 授予完全磁盘访问、自动化、通知三项权限；
- 消息、备忘录、邮件这类在本地存信息的应用，可以分别设为关闭、只读、读取并交互；
- 发邮件或购物前会先请用户确认；
- 要关掉计算机操作，得去 macOS 系统设置里撤销权限（[帮助：Mac 文件与应用]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})）。

Mac 是 Muse 争议最集中的终端：
- **iMessage 同步争议。** 9 月，Inc. 的 Jason Aten 称，Mac 应用同步了他本地的 Messages 数据库，截图里同步到了第 187,462 行。社区复盘指出，这件事只涉及桌面应用读取 `chat.db`，手机应用没有这条路径（[iMessage 事件详解]({{< relref "/docs/muse/sources/community/2026-10-01-did-muse-read-your-messages" >}})）。
- **听写端点可被篡改。** Wardle 发现，macOS 版的听写端点设置可以被非特权的本地进程修改（[Wardle：not-a-mused]({{< relref "/docs/muse/sources/community/2026-09-21-wardle-not-a-mused" >}})）。
- **借辅助功能读 Signal。** 据路透社，Muse 在 macOS 上结合辅助功能和截图工具读取 Signal 消息。Apple 当周的系统更新堵住了这条路径，大幅限制开发者在 Mac 上使用辅助功能，还引入了一套面向智能体的新权限（[路透：Muse 安全事故]({{< relref "/docs/muse/sources/media/2026-11-18-muse-early-safety-mishaps-surface" >}})、[Signal 限制截图防读取]({{< relref "/docs/muse/sources/media/2026-11-21-signal-screenshots-block-ai-agents" >}})）。
- **Apple 改写权限界面。** 社区整理称，Apple 2026-11-16 宣布 macOS 27.3 beta 2 为完全磁盘访问和相关 API 增加透明度：授权改为从列表里选应用，引导用户只授予特定文件夹，可以设成每次访问都询问，一个应用控制另一个应用时会显示指示器；已授予的权限继续有效（[苹果重写 Mac 权限提示]({{< relref "/docs/muse/sources/community/2026-11-19-apple-rewrote-mac-permission-screen" >}})）。

推断：Muse 是在 Apple 新权限落地之前上线的。Mac 端能做到什么程度，此后会受操作系统厂商的规则约束；macOS 27.3 正式版之后实际怎样，资料还没有覆盖。

## 手机：iPhone 与 Android 的权限差异

路透社和 Signal、AI Now Institute 的复现结果是：Muse 在 Android 上借推送通知权限读到 Signal 消息，同样的请求在 iPhone 上被拦截；而且这条路径不经过 Muse 自己的连接器（[路透：Muse 安全事故]({{< relref "/docs/muse/sources/media/2026-11-18-muse-early-safety-mishaps-surface" >}})、[Signal 消息与通知权限]({{< relref "/docs/muse/sources/community/2026-11-19-muse-signal-notification-permission" >}})）。路透社还报道，Android 版默认拥有访问推送通知的权限（[路透：Muse 安全事故]({{< relref "/docs/muse/sources/media/2026-11-18-muse-early-safety-mishaps-surface" >}})）。

推断：同一个产品在两种手机系统上能拿到的权限不同，Android 端的风险面更大。这一点和 Android「节点」能代打电话、读短信的能力一致。各端权限的完整对照，资料里没有。

## 平板与手表：同一个智能体的小屏入口

- **iPad：** TechCrunch 称，手表版上线距 iPad 专用应用约一个月（[上线手表双平台]({{< relref "/docs/muse/sources/media/2026-11-10-techcrunch-muse-apple-watch-wear-os" >}})）。资料里没有 iPad 应用的官方公告。
- **手表：** 2026-11-09，Wang 和 Muse 官方账号在 X 上宣布 Muse 登陆 Apple Watch 和 Wear OS（[登陆手表双平台]({{< relref "/docs/muse/sources/media/2026-11-09-muse-apple-watch-wear-os" >}})）。
  - **功能：** 可以通话、发消息、听写；Apple Watch 版有表盘复杂功能（[Muse 登陆 Apple Watch]({{< relref "/docs/muse/sources/media/2026-11-09-muse-apple-watch" >}})、[上线手表双平台]({{< relref "/docs/muse/sources/media/2026-11-10-techcrunch-muse-apple-watch-wear-os" >}})）。演示里，Muse 在手表上提醒用户关注的电影开票了，用户确认后它订了两张票（[登陆手表双平台]({{< relref "/docs/muse/sources/media/2026-11-09-muse-apple-watch-wear-os" >}})）。
  - **限制：** 社区核查称，手表应用要配对手机和 Muse 账号，没有任何来源提到手表能用蜂窝网络独立使用；Meta 也没有宣布能直接读取手表的传感器（[Muse 登陆手表核查]({{< relref "/docs/muse/sources/community/2026-11-12-muse-on-apple-watch-wear-os" >}})）。iOS 18、watchOS 9、Android 10 这些系统要求，以及 Wear OS 版尚待上架 Google Play 的说法，只出自二手来源 The Gadgeteer（[Muse 登陆手表核查]({{< relref "/docs/muse/sources/community/2026-11-12-muse-on-apple-watch-wear-os" >}})）。
  - **定位：** 雷科技认为，手表适合给持续数小时到数天的任务做零散交互，比如提醒和确认；但 Muse 远没有拿到系统级权限，对手表市场的影响未必很快显现（[雷科技：Muse 登上智能手表]({{< relref "/docs/industry/sources/media/2026-11-10-leikeji-muse-smartwatch" >}})）。

另据 The Information，Meta 把原定今年推出的自家智能手表推迟到 2027 年，以便集中精力做 Charm（经 [PYMNTS]({{< relref "/docs/muse/sources/media/2026-11-19-pymnts-muse-charm-price-300" >}}) 转述）。这条说的是 Meta 自家的手表硬件，与上面的 Apple Watch、Wear OS 应用是两回事。

## AI 眼镜：Beta 可用，替换而不是并存

2026-09-23 的 Connect 上，Meta 宣布「未来几个月」把 Muse 带到 Meta AI 眼镜上（[个人智能体登陆 AI 眼镜]({{< relref "/docs/muse/sources/official/2026-09-23-muse-on-ai-glasses" >}})、[Connect 2026 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})）：
- 说出名字即可唤醒，全程免手持；
- 可以针对眼前看到的东西行动，比如货架上的商品、墙上的传单；
- 示例有指导锻炼、记录饮食、预约、帮用户买下看到的商品。

扎克伯格在 Q3 财报电话会上称，Muse 从 11 月起登陆 Meta 眼镜（经 [Muse 101：智能体商务]({{< relref "/docs/muse/sources/community/2026-11-04-muse-101-agentic-commerce" >}}) 转述）。

眼镜版帮助页的日期是 2026-10-27，标为 Beta（[帮助：眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})）：
- 要同时用两个应用：Meta AI 应用负责配对、设置、固件和照片视频，Muse 应用负责对话；
- 眼镜一次只能启用一个助手，可以在 Muse 和 Meta AI 之间切换；
- 两个应用里连接的服务互不相通；
- 部分音乐、通话、消息、导航体验暂不支持，需要切回 Meta AI；
- 自定义唤醒名和「Hey Muse」不是所有型号都支持。

社区整理称，截至 2026-11-06，眼镜已经可以开启 Beta，距 Connect 约六周。作者没有实测硬件；他指出切换开关的作用是替换掉 Meta AI，不是两者并存；已连接的服务和权限都不会带过去，要在 Muse 里逐项重连（[眼镜端 Muse beta 解析]({{< relref "/docs/muse/sources/community/2026-11-09-muse-on-glasses-beta" >}})）。

开放地区的说法不一：
- 澳大利亚的官方稿写 AI 眼镜支持「即将推出」（[Muse 上线澳大利亚]({{< relref "/docs/muse/sources/official/2026-11-17-muse-available-australia" >}})）；
- 英国写「未来数月」（[英国第七个市场]({{< relref "/docs/muse/sources/media/2026-11-24-muse-launches-uk" >}})、[英国上线与监管协商]({{< relref "/docs/muse/sources/community/2026-11-24-muse-uk-launch-and-regulators" >}})）；
- 墨西哥一篇报道一边说眼镜「已经运行由 Muse 驱动的助手」，一边转述 Meta「计划增加」眼镜兼容，前后矛盾（[墨西哥上线]({{< relref "/docs/muse/sources/media/2026-11-05-muse-launches-mexico" >}})）。

眼镜 Beta 在哪些国家开放，资料都没有写明。

推断：眼镜版 Muse 现在是试用性质的替换方案：要放弃 Meta AI 的部分能力，还要在 Muse 里重新授权。在 Connect 宣传的用法中，「看见即行动」要靠摄像头的上下文；而早期传闻称 Confidential VM 发布时不支持可穿戴设备（[Secure VM 解析]({{< relref "/docs/muse/sources/community/2026-09-16-ifynx-muse-secure-vm" >}})）。眼镜用户的数据怎样处理，要结合 [隐私]({{< relref "/docs/muse/analysis/privacy" >}}) 一起看。

## Muse Charm：专用硬件只有发布与报道

Connect 上，Meta 发布了 Muse Charm：一个口袋大小、专门用来和 Muse 交谈的设备，搭载实时语音模型，「今年晚些时候」再公布更多信息（[Connect 2026 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})、[Connect 2026]({{< relref "/docs/muse/sources/official/2026-09-24-connect-2026" >}})）。Meta 11-05 的语音功能公告说，语音对话「即将登陆 AI 眼镜和 Muse Charm」（[语音与表情化身]({{< relref "/docs/muse/sources/official/2026-11-05-give-your-muse-a-voice" >}})）。

各家报道的规格不完全一致：

| 来源 | 说法 |
| --- | --- |
| Meta（经社区拆解转述） | 轻触角落的指纹传感器就能说话；点名的用途有找优惠、订位、管理收件箱；12 月假日季前上市，未公布价格（[拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})） |
| Bloomberg（经 The Verge，再经社区拆解转述） | 5G 调制解调器、2 英寸 OLED 触屏、新的操作系统、摄像头、扬声器、麦克风、USB-C；Meta 自己没有提摄像头，拆解作者把摄像头列为「据报道」，不是「已确认」（[拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})） |
| 橘AI 播客讨论者 | 两英寸屏幕、前后摄像头、5G 和 eSIM，赶在圣诞节发货（[橘AI：深入讨论 Muse]({{< relref "/docs/muse/sources/community/2026-10-04-juai-muse-discussion" >}})） |
| The Information（经 PYMNTS 转述） | 计划定价 300 美元，购买者最多可获 12 个月免费 5G；Meta 当时计划 12 月发货；Meta 没有证实，发言人只说「很快会有更多消息分享」（[Charm 定价 300 美元]({{< relref "/docs/muse/sources/media/2026-11-19-pymnts-muse-charm-price-300" >}})） |
| The Verge 记者 | 真品 Charm 有摄像头和 5G（[50 美元自制 Muse Charm]({{< relref "/docs/muse/sources/media/2026-10-31-verge-diy-muse-charm" >}})） |

36 氪整理的 Wang 访谈称，2026 年 2 月之后的原型里已经有 Charm 的早期版本（[Muse 是玩龙虾玩出来的]({{< relref "/docs/muse/sources/media/2026-10-12-36kr-wang-openclaw-origin" >}})）。截至 2026-11-28，资料库里没有 Charm 开售或发货的记录。

The Verge 记者用 50 美元的 Waveshare ESP32-S3 开发板，按官方 Gadgets 方案自制了一个「Charm」（[50 美元自制 Muse Charm]({{< relref "/docs/muse/sources/media/2026-10-31-verge-diy-muse-charm" >}})）：
- 刚装好时基本不能用：Muse 把语音当成要转录的音频，回复慢、不出声；
- 记者借 Claude Code 改造后才可用，延迟主要来自 Meta 的服务器；
- 他的结论是，Muse 本身不是买一块专用硬件的理由，专用硬件应该做手机做不到的事。

推断：Charm 不承载智能体，它的差异只能来自随身、免解锁、独立联网和摄像头。最后两项在官方资料里都没有确认。在 2 英寸屏幕上怎样呈现审批提示，Meta 也没有说明（[拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})）。这个问题直接影响 [安全]({{< relref "/docs/muse/analysis/security" >}}) 里的审批机制。

## Gadgets SDK 与 Home Link：把家里的设备接进来

**Muse Gadgets SDK（2026-10-02）。** 包括 ESP32 Device SDK 和 Linux Device SDK，可以把 ESP32 开发板或 Raspberry Pi 接到 Muse，再接上屏幕、按钮、传感器（[Gadget SDK README]({{< relref "/docs/muse/sources/official/2026-10-02-muse-gadget-sdk-readme" >}})、[Muse Gadgets 主页]({{< relref "/docs/muse/sources/official/2026-11-04-muse-gadgets-home" >}})）。使用条件：
- 刷写或配对前要申请 SDK 令牌，每台小设备都要凭令牌配对；
- 配对在 Muse 应用「设置 > 设备」里进行，要先打开开发者模式；
- 代码采用 Apache 2.0 许可，Jollybot 头像不在许可范围内；
- 页面自称「为黑客打造，风险自负」（[Gadget SDK README]({{< relref "/docs/muse/sources/official/2026-10-02-muse-gadget-sdk-readme" >}})、[Muse Gadgets 主页]({{< relref "/docs/muse/sources/official/2026-11-04-muse-gadgets-home" >}})）。

社区解读认为，开放的是设备，不是智能体：小设备没有 Muse 账号就没有可以对话的对象（[拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})、[Meta Muse 开源吗]({{< relref "/docs/muse/sources/community/2026-11-05-is-meta-muse-open-source" >}})）。

**Muse Home Link。** Meta 自家的 USB-C 网关（[Muse Home Link]({{< relref "/docs/muse/sources/official/2026-11-04-muse-home-link" >}})）：
- 硬件：ESP32-C5、8 MB PSRAM、8 MB 闪存、Wi-Fi 6，尺寸 35×42×10 mm，只运行官方固件，不能重刷；
- 设置：在 Muse 应用里用低功耗蓝牙配对并选 Wi-Fi，之后常驻家庭网络，Muse 由此能访问兼容设备或本地 HTTP API；
- 领取：仅限美国，随有效订阅附赠，每位订阅用户限领一个，页面写「10 月发货」。

社区转述 The Verge，称 Meta 只做了 5,000 台，开放了等待名单（[智能家居接入]({{< relref "/docs/muse/sources/community/2026-11-20-muse-smart-home-tuya-skill" >}})）。9 月的文件系统导出里已经有一份 Home Link 文档，写明设备配对、本地网络发现，以及要单独批准的智能体访问步骤（[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})、[The Verge：下载整个文件系统]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}})）。

**社区技能。** 官方页面列出 Philips Hue、Sonos、Apple TV、Google Nest 音箱、Samsung 电视等社区技能，提醒不要把它们用于家庭安防、紧急情况或医疗需求（[Muse Home Link]({{< relref "/docs/muse/sources/official/2026-11-04-muse-home-link" >}})、[Muse Gadgets 主页]({{< relref "/docs/muse/sources/official/2026-11-04-muse-gadgets-home" >}})）。2026-11-10，涂鸦的 Tuya Skill 以 PR #61 合并进 Meta 的 muse-gadget-sdk 仓库，把 Muse 能控制的范围扩展到家里已有的量产联网设备（[Tuya 智能家居 Skill]({{< relref "/docs/muse/sources/community/2026-11-12-tuya-cloud-devices-skill" >}})、[智能家居接入]({{< relref "/docs/muse/sources/community/2026-11-20-muse-smart-home-tuya-skill" >}})）。

**用户自有电脑。** PC Watch 的作者让 Muse 从云端虚拟机经 Tailscale 和 SSH 进入自己的家用电脑，再经 Telnet 开发 2005 年的 Zaurus 旧机（[Muse 当 Zaurus 开发者]({{< relref "/docs/muse/sources/media/2026-11-19-pc-watch-muse-zaurus-developer" >}})）。这条路不经过任何官方设备通道，是用户自己搭的。

推断：Home Link 只有 5,000 台，Muse 的用户却超过 1000 万（据 Meta 财报会口径，见 [商业与规模]({{< relref "/docs/muse/analysis/business" >}})）。所以家居接入实际上主要靠社区技能和第三方云。对 [连接器]({{< relref "/docs/muse/analysis/connectors" >}}) 来说，这是另一条接入路径。

## 远期形态：人形机器人

NDTV 转述 The Information 的报道（[NDTV：Max 人形机器人]({{< relref "/docs/muse/sources/media/2026-11-02-meta-max-humanoid-robot" >}})）：
- Meta 和上海的 Fourier 合作，用三个月造出人形机器人原型 Max；
- Meta 的要求包括在五米外识别声音、在三米外读懂手势；
- Meta CTO Andrew Bosworth 在内部把人形机器人描述为 Muse 的一种潜在实体形态；
- Meta 发言人称这项合作只用于内部研究和实验，没有销售计划。

这条信息只有一个二手来源，只能说明方向，不说明产品计划。

## 资料缺口

- Muse Charm 的官方规格、价格、发货日期和开售地区，审批提示在小屏上怎样呈现；是否有摄像头，各方说法不一。
- 眼镜 Beta 开放的国家和型号、额外用量的数值，眼镜摄像头数据的处理方式。
- iPad 应用和 Wear OS 版的官方公告，手表端能用哪些功能、系统要求是什么。
- Home Link 的实际发货数量和后续供应；Gadgets 令牌的审批规则。
- macOS 27.3 正式版后 Mac 端权限的实际变化，Meta 的应对；各终端权限的官方对照（Android 默认授予通知权限的依据）。
- Max 人形机器人的一手报道（The Information 原文）。

## 主要资料

**官方**

- [个人智能体登陆 AI 眼镜]({{< relref "/docs/muse/sources/official/2026-09-23-muse-on-ai-glasses" >}})、[Connect 2026 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})、[Connect 2026]({{< relref "/docs/muse/sources/official/2026-09-24-connect-2026" >}})：Connect 2026 上的眼镜、Charm 和 Mac 计划。
- [帮助：Mac 文件与应用]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})：Mac 计算机操作的三项权限和分级访问。
- [帮助：眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})：眼镜 Beta 的使用条件和限制。
- [Gadget SDK README]({{< relref "/docs/muse/sources/official/2026-10-02-muse-gadget-sdk-readme" >}})、[Muse Gadgets 主页]({{< relref "/docs/muse/sources/official/2026-11-04-muse-gadgets-home" >}})、[Muse Home Link]({{< relref "/docs/muse/sources/official/2026-11-04-muse-home-link" >}})：Gadgets SDK 和 Home Link 的规格与领取条件。
- [语音与表情化身]({{< relref "/docs/muse/sources/official/2026-11-05-give-your-muse-a-voice" >}})、[Muse 上线澳大利亚]({{< relref "/docs/muse/sources/official/2026-11-17-muse-available-australia" >}})：语音登陆眼镜和 Charm 的预告；澳大利亚的终端清单。

**媒体**

- [路透：Muse 安全事故]({{< relref "/docs/muse/sources/media/2026-11-18-muse-early-safety-mishaps-surface" >}})、[Signal 限制截图防读取]({{< relref "/docs/muse/sources/media/2026-11-21-signal-screenshots-block-ai-agents" >}})：路透社复现 Muse 跨端读取 Signal，Apple 的应对。
- [登陆手表双平台]({{< relref "/docs/muse/sources/media/2026-11-09-muse-apple-watch-wear-os" >}})、[Muse 登陆 Apple Watch]({{< relref "/docs/muse/sources/media/2026-11-09-muse-apple-watch" >}})、[上线手表双平台]({{< relref "/docs/muse/sources/media/2026-11-10-techcrunch-muse-apple-watch-wear-os" >}})：手表版上线和功能；iPad 应用时间。
- [Charm 定价 300 美元]({{< relref "/docs/muse/sources/media/2026-11-19-pymnts-muse-charm-price-300" >}})：Charm 的定价报道，Meta 自家手表推迟。
- [50 美元自制 Muse Charm]({{< relref "/docs/muse/sources/media/2026-10-31-verge-diy-muse-charm" >}})：自制 Charm 的一手实测。
- [TechCrunch：Connect 上的 Muse]({{< relref "/docs/muse/sources/media/2026-09-23-techcrunch-everything-new-muse" >}})：Connect 上的 Mac 计算机操作。
- [NDTV：Max 人形机器人]({{< relref "/docs/muse/sources/media/2026-11-02-meta-max-humanoid-robot" >}})：人形机器人 Max。
- [雷科技：Muse 登上智能手表]({{< relref "/docs/industry/sources/media/2026-11-10-leikeji-muse-smartwatch" >}})：手表端的定位分析。

**社区**

- [拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})：Charm 三类来源的区分，「Charm 不是 Muse 居住的地方」。
- [眼镜端 Muse beta 解析]({{< relref "/docs/muse/sources/community/2026-11-09-muse-on-glasses-beta" >}})：眼镜 Beta 是替换而不是并存。
- [Muse 登陆手表核查]({{< relref "/docs/muse/sources/community/2026-11-12-muse-on-apple-watch-wear-os" >}})：手表版的分层核查。
- [Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})、[Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})、[OpenClaw 同源拆解]({{< relref "/docs/muse/sources/community/2026-11-04-muse-openclaw-teardown" >}})：Android 节点能力和设备数据同步。
- [苹果重写 Mac 权限提示]({{< relref "/docs/muse/sources/community/2026-11-19-apple-rewrote-mac-permission-screen" >}})：macOS 27.3 beta 2 的权限改动。
- [智能家居接入]({{< relref "/docs/muse/sources/community/2026-11-20-muse-smart-home-tuya-skill" >}})、[Tuya 智能家居 Skill]({{< relref "/docs/muse/sources/community/2026-11-12-tuya-cloud-devices-skill" >}})：Home Link 数量和 Tuya Skill。
- [iMessage 事件详解]({{< relref "/docs/muse/sources/community/2026-10-01-did-muse-read-your-messages" >}})：Mac 的 iMessage 同步争议。

**实测**

- [我的实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})：VM 中 `device` schema 的同步数据。
