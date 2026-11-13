---
title: "Manus Cue：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Cue 的每个智能体有自己的云端电脑，与 Manus 共用基础设施；用户可以在应用里看它操作，关掉应用它仍在运行。实测到的是 Ubuntu 虚拟机，配置与出口 IP 因人而异，IP 常落在非主要西方国家，影响注册与验证。
---

## 概要

- 官方称每个智能体都有「自己的电脑」，在自己的机器上完成任务，Cue 与 Manus 构建在同一套基础设施上。规格、持久化、休眠与回收规则，官方资料都没有写。
- 唯一的一手环境报告来自 xiangxiang103：Ubuntu 24.04.4 LTS、8 核、15.6 GiB 内存、54 GB 磁盘，出口 IP 在孟加拉国。作者转述其他测试者看到的配置和 IP 地区都不同。
- 用户能在应用右侧看到「智能体的电脑」画面，群聊里也可以展开；关掉应用后智能体继续运行。
- 社区反馈集中在出口 IP：重启容器换「住宅」IP，常落到巴基斯坦、埃及、越南等地，影响本地服务注册和短信验证。这些反馈都是转述，没有注明原帖。

## 每个智能体一台云端电脑

发布文写明，Cue 中每个智能体都有自己的电子邮件、电话号码、钱包和电脑，能「在自己的机器上把一项任务做完」；Cue「构建在与 Manus 相同的基础设施之上」（[Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})）。应用商店介绍也把「专属电脑」列为每个 Cue 的四项身份之一（[Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}})）。据 cellcog.ai 的引用，Google Play 10-08 版的介绍在这句前写着「视可用情况而定（Depending on availability）」，11-04 版已删去（见 [Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}}) 的日期说明）。

xiangxiang103 实测新建的智能体开箱即有邮箱和电脑，电话和钱包默认关闭（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。中金、鸿煊等行业资料重述了「每个 Agent 拥有邮箱、电话、钱包和电脑」的官方说法，没有新的信息（[中金]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。

## 实测到的环境：Ubuntu 虚拟机，配置因人而异

xiangxiang103 让智能体自报环境，得到 Ubuntu 24.04.4 LTS、8 核 CPU、15.6 GiB 内存、根磁盘 54 GB，公网 IP 归属孟加拉国库尔纳；可用工具包括网页搜索与抓取、文件读写、命令行、任务委派、应用内浏览器、文件传递、授权历史检索和设备信息（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。作者转述，另有博主测到 4 核至强加 16G 内存、IP 在印度，还有人查出是家宽 IP，作者的结论是「每个人分到的机器不一样」（同上）。

Manus 本体的 Cloud Computer 在帮助中心被定义为持续运行的 Ubuntu Linux 虚拟机（据[财经涂鸦]({{< relref "/docs/manus-cue/sources/media/2026-09-29-caijingtuya-xiaohong-on-cue" >}})转述）。Cue 实测到的环境与之一致，但官方没有说明 Cue 的电脑与 Manus 的 Cloud Computer 是否是同一种产品。App Store 内购里单列了一项 39 美元的 Cloud Computer（[App Store 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-05-app-store-listing" >}})），xiangxiang103 转述网友实测为「Linux 云电脑 39 美元一个月」（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）；免费附带的电脑与这项付费电脑有什么区别，资料没有说明。

推断：从实测看，Cue 的「电脑」至少在早期是一台通用 Linux 云主机，模型通过命令行和应用内浏览器操作它；配置不统一，说明它很可能直接取自 Manus 已有的云电脑资源池，而非为 Cue 单独设计。

## 用户可以看、关掉应用仍运行

xiangxiang103 用的 Mac 版右侧有「智能体的电脑」面板，可以实时看智能体操作的画面；关掉应用后智能体仍在运行（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。硅星人在群聊中也从右侧展开过智能体的电脑屏幕查看实际操作（[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})）。资料只写了「看」，没有提到用户能否接管这台电脑。

肖弘称云上 Computer Use「不会和我自己争抢电脑光标」，说的是 Manus 本体（[财经涂鸦]({{< relref "/docs/manus-cue/sources/media/2026-09-29-caijingtuya-xiaohong-on-cue" >}})），xiangxiang103 把这句话用在 Cue 的云电脑上（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。飞雪谈AI 称「个人云电脑」的概念最早由 Manus 提出，作用是 7×24 小时在线、不因用户关机而中断（[飞雪谈AI]({{< relref "/docs/industry/sources/community/2026-10-16-feixue-personal-agent-comparison" >}})）。

## 出口 IP 落在非主要西方国家

Datawhale 转述用户反馈：重启容器会换「住宅」IP，有人连试三次得到巴基斯坦、埃及、越南，别人得到菲律宾、哥伦比亚，几乎看不到主要西方国家（[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。鸿煊重述了这一反馈，并指出它直接影响本地服务注册与短信验证（[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。两篇都没有注明原帖出处。

xiangxiang103 实测中，智能体用 @bot.cue.im 邮箱和云电脑注册的 Claude 账号约 22 分钟后因「可疑信号」被暂停，作者推测与机器人邮箱域名、机房 IP 和自动化操作有关（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})），见[实际效果与可靠性](../reliability/)。

推断：出口 IP 不在用户所在地区，对美国本地生活服务（Cue 官网示例的主要场景）和风控严格的平台都是障碍。这与「给智能体独立身份」的路线有关：智能体以自己的身份、从自己的机器出发办事，平台看到的是一个陌生账号加一个异地 IP。

## 资料缺口

- 官方的电脑规格、持久化方式、休眠与回收、并发与超时；同一账号下多个智能体是否各有一台电脑。
- 免费附带的电脑与 39 美元 Cloud Computer 内购的区别。
- 出口 IP 的分配规则、能否指定地区，IP 问题的原始反馈出处。
- 用户能否接管智能体的电脑。

## 主要资料

官方
- [Manus 2.0 发布文]({{< relref "/docs/manus-cue/sources/official/2026-09-28-introducing-manus-2-0" >}})：每个智能体一台电脑，与 Manus 共用基础设施
- [Google Play 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-04-google-play-listing" >}})：「专属电脑」；10-08 版曾有「视可用情况而定」
- [App Store 介绍]({{< relref "/docs/manus-cue/sources/official/2026-11-05-app-store-listing" >}})：Cloud Computer 内购 39 美元

媒体
- [财经涂鸦]({{< relref "/docs/manus-cue/sources/media/2026-09-29-caijingtuya-xiaohong-on-cue" >}})：Manus Cloud Computer 是 Ubuntu 虚拟机；肖弘谈云上 Computer Use
- [硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})：群聊中查看智能体电脑屏幕

社区
- [xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})：环境自报、配置因人而异、电脑面板、注册被封
- [Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})：出口 IP 反馈（转述）
- [飞雪谈AI]({{< relref "/docs/industry/sources/community/2026-10-16-feixue-personal-agent-comparison" >}})：个人云电脑概念
