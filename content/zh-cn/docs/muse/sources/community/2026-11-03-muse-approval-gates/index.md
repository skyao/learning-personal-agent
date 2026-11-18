---
title: "审批关卡地图：智能体何时停下来"
linkTitle: "审批关卡地图"
date: 2026-11-03
originalTitle: "The Approval Gates Map: When Does the Agent Stop?"
sourceUrl: "https://aihomebuilding.com/stories/approval-gates-2026.html"
author: "Elena Vasquez"
publisher: "AIHomeBuilding"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-17
tags: [安全, 持续执行]
products: [muse]
---

{{< source-info >}}

## 收录说明

本页收录的文章于 2026-11-03 发布在 AIHomeBuilding。直接下载全文，未做任何删改。全文为英文，原文全文存于本目录的 original.md，网站上不显示，待翻译。

本页全文无图片、无表格。作者在文末声明：Meta 未公布触发审批的完整动作清单，第一档依据上线公告的举例，“like”一词表明清单是示例而非穷尽；Wardle 漏洞依据其概念验证与二手报道，Meta 除确认修复外的说法未独立核实；任务范围蔓延的警告是设计推论而非实测频率。

## 内容摘要

Meta 在 2026 年 9 月 8 日的上线公告中承诺，Muse 会在登录、完成预订、购买、发送邮件等敏感操作前征求批准，架构上每人一台专用云电脑 Muse Secure VM，由独立程序 Sentinel 审批一切联网操作，密码与支付方式存于智能体看不到的安全存储，用户另有 Activity 日志可查。作者把审批分为三档：每次都停的登录、预订、购买与发邮件；“Allow for this task”一次批准覆盖该任务后续全部步骤，但“任务”的边界由智能体自己的计划划定，Meta 未公布任务何时结束。第三档为从不停顿的阅读、搜索、摘要、起草、比价与定时后台工作，其中定时任务的审批会在用户不在时排队，导致任务静默停滞或因事先批准过宽而自行推进；另有一道不属于 Meta 的关卡：2026 年 9 月 21 日亚马逊封禁了 Muse 在亚马逊站内购物。2026 年 9 月，安全研究员 Patrick Wardle 发现 Muse 桌面客户端存在未公开的 macOS 偏好设置键，可被任意非特权进程改写以劫持语音流量并窃取 Muse 认证令牌，Meta 在约一天内从生产版本中移除该键，Wardle 于 2026 年 9 月 22 日确认修复，未分配 CVE 编号；另据上线报道，Muse 上线头 13 天下载量超过 250 万次，但组织用户没有 SIEM 审计导出、IT 管理控制台与 DLP 集成。

## 保留理由

已收资料已有 Sentinel 与审批的官方说明；本篇是同站独立分析，首次把审批画成三档地图并指出“Allow for this task”的任务边界未定义、定时任务审批排队两种失效模式，另补入 Wardle 漏洞与组织审计缺口。
