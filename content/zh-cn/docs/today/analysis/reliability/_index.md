---
title: "Today AI：实际效果与可靠性"
linkTitle: "实际效果与可靠性"
weight: 120
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  媒体实测对 Today 的信息整理与主动提醒评价较好，对执行环节褒贬不一：翻译、汇总、发邮件能完成，安装步骤误判、轻任务做重、交易类服务进不去。官方和第三方都没有完成率、出错率数字；官方评测框架发布时尚未打分。
---

## 概要

- 官方没有公布任务完成率、出错率；9 月发布的评测框架 v0.1 写明「目前什么都还没测」。唯一的量化结果是 Today Recording 的说话人归属错误率下降超过四个百分点（对比三家语音供应商）。
- 做得好的：主动提醒与信息整理（考试公告、行业动态、图书馆检索「完全准确」）、多任务并行、跨周记忆、确认后发邮件。
- 做不好的：归纳用户情况不准确（Founder Park）；安装步骤给出笃定但无效的指令，耗费作者一小时（极客公园）；轻问题处理过重；挂号、缴费、订酒店、买机票「一个都进不去」（AIX财经）。
- 用户反馈两极分化：团队称有人下载两分钟就卸载，也有人离不开；资深用户尚晋认为 Today 的交互「不够自然」。
- 官方自称「Today 还没做完」，「并非冻结的企业 SLA」。

## 官方的量化信息

官方评测框架 v0.1 有 12 个维度，发布时「目前什么都还没测，Today 没测，任何产品都没测」（[官方评测框架]({{< relref "/docs/today/sources/official/2026-09-20-today-assistant-benchmark" >}})）。Today Recording 的转写评测：公开基准中 5.5 小时的多人重叠长会议，对比三家语音供应商原始输出，说话人归属错误率下降超过四个百分点，文字误差保持稳定（[官方：Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})）。官方博客称「Today 还没做完」（[官方：Meet Today]({{< relref "/docs/today/sources/official/2026-08-03-meet-today" >}})），简报、连接器和 Skills 都在持续演进，「并非冻结的企业 SLA」（[官方：What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})）。

## 实测汇总

| 来源 | 时间 | 做到的 | 问题 |
| --- | --- | --- | --- |
| [品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}}) | 2026-09-09，一周 | 约采访：查联系人、查日历、确认后发邮件，对方回信后主动跟进；提前推送模型发布与 Suno 政策变化 | 主动程度有时让人「烦」；记忆错误可能难纠正（作者担忧） |
| [Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}}) | 2026-10-01，国内版 | 4 个任务后台并行；整理结果生成可分享的 HTML 页 | 对个人情况的归纳不完全准确；纠错效果待验证 |
| [极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}}) | 2026-10-08，十天 | mod 汉化 15 分钟完成，重构干净；每天推送选题并追问进度 | 安装目录判断错误耗费一小时；足球陪练方案做成网页，「很轻的问题被处理得过重」 |
| [产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}}) | 2026-10-22 | 浏览器插件汇总三天发帖；简报选题贴合 | 作者个人感受，无对照 |
| [二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}}) | 2026-11-06，数周 | 考试公告提醒后成功报名；深圳图书馆检索「完全准确」；周末活动推荐 | 不支持淘宝、天猫；生活类上下文来源有限 |

二阶变量作者称最有用的案例几乎都和教育、公共信息有关（[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})）。极客公园作者对 Today「又爱又恨」，认为它分不清轻重缓急（[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})）。

## 用户反馈

- 晚点访谈：公测一个月后用户两极分化，有人下载手机端两分钟就卸载，不习惯长对话；团队上线 multi-task 应对（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）。
- AIX财经：一位 Today 用户让 Agent 挂号、缴费、订酒店、买机票，「一个都进不去」；资深用户尚晋认为 Today AI 和 Dots 的交互仍不够自然，最终留下 Instinct 和 Muse（[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})）。
- Datawhale 刊发的阿里云专家综述称 Today「整体交互比较简单」（[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。

晚点访谈中团队自评主动性「仍只有二三十分」，并称还没有信心说一年内能大规模普及（[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})）。

推断：官方宣称与实测的差距主要不在「先确认再执行」这类设计原则（品玩实测与官方一致），而在执行深度：对交易和第三方平台的覆盖有限，本机操作中会出现自信的错误判断。

## 资料缺口

- 任何口径的任务完成率、出错率；评测框架之后公布的分数。
- 一个月以上的长期使用实测；国际版的英文媒体或用户实测（目前资料全部是中文）。
- 服务可用性、宕机记录。
- 用户评分与应用商店评论。

## 主要资料

- 官方：[What is Today]({{< relref "/docs/today/sources/official/2026-08-03-what-is-today" >}})（「并非冻结的企业 SLA」）；[官方评测框架]({{< relref "/docs/today/sources/official/2026-09-20-today-assistant-benchmark" >}})；[Today Recording]({{< relref "/docs/today/sources/official/2026-09-18-introducing-today-recording" >}})；[Meet Today]({{< relref "/docs/today/sources/official/2026-08-03-meet-today" >}})。
- 媒体：[品玩]({{< relref "/docs/today/sources/media/2026-09-09-pingwest-today-demo" >}})、[Founder Park]({{< relref "/docs/today/sources/media/2026-10-01-founderpark-today-china-launch" >}})、[极客公园]({{< relref "/docs/today/sources/media/2026-10-08-geekpark-today-ten-days" >}})、[二阶变量]({{< relref "/docs/today/sources/media/2026-11-06-erjiebianliang-today-hands-on" >}})（实测）；[晚点]({{< relref "/docs/today/sources/media/2026-10-16-latepost-today-ai-interview" >}})（两极分化、自评）；[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})（用户反馈）。
- 社区：[产品笔记]({{< relref "/docs/today/sources/community/2026-10-22-chanpinbiji-today-funding" >}})；[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})。
