---
title: "WorkBuddy：实际效果与可靠性"
linkTitle: "实际效果与可靠性"
weight: 120
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  WorkBuddy 只有一篇独立实测：企业微信中的定时任务因模型排队失败，推送内容日期错了一年，作者称它「还需要人盯交付」。更新日志反映的高频问题是会话丢失、定时任务调度、渠道收发和长期运行后的内存膨胀。
---

## 概要

- 独立实测只有数智奔流一篇（2026-10-19，企业微信场景）：总结一小时直播用了 14 分钟；定时任务首次运行因模型队列已满失败；推送内容日期错一年，改提示词后才恢复；执行与推送状态不同步。
- 作者的结论是它像「一个已经学会接活、但还需要人盯交付的实习同事」，时效敏感的自动化任务仍需人工核查。
- 更新日志每一两周一版，反复修复的问题集中在：会话丢失或打不开、定时任务卡死或误判补跑、即时通讯消息收发、上下文压缩、长期运行后内存膨胀。
- 官方在多处承认局限：模型「可能存在理解偏差或非预期行为」，记忆可能有概括偏差。
- 没有完成率、出错率或可用性数据；其余第三方文章只做概念对比，没有实测 WorkBuddy。

## 唯一的独立实测：企业微信里的「实习同事」

数智奔流的作者此前没有用过 WorkBuddy，在企业微信中测试了部分功能（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）：

| 测试 | 结果 |
| --- | --- |
| 总结约一小时的官方直播 | 14 分钟完成；中途它建议暂停稍后再试，继续则重复消耗积分和运行配额 |
| 「看看我最近在忙啥」 | 翻了自己的会话记录、列出桌面和素材文件夹目录作答 |
| 每天 10:10 搜集 AI 动态并推送 | 首次「当前模型队列已满」，10:10 到 10:47 反复尝试全部失败；第二天成功 |
| 推送内容的日期 | 标成 2025 年 10 月，搜索关键词一开始就写错；复制同样提示词次日仍错，写入具体日期后恢复 |
| 执行与推送 | 出现过文件已生成但企业微信没收到、任务失败却没有清晰反馈 |

作者追问日期错误时，它第一次认为自己没错，被指出后才解释，称 15 日的简报其实生成正确，只是因系统问题没推送；作者据此认为时间错误至少有模型生成和任务执行两层原因（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。这一归因来自 AI 的自述，可信度有限。

作者的结论：WorkBuddy 更像「一个已经学会接活、但还需要人盯交付的实习同事」；「算力是第一道瓶颈，可靠性才是最后一道门槛」；建议系统在检索前确认当前日期、发送前检查内容日期（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。

## 更新日志反映的高频问题

更新日志从 3 月到 11 月记录了几十个版本（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。4.5.2（03-06）在首批上线后「集中修复用户反馈的关键问题」，4.5.8（03-11）是「稳定性专项」。反复出现的问题类别（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）：

- **会话**：历史会话打不开或丢失（4.5.2、5.0.4、5.7.0、5.8.2、5.9.3）；消息已处理后仍继续运行、重复续写（5.5.3）。
- **定时任务**：长期显示运行中、被误判为补跑（5.5.2），卡死不触发、休眠期间调度不准（5.6.0）。
- **即时通讯**：微信客服号扫码后无法发消息（5.8.1）、企微机器人生成文件后回复卡住（5.8.2）、云助理发消息后无回复（5.7.6）。
- **长期运行**：本地沙箱内存膨胀导致卡死（5.8.3），本地助理内存快速增长导致白屏或崩溃（5.3.12）。
- **误拦截**：沙箱自动审批误拦截用户明确要求的操作（5.8.1），工作区授信误判导致无法执行命令（5.9.1）。
- **产出质量**：PPT 和表格在部分设备上无法生成、公式重算不准（5.4.4），PPT 内容与配图不符（5.9.1 优化）。

这些是厂商自述的修复，没有说明影响面。数智奔流转述的 9 月与 10 月 16 日更新（修复企业微信机器人文件未回传、定时任务通知延迟或漏发）与实测中遇到的问题吻合（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。

## 官方承认的局限

- 定时任务页：「大模型在执行过程中可能存在理解偏差或非预期行为」，对文件改动、数据变更、对外发送的结果建议保留可追溯日志（[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})）。
- 记忆页：记忆「可能存在概括偏差或时效性问题」（[帮助：记忆]({{< relref "/docs/workbuddy/sources/official/2026-07-08-help-memory" >}})）。
- 权限页：默认权限「不能替代备份」（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。

## 其他第三方资料

《中国新闻周刊》只给了 90 亿次任务请求和包子铺案例两处正面信息，没有 WorkBuddy 的失败案例（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})）。程序员鱼皮、黑咖啡全景解读、易论AI 对谈都只做概念对比，没有实测（[程序员鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})、[黑咖啡全景解读]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})、[易论AI 对谈]({{< relref "/docs/industry/sources/community/2026-11-03-yilun-ai-personal-agent-overhyped" >}})）。易论AI 对谈的嘉宾泛指 Agent 称，连续一周、环境会变的长任务综合成功率「还在 40% 以下」（[易论AI 对谈]({{< relref "/docs/industry/sources/community/2026-11-03-yilun-ai-personal-agent-overhyped" >}})），未注出处。

## 资料缺口

- 更多独立实测，尤其是桌面客户端的文件处理、PPT/表格生成、本地定时任务，以及微信助理。
- 任务完成率、出错率、可用性或状态页。
- 数周以上的长期使用反馈；用户社区（论坛、应用商店评论）的整体倾向。
- 腾讯对实测问题（排队、日期错误）的回应。

## 主要资料

- 官方：[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})（高频问题）、[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})、[帮助：记忆]({{< relref "/docs/workbuddy/sources/official/2026-07-08-help-memory" >}})、[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})（官方承认的局限）
- 媒体：[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})
- 社区：[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})（唯一的独立实测）、[程序员鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})、[黑咖啡全景解读]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})、[易论AI 对谈]({{< relref "/docs/industry/sources/community/2026-11-03-yilun-ai-personal-agent-overhyped" >}})
