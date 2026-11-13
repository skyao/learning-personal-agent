---
title: "蚂蚁灵光 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  灵光 2.0 是蚂蚁集团 2026-10-27 在原灵光 App 上重构推出的个人 AI 助理，定位「能管事」：在云端持续盯价、汇总、提醒，个人数据以支付宝账单为核心，被多家媒体称为国内大厂首个 Personal Agent；分析覆盖截至 2026-11-10 收集的 16 篇灵光资料和 7 篇涉及灵光的行业资料。
---

## 概要

- 灵光 2.0 不是新产品，而是把 2025 年 11 月上线的灵光 App（以一句话生成小应用为主打）重构成个人助理。官方称之为从「任务执行者」向「任务管理者」的转变，媒体多称它是国内大厂首个 Personal Agent，也是「中国版」「中国化」的 Muse。
- 核心是「帮我管」：每件交给灵光的事生成一张事务卡片，灵光在云端持续盯价格、定时汇总群消息和开销、在节点主动提醒，检查频率常由它自己决定。实测中这部分评价最好。（[持续执行](continuous-execution/)、[记忆与上下文](memory/)）
- 个人数据以授权后的支付宝账单为核心，另接邮箱、钉钉、飞书、网盘、米家和手机系统服务。账单只能看到扣款记录，其他支付渠道不在其中。（[记忆与上下文](memory/)）
- 连接面扩张快（11 月 4 日外部连接器达 40 项），但能读不能写：发消息被拦截、转账无权限、付款只能跳转支付宝、淘宝进不去。蚂蚁与阿里在数据接口上合规隔离，千问能做的淘宝操作灵光做不到。（[连接器](connectors/)）
- 安全以蚂蚁 APASS 为中心，授权密钥与智能体分离托管；高风险动作目前基本交回用户。资料中没有提示注入防护或安全事件的信息。（[安全](security/)）
- 灵光自报 2.0 上线一周管理超 116 万项事务、用户超 2000 万，口径不明。商业模式未公开，目前对个人用户免费；在蚂蚁内部是探索前沿形态的试验田，验证后的能力有望用到阿宝。（[商业与规模](business/)）
- 评测者的共同判断是「有管事的意图，还没有办事的工具」，瓶颈在平台权限而不在模型。所有实测都在发布前后两三周内，没有长期数据。（[实际效果与可靠性](reliability/)）

## 定位

官方发布稿称，灵光已从多模态 AI 助手升级为主动式个人智能体，实现从「任务执行者」向「任务管理者」的转变（[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})）。App Store 简介称它是「能管事的个人助理」，口号由「让复杂，变简单」改为「平凡日子里的小目标，交个灵光就好」（[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})、[三哥：1.0 与 2.0]({{< relref "/docs/lingguang/sources/community/2026-10-13-chanpinbiji-1-0-vs-2-0" >}})）。36氪强调灵光没有把定位放在「什么都替用户做」，而是记住、跟进、提醒（[36氪]({{< relref "/docs/lingguang/sources/media/2026-10-27-36kr-lingguang-2-china-muse" >}})）。

2.0 是在原 App 上的重构：「对话」tab 改名「灵光」，去掉打电话和开眼两个 tab，新增「我的生活」和「个人」，应用生成和灵光圈仍保留但权重降低（[三哥：1.0 与 2.0]({{< relref "/docs/lingguang/sources/community/2026-10-13-chanpinbiji-1-0-vs-2-0" >}})）。在蚂蚁的 AI 布局中，阿福做健康，阿宝依托支付宝服务大众日常需求，灵光负责前沿探索（[36氪]({{< relref "/docs/lingguang/sources/media/2026-10-27-36kr-lingguang-2-china-muse" >}})、[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})）。

与其他跟踪产品及国内同类产品相比，资料中的主要差异是：

| 对比对象 | 差异 | 资料 |
| --- | --- | --- |
| Meta Muse | 智东西称灵光形式上是「中国版」Muse，内容上是「中国化」Muse：Muse 靠邮箱等开放通道和云端浏览器，灵光须接入支付宝、钉钉、飞书、米家等本土服务。光子星球称 Muse 依托社交数据，灵光靠场景闭环。36氪称 Muse 强调自主执行，灵光重在管事 | [智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}})、[光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}})、[36氪]({{< relref "/docs/lingguang/sources/media/2026-10-27-36kr-lingguang-2-china-muse" >}}) |
| Today | 新眸认为 Muse 偏交易闭环的执行代理，Today 偏长期关系与陪伴，灵光处在「办事」与「陪伴」之间 | [新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}}) |
| 千问 Go（未跟踪） | 都想用自家服务承接个人事务；千问能进淘宝购物车、在 App 内点单，灵光不能；比价时千问只查淘宝，灵光比对京东和淘宝 | [极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})、[生活有变量]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}}) |
| LightVela（未跟踪） | 以微信、QQ、企业微信、飞书、钉钉为入口，用户自配记忆、模型与技能；灵光是独立 App，强调授权后主动发现 | [潜在工作室]({{< relref "/docs/industry/sources/community/2026-11-10-qianzai-answer-to-follow-up" >}}) |

白鲸技术栈认为灵光与 Muse 的差异「未必来自 Agent 框架，而来自它站在支付宝里」：个人上下文、服务网络、云端持续运行三者缺一，就会退化为聊天机器人、点屏工具或提醒器（[白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}})）。新眸认为在国内，外部智能体的核心约束从「集成」变成了「授权与准入」（[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})）。AI故事计划称国庆后大厂「下场者稀疏，最后只有灵光交出了答卷」，同时质疑国内是否需要单独的 Personal Agent，个人助理能力可能长进豆包、千问等通用助手（[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})）。

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2025-11-17 | 灵光 App 首次发布（App Store，UTC），主打全模态对话与闪应用；官方称 6 天下载超 200 万 | [App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})、[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}}) |
| 2026-03 | 月活跌出 AI 类 App 榜单（此前一度进前十） | [AI故事计划：二线厂]({{< relref "/docs/industry/sources/media/2026-11-05-aigushijihua-second-tier-personal-agent" >}}) |
| 2026-04-24 | 1.0.70 上线灵光圈与「闪应用创作者激励计划」 | [App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}}) |
| 2026-05-29 | 《灵光用户服务协议》当前版本日期 | [极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}}) |
| 2026-10-11 | 据新浪科技报道，灵光 2.0 内测，新增「我的生活」板块 | [AI新榜]({{< relref "/docs/industry/sources/media/2026-10-12-aixinbang-do-people-need" >}}) |
| 2026-10-13 | 内测并邀请部分用户公测，评测文章陆续发出 | [三哥：1.0 与 2.0]({{< relref "/docs/lingguang/sources/community/2026-10-13-chanpinbiji-1-0-vs-2-0" >}})、[特工宇宙：内测]({{< relref "/docs/lingguang/sources/community/2026-10-13-tegongyuzhou-beta-hands-on" >}}) |
| 2026-10-26 | App Store 1.3.80 起更新说明写「灵光2.0全新升级」 | [App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}}) |
| 2026-10-27 | 蚂蚁发布灵光 2.0，在中国的 iOS、Android 和 LingGuang.com 上逐步开放 | [官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}}) |
| 2026-10-28 | App Store 2.0.0 版（UTC） | [App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}}) |
| 2026-11-02 至 11-05 | 2.0.20、2.0.30、2.0.60 连续发布 | [App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}}) |
| 2026-11-04 | 新一轮升级，新增哈啰打车、麦当劳、微信读书等，外部连接器达 40 项 | [亿邦]({{< relref "/docs/lingguang/sources/media/2026-11-05-ebrun-lingguang-weekly-tasks" >}}) |
| 2026-11-05 | 公布上线一周数据：管理超 116 万项事务、执行超 360 万次任务、用户超 2000 万 | [亿邦]({{< relref "/docs/lingguang/sources/media/2026-11-05-ebrun-lingguang-weekly-tasks" >}})、[财经网]({{< relref "/docs/industry/sources/media/2026-11-06-caijingwang-transaction-management" >}}) |

## 整体架构

用户在灵光 App（iOS、Android）或 LingGuang.com 上与它对话，交代一件事后，灵光在「我的生活」中生成一张事务卡片，记下目标、条件和进展（[记忆与上下文](memory/)）。任务在一台独立的云端实例上运行，关掉 App 后继续；环境里有浏览器，可安装 Skill 和命令行工具（[运行环境](runtime/)）。灵光按自己排定或用户约定的频率去检查价格、账单、群消息，有变化或到节点时通过 App 通知提醒（[持续执行](continuous-execution/)）。

数据和服务的主干是支付宝的账单、会员与出行服务，外围通过授权、MCP、CLI 和 Skill 接入钉钉、飞书、邮箱、米家、滴滴等 40 项外部服务（[连接器](connectors/)）。账号与授权凭证由 APASS 托管，智能体不直接接触密钥；转账、付款、对外发消息目前做不到，交还用户在原 App 中完成（[安全](security/)）。商业模式未公开，个人用户免费使用（[商业与规模](business/)）。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境](runtime/) | 每个用户一台独立云端实例，关 App 后继续运行；内测作者称是可自装工具的 Linux 云电脑。云端浏览器进不了淘宝；规格、可见性、额度未公布 |
| [记忆与上下文](memory/) | 记忆以事务卡片为单位，偏好与条件在后续任务中沿用；核心数据是支付宝账单。查看、编辑、删除记忆的方式没有资料 |
| [持续执行](continuous-execution/) | 盯价、定时汇总、节点提醒，频率常由灵光自定，评测者认为主动性强；退订、付款等决定由用户确认。没有数量上限和长期稳定性资料 |
| [连接器](connectors/) | 11-04 达 40 项，接入方式包括授权、MCP、CLI、Skill；读多写少，付款与发消息做不到，蚂蚁与阿里之间有合规隔离 |
| 交互渠道 | 资料不足，不单独成页。入口只有灵光 App 与 LingGuang.com，支持语音对话和摄像头识别；通知在 App 内。资料中没有短信、微信等外部渠道，也没有灵光自己的邮箱或号码（[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})、[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})） |
| 设备 | 资料不足，不单独成页。终端以手机为主（iOS 15.0 及以上），网页版次之；智能家居与汽车控制通过米家、车企等连接器实现，写在[连接器](connectors/)中。没有专用硬件 |
| 模型 | 资料不足，不单独成页。资料没有说明灵光 2.0 使用哪个模型；AI故事计划只提到蚂蚁有百灵模型（[AI故事计划：二线厂]({{< relref "/docs/industry/sources/media/2026-11-05-aigushijihua-second-tier-personal-agent" >}})） |
| [安全](security/) | APASS 托管凭证，授权按需、可撤销；转账、付款、对外发送在实测中都被挡住；协议规定 Agent 操作视为用户本人操作 |
| 隐私 | 资料不足，不单独成页。官方只称 APASS 把隐私保护嵌入执行过程、授权可随时撤销；是否用于训练、保存期限、导出删除、群聊中他人信息的处理都没有资料（[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})） |
| 开放与价格 | 资料不足，不单独成页。2.0 在中国逐步开放，发布前约两周起小范围内测；App Store 标为免费、提供 App 内购买，白鲸技术栈称现阶段对个人用户免费；官方未公开收费计划（[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})、[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})、[白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}})） |
| [商业与规模](business/) | 一周 116 万项事务、用户超 2000 万（厂商自报）；商业模式未公开；交易未在智能体内闭环，抽佣暂时无从谈起 |
| [实际效果与可靠性](reliability/) | 账单、盯价、汇总、内容生成做得好；付款、下单、发消息做不到。没有完成率和长期数据 |

## 资料缺口

- 官方一手资料很少：只有一篇经 Business Wire 分发的发布稿和 App Store 页。缺帮助文档、隐私政策、《灵光用户服务协议》原文、APASS 的技术说明。
- 运营数据的口径：「2000 万用户」是否含 1.0 时期，2.0 的活跃与留存，「事务」「任务」的定义；IT之家 11-08 报道原文。
- 底层模型。
- 收费计划与 App 内购买内容；是否引入交易佣金。
- 40 项连接器的清单与读写范围；11-04 新增连接器的实测；支付宝 AI付 何时向灵光开放。
- 发布一个月以上的长期使用记录；用户自己的实测（`exploration/` 为空）。
- 隐私与数据处理：训练用途、保存期限、断开授权后的数据处理、群聊中他人信息。
