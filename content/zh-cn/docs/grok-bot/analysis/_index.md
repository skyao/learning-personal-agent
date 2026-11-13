---
title: "Grok Bot 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Grok Bot 是 xAI（SpaceXAI）推出、运行在 Cursor 托管云上的常驻 Bot 团队，主打工作场景，随 X、Cursor、SuperGrok 套餐提供；分析覆盖截至 2026-11-12 收集的 56 篇 Grok Bot 资料和 35 篇行业资料。
---

## 概要

- Grok Bot 卖的是「一队有名字的 Bot」，不是单个助理。每个 Bot 有自己的职责、记忆和例程，但同一用户的所有 Bot 共用一台云端微虚拟机，文件、浏览器会话和登录状态互通。官方文档明说 Bot 之间「不是安全边界」。（[运行环境](runtime/)、[安全](security/)）
- 产品由 xAI 出名、Cursor 承载：账号、计费、云端计算机、连接器后端、隐私模式和企业管理都沿用 Cursor 的体系，xAI 自己的页面几乎没有数据说明。（[隐私](privacy/)、[连接器](connectors/)）
- 持续执行以例程为核心，可按时间表或 Slack、GitHub、邮件、webhook 等事件触发，社区评为事件触发最丰富的托管型智能体。实际约束主要是用量额度，而不是功能。（[持续执行](continuous-execution/)）
- 安全靠独立审查模型 Auto Review 加审批卡，凭证经 Vault 和安全表单填入、不让模型看到。但已有两起公开问题：一个 Bot 读到的银行数据被另一个 Bot 发到公司 Slack；有研究者报告能伪造 Web Bot Auth 签名。资料中都没有厂商回应。（[安全](security/)）
- 没有单独订阅，一直是套餐权益。2026-10-12 起新客户从 The X Subscription 的 Premium（每月 30 美元）起步，用量与 Cursor、Grok 共用每周池。2026-11-01 Musk 以服务成本「高得不可持续」为由收紧限额，用量上限是用户最集中的不满。（[开放与价格](access-pricing/)、[商业与规模](business/)）
- 工作类横向实测中多次排第一，「就是能用」、成品可交付是最一致的评价。弱项是日常生活任务、多 Bot 长期运行的稳定性和编码修复。（[实际效果与可靠性](reliability/)）
- 用户看不到、也选不了模型：系统按任务在 xAI 第一方模型和第三方模型间路由。第三方对底层模型的说法互相矛盾。（[模型](models/)）

## 定位

官方把 Grok Bot 定为「AI 队友」：Bot 有自己的云端计算机，能登录用户已在用的工具，在应用和收件箱之间端到端完成工作，只在需要审批时回来找人（[官方发布]({{< relref "/docs/grok-bot/sources/official/2026-08-11-introducing-grok-bot" >}})）。设计文章强调对象是持久的 Bot 而不是一次性对话，「界面对人的要求应该更少」（[设计文章]({{< relref "/docs/grok-bot/sources/official/2026-09-03-designing-grok-bot" >}})）。官方文档建议按岗位拆分 Bot，工作、工具、审批边界或时间表不同就建单独的 Bot（[文档：工作方式]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})）。

厂商关系比其他跟踪产品复杂。发布稿署名 xAI（SpaceXAI），Cursor 于 2026-08-14 成为 SpaceXSI 的一部分（[客服用例]({{< relref "/docs/grok-bot/sources/official/2026-09-22-grok-bot-customer-support" >}})）；Grok Bot 用 Cursor 账号登录，运行在 Cursor 托管的云计算机上，与 Grok 聊天应用的付费墙和每周上限无关（[FAQ]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})、[文档：安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})）。同时它与 X 平台绑定：X 连接器、帖子里 @bot、X Chat、X Money 付款，2026-10 起随 The X Subscription 提供（[与 X 集成]({{< relref "/docs/grok-bot/sources/official/2026-08-29-grok-bot-and-x" >}})、[帮助：套餐]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-plans" >}})）。据 TechCrunch，Grok Bot 被当作刚上市的 SpaceX 的成功案例（[TechCrunch：用量限制收紧]({{< relref "/docs/grok-bot/sources/media/2026-11-02-techcrunch-throttles-limits" >}})）。

社区资料普遍把它归入偏工作场景的一类，称其为「数字同事团队」，与偏个人生活的 Muse 相对（[黑咖啡全景]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})）。与其他跟踪产品的主要差异：

| 对比对象 | 差异 | 资料 |
| --- | --- | --- |
| OpenAI Dots | 一队 Bot 共用一台电脑，对一个 dot 一台电脑；Grok Bot 入门价更低（30 美元对 Pro 100 美元起） | [入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}}) |
| Meta Muse | 跨应用的工作选 Grok Bot，手机上的个人任务选 Muse；Muse 有免费档和打电话、个人生活连接器 | 同上；[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}}) |
| Claude Duet | Duet 是一个主线程而不是一队，且不能接管电脑 | [入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}}) |
| OpenClaw 等自部署 | 托管、开箱即用，但不能选模型，可控性低 | [Claire Vo 评测]({{< relref "/docs/grok-bot/sources/community/2026-08-18-chatprd-claire-vo-grokbot" >}}) |

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-08-11 | 以 beta 发布 | [官方发布]({{< relref "/docs/grok-bot/sources/official/2026-08-11-introducing-grok-bot" >}}) |
| 2026-08-26 | 扩大到所有 SuperGrok、Cursor Pro、Cursor Teams 套餐（更新日志 v0.27.0 记为 08-25） | [扩大套餐]({{< relref "/docs/grok-bot/sources/official/2026-08-26-grok-bot-more-plans" >}}) |
| 2026-08-29 | X 连接器第一个版本 | [与 X 集成]({{< relref "/docs/grok-bot/sources/official/2026-08-29-grok-bot-and-x" >}}) |
| 2026-09-03 | 向所有 Enterprise 团队开放，两周免费 | [企业版]({{< relref "/docs/grok-bot/sources/official/2026-09-03-grok-bot-for-enterprise" >}}) |
| 2026-09-23 | 研究者向 xAI 披露 Web Bot Auth 签名可被伪造，10-07 公开 | [nightd]({{< relref "/docs/grok-bot/sources/community/2026-10-07-nightd-impersonating-grok-bot" >}}) |
| 2026-09-28 | Team Bots 公开 beta（更新日志 v0.61.0 记为 09-26） | [Team Bots]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}}) |
| 2026-10-02 | 主 Bot 开始主动寻找可接手的工作（v0.66.0） | [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}}) |
| 2026-10-07 | Cybernews 报道 Bot 把 CEO 银行数据发到公司 Slack | [Cybernews]({{< relref "/docs/grok-bot/sources/media/2026-10-07-cybernews-bank-data-slack" >}}) |
| 2026-10-11 | Bot 自有邮箱、X Money 与 Link 付款（v0.70.2） | [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}}) |
| 2026-10-12 | 新客户改从 The X Subscription 入手 | [入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}}) |
| 2026-10-15 | 据报道亚马逊阻止 Grok Bot 下单，Musk 回复「也许我们应该创办一个亚马逊的竞争对手」 | [Not a Tesla App]({{< relref "/docs/grok-bot/sources/media/2026-10-15-notateslaapp-amazon-blocked" >}}) |
| 2026-10-22 至 10-23 | Pages、视频生成、Shop Pay、Vault（v0.75.x） | [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}}) |
| 2026-10-26 | 据财联社转述，日活超过 60 万（9 月初不足 10 万） | [黑咖啡全景]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}}) |
| 2026-11-01 | Musk 确认收紧用量限制，称服务成本相对收入「高得不可持续」 | [TechCrunch]({{< relref "/docs/grok-bot/sources/media/2026-11-02-techcrunch-throttles-limits" >}}) |
| 2026-11-06 | 更新日志最新版本 v0.79.3 | [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}}) |

## 整体架构

用户在 Grok Bot 的桌面或手机应用里，用类似消息应用的聊天线程与多个 Bot 对话，也可以在 X、Slack、Microsoft Teams 里找它们。每个用户一台位于美国、由 Cursor 托管的 Firecracker 微虚拟机，所有 Bot 在上面工作，各有自己的屏幕，共享文件和登录状态；空闲时休眠，按需唤醒。第三方服务优先走 OAuth 应用（令牌留在 Cursor 后端），其次是与 Cursor 通用的 MCP、插件和技能，没有接口的网站由浏览器操作，登录信息来自 Vault 或 1Password。每个 Bot 有自己的记忆，可挂最多 50 个按时间或事件触发的例程。写操作先经 Auto Review 评估，再由用户在审批卡上批准；非用户当场要求的外发邮件一律停在草稿。模型由系统按任务选择。费用计入所属套餐的每周用量池，超出部分用预付额度。企业版另有网络控制、推理钩子、操作记录、保留期和数据驻留。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境](runtime/) | 每用户一台 Cursor 云端 Firecracker 微虚拟机，所有 Bot 共用；早期官方稿写「每个 Bot 有自己的计算机」，后来的文档改为按用户分配 |
| [记忆与上下文](memory/) | 记忆按 Bot 隔离、由 Bot 自行保存，没有管理界面；Team Bot 的共享学习需管理者批准 |
| [持续执行](continuous-execution/) | 例程按时间或事件触发，每 Bot 最多 50 个、每小时合计 300 次；用量是主要约束 |
| [连接器](connectors/) | OAuth 应用、MCP、浏览器三条路径，偏工作场景；遭亚马逊拦截 |
| [交互渠道](channels/) | 自有应用为主，外延到 X、Slack、Teams；每个用户一个永久 mail.grokbot.com 邮箱，无人值守不发信 |
| [设备](devices/) | 桌面和手机只做聊天与审批；用户电脑可作本地执行端和网络出口；没有专用硬件 |
| [模型](models/) | 系统按任务选模型，用户不可选；第三方说法有 Grok 4.7 与 Claude Opus 5.5 两种 |
| [安全](security/) | Auto Review 加审批卡，凭证不进模型；Bot 之间不是安全边界，已有两起公开问题 |
| [隐私](privacy/) | 沿用 Cursor 的隐私模式和条款；共用计算机是已发生隐私事件的根源 |
| [开放与价格](access-pricing/) | 无单独订阅；X Subscription 30/100/200 美元三档，共用每周池；11 月收紧限额 |
| [商业与规模](business/) | 没有官方用户数和收入；日活数字来自第三方追踪；Musk 承认成本过高 |
| [实际效果与可靠性](reliability/) | 工作类实测多次第一；用量上限、多 Bot 长期运行不稳定、编码修复不可靠 |

## 资料缺口

- 用户数、付费人数和收入的官方数字；日活「超过 60 万」的一手出处。
- The X Subscription 的官方价格页，各档 Grok Bot 可用的额度，11 月收紧后的新限额。
- 计算机的规格、休眠阈值、并发上限；「每个 Bot 一台」改为「按用户一台」是措辞变化还是架构变化。
- 第一方模型的名称与路由规则；子处理方名单。
- xAI 与 Cursor 之间的数据流向，个人用户的默认训练设置与保存期限。
- 厂商对 Slack 银行数据事件、Web Bot Auth 签名问题、亚马逊拦截的回应；漏洞赏金与独立安全审计。
- 电话功能的官方说明；Microsoft Teams 渠道的帮助文档；Tesla 车载集成的形态。
- 用户自己的实测（`exploration/` 为空）和数周以上的长期使用记录。
