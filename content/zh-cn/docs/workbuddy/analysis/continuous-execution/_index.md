---
title: "WorkBuddy：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  WorkBuddy 的后台工作以定时任务为主，另有邮件到达、项目 Webhook 和即时通讯消息三种触发。机制较完整，但无人值守与审批相冲突，唯一的独立实测遇到排队失败和日期错误。
---

## 概要

- 定时任务（2026-03-19 上线，09-08 由「自动化」改名）是主要的后台机制，分本地、项目、云端三种来源；本地任务要求电脑开机并运行客户端，云端任务不要求。
- 生命周期管理在 9–11 月逐步补齐：汇总页、运行时间线、失败分层提醒、失败后在原会话重试；5.11.0（11-03，灰度中）支持立即运行、编辑、暂停、删除。
- 无人值守与审批有冲突：默认权限下，敏感操作会让任务停在等待确认状态，定时任务页因此把「完全访问权限」标为推荐，而权限页建议只在隔离环境中短时使用完全访问。
- 失败处理有专门设计：模型排队满时自动重新排队；模型下线时运行前切换模型，但提示词已发出后失败就不再换模型重跑，以免重复产生副作用；检测到循环时暂停并请用户确认。
- 数量限制按套餐：自动任务数体验版 3 个、标准 15 个、高级 30 个、旗舰 99 个（前三档限免期内均为 99 个）。
- 数智奔流的实测中，定时任务首次运行因「当前模型队列已满」从 10:10 反复尝试到 10:47 全部失败；之后推送的内容日期错了一年。

## 定时任务：三种来源

定时任务保存名称、提示词、执行时间、工作空间、权限等配置，到时间「以用户当前登录身份」自动发起（[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})）。三种来源（[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})）：

| 来源 | 在哪里执行 | 限制 |
| --- | --- | --- |
| 本地 | 本机客户端 | 执行期间不能关机或退出客户端 |
| 项目 | 在项目中创建 | 个人级别，只有创建者可见、可管理，在创建者本人的会话中运行（[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})） |
| 云端 | 云端沙箱 | 电脑关机也能运行；访问不到本机文件，不能推送企业微信 |

重复规则有间隔、单次、每天、每周、每双周、每月、每年；创建方式有手动新建、从对话新建（普通对话里描述周期性需求也会自动创建）、从模板新建（如每日 AI 新闻推送、每周工作周报、会议前准备）（[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})）。

演变（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）：4.6.0（03-19）支持自动化定时任务；4.7.0 支持单次执行；4.7.2 支持临时工作空间；5.4.0（08-20）支持每月多个日期；5.5.4（09-08）统一改名「定时任务」；5.5.6（09-10）失败后可在当前会话继续重试；5.7.5（10-03）新增汇总页，同一任务的历次运行按时间线展示；5.8.0（10-09）新增任务失败分层提醒；5.11.0（11-03，灰度中）支持立即运行、编辑、重命名、删除与启动/暂停。阿言er 提醒，5.11.0 仍标「灰度中」，最新界面不能默认覆盖全部账号（[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})）。

## 其他触发方式

- **邮件到达**：WorkBuddy 的专属邮箱收到邮件即可触发处理，结果回到对话和邮箱；官方称邮件是「办公自动化最稳定的触发器之一」（[帮助：我的邮箱]({{< relref "/docs/workbuddy/sources/official/2026-07-27-help-mailbox" >}})）。邮箱见[交互渠道]({{< relref "/docs/workbuddy/analysis/channels" >}})。
- **项目外部数据源**：5.0.0（06-03）起项目可接入外部数据源，支持定时导入与 Webhook 事件触发（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。
- **即时通讯消息**：在微信、企业微信、QQ、钉钉、飞书发一条消息，电脑上的 WorkBuddy 执行后回复到手机（[帮助：助理]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant" >}})）。

除完成、待确认、失败的通知外，资料中没有 WorkBuddy 主动发起联系、长期跟进某个目标的机制。《中国新闻周刊》称「主动找人」已是个人智能体标配（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})），但没有举 WorkBuddy 的例子。

## 无人值守与审批的冲突

定时任务页写明，「完全访问权限」（页面标「推荐」）下工具调用无需逐次确认；默认权限下敏感操作需确认，用户不在电脑前时「任务会停在等待确认状态」（[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})）。同时，权限页称完全访问「并非更安全，只是把确认环节交给 AI 自动通过」，建议只在 Docker、虚拟机、临时目录等隔离环境中短时使用（[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})）。两页的建议方向相反。定时任务页另提醒，涉及写入、删除、资金操作的提示词要审慎，文件改动、数据变更、对外发送应保留可追溯日志，新建后先试跑一次（[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})）。

远程助理同理：文件删除、系统配置修改、批准命令执行等操作要确认后才执行，确认可以直接在聊天里回复（[帮助：助理]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant" >}})）。

## 失败、重试与通知

- **模型排队**：当前模型队列已满时不立即失败，自动重新排队重试，多次重试仍失败才标记失败。官方列出的失败原因还有连接器未授权、登录失效、电脑离线错过执行时间（[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})）。
- **模型下线**：每次运行前先切换到同系列新模型（没有则用「快速」档默认模型），并回写任务配置；若提示词已发出后失败，则按失败处理、不再换模型，「避免对同一个提示词重复执行产生副作用」（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）。
- **循环检测**：检测到任务可能在循环时，在工具调用前暂停并弹出确认；继续照常计费，终止则已产生但未出最终回答的消耗进入退费评估（[帮助：积分]({{< relref "/docs/workbuddy/sources/official/2026-10-09-help-credits" >}})）。
- **通知**：电脑端系统通知；WorkBuddy App 关联当前电脑时，完成、待确认、失败推送到手机，标题以「定时任务：」开头；也可推送到助理已绑定的企业微信机器人，仅支持 WebSocket 长连接，推送失败不影响任务本身（[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})）。

日志中与调度相关的修复不少：5.5.2 修复长期显示运行中、正常执行被误判为补跑；5.6.0 修复任务卡死不触发、休眠期间调度不准；5.3.14 优化高峰期调度、减少集中触发（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

## 数量限制

自动任务数按套餐：体验版 3 个、标准版 15 个、高级版 30 个（三档限免期内均为 99 个），旗舰版 99 个（[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})）。定时任务页称执行还受「任务频率、最大执行时长与系统并发控制」限制，未给数值（[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})）。

## 实测：排队、日期错误与推送状态

数智奔流在企业微信中设了每天 10:10 搜集 AI 动态并推送的定时任务（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）：

- 首次运行提示「当前模型队列已满」，换成界面标「轻微拥堵」「空闲」的模型也不行，从 10 点 10 分到 10 点 47 分反复尝试，全部失败；第二天才成功。
- 推送内容的日期写成 2025 年 10 月，执行记录显示搜索关键词一开始就是「2025年10月」；次日复制同样的提示词仍然出错，把具体日期写进提示词后才恢复。
- 任务执行与消息推送是两个状态：出现过文件已生成但企业微信没收到、任务失败却没有及时清晰反馈的情况。

作者的结论是「算力是第一道瓶颈，可靠性才是最后一道门槛」（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。更多见[实际效果与可靠性]({{< relref "/docs/workbuddy/analysis/reliability" >}})。

## 资料缺口

- 定时任务的频率下限、最大执行时长、并发上限的具体数值。
- 「限免」的截止日期，以及之后各档的实际任务数。
- 云端定时任务能用哪些工具和连接器。
- 长期（数周以上）运行的稳定性实测。

## 主要资料

- 官方：[帮助：定时任务]({{< relref "/docs/workbuddy/sources/official/2026-10-28-help-automation" >}})（定时任务全貌）、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})（演变与调度修复）、[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})（模型下线时的切换规则）、[帮助：积分]({{< relref "/docs/workbuddy/sources/official/2026-10-09-help-credits" >}})（循环检测）、[帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})（完全访问的风险说明）、[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})（自动任务数）、[帮助：我的邮箱]({{< relref "/docs/workbuddy/sources/official/2026-07-27-help-mailbox" >}})（邮件触发）、[帮助：助理]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant" >}})（远程消息触发）、[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})（项目定时任务）
- 媒体：[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})
- 社区：[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})（企业微信定时任务实测）、[阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})（灰度提醒）
