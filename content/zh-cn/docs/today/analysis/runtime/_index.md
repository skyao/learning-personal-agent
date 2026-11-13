---
title: "Today AI：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Today 是「云端执行 + 用户设备网关」的混合结构：官方称有始终在线的云计算机承担后台任务，同时通过桌面客户端和 Chrome 插件直接操作用户本机与已登录的浏览器。云端环境的形态、规格与持久化官方没有公开，第三方「只是沙箱」的说法没有出处。
---

## 概要

- 官方称 Today 由前沿模型、任务执行和「始终在线的云计算机」组成，多步骤工作在用户离线时也能继续；能力页补充，依赖本地设备、文件或权限的任务仍可能要求设备在线。
- 与多数海外同类不同，Today 把用户自己的设备当作执行环境的一部分：macOS 客户端可读屏幕、操作没有 API 的应用、跑 Shell 脚本；Chrome 插件可在用户已登录的网站里点击、填表。
- 团队自述「技术原理上是 OS Agent」，设备网关从一开始按可扩展到更多设备设计；放弃纯 IM 形态的原因之一是没有客户端拿不到设备权限。
- 任务以「单一主对话 + 后台独立任务」运行：实测中多个任务并排显示「运行中」，对话不被阻塞；团队认为 Agent Team 在日常琐事上耗 token、增时延，不采用。
- 云端环境的规格、是否每用户一台、持久化与休眠策略，截至 2026-11-10 的资料均无官方说明。

## 云端执行：官方只说「始终在线的云计算机」

官方博客称 Today 的底层是把前沿模型、任务执行和「始终在线的云计算机」组合起来的智能体循环，用户离线时多步骤工作也能继续（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})）；另一篇称长期任务跨天存活，内部栈包括模型编排、规划、记忆检索、任务队列和跨设备同步（[官方：Meet Today]({{< relref "/docs/today/sources/official/2026-08-03-meet-today" >}})）。

能力页的表述更保守：符合条件的云端任务可以在不保持对话开启的情况下继续，依赖本地设备、文件或权限的任务仍可能要求设备在线；能力受设备、地区、分发渠道、账户、灰度和权限影响（[能力页]({{< relref "/docs/today/sources/official/2026-11-05-capabilities" >}})）。

晚点访谈中团队称，让 agent 在云端有自己的执行空间、用户在手机上也能发起复杂任务，已是行业架构共识（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）。

关于云端环境的具体形态，只有第三方说法：Datawhale 刊发的阿里云 Agent 技术专家综述称 Today 的云电脑「其实只是一个沙箱」，可能出于成本考量，不像海外产品那样真正使用云电脑（[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）；鸿煊综述有同样的说法（[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。两篇都没有注明出处，后者的对照表与前者内容相近。官方没有公开虚拟机或沙箱的规格。

## 用户设备是执行环境的一部分

集成页把能力分成「云集成」和「连接你自己的设备」两部分。设备部分按系统列出权限：macOS 上有 Apple Mail、Notes、Messages、屏幕上下文（Screen Recording）、Computer Control（Accessibility，在「没有 API 的应用里点击和输入」）、剪贴板、Shell 脚本（每次运行需批准）；iOS 上有 Apple Health、照片、相机麦克风；Android 上有 Health Connect、通知、应用使用时长、短信通话（仅直装版）。Windows 原生邮件日历、Linux 剪贴板与屏幕标为 Soon（[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})）。

中国版 Chrome 插件（2026-10-15 更新）安装登录后，Today 可读取打开的标签页，在用户已登录的网站里打开页面、点击、输入、填表，并可指定做到哪一步为止；任务期间 Chrome 须保持运行、插件保持连接（[Chrome 插件（中国版）]({{< relref "/docs/today/sources/official/2026-10-15-chrome-extension-china" >}})）。产品笔记作者用插件汇总即刻圈子三天内的发帖，执行良好（[产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}})）。

智能涌现整理的团队自述称，Today 在技术愿望与原理上是 OS Agent，但不局限于某一个操作系统，设备网关从一开始按可扩展到更多设备设计；3 月放弃只住在 IM 里的形态，原因之一是没有客户端就拿不到一部分设备权限（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。

推断：Today 的运行环境更接近「云端调度 + 本机代理」，与 Muse、dots 那种每用户一台云端虚拟机、主要在云端浏览器里操作的路线不同。好处是能直接使用用户已有的登录状态和本地文件；代价是部分任务要求用户设备在线。这一判断依据的是集成页与插件说明，官方没有正面描述两者的分工。

## 单一对话，后台并行任务

Founder Park 实测国内版：同时交代归拢 163/QQ 邮箱未读邮件、写稿件提纲、整理飞书待办、生成图文简报，Today 拆成 4 个独立任务，并排显示「运行中」，对话不被卡住，可点开看每个任务的执行说明（[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})）。晚点访谈称 Today 上线了 multi-task 系统，会主动识别复杂任务移到独立任务，结果同步回主对话（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）。极客公园实测中，一个足球陪练方案被升级成后台任务，花了近一小时（[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})）。

团队自述称，同一任务用 Agent Team 跑的 token 消耗明显高于单 session，日常琐事上效率不一定更好还增加时延，只在代码审核这类需要互相 review 的专业场景有价值（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。

## 成本

团队自述称 Personal AI 的运行成本比上一代 AI 产品高很多，沙箱、搜索、主动性机制、长程任务都是大成本，并引市场调查推测 Instinct 单日运行成本约 1–3 美元（[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。晚点访谈称降本之后才能运行更多主动化策略（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）。

Today 自身的成本数据资料中没有。Z Finance 引摩根士丹利对 Muse 的测算（2 vCPU、8GB 沙箱约每小时 0.1217 美元等），并据此假设 Today 达到 100 万日活时的月账单，这是作者的推算，不是 Today 的数据（[Z Finance]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})）。

## 资料缺口

- 云端执行环境的形态（虚拟机、容器还是沙箱）、规格、是否每用户独占、持久化与休眠策略。
- 云端与本机的任务分工规则：哪些任务必须本机在线，离线时如何排队或失败。
- 并发任务数、单任务时长、算力额度的限制。
- 「扫描本地磁盘」「云电脑只是沙箱」两种说法的一手出处。

## 主要资料

- 官方：[What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})、[Meet Today]({{< relref "/docs/today/sources/official/2026-08-03-meet-today" >}})（云计算机、任务跨天存活）；[能力页]({{< relref "/docs/today/sources/official/2026-11-05-capabilities" >}})（设备在线要求）；[集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}})（设备权限清单）；[Chrome 插件（中国版）]({{< relref "/docs/today/sources/official/2026-10-15-chrome-extension-china" >}})（浏览器操作）。
- 媒体：[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})（OS Agent、设备网关、Agent Team 取舍）；[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})（multi-task）；[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})、[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})（后台任务实测）；[Z Finance]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})（行业成本测算）。
- 社区：[产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}})（插件实测）；[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})（「只是沙箱」，无出处）。
