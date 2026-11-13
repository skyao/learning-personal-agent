---
title: "Grok Bot：模型"
linkTitle: "模型"
weight: 70
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Grok Bot 不绑定单一模型，由系统为每个任务挑选后端模型（xAI 第一方模型或子处理方名单上的第三方模型）。用户看不到、选不了，也屏蔽不了某个模型。具体用的是哪个模型，第三方说法互相矛盾：有说 Grok 4.7 的，也有说 Claude Opus 5.5 的。
---

## 概要

- 官方帮助文档与两套官方文档（cursor.com、docs.x.ai）一致写明：Grok Bot「不绑定单一模型」，对每个任务使用「最有可能带来最佳结果」的后端模型，可能是 xAI 第一方模型，也可能是子处理方名单上的第三方模型。同一用户的不同请求可能用到不同模型。
- 用户无法查看、指定或屏蔽模型，设置里没有模型选择器。用量与支出统一记作 Grok Bot 用量，不按模型拆分。团队在 Cursor 中设置的模型允许列表、屏蔽列表对 Grok Bot 不生效。
- 官方资料中唯一点名的第三方模型是 Opus 5.5：帮助文档答复称，任务路由到 Opus 5.5「不会改变你每个 token 的成本」。
- 具体由哪个模型驱动，第三方说法并存且互相矛盾：Grok 4.7（AI for Mortals、湾区OPC指南、AI问消）、Claude Opus 5.5（程序员鱼皮转述团队成员），以及「官方未说明」（Top5Apps、iThome）。资料库中没有官方的模型分配比例或规则。
- 模型之外还有两层专门分工：编码交给 Cursor 内的专用编码运行框架；有风险的操作在执行前由独立的审查模型（Auto Review）评估。

## 每个任务由系统选模型，用户不可见、不可选

据官方帮助文档（截至 2026-11-05 的资料），模型选择完全由系统负责：

| 问题 | 官方答复 | 资料 |
| --- | --- | --- |
| 用什么模型 | 不绑定单一模型；每个任务使用最可能取得最佳结果的后端模型，可能是 xAI 第一方模型，也可能是子处理方名单上的第三方模型；同一用户的不同请求可能不同 | [帮助：Grok Bot 用哪些模型]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-models" >}})、[安全文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}}) |
| 能否自选 | 不能。没有模型选择器，用户「不能被路由到某个特定模型，也不能被路由离开某个特定模型」 | [帮助：Grok Bot 用哪些模型]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-models" >}})、[docs.x.ai 常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}}) |
| 能否看到所用模型 | 不能。用量与支出界面统一记作 Grok Bot 用量 | [帮助：Grok Bot 用哪些模型]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-models" >}}) |
| 团队模型策略 | Cursor 的模型允许列表或屏蔽列表对 Grok Bot 不生效；设有允许列表的团队启用时会看到确认；合同限制子处理者的客户需联系客户团队 | [安全文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}}) |
| 模型集合是否固定 | 不保证固定的供应商集合，服务组合可能随时间变化 | [安全文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}}) |
| 成本 | 路由到 Opus 5.5 不会改变每个 token 的成本 | [帮助：Grok Bot 用哪些模型]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-models" >}}) |

docs.x.ai 上的另一套文档说法相同，把第一方模型称为「SpaceXSI 模型」（[docs.x.ai 常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})）。面向企业的推理钩子（inference hooks）会把每次模型请求发给客户自己的安全服务器，请求帧中的 `model` 字段是「Cursor 模型标识符」。文档特意说明该字段只用于报表，不要用于允许列表（[推理钩子文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-inference-hooks" >}})）。这与「不承诺模型集合」的口径一致。

更新日志中有两条体现了按地区和按安全过滤切换模型：

- v0.70.2（2026-10-11）：「当模型在你的地区不可用时，回合会停止并解释原因，Bot 会回退到 Grok」。
- v0.77.0（2026-10-26）：「当安全过滤器停止计算机任务时，Bot 会先在另一个模型上重试，然后再请你完成该步骤」。

（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）

用户实测普遍注意到不能选模型。Claire Vo 在发布初期的上手评测中认为，这让 Grok Bot 开箱即用，但可控性低：「你不能选择底层模型，也无法深入其配置的细节」。她还称模型的个性有她所说的「Claude Slop」，即「没有感觉」（[How I AI 评测]({{< relref "/docs/grok-bot/sources/community/2026-08-18-chatprd-claire-vo-grokbot" >}})）。Archieli 则把同一点看作优点：用户「不需要选择模型，也不需要主动配置 agent 的协作」（[Archieli]({{< relref "/docs/industry/sources/community/2026-11-11-archieli-grok-bot-work-mode" >}})）。

## 第三方对「用哪个模型」说法不一

| 说法 | 来源 | 说明 |
| --- | --- | --- |
| 运行于 Grok 4.7 | [AI for Mortals（Pat Simmons，10-06）]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}}) | 作者对 Grok 4.7 的评价：「人们不太喜欢它，包括我」 |
| 自研 Grok 4.7，「中规中矩」 | [湾区OPC指南（10-23）]({{< relref "/docs/industry/sources/community/2026-10-23-wanqu-opc-how-to-choose" >}})、[AI问消（11-09）]({{< relref "/docs/industry/sources/community/2026-11-09-aiwenxiao-personal-agent-family-tree" >}}) | 选购指南式的评价，未给出处 |
| 由 Claude Opus 5.5 驱动 | [程序员鱼皮（10-12）]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}}) | 转述：10 月 7 日马斯克在 X 上宣布 Grok Bot 会为每个任务选择最合适的后端模型，点名 Claude Opus 5.5、Midjourney 和 Suno；又称团队成员透露「所有 Bot 都会由 Claude Opus 5.5 驱动」。资料库中没有这条 X 帖的原文 |
| 官方未说明是否运行 Grok 4.7 | [Top5Apps（11-01）]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}}) | 称 SpaceXAI 只说 Grok 4.7 经训练能「原生理解 Grok Bot harness」 |
| 官方未公开绑定单一模型，由 Cursor 管理模型选择 | [iThome（10-02）]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}}) | 与官方帮助文档的说法一致 |

几种说法并不完全互斥：官方的机制是按任务混用第一方和第三方模型，因此「用 Grok 4.7」和「用 Opus 5.5」都可能只描述了一部分请求。各方没有给出比例，资料也不足以判断哪种说法更接近实际。

Claire Vo 8 月评测的是同期的 Grok 4.6（标题写 Grok 4.6，正文写作「Groq 4.6」），认为它「在创意设计任务上」表现好。但她没有说明 Grok Bot 用的就是 4.6（[How I AI 评测]({{< relref "/docs/grok-bot/sources/community/2026-08-18-chatprd-claire-vo-grokbot" >}})）。

湾区OPC指南与 AI问消都认为，Grok Bot（以及 Muse）绑定自家模型，一旦 GPT 或 Claude 拉开差距，用户无法更换。这与官方「混用第三方模型」的说明不符。推断：这类说法可能把 Grok 品牌等同于 Grok 模型，没有参考帮助文档。

## 编码、审查与客服：模型之外的专门分工

- **编码交给 Cursor**：官方入门指南称 Grok Bot「并不写代码」，而是生成提示词，发给「位于 Cursor 内部的一个专用编码运行框架」（[入门 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})）。Datawhale 的综述也把它描述为外层 Bot 调度 Cursor 云端 Agent（[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。
- **独立审查模型**：Auto Review 是「一个独立的审查模型」，在有风险的操作执行前评估 shell 命令、应用调用、计算机使用、自动化写入和委派。它审查的是即将执行的操作，而不是用户的提示词（[安全文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})）。详见[安全](../security/)。
- **客服场景的训练**：xAI 的客服实践文章称「我们在超过一百万次客户互动上训练了 Grok Bot」，用来学习回复语气。为控制令牌开销，他们还对常见工单做了分类（[客服实践]({{< relref "/docs/grok-bot/sources/official/2026-09-22-grok-bot-customer-support" >}})）。文中没有说明这里的「训练」是指模型训练，还是提示词与知识库的配置。

## 上下文窗口与改进机制（转述演讲）

Peter Piekarczyk 的博客文章大部分转述自 Cursor 的 Lee Robinson 关于 Grok Bot 实现方式的演讲，演讲没讲到的部分由作者凭经验补充（收录说明已写明）。文中称：

- 主智能体的上下文窗口「大约是 200K token」，对比 Codex 和 Claude「大约是 1M，但可配置」；
- 改进分两个循环：内循环每天运行，修复运行框架、提示词等，再用 eval 检查；外循环「每月或每几个月」运行一次，「用收集到的失败案例训练新模型」。

（[给 Grok Bot 发消息时实际发生了什么]({{< relref "/docs/grok-bot/sources/community/2026-10-14-peterp-what-happens-when-you-message" >}})）

这两点是转述，官方资料中没有对应说明。外循环训练出的是哪一家的模型，文中也没有说。

## 生成类能力

更新日志显示，v0.75.2（2026-10-22）起，Bot 可以「根据描述或你分享的图片创建视频」（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。程序员鱼皮做了实测：

- Bot 坚持不生成真实人物的照片；
- 根据 20 个帖子生成了一条「60 多秒的竖屏视频」，但原计划的中文配音因「中文语音服务连接失败」，最后交付的是无声版本。

（[程序员鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})）

资料没有说明图像、视频、语音分别由哪个模型或服务提供。

## 资料缺口

- 第一方模型的名称与版本（Grok 4.7 是否、何时用于 Grok Bot），以及第一方与第三方模型的分配规则或比例。
- 马斯克 10 月 7 日关于后端模型选择的 X 帖原文；「所有 Bot 由 Claude Opus 5.5 驱动」的一手出处。
- 子处理方名单中实际涉及模型的供应商。
- 上下文窗口、失败案例训练等实现细节的官方说明，以及 Lee Robinson 演讲的原始记录。
- 图像、视频、语音生成所用的模型或服务。

## 主要资料

**官方**

- [帮助：Grok Bot 用哪些模型]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-models" >}})：模型选择机制、不可选、用量统计、Opus 5.5 成本答复
- [安全文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})：第一方与子处理方模型、团队允许列表不生效、Auto Review 审查模型
- [docs.x.ai 常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})：另一套文档中的相同说法（SpaceXSI 模型）
- [推理钩子文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-inference-hooks" >}})：`model` 字段只用于报表
- [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})：地区回退到 Grok、安全过滤后换模型重试、视频生成
- [入门 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})：编码交给 Cursor 编码运行框架
- [客服实践]({{< relref "/docs/grok-bot/sources/official/2026-09-22-grok-bot-customer-support" >}})：在一百万次客户互动上训练

**媒体**

- [iThome]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})：由 Cursor 管理模型选择

**社区**

- [How I AI 评测]({{< relref "/docs/grok-bot/sources/community/2026-08-18-chatprd-claire-vo-grokbot" >}})：不能选模型、模型个性
- [给 Grok Bot 发消息时实际发生了什么]({{< relref "/docs/grok-bot/sources/community/2026-10-14-peterp-what-happens-when-you-message" >}})：200K 上下文、内外循环（转述演讲）
- [程序员鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})：Opus 5.5 说法、视频生成实测
- [AI for Mortals]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})、[湾区OPC指南]({{< relref "/docs/industry/sources/community/2026-10-23-wanqu-opc-how-to-choose" >}})、[AI问消]({{< relref "/docs/industry/sources/community/2026-11-09-aiwenxiao-personal-agent-family-tree" >}})：Grok 4.7 说法
- [Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})：官方未说明是否运行 Grok 4.7
- [Archieli]({{< relref "/docs/industry/sources/community/2026-11-11-archieli-grok-bot-work-mode" >}})、[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})：用户视角的「不需选模型」、外层 Bot 调度 Cursor
