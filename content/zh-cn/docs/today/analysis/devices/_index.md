---
title: "Today AI：设备"
linkTitle: "设备"
weight: 60
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Today 覆盖三大桌面系统、两大移动系统、网页端和 Chrome 插件，各端共享一份记忆；电脑端承担读屏、操作应用、跑脚本等本机执行，手机承担健康数据、录音与提醒。团队称硬件将与合作伙伴一起做，不自己做。各资料对平台范围和上线时间的说法不一。
---

## 概要

- 截至 2026-10-22 的资料，Today 支持 macOS、Windows、Linux、iOS、Android 和网页端，另有 Chrome 插件；产品笔记称「基本全端覆盖」。
- 各端角色不同：macOS 客户端权限最深（读屏、Computer Control、Shell、iMessage）；手机提供 Apple Health / Health Connect、照片、录音与锁屏提醒；Windows、Linux 部分能力标为 Soon。
- 平台范围与上线时间各资料说法不一：官方 8 月博客称 Mac、iOS、Android 已正式上线；国内版 10 月初的报道列 macOS、Windows、Linux、iOS；产品笔记称 iPhone 版此前一直走 TestFlight，10 月下旬才正式上线。
- 晚点访谈中团队称硬件会和合作伙伴一起做，原计划「先软件、再硬件、再模型」，现改为软件和模型同时做，再考虑硬件。

## 平台覆盖与上线时间

| 资料 | 时间 | 平台说法 |
| --- | --- | --- |
| [官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}}) | 2026-08-03（页面更新至 09-15） | 已在 Mac、iOS、Android 正式上线；平台在开发中的用户可先用网页端或桌面端 |
| [Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}}) | 2026-10-01 | 国内版支持 macOS、Windows、Linux、iOS |
| [产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}}) | 2026-10-22 | 3 大桌面系统、2 大移动系统、1 个网页端，加浏览器插件；iPhone 版此前走 TestFlight，这次正式上线 |
| [集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}}) | 2026-11-05 收集 | 设备能力按 macOS、Windows、Linux、iOS、Android 列出，Windows、Linux 部分为 Soon |

推断：官方博客的「正式上线」与产品笔记的「iPhone 版此前走 TestFlight」可能分别指国际版与国内版，资料没有说明。

## 各端的分工

集成页的设备部分显示 macOS 权限最深：Apple Mail、Notes、Messages、屏幕上下文、Computer Control（在没有 API 的应用里点击输入）、剪贴板、Shell 脚本（每次运行需批准）、桌面与下载文件夹。iOS 提供 Apple Health、照片、相机麦克风；Android 提供 Health Connect（14+）、通知、应用使用时长、短信通话（仅直装版）（[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})）。二阶变量称接入列表中「本机」「其他设备」两类服务于在苹果与安卓、手机与电脑之间切换的人（[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})）。

Today Recording 率先登陆 Mac 和 iPhone：会议室里手机开录，桌面读 Summary，通勤路上追问；iPhone 锁屏以 Live Activity 提示录音（[官方：Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})）。官方称同一段记忆跟着用户换设备（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})）。

## 硬件：与合作伙伴做

晚点访谈中团队称硬件将与合作伙伴一起做、不自己做，假设个人助理需要戒指、手环等硬件获取健康等个性化上下文；软件和模型层统一，硬件形态和品牌可以多样；原计划先软件、再硬件、再模型，现在软件和模型同时做，硬件渗透速度有限，是否成为胜负手吃不准（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）。品玩称对于是否绑定某种终端，团队回答「keep it open」（[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})）。投资方中有手机厂商传音控股（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})），资料中没有双方硬件合作的信息。

## 资料缺口

- 国际版与国内版各平台的上线时间与功能差异。
- Android 国内版的情况（Founder Park 的清单中没有 Android）。
- 硬件合作的对象与进展；与传音是否有合作。
- 可穿戴设备（WHOOP、Oura 等）数据在实际建议中的使用实测。

## 主要资料

- 官方：[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})（各系统权限）；[What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})；[Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})。
- 媒体：[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})（硬件策略）；[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})、[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})、[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})、[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})。
- 社区：[产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}})（平台覆盖、TestFlight）。
