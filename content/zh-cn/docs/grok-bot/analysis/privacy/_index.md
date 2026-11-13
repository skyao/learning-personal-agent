---
title: "Grok Bot：隐私"
linkTitle: "隐私"
weight: 90
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Grok Bot 的数据政策整体沿用 Cursor：训练与否取决于 Cursor 的隐私模式，删除账号即删除 Cursor 账号，Enterprise 另有保留期、批量删除和美国数据驻留；xAI 自己的页面几乎不单独说明数据用途，同一用户的所有 Bot 共用一台云端计算机，是已发生隐私事件的根源。
---

## 概要

- Grok Bot 没有独立的隐私政策。官方文档把训练、保留和删除都指向 Cursor 的账号设置与条款：退出训练「遵循适用的 Cursor 账户和隐私设置」，后端保留「遵循适用的 Cursor 条款」。截至 2026-11-12 的资料，xAI 侧的文档没有写明数据是否用于训练，也没有写明保存期限。
- 隐私模式是唯一的训练开关。Cursor 文档写明启用 Privacy Mode 时客户数据不用于训练，设置无法验证时默认不训练；旧版隐私模式（Privacy Mode (Legacy)）不允许云端存储，因此会完全阻止 Grok Bot。
- 删除粒度有三层：删除单个 Bot（对话、记忆、例程、附件），删除账号（即删除 Cursor 账号，数据 30 天内清除），以及 Enterprise 管理员的批量删除与计算机保留期。共享计算机上的文件和登录信息不随 Bot 删除，需要用户自己清理。
- 数据边界的主要风险来自架构：同一用户的所有 Bot 共用一台云端计算机。Cybernews 报道的事件中，一个只管财务的 Bot 读到的银行数据，被另一个有 Slack 权限的 Bot 发到了公司频道。
- 面向企业的控制较完整：美国数据驻留、零数据保留（沿用 Cursor 与模型提供商的协议）、推理钩子不在 Cursor 侧留存内容、操作记录只记清理过的元数据。面向个人用户的说明则较少，有社区作者把 xAI 的 Bot 页面列为五家中唯一「完全没有数据说明」的一家。

## 隐私政策整体沿用 Cursor

Grok Bot 用 Cursor 账号登录，数据与隐私设置也随之沿用。xAI 文档的常见问题写明，Grok Bot 使用 Cursor 的身份验证和账号数据设置，「退出训练遵循适用的 Cursor 账号和隐私设置」；模型由系统自动选择，可能是 xAI 的第一方模型，也可能是子处理方名单上的第三方模型（[xAI 文档：常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})）。审批与安全页同样只给出指向：隐私和数据共享通过 Cursor 账户设置管理，合同细节「请查看当前的 Cursor 隐私政策」（[xAI 文档：批准、安全与隐私]({{< relref "/docs/grok-bot/sources/official/2026-10-29-xai-docs-approvals-security-and-privacy" >}})）。

Cursor 侧的企业文档写得更具体：成员在团队中时由团队的隐私模式管辖，启用 Privacy Mode 时客户数据不用于训练，Cursor 在服务器上执行这一规则，「当该设置无法验证时，系统默认不进行训练」（[Cursor 文档：团队]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})）。安全页写明零数据保留沿用 Cursor 与模型提供商的既有协议，提供商不保留提示词和输出，Grok Bot 没有另加控制项；但提供商可能运行滥用和安全分类器，「被标记的数据可能会被存储以供调查」（[Cursor 文档：安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})）。

社区一侧的评价因此分为两种。一位自称有 15 年企业安全经验的作者在 2026-10-28 对照六家厂商页面，写道「xAI 的 Bot 页面完全没有数据说明」，同时注明「未说明」只是指在厂商自己页面上找不到，「并不是说厂商对你的数据做了什么坏事」（[六款智能体对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。这一判断与上面的官方材料并不矛盾：数据说明存在，但放在 Cursor 的文档和条款里，而不在 xAI 的 Bot 页面上。

推断：从文档结构看，Grok Bot 在数据层面实际是 Cursor 的一个产品。对个人用户而言，要弄清自己的数据是否被训练，需要同时理解 Cursor 的两种隐私模式和团队归属，门槛高于 Muse 那样的单一开关。

## 旧版隐私模式完全阻止 Grok Bot

Grok Bot 需要云端存储对话、记忆和计算机磁盘，因此「不支持旧版隐私模式（Legacy Privacy Mode）」（[xAI 文档：常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})）。部署清单把「退出隐私模式（Legacy）」列为前提，写明该模式「会完全阻止 Grok Bot」（[Cursor 文档：部署]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-deployment" >}})）。从 X Chat 使用时，账号或团队处于 Privacy Mode (Legacy) 的用户要先切换到 Privacy Mode，属于团队的由管理员更改（[xAI 文档：聊天与协作]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})）。

更新日志补充了两条行为：当对话不得存储时，Privacy Mode 会使其不进入 Bot 的计算机；选择团队后，Grok Bot 使用该团队的隐私设置（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。共享 Bot 时，如果使用者的隐私模式比所有者更严格，Bot 会为那次对话单独使用一台计算机（[帮助中心：共享 Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-shared-bots" >}})）。

## 删除：Bot、账号与 Enterprise 批量删除

| 操作 | 删除什么 | 不删除什么 | 资料 |
| --- | --- | --- | --- |
| 删除 Bot | 资料、会话、记忆、例程、附件；不可撤销 | 共享计算机上的文件和登录信息不按 Bot 隔离，「请单独清理它们」 | [xAI 文档：Bot]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-bots" >}}) |
| 删除账号 | 即删除 Cursor 账号，自助、永久，数据 30 天内清除；Agent 邮箱的邮件和附件删除，地址停用 | 桌面端只能退出登录；App Store、Google Play 订阅及关联的 SuperGrok、X Premium+ 订阅需另行取消 | [常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})、[帮助中心：Agent 邮箱]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-agent-email" >}}) |
| 删除计算机与数据（Enterprise） | 成员的计算机及持久磁盘，一次最多 1,000 名成员 | Bot 和对话保留 | [Cursor 文档：计算机]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-computers" >}}) |
| 删除全部 Grok Bot 数据（Enterprise） | Bot、对话、记忆、例程和计算机，一次最多 100 名成员 | Cursor 账号保留 | 同上 |

两项 Enterprise 删除都不可撤销，并写入审计日志，成员看不到这些控制项。管理员也可以通过 Admin API 删除成员数据（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。合同层面，Cursor 的数据处理协议规定服务结束后，数据在收到书面指示后 30 天内删除或返还（[Cursor 文档：安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})）。

审批与安全页还给出一份「移除访问」清单：暂停或删除例程、在共享计算机上退出网站登录、卸载连接器并在源服务撤销授权、从 `/workspace` 移除敏感文件、隐藏或删除 Bot（[xAI 文档：批准、安全与隐私]({{< relref "/docs/grok-bot/sources/official/2026-10-29-xai-docs-approvals-security-and-privacy" >}})）。这份清单说明删除 Bot 本身并不能撤回它曾获得的访问。

## 保留期由 Enterprise 管理员设定，删除前不通知

Enterprise 管理员可以设置保留期，自动删除不活动的 Bot、不活动的计算机和旧消息（[Cursor 文档：安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})）。团队文档的摘要列出的区间是 Bot 60 至 365 天、计算机与消息 30 至 365 天（[Cursor 文档：团队]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})）。

计算机保留期（Retention Period for Computers）的规则写得最细：默认关闭，可选 30、60、90、180、365 天或 30 至 365 天自定义；某成员的任何 Bot 在该期间无人发消息时（应用或 Slack 消息计入，例程和 Bot 自行启动的工作不计入），Cursor 在计算机下一次休眠时删除计算机及持久磁盘；「成员的计算机被删除前不会收到任何通知」；成员属于多个 Enterprise 团队时取最短时段（[Cursor 文档：计算机]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-computers" >}})）。

推断：例程不计入活跃度，意味着只靠定时任务运转的 Bot 在保留期到期后会丢失计算机上的文件和登录状态。这对持续执行类用法是一个需要管理员注意的副作用。

## 同一用户的所有 Bot 共用一台计算机

官方写明「你所有的 Bot 都可以访问分配给你账号的同一台云端电脑」（[xAI 文档：常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})）。Bot 之间分开的是角色和记忆，不是文件和登录状态。有社区作者据此提醒，「岗位分开了，数据边界仍要认真设置」（[AI应用与大模型：三家对比]({{< relref "/docs/industry/sources/community/2026-11-01-aiyingyong-grok-muse-dots" >}})）。

据 Cybernews 2026-10-07 报道，XMTP Labs 的 CEO Shane Mac 把一个 Grok Bot 连接到个人银行账户作只读财务助理，另一个 Grok Bot 却以他的身份把银行余额和支出明细发到了公司 Slack 频道。Mac 称管财务的 Bot 没有 Slack 权限，但另一个有，「Turns out, they're all connected」。报道引用官方说明：计算机分配给用户账号而不是单个 Bot（[Cybernews：银行数据泄露到 Slack]({{< relref "/docs/grok-bot/sources/media/2026-10-07-cybernews-bank-data-slack" >}})）。这是一个事件的报道，资料中没有同类事件的统计。

共享给团队的 Bot 则相反：每人与共享 Bot 的对话私密，「所有者和 Manager 无法读取你的聊天」；Bot 从某位队友那里学到的内容，要经所有者或 Manager 在 Review learnings 下批准后才对团队生效（[帮助中心：共享 Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-shared-bots" >}})）。Team Bot 请求使用某人连接的账户时，卡片会说明「该访问仅涵盖你自己的消息」（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

## 联系信息、分享页面与模板

Vault 存放登录信息、银行卡和联系信息，与记忆分开。用户在聊天中给 Bot 姓名、地址、电话或邮箱时，Bot「会在任务完成后将其保存为联系信息」并告知保存了什么，不想保留需要用户明说（[xAI 文档：Vault]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-vault" >}})）。这是默认保存、事后告知的设计。

Bot 生成的网页（Pages）默认仅自己可见，可分享给受邀者、团队或「任何拥有链接的人」；公开页在 `pages.grok.bot` 下，任何人无需登录即可打开，企业版暂不可用（[xAI 文档：文件与结果]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-files-and-results" >}})）。页面所有者删除页面后，对所有共享对象移除（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

模板分享不会公开 Bot 本身，只生成「匿名的私有版本」，内部记忆默认不包含，模板不包含秘密（[模板指南]({{< relref "/docs/grok-bot/sources/official/2026-09-08-guide-templates" >}})）。Enterprise 团队默认关闭模板的公开分享（[Cursor 文档：团队]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})）。

## 推理钩子与操作记录：企业审计不在 Cursor 侧留存内容

推理钩子（Inference Hooks）把每一帧对话发往客户或安全厂商的端点做裁决。每帧包含到当时为止的完整对话、工具结果、共享记忆和规则；用户只以不透明 ID 标识，`email_address` 字段始终为空；Cursor 不加入秘密值，但「输入不会被脱敏」，粘贴进命令的令牌会原样进入帧。Cursor 声明「不保留发往钩子的内容」，收到裁决后丢弃，端点侧如何存储由客户决定；默认的影子模式（只记录不拦截）同样会把成员对话发出，文档建议先告知成员（[Cursor 文档：推理钩子]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-inference-hooks" >}})）。

操作记录（Action Recording）只记录清理过的元数据：Shell 命令清除秘密，浏览器导航去掉查询字符串，计算机使用会话不记录截图和输入文字，其余事件「绝不包含工具参数、文件路径或消息内容」（[Cursor 文档：团队]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})）。

## 地区：计算机在美国，部分地区不开放 @bot

Grok Bot 计算机在美国运行，并受 Cursor 的仅限美国数据驻留计划覆盖，注册后推理、数据处理和存储都留在美国（[Cursor 文档：安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})）。在 X 上 @bot 的功能在澳大利亚、英国、欧盟、冰岛、列支敦士登和挪威不可用，按 X 记录的国家判断（[xAI 文档：在 X 上标记]({{< relref "/docs/grok-bot/sources/official/2026-10-07-xai-docs-tag-on-x" >}})）。文档没有说明排除这些地区的原因。

推断：被排除的地区与 GDPR 及英国、澳大利亚的数据保护法适用范围大体重合，可能与监管有关，但资料没有直接证据。

## 第三方数据

官方对他人信息的处理只有零散的使用规范：人才寻访示例要求 Bot「尊重候选人隐私和每个来源的条款」（[Cursor 文档：用例]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-use-cases" >}})）；在 Slack 共享对话中发送前，Bot 会检查每条帖子对相应人员是否可见（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）；官方教程中的个人 CRM 示例「只使用公开的个人资料信息」（[Grok Bot 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})）。资料中没有关于联系人、通话对象等非用户数据如何保存、能否删除的说明。

社区作者把数据放在厂商云上视为托管式产品的固有代价：「你的数据和记忆都放在厂商的云上，模型也由厂商说了算」，重视隐私的用户可选自部署方案（[程序员鱼皮：大厂为何卷]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})）。

## 资料缺口

- xAI（SpaceXSI）自己是否接触、使用 Grok Bot 数据；Cursor 与 xAI 之间的数据流向和子处理方名单的具体内容。
- 个人用户（非团队）默认是否开启训练；Cursor 隐私政策原文。
- 非 Enterprise 用户的对话、记忆、计算机磁盘保存多久。
- @bot 排除欧盟、英国等地区的原因；欧盟用户能否使用 Grok Bot 应用本身。
- 联系人、邮件往来对象等第三方信息的保存与删除；Agent 邮箱收到的他人邮件如何处理。
- Cybernews 事件后官方是否调整 Bot 之间的隔离。

## 主要资料

官方

- [xAI 文档：常见问题]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})：隐私沿用 Cursor、不支持旧版隐私模式、删除账号。
- [xAI 文档：批准、安全与隐私]({{< relref "/docs/grok-bot/sources/official/2026-10-29-xai-docs-approvals-security-and-privacy" >}})：训练退出与移除访问清单。
- [xAI 文档：Bot]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-bots" >}})：删除 Bot 的范围。
- [xAI 文档：Vault]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-vault" >}})：联系信息默认保存。
- [xAI 文档：文件与结果]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-files-and-results" >}})：Pages 分享范围。
- [xAI 文档：在 X 上标记]({{< relref "/docs/grok-bot/sources/official/2026-10-07-xai-docs-tag-on-x" >}})：不开放的地区。
- [Cursor 文档：安全]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})：零数据保留、DPA 删除、数据驻留。
- [Cursor 文档：团队]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})：隐私模式与训练、操作记录、保留期。
- [Cursor 文档：计算机]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-computers" >}})：批量删除与计算机保留期。
- [Cursor 文档：推理钩子]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-inference-hooks" >}})：帧内容与不留存声明。
- [帮助中心：共享 Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-shared-bots" >}})：对话私密与学习审核。
- [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})：隐私模式行为、Admin API 删除、Slack 可见性检查。
- [模板指南]({{< relref "/docs/grok-bot/sources/official/2026-09-08-guide-templates" >}})：模板包含与不包含的内容。

媒体

- [Cybernews：银行数据泄露到 Slack]({{< relref "/docs/grok-bot/sources/media/2026-10-07-cybernews-bank-data-slack" >}})：共用计算机导致的数据外泄事件。

社区

- [六款智能体对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})：xAI 页面缺少数据说明。
- [AI应用与大模型：三家对比]({{< relref "/docs/industry/sources/community/2026-11-01-aiyingyong-grok-muse-dots" >}})：共用计算机的数据边界。
- [程序员鱼皮：大厂为何卷]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})：托管式产品的数据代价。
