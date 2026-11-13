---
title: "Claude Duet：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Claude Duet 在 Anthropic 云端自己的计算机上工作，浏览器另放在一台专用虚拟机里，模型只能用固定命令驱动它；用户看不到、也不能接管这个浏览器，Duet 也访问不到用户本机的文件。
---

## 概要

- 官方称 Duet 用「一台基于云的计算机」工作，带自己的浏览器，用户的手机和电脑关着也能继续运行。
- 浏览器单独运行在一台云端专用虚拟机上，与模型和智能体所用的计算机分开；智能体只能用打开页面、点击、输入等固定命令驱动它，网站代码和 Cookie 留在浏览器机器上。这是官方资料里写得最具体的一层，主要为凭证隔离服务（见[安全]({{< relref "/docs/claude-duet/analysis/security" >}})）。
- 环境对用户不透明：截至 2026-11-12 的资料，用户不能观看 Duet 的浏览器，也不能接管；Duet 看不到用户计算机上的文件，能读取用户在 Claude 中的工作但不能修改。这是它与 Muse、Dots 最明显的差别。
- 虚拟机规格、持久化、休眠与回收、并发与超时，官方都没有公布，资料库里也没有用户对 Duet 环境的实测。
- 评测者反映后台工作慢，多个线程常要 10 分钟以上才完成或请求权限。

## 云端计算机加一台专用浏览器虚拟机

发布稿称 Duet「有一台带自己浏览器的虚拟机」，不需要用户的笔记本或手机开着；用户发一条简短消息描述任务，它在后台自己决定用哪些应用和步骤，完成或需要审阅时通知用户（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。帮助文档写明，对没有连接器的网站，Duet 使用「它在云端的自有浏览器」（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。

安全文章把浏览器和智能体分开描述：浏览器运行在云端一台专用虚拟机中，与模型及智能体所用的云计算机分离；智能体只通过一组固定命令（打开页面、点击、输入）驱动浏览器，网站代码和 Cookie 留在浏览器机器上，返回给智能体的是页面文本和下载内容；经浏览器上传的文件与消息接受同样的敏感信息检查（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。登录时，密码在用户手机上加密，只在这台浏览器机器上解密（同上）。

完成的较大工作（研究报告、财务模型、幻灯片、仪表盘等）以文件形式出现在「制作（Make）」标签页（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。

## 用户看不到浏览器，Duet 看不到本机

帮助文档列出的局限包括：用户不能观看 Duet 在浏览器中工作，也不能接管；它看不到用户的所有项目，也看不到用户计算机上的文件；它可以读取用户在 Claude 中的工作，但不能修改（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。发布稿也写明它「目前还不能向你展示它的浏览器」（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。

这些限制在实测中都有体现。Chris Alarcon 第一天就碰到访问不到本地代码仓库、MacBook 和 Mac mini 的问题（[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})）。施言转述的一则 Reddit 案例中，Duet 投递简历时卡在 Cloudflare 验证码，既不能自己通过，也没有顺利交给用户接手（[施言：十个海外案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})，二手转述，无原帖链接）。

与其他跟踪产品对照，第三方资料的说法一致：Dots 的电脑可以由用户打开并接管，Muse 可以打开查看窗口、接管或停止任务，Duet 的浏览器则完全看不到（[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})、[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})、[PM九筒：什么是 Personal Agent]({{< relref "/docs/industry/sources/community/2026-10-28-pmjiutong-what-is-personal-agent" >}})）。详见 [Muse：运行环境]({{< relref "/docs/muse/analysis/runtime" >}})、[Dots：运行环境]({{< relref "/docs/dots/analysis/runtime" >}})。

推断：不让用户看到浏览器，和「智能体只能用固定命令操作浏览器、凭证只在浏览器机器上解密」的设计是一致的，可能是有意收窄的界面；但资料里没有 Anthropic 对这一取舍的解释，发布稿用的是「目前还不能」，说明它被当作待补的功能。

## 工作的层级与本地访问

有用户描述了 Duet 内部的权限层级：顶层能看到所有工作线但没有底层权限，频道权限更多但上下文受限，频道派生的子线程在特定的代码沙箱里工作时权限还可以再收窄；桌面应用可以访问用户允许的本地主机，作者只把它用于云端写完代码后的 QA 或部署（[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})）。这是单个用户的描述，官方资料没有对应说明。

桌面端的说法不一：发布稿列出的入口是 iOS、Android 与 claude.ai（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）；Claire Vo 测试 TestFlight 早期版本时没有桌面应用（[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})）；fig.blue 则提到桌面应用和本地主机访问。资料不足以判断桌面端是否已正式提供（见[交互渠道]({{< relref "/docs/claude-duet/analysis/channels" >}})）。

## 后台工作慢、用量大

官方说较大的任务（财务模型、演示文稿）需要更多模型轮次和后台工作（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})），这些工作计入套餐用量（见[开放与价格]({{< relref "/docs/claude-duet/analysis/access-pricing" >}})）。Claire Vo 称手机界面本身轻快，但邮件、幻灯片、编辑、社交等多个线程常要 10 分钟以上才完成、返回或请求权限（[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})）；ChatPRD 的九项任务横评也说 Duet「很慢」（[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。fig.blue 的感受相反，称 Duet 响应快，先给简短回复、把工作放到后台（[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})）。两者并不矛盾：前者说的是任务完成时间，后者说的是对话响应。

## 资料缺口

- 云端计算机和浏览器虚拟机的规格、是否每个用户独占、是否持久、休眠与回收机制、并发与超时上限。
- 多个频道、子线程是否共用同一台计算机。
- 桌面应用是否正式提供，本地主机访问的授权方式。
- 用户对 Duet 运行环境的实测（资料库目前没有 `exploration/` 资料）。

## 主要资料

- 官方：[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})（虚拟机与浏览器、不能展示浏览器）、[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})（浏览器虚拟机分离、固定命令）、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})（局限清单、Make 标签页）
- 社区：[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})（权限层级、本地主机）、[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})（无本机访问）、[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})（速度、无桌面端）、[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})（速度）、[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})、[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})（与 Dots、Muse 对照）、[施言：十个海外案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})（验证码案例，二手）
