---
title: "Grok Bot：设备"
linkTitle: "设备"
weight: 60
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Grok Bot 的工作在每位用户一台的云端计算机上完成。桌面端（macOS、Windows、Linux）和手机端（iPhone、Android）只用来聊天、审核和审批，两端看到的是同一批 Bot 和同一台云端计算机。桌面电脑还可以作为 Bot 的本地执行端和网络出口。资料中没有手表、眼镜或专用硬件。
---

## 概要

- 截至 2026-11-12 的资料，Grok Bot 的客户端有两类：桌面应用（macOS、Windows、Linux）和手机应用（iOS 18 以上的 iPhone、Android 9 以上）。官方部署文档把客户端定为聊天、审核和审批的「瘦客户端」，工作在托管的云端计算机上完成。
- 手机与桌面连接的是同一批 Bot、对话、例程和同一台云端计算机，因此登录状态两端通用。但示范教学、测试例程、更新计算机仍只能在桌面端做；手机端 1.19.0 起也不能新建群聊。
- 用户自己的桌面电脑有两个额外角色。一是作为 Bot 的本地执行端：Bot 可在上面运行命令、复制文件，每台电脑可分别设为「始终允许」「每次询问」「从不允许」。二是作为网络出口：开启后，Bot 云端计算机的网页流量经桌面转出。
- 通知按设备做了分工和去重：用户正在用桌面时，提醒先发到桌面，约 3 分钟后才推送到手机。
- 资料中没有手表、眼镜或专用硬件。设备以外唯一的终端线索是 Tesla 车辆集成，资料只有一句话。

## 桌面与手机：同一台云端计算机的两个入口

官方部署文档写明，客户端只用于聊天、审核和审批，Bot 在托管计算机上工作。托管计算机是 Cursor 云端的 Linux 机器，每位成员一台，不加入 MDM（[部署文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-deployment" >}})）。运行环境的细节见[运行环境]({{< relref "/docs/grok-bot/analysis/runtime" >}})。

2026-08-11 发布时，beta 只面向桌面和 iOS（[官方发布]({{< relref "/docs/grok-bot/sources/official/2026-08-11-introducing-grok-bot" >}})）；Android 应用出现在之后的文档中。

各终端的系统要求，以 docs.x.ai 常见问题（2026-10-28 版）和 Cursor 部署文档（2026-11-05 收集）为准：

| 终端 | 要求与形态 | 资料 |
| --- | --- | --- |
| macOS | Apple 芯片与 Intel；`.dmg` 安装 | [常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})、[部署文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-deployment" >}}) |
| Windows | x64、Arm64；Setup `.exe`，按用户安装 | 同上 |
| Linux | x64、Arm64；`.deb`、`.rpm`、AppImage | 同上 |
| iPhone | iOS 18 以上，App Store 分发 | 同上 |
| Android | Android 9 以上，Google Play 分发 | 同上 |

官方常见问题称，桌面端界面有 37 种语言，手机应用有 12 种。桌面、iPhone 和 Android 都支持实时语音聊天，Bot 还可以发送语音备忘录（[常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})）。社区教程的描述是「你在电脑上和手机上看到的是同一批 Bot，聊天记录也是同步的」（[鱼皮：大厂为什么都在卷]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})）。

xAI 的入门指南从用户角度说明了「同一台计算机」的效果。作者称 Bot 在云端运行，「我在手机和桌面上得到的是同一台计算机」，所以 Facebook 已登录的状态两端都能用；作者的个人 CRM Bot 是「在手机上用 10 到 15 分钟搭好」的（[Grok Bot 入门 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})）。用量也不分端：帮助文档写明，macOS 和 iOS 共享同一个与 Cursor 账号绑定的用量桶，两个应用调用同一后端（[套餐与计费]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-plans" >}})）。

### 手机端能做的事比桌面少

据官方入门文档，手机端可以发消息、查看和接管计算机、审批动作、暂停或恢复例程，但「示范教学、测试例程和更新计算机仍在桌面端」（[开始使用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-get-started" >}})）。帮助文档还列出了几处手机端限制：

- 手机应用 1.19.0 起不能新建群聊，只能在电脑上创建（[群聊]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-group-chats" >}})）。
- 有些提供方无法从手机浏览器完成登录。在 1.19.0 以上的手机应用中，Adapter、Robinhood、Intercom 以及 iPhone 上的 Postiz 会提示在电脑上连接（[连接应用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-connect-apps" >}})）。
- 手机上共享和浏览 Bot 需要 1.19.0 以上；共享 Bot 不能成为主 Bot（[共享 Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-shared-bots" >}})）。

推断：从这些限制看，手机端的定位是随时查看和审批，需要较长交互或复杂登录的配置仍放在桌面端。

## 用户自己的电脑：本地执行端与网络出口

### Bot 可以在用户电脑上运行命令

官方推理钩子文档的工具分类中，有「成员电脑上的相同工具，以及两台电脑之间的文件复制」（`user-computer`），以及手机和设备工具（`user-phone`、`user-device`）（[推理钩子]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-inference-hooks" >}})）。资料没有说明 `user-phone`、`user-device` 能做哪些具体操作。

更新日志记录了这部分能力的演进（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）：

- 设置中有「计算机」部分，列出用户的计算机，每台可分别选「始终允许」「每次询问」或「从不允许」。
- 用户可以在另一台已登录的计算机上批准某台计算机上的任务。
- Bot 在用户计算机上运行的命令会在短暂连接中断和长时间等待中继续。工作原本是给某台离线计算机准备的时，Bot 会告诉用户，不会未经询问就换到另一台计算机上运行。

审批规则的整体设计见[安全]({{< relref "/docs/grok-bot/analysis/security" >}})。

### 经桌面转出网页流量

部分网站会屏蔽云端计算机的流量。为此，官方提供「通过这台电脑路由流量」开关，打开后「让网站看到你自己的连接」（[常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})）。设置文档的说明如下（[设置]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-settings" >}})、[设置与通知]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-settings-and-notifications" >}})）：

- 打开后，Bot 计算机的网页流量经当前桌面转出，目的地看到的是桌面的 IP 地址。
- 解析到私有地址或 VPN 地址的站点会被阻止，除非组织已经允许；设置里会显示本次会话阻止了多少站点。
- 同一时间只有一台桌面在路由。
- Enterprise 管理员关闭「Allow Local Egress Routing」后，开关锁定，生效中的路由在五分钟内停止。

## 通知在桌面与手机之间分工

据 docs.x.ai 的设置文档，macOS 或 Windows 桌面正在使用时，Bot 的通知发到桌面，不发手机；Bot 需要用户输入时，手机约 3 分钟后才收到通知，除非用户先打开了该 Bot、关闭了通知或隐藏了它（[设置与通知]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-settings-and-notifications" >}})）。Cursor 版设置文档补充，Grok Bot 处于焦点时通知会被抑制；群聊没有按 Bot 的通知开关（[设置]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-settings" >}})）。更新日志中，桌面通知会跳过用户在另一台设备上已读的回复（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

设置也分账号级和设备级：个人的 Auto-review 规则保存到账号，「相同的规则会应用于每台桌面和 iPhone」（[设置]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-settings" >}})）。

## 企业部署：无法由管理员关闭更新

部署文档写明，安装包只有 macOS `.dmg`、Windows Setup `.exe` 和 Linux 的 `.deb`、`.rpm`、AppImage，「没有 MSI 或 PKG」（[部署文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-deployment" >}})）。更新策略如下：

- 管理员没有办法关闭应用更新。成员可以关闭自动更新，但仍会收到新版提示。
- 低于最低版本或超过最大期限的旧版会显示「Update required」，两项限制由 Cursor 远程设置，不对外公布。
- 托管计算机的镜像由 Cursor 维护。

docs.x.ai 的设置文档称，桌面自动更新默认开启，只在屏幕锁定、空闲至少 10 分钟且 Bot 不忙时安装（[设置与通知]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-settings-and-notifications" >}})）。Teams 文档建议通过身份提供商把登录限制到受管设备，同时说明「这限制的是登录，而不是托管计算机本身」（[Teams 与 Enterprise]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})）。

## 车辆：Tesla 集成只有零星记录

Not a Tesla App 在 2026-10-15 的报道中提到，上个月特斯拉在车辆中集成了 Grok Bot，但没有展开（[Not a Tesla App：被亚马逊屏蔽]({{< relref "/docs/grok-bot/sources/media/2026-10-15-notateslaapp-amazon-blocked" >}})）。更新日志 v0.79.2（2026-11-05）写明，打开或解锁 Tesla、或让别人驾驶它的命令「始终会请求你的批准」（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

推断：这条审批规则说明 Bot 能向 Tesla 车辆发出控制命令，但通过什么途径（车载系统内的 Bot、Tesla 账号连接器或其他方式），资料没有说明。

## 资料缺口

- 手表、眼镜、专用硬件：资料中没有任何说明，无法判断是没有计划还是没有收集到。
- Tesla 集成的形态、上线时间、开放范围，以及 Bot 可执行的车辆命令清单。
- 推理钩子中 `user-phone`、`user-device` 的具体能力：Bot 能在手机上做什么，是否像其他产品一样读写短信、通知。
- 手机端与桌面端功能差异的完整清单；iPad 与平板形态的支持情况（资料只列出 iPhone 与 Android 手机）。
- 用户电脑作为本地执行端的独立实测：权限范围、对 macOS 和 Windows 系统权限的要求。

## 主要资料

官方

- [官方发布]({{< relref "/docs/grok-bot/sources/official/2026-08-11-introducing-grok-bot" >}})：beta 发布时只支持桌面和 iOS。
- [部署文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-deployment" >}})：瘦客户端定位、安装包、更新策略
- [常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})：系统要求、语言、语音、流量路由
- [开始使用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-get-started" >}})：手机端能做和不能做的事
- [设置]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-settings" >}})、[设置与通知]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-settings-and-notifications" >}})：出口路由、通知节奏、规则同步
- [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})：本地计算机权限、离线处理、Tesla 审批
- [推理钩子]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-inference-hooks" >}})：用户电脑、手机与设备工具分类
- [群聊]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-group-chats" >}})、[连接应用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-connect-apps" >}})、[共享 Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-shared-bots" >}})、[套餐与计费]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-plans" >}})：手机端限制、用量共享
- [Teams 与 Enterprise]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})：受管设备登录限制
- [Grok Bot 入门 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})：手机与桌面共用一台计算机的使用体验

媒体

- [Not a Tesla App：被亚马逊屏蔽]({{< relref "/docs/grok-bot/sources/media/2026-10-15-notateslaapp-amazon-blocked" >}})：Tesla 车辆集成的一句记录

社区

- [鱼皮：大厂为什么都在卷]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})：多端同步的用户描述
