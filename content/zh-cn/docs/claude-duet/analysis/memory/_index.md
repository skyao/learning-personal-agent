---
title: "Claude Duet：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Claude Duet 不另建一套个人数据，而是直接沿用用户 Claude 账号的记忆、技能、连接器和历史对话；多名评测者认为这是它晨报和会议准备做得好的原因，但本地技能、本地 Claude Code 会话带不过来，上下文稀薄时会编造。
---

## 概要

- Duet 的上下文来自用户已有的 Claude 账号：记忆、技能、已连接应用「从第一条消息起就已就位」，还能搜索用户在 Claude 中的历史聊天。官方资料没有描述记忆如何形成、存放和编辑。
- Duet 自己的对话历史和记忆保留到用户删除或重置为止；断开某个应用只停止新的访问，已经了解到的内容保留到重置记忆；删除账号清除全部内容。没有资料说明能否逐条查看或删除记忆。
- 主线程加多个频道，频道共享同一份记忆，每个频道可以有自己的常设指令。
- 评测者的反馈集中在两点：继承来的上下文让晨报、会议准备明显好于同类产品；但「同一个账号」不等于全部上下文，本地技能和本地 Claude Code 会话没有带过来，上下文稀薄时 Duet 会以用户口吻编造内容。
- 凭证不进记忆：官方称 Duet 不能把密码、Cookie、登录令牌保存到记忆中。

## 沿用 Claude 账号的记忆、技能与连接器

发布稿称 Duet 沿用用户 Claude 账号中的记忆、技能和已连接应用，因此设置只需很少工作（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。帮助文档写明这些「从第一条消息起就已就位」；Duet 可以搜索用户过去的聊天，包括 Duet 中的聊天和用户在项目之外的 Claude 聊天，删除的聊天会从搜索中移除；这与 Claude 的「搜索并引用聊天」是同一个设置，可在 设置 > 你的 Claude 中关闭（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。安全文章补充，Claude 从早先对话中记住的细节也可在 Duet 中使用（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。

帮助文档还写明，Duet 给出数字或摘要时会说明出自哪封邮件、哪个文件或哪张电子表格（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。

资料中没有 Duet 记忆的形成机制（何时写入、存在哪里、能否逐条查看和编辑）。这一点与 Muse 形成对照：Muse 的记忆是用户可以查看和编辑的 Markdown 文件（见 [Muse：记忆与上下文]({{< relref "/docs/muse/analysis/memory" >}})）。

## 保留、断开与重置

| 操作 | 结果 | 资料 |
| --- | --- | --- |
| 正常使用 | 保留对话历史及其记忆，在任务之间携带上下文，直到用户删除历史或重置 | [安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}}) |
| 断开某个应用 | 从那一刻起停止新的访问；Duet 已从中了解到的内容保留，直到用户重置其记忆 | [安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}}) |
| 重置记忆 | 在应用设置中随时可做 | [帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}}) |
| 删除账号 | 清除 Duet 存储的所有内容 | [安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}}) |

凭证不进入记忆：官方称 Duet 永远看不到用户的密码、Cookie 和登录令牌，也无法把它们保存到记忆中；网站代码和 Cookie 留在浏览器机器上（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。

LaoZhang AI 的对照表把 Duet 列为「断开应用不删除已了解的内容」一类，并称其训练数据遵循 Claude 账户的训练设置、Anthropic 消费者政策排除原始连接器内容（[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})，据厂商文档整理）。Duet 自己的官方资料没有谈训练；Freistyle AI 的对照表在这一栏写「Duet 页面未说明」（[Freistyle AI：小企业六款对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。

## 主线程与频道共享一份记忆

帮助文档称主线程保持在一处，用户可以为不同主题建立独立频道，频道共享同一份记忆（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。用户描述的用法更进一步：Duet 可以自己创建和管理频道，频道之间能互相看到和引用（[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})）；每个频道保留自己的常设指令，用户可以让一个频道改写自己的指令，去读取其他每个频道并汇报状态，这是用户自己搭的「幕僚长」频道，不是内置功能（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。

## 继承的上下文：最被称道，也有边界

多名评测者把 Duet 的长处归于继承来的 Claude 上下文。Aakash 称，因为 Duet 从他长期使用的 Claude 那里获得了上下文，会议准备和晨报明显优于 Dots、Grok Bot、Muse、Instinct，邮件草稿也更好，第一条消息就给出了他这一周的画像（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。aiagentslibrary 的测试里，点名让 Duet 使用作者的 Website Builder 技能时页面得 10/10，普通请求 8.9/10，作者说明只测了一个技能、一份简报（[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）。

边界也被反复提到：

- Claire Vo 发现 Duet 继承了 Claude 的插件和连接器，能读取她账号里的产物（artifacts），但她的本地技能没有带过来；她怀疑需要先发布为 Claude 插件，没有验证。她的看法是，已有产物、已连接服务和本地技能是不同类型的上下文，「访问同一个账号并不意味着可以访问让原工作流运转的每一种要素」（[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})）。
- Aakash 认为 Duet「还没有把回忆做得很好」，尤其是对本地 Claude Code 会话；上下文稀薄时它以作者口吻编造内容，上下文丰富（有代码仓库）时则改为追问（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。
- ChatPRD 的家庭报纸任务中，Duet 只拿到工作日历，发现缺少相关日历权限后只交出 Markdown 大纲；作者提醒，表面上的智能差异可能只是访问权限的差异（[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。

推断：Duet 的记忆策略是把 Claude 账号当作上下文的来源，自身不另建个人数据档案。好处是老用户零设置就有上下文，代价是它的上限取决于用户在 Claude 里积累了多少、放在哪里；放在本机（本地技能、Claude Code 会话、本地文件）的部分目前够不到。这与它看不到本机文件的运行环境一致（见[运行环境]({{< relref "/docs/claude-duet/analysis/runtime" >}})）。

## 资料缺口

- Duet 记忆的形成方式、存放形态，用户能否逐条查看、编辑、删除。
- Duet 记忆与 Claude 主应用记忆的关系：Duet 中形成的记忆是否回写到 Claude 账号。
- 本地技能、Claude Code 会话能否、如何进入 Duet。
- Duet 数据是否用于训练的官方说明（隐私资料不足，未单独成页，见[产品总览]({{< relref "/docs/claude-duet/analysis" >}})的主题分析表）。

## 主要资料

- 官方：[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})（沿用记忆、技能、连接器）、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})（搜索历史聊天、频道共享记忆、断开与重置）、[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})（保留与删除、凭证不进记忆）
- 社区：[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})（上下文带来的优势、编造、频道指令）、[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})（本地技能未继承）、[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})（频道管理）、[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})（技能测试）、[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})（权限差异）、[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})、[Freistyle AI：小企业六款对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})（训练条款）
