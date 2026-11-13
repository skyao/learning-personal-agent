---
title: "Today AI 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Today 是齐俊元创立的独立 Personal Agent，以可编辑的长期记忆、早晚简报式的主动性和单一长对话为核心，全球版与国内版均于 2026 年 9 月上线。分析覆盖截至 2026-11-10 收集的 22 篇资料。
---

## 概要

- Today 把自己定义为「个人智能体」，三项核心能力是持久、用户可编辑的记忆，克制的主动帮助，以及带确认的跨工具执行；所有交互在一个长对话里。（[记忆与上下文]({{< relref "/docs/today/analysis/memory" >}})）
- 主动性是实测中最受认可的能力：早晚两份简报加主动提醒，多篇实测记录了提前提醒考试报名、模型发布、行业活动的案例。团队自评主动性「只有二三十分」。（[持续执行]({{< relref "/docs/today/analysis/continuous-execution" >}})）
- 运行环境是「云端执行 + 用户设备」的混合：官方称有始终在线的云计算机，同时 macOS 客户端和 Chrome 插件直接在用户本机、已登录的浏览器里操作。云端环境的形态没有公开。（[运行环境]({{< relref "/docs/today/analysis/runtime" >}})）
- 连接器以办公协作为主，国际站 55 项云集成，国内版接飞书、钉钉、企业微信、腾讯文档和邮箱；不碰外卖、打车、订票、购物等交易，淘宝、天猫明确不支持。（[连接器]({{< relref "/docs/today/analysis/connectors" >}})）
- 全球版与国内版都对所有用户开放：全球版免费加 20 / 200 美元订阅，国内版基础版永久免费，团队称国内版现阶段不准备收费。（[开放与价格]({{< relref "/docs/today/analysis/access-pricing" >}})）
- 2026-10-21 宣布超 2 亿美元首轮融资，投资方含腾讯、蚂蚁、IDG、红杉中国；没有公开任何用户数或收入，商业模式团队自称「没有想清楚」。（[商业与规模]({{< relref "/docs/today/analysis/business" >}})）
- 团队计划自研「交互模型」，理由是前沿模型 coding 变强、「说人话」变差，截至 10 月中旬有早期实验版本。（[模型]({{< relref "/docs/today/analysis/models" >}})）
- 实测中信息整理和提醒较可靠，执行环节有误判；官方与第三方都没有完成率数据。（[实际效果与可靠性]({{< relref "/docs/today/analysis/reliability" >}})）

## 定位

Today AI 由齐俊元创立。他曾创办 Teambition（2019 年被阿里收购），后任飞书产品副总裁、豆包 PC 端负责人，2025 年 11 月离开字节后创业（[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})）。

官方博客把 Today 定义为「AI 个人智能体」，口号是「连续性胜过聪明、克制胜过喧哗、办完胜过建议」；与聊天机器人（只有会话记忆）、通用助理（浅记忆、用户配置提醒）区分，也与 Cowork 一类工作智能体区分（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})、[官方定义文]({{< relref "/docs/today/sources/official/2026-08-04-what-is-ai-personal-agent" >}})）。国内版口号是「懂你所想，为你先行的个人 AI 助理」，团队称 Today 以「人」而非任务组织，面向最大众的用户（[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})、[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。官方明确说 Today 不适合只偶尔提问、想要完全自主或需要医疗诊断的用户（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})）。

与其他跟踪产品的主要差异：

- 与 Muse 相比：Founder Park 对照试用后称两者都是长对话产品，Today 更彻底地维持单一对话、更主动；Muse 有分支对话，主动消息门槛较高（[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})）。产品笔记作者称 Today 不碰交易，与 Muse 订票、扫低价不同（[产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}})）。
- 与 Instinct 相比：Instinct 住在 iMessage 里、没有独立 App；Today 试过这种形态后放弃（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})、[智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}})）。
- 与国内大厂产品相比：多篇资料称 Today 是国内最早发布的 Personal Agent（[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）；团队自称「大战的引领者」（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）。二阶变量认为 Today 更像信息助手，缺少千问 Go、Muse、Cue 那样的执行闭环，但大厂平台像「换壳的广告推荐系统」，中立第三方 Agent 有空间（[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})）。

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2025-11 | 齐俊元离开字节创业；Z Finance 转述称 2026 年 3 月立项 | [Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})、[Z Finance]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}}) |
| 2026-03 | 团队探索住在 IM 里的无 App 形态，后放弃 | [智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}}) |
| 2026-08-03 | 官方博客 What is Today、Meet Today 发布，称已在 Mac、iOS、Android 上线、目前免费（页面更新至 09-15） | [官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})、[官方：Meet Today]({{< relref "/docs/today/sources/official/2026-08-03-meet-today" >}}) |
| 2026-09-08 | 全球版上线（晚点；智能涌现称 9 月 9 日起陆续上线） | [晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}}) |
| 2026-09-09 | 品玩发表一周体验，称国际版开启公测 | [品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}}) |
| 2026-09-18 | 发布 Today Recording（Mac、iPhone 先行） | [官方：Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}}) |
| 2026-09-20 | 发布助理评测框架 v0.1（未打分） | [官方评测框架]({{< relref "/docs/today/sources/official/2026-09-20-today-assistant-benchmark" >}}) |
| 2026-09-24 | 国内版（todayai.cn）上线 | [晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})、[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}}) |
| 2026-10-01 前后 | 国内版报道：支持 macOS、Windows、Linux、iOS，注册送 1 亿 Tokens + 1 个月 Pro | [Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}}) |
| 2026-10-15 | 中国版 Chrome 插件更新（版本 2026.10.12.16） | [Chrome 插件（中国版）]({{< relref "/docs/today/sources/official/2026-10-15-chrome-extension-china" >}}) |
| 2026-10-21 | 宣布超 2 亿美元首轮融资 | [智能涌现]({{< relref "/docs/today/sources/media/2026-10-24-zhinengyongxian-today-ten-questions" >}}) |
| 2026-10-22 前 | 三周内新增浏览器插件、「灵感」板块、简报时间设置、邀请重置额度；iPhone 版正式上线；注册赠送升至 3 亿 tokens + 3 个月 Pro | [产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}}) |
| 2026-11-05 | 集成页显示 55 项云集成（收集日期） | [集成页]({{< relref "/docs/today/sources/official/2026-11-05-integrations" >}}) |

上线日期各资料不一致：官方 8 月初已称「正式上线」，晚点称全球版 9 月 8 日上线，智能涌现称 9 月 9 日起陆续上线，AIX财经称全球版与 Muse 同日上线（[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})）。本页以晚点的说法为主，并列其他说法。

## 整体架构

用户在桌面端、移动端、网页端或绑定的微信里，与一个自己起了名字的助手进行单一长对话。助手的「活记忆」从对话和用户授权的连接器（邮件、日历、飞书、健康数据）中提取结构化事实，用户可在记忆面板查看、修改、删除。每天早晚各推送一份简报，其余时间按记忆判断是否值得主动开口，并按用户是否回复、阅读来调整频率。复杂任务被拆成后台独立任务，在官方所称的云计算机上运行，或通过 macOS 客户端、Chrome 插件在用户本机和已登录的浏览器中执行；对外发送、改日历、付款等动作须用户确认。全球版免费加订阅，国内版目前免费。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境]({{< relref "/docs/today/analysis/runtime" >}}) | 云端执行 + 用户设备网关；macOS 与 Chrome 插件直接操作本机；云端形态未公开 |
| [记忆与上下文]({{< relref "/docs/today/analysis/memory" >}}) | 结构化、可编辑的活记忆，单一长对话；实测跨周有效，也有归纳不准 |
| [持续执行]({{< relref "/docs/today/analysis/continuous-execution" >}}) | 早晚简报、周期任务、按反馈降频；主动提醒是实测中最受认可的能力 |
| [连接器]({{< relref "/docs/today/analysis/connectors" >}}) | 国际站 55 项、国内办公入口为主；不碰交易，团队称一家家谈合作 |
| [交互渠道]({{< relref "/docs/today/analysis/channels" >}}) | 自有 App 为主，可绑定微信；无独立对外身份 |
| [设备]({{< relref "/docs/today/analysis/devices" >}}) | 全平台覆盖，macOS 权限最深；硬件与合作伙伴做 |
| [模型]({{< relref "/docs/today/analysis/models" >}}) | 前沿模型 + 编排，实测见调用 Claude Opus 5；计划自研交互模型 |
| [安全]({{< relref "/docs/today/analysis/security" >}}) | 对外动作一律先确认；无提示注入防护、凭证管理的信息 |
| [隐私]({{< relref "/docs/today/analysis/privacy" >}}) | 连接数据不用于训练；国内服务由国内主体运营；权限争议无出处 |
| [开放与价格]({{< relref "/docs/today/analysis/access-pricing" >}}) | 全面开放；全球版免费 + 20/200 美元，国内版免费并加大赠送 |
| [商业与规模]({{< relref "/docs/today/analysis/business" >}}) | 超 2 亿美元首轮融资；无规模数据；商业模式未定 |
| [实际效果与可靠性]({{< relref "/docs/today/analysis/reliability" >}}) | 信息整理与提醒较好，执行有误判；无完成率数据 |

## 资料缺口

- 规模与商业：用户数、活跃度、留存、付费数据；融资轮次与估值。
- 官方文档：隐私政策原文、价格页与各档额度、国际版与国内版的功能差异对照。
- 技术：云端执行环境的形态与规格、模型路由与自研模型进展、提示注入防护与凭证管理。
- 实测：资料全部为中文，缺少国际版的英文媒体与用户实测；缺少一个月以上的长期使用记录。
- 争议说法的出处：「扫描本地磁盘」「云电脑只是沙箱」。
