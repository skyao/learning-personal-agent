---
title: "Gemini Spark 资料分析和总结"
linkTitle: "分析总结"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Gemini Spark 是 Google 2026-05-19 在 I/O 发布的全天候个人智能体，内嵌在 Gemini 应用中，2026-10 改名为 Gemini 的 Task 模式；分析覆盖截至 2026-11-10 收集的 20 篇 Spark 资料和 10 篇涉及 Spark 的行业资料。
---

## 概要

- Spark 不是独立产品，而是 Gemini 应用（手机、网页、Mac）里的一种模式。10 月它从独立空间并入主界面，改名为 Task，官方没有发公告。它捆绑在 Google AI Pro 和 Ultra 订阅里，不单独收费。（[交互渠道]({{< relref "/docs/gemini-spark/analysis/channels" >}})、[开放与价格]({{< relref "/docs/gemini-spark/analysis/access-pricing" >}})）
- 上下文直接来自用户的 Google 账号（Gmail、Workspace、相册、Personal Intelligence），连接器以 Google 自家服务为主，第三方只有少数合作和用户自填的 MCP 服务器。实测中它的个人化程度最让人印象深刻，也最让人不安。（[记忆与上下文]({{< relref "/docs/gemini-spark/analysis/memory" >}})、[连接器]({{< relref "/docs/gemini-spark/analysis/connectors" >}})、[隐私]({{< relref "/docs/gemini-spark/analysis/privacy" >}})）
- 在 Google 云端运行，设备关机后继续工作；上网有本地 Chrome（用已登录账号和保存的密码）和云端远程浏览器两条路径；Mac 应用负责本机文件，可从手机远程控制。（[运行环境]({{< relref "/docs/gemini-spark/analysis/runtime" >}})、[设备]({{< relref "/docs/gemini-spark/analysis/devices" >}})）
- 后台工作由「任务、计划、技能」三块组成：计划可按时间、Gmail 来信或话题事件触发，上限为 50 个活跃计划、15 个并发任务。机制设计完整，但没有长期运行的实测。（[持续执行]({{< relref "/docs/gemini-spark/analysis/continuous-execution" >}})）
- 安全靠逐项确认，加上敏感信息检查和接管模式；官方明确承认提示注入风险，并把用户监督称为最重要的防线。使用前提是开启 Keep Activity，第三方据此称数据会用于训练和人工审核。（[安全]({{< relref "/docs/gemini-spark/analysis/security" >}})、[隐私]({{< relref "/docs/gemini-spark/analysis/privacy" >}})）
- 实测结论比较一致：在 Google 生态内整理、起草做得好（AI Agents Library 中与 Dots 几乎持平），在外部网站上下单、订位和常识判断上频繁失败。用户讨论统计中，「完成任务」一项排 12 款中第 10。（[实际效果与可靠性]({{< relref "/docs/gemini-spark/analysis/reliability" >}})）
- 开放上，5 月只给美国 Ultra，7 月扩到 160 多个国家的 Pro；欧洲经济区、英国、瑞士、尼日利亚始终除外，只支持个人账号。（[开放与价格]({{< relref "/docs/gemini-spark/analysis/access-pricing" >}})）

## 定位

官方称 Spark 让 Gemini 「从一个能回答问题的助手，转变为在你的指示下代表你实际做事的主动伙伴」，是 Gemini 应用 I/O 一揽子更新的一部分，与 Gemini 3.5 Flash、Daily Brief、macOS 应用同日发布（[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})）。产品页称它是「你的 24/7 个人 AI 智能体」，帮用户打理数字生活：聊天机器人等提示，Spark 在用户指挥下主动行动、跨应用完成多步任务；面向普通人，不需要编程（[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})）。

媒体把它看作 Google 对 OpenClaw 的回应：WIRED 称它是「Google 对爆红的 OpenClaw 智能体的回应」（[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})），The Verge 认为「网络访问更好的 OpenClaw」是不算错的描述，Google 打算让它成为用户使用外部应用的界面，并逐渐操作用户的电脑（[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})）。

2026-10 改名为 Task，官方给的理由是用户总在说「任务」（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。Chrome Unboxed 和 9to5Google 都认为这是在淡化 Spark 品牌，把智能体能力并入 Gemini 主体验（[Chrome Unboxed]({{< relref "/docs/gemini-spark/sources/media/2026-10-01-chromeunboxed-ditching-spark-brand" >}})、[9to5Google]({{< relref "/docs/gemini-spark/sources/media/2026-10-12-9to5google-task-redesign" >}})）。

与其他跟踪产品相比，第三方资料中的主要差异是：

| 对比对象 | 差异 | 资料 |
| --- | --- | --- |
| OpenAI Dots | 同属平台型；Dots 擅长交付成品，Spark 在工作位于 Google Workspace 时最强，「区分它们的是形态，而不是质量」；Dots 经插件连 4,000 多个应用，入门价每月 100 美元 | [AI Agents Library 三方对照]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})、[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})、[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}}) |
| Meta Muse | 同属平台型；Muse 免费起步、有独立的 Sentinel 审查智能体，Mac 版离开电脑可继续；WIRED 的 30 分钟研究测试中 Muse 持续工作、Spark 几分钟交卷 | [iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})、[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}}) |
| Claude Duet、Grok Bot | 二者都有独立应用；Spark 只是 Gemini 内的模式 | [WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}}) |
| Instinct、Manus Cue | 独立助手，有自己的号码或邮箱（Instinct 通过短信、电话工作）；Spark 以用户的 Gmail 对外 | [中金研报]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})、[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}}) |

国内资料把 Spark 与 Muse、Dots 归为「依托既有平台入口」的平台型助手：中金研报认为平台型助手可复用分发渠道、付费体系和个人数据，但可能因与其他平台的利益冲突而权限受限（[中金研报]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})）；Datawhale 综述与鸿煊称 Spark 的优势来自 Google 生态（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。多位评测者的选择建议相同：生活和工作已经在 Google 上的人选 Spark（[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})、[Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})、[AI Agents Library 三方对照]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})）。

## 时间线

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-05-19 | I/O 发布：当周给受信测试者，下周以 Beta 向美国 AI Ultra 推出；运行在 Gemini 3.5 上；带计划和技能；Canva、OpenTable、Instacart MCP 连接；macOS 应用开放下载 | [I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})、[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}}) |
| 2026-05-29 至 06-02 | WIRED、The Verge 发表上手实测 | [WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})、[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})、[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}}) |
| 2026-06-17 | 扩展到大部分地区（澳大利亚、加拿大、欧洲经济区、香港、印度、日本、尼日利亚、韩国、瑞士、英国除外） | [更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}}) |
| 2026-06-29 | 接入 Google Tasks、Keep、Docs 评论；支持自定义 MCP 应用 | [更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}}) |
| 2026-06-30 | 话题监控；Mac 版 Beta（美国、Ultra、18 岁以上），Mac 应用提供计划和技能 | [6 月更新]({{< relref "/docs/gemini-spark/sources/official/2026-06-30-spark-updates-june" >}})、[更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}}) |
| 2026-07-01、07-07 | Canva、Instacart、OpenTable；Dropbox、Zillow 接入 | [更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}}) |
| 2026-07-14 | Ultra 全地区全语言（欧洲经济区、尼日利亚、瑞士、英国除外）；Workspace 编辑操作扩充；远程控制 Mac | [更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}}) |
| 2026-07-16 | 向美国 AI Pro 推出英语版 | [更新日志]({{< relref "/docs/gemini-spark/sources/official/2026-07-17-whats-new-for-spark" >}}) |
| 2026-07-30 | Chrome 自动浏览（最初只在美国）；向 160 多个新增国家的 AI Pro 开放 | [Chrome 集成]({{< relref "/docs/gemini-spark/sources/official/2026-07-30-spark-chrome" >}}) |
| 2026-08-13 | 改用 Gemini 3.7 Flash | [3.7 Flash 发布]({{< relref "/docs/gemini-spark/sources/official/2026-08-13-gemini-3-7-flash-spark" >}}) |
| 2026-09 | Google 相册逐步在任务中可用（资料页依据 The Verge 2026-09-04 报道） | [帮助：相册工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-google-photos-workflows" >}}) |
| 2026-09-30 | 技能扩展到 Gemini 普通聊天 | [帮助：技能]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-skills" >}}) |
| 2026-10-01 前后 | 网页版改版，「Switch to Spark」改为 Chat / Task 切换，新增 Scheduled 区域；无官方公告 | [Chrome Unboxed]({{< relref "/docs/gemini-spark/sources/media/2026-10-01-chromeunboxed-ditching-spark-brand" >}}) |
| 2026-10 | 改名为 Task；Argon 模型推出，任务模式可选 Flash 或 Argon | [帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})、[帮助：Gemini 模型]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-gemini-models" >}}) |
| 2026-10-12 | Android 版改版，「Gemini Spark Settings」改名「Task settings」 | [9to5Google]({{< relref "/docs/gemini-spark/sources/media/2026-10-12-9to5google-task-redesign" >}}) |
| 2026-10-13 至 10-16 | 表格写入被「Blocking policy check」拦截，楼主回报已修复 | [开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}}) |
| 2026-11-10 | 帮助页更新，删去「选择加入 Personal Intelligence」的要求 | [帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}}) |

## 整体架构

用户在 Gemini 应用里用「Task」切换发起任务，手机、网页、Mac 三端共用（[交互渠道]({{< relref "/docs/gemini-spark/analysis/channels" >}})）。任务在 Google 云端运行，设备关机后继续；需要上网时，用户桌面上的 Chrome 开着就用本地浏览器和已登录账号，否则用云端远程浏览器；另有一台远程计算机运行代码、生成文件；Mac 应用负责本机文件（[运行环境]({{< relref "/docs/gemini-spark/analysis/runtime" >}})、[设备]({{< relref "/docs/gemini-spark/analysis/devices" >}})）。

上下文来自用户的 Google 账号——Personal Intelligence、Gmail、Workspace、相册——加上用户编写的技能（[记忆与上下文]({{< relref "/docs/gemini-spark/analysis/memory" >}})）。外部服务以 Google 自家应用为主，第三方经少数官方合作或用户自填的 MCP 服务器接入，其余网站走浏览器（[连接器]({{< relref "/docs/gemini-spark/analysis/connectors" >}})）。计划按时间、Gmail 来信或话题事件触发任务（[持续执行]({{< relref "/docs/gemini-spark/analysis/continuous-execution" >}})）。

发送、修改删除、购买、提交表单、用 Google 登录每次都要用户确认，输入密码和付款信息时由用户接管（[安全]({{< relref "/docs/gemini-spark/analysis/security" >}})）。模型默认用 Flash，可手动换 Argon（[模型]({{< relref "/docs/gemini-spark/analysis/models" >}})）。用量按计算量计入用户的 Google AI Pro 或 Ultra 订阅（[开放与价格]({{< relref "/docs/gemini-spark/analysis/access-pricing" >}})）。

## 主题分析

| 主题 | 要点 |
| --- | --- |
| [运行环境]({{< relref "/docs/gemini-spark/analysis/runtime" >}}) | 云端运行，设备关机后继续；本地 Chrome 与云端远程浏览器两条路径，另有保存数据的远程计算机；环境规格官方未公开 |
| [记忆与上下文]({{< relref "/docs/gemini-spark/analysis/memory" >}}) | 不另建记忆，用 Google 账号数据和 Personal Intelligence；实测个人化程度很高，但会判断错人际关系；技能是用户可管理的长期上下文 |
| [持续执行]({{< relref "/docs/gemini-spark/analysis/continuous-execution" >}}) | 任务、计划、技能三块；时间、Gmail、话题三种触发；50 个活跃计划、15 个并发任务；实测中交卷快、跟进弱 |
| [连接器]({{< relref "/docs/gemini-spark/analysis/connectors" >}}) | Google 自家服务为主，第三方合作少，自定义 MCP 只对美国开放；10 月表格写入故障 |
| [交互渠道]({{< relref "/docs/gemini-spark/analysis/channels" >}}) | 只在 Gemini 应用内，10 月并入主界面改名 Task；以用户的 Gmail 对外，I/O 预告的短信和邮件入口未见落地 |
| [设备]({{< relref "/docs/gemini-spark/analysis/devices" >}}) | 手机、网页、Mac；Chrome 自动浏览仅桌面，远程浏览器仅移动端；Mac 可被远程控制；无专用硬件 |
| [模型]({{< relref "/docs/gemini-spark/analysis/models" >}}) | Gemini 3.5 → 3.7 Flash（8-13）→ Flash / Argon 可选（10 月）；思考级别可调，越高越耗用量 |
| [安全]({{< relref "/docs/gemini-spark/analysis/security" >}}) | 逐项确认加敏感信息检查和接管模式；官方承认提示注入风险；可用保存的密码引来「最宽松」的评价；无已披露漏洞 |
| [隐私]({{< relref "/docs/gemini-spark/analysis/privacy" >}}) | 必须开启 Keep Activity，第三方称会用于训练和人工审核；任务中可能向网站分享个人信息；删除入口分散 |
| [开放与价格]({{< relref "/docs/gemini-spark/analysis/access-pricing" >}}) | 捆绑在 AI Pro（约 20 美元）和 Ultra（约 100 美元）中；美国 Ultra → 160 多国 Pro；欧洲、英国除外，只支持个人账号 |
| 商业与规模 | 资料不足，不单独成页。本库没有 Spark 的用户数、付费或收入数据；I/O 稿中「230 个国家和地区的 9 亿多人」是 Gemini 应用整体的数字（[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})）。Enterpret 的统计中，Spark 的发帖用户只有 2,960 人，是 Dots（13,279 人）的约四分之一，声量份额 1.6%（[Enterpret 用户偏好]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})）。商业模式是捆绑订阅，中金研报认为这是平台型助手复用既有付费体系（[中金研报]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})）。产品页称「部分企业用户」可用，但帮助页写明工作和学校账号不可用（[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})、[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。 |
| [实际效果与可靠性]({{< relref "/docs/gemini-spark/analysis/reliability" >}}) | Google 生态内整理和起草好，外部网站动作和常识判断弱；测评排名从与 Dots 持平到中下游不等 |

## 资料缺口

- Spark（Task）的用户数、使用量、付费转化等任何规模数据；Google 是否在财报中提及。
- 云端环境的规格与隔离方式；各档位的计算量额度。
- Gemini 隐私政策与 Keep Activity 的原文：任务数据是否用于训练、保存期限；排除欧洲经济区、英国等地的原因。
- 改名 Task 的官方说明与日期；I/O 预告的短信和邮件入口、自定义子智能体是否落地。
- 8 月以后（3.7 Flash、Argon、Chrome 自动浏览）的独立实测；计划和话题监控的长期使用实测；用户自己的实测（`exploration/` 为空）。
- 「部分企业用户」的含义与 Workspace 版计划。
- 10 月表格写入故障的官方说明；漏洞赏金与第三方安全研究。
