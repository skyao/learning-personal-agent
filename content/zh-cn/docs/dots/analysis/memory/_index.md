---
title: "OpenAI Dots：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-12
sourcesUntil: 2026-11-11
description: >
  dot 的上下文来自当前任务、ChatGPT 记忆和它自己维护的笔记；它会主动从已连接应用形成记忆，但用户无法逐条查看或删除，断开应用也不清除，只能重置整个 dot。
---

## 概要

- 官方把 dot 的上下文分为三层：当前对话或任务、相关的 ChatGPT 记忆、dot 自己保存的笔记。笔记独立于 ChatGPT 记忆，「不是你所说的一切的完整记录」。
- 个人数据主要通过插件接入（邮件、日历、文件、Slack 等），插件权限与 ChatGPT、Work、Codex 共享。dot 默认会在后台查看已连接的信息并形成记忆，即使用户没有提问。
- 用户目前不能查看、编辑或删除单条 dot 记忆；断开插件只停止新的访问，不删除已获得的信息；唯一的清除办法是删除或重置 dot。
- 同一个 dot 跨设备、跨渠道共享记忆，但各渠道的可见对话分开；把私人信息带到团队频道需要所有者许可。委派出去的任务只拿到 dot 给它的上下文。
- 依托 ChatGPT 是 dots 的记忆优势：实测用户提到 dot 会翻出 ChatGPT 历史里的待办；但国内用户的上下文主要在微信，dots 接不到。

## 三层上下文：任务、ChatGPT 记忆、dot 的笔记

官方文档给出的上下文来源是：当前对话或任务的上下文、相关的 ChatGPT 记忆，以及 dot 自己保存的笔记（偏好、决定、进行中的工作）；这些笔记「独立于 ChatGPT 保存的记忆」，改变 ChatGPT 记忆设置「并不一定会改变你的 dot 已经做的笔记」。检索到的过往 ChatGPT 对话只是「这项工作的上下文」，不等同于持久记忆；语音通话使用挑选后的对话上下文，可能与后台任务获得的不同（[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})）。

帮助中心的说法侧重共享：dot 可以接收 ChatGPT 记忆和近期对话上下文，与 dot 的对话也可能为 ChatGPT 记忆提供内容；在 ChatGPT 中关闭「记忆」会停止这种共享，但不删除 dot 已接收的信息（[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}})）。dot 也「可以创建它自己的记忆，包括来自已连接应用的记忆」（[帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}})）。

2026-10-05 至 10-09 那一周的更新让 dot 可以搜索 ChatGPT 对话，并利用已有 Codex 会话线程和自动化中的上下文（[移动端创建 dot]({{< relref "/docs/dots/sources/official/2026-10-09-docs-whats-new-dots-mobile" >}})）。发布稿称 dot「会随着时间推移从反馈中学习」，「一起工作得越多，就越了解你的偏好」（[推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}})）。

两处官方文档的侧重并不矛盾：dot 从 ChatGPT 记忆起步并可能回写，同时另有一套自己的笔记。但文档没有说明双向同步的规则，例如哪些内容会写回 ChatGPT 记忆。

## 主动从已连接应用形成记忆

帮助中心写明，dot 默认会「在后台主动查看已连接信息，并从中形成记忆，即使你并没有就此提出具体问题」（[帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}})）。这一机制叫主动研究：后台智能体读取被允许的已连接来源，为 dot 保存私人笔记，工具只读（[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})，详见[持续执行]({{< relref "/docs/dots/analysis/continuous-execution" >}})）。

接入的数据以插件为主，官方举例有 Gmail、Google Drive、GitHub、Slack、日历；插件权限在 dots、ChatGPT、ChatGPT Work 和 Codex 之间共享，在 ChatGPT「插件」标签页管理（[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}})）。电脑、应用、消息渠道三类连接互相独立；访问摄像头、麦克风、屏幕要先连接电脑并在系统设置中授权；开通短信不会让 dot 或 OpenAI 读到用户的其他短信。连接机制见[连接器]({{< relref "/docs/dots/analysis/connectors" >}})。资料中没有相册、购物记录等数据的 dot 专属说明。

用户实测：一位国内用户授权 Google 系产品后，dot「自己读取了 ChatGPT 过往对话栏里的任务」，随后主动发来待办和邮箱优惠提醒；作者认为能拿到 ChatGPT 和 Codex 的交互资料是优势，但国内大部分上下文在微信里，难以接入（[靖轩：深度体验 11 天]({{< relref "/docs/industry/sources/community/2026-10-10-jingxuan-dots-11-days" >}})）。Slide Factory 的 dot 则误以为作者用 Gmail，实际是 Zoho 加 Apple Mail 和 Outlook，邮件任务没有完成（[Slide Factory 第一天]({{< relref "/docs/dots/sources/community/2026-10-03-slidefactory-dots-first-day" >}})）。

## 看不到、改不了，只能整体重置

| 操作 | 效果 | 资料 |
| --- | --- | --- |
| 查看、编辑、删除单条 dot 记忆 | 目前不支持，包括从插件进入上下文的细节 | [隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}}) |
| 移动端「自定义 > 记忆」 | 显示的是 ChatGPT 记住的内容，不是 dot 的笔记 | [帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}}) |
| 断开插件 | 停止新的信息共享，已纳入上下文的信息保留 | [安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}}) |
| 关闭 ChatGPT 记忆 | 停止 ChatGPT 与 dot 之间的共享，不删除 dot 已接收的信息 | [隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}}) |
| 重置或删除 dot | 删除 dot 的对话、已保存的记忆和计划任务，不可撤销；不删除 ChatGPT 记忆，也不删除 dot 创建的文件、Codex 会话线程和 ChatGPT 对话 | [帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}})、[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}}) |

官方还说明 dot 的上下文不保留凭证、图片或屏幕截图；委派工作时，其他智能体被指示只保留任务所需的信息。Cyera 的评价是，断开应用后 dot 保留已学到的一切，「只有完全重置才能清除」（[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})）。记忆用于训练的规则见[隐私]({{< relref "/docs/dots/analysis/privacy" >}})。

社区综述把这种设计与 Today 对照：Today 允许用户查看、编辑和删除记忆（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。

推断：dot 会主动从应用中形成记忆，用户却不能逐条审查，这使得「连接哪些应用」成为唯一真正有效的控制点。官方入门文档允许创建时跳过插件、以后再加（[文档：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-docs-getting-started" >}})），Cyera 则明确建议少连应用、用完撤销。

## 跨设备、跨渠道、跨任务

同一个 dot 在 ChatGPT 各端、Slack、Teams、通话、短信之间切换，不会新建 dot，也不重置笔记；但各渠道的可见对话彼此独立，dot 能用某条信息不代表有权向另一批人披露，把私人对话中的信息分享到团队频道需要许可（[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})）。短信中的 dot 与应用内的 dot「共享同样的记忆和插件」（[发布说明：给你的 dot 发短信]({{< relref "/docs/dots/sources/official/2026-10-28-relnotes-texting-your-dot" >}})）。

新任务只获得 dot 给它的指示和上下文，有自己的对话，「不会自动获得你与你的 dot 之间的每一段对话」。发布稿的说法更宽：dots「在每个渠道之间携带上下文」，「都掌握完整的上下文」（[推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}})）；之后的文档说法更具体，以文档为准。

实测反馈不一。Reddit 用户在持续多天的文档审阅中发现「Dot 一直记得自己做到了哪里」，中途插问后能回到原任务（[Reddit：拿棍子戳 Dots]({{< relref "/docs/dots/sources/community/2026-10-01-reddit-poking-dots-with-sticks" >}})）；另有用户（经公众号文章转述 Reddit 帖子）称 10 月 19 日那个周末连续任务没接上，要重新唤起 dot 并解释前情（[十个海外案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})）。国内用户指出 dot 只有一个持续对话、没有分栏，长上下文没有任务分区，不利于管理大项目（[靖轩：深度体验 11 天]({{< relref "/docs/industry/sources/community/2026-10-10-jingxuan-dots-11-days" >}})）。三条都是单个用户的报告。

## 资料缺口

- 笔记的存放位置、容量、保留期限，以及如何整合、压缩和遗忘。
- 是否会提供查看和编辑单条记忆的功能。
- dot 笔记与 ChatGPT 记忆双向同步的具体规则。
- 删除 dot 后笔记多久真正清除。
- 将来有多个 dot 时记忆如何共享。

## 主要资料

- 官方：[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})（三层上下文、跨渠道规则）；[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}})（与 ChatGPT 记忆的关系、不能逐条删除）；[帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}})（主动形成记忆、重置）；[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})（主动研究笔记、断开后的残留）。
- 社区：[靖轩：深度体验 11 天]({{< relref "/docs/industry/sources/community/2026-10-10-jingxuan-dots-11-days" >}})（读取 ChatGPT 历史、国内上下文）；[Reddit：拿棍子戳 Dots]({{< relref "/docs/dots/sources/community/2026-10-01-reddit-poking-dots-with-sticks" >}})（长任务记忆）；[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})（只能重置清除）。
