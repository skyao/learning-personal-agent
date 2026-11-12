---
title: "OpenAI Dots：隐私"
linkTitle: "隐私"
weight: 90
analyzedAt: 2026-11-12
sourcesUntil: 2026-11-11
description: >
  个人套餐的 dots 数据是否用于训练取决于「为所有人改进模型」设置，企业版默认不训练；dot 的记忆无法逐条删除，活跃 dot 的云端快照在多数工作区没有最长保留期；EEA、英国、瑞士的 Pro 用户暂不可用。
---

## 概要

- 训练：Business、Enterprise、Edu 默认不用于训练；个人套餐由「为所有人改进模型」设置决定，范围可能包括 dot 执行的操作、委派的工作和来自已连接应用的数据。主动研究的笔记不直接用于训练，但被带入对话后可能被用到。官方资料没有说明个人套餐的默认值。
- 删除：不能逐条删除 dot 的记忆，只能删除整个 dot；删除后 dot 的数据在 30 天内删除，但 ChatGPT 对话、Codex 会话线程、已发出的消息等不随之删除。
- 保存：活跃 dot 的云端快照在未启用数据驻留或 EKM 的工作区「没有最长保留期限」，客户目前无法要求提前清除。dots 不提供严格的零数据保留。
- 第三方：Slack 中 dot 只对所有者负责，把私人信息带到频道前需要同意；资料中没有关于对方知情同意的官方说明。
- 地区：个人 Pro 不覆盖 EEA、英国、瑞士，需 18 岁以上。关于数据驻留，两份同日收集的官方文档说法不一致。

## 训练：企业默认不用，个人看设置

| 情形 | 是否可能用于训练 | 资料 |
| --- | --- | --- |
| Business、Enterprise、Edu 工作区 | 默认不用 | [推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}}) |
| 个人套餐 | 由「为所有人改进模型」设置决定；范围可能包括 dot 的操作、委派给其他智能体的工作、自动化，以及为对话提供信息的已连接应用数据；使用前尽可能去标识化 | [隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}}) |
| 主动研究的线程和私人笔记 | 不直接用于训练；被 dot 带入符合条件的对话或任务后，按用户设置可能被用到（官方举了里斯本旅行的例子） | [安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}}) |
| 关闭模型改进后 | 在有限情形（包括安全相关）下仍可能有人工审查 | [隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}}) |

官方 dots 资料没有提到广告用途。Engadget 对 Dots 只写个人套餐的活动「可能会被用于改进其模型」，对 Muse 则指出其改进模型设置默认开启（[Engadget]({{< relref "/docs/industry/sources/media/2026-10-11-engadget-dot-vs-muse" >}})）。

## 记忆与数据：删得掉整体，删不掉单条

dot 的记忆无法逐条查看、删除或修改，断开插件不删除已获得的信息，关闭 ChatGPT 记忆只停止共享（详见[记忆与上下文]({{< relref "/docs/dots/analysis/memory" >}})）。删除或重置 dot 时，归 dot 所有的聊天、子智能体历史、私人研究笔记、云端计算机数据及备份在 30 天内删除，操作不可恢复（[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})）。

不随 dot 一起删除的内容：单独存储的 ChatGPT 对话、Codex 会话线程、Space 文件、项目、已连接的存储、用户电脑上的内容、已进入 ChatGPT 记忆的信息、已经发出的消息（[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}})）。企业文档还自述了两个未决点：删除 Space 文件不会触发删除 dot 聊天中的缓存副本，「尚未确认有单独的自助删除流程」；文件删除后可能仍出现在「产出」列表中，如何清除「仍未确认」。

保留期限：

| 数据 | 保留 | 资料 |
| --- | --- | --- |
| 云端计算机快照（启用数据驻留或 EKM 的工作区） | 五天周期清除，最长不超过七天 | [文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}}) |
| 云端计算机快照（其他工作区，活跃 dot） | 没有最长保留期限，客户目前无法要求提前清除 | 同上 |
| dot 删除后 | 30 天内删除 | 同上 |
| Compliance 日志 | 每个事件保留 30 天 | 同上 |

dots 与带本地访问的 Work 都不提供严格的零数据保留；任务在云端编排，意味着对话、工具结果和任务上下文不会只留在用户的电脑上（[文档：Work Cloud 与本地计算机访问]({{< relref "/docs/dots/sources/official/2026-11-05-docs-cloud-local-access" >}})）。静态数据使用 AES-256 加密，传输使用 TLS 1.2 或更高版本。

导出方面，资料中没有面向用户的 dot 数据导出功能；用户可以通过 OpenAI 隐私门户或 dsar@openai.com 提交访问、更正、删除请求，没有账户也可以提交（[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}})）。管理员可以通过 Compliance API 和 Analytics API 导出数据。

推断：对个人用户来说，dots 的隐私控制颗粒度很粗。能做的是选择连接哪些应用、关闭模型改进、整体删除 dot；看不到 dot 记住了什么，也不能只删一部分。社区有文章认为「能随时收回的权限才产生信任」（[灵络：之后呢]({{< relref "/docs/industry/sources/community/2026-11-04-lingluo-personal-ai-center" >}})），dots 目前的设计在这一点上偏弱。

## 他人的信息

在 Slack 中，dot 默认只回应所有者，回复频道前可以私下询问所有者愿意分享什么；把私人对话中的信息分享给他人前会先确认（[文档：给你的 dot 发消息]({{< relref "/docs/dots/sources/official/2026-11-05-docs-message-your-dot" >}})）。dot 在频道中发的帖子所有能看到该对话的人都能读到，官方以「dot 能读 HR 文档，却在项目频道里发出薪资数字」为例，建议只在成员都属于本组织的频道使用（[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})）。

企业处理隐私请求时，官方要求「把客户信息和非用户的信息都包括进来」：删除一条 Slack 消息，要同时找到引用或总结了它的私人笔记和据此保存的报告。短信渠道中，dot 只与用户本人收发，不会访问用户的其他短信对话。

资料中没有关于被处理信息的第三方（邮件往来对象、群聊成员）是否需要知情或同意的官方说明。

## 地区与监管

个人 Pro 需要 18 岁以上，覆盖 EEA、瑞士、英国之外的符合条件市场；Business Premium 在受支持的 ChatGPT 地区可用；Enterprise、Edu、Healthcare 为测试版，默认关闭（[帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}})）。第三方对比文章称，欧洲用户目前只能选择 Copilot Cowork、Grok Bot 等产品，并认为几家厂商在等待欧盟规则（[六款智能体对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。资料中没有 OpenAI 对欧洲开放时间的说明。

数据驻留的说法不一致。企业安全文档列出多个地区的存储驻留和美国、欧洲的推理驻留，并写明符合条件的工作区支持 EKM（[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})）；同日收集的本地访问文档则写「在企业测试期间，dots 不支持数据驻留或推理驻留」，且 dots 不适用于使用 EKM 的工作区（[文档：Work Cloud 与本地计算机访问]({{< relref "/docs/dots/sources/official/2026-11-05-docs-cloud-local-access" >}})）。两份文档都没有标日期，资料无法判断哪份更新。

## 资料缺口

- 个人套餐「为所有人改进模型」的默认状态，以及 dots 是否沿用这一默认值。
- 用户导出 dot 数据的方式。
- 第三方信息的知情同意，以及第三方如何提出删除请求。
- 语音通话内容的保存、转写和训练用途。
- 欧盟、英国开放的时间表与合规措施。
- 数据驻留两份文档说法不一的澄清。

## 主要资料

- 官方：[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}})（训练、删除、数据请求）；[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})（保留期限、他人信息、驻留）；[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})（主动研究笔记的训练规则）；[文档：Work Cloud 与本地计算机访问]({{< relref "/docs/dots/sources/official/2026-11-05-docs-cloud-local-access" >}})（零数据保留、驻留限制）。
- 媒体：[Engadget]({{< relref "/docs/industry/sources/media/2026-10-11-engadget-dot-vs-muse" >}})（与 Muse 训练默认值的对照）。
- 社区：[六款智能体对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})（地区限制）。
