---
title: "OpenAI Dots：设备"
linkTitle: "设备"
weight: 60
analyzedAt: 2026-11-12
sourcesUntil: 2026-11-11
description: >
  dot 运行在云端，手机负责下达请求和查看结果，桌面应用负责连接本地计算机；没有专用硬件，也不支持手表、眼镜等终端。
---

## 概要

- dot 的执行主体在云端，用户设备关机时云端工作可以继续；终端只是入口。
- 手机（iOS、Android 的 ChatGPT 应用）用于创建 dot、发请求、查看云端会话；2026-10-09 起才能在手机上创建 dot。
- 桌面应用（macOS、Windows）是唯一能把本地计算机连接给 dot 的地方，一次只能连一台；连接后本地文件、已登录的浏览器和 Codex 任务可供 dot 使用，但电脑要在线并打开 ChatGPT 应用。
- iOS 有小组件、快捷指令、操作按钮等专属入口；Android 的同类入口资料中没有。
- 没有专用硬件。Wired 问及 Dots 与 OpenAI 传闻中硬件的关系，Altman 拒绝回答。

## 各终端的角色

| 终端 | 能做什么 | 资料 |
| --- | --- | --- |
| 手机（iOS、Android ChatGPT 应用） | 创建 dot（2026-10-09 起）、发消息和通话、管理插件和记忆、查看云端会话线程；云端计算机在移动端以受控方式打开 | [移动端创建 dot]({{< relref "/docs/dots/sources/official/2026-10-09-docs-whats-new-dots-mobile" >}})、[帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}}) |
| iOS 专属 | 主屏小组件、快捷指令「打开你的 dot」（消息、听写、通话三种模式）、操作按钮；2026-11-04 起可从通知直接回复、从其他应用分享内容 | [文档：给你的 dot 发消息]({{< relref "/docs/dots/sources/official/2026-11-05-docs-message-your-dot" >}})、[11 月 2–6 日更新]({{< relref "/docs/dots/sources/official/2026-11-04-docs-whats-new-november-2-6" >}}) |
| 桌面应用（macOS、Windows） | 创建 dot、连接本地计算机、查看活动和已安排任务、管理委派任务 | [文档：连接计算机和应用]({{< relref "/docs/dots/sources/official/2026-11-05-docs-computers-and-apps" >}}) |
| 桌面浏览器 | 创建 dot、发消息、通话；不支持移动端网页 | [文档：认识 dots]({{< relref "/docs/dots/sources/official/2026-11-05-docs-meet-dots" >}}) |
| 手表、眼镜、车载、音箱 | 资料中没有任何支持的说法 | — |

用户可以在一台设备开始对话，在另一台设备继续与同一个 dot 交谈（[文档：认识 dots]({{< relref "/docs/dots/sources/official/2026-11-05-docs-meet-dots" >}})）。

## 云端为主，本地计算机可选

官方文档写明，dot「住在云端」，有自己的计算机和浏览器，用户的设备关闭时云端工作仍可继续；用户在自己电脑上登录某个网站，不会让 dot 也登录（[文档：连接计算机和应用]({{< relref "/docs/dots/sources/official/2026-11-05-docs-computers-and-apps" >}})）。云端环境的细节见[运行环境]({{< relref "/docs/dots/analysis/runtime" >}})。

连接自己的计算机是可选项，默认关闭，只能从桌面应用连接，一次只能连一台个人计算机。连接后 dot 可以使用本地文件、已登录的浏览器上下文，启动和管理本地 Codex 任务；本地任务要求计算机在线并打开 ChatGPT 应用（[文档：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-docs-getting-started" >}})）。本地访问权限在任何联系 dot 的地方都生效，「包括从你的手机上」，也就是说用户可以在手机上指挥 dot 操作家里或办公室的电脑。

企业侧要由管理员开启本地计算机访问（Enterprise 默认关闭），员工的桌面应用需要 26.929 或更高版本；本地执行遵循设备管理（MDM）和智能体安全策略（[文档：Work Cloud 与本地计算机访问]({{< relref "/docs/dots/sources/official/2026-11-05-docs-cloud-local-access" >}})）。

实测中的摩擦：Slide Factory 报告一台在线的 Mac 仍无法使用，原因是要先在该电脑的桌面应用里完成连接确认；文章还转引一个 GitHub issue，称在 Mac 上创建的任务从移动端看不到（[Slide Factory 第一天]({{< relref "/docs/dots/sources/community/2026-10-03-slidefactory-dots-first-day" >}})）。Datawhale 综述转引有用户反馈 Windows 本机的电脑操作还不可用（2026-10-18，[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）；2026-11-04 官方称 Windows 上的本地任务、电脑与浏览器操作更可靠了，资料无法确认此前的问题是否已解决。

推断：设备分工体现的是「云端干活、手机指挥、桌面授权」。手机上没有本地执行能力，dot 也不读取手机上的数据（资料中没有相关说法）；需要个人设备上的数据时，路径是连接桌面电脑，而不是手机。

## 没有专用硬件

官方资料没有 dot 专用硬件，只有企业预览中的「专职 dots」提到「IT 配置的硬件」（[推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}})）。Wired 在发布时问 Altman，Dots 是否是 OpenAI 传闻中硬件的软件先导，Altman 拒绝回答（[Wired：个人智能体之战]({{< relref "/docs/industry/sources/media/2026-09-30-wired-battle-personal-agent" >}})）。官方文档中的「眼镜」只是 dot 卡通形象的外观配件。

## 资料缺口

- Android 与 iOS 的功能差异；小组件、快捷指令只有 iOS 的文档。
- 桌面应用支持的系统版本，是否支持 Linux 桌面。
- 手机上「接管」云端计算机的具体体验，以及摄像头、麦克风、屏幕访问的实际效果。
- 手表、眼镜、音箱等终端以及硬件计划，资料中均无。

## 主要资料

- 官方：[文档：连接计算机和应用]({{< relref "/docs/dots/sources/official/2026-11-05-docs-computers-and-apps" >}})（云端与本地分工）；[文档：给你的 dot 发消息]({{< relref "/docs/dots/sources/official/2026-11-05-docs-message-your-dot" >}})（iOS 入口）；[移动端创建 dot]({{< relref "/docs/dots/sources/official/2026-10-09-docs-whats-new-dots-mobile" >}})；[11 月 2–6 日更新]({{< relref "/docs/dots/sources/official/2026-11-04-docs-whats-new-november-2-6" >}})（Windows、iOS 改进）；[文档：Work Cloud 与本地计算机访问]({{< relref "/docs/dots/sources/official/2026-11-05-docs-cloud-local-access" >}})（企业版本要求）。
- 媒体：[Wired：个人智能体之战]({{< relref "/docs/industry/sources/media/2026-09-30-wired-battle-personal-agent" >}})（硬件问题）。
- 社区：[Slide Factory 第一天]({{< relref "/docs/dots/sources/community/2026-10-03-slidefactory-dots-first-day" >}})（本地连接的摩擦）；[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})（Windows 反馈转引）。
