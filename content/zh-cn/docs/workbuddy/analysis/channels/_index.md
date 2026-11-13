---
title: "WorkBuddy：交互渠道"
linkTitle: "交互渠道"
weight: 50
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  WorkBuddy 以桌面客户端为主入口，手机端有 App 和六种即时通讯「助理」作为遥控器；WorkBuddy 有自己的 agent.qq.com 邮箱，不借用用户邮箱代发。
---

## 概要

- 主入口是桌面客户端。手机上有两条路：WorkBuddy 移动端 App（官方推荐），以及在微信、微信客服号、企业微信、QQ、飞书、钉钉里绑定的「助理」。
- 助理的定位是「遥控器」：手机发指令、回答追问、批准操作，执行在电脑上完成，结果回到手机；所有远程指令进同一个会话。
- 接入门槛差别很大：微信扫码即可绑定；企业微信、QQ、飞书、钉钉要先在平台侧创建机器人或应用，飞书要导入大量权限，钉钉要管理员权限。
- WorkBuddy 有自己的邮箱身份（如 `xxx.agent@agent.qq.com`，由 Agent Mail 提供），回复、转发须用户确认。
- 10 月 14 日起以企业微信机器人的形式进入企业微信聊天列表，可在群聊中 @它派任务。

## 手机上的两条路：App 与助理

接入指南称助理支持通过微信、企业微信、QQ、飞书、钉钉远程控制电脑上的 WorkBuddy，同时「推荐使用移动端 App」：App 可用文字、语音、图片、文件下达任务，有「云端工作」和「连接电脑」两种模式，同账号登录即可，不必创建机器人（[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})）。

助理的帮助页把它比作「遥控器」：手机发一条消息，电脑上的 WorkBuddy 自动执行，完成后回复到手机，场景是出门在外、会议中、通勤路上（[帮助：助理]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant" >}})）。助理固定一个会话、一个专属文件夹（见[运行环境]({{< relref "/docs/workbuddy/analysis/runtime" >}})）。微信发起的任务可以回到电脑上查看完整的思考过程、操作步骤、文件和结果；微信消息到达时桌面端自动切到「助理」标签（[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})）。

## 六种即时通讯接入的门槛

| 平台 | 绑定方式 | 要求与限制 |
| --- | --- | --- |
| 微信助理（推荐） | 扫码，不需要 App ID/Secret | WorkBuddy ≥ 4.6.4、微信 ≥ 8.0.70；一台电脑同时只能绑定一个微信账号 |
| 微信客服号 | 扫码 | 与微信助理功能相同，二选一 |
| 企业微信 | 创建智能机器人；推荐 WebSocket 长连接（Bot ID + Secret，可扫码快捷绑定），备选 URL 回调 | 支持私有化部署企业微信的自定义地址；群聊 @机器人 下发任务 |
| QQ | 在 QQ 开放平台创建机器人取得 AppID/AppSecret | 须实名认证的 QQ 账号；AppSecret 二次查看强制重置；私聊与群聊 @ |
| 飞书 | 企业自建应用，批量导入消息、日历、多维表格、云文档等权限，配事件订阅与卡片回调后发布 | WebSocket 适合没有公网 IP 的用户 |
| 钉钉 | 创建应用并开通三项权限 | 须企业管理员权限；群的归属组织须与机器人相同 |

来源：[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})、[帮助：助理]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant" >}})。微信助理能做的事包括启动或继续任务、回答追问、批准命令执行和文件修改、查看输出和差异、收到完成通知，支持文字、图片、文件和语音（需开启微信语音转文字）（[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})）。接入指南中飞书、钉钉两节把用途写成「远程控制 WorkBuddy 完成各种编程任务」，其余各节写办公场景（[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})）。

渠道的时间线（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）：4.6.0（03-19）企业微信、钉钉、飞书、QQ 多渠道机器人；4.6.4（03-22）微信 ClawBot；4.9.1 IM 文本审批，可以用文字回复批准高危命令；5.3.11（08-07）企微助理逐字流式输出。日志也记录了多次渠道故障修复，如 4.22.4 修复「群消息未检查 @mention 就自动回复」、5.5.3 修复企微群聊 @机器人后一直「思考中」、5.8.1 修复扫码连接微信客服号后无法发消息（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

## 企业微信：机器人进聊天列表

10 月 14 日 WorkBuddy 宣布与企业微信深度融合，以企业微信机器人的形式出现在聊天列表里；企业微信桌面端升级到 5.0.12 后，可在侧边栏「智能机器人」入口领取试用（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。据作者转述 10 月 15 日的官方直播，推荐用法是「手机上派活、到工位打开电脑活已干完的多端接力」（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。作者实测中，日常对话与定时任务都在这个机器人窗口进行，回复只发回消息的来路（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。

## 自己的邮箱

「我的邮箱」为每个用户创建专属地址（如 `xxx.agent@agent.qq.com`），由 Agent Mail 提供底层服务，让 WorkBuddy 有独立的收发邮件身份，「不借用您的个人邮箱代发」（[帮助：我的邮箱]({{< relref "/docs/workbuddy/sources/official/2026-07-27-help-mailbox" >}})）。官方称做它是为了解决入口（发封邮件就能触发）、身份和工作流三个问题，「收件在界面看，干活在对话里」（[帮助：我的邮箱]({{< relref "/docs/workbuddy/sources/official/2026-07-27-help-mailbox" >}})）。

- **开通**：手动开通，须同意补充协议并用手机号验证；开通和在界面查看不收费，在对话里处理邮件按正常任务消耗积分；端内查看邮件不消耗 Token。
- **对外动作**：回复、转发不自动发送，须用户确认；没有补充内容时会先询问「你想怎么回、发给谁」。
- **状态**：运行中、已停用、已封禁/冻结（显示错误码与原因）。

来源：[帮助：我的邮箱]({{< relref "/docs/workbuddy/sources/official/2026-07-27-help-mailbox" >}})。

## 以谁的名义对外

资料中有三种身份：即时通讯里是 WorkBuddy 的机器人；邮箱是 WorkBuddy 自己的 agent 地址；连接器（如 QQ 邮箱的发送邮件权限）则以用户本人身份和授权范围执行（[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})）。资料没有说明对外发信时是否标明 AI 身份。

## 资料缺口

- 移动端 App 的平台（iOS、Android）、上线时间与功能范围。
- 邮箱的发信频率限制、反垃圾规则和封禁条件。
- 「频道 IM」（5.11.0 新增消息卡片）是什么、面向谁。
- 海外版是否支持 WhatsApp、Slack、Telegram 等渠道。

## 主要资料

- 官方：[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})（六种接入方式的步骤）、[帮助：助理]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant" >}})（助理定位）、[帮助：我的邮箱]({{< relref "/docs/workbuddy/sources/official/2026-07-27-help-mailbox" >}})（专属邮箱）、[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})（连接器以用户身份执行）、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})（渠道时间线与故障修复）
- 社区：[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})（企业微信机器人实测）
