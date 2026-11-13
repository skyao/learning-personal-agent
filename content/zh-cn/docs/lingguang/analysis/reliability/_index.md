---
title: "蚂蚁灵光：实际效果与可靠性"
linkTitle: "实际效果与可靠性"
weight: 120
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  实测评价比较一致：账单分析、盯价提醒、群消息汇总、内容生成做得好；付款、下单、对外发消息、淘宝和部分设备控制做不到。评测者认为灵光「有管事的意图，却还没有办事的工具」，瓶颈在平台权限而不在模型。所有实测都在发布后两周内，没有完成率、出错率或长期使用数据。
---

## 概要

- 做得好的部分集中在「看」和「盯」：支付宝账单梳理与找自动续费、定时盯价并通知、钉钉群与邮件汇总、按日汇报开销；内容生成（闪应用、表格、PPT、网页）被 Z Finance 评为测试中表现最好的部分。
- 做不到的集中在「办」：付款、转账、外卖网购、淘宝购物车、在钉钉飞书发消息、扫拖机器人控制等（详见[连接器]({{< relref "/docs/lingguang/analysis/connectors" >}})）。
- 规划类任务需要用户多轮补充信息，灵光更像「一起把计划做细的协作者」。
- 评测者的总体判断：方向对、底座刚搭好；瓶颈已经不是模型推理，而是跨平台权限、安全责任和商业利益。
- 官方和第三方都没有发布任务完成率或出错率；所有实测都在 2026-10-13 到 11-04 之间，没有数周以上的长期记录。

## 做得好的部分

- 账单：AI故事计划称支付宝账单是测试里「真正比较顺畅」的（[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})）；光子星球实测中灵光先筛选订阅相关消费，计算时「对帐单进行了反复的验证」后给出订阅清单（[光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}})）。
- 盯价与提醒：光子星球、AI沃茨的盯价任务都在云端持续运行并按条件通知；小朱的每晚开销汇报到点确实提醒（[光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}})、[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})、[小朱]({{< relref "/docs/lingguang/sources/community/2026-11-04-aizxiaozhu-lingguang-domestic" >}})）。
- 钉钉：连通之后可定时获取指定群的信息，查询文档、日程、审批和考勤（[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})）。
- 内容生成：Z Finance 测了调研表格、PPT 和 HTML 展示页，称这是「整体表现最好的部分」（[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})）。
- 比价的中立性：同一问题灵光比对京东和淘宝（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})）。

## 做不到的部分

AI故事计划列出：暂不支持阿里邮箱，不能从亲情号转账，不能查医保余额，淘宝没有直接接入，扫拖机器人不能下指令，并总结为「灵光已经有管事的意图，却还没有完全获得办事的工具」（[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})）。极客公园记录了钉钉飞书发消息失败、米家接口限流、淘宝购物车被风控拦截、付款只能跳转（[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})）。白鲸技术栈记录了 ETC 和充电 App 不能拉订单，记账服务首次发布遇到后台问题，支出先存进项目档案、功能补齐后再迁入账本（[白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}})）。小朱想让灵光顺手领积分，结果「有点鸡肋」，作者归因于各平台的操作权限（[小朱]({{< relref "/docs/lingguang/sources/community/2026-11-04-aizxiaozhu-lingguang-domestic" >}})）。

## 规划要用户补信息

Z Finance 让灵光做慕田峪长城攻略，得到完整时间表并能一键加入本机日历，但需要用户补充不少信息，作者称它「更像一个和你一起把计划做细的协作者」（[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})）。智东西的找房、比价任务同样经过多轮对话才敲定计划（[智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}})）。

## 评测者的整体判断

| 评测者 | 判断 | 资料 |
| --- | --- | --- |
| 小象AI | 完成度不高，「更像是一个底座框架刚刚搭好」 | [小象AI]({{< relref "/docs/lingguang/sources/community/2026-10-28-xiaoxiang-lingguang-2-hands-on" >}}) |
| AI沃茨 | 测过 12 个同类产品，认为手机上的智能体与电脑上是「两个物种」，看重配置方便、接上一直有效；对灵光总体正面 | [AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}}) |
| AI故事计划 | 能把信息搬进同一对话框，还没把 App 变成工具 | [AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}}) |
| 极客公园 | 真正的瓶颈「已经不再是模型的推理能力」，而是权限、责任与利益 | [极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}}) |
| Z Finance | 交易能力停留在辅助决策与跳转引导 | [Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}}) |
| 白鲸技术栈 | 要在几周、几个月后才能验证长期任务 | [白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}}) |

## 官方说法与实测的差距

官方强调授权后主动发现需求、跨平台工作流和智能家居控制（[官方发布]({{< relref "/docs/lingguang/sources/official/2026-10-27-ant-group-lingguang-2-0" >}})）。实测中「发现」和「提醒」基本兑现，「跨平台执行」大多停在读取：对外发送、付款、跨阿里生态的操作都未完成。亿邦指出成功率、人工接管比例、留存「还有待给出可以被验证的答案」（[亿邦]({{< relref "/docs/lingguang/sources/media/2026-11-05-ebrun-lingguang-weekly-tasks" >}})）。

资料中的实测几乎都是单个评测者一次性的体验，测试时间多在内测期或发布后一周内，版本迭代很快（App Store 显示 11 月 2 日到 5 日连发三个版本，[App Store 页]({{< relref "/docs/lingguang/sources/official/2026-11-05-app-store-listing" >}})），部分结论可能已经过时。资料库中没有用户自己的实测（`exploration/` 为空）。

## 资料缺口

- 官方或第三方的任务完成率、出错率、人工接管比例。
- 发布一个月以上的长期使用记录；双十一盯价、养车周报等长期任务的最终结果。
- 11 月 4 日升级后新连接器的实测。
- 用户自己的实测。
- 应用商店评分与用户评论的整体倾向（App Store 页未收评分）。

## 主要资料

- 媒体：[AI故事计划：实测]({{< relref "/docs/lingguang/sources/media/2026-10-29-aigushijihua-lingguang-2-test" >}})、[极客公园]({{< relref "/docs/lingguang/sources/media/2026-10-31-geekpark-lingguang-2-hands-on" >}})，能力清单与失败案例；[白鲸技术栈]({{< relref "/docs/lingguang/sources/media/2026-10-30-baijing-lingguang-super-app" >}})、[光子星球]({{< relref "/docs/lingguang/sources/media/2026-10-27-guangzixingqiu-three-life-cases" >}})、[智东西]({{< relref "/docs/lingguang/sources/media/2026-10-28-zhidx-lingguang-2-hands-on" >}})，场景实测；[亿邦]({{< relref "/docs/lingguang/sources/media/2026-11-05-ebrun-lingguang-weekly-tasks" >}})，可验证性的质疑。
- 社区：[Z Finance]({{< relref "/docs/lingguang/sources/community/2026-11-01-zfinance-lingguang-2-vs-muse" >}})、[AI沃茨：15 个 App]({{< relref "/docs/lingguang/sources/community/2026-10-27-kaerdeaiwozi-lingguang-15-apps" >}})、[小朱]({{< relref "/docs/lingguang/sources/community/2026-11-04-aizxiaozhu-lingguang-domestic" >}})、[小象AI]({{< relref "/docs/lingguang/sources/community/2026-10-28-xiaoxiang-lingguang-2-hands-on" >}})，个人实测与评价。
