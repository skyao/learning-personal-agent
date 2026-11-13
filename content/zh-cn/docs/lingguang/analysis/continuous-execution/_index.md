---
title: "蚂蚁灵光：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  「帮我管」是灵光 2.0 的核心：用户交代一件事，灵光自己定检查频率和提醒时点，在云端持续盯价格、汇总群消息、出周报，有变化时弹窗通知。实测中的定时与盯价大多按时发生，但都是一两周内的观察；数量上限、失败处理和长期稳定性没有资料。
---

## 概要

- 官方把 2.0 的变化概括为从「任务执行者」转向「任务管理者」：在用户授权后发现需求、发起跟进，订完机票后继续监控价格，宠物、家人生日、车辆年检等节点按授权范围安排提醒。
- 实测中最常见的用法是盯价（机票、商品、金价、房源）和定时汇总（每晚开销、钉钉群消息、邮件分拣、养车周报）。检查频率常由灵光自己决定，例如「每 12 小时看一轮」「每小时监控」。
- 灵光会主动把一个问题拆成多个时间点去提醒，评测者普遍认为它「主动」程度高。
- 主动性有边界：在授权范围内跟进，退订、改签、支付等决定由用户确认。
- 截至 2026-11-10 的资料，没有任务数量、时长上限，也没有暂停、失败重试的说明；长期任务能否按时交付还没有人验证。

## 从「任务执行者」到「任务管理者」

官方发布稿称，灵光 2.0 在用户明确授权后，利用已连接的信息和服务发现潜在需求，主动发起分析和跟进，在需要用户关注时提醒；例如机票或酒店订好后继续监控价格，更低时通知（[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})）。App Store 简介举的例子是机票降价、演唱会开票或加场、出行天气路况，「按约定持续关注，在需要你留意或行动时主动提醒」（[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})）。

新眸把「管事」拆成一个生命周期：识别需求、记住条件、拆解推进、持续监测、关键节点提醒、变化后调整、阶段性复盘（[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})）。各家媒体对官方口号的转写不一致：36氪写「记得住、能推进、会跟进、会调整」（[36氪]({{< relref "/docs/lingguang/sources/media/2026-10-27-36kr-lingguang-2-china-muse" >}})），光子星球写「记得住」「盯得住」「办得了」（[光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}})），极客公园写「记得住、盯得牢、办得了」（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})）。

## 实测中的持续任务

| 任务 | 做法 | 资料 |
| --- | --- | --- |
| 北京租房盯梢 | 先给方案，多轮对话敲定计划，之后按约定时间搜集并汇报 | [智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}}) |
| 金价 | 每小时监控大盘并更新（图注） | [智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}}) |
| 淘宝 iPhone 价格 | 灵光自定「整个双十一到 11 月 13 日，每 12 小时看一轮」 | [AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}}) |
| 双十一宠物囤货 | 半个月、5000 元预算，拆为六个板块，从 10 月 28 日核对基线价到 11 月 13 日收官排出盯盘时间表 | [白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}}) |
| 养车记账 | 每周日 20:00 出周报、每月最后一天 20:00 出月报，已排期 | [白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}}) |
| 每日开销 | 每晚 9 点半汇报当天开销，累计超 50 元提醒，大额支出每月总结，到点确实提醒 | [小朱]({{< relref "/docs/lingguang/sources/community/2026-11-04-aizxiaozhu-lingguang-domestic" >}}) |
| 钉钉群与邮件 | 每天总结群聊和邮件，发在对话里并推送通知；可定时获取指定群的信息 | [AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})、[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}}) |
| 邮件分拣 | 新建一个「事件」持续分拣 GitHub 通知邮件 | [光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}}) |
| 天气穿衣 | 只问了一次，灵光自己拆成三个时间点提醒；作者称「我可没让它定时」 | [AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}}) |
| 公司与人物动态 | 设置追踪并在有动态时通知，文章发表时尚未见结果 | [小象AI]({{< relref "/docs/lingguang/sources/community/2026-10-28-xiaoxiang-lingguang-2-hands-on" >}}) |

内测阶段，特工宇宙称让灵光长期处理不紧急消息、抓数据写周报、处理家校群待办，写稿时这些定时任务「还在安静地运行着」（[特工宇宙：内测]({{< relref "/docs/lingguang/sources/community/2026-10-13-tegongyuzhou-beta-hands-on" >}})）。

## 通知与界面

任务完成或有变动时，App 弹窗或通知栏提醒，点击回到对应对话（[智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}})、[光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}})）。首页中部是灵光正在管理的事务，下方是「要我管」入口（[智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}})）。资料中的通知都发生在灵光 App 内，没有短信、微信等外部渠道（见总览中的交互渠道）。

## 主动性的边界

新眸称主动在授权范围内进行，关键节点才提醒，「支付和重要决定先确认」，设计上试图避免把主动做成打扰（[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})）。36氪的例子中，天气变化后灵光梳理调整方案，「涉及退订、改签等决定，再由用户确认」（[36氪]({{< relref "/docs/lingguang/sources/media/2026-10-27-36kr-lingguang-2-china-muse" >}})）。AI沃茨的评价相反方向：到点了它「恨不得把所有的都推到我面前」，不用追着问进度（[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})）。资料没有提到用户如何调节提醒频率。

## 还没被验证的长期交付

所有实测都在发布后一两周内完成。白鲸技术栈写稿时养车周报尚未到第一个周日，作者说真正要验证的是「在几周甚至几个月后」能否按时主动交付、费用异常时能否归因（[白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}})）。亿邦认为任务成功率、需人工接管的比例还有待给出可验证的答案（[亿邦]({{< relref "/docs/lingguang/sources/media/2026-11-05-ebrun-lingguang-weekly-tasks" >}})）。

推断：灵光的「持续执行」主要是定时检查加条件提醒，执行动作（下单、改签、发消息）多数仍交回用户或受平台限制（见[连接器]({{< relref "/docs/lingguang/analysis/connectors" >}})）。它更接近一个会自己排日程的监控器，而不是能在后台完成交易的代理。

## 资料缺口

- 每个用户可同时运行的事务数量、单个事务的时长上限、检查频率的上下限。
- 任务的暂停、修改、停止入口；失败后是否重试、是否通知。
- 发布数周以上的长期使用记录，定时任务的准点率。
- 「一周 360 万次任务」中定时任务所占比例。

## 主要资料

- 官方：[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})、[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})，主动跟进的官方描述与示例。
- 媒体：[新眸]({{< relref "/docs/lingguang/sources/media/2026-10-27-xinmou-lingguang-china-solution" >}})，事务生命周期与主动边界；[智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}})、[光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}})、[白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}})，持续任务实测；[36氪]({{< relref "/docs/lingguang/sources/media/2026-10-27-36kr-lingguang-2-china-muse" >}})，用户确认的例子。
- 社区：[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})、[小朱]({{< relref "/docs/lingguang/sources/community/2026-11-04-aizxiaozhu-lingguang-domestic" >}})，自定频率与每日汇报；[特工宇宙：内测]({{< relref "/docs/lingguang/sources/community/2026-10-13-tegongyuzhou-beta-hands-on" >}})，内测期的长期任务。
