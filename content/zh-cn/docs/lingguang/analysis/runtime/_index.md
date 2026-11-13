---
title: "蚂蚁灵光：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  灵光 2.0 的任务在「独立的云端实例」上运行，关掉 App 后继续执行；媒体称其为 24 小时运行的独立云主机，带浏览器，内测作者称是一台可自装工具的 Linux 云电脑。规格、持久化、并发与可见性官方均未公布。
---

## 概要

- 官方称灵光 2.0「运行在独立的云端实例上」，单次对话结束后任务仍可继续。媒体与评测者普遍称之为「独立云主机」，并称其 24 小时运行。
- 环境里有浏览器，可通过网页操作完成任务；内测作者称这是每用户一台完整的 Linux 云电脑，能下载 Claude Code 作为子代理、安装 Skill。后者是作者在正式发布前的观察，含推测，官方没有写到这一层。
- 云端浏览器在国内电商面前受限：极客公园实测中，灵光只能在云端打开淘宝网页版，购物车被风控拦截。运行环境的能力边界主要由平台开放程度决定（见[连接器]({{< relref "/docs/lingguang/analysis/connectors" >}})）。
- 截至 2026-11-10 的资料，没有说明用户能否观看或接管云端环境，也没有虚拟机规格、休眠回收、并发、超时与额度的说明。
- 成本方面只有评论者推断：每个「帮我管」任务背后都是定时唤醒的云端主机，重度用户的轮询成本可能很高。

## 每个用户一台云端主机

官方发布稿称，灵光 2.0 的主动发现与持续跟进依靠跨会话记忆、长程任务调度和工具调用的升级，并「运行在独立的云端实例上」，对话结束后任务仍可继续（[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})）。财经网与 AI故事计划转述官方宣传时写作「独立云主机」（[财经网]({{< relref "/docs/industry/sources/media/2026-11-06-caijingwang-transaction-management" >}})、[AI故事计划：二线厂]({{< relref "/docs/industry/sources/media/2026-11-05-aigushijihua-second-tier-personal-agent" >}})）。新眸称这台云主机「24 小时运行」，在它之上叠加跨会话记忆、长程任务调度、工具连接三层能力（[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})）。

智东西写到，产品「还提供独立电脑和浏览器」，可以通过网页操作处理任务；任务跑在云端，不会因为关掉应用停止，独立主机也为执行提供干净的环境（[智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}})）。光子星球实测时退出 App，任务在后台执行，完成后在通知栏提醒；灵光自己说明价格监控会「自动生成一个事件，在云端环境中持续运行」（[光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}})）。小朱的截图里，灵光自述有「独立云主机机制」，每个用户有专属的云端运行环境（[小朱]({{< relref "/docs/lingguang/sources/community/2026-11-04-aizxiaozhu-lingguang-domestic" >}})），这是产品的自我描述，不是官方文档。

小象AI 认为整个架构以云端为中心，手机和电脑上只是「非常薄的 App 和 Web 界面」，好处是记忆连续、长程任务不受个人电脑开关机影响（[小象AI]({{< relref "/docs/lingguang/sources/community/2026-10-28-xiaoxiang-lingguang-2-hands-on" >}})）。

## 内测作者看到的 Linux 云电脑

特工宇宙在正式发布前两周的内测中称，灵光给每个用户分配一台 24 小时在线的独立 Linux 云电脑，有自己的浏览器，可以自行安装工具（[特工宇宙：内测]({{< relref "/docs/lingguang/sources/community/2026-10-13-tegongyuzhou-beta-hands-on" >}})）。作者的两个实测：

- 让云电脑里的浏览器打开作者自建的网页输入框，经 Claude Code 控制作者自己的电脑，一句话取回文件、调用电脑上的 Agent，任务「只跑了三分钟」。
- 让灵光在云电脑里下载 Claude Code 作为执行任务的子代理，顺手写出一个计算器小程序。奈势AI 转述了同一做法，未注出处（[奈势AI]({{< relref "/docs/industry/sources/community/2026-10-15-naishi-what-can-it-do" >}})）。

作者自述文章「更多是从内测体验和观察所做的理解与推测」，正式发布稿只写「独立云端实例」，所以「Linux」「完整机器」等细节应视为单个用户的观察。正式版中也有旁证：AI沃茨让灵光安装飞猪 Skill 时 GitHub 一直超时，灵光自己改为手动安装并把 Key 写进配置（[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})），说明环境内可以装 Skill 和命令行工具。

## 云端浏览器进不了淘宝

极客公园让灵光查看淘宝购物车，灵光只能在云端打开淘宝网页版，要求用户扫码、提交短信验证码登录，之后购物车被淘宝的反爬风控拦截，一直加载不出；同一任务千问可以直接列出购物车（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})）。文章的解释是：美国电商分散，Muse 能用云端浏览器直接访问店铺；中国消费集中在少数超级 App 内部，网页这条路走不通。

推断：从这个例子看，灵光的云端浏览器是兜底手段，主路径是支付宝内置能力和官方连接器；在没有开放接口的国内平台上，「有一台云电脑」并不等于能办事。

## 成本与限制

官方没有公布单用户的算力额度、任务并发数或超时规则。Z Finance 设想一个重度用户挂上十个「每两小时查一次」的任务，云端每天要执行上百次检索、拉取与模型推理，认为每个「帮我管」背后「都是一台在云端持续驻留、定时唤醒的独立主机」，并发轮询成本是财务难题（[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})）。这是作者推演，不是披露的数据。

## 资料缺口

- 云端实例的规格、操作系统、持久化方式，空闲时是否休眠或回收。
- 用户能否查看云端浏览器的操作过程、能否接管登录（特工宇宙称执行时「可以清楚看到当前在做什么操作」，正式版是否保留不明）。
- 多个事务是否共用同一实例；并发上限、单任务时长上限、每日额度。
- 云端浏览器中登录状态如何保存，与 APASS 托管的凭证是什么关系。

## 主要资料

- 官方：[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})，「独立的云端实例」的唯一官方出处。
- 媒体：[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})、[智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}})，独立云主机与浏览器；[光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}})，后台执行与通知；[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})，云端浏览器访问淘宝失败。
- 社区：[特工宇宙：内测]({{< relref "/docs/lingguang/sources/community/2026-10-13-tegongyuzhou-beta-hands-on" >}})，Linux 云电脑与 Claude Code 子代理；[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})，环境内安装 Skill；[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})，成本推演；[小象AI]({{< relref "/docs/lingguang/sources/community/2026-10-28-xiaoxiang-lingguang-2-hands-on" >}})，云端为中心的架构判断。
