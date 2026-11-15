---
title: "Instinct：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-15
sourcesUntil: 2026-11-13
description: >
  Instinct 在云端替用户操作「自己的一部手机和一台电脑」，像人一样加载网页和应用；后台任务按批处理异步运行。算力是它的主要约束：创始人称邀请制下算力成本每周翻倍，这是不开放注册的原因。环境的规格、持久性和并发限制，资料都没有说明。
---

## 概要

- 官方称 Instinct「能像你一样使用手机和电脑」：它有自己的电话号码、邮箱、一部虚拟手机和一台云端电脑，在上面加载网页和应用，直接点击、填表。
- 创始人称后台任务不需要即时返回，用空闲集群批处理、异步运行；日程检查之类的工作可以在任意时间「静默苏醒」后执行。
- 云端电脑能从用户邮箱里取验证码，完成两步验证和注册，端到端走完流程。内测期这项能力就引起过测试者的担心。
- 像人一样高频访问网站会被平台识别和封禁：有用户报告清理 Gmail 时被谷歌踢出，有用户因它高频请求 Resy 而被封号。
- 算力是主要约束。创始人称邀请制下算力成本每周翻倍，算力需要提前数月采购。环境配置、是否持久、并发和超时，资料都没有说明。

## 自己的一部手机和一台电脑

官网写明 Instinct「能像你一样使用手机和电脑」，用户这边没有新界面（[官网首页]({{< relref "/docs/instinct/sources/official/2026-11-05-instinct-homepage" >}})）。2026-09-28 C 轮公告的说法是：Instinct 有自己的虚拟手机和虚拟电脑，像人类助理一样加载网页和应用、直接交互；SiliconANGLE 据此推断它的核心基于计算机使用（computer use）范式（[SiliconANGLE：C 轮与新功能]({{< relref "/docs/instinct/sources/media/2026-09-28-siliconangle-series-c" >}})）。创始人在 Z Finance 整理的访谈中称，Instinct 有专属电话号码、邮箱和一台完整配置的云端电脑，用户能在互联网上自己办成的事，原则上它都能代办（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。

第三方资料的描述一致：Top5Apps 称它代用户操作「一部手机和一台电脑」（[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})），六款主动型智能体对比一文称它运行在「Instinct 自己的手机和电脑」上（[六款主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})）。一位美国投资人把 Muse、Instinct、ChatGPT Dot 和 Grok Bot 归为一类：都有自己的电脑，不占用他正在用的那台，会打开邮箱、Google Drive、DoorDash，点按钮、填输入框，而不只是调 API。这段话说的是四款产品，没有单独讲 Instinct（[特工宇宙：投资人用四款 Agent]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})）。

复杂内容的呈现也在云端完成：创始人称，度假行程、婚礼筹备这类信息可以在后台即时生成全功能的 Web 界面或交互式 Mini App（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。Android Authority 作者用它做过一个网页版的互动婚礼请柬（[Android Authority：一个月使用]({{< relref "/docs/instinct/sources/media/2026-10-17-androidauthority-one-month" >}})）。

## 后台批处理与「静默苏醒」

创始人称主动式智能体有自己的「作息」：早上 6 点醒来梳理当天日程和未读邮件，下午 4 点发现行程冲突时再介入。这类后台任务不需要同步返回，用空闲集群批处理、异步离线运行（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。Z Finance 另一篇文章转述播客内容：后台任务推迟到低谷时段，用低价的点存（spot）算力异步批处理（[Z Finance：齐俊元与伪命题]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})）。成本和吞吐的数字见 [模型]({{< relref "/docs/instinct/analysis/models" >}})。

据甲子光年转述，一个流传很广的故事是：Instinct 在后台连续工作 18 小时，发邮件、查录播、问客服，最后联系到美网的剪辑人员，帮用户拿到现场大屏幕的视频（[甲子光年：是不是好生意]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})）。这是未注出处的转述，不能当作可核实的案例。

## 从邮箱取验证码：端到端执行与平台封禁

创始人举例：用户让 Instinct 用云端电脑登录网站，从邮箱里自动取验证码完成两步验证，再退订服务（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。内测期，一位测试者发现它能从邮箱收件箱取出注册验证码，通过 Resy 订餐厅，并对此表示担心（[TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})）。2026-08-24 的报道还引用服务条款：Instinct 可以从用户设备接收屏幕截图、光标移动和键盘输入（[TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})）。条款写的范围比「云端电脑」大，但资料里没有用户端设备采集如何实现的描述。

像人一样操作网站，也会像机器人一样被拦。据 36氪转述 The Verge 等报道，有用户称 Instinct 清理 Gmail 收件箱时被谷歌踢出系统（[36氪：Agent 遭集体拉黑]({{< relref "/docs/industry/sources/media/2026-10-21-36kr-agents-blocked" >}})）；WIRED 引用的一位 X 用户称，它在尝试预订时约每小时请求 Resy 的 API 200 次，导致他被 Resy 封禁（[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})）。平台拦截的整体情况见 [连接器]({{< relref "/docs/instinct/analysis/connectors" >}})。

## 算力是开放的瓶颈

据甲子光年转述创始人的播客发言，Instinct 在现有邀请制下算力成本每周翻倍；算力交付有滞后，只能提前采购，所以一直不开放注册（[甲子光年：是不是好生意]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})）。创始人在访谈中称，自己约 40% 的精力花在防止「算力空置」和「算力击穿」上（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。Top5Apps 实测时，Instinct 满负荷运行、被限流，「回复可能更慢」（[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。

推断：从「每周翻倍」「提前数月采购」和限流这几条看，Instinct 的开放节奏主要受算力供给限制，而不是产品成熟度。资料没有给出单用户算力配额或任务并发上限，这一点无法核实。

行业资料给出的成本只能当背景参考：海外独角兽社群讨论转述，一个团队估计桌面虚拟机即使按 AWS 大客户价，每个智能体每月也要 10 到 15 美元，这说的不是 Instinct（[海外独角兽：PA 社群讨论]({{< relref "/docs/industry/sources/community/2026-10-23-haiwaidujiaoshou-discussion" >}})）。中金认为，独立助手的外部模型、账户连接、电话与浏览器执行会持续产生服务费用（[中金：消费级 AI 的破晓时分]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})）。

## 资料缺口

- 云端电脑和虚拟手机的规格、操作系统、是否每个用户一台、会话是否持久、登录状态如何保存。
- 服务条款里「从用户设备接收屏幕截图、键盘输入」靠什么客户端实现，是否已经上线。
- 单用户的算力配额、并发任务数、超时；限流的具体规则。
- 公司没有帮助中心或文档站（[官网首页]({{< relref "/docs/instinct/sources/official/2026-11-05-instinct-homepage" >}})），上面这些很难从官方渠道补齐。

## 主要资料

- 官方：[官网首页]({{< relref "/docs/instinct/sources/official/2026-11-05-instinct-homepage" >}})，「像你一样使用手机和电脑」。
- 媒体：[SiliconANGLE：C 轮与新功能]({{< relref "/docs/instinct/sources/media/2026-09-28-siliconangle-series-c" >}})，C 轮公告中的虚拟手机与电脑；[TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})，内测期取验证码与条款范围；[甲子光年：是不是好生意]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})，算力成本每周翻倍、18 小时故事；[Z Finance：齐俊元与伪命题]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})，点存算力批处理；[36氪：Agent 遭集体拉黑]({{< relref "/docs/industry/sources/media/2026-10-21-36kr-agents-blocked" >}})、[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})，平台封禁。
- 社区：[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})，创始人对云端电脑、后台批处理的描述；[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})，限流；[六款主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})、[特工宇宙：投资人用四款 Agent]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})，第三方描述。
