---
title: "Grok Bot：实际效果与可靠性"
linkTitle: "实际效果与可靠性"
weight: 120
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  在多家社区和媒体的横向实测中，Grok Bot 在工作类任务上多次排第一，评价集中在「就是能用」、成品质量高；反复出现的问题是用量上限、多 Bot 长期运行不稳定、编码修复不可靠，以及官方文档自列的一批连接与例程故障。
---

## 概要

- 工作类任务的横向实测中，Grok Bot 多次排第一：Pat Simmons 的模拟咖啡公司三项工作全胜（总体 A-），Claire Vo 的九项任务综合第一（93%），Enterpret 的用户帖子统计中「完成任务」「完成设置」两项都排 12 款第一。日常杂事类的 Wired 记分卡上，它不在前两名。
- 评价最一致的优点是上手简单、成品可用：Claire Vo 在 2026-08 的首测中说它「就是能用」，Top5Apps 把它评为「最适合常规工作交接」。
- 用户反馈最集中的问题是用量上限。Enterpret 统计中它在「为智能体付费」一项垫底；2026-11-01 前后用量被收紧，Musk 确认不是故障（见[开放与价格]({{< relref "/docs/grok-bot/analysis/access-pricing" >}})）。
- 长期、多 Bot 运行的报告以失败为主：Reddit 用户称 4 个 Bot 做电商上架时基础操作反复出错，6 个 Bot 的团队第一天用掉约 42% 的周额度。这些报告都经中文自媒体转述。
- 官方没有公布完成率或出错率。帮助文档和更新日志公开列出了一批已知问题与修复，包括例程共享速率限制导致运行失败、回合静默结束、文件「悄悄丢失」等。

## 横向实测：工作任务领先，日常任务一般

| 测试方 | 时间与条件 | Grok Bot 的结果 | 资料 |
| --- | --- | --- | --- |
| Pat Simmons（AI for Mortals） | 模拟咖啡公司约四小时客服，另有旅行、YouTube 调研两项；咖啡公司由 Opus 5.5 打分 | 三项工作全胜；咖啡公司总体 A-（Dots B，Muse D） | [Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}}) |
| 程序员鱼皮 | 个人账号，接入 X | 简报、发帖复盘可用；视频「每页长得都一样的 PPT」；复杂任务偶尔掉链子 | [鱼皮实测]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}}) |
| Wired（Reece Rogers） | 一天五项日常任务，每项 1–5 分，六款同测 | 晨间选题 1、午餐 4、日程冲突 2、度假行程 4、失眠建议 5；最佳整体为 Dots | [Wired 全面对比]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}}) |
| Claire Vo（ChatPRD） | 九项真实任务，非受控，Claude 依她的记录打分 | 综合第一，报告 93%（Duet 79%）；缩略图、收件箱待办、买鞋胜出 | [ChatPRD 九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}}) |
| Kunal Ugale（Medium） | 真实收件箱分拣，与 Muse 对比 | 本次占优；与 Muse 同样漏查已发送文件夹 | [收件箱测试]({{< relref "/docs/industry/sources/community/2026-10-29-grokbot-muse-inbox-test" >}}) |
| Top5Apps | 同账号同任务（订餐、跟进邮件、小额购买、调整日程），加权评分 | 4.4 分第三（Muse 4.6，Instinct 4.5），「最适合常规工作交接」 | [Top5Apps 排名]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}}) |
| Enterpret | 27.7 万条帖子的用户反馈统计，12 款 | 总排名第三（57.9）；「完成任务」「完成设置」第一，「为智能体付费」垫底 | [Enterpret 用户排名]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}}) |

这些测试的口径差别很大，作者大多自己说明了局限。Claire Vo 称 93% 和 79% 没有透明的评分公式，应当作「这次运行的总结，而不是可移植的性能统计数据」，并说明 Muse 没有接 Slack、GitHub。Medium 收件箱测试的资料页只有链接，摘要依据搜索索引摘录，作者称只是「一次快照」。

从排名分布看，可能的解释是：Grok Bot 的优势集中在需要产出成品、跨多个工作系统的任务上，在要求长时间深度研究或日常生活事务的任务上并不突出。依据是 Pat Simmons 和 Claire Vo 的工作类测试都排第一，而 Wired 的晨间选题只得 1 分（Wired 记者称只有 Muse 和 Dots 在要求的 30 分钟里持续研究），Pat Simmons 也建议「个人生活，用 Muse」。

## 做得好的地方：成品可用、能绕过拦截

- **客服与运营。** Pat Simmons 的模拟中，Grok Bot 发出 58 封回复（Dots 42 封），在回复里直接处理问题，例如直接寄免费替换品；网站任务中修复坏链接、让图片加载快 15 倍、按品牌指南重写文案并保留原设计（[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。
- **成品形态。** Claire Vo 认为收件箱分拣的胜负在界面：Grok Bot 把待办放进带勾选框的文档，「能充当我的幕僚长」；Slack 回复「听起来最像我」，但 Dot 多问了是否远程、有无报酬，更理解决策（[ChatPRD 九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。
- **通过网站拦截。** 旅行任务中，Dots 被 FlightHub 的机器人检查拦住，Grok Bot「直接通过」，并找到总计 709 美元的航班和三晚 497 美元的 Airbnb（Muse 分别为 801、633 美元）；作者称它此前在另外两款被拦时也进入了 Amazon（[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。Claire Vo 的买鞋任务中，Grok 找到了不错的选项，Claude 被封锁网站困住。
- **个人事务的成功案例。** 据施言转述的 Reddit 帖（10 月 22 日），一位用户让 Grok Bot 翻出一笔 240 英镑的会计师费用错账和一笔 119 英镑的保险退款，合计 359 英镑；Bot 整理证据、草拟邮件，用户检查后发出（[施言十个案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})）。
- **上手与工作方式的变化。** 早期用户 James Pember 称过去一周因 Grok Bot 发生的工作流变化比过去 6 个月还多，但说不清是模型、运行框架还是集成质量的作用（[Pember 通讯]({{< relref "/docs/grok-bot/sources/community/2026-10-04-james-pember-grok-bot-is-really-good" >}})）；Datawhale 的作者称它是「目前 Personal Agent 体验的代表之作」（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。

## 典型失败

### 编码修复不可靠

Claire Vo 的 Sentry bug 修复任务中，Grok 很快，但修复方式是「放宽了验证」，接受本应被拒绝的输入，作者称「速度并没有让这个改动正确」；Dot 最接近预期（[ChatPRD 九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。Pat Simmons 也写明「我不会信任它做日常编码」，建议让它把大的编码工作交给 Claude Code 或 Codex（[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。

### 状态不一致与时序错误

Pat Simmons 的咖啡公司测试中，Grok Bot 在后台暂停了售罄商品，但网站仍在销售，这一项只得 B；客户 Greta 写下「Please DON'T cancel」两分钟后，它仍取消了她的替换。其他得分较低的是保持记录整洁 B、大销售线索 B+（[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。

### 视觉与多媒体成品粗糙

- YouTube 任务中，Grok Bot 的调研最详尽、标题最像作者本人风格，但没有做出缩略图、只给了样稿，并两次触到用量限制（Pat Simmons）。
- Claire Vo 的短视频任务中，叠加层「很丑」，有一个落在人物额头上；发布视频遵循了她的技能，但有布局问题和内容溢出。
- 程序员鱼皮让它做热点速览视频，交付的是「每页长得都一样的 PPT」，原定的中文配音因语音服务连接失败没有做成（[鱼皮实测]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})）。

### 多 Bot 长期运行：不稳定、管理成本高

施言转述的两篇 Reddit 帖都来自重度用户（[施言十个案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})）：

- 9 月 7 日，一位电商老板用 4 个 Grok Bot 做商品上架。复制粘贴、填写页面等基础操作仍会出错；他为各 Bot 写了大量 Skill 文件，「该出错还是出错」，前一天能完成的步骤第二天又会出问题，需要经常介入。
- 另一位用户搭了 6 个 Grok Bot 的团队，第一天用掉约 42% 的周额度，还要处理浏览器登录、任务故障和额度分配，「管理成本倒是先上来了」。

这两条是自媒体对 Reddit 截图的转述，资料页没有原帖链接，只能算单个用户的报告。一位早期用户的 BotOps 做法也说明多 Bot 需要人工管理：用表情前缀标记 Bot 的状态，其中有「死掉 / 失败」一类（[Granda BotOps]({{< relref "/docs/grok-bot/sources/community/2026-09-06-granda-botops" >}})）。

### 被平台拦截

据 Not a Tesla App 2026-10-15 的报道，一位 X 用户称亚马逊在阻止 Grok Bot 下单，他的一个 Bot 专门处理亚马逊退货；Musk 此前的回应是让 Bot 去其他商店购买（[亚马逊屏蔽]({{< relref "/docs/grok-bot/sources/media/2026-10-15-notateslaapp-amazon-blocked" >}})）。这与 Pat Simmons 10-06 发布的测试中「进入 Amazon」的描述不一致，两者时间不同，资料无法判断拦截从何时开始、覆盖哪些操作（拦截与连接器详见[连接器]({{< relref "/docs/grok-bot/analysis/connectors" >}})）。

## 官方的说法：公开已知问题，没有公布数字

资料中没有官方的任务完成率、出错率或可用性数字。官方的做法是在文档里写明失败情形和处理方法：

- **已知问题（截至 2026-11-05 的帮助文档）。** 例程可能因「所有 Grok Bot 例程共享的一个限制」报速率错误，即使自己的运行次数未超限，失败运行不自动重试，需手动重跑（[帮助：例程]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-routines" >}})）；桌面应用的 Zoom 授权报错 4700，SharePoint 应用级权限报错 AADSTS50011（[帮助：连接应用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-connect-apps" >}})）；iOS 26 以上的 iPhone 1.18.0 新建登录没有保存按钮，1.19.0 修复并逐步推出（[帮助：秘密]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-secrets" >}})）。官方对前三个都写「这是一个已知问题，我们的工程师正在修复」。
- **运行环境的失败。** 计算机显示「正在重新连接」或「无法连接」时 Bot 无法完成一轮；恢复或重置失败只建议重试一次，再联系支持（[文档：计算机与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})）。有些网站会因数据中心 IP 阻止 Bot（[安全 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security-faq" >}})）。
- **更新日志里的修复。** 截至 v0.79.3 的更新日志（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）记录了多项可靠性修复：Bot「更可靠地回复，而不是静默结束回合」；Bot 声称发送的文件不再「悄悄丢失」；Gmail 发送与回复不再报告缺少工具；下单前重新核对已批准的配送方式和总额；批准 Link 付款后继续检查约十分钟；无人接回交给用户的计算机时，聊天在 24 小时后不再显示「等待你」。这些条目说明此前存在对应的问题，但没有说明发生频率。
- **建议用户复核结果。** 工作类文档建议要求 Bot 区分源系统事实、假设、已完成动作和待批准动作，保留来源链接、截图、时间戳与操作日志，对快速变化的数据「不要只依赖截图」（[文档：工作]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})）。官方的 Data Bot 案例也承认数据团队仍处理需要更多判断的分析，并在了解它「在哪些方面需要额外指导」（[Data Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-02-data-bot" >}})）。

## 用户反馈：能力强，被上限和管理成本拖累

- 正面评价集中在「能用」：Claire Vo 首测称「GrokBot 最大的优点是它就是能用」，同时认为可控性低，不能选底层模型或深入配置（[Claire Vo 首测]({{< relref "/docs/grok-bot/sources/community/2026-08-18-chatprd-claire-vo-grokbot" >}})）；Top5Apps 转引的早期用户称它是「第一个我会交给从未用过 AI 的人的产品」。
- 负面反馈集中在用量：Enterpret 的结论是「任务最强，限制最糟」，Grok Bot 表明「一款有能力的智能体仍可能在上限处流失用户」（[Enterpret 用户排名]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})）。TechCrunch 报道，万圣节周末一些用户发现每周用量在没有使用的情况下被用满，Musk 2026-11-01 确认不是故障，原因是服务成本「相对收入」高得不可持续（[TechCrunch 收紧用量]({{< relref "/docs/grok-bot/sources/media/2026-11-02-techcrunch-throttles-limits" >}})）。
- 程序员鱼皮的评价代表了一般用户的体验：「省心」，但速度不快，「复杂任务偶尔也会掉链子，结果还是得人工检查一遍」。

推断：从 Pat Simmons 的 YouTube 任务（两次触限）、6 Bot 用户第一天用掉约 42% 周额度和 Enterpret 的付费项垫底看，用量上限对重度、多 Bot 用户的影响可能大于能力本身的不足。资料中没有不同档位能支撑多少任务的官方数字，这一点无法量化。

## 资料缺口

- 官方的任务完成率、出错率、可用性数据或状态页；已知问题（例程共享速率限制、Zoom、SharePoint）的修复时间。
- 用户自己的实测（`exploration/` 为空）；数周以上的长期使用记录与复测。
- 电商上架、6 Bot 团队两篇 Reddit 原帖（目前只有施言的转述）；Medium 收件箱测试原文（仅链接）。
- 亚马逊拦截的时间、范围与官方回应；Pat Simmons 测试时能进入 Amazon 与之后被拦的先后关系。
- 不同档位实际能支撑的任务量，与 2026-11 收紧前后的对比。

## 主要资料

**官方**

- [帮助：例程]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-routines" >}})：共享速率限制的已知问题。
- [帮助：连接应用]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-connect-apps" >}})、[帮助：秘密]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-secrets" >}})：Zoom、SharePoint、iPhone Vault 的已知问题。
- [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})：可靠性相关的修复。
- [文档：计算机与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})、[安全 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security-faq" >}})：运行环境的失败情形、网站拦截。
- [文档：工作]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})、[Data Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-02-data-bot" >}})：复核建议与官方承认的局限。

**媒体**

- [Wired 全面对比]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})：六款一天五项任务的记分。
- [TechCrunch 收紧用量]({{< relref "/docs/grok-bot/sources/media/2026-11-02-techcrunch-throttles-limits" >}})：用量收紧与 Musk 的确认。
- [亚马逊屏蔽]({{< relref "/docs/grok-bot/sources/media/2026-10-15-notateslaapp-amazon-blocked" >}})：用户报告被亚马逊阻止下单。

**社区**

- [Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})：模拟公司、旅行、YouTube 三项同题测试。
- [ChatPRD 九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})：四款九项任务，含编码修复的失败。
- [Claire Vo 首测]({{< relref "/docs/grok-bot/sources/community/2026-08-18-chatprd-claire-vo-grokbot" >}})、[Pember 通讯]({{< relref "/docs/grok-bot/sources/community/2026-10-04-james-pember-grok-bot-is-really-good" >}})、[Granda BotOps]({{< relref "/docs/grok-bot/sources/community/2026-09-06-granda-botops" >}})：早期用户的使用体验。
- [鱼皮实测]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})、[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})：中文用户的体验。
- [收件箱测试]({{< relref "/docs/industry/sources/community/2026-10-29-grokbot-muse-inbox-test" >}})、[Top5Apps 排名]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})、[Enterpret 用户排名]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})：对照测试与用户反馈统计。
- [施言十个案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})：Reddit 成功与失败案例的转述。
