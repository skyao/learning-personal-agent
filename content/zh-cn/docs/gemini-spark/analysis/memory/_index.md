---
title: "Gemini Spark：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Spark 不另建记忆，上下文直接来自用户的 Google 账号：Personal Intelligence、Gmail 与 Workspace、相册和已登录网站；实测个人化程度很高，但官方没有说明 Spark 自己如何形成和管理记忆。
---

## 概要

- Spark 的上下文来自用户已有的 Google 账号，而不是另起一套记忆：帮助页列出的来源有关联应用、技能、聊天、任务、已登录网站、位置和 Personal Intelligence（含过去 Gemini 聊天的记忆、给 Gemini 的指令、Google 关联应用）。
- 使用前提是开启「保留活动」（Keep Activity），Google 应用连接默认关闭，要在设置里打开。帮助页在 2026-11-10 删去了「选择加入 Personal Intelligence」这一要求。
- 实测中个人化程度是 Spark 最突出的地方：The Verge 作者没说名字，它就从邮件里找到妻子邮箱、狗的名字和家人的饮食禁忌；WIRED 的派对行程里连定金所用信用卡的后四位都有。但人际关系会判断错：WIRED 作者同住的男友被列为「密友」。
- 用户能显式管理的长期上下文主要是技能：可复用的指令加参考文件，采用 `SKILL.md` 格式，2026-09-30 起扩展到普通聊天。
- Spark 自己如何形成、更新、遗忘记忆，用户能否查看和编辑，官方资料都没有说明；能删的只有任务线程、活动记录、远程浏览器与代码执行数据。

## 上下文来自 Google 账号

帮助页列出任务可使用的信息来源：关联应用、技能、聊天、任务、已登录网站、个人智能（Personal Intelligence）和位置；其中 Personal Intelligence 包括「对你过去 Gemini 聊天的记忆」、给 Gemini 的指令以及可配合的 Google 关联应用（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。可连接的 Google 服务包括通讯录、Gemini Notebook、Google 相册、Workspace 全家和搜索系服务（详见[连接器]({{< relref "/docs/gemini-spark/analysis/connectors" >}})）。产品页称这些连接「默认关闭」，要到设置里开启（[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})）。

授权条件随时间有变化：

- Freistyle AI 2026-10-28 访问的帮助页写明，使用 Tasks 要开启 Keep Activity 并主动选择加入 Personal Intelligence（[Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。
- 帮助页 2026-11-10 的更新删去了「选择加入 Personal Intelligence」，Keep Activity 仍是前提（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。关闭 Keep Activity 时，任务不再列在侧栏中，自定义应用不可用（[帮助：查找与管理任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-find-and-manage-tasks" >}})、[帮助：自定义应用]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-custom-apps" >}})）。

Google 相册约在 2026-09 起逐步在任务中可用（资料页依据 The Verge 2026-09-04 的报道定日期），可以搜索、编辑（生成副本，不覆盖原图）、建相册（[帮助：相册工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-google-photos-workflows" >}})）。

The Verge 作者说，Spark 在深度使用 Google 生态、开启 Personal Intelligence 时效果最好，他用 Google 账号约二十年，Spark 有大量数据可用（[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})）。AI Agents Library 的对照测试也认为，Spark 的优势在于「它原生位于这些工作本来所在的地方」（[AI Agents Library 三方对照]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})）。

## 实测：个人化强，关系判断会错

| 实测 | 用上了什么 | 出错的地方 | 资料 |
| --- | --- | --- | --- |
| WIRED，2026-05 Beta 首周，授权 Gmail、Docs、Calendar | 从邮件找到作者已在筹备的卡拉 OK 派对，生成五页行程，含日期、地址、预订详情和 50 美元定金所用信用卡的后四位 | 宾客名单把同住男友写成「密友和经常同行的伙伴」，作者本人不在名单上；追问时 Spark 称依据关键词、行程和交易记录，「不会对你的个人身份作出推断」 | [WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}}) |
| The Verge，2026-06-01 | 没有告诉名字就从 Gmail、Drive 找到妻子邮箱；文件名没有「budget」也找到预算表并提取 2026 年每月食品杂货总额 | 起草的邮件提到不存在的报名表；创建的 Doc 无法共享给妻子 | [The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}}) |
| The Verge，2026-06-02，周末旅行规划 | 从家出发的驾车路线、狗名 Frida、孩子年龄与门票、妻子不吃洋葱、已买的演唱会票；补充父母同行后改推 Airbnb，并直呼父母的名字 | 给妻子的邮件语气像业务同事 | [The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}}) |

两位作者都对这种程度的个人化感到不安：WIRED 作者写「隐私，再见」，The Verge 作者称 Spark 把数据当作「需要挖掘的东西」而不是需要保护的东西（详见[隐私]({{< relref "/docs/gemini-spark/analysis/privacy" >}})）。

推断：从 WIRED 的例子看，Spark 能从交易和行程记录里拼出事实，却缺少对人际关系的可靠判断；它追问时的回答说明，关系是从关键词和共同行程推出的，而不是用户声明过的。

## 技能：用户可管理的长期上下文

技能是「保存的可复用指令加补充上下文」，可在聊天和任务中通用，可以组合、引用其他技能；Gemini 会根据任务上下文自动使用已开启的技能（[帮助：技能]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-skills" >}})）。规则包括：

- 可附参考文件（来自设备、Drive、Google 相册、Notebook）；更新文件要重新上传整个技能；下载为 .zip，不含 Drive 文件和笔记本。
- 技能名全小写、用连字符分隔，根目录须有 `SKILL.md`；不能在聊天或任务线程里启用、停用、删除技能。
- Gems 被移除时会自动重建为技能。
- 技能最早是 Spark 的功能，2026-09-30 起扩展到普通聊天，且无需 Google AI 订阅即可使用。

产品页的示例是让 Spark 读最近 50 封邮件，生成写作风格指南，存为名为 ghostwriter 的技能，以后起草邮件时调用（[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})）。

## 任务线程与删除

- 只有开启 Keep Activity 时任务才列在侧栏；任务线程可置顶、重命名、按状态筛选、加入笔记本（[帮助：查找与管理任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-find-and-manage-tasks" >}})）。
- 删除任务线程会同时删除该任务、Gemini 应用活动记录中的相关活动、关联的计划；不会删除已创建或修改的文件，也不删除远程浏览器数据和远程代码执行数据（[帮助：查找与管理任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-find-and-manage-tasks" >}})）。

推断：从这些规则看，Spark 的「记忆」分散在几处——Google 账号里的原始数据、Personal Intelligence、技能、任务线程与活动记录、远程浏览器和远程计算机上的数据——各有各的删除入口，没有一个统一的「Spark 记得什么」视图。

## 与平台数据的关系

Top5Apps 称 Spark 原生访问 Gmail、Calendar、Drive、Docs、Sheets、Keep、Tasks、Photos，「无需接线」（[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。中金研报认为平台型助手的优势之一，是平台积累的用户信息为助手理解需求提供背景（[中金研报]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})）。The Verge 作者的看法类似：Google 地位强势，「正是因为它已经拥有所有这些信息」（[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})）。

## 资料缺口

- Spark 自己的记忆机制：会不会从任务中沉淀长期记忆，存在哪里，用户能否查看、编辑、删除。
- Personal Intelligence 与 Spark 的具体关系，以及 2026-11-10 删去「选择加入」要求后的默认状态。
- 跨设备（手机、网页、Mac）上下文是否完全一致。

## 主要资料

- 官方：[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})（信息来源、前提）；[帮助：技能]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-skills" >}})；[帮助：查找与管理任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-find-and-manage-tasks" >}})（删除）；[帮助：相册工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-google-photos-workflows" >}})；[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})（默认关闭、ghostwriter 示例）；[帮助：自定义应用]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-custom-apps" >}})。
- 媒体：[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})、[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})、[The Verge 旅行规划]({{< relref "/docs/gemini-spark/sources/media/2026-06-02-verge-spark-trip-planning" >}})（个人化实测）。
- 社区：[AI Agents Library 三方对照]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})；[Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})（10 月的授权条件）；[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})；[中金研报]({{< relref "/docs/industry/sources/community/2026-11-04-cicc-personal-agent-outlook" >}})。
