---
title: "WorkBuddy 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  WorkBuddy 是腾讯 2026-03-04 正式发布的桌面 AI 工作台，在用户电脑上执行任务，可经微信、企业微信等即时通讯软件远程遥控；分析覆盖截至 2026-11-10 收集的 18 篇 WorkBuddy 资料和 5 篇涉及它的行业资料。
---

## 概要

- WorkBuddy 是 macOS、Windows 桌面客户端，任务在用户自己的电脑上执行；手机 App 和六种即时通讯「助理」只负责下指令和审批，电脑离线远程即中断。云端沙箱只用于部分定时任务和移动端。（[运行环境]({{< relref "/docs/workbuddy/analysis/runtime" >}})、[交互渠道]({{< relref "/docs/workbuddy/analysis/channels" >}})）
- 第三方普遍据此把它归为「桌面端 Agent」或「Work Agent」，与有自己云端电脑的 Personal Agent 区分；《中国新闻周刊》则把它与 Muse、Dots、Claude Duet 并列为个人智能体。（[运行环境]({{< relref "/docs/workbuddy/analysis/runtime" >}})）
- 后台工作以定时任务为主，另有邮件、项目 Webhook、即时通讯消息三种触发；生命周期和失败重试设计较完整，但无人值守与默认审批相冲突。（[持续执行]({{< relref "/docs/workbuddy/analysis/continuous-execution" >}})）
- 安全靠本机沙箱、分级审批、删除保护与自动备份；针对模型的审查与提示注入防护默认关闭。日志披露过沙箱逃逸和审批绕过的修复，没有外部安全事件。（[安全]({{< relref "/docs/workbuddy/analysis/security" >}})）
- 连接器以腾讯自家办公服务为主，外加自定义 MCP 和兼容 OpenClaw 生态的技能市场；10 月 14 日与企业微信深度融合。（[连接器]({{< relref "/docs/workbuddy/analysis/connectors" >}})）
- 多模型并列（混元、GLM、MiniMax、Kimi、DeepSeek），用户按三档自选；算力紧张时排队，唯一的独立实测中定时任务因此失败。（[模型]({{< relref "/docs/workbuddy/analysis/models" >}})、[实际效果与可靠性]({{< relref "/docs/workbuddy/analysis/reliability" >}})）
- 国内个人版按积分计费，体验版免费、付费 99/199/999 元每月三档，积分与 CodeBuddy 共享；10 月底起以 Buddy One VIP 与腾讯文档、会议、ima、网盘打包。规模数据只有口径不明的「累计 90 亿次任务请求」。（[开放与价格]({{< relref "/docs/workbuddy/analysis/access-pricing" >}})、[商业与规模]({{< relref "/docs/workbuddy/analysis/business" >}})）

## 定位

官方称 WorkBuddy 是「腾讯出品的全场景 AI 工作台」，口号是「你的办公好搭子」，与传统 AI 对话的区别在于能实际执行任务、自动操作本地文件、处理多步骤任务、交付可验收的成果（[帮助：简介]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-overview" >}})）。它与腾讯的编程助手 CodeBuddy 同属 Buddy AI 系列，共用账号积分（[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})），项目配置也与 CodeBuddy Code 一致（[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})）。更新日志中的「Claw」术语、兼容 OpenClaw 生态的 Skill、QQ 机器人入口路径中的 `openclaw` 字样，显示它与 OpenClaw 路线的关联（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})、[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})）。

产品重心在 2026 年内从个人桌面助手向团队协作扩展：6 月加入 Teams 与项目，7 月加入企业智能体，10 月接入企业微信，11 月的 5.11.0 下线办公、开发、设计三个入口、统一首页（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

第三方对它的归类不一致：

| 资料 | 归类 | 理由 |
| --- | --- | --- |
| [黑咖啡全景解读]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}}) | Work Agent | 「对事情负责」，与 Codex 并列；Personal Agent 对「这个人」负责 |
| [程序员鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}}) | 桌面端 Agent | 「用你的电脑干活的实习生」，干完一单就结束 |
| [易论AI 对谈]({{< relref "/docs/industry/sources/community/2026-11-03-yilun-ai-personal-agent-overhyped" >}}) | 不是 AI 助理 | 不会主动做事、没有自己的电脑 |
| [阿言er 长文]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}}) | 中国办公生态入口 | 与千问办公并列，区别于海外从团队、生活、对话上下文切入的产品 |
| [中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}}) | 个人智能体 | 与 Muse、Dots、Claude Duet、Copilot 并列 |

推断：按本笔记跟踪的 Personal Agent 定义，WorkBuddy 的核心差异在运行环境：它不给用户分配一台云端电脑，而是让用户自己的电脑充当执行环境，用即时通讯软件弥补「人不在电脑前」的问题。它在记忆、定时任务、邮箱身份上的设计已接近 Personal Agent，但「电脑必须在线」这一前提没有改变。

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-03-04 | 4.5.0 正式发布：macOS、Windows 双平台，多模型切换、工作空间、Skill、文件读写与终端命令 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-03-19 | 4.6.0：专家中心、MCP 集成面板、插件市场、企业微信/钉钉/飞书/QQ 机器人、自动化定时任务 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-03-22 | 4.6.4：微信 ClawBot，可在微信直接对话 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-03-25 至 03-30 | 4.7.x：自定义模型、MEMORY.md、QQ 邮箱连接器、MCP OAuth、Skill 安装前安全扫描 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-04-28 | 4.21.0：腾讯文档资料库、生成内容自动加水印、连接器 DNS Rebinding 防护 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-06-03 | 5.0.0：Teams 团队协作、项目计划看板、锁屏远程、助理面板 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-06-13、06-14 | 5.1.0、5.1.1：Token Plan、企业自建 Skill/插件市场、微信支付内置插件；修复沙箱逃逸攻击链 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-07-01 | 国内个人版改为体验、标准、高级、旗舰四档 | [帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}}) |
| 2026-07-21 | 5.3.3：企业智能体、本地长期记忆展示与编辑、安全中心文件自动备份 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-08-20 | 5.4.0：Worktree 任务、3D 模型生成、每月多日期定时 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-09-08 | 5.5.4：「自动化」改名「定时任务」；锁屏运行三种模式 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-10-03、10-04 | 5.7.5、5.7.6：定时任务汇总页；海外版 Outlook、Gmail 连接器 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-10-14 | 宣布与企业微信深度融合，以企业微信机器人形式出现；10-15 联合直播 | [数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}}) |
| 2026-10-22 | 5.9.1：Buddy One 会员购买、云端记忆、跨电脑导入任务 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-11-03 | 5.11.0（灰度中）：首页改版、下线办公/开发/设计入口、定时任务全面升级 | [更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}}) |
| 2026-11-09、11-10 | 帮助页更新：HTTP 类 MCP 受域名规则管控；模型下线后自动切换 | [帮助：权限与沙箱]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-permission-modes" >}})、[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}}) |

## 整体架构

用户在桌面客户端里新建任务，选一个工作空间目录；WorkBuddy 在本机沙箱中读写文件、执行命令、调用连接器和技能（[运行环境]({{< relref "/docs/workbuddy/analysis/runtime" >}})）。人不在电脑前时，可以用移动端 App 或在微信、企业微信、QQ、飞书、钉钉中绑定的助理发指令，执行仍在电脑上，结果和审批请求回到手机；WorkBuddy 还有自己的邮箱，邮件到达即可触发任务（[交互渠道]({{< relref "/docs/workbuddy/analysis/channels" >}})）。

上下文来自每晚整理的个人记忆、工作空间与项目的记忆文件和资料库，以及连接器接入的腾讯文档、QQ 邮箱等服务（[记忆与上下文]({{< relref "/docs/workbuddy/analysis/memory" >}})、[连接器]({{< relref "/docs/workbuddy/analysis/connectors" >}})）。定时任务按时间自动发起，本地任务需要电脑在线，云端任务在云端沙箱运行但碰不到本机文件（[持续执行]({{< relref "/docs/workbuddy/analysis/continuous-execution" >}})）。

高风险操作在默认权限下逐项确认，可以在聊天中回复批准；完全访问权限一键放开全部确认（[安全]({{< relref "/docs/workbuddy/analysis/security" >}})）。模型按快速、均衡、极致三档选择，按积分计费，积分与 CodeBuddy、Buddy One 下的腾讯办公产品共享（[模型]({{< relref "/docs/workbuddy/analysis/models" >}})、[开放与价格]({{< relref "/docs/workbuddy/analysis/access-pricing" >}})）。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境]({{< relref "/docs/workbuddy/analysis/runtime" >}}) | 本机执行为主，手机和即时通讯只遥控；电脑离线即中断；云端沙箱只用于部分定时任务和移动端，规格未公开 |
| [记忆与上下文]({{< relref "/docs/workbuddy/analysis/memory" >}}) | 每晚从会话提取个人记忆，可查看、编辑、关闭、导入；加上工作空间与项目的记忆文件和资料库；本地与云端记忆的关系不明 |
| [持续执行]({{< relref "/docs/workbuddy/analysis/continuous-execution" >}}) | 定时任务分本地、项目、云端三种，另有邮件、Webhook、即时通讯触发；失败重试与模型切换设计细致；无人值守与审批冲突 |
| [连接器]({{< relref "/docs/workbuddy/analysis/connectors" >}}) | 腾讯办公服务为主，海外版加 Gmail、Outlook；自定义 MCP；技能、插件、专家市场兼容 OpenClaw 生态；企业微信深度融合 |
| [交互渠道]({{< relref "/docs/workbuddy/analysis/channels" >}}) | 桌面客户端为主入口；移动 App 与六种即时通讯助理；有自己的 agent.qq.com 邮箱 |
| 设备 | 资料不足，未单独成页。执行端是 macOS 与 Windows（含 Windows ARM）桌面，computer-use 工具仅 macOS；手机端 App 与即时通讯负责遥控和接收通知；没有专用硬件（[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})） |
| [模型]({{< relref "/docs/workbuddy/analysis/models" >}}) | 混元、GLM、MiniMax、Kimi、DeepSeek 多模型并列，三档自选；可接自定义 API 与本地 Ollama；繁忙时排队 |
| [安全]({{< relref "/docs/workbuddy/analysis/security" >}}) | 本机沙箱、分级审批、删除保护、自动备份、凭证检测；AI 审查与注入防护默认关闭；日志披露沙箱逃逸等修复 |
| [隐私]({{< relref "/docs/workbuddy/analysis/privacy" >}}) | 记忆仅本人可见、不共享；自定义与本地模型可绕开 WorkBuddy；训练用途、保存期限、导出均无说明 |
| [开放与价格]({{< relref "/docs/workbuddy/analysis/access-pricing" >}}) | 3 月正式发布，无邀请制；积分订阅 0/99/199/999 元四档，与 CodeBuddy 共享；Buddy One VIP 打包腾讯办公产品 |
| [商业与规模]({{< relref "/docs/workbuddy/analysis/business" >}}) | 只有「90 亿次任务请求」一个口径不明的数字；订阅与会员捆绑；战略重心是腾讯办公生态和企业微信 |
| [实际效果与可靠性]({{< relref "/docs/workbuddy/analysis/reliability" >}}) | 只有一篇独立实测：排队失败、日期错一年、推送不同步，「还需要人盯交付」；日志显示会话、调度、渠道问题反复出现 |

## 资料缺口

- **规模与商业**：用户数、付费数、收入；「90 亿次任务请求」的一手出处与口径；Buddy One VIP 与企业版的价格。
- **运行环境**：云电脑、云助理、云端沙箱的规格与额度；本地任务的并发与时长上限。
- **隐私**：隐私政策原文；是否用于训练；保存期限、导出、注销；群聊等场景中他人信息的处理。
- **安全**：外部审计、漏洞赏金；5.1.0 沙箱逃逸问题的发现经过。
- **实测**：桌面客户端、微信助理、PPT/表格生成的独立实测；长期使用反馈；腾讯对实测问题的回应。
- **海外版**：开放地区、价格、连接器清单（腾讯官网文章提到的 Canva、GitHub、Morningstar、Notion）。
- **相关产品**：腾讯 Handy Bot 与 WorkBuddy 的关系；移动端 App 的平台与上线时间。
