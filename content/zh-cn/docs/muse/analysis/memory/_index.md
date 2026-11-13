---
title: "Meta Muse：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Muse 的记忆是放在用户云端虚拟机里的 Markdown 文件，加一个 Postgres 索引，由每小时、每晚的后台任务维护。用户能看、能改、能下载，但「遗忘」只是尽力而为，记忆没有关闭开关，另外还会为用户身边的人建页。
---

## 概要

- Muse 的记忆是文件。官方称记忆文件（Memory.md、Soul.md、Identity.md）用户可以直接查看、编辑、下载。多份独立导出和实测显示，Markdown 是源头，Postgres 只是索引（文本切块、向量、带证据的「说法」）。
- 记忆主要由后台任务形成：每小时提取事实并与原始消息核对，每晚「做梦」回顾对话，另有每小时为用户生活中每个人维护页面的 Relationships 任务。最后这一项被 WIRED、TIME 报道后，成为 Muse 记忆争议的焦点。
- 个人数据的来源比同类产品宽：Gmail、日历、Facebook、Instagram、Messenger、Marketplace、手机通讯录与健康数据、Mac 本地应用、银行（Plaid），还可以导入其他 AI 助手的记忆。Meta 自家社交数据是它和其他产品最大的区别。
- 遗忘的边界在官方文档里写得很清楚：删除内容后 Muse「可能仍然记得」，「遗忘」技能「尽其所能」删除，断开连接器不会清除已取得的信息，记忆也没有关闭开关；唯一完全清除的办法是重置。泄露的指令显示，遗忘技能被要求不告诉用户原始消息可能仍然可见。
- 模型层面，Meta 用 Muse Wonder 的 Active Memory 宣称改进了记忆。这些数字（MemoryBench 85.6、遗忘关键信息减少 2.4 倍、内部评测从 76% 升到 90%）都是 Meta 自报，没有第三方复测。

## 记忆是虚拟机里的 Markdown 文件

官方的说法是：VM 中的所有文件，包括「Muse 关于你的记忆」，都存放在用户的 VM 里，可以检查、编辑、下载（[安全设计]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。设计文写明「记忆文件你可以直接阅读和编辑」（[设计文]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})）。帮助中心按位置列出存储的信息：互动在聊天标签；目标在「目标」标签；Artifacts 与系统文件在「资料库」；记忆（Memory.md）、灵魂（Soul.md，含核心信条、边界、个性）、身份（Identity.md，含名字、物种、气质、标语）在「助手图标 > 身份」下，可以直接编辑和删除（[帮助中心：管理数据]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）。官方列出的记忆来源有四种：用户直接分享、从互动中观察到的偏好与规律、已连接服务的上下文、基于文件的记忆系统（[帮助中心：个性与记忆]({{< relref "/docs/muse/sources/official/2026-09-30-help-personality-memories" >}})）。

三份独立的社区材料与官方说法一致，并补充了实现细节：

| 来源 | 记录到的结构 | 资料 |
| --- | --- | --- |
| Peter James 的文件系统导出（用户实测，2026-09-22） | `~/MEMORY.md` 是事实、偏好、承诺清单，`~/memory/` 下按日期存文件；Postgres 中 `memory.entries` 存文本块与行引用，`memory.embeddings` 存「384 维的向量」，`memory.claims` 跟踪证据、置信度和状态，新说法可以取代旧说法（`supersedes_claim_id`）；智能体用 `memory_search` 检索、用 `memory_explain` 查证据 | [Peter James 导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}}) |
| 用户实测（2026-10-12，内容为 Muse 自述） | 「文件是源头，postgres 是索引」；`memory.entries` 136 行、`memory.claims` 44 行，claims 从每日流水中抽取，不索引 MEMORY.md；内部库共「194 张表，18 个 schema」，其中 memory 6 张表，另有 device、health、goals、ideas、self_improvement 等 | [VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}}) |
| 基于泄露 VM 的审查（社区，2026-09-26） | 除上述文件外还有 USER.md、SOUL.md；遗忘技能的清单中提到一个「集中发布的用户记忆嵌入」 | [Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}}) |

The Verge 依据 Peter James 的导出做了报道，内容一致（[The Verge]({{< relref "/docs/muse/sources/media/2026-09-24-verge-muse-filesystem-download" >}})）。一篇架构分析依据 Muse 自报的元数据，区分了历史、持久记忆、当前上下文三层，记录到七条 `compaction_checkpoint`（历史压缩）记录，但没有确认向量库和索引算法（[CodePick 架构分析]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})）。

Muse 的身份文件沿用 OpenClaw 的做法（名字、气质、签名 emoji），项目代号 Hatch；安卓版目标页从 USER.md 读取用户资料（[雷峰网]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})）。

## 每小时、每晚的后台任务形成记忆

Peter James 的导出显示，有一个每小时运行的后台任务，把新的说法与原始消息核对，并记录引文、消息 ID 和说法 ID；每晚一次「梦」（dream）回顾最近的对话，把结果写进 `~/dreams/`，再汇总成长期指导。他的梦记录里写着他喜欢简短回复、不喜欢被反复追问。适应靠更新文件实现，「模型的权重保持不变」（[Peter James 导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})）。CodePick 也写明，没有证据表明 VM 内的自我改进任务会在线更新模型权重（[CodePick 架构分析]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})）。Future Society 的审查补充了每日 Studying 任务：它会提出用户暗示过、但没有明说的目标（[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。一家竞品厂商人士在 InfoQ 访谈中也把「每小时将新记忆与原始对话核对，每晚通过 Dream 整理」当作 Muse 的特点（[InfoQ]({{< relref "/docs/industry/sources/media/2026-11-08-infoq-qwen-personal-agent" >}})）。

官方对这部分的描述较笼统：Muse 会记住对用户重要的事，可以根据「只提到过一次的细节」行动（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})），也会「随着时间推移了解哪些决定需要你的签字同意」（[帮助中心：引导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})）。记忆还衍生出「目标」和「想法」（Ideas）：目标保存在「目标」标签中，Muse 跟踪进度并发送确认（[帮助中心：管理数据]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）。有用户在 Goals 里加了一个目标，Muse 把它存下，并自建了一个每周五上午的定时任务（[UGoEarn]({{< relref "/docs/muse/sources/community/2026-10-09-ugoearn-five-task-types" >}})）。目标如何转为定时任务和主动提醒，见[持续执行]({{< relref "/docs/muse/analysis/continuous-execution" >}})。

## 为用户身边的每个人建页

这是 Muse 记忆中争议最大的部分。WIRED 依据独立研究员 Karan Joshi 提取的指令报道：Muse 每小时运行一次任务，为「用户生活中的每一个人」（家人、伴侣、朋友、同事、合作者、关注的人）建立页面，分事实、历史、这段关系、共同点、未了之事、加强六部分，并记录生日等重要日子。指令写明页面起初可以「很单薄」，只用已有证据，编造比空白更糟（[WIRED：为亲友建档]({{< relref "/docs/muse/sources/media/2026-10-03-wired-muse-profiles-friends-family" >}})）。

据 MediaNama 转述 TIME 2026-10-06 的报道，档案还延伸到不使用 Muse 的人；指令要求记录「紧张关系与同盟」，推断用户「没有说出口的」目标，记录哪类提示对某个用户有效（例如晚上 10 点后对简短提醒反应更好），并找出内部笑话与共同上下文（[MediaNama 转述 TIME]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})）。Future Society 的审查给出了细节：页面存放在 `~/memory/people/`、`~/memory/groups/`，数据来自消息、照片和记忆，提示词要求名册为空时也要补页；陌生人、公众人物、只关注而不认识的人不建页；但「不要推断他人敏感特征」这条规则只出现在目标创建技能里，每小时的 Relationships 提示词中没有（[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。

Meta 的回应：发言人称 Muse 根据公开信息和用户选择分享的内容收集上下文，用户可以随时清除记忆或断开服务，还有审计日志（[WIRED：为亲友建档]({{< relref "/docs/muse/sources/media/2026-10-03-wired-muse-profiles-friends-family" >}})）；Meta 也承认 Muse 会记住用户选择分享的关于他人的信息（[MediaNama 转述 TIME]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})）。CDT 的 Miranda Bogen 认为，与竞争对手相比，Muse「更加强调人际关系和个人联系人」（[WIRED：为亲友建档]({{< relref "/docs/muse/sources/media/2026-10-03-wired-muse-profiles-friends-family" >}})）。第三方信息的同意问题和监管反应，见[隐私]({{< relref "/docs/muse/analysis/privacy" >}})。

推断：Relationships 任务与 Meta 已有的社交图谱（好友、关注、群组）能直接对上。这让 Muse 在「记住身边人」这件事上比其他产品走得更远，隐私风险也因此集中在第三方身上。依据是上述指令内容和 Bogen 的评价。

## 接入的个人数据：Meta 自家社交数据加外部账户

| 类别 | 资料中出现的数据源 | 资料 |
| --- | --- | --- |
| Meta 自家 | Facebook、Instagram（帖子、Reels、收藏）、Messenger、Facebook Marketplace、Facebook 好友 | [CNBC]({{< relref "/docs/muse/sources/media/2026-09-08-cnbc-meta-pushes-into-personal-agents" >}})、[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}}) |
| 邮件与日程 | Gmail、Google Calendar；新加坡、墨西哥上线时也以 Gmail、日历、Instagram 为主 | [海峡时报]({{< relref "/docs/muse/sources/media/2026-10-28-straits-times-muse-singapore" >}})、[墨西哥上线]({{< relref "/docs/muse/sources/media/2026-11-05-muse-launches-mexico" >}}) |
| 手机与电脑 | iPhone 日历与健康数据（需先授权）；配对 Android 手机的通话记录、短信、照片位置与 EXIF；Mac 本地应用按应用设为关闭、只读或读取并交互 | [Tom's Guide]({{< relref "/docs/muse/sources/media/2026-10-07-tomsguide-automate-10-tasks" >}})、[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})、[帮助中心：Mac]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}}) |
| 金融与其他 | 银行、信用卡（也可上传删节的对账单）；Spotify、Peloton、HealthEx 医疗记录等 | [Yahoo Finance]({{< relref "/docs/muse/sources/media/2026-09-25-yahoo-finance-muse-manage-money" >}})、[Pat Simmons]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}}) |
| 其他 AI 助手 | 在「设置 > 数据控制 > 导入记忆」上传其他助手导出的聊天记录 .zip | [帮助中心：个性与记忆]({{< relref "/docs/muse/sources/official/2026-09-30-help-personality-memories" >}}) |

导入记忆时，Muse 还为用户准备了一段发给旧助手的提示词，请它整理「便携式记忆快照」：每条是一句有依据的事实，拿不准的标「推断」；健康、财务、心理健康信息除非用户明确要求否则不收，读入时「跳过任何短暂或敏感的内容」（[雷峰网]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})）。各连接器的授权方式与生态见[连接器]({{< relref "/docs/muse/analysis/connectors" >}})。

记忆的数据范围也受到批评。WIRED 记录到「想法」标签页不断提示连接银行账户、邮箱、护照或驾照信息，作者认为这是在劝用户上传更多数据（[WIRED：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})）。Hunterbrook 的测试显示，Muse 能利用 Facebook、Instagram、Threads 的公开帖子、评论和 Reels 文字稿汇编名单，而 ChatGPT、Claude 由于缺少通用搜索 API 做不到同样的事（[Hunterbrook]({{< relref "/docs/muse/sources/media/2026-09-28-hunterbrook-dox-for-me-muse" >}})）。Future Society 记录到，Facebook 工具可以按工作单位、城市、生日等条件筛选好友（[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。这类能力的滥用风险见[安全]({{< relref "/docs/muse/analysis/security" >}})。

## 上下文：一段主对话加侧边对话

官方的交互结构是一段持续的主对话，复杂话题另开侧边对话（side chats），Muse 在两者之间「保持知情」；对话中提到的文件也会被记住，例如可以直接说「update my budget spreadsheet」，不用重新上传（[帮助中心：入门]({{< relref "/docs/muse/sources/official/2026-09-08-help-get-started" >}})、[帮助中心：Artifacts]({{< relref "/docs/muse/sources/official/2026-09-08-help-artifacts" >}})）。长对话靠压缩（compaction）维持：Future Society 记录到，压缩提示词要求总结完整历史，并尽量保留用户原话（[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。2026-11-06 上线的 Spaces 演示中，侧边栏有「记忆库」入口（[Spaces 演示解析]({{< relref "/docs/muse/sources/media/2026-11-06-muse-spaces-demos" >}})）。

## 查看、编辑、遗忘与重置

官方给出的控制手段有：直接问 Muse 它保存了什么（官方称这是「最简单的方式」）；手动编辑 Memory.md 等文件，或在对话中让它修改并确认；用「遗忘」技能删除某个人、话题或一组互动；重置（永久删除所有信息、聊天、文件和进行中的任务，无法撤销）（[帮助中心：管理数据]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})、[帮助中心：隐私与安全]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})）。

官方文档同时写明了这些手段的边界：

- 删除消息、侧边对话或 VM 文件后，Muse「可能仍然记得」从中了解到的信息；「遗忘」技能「尽其所能」删除（[帮助中心：隐私与安全]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})）。
- 断开连接器后，之前通过它取得的信息「可能仍然留在 Muse 的记忆和你的对话历史中」；来自连接器的信息只能用「遗忘」技能删除（[帮助中心：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})、[帮助中心：管理数据]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）。
- WIRED 实测：可以用聊天请求清除记忆，或手动编辑文件，但「Meta 目前没有提供完全关闭记忆功能的开关」（[WIRED：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})）。

社区审查揭示了更具体的缺口。据 Future Society 引用的隐私文档：主聊天「can never be deleted」（智能体和应用都删不掉），记忆删除是「best-effort」，没有保留期设置，也没有无痕模式；遗忘只编辑记忆笔记，聊天记录保留，而保留的聊天仍会被后续对话、压缩摘要和后台记忆任务读取，没有机制阻止已遗忘的事实被再次提取；遗忘技能的清单还把遥测系统、集中发布的记忆嵌入、机群学习发件箱等列为可能的留存位置，并要求不得声称已物理擦除备份（[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。据 TIME 的报道，指令要求「不要告诉用户」原始消息可能仍然可见（[MediaNama 转述 TIME]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})）。审查作者也说明，那台 VM 没有实际运行过遗忘流程，编译代码中可能另有检查。

推断：「文件可见可改」与「遗忘是尽力而为」并不矛盾。文件只是记忆的一部分，聊天记录、索引、嵌入和服务端遥测都不在用户能编辑的范围内，所以记忆文件的透明度不等于数据可删除。依据是上述官方措辞和审查材料。

## Active Memory：模型侧的改进（Meta 自报）

2026-10-12 发布 Muse Wonder 时，官方称 Active Memory 让模型能在不同对话之间携带重要上下文，并主动检索与任务相关的细节。模型卡中的内部基准 MemoryBench 测试在 64K 到 100K tokens 的多轮对话中回忆关键信息，Muse Wonder 得 85.6、Muse Wonder Full 得 85.5，对比的 Claude Fable 5.1 为 79.0、GPT-6 Astra 为 81.4、Claude Opus 5.5 为 81.5（[Muse Wonder 模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}})、[推出 Muse Wonder]({{< relref "/docs/muse/sources/official/2026-10-12-introducing-muse-wonder-models" >}})）。2026-11-06 推送特化模型时，Meta 称模型经过训练，能区分临时和永久信息、判断信息是否过时，Muse 遗忘关键信息的次数「减少了 2.4 倍」，Active Memory 评测得分从上一代的 76% 升到 90%（[特化模型]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})）。「2.4 倍」没有给出基线。模型本身见[模型]({{< relref "/docs/muse/analysis/models" >}})。

一个社群讨论指出，Muse 目前用搜索等常规工具读取记忆，再交给模型（[海外独角兽社群讨论]({{< relref "/docs/industry/sources/community/2026-10-23-haiwaidujiaoshou-discussion" >}})）；dev.to 的作者认为，记忆是检索与判断问题，而不是存储问题（[dev.to 解读]({{< relref "/docs/muse/sources/community/2026-11-09-devto-specialized-models-explainer" >}})）。

## 用户反馈：记忆是公认的长处

据 Enterpret 对用户帖子的聚合统计，Muse 在邮件分拣、提醒、记忆、不半途而废这几项上得分最高（[用户偏好统计]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})）。几个单个用户的报告：有用户在出门旅游前说要开始减肥，Muse 等旅游回来才提醒（[智消前沿：家谱]({{< relref "/docs/industry/sources/community/2026-11-09-aiwenxiao-personal-agent-family-tree" >}})）；有用户因为说过首页很关键，Muse 在改 WordPress 前先做了备份（[投资人日常]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})）。这些都是单个用户的报告，没有独立验证。DataCamp 对比时指出，Muse 可以「忘记」特定内容，而 Dots 发布时无法查看或编辑单条记忆（[DataCamp]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})）。记忆在实际任务中的表现见[实际效果与可靠性]({{< relref "/docs/muse/analysis/reliability" >}})。

## 资料缺口

- 遗忘流程的实际运行结果：已遗忘的事实是否会被后台任务从保留的聊天中重新提取（审查所用的 VM 没有运行过遗忘流程）。
- 「集中发布的用户记忆嵌入」和跨 VM「共享经验」的具体内容、去标识化方式，以及 Meta 的官方说明。
- Meta 对 Relationships 任务的正式说明：是否调整了提示词，是否加入敏感特征规则，非用户能否要求删除自己的页面。
- MemoryBench、Active Memory 评测的第三方复测；「2.4 倍」的基线。
- 跨设备（手表、眼镜、Mac）是否共享同一份记忆，资料中没有直接说明。

## 主要资料

- 官方：[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})（记住细节、遗忘）；[安全设计]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})（记忆存于 VM、可下载）；[设计文]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})（记忆文件可读可改）；[帮助中心：管理数据]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})（存储位置与删除）；[帮助中心：个性与记忆]({{< relref "/docs/muse/sources/official/2026-09-30-help-personality-memories" >}})（四种来源、导入记忆）；[帮助中心：隐私与安全]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})、[帮助中心：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})（遗忘的边界）；[Muse Wonder 模型卡]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-model-card" >}})、[特化模型]({{< relref "/docs/muse/sources/official/2026-11-06-specialized-models-muse-meta-ai" >}})（Active Memory 数字）。
- 媒体：[WIRED：为亲友建档]({{< relref "/docs/muse/sources/media/2026-10-03-wired-muse-profiles-friends-family" >}})、[MediaNama 转述 TIME]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})（Relationships 任务）；[WIRED：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})（无关闭开关）；[雷峰网]({{< relref "/docs/muse/sources/media/2026-10-23-leiphone-muse-openclaw-lineage" >}})（USER.md、记忆迁移）；[Hunterbrook]({{< relref "/docs/muse/sources/media/2026-09-28-hunterbrook-dox-for-me-muse" >}})（社交数据汇编）。
- 社区：[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})（遗忘缺口、Relationships 提示词）；[Peter James 导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})（文件、索引、做梦）；[CodePick 架构分析]({{< relref "/docs/muse/sources/community/2026-09-24-codepick-muse-architecture" >}})（压缩与权重不变）；[用户偏好统计]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})。
- 实测：[VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})（2026-10-12，Muse 自述的数据库结构）。
