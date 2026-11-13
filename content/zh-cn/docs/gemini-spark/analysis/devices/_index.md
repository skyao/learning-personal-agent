---
title: "Gemini Spark：设备"
linkTitle: "设备"
weight: 60
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Spark 覆盖手机、网页和 Mac 三端：手机负责下指令和远程浏览器，Mac 负责本机文件、本地 Chrome，并可被手机远程控制；没有专用硬件，资料中也没有 Windows 应用。
---

## 概要

- 支持的终端是 Gemini 移动应用（Android、iPhone）、网页版和 Mac 版 Gemini 应用；资料中没有 Windows 应用、手表、眼镜或专用硬件。
- 各端分工不同：Chrome 自动浏览只在桌面端，远程浏览器只在移动设备上使用；自定义 MCP 应用、Google 相册任务只在手机和网页，不在 Mac。
- Mac 是 Spark 唯一能碰本机文件的终端：6 月 30 日以 Beta 推出（美国、18 岁以上、Ultra），7 月 14 日起可以从手机等另一台设备远程控制，条件是同一账号、同一 Wi-Fi 或打开蓝牙。
- 云端任务不依赖设备在线，但用本地 Chrome 或 Mac 文件的任务需要设备开着。

## 三端与分工

| 终端 | 能做什么 | 不能做什么 | 资料 |
| --- | --- | --- | --- |
| 移动应用（Android、iPhone） | 发起和管理任务、计划、技能；用云端远程浏览器；自定义应用；相册任务 | Chrome 自动浏览 | [帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})、[帮助：自定义应用]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-custom-apps" >}})、[帮助：相册工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-google-photos-workflows" >}}) |
| 网页版 | 同上，自定义应用的连接在网页设置中添加 | — | [帮助：自定义应用]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-custom-apps" >}}) |
| Mac 应用 | 本机文件（「已连接的文件夹」）、计划与技能（6 月 30 日起）、被其他设备远程控制 | 自定义应用、相册任务未列入 | [帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})、[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}}) |
| 桌面 Chrome | Chrome 自动浏览，用已登录账号和密码管理器 | 仅桌面端；设备和 Chrome 要保持开着 | [帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})、[Chrome 集成]({{< relref "/docs/gemini-spark/sources/official/2026-07-30-spark-chrome" >}}) |

帮助页写明「目前，Chrome 自动浏览仅在桌面端可用」「远程浏览器仅在移动设备上使用」（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。Top5Apps 称 Chrome 自动浏览仅限美国（[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})），Chrome 集成发布稿也写最初只在美国（[Chrome 集成]({{< relref "/docs/gemini-spark/sources/official/2026-07-30-spark-chrome" >}})）；截至 2026-11-10 的帮助页没有写地区限制。

## Mac 应用

- I/O 当天（2026-05-19）Gemini 的 macOS 应用开放下载，官方称 Spark 将在「今年夏天晚些时候」进入，用来处理涉及本地文件的任务（[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})）。
- 2026-06-30，Spark for macOS 以 Beta 面向 18 岁以上的 Google AI Ultra 订阅用户推出，首先在美国（[6 月更新]({{< relref "/docs/gemini-spark/sources/official/2026-06-30-spark-updates-june" >}})）；同日 Mac 应用提供计划和技能（[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})）。
- 2026-07-14，支持从另一台设备远程控制 Mac 上的 Gemini（[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})）。帮助页的条件是：Mac 上的 Gemini 已设置好并接受移交任务的条款，两台设备登录同一账号，处于同一 Wi-Fi 或打开并连接蓝牙；可以分配任务、语音或文字输入、读历史对话、执行快捷操作、控制媒体（[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})）。

本机文件的权限与备份规则见[运行环境]({{< relref "/docs/gemini-spark/analysis/runtime" >}})。iThome 的对照是：Dots 要求电脑保持联网并开着 ChatGPT 应用，Muse 的 Mac 版离开电脑后仍可继续（[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。

推断：远程控制要求两台设备在同一 Wi-Fi 或蓝牙范围内，这意味着「出门在外用手机让家里的 Mac 干活」（6 月更新稿描述的场景）未必能直接实现；帮助页的条件与宣传场景之间的差距，资料中没有实测。

## 没有专用硬件

资料中 Spark 没有手表、眼镜、音箱等终端的说明。iThome 的比较表中，五款产品只有 Muse 宣布将支持 AI 眼镜（[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。

## 资料缺口

- Windows 端是否支持 Spark（Gemini 应用或 Chrome 自动浏览）。
- 远程控制 Mac 能否跨网络使用。
- Android 系统层面（如 Gemini 作为系统助手）与 Spark 的关系。

## 主要资料

- 官方：[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})；[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})；[帮助：自定义应用]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-custom-apps" >}})；[帮助：相册工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-google-photos-workflows" >}})；[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})、[6 月更新]({{< relref "/docs/gemini-spark/sources/official/2026-06-30-spark-updates-june" >}})、[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}})、[Chrome 集成]({{< relref "/docs/gemini-spark/sources/official/2026-07-30-spark-chrome" >}})。
- 媒体：[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
- 社区：[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})。
