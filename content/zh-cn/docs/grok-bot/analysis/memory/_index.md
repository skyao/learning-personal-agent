---
title: "Grok Bot：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Grok Bot 的记忆按 Bot 隔离，只有姓名、时区等少数事实全账号共享；记忆由 Bot 自行决定保存，个人 Bot 没有记忆管理界面，查看、纠正、删除都靠聊天；Team Bot 为每个用户分别保存记忆，面向全队的「学到的内容」须经管理者批准才共享。
---

## 概要

- 记忆的基本单位是单个 Bot，而不是账户：每个 Bot 有自己的记忆和例程，工具和技能在账户层级共享。官方的说法是「能力可以广泛共享，而上下文留在需要它的角色那里」。姓名、时区等少数关于用户的事实例外，由所有 Bot 共享。
- 记忆由 Bot 自行决定保存，「不会先询问」。个人 Bot 没有记忆界面，查看、纠正、删除都要在聊天中提出。可以从其他 AI 助手导入记忆（10-26 的 v0.77.0 加入）。
- 记忆之外，Bot 之间还通过共用的云端电脑传递上下文：同一账户的所有 Bot 共用一台电脑，文件、浏览器会话和登录信息互通。删除 Bot 会清掉它的记忆，但电脑上的文件和登录可能保留。
- 团队场景分两层。Team Bot 为每个用户分别保存上下文和私人笔记；面向全队的「学到的内容」要经所有者或 Manager 批准才共享。Enterprise 可以设定数据保留期限，期满自动删除 Bot 及其记忆。
- 官方反复提醒：记忆「不能替代权威来源」，重要决策要让 Bot 重新查当前数据，安全边界要靠审批而不是记忆。

## 每个 Bot 一份记忆，少数事实全账号共享

官方设计文章把 Grok Bot 的「能力」和「上下文」分开。工具和技能放在账户层级，因为许多 Bot 都要浏览网页、处理文档；记忆和例程属于 Bot，因为它们反映「该特定角色随时间知道什么、做什么」。文章举例说，法务 Bot 需要争议历史，财务 Bot 需要多年财务记录，把这些合并成一个大记忆，会让每个 Bot 更难拿到与自己工作相关的信息（[设计文章]({{< relref "/docs/grok-bot/sources/official/2026-09-03-designing-grok-bot" >}})）。

帮助文档写明了具体范围（[帮助文档：Bot]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-bots" >}})）：

- Bot 在一个聊天中保存的内容，在与它的所有聊天中都可用。
- 每个 Bot 有自己的记忆。但「少数关于你的事实（比如你的姓名和时区）由你所有的 Bot 共享」，一个 Bot 得知后，其他 Bot 也会知道。
- 语音聊天可以用到此前的通话和近期聊天。更新日志 v0.75.2 也写了这一条（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。
- 群聊中，Bot 可能用到用户在私聊里说过的内容。每个 Bot 保留自己的记忆，不与群内其他 Bot 共享，但「群里的每个人都能读到你的 Bot 说的话」。

记忆之外还有别的上下文通道。FAQ 写明，同一账号的每个 Bot 都使用同一台持久化云端电脑，共享文件、浏览器会话和登录信息；「共享文件、浏览器会话、群组消息和直接交接也可以在它们之间传递上下文」。FAQ 同时提醒，电脑按用户分配，不要把单独的 Bot 当作安全边界（[FAQ]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})）。也就是说，记忆按 Bot 隔离，并不等于数据按 Bot 隔离。

模板（Template）会打包 Bot 的指令、记忆、技能和插件，但「默认情况下」排除个人的或只适用于创建者的记忆（[模板指南]({{< relref "/docs/grok-bot/sources/official/2026-09-08-guide-templates" >}})）。复制（Duplicate）一个 Bot 会带走配置、技能、例程和头像，「但不带对话历史、学到的记忆或附件」（[工作指南]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})）。

推断：这种按角色分记忆的设计，和 Grok Bot「一个 Bot 一份工作」的产品形态一致。有用户实测印证了这种用法：Pat Simmons 为 YouTube 频道分设脚本、缩略图、调研 Bot，称「一个只写脚本的 bot 会保留我所有的脚本反馈」，不会被其他内容堆满（[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。

## Bot 自行决定记什么，没有记忆界面

帮助文档写明（[帮助文档：Bot]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-bots" >}})）：

- 「Bot 自行决定什么值得保留。它不会先询问」，通常会在回复中提到一次保存，但并非每次都显示。保存的内容包括偏好、规则、关于用户的事实和工作记录。登录信息、卡和联系信息属于 Vault，不进记忆。
- 要确保保留某件事，就直接让它记住，例如「记住我每周五都不在」。工作指南建议，长期规则（如审批边界）在第一条消息里交代并让 Bot 记住，具体任务用普通消息下达（[工作指南]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})）。
- 「个人 Bot 没有记忆界面」。查看、纠正、移除都在聊天里提出，例如问「你记得关于我的什么」。共享事实有误时，可以告诉任意一个 Bot；要彻底删除一项共享事实，得让保存它的那个 Bot 来做。
- 可以从其他 AI 助手导入记忆：在设置的「导入」里，把提示词复制到另一个助手，粘回它的回答，选「添加到记忆」，内容会发给主 Bot。更新日志记为 v0.77.0（2026-10-26）加入（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

重置和删除的效果，帮助文档列了一张表：重置会话不清记忆；删除 Bot 会抹除它的资料、会话、记忆、例程和附件，「包括它为你的其他 Bot 保存的共享事实」，且无法撤销；但「共享计算机上的文件和登录信息不按 Bot 隔离，可能仍留在那里」，需要单独清理（[帮助文档：Bot]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-bots" >}})）。更新日志另写明，个人 Bot 保存的记忆「只有你可以更改」，删除 Bot 还会移除它的 Slack 应用（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。一篇四产品费用对比把「删除 Bot 会把共享文件和登录留在电脑上」列为 Grok Bot 的特点；该文作者说明自己没有做同任务实测，依据的是厂商文档（[四产品费用对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})）。

资料库（Library）列出 Bot 制作的页面、文件和应用，用户自己上传的内容和 Cloud Agent 返回的文件不列出（[帮助文档：文件与结果]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-files-and-results" >}})）。v0.79.2 起，让 Bot 保存到资料库的文件放进「Bot 的文件」，「所有能使用该 Bot 的人都可以看到」（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

对比：一位同时用过 Muse、Dots、Grok Bot 的用户认为，Muse 的「人格文件和记忆都是开放的，你可以修改」，在这方面强于 Grok Bot 和 Dots（[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。

## 记忆存在虚拟机文件里，长对话靠压缩

以下技术细节不是官方资料。Peter Piekarczyk 在个人博客中整理了 Cursor 的 Lee Robinson 关于 Grok Bot 实现的演讲，演讲没讲到的部分由作者凭经验补充，文中已标出。下列说法应视为「据该文转述」（[Peter Piekarczyk：消息处理流程]({{< relref "/docs/grok-bot/sources/community/2026-10-14-peterp-what-happens-when-you-message" >}})）：

- 对话历史单独存放在数据库中。技能是存在虚拟机上的 markdown 文件，备份到对象存储；「你的记忆也以同样的方式工作，智能体使用 grep 来搜索它」。
- 上下文管理有几种做法：保持提示词前缀稳定以命中缓存；技能延迟加载，提示词里只放名称和简短描述；重活交给辅助工作流，主上下文保持精简；压缩（compaction）。
- 压缩有两种触发。一是上下文超过 100K token、用户离开约 10 到 60 分钟时在后台压缩。二是接近窗口上限时强制压缩并阻塞主线程，该文称 Grok Bot 的窗口「大约是 200K token」。

用户可见的历史在压缩后是否保留，资料没有说明。

## 团队中的记忆：个人笔记与需批准的共享知识

Team Bot（2026-09-28 以公开 beta 面向 Teams 和 Enterprise 推出）由上下文、插件、凭证、记忆四部分构成。官方称 Bot 共享给团队，但「Bot 为每个用户保留独立的上下文和记忆」，同时使用团队共享的技能（[Team Bots 发布]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}})）。更新日志写明，Team Bot 会在应用、Slack 和例程中为每个人保留私人笔记（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

共享 Bot 可以「为整个团队学习内容」，但从某位队友那里学到的东西，「要等所有者或 Manager 在 Review learnings 下批准」。关于用户个人的内容不会存给团队，与某人合作中记住的东西只留在此人和 Bot 之间（[帮助：共享 Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-shared-bots" >}})）。官方的 Data Bot 案例给了例子：Bot 记下某条管道归谁负责，或某次指标下跌其实是区域假日，这些新增记忆由 Manager 审核，批准后才与所有使用者共享（[Data Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-02-data-bot" >}})）。

Enterprise 的数据保留设置（[团队部署指南]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})）：

| 设置 | 删除对象 | 期限 |
| --- | --- | --- |
| Bot 保留期 | 期限内无人发消息的 Bot，连同对话、记忆、技能、例程；删除前 30 天邮件通知所有者 | 60 至 365 天 |
| 计算机保留期 | 成员所有 Bot 都无人发消息后，该成员的计算机及文件 | 30 至 365 天 |
| 消息保留期 | 超期的 Bot 消息和附件，每天执行，「不会通知任何人」 | 30 至 365 天 |

同一指南提到，Enterprise 的 Analytics 中 Conversation Insights 有 Grok Bot 来源，按工作类型（Type of Work）和自动化程度（Level of Automation）对 Bot 对话分组。

推断：个人 Bot 的记忆完全由 Bot 自管、没有界面，团队共享的知识却要人工审批，两者的管控力度差别明显。从官方说法看，团队层面多出来的这道审批，针对的是「一个人教给 Bot 的东西扩散给全队」这种风险。

## 记忆不是事实来源

官方在多处给出同一条告诫：「记忆不能替代权威来源」。变化中的事实应保存在源系统，重要决策让 Bot 引用或重新打开当前数据，过时的假设直接纠正，安全边界用审批和自动审核（Auto-review）规则来守，而不是靠记忆（[帮助文档：Bot]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-bots" >}})、[FAQ]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})）。

重度用户的做法与此一致。Granda 让 Notion 充当「记录来源」，聊天里只传工单链接，不传长文（[Granda：BotOps]({{< relref "/docs/grok-bot/sources/community/2026-09-06-granda-botops" >}})）。另有用户的做法是给每个 Bot 写明职责、持续喂领域信息，让 Bot「积累记忆」；Bot 出问题时，由市场里的 doc bot 查看来往记录，再去改描述或记忆（[特工宇宙：投资人日常]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})）。

记忆功能本身也有过问题：v0.78.1（2026-10-27）修复了「同时对同一记忆进行两次保存」会互相覆盖的问题（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

## 资料缺口

- 记忆的存放位置、保存期限，以及是否用于训练，都缺官方说明。帮助文档只写「后端保留遵循适用的 Cursor 条款」；存储细节只有 Peter Piekarczyk 的二手整理。
- 没有关于压缩的官方说明，也没有压缩后记忆质量的实测。窗口大小（约 200K token）只有单一来源。
- 删除 Bot 或删除账户后，后端何时真正删除记忆；「要求 Bot 忘记」是否真正删除，缺独立核实。
- 群聊中私聊内容被带入的边界，以及多人群聊中的泄露风险，缺实测。
- 记忆导入功能的实测，以及导入内容如何进入主 Bot、能否分发给其他 Bot，资料中没有。

## 主要资料

- 官方：[帮助文档：Bot]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-bots" >}})（记忆范围、保存规则、删除表、导入）；[设计文章]({{< relref "/docs/grok-bot/sources/official/2026-09-03-designing-grok-bot" >}})（能力与上下文分界）；[FAQ]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})（共用电脑、上下文传递）；[工作指南]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-work" >}})（长期规则、复制 Bot）；[模板指南]({{< relref "/docs/grok-bot/sources/official/2026-09-08-guide-templates" >}})（模板排除个人记忆）；[帮助文档：文件与结果]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-files-and-results" >}})（资料库）；[Team Bots 发布]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}})、[帮助：共享 Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-shared-bots" >}})、[Data Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-02-data-bot" >}})（团队记忆与审批）；[团队部署指南]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})（数据保留）；[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})（导入、并发保存修复、私人笔记）。
- 社区：[Peter Piekarczyk：消息处理流程]({{< relref "/docs/grok-bot/sources/community/2026-10-14-peterp-what-happens-when-you-message" >}})（存储与压缩，转述演讲）；[Granda：BotOps]({{< relref "/docs/grok-bot/sources/community/2026-09-06-granda-botops" >}})（Notion 作记录来源）；[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})（按角色分 Bot 的效果、与 Muse 对比）；[特工宇宙：投资人日常]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})（积累记忆的用法）；[四产品费用对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})（删除后的残留）。
