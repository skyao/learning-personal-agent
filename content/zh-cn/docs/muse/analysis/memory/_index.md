---
title: "Meta Muse：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  Muse 的记忆是用户虚拟机里可读可改的 Markdown 文件，由每小时、每晚的后台任务维护，接入的个人数据在跟踪产品中最宽；遗忘只是「尽力而为」，11 月又暴露出记忆可被篡改、疑似串号的问题。
---

## 概要

- **记忆是文件。** 官方称记忆文件（Memory.md、Soul.md、Identity.md）可以直接查看、编辑、下载。多份独立导出和本库自己的实测显示，Markdown 文件是源头，Postgres 只做索引，存放文本切块、向量和带证据的「说法」。在跟踪产品中，Muse 的记忆机制公开得最透明。
- **记忆主要由后台任务形成。** 每小时有一个任务把新说法与原始消息核对，每晚有一次「做梦」回顾对话。另有每小时为用户身边每个人维护页面的 Relationships 任务，被维护的人包括不用 Muse 的人。这个任务经 WIRED（2026-10-03）、TIME（10-06）报道后，一直是记忆争议的焦点。截至 11 月下旬，监管机构的提醒里仍提到这一点。
- **接入的个人数据最宽。** 同一账户中心下的 Facebook、Instagram、Threads 自动连接。此外可以接 Gmail、日历、银行，手机通讯录、通话记录、健康数据，以及 Mac 本地应用，还能导入其他 AI 助手的记忆。Mac Messages 同步（9 月）和经安卓通知读到 Signal 消息（11 月）两起事件说明，进入记忆的数据不只来自连接器。
- **遗忘的边界，官方文档自己写明了。** 删除内容后 Muse「可能仍然记得」；「遗忘」技能「尽其所能」删除；断开连接器不会清除已取得的信息；记忆没有关闭开关。完全清除只有两条路：重置 Muse，或删除 Meta 账户。泄露的指令要求遗忘流程不告诉用户原始消息可能仍然可见。
- **11 月出现两个新问题。** 一是完整性：NebuSec 演示经浏览器漏洞外传并篡改记忆与对话历史，称漏洞已修复。二是疑似串号：路透报道员工称 Muse 说出了「不属于自己的」对话和银行余额，Meta 称是幻觉。模型层面的改进（MemoryBench 85.6、遗忘关键信息减少 2.4 倍）都是 Meta 自报。

## 记忆存放在虚拟机里的 Markdown 文件中，数据库只做索引

官方说法：记忆在各次对话之间持续保留，记忆文件「你可以直接阅读和编辑」（[设计说明]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})）。帮助文档的存储清单列出了互动、目标、Artifacts、提醒，以及 Memory.md（记忆）、Soul.md（核心信条与个性）、Identity.md（身份），后三者可在「助手图标 > 身份」下直接编辑或清空（[帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）。安全文章称，用户可以检查、编辑、下载虚拟机里的所有文件，「包括 Muse 关于你的记忆」，虚拟机数据持续备份（[我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。

独立资料与官方说法一致，并补充了实现细节：

| 资料 | 时间 | 看到的结构 |
| --- | --- | --- |
| [Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})（用户导出整个文件系统，[The Verge：下载整个文件系统]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}}) 报道） | 2026-09-22 | `~/MEMORY.md` 是简短的事实、偏好、承诺清单；`~/memory/` 下是按日期的日志；`memory/bank/` 按境况、经历、偏好整理，带源文本行引用；Postgres 的 `memory.entries` 存文本块，`memory.embeddings` 存 384 维向量，`memory.claims` 记录证据、置信度和状态，新说法可经 `supersedes_claim_id` 取代旧说法 |
| [Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})（个人博客，2026 年 9 月） | 9 月 | 同样是 Markdown 加 Postgres 索引，混合检索加重排；嵌入用盒内 MiniLM，片段不离开加密卷；有后台压缩（compaction）和重启检查点；备份走 btrfs 快照 |
| [Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})（第三方逐条核验报告，页面自注由 AI 生成） | 9 月下旬 | 另有 `USER.md`、人物页 `~/memory/people/`、群组页 `~/memory/groups/`、购物档案 `~/memory/shopping/PROFILE.md`；示例行存了门禁码、卡号后四位、过敏信息 |
| [我的实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})（用户实测） | 2026-10-12 | Muse 自述「文件是源头，postgres 是索引」；`memory.entries` 136 行，`memory.claims` 44 行，只从每日流水抽取，不索引 MEMORY.md；数据库有 194 张表、18 个 schema。实测让它「叫我 Sky」后，虚拟机重建、上下文压缩之后它仍这样称呼 |

CodePick 根据 Muse 自报的元数据提醒：存储、可搜索、被加载是不同的状态，不能假定每轮都把全部记忆文件注入上下文（[CodePick：Muse 架构详解]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})）。Personal Agent Bench 的拆解没有终端，未能验证用户能否直接打开这些文件（[Muse 拆解实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-teardown-personalagentbench" >}})）。

推断：结构上，Muse 把「可读的源头」和「检索用的索引」分开了。用户能看到、能改的是 Markdown；检索和去重由数据库完成。这能解释后面遗忘时遇到的问题：改了文件，索引、对话原文和备份里的副本不一定跟着变。

## 记忆的形成：对话中写入，加上每小时、每晚的后台任务

- **对话中写入、上传文件、连接器取得的上下文。** 帮助文档列出记忆有四个来源：用户直接分享的信息、从互动中观察到的偏好、已连接服务的上下文、基于文件的记忆系统（[帮助：个性与记忆]({{< relref "/docs/muse/sources/official/2026-09-30-help-personality-memories" >}})）。文件会被记住，可以说「update my budget spreadsheet」而不必重传（[帮助：Artifacts]({{< relref "/docs/muse/sources/official/2026-09-08-help-artifacts" >}})）。
- **每小时核对。** 后台任务把新说法与原始消息核对，记录引文、消息 ID、说法 ID，再决定进入精选清单还是留在每日日志（[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})）。千问负责人对 InfoQ 介绍竞品时，也称 Muse「强调溯源」，每小时把新记忆与原始对话核对（[InfoQ：千问谈下限与上限]({{< relref "/docs/industry/sources/media/2026-11-08-infoq-qwen-personal-agent" >}})）。
- **每晚「做梦」。** 每晚回顾近期对话，在 `~/dreams/` 写下给以后会话的指导，文字本身不注入提示（[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})）。Future Society 报告另记了每天一次的「Studying」任务，会建议用户「暗示过但从未明说」的目标（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。TIME 查阅的指令也要求推断用户「没有说出口的」目标（[Medianama：人物档案（二手）]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})，Medianama 转述 TIME）。
- **规模示例。** 有作者的重度部署积累了 18 份每日日志、263 个人物画像、21 个群组画像（[2000 万条已删聊天]({{< relref "/docs/muse/sources/community/2026-10-24-muse-subpoena-agent-memory" >}})），这是个例，不代表一般用户。

## 为用户身边的每个人建页

据 WIRED 2026-10-03 报道，研究员 Karan Joshi 提取的内部指令要求 Muse「为用户生活中的每一个人建立一个页面」。任务每小时运行，覆盖家人、伴侣、朋友、同事和「关注」的人；页面分事实、历史、关系、共同点、未了之事等部分；指令要求只用已掌握的证据（[WIRED：亲友人物档案]({{< relref "/docs/muse/sources/media/2026-10-03-wired-muse-profiles-friends-family" >}})）。TIME 的报道（经 [Medianama：人物档案（二手）]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}}) 转述）补充：档案延伸到不使用 Muse 的人；指令还要求记录哪种互动方式对用户有效；不同虚拟机上的 Muse 通过去标识化的「shared lessons」互相学习。Meta 回应称数据不与广告系统共享，经验用于改进整体产品。

Future Society 的报告从导出的虚拟机里取得了这一任务的提示词，并指出了两处具体问题。第一，提示词设了门槛，陌生人、公众人物、只出现在搜索结果里的人不建页。第二，目标创建技能写有「不要推断他人的敏感特征」，Relationships 任务的提示词里却没有这条规则（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。Meta 称这些页面只在「明确相关」时才参考；有作者指出，这是指令层面的政策，不是技术屏障（[非用户消息隐私]({{< relref "/docs/muse/sources/community/2026-11-04-muse-non-user-messages" >}})）。被写进页面的第三方没有登录、导出或删除的途径（[删对话不等于删记忆]({{< relref "/docs/muse/sources/community/2026-10-10-muse-memory-what-it-keeps" >}})）。

这个问题到 11 月仍未了结：Walsh 引用 WIRED、TIME 再次讨论非用户隐私（[Walsh 非用户隐私]({{< relref "/docs/muse/sources/community/2026-11-13-walsh-muse-non-user-privacy" >}})）；马恩岛信息专员 11-27 提醒，Muse 可能处理「从未使用过或同意过它的人」的信息（[信息专员谈代理式 AI]({{< relref "/docs/muse/sources/community/2026-11-27-isle-of-man-commissioner-agentic-ai" >}})）。资料中没有 Meta 改动这一任务的记录。

## 接入的个人数据：Meta 账户自动连接，再加外部账户与设备

| 来源 | 接入方式与说明 | 资料 |
| --- | --- | --- |
| Facebook、Instagram、Threads | 在同一账户中心时自动连接；Muse「只能看到你能看到的东西」 | [英国上线与控制权]({{< relref "/docs/muse/sources/official/2026-11-24-muse-you-stay-in-control" >}}) |
| Instagram 收藏与推荐兴趣 | 可整理收藏的帖子、Reels；技能能读到推荐系统给用户分配的兴趣话题，被告知呈现时不区分推断与明示，还能写回「感兴趣」 | [Muse 进 Instagram 私信]({{< relref "/docs/muse/sources/media/2026-11-24-techcrunch-muse-instagram-dms" >}})、[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}}) |
| 邮件、日历 | Gmail、Outlook 等，官方称只交换完成任务所需的数据，不下载整个收件箱；邮箱连接器过滤验证码和登录链接 | [帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})、[我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}}) |
| 手机数据 | 数据库有通讯录、通话记录、日历、照片位置等表；健康数据经 Apple Health、Health Connect 接入，Meta 没有公布可读的数据类型清单 | [我的实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})、[健康数据连接细则]({{< relref "/docs/muse/sources/community/2026-11-15-health-data-permission-chain" >}}) |
| Mac 本地数据 | Inc. 专栏作家 Aten 称 Muse 把他的 Messages 数据库同步到第 187,462 行；Meta 称需用户主动启用，未解释开关如何被打开 | [iMessage 事件详解]({{< relref "/docs/muse/sources/community/2026-10-01-did-muse-read-your-messages" >}})、[苹果重写 Mac 权限提示]({{< relref "/docs/muse/sources/community/2026-11-19-apple-rewrote-mac-permission-screen" >}}) |
| 消息通知 | 据路透社（经 ThePrint 转述），安卓上经通知权限读到 Signal 消息，员工称默认已配置通知访问 | [Signal 消息与通知权限]({{< relref "/docs/muse/sources/community/2026-11-19-muse-signal-notification-permission" >}}) |
| 其他 AI 助手 | 「设置 > 数据控制 > 导入记忆」可上传导出的 .zip；迁移提示词让旧助手生成「便携式记忆快照」，跳过健康、财务、心理健康和「任何短暂或敏感的内容」 | [帮助：个性与记忆]({{< relref "/docs/muse/sources/official/2026-09-30-help-personality-memories" >}})、[雷峰网：Muse 与 OpenClaw]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}}) |

CDT 的 Miranda Bogen 对 WIRED 说，Muse「积极地诱导用户把自己的整个生活都接进来」（[WIRED：亲友人物档案]({{< relref "/docs/muse/sources/media/2026-10-03-wired-muse-profiles-friends-family" >}})）。CSA 的札记指出，通知、无障碍这类信道不经 Sentinel 审查，Muse 的数据入口不止连接器（[Sentinel 绕过的教训]({{< relref "/docs/muse/sources/community/2026-11-21-csa-sentinel-bypass-lessons" >}})）。

推断：Meta 账户自动连接，加上推荐系统的兴趣数据，是 Muse 与其他跟踪产品最大的区别。用户没有逐项授权，这部分上下文就已经在了。

## 上下文的组织：主对话、侧边对话、Spaces 与多个入口

- **主对话与侧边对话。** 设计说明称，侧边对话是应早期测试者希望按话题分开上下文而加的，Muse 在主聊天和各侧边对话之间保持知情（[我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})）。Instagram 私信里与 Muse 的对话，会作为侧聊出现在主应用中（[Muse 进 Instagram 私信]({{< relref "/docs/muse/sources/media/2026-11-24-techcrunch-muse-instagram-dms" >}})）。
- **Goals、Spaces。** 长期目标放在 Goals 页，每个目标带一行状态（[AgentConnect：路由与权限]({{< relref "/docs/industry/sources/community/2026-11-23-agentconnect-always-on-routing" >}})）。Spaces 是后台持续更新的自定义页面，例如读学校邮件和日历的学校看板；目前只限个人，不能分享、导出（[Spaces：从对话到居所]({{< relref "/docs/muse/sources/community/2026-11-14-spaces-describe-once-keep-it" >}})）。
- **入口之间不一定共享。** 眼镜端切换到 Muse 后，已连接的服务不从 Meta AI 继承，「两者互不共享任何东西」（[眼镜端 Muse beta 解析]({{< relref "/docs/muse/sources/community/2026-11-09-muse-on-glasses-beta" >}})，作者据帮助文档，未实测硬件）。

## 查看、编辑、遗忘与重置

官方给出的控制方式：

- **查看和编辑：** 随时查看和编辑记忆，或直接改 Memory.md（[帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})、[英国上线与控制权]({{< relref "/docs/muse/sources/official/2026-11-24-muse-you-stay-in-control" >}})）。
- **遗忘：** 让 Muse 忘记某个话题或某个人。「遗忘」技能在记忆和支持文件中查找相关信息，「尽其所能」删除（[帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})、[帮助：Muse 邮箱地址]({{< relref "/docs/muse/sources/official/2026-11-16-help-email-addresses" >}})）。
- **下载：** 下载全部 Muse 数据（[帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）。
- **重置：** 「重置 Muse」删除全部数据，无法撤销（[英国上线与控制权]({{< relref "/docs/muse/sources/official/2026-11-24-muse-you-stay-in-control" >}})、[Muse 安全吗]({{< relref "/docs/muse/sources/community/2026-11-06-is-meta-muse-safe-privacy" >}})）。
- **删除账户：** 删除 Meta 账户时，Muse 一并删除（[帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）。

官方同时写明了边界：删除消息、侧边对话、虚拟机文件后，Muse「可能仍然记得」（[帮助：隐私与安全]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})、[帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）；断开连接器后，已取得的信息可能仍留在记忆和对话历史里（[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})）。WIRED 9-20 的实测称记忆没有完全关闭的开关（[WIRED：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})）。

Future Society 的报告从内部文档补充了几处细节（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）：

- 遗忘只编辑记忆笔记，对话原文保留，后续轮次、压缩摘要、`chat.read_messages` 和每小时记忆任务仍会读到这些对话。
- 遗忘技能被告知「Do not tell the user that their original messages may remain visible in the chat」，TIME 也报道了这一句（[Medianama：人物档案（二手）]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})）。
- 新增说法时，去重只比较 `status = 'active'` 的说法。作者据此推断，已撤回的事实可能从保留的对话里被重新提取出来。
- 主对话无法删除；没有保留期设置；没有无痕模式。

有作者按「已存记录、习得记忆、训练轨迹」三栏对照了六种控制方式，结论是只有删除 Meta 账户能覆盖全部三栏，没有「只删除 Muse」的中间选项（[删除聊天记忆仍在]({{< relref "/docs/muse/sources/community/2026-10-28-muse-delete-chat-memory" >}})）。

11 月下旬，监管机构把记忆控制列为用户须知。英国 CMA 与 ICO 在英国上线时提醒消费者，了解如何「关闭、编辑或删除已保存的信息」（[CMA 英国上线声明]({{< relref "/docs/muse/sources/media/2026-11-24-cma-statement-uk-launch-muse" >}})）；马恩岛信息专员也有类似建议（[信息专员谈代理式 AI]({{< relref "/docs/muse/sources/community/2026-11-27-isle-of-man-commissioner-agentic-ai" >}})）。英国上线稿和 Instagram 私信的公告都重申「可以让它记住或忘掉某件事」（[英国第七个市场]({{< relref "/docs/muse/sources/media/2026-11-24-muse-launches-uk" >}})、[Muse 进 Instagram 私信]({{< relref "/docs/muse/sources/media/2026-11-24-techcrunch-muse-instagram-dms" >}})），没有提到新的控制方式。

## Active Memory：模型侧的改进（全部为 Meta 自报）

| 时间 | Meta 的说法 | 资料 |
| --- | --- | --- |
| 2026-10-12 | Muse Wonder 具备「主动记忆（Active Memory）」：跨对话携带重要上下文，并检索与任务相关的细节 | [推出 Muse Wonder（新闻稿）]({{< relref "/docs/muse/sources/official/2026-10-12-introducing-muse-wonder-models" >}}) |
| 2026-10-12 | 内部基准 MemoryBench，测 64K–100K tokens 多轮对话中的回忆，含干扰和中途变化的事实：Wonder 85.6，Opus 5.5 81.5，GPT-6 Astra 81.4，Fable 5.1 79.0 | [Muse Wonder 模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}}) |
| 2026-11-06 | 特化模型经训练区分临时与永久信息、判断信息是否过时；Muse 中遗忘关键信息减少 2.4 倍；正确使用关键上下文的比例从上一代的 76% 升到 90% | [特化模型：Muse 与 Meta AI]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}}) |

Muse Explained 引 datastudios 的算法指出，错误率从 24% 降到 10%，正好是 2.4 倍，两个数字可能是同一次测量的两种说法；Meta 的帖子没有说明 Active Memory 对数据留存意味着什么（[Wonder 训练模型上线]({{< relref "/docs/muse/sources/community/2026-11-09-museexplained-wonder-trained-models-live" >}})）。有作者按 API 价格估算，全量塞入记忆的成本过高，推断 Active Memory 必然是选择性检索（[Wonder 与主动记忆]({{< relref "/docs/muse/sources/community/2026-10-20-muse-wonder-active-memory" >}})，作者推断）。资料中没有第三方复测。

## 11 月的新问题：记忆可被篡改，疑似串号

- **完整性。** NebuSec 11-20 演示：恶意网页经 Muse 内置的 Chromium 取得代码执行后，可以外传对话历史和存储的记忆，还能修改记忆、向对话历史注入条目。研究称漏洞已在发布前报告并修复（[黑进 Muse 窃取对话]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-hacking-muse-browser-use" >}})、[Muse 内部架构剖析]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-inside-meta-muse" >}})）。早在 9 月就有研究者指出，技能更新可以改写记忆文件，借此伪造「用户」权限（[两种入侵路径]({{< relref "/docs/muse/sources/community/2026-09-25-optimus-muse-two-ways-in" >}})）。
- **疑似跨账号泄露。** 据路透报道，有员工称 Muse 提到了「不属于自己的」对话，还在没被问到时报出了他的银行余额。Meta 内部称是幻觉，路透无法确认是编造还是他人的真实数据（[路透：Muse 安全事故]({{< relref "/docs/muse/sources/media/2026-11-18-muse-early-safety-mishaps-surface" >}})，余额数字见 [Signal 消息与通知权限]({{< relref "/docs/muse/sources/community/2026-11-19-muse-signal-notification-permission" >}})）。

推断：记忆以纯文本存放、用户可以改，这让它透明，也让它成了攻击面。被注入的记忆会在以后的每次会话里生效。资料中没有 Meta 对记忆完整性校验的说明。

## 用户实测：连续性是公认的长处，检索有盲区

- **长处。** 有用户用了两个月，Muse 记住了只说过一次的执照到期日，并提前两个月提醒；他最看重的是连续性（[两个月 Muse 使用记录]({{< relref "/docs/muse/sources/community/2026-11-07-muse-my-ai-assistant" >}})）。有选民案例中，Muse 凭对用户几个月的记忆，找出了选民指南里没有的利益冲突（[Muse 读选票实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-read-my-ballot" >}})，作者称是单一案例）。Enterpret 对用户帖子的统计中，Muse 在记忆一项得分最高（[12 款个人智能体用户排名]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})）。
- **盲区。** Kunal Ugale 的收件箱测试中，Muse 只查了前 20 封邮件，也没有查已发送文件夹（[Grokbot 与 Muse 收件箱测试]({{< relref "/docs/industry/sources/community/2026-10-29-grokbot-muse-inbox-test" >}})，只收到页面摘要）。有作者提醒，一次性的请求可能悄悄变成长期偏好（[联系不上时智能体在做什么]({{< relref "/docs/muse/sources/community/2026-10-27-muse-unreachable-decision-rules" >}})）。Meta 没有公布长任务中上下文衰减、漂移的数据（[智能体忘了任务中段]({{< relref "/docs/muse/sources/community/2026-11-04-muse-mid-job-forgetting-context-rot" >}})）。

## 资料缺口

- Relationships 任务的官方说明与现状：是否修改或增加开关，非用户如何删除自己的页面。
- 遗忘与重置的实测：遗忘后索引、压缩摘要、备份中的残留；已撤回的事实会不会被重新提取。
- Messages、Signal 通知等同步数据的保存位置、期限与删除方式；Meta 对 NebuSec 研究、路透串号报道的公开回应。
- Active Memory 的方法论与第三方复测；与数据留存的关系。
- 健康数据可读的类型清单；Instagram 推荐兴趣进入记忆的范围。
- 隐私政策原文中记忆的保存期限，以及英国、欧盟地区有无不同的记忆设置。

## 主要资料

- 官方：[我们如何设计 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})（设计：记忆文件可读可改、侧边对话）；[帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})（存储清单、遗忘、导出）；[帮助：个性与记忆]({{< relref "/docs/muse/sources/official/2026-09-30-help-personality-memories" >}})（记忆来源、导入记忆）；[帮助：隐私与安全]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})、[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})（删除与断开后仍可能记得）；[我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})（虚拟机内文件可下载）；[Muse Wonder 模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}})、[特化模型：Muse 与 Meta AI]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})（Active Memory 数字）；[英国上线与控制权]({{< relref "/docs/muse/sources/official/2026-11-24-muse-you-stay-in-control" >}})（英国上线时的记忆控制）
- 媒体：[WIRED：亲友人物档案]({{< relref "/docs/muse/sources/media/2026-10-03-wired-muse-profiles-friends-family" >}})（WIRED 人物页报道）；[Medianama：人物档案（二手）]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})（转述 TIME 的档案与遗忘指令）；[WIRED：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})（无关闭开关）；[路透：Muse 安全事故]({{< relref "/docs/muse/sources/media/2026-11-18-muse-early-safety-mishaps-surface" >}})（路透：疑似串号）；[CMA 英国上线声明]({{< relref "/docs/muse/sources/media/2026-11-24-cma-statement-uk-launch-muse" >}})（CMA、ICO 提示）；[Muse 进 Instagram 私信]({{< relref "/docs/muse/sources/media/2026-11-24-techcrunch-muse-instagram-dms" >}})（Instagram 私信与 Collections）
- 社区：[Peter James：文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})、[Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})（文件系统与索引结构）；[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})（内部指令逐条核验，页面自注由 AI 生成）；[删除聊天记忆仍在]({{< relref "/docs/muse/sources/community/2026-10-28-muse-delete-chat-memory" >}})（删除控制对照）；[iMessage 事件详解]({{< relref "/docs/muse/sources/community/2026-10-01-did-muse-read-your-messages" >}})、[Signal 消息与通知权限]({{< relref "/docs/muse/sources/community/2026-11-19-muse-signal-notification-permission" >}})（Messages 同步与 Signal 通知）；[黑进 Muse 窃取对话]({{< relref "/docs/muse/sources/community/2026-11-20-nebusec-hacking-muse-browser-use" >}})（NebuSec：记忆外传与篡改）；[Wonder 训练模型上线]({{< relref "/docs/muse/sources/community/2026-11-09-museexplained-wonder-trained-models-live" >}})（Active Memory 数字核对）；[两个月 Muse 使用记录]({{< relref "/docs/muse/sources/community/2026-11-07-muse-my-ai-assistant" >}})、[Muse 读选票实测]({{< relref "/docs/muse/sources/community/2026-11-11-muse-read-my-ballot" >}})（长期使用实例）；[信息专员谈代理式 AI]({{< relref "/docs/muse/sources/community/2026-11-27-isle-of-man-commissioner-agentic-ai" >}})（马恩岛信息专员）
- 实测：[我的实测：VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})（2026-10-12 虚拟机探索：文件为源、数据库为索引、跨虚拟机重建保留）
