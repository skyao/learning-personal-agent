---
title: "在 Gemini 中为任务创建和管理计划"
linkTitle: "帮助：计划"
date: 2026-11-05
originalTitle: "Create & manage schedules for tasks in Gemini"
sourceUrl: "https://support.google.com/gemini/answer/17094710?hl=en"
author: "未署名"
publisher: "Google（Gemini Apps 帮助中心）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-28
dateNote: "帮助页不标日期，结构化数据中也没有；日期取收集日期（美东时间）。2026-10 Spark 改名为 Task 后，帮助页的用词已改为 tasks / task mode；2026-11-10 发现原文更新：「What you need」删去了「选择加入 Personal Intelligence」一条，原文存档与译文同步删除，其余未变；2026-11-28 发现原文更新：不再要求 Google AI Pro 或 Ultra 订阅，地区改为免费六国与其他地区的订阅用户两层；新增无订阅或 Plus 用户的计划方式（每天最多一次、按大致时段运行）与分档的活跃计划上限（50 与 10）；「Keep Activity」改称「History」；删去「取消或降级订阅」一节。原文存档已覆盖，旧译文删除，已重新翻译"
tags: [持续执行, 运行环境]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：官方帮助页，取英文版的默认（Computer）视图；页面中的界面小图标已下载。旧笔记 learning-ai-agent 的 Gemini Spark 资料索引引用过这篇。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：计划（schedule）有三种：按时间、Gmail 监控、话题监控。2026-11 起不再要求订阅：无订阅可用于澳大利亚、加拿大、印度、日本、韩国和美国，其他支持 Gemini 应用的地区（欧洲经济区、尼日利亚、瑞士、英国除外）需要 Google AI Pro 或 Ultra。有 Pro 或 Ultra 时可以创建全部三种计划；无订阅或只有 Google AI Plus 时，任务每天最多运行一次，只能选夜间、白天或晚上这样的大致时段。活跃计划上限是 Pro/Ultra 50 个、Plus 或无订阅 10 个。页面提醒监控不适合追踪变化很快的数据或时间要求极高的任务。

**保留理由**：说明了持续执行的触发方式和各档位的上限，免费开放后的版本给出了免费档与订阅档在计划能力上的差别。

---

你可以给任务加上计划（schedule），让工作流自动运行。计划是任务的自动触发器，告诉 Gemini 在什么时间介入并执行你的指令。触发器可以基于时间间隔设置，比如每周一早上；也可以基于特定条件设置，比如收件箱里收到某封邮件时。

上手时，你可以在任务线程或 Live 聊天中与 Gemini 对话式地创建计划。只要说明你想让 Gemini 做什么、什么时候做。你也可以前往 Scheduled（已排期）页面自己创建。

**重要：** 本文介绍的是任务中的计划，与聊天中的计划不同。[了解聊天中的计划如何运作](https://support.google.com/gemini/answer/16316416)。

## 需要什么

要给 Gemini 分配任务，你必须：

- **年满 18 岁**。
- **用个人 Google 账号登录 Gemini 应用。** 目前，用工作或学校 Google 账号登录时无法使用此功能。[了解如何登录 Gemini Apps](https://support.google.com/gemini/answer/13278668)。
- **开启 [History](https://myactivity.google.com/product/gemini)（历史记录）**。

**重要：** 目前，Gemini 中的任务：

- 在澳大利亚、加拿大、印度、日本、韩国和美国，无需 Google AI 订阅即可使用。
- 在其他支持 Gemini Apps 的地区，需要 Google AI Pro 或 Ultra 订阅；欧洲经济区、尼日利亚、瑞士和英国除外。
- 仅在 Gemini 移动应用、Mac 上的 Gemini 应用，以及 [gemini.google.com](https://gemini.google.com) 上的 Gemini 网页应用提供。

## 计划的类型

有 Google AI Pro 或 Ultra 订阅时

有 Google AI Pro 或 Ultra 订阅时，你可以创建三种计划。

- **按时间：** 让任务运行一次、每小时、每天、每周、每月或每年运行。
  - 例如：「每天早上 7 点，翻看我的邮件、日历和 Drive，告诉我今天该优先做什么」
- **Gmail 监控：** 当你收到符合某个 Gmail 筛选条件的邮件时，让任务运行。
  - 例如：「每当我收到经理发来、给我布置了待办事项的邮件，帮我处理该事项并起草回复。」
- **话题监控：** 监控新闻、财经、体育、本地活动等各类话题，并让任务在出现特定事件时运行。
  - 例如：「每当我的城市宣布新的快闪美食活动，把详情发邮件给我，并在我的日历上建议一个去看看的时间。」

虽然 Gemini 在监控和更快响应事件方面有所改进，但监控仍不适合追踪变化很快的数据，也不适合执行时间要求极高的任务，比如「门票一开售就立刻通知我，好让我买到」。

[了解按时间的计划如何处理时区](#schedules_timezones)。

没有 Google AI 订阅，或只有 Google AI Plus 时

没有 Google AI 订阅，或只有 Google AI Plus 时，你可以让任务每天最多运行一次，运行时间落在一个大致时段内：夜间、白天或晚上。设置完成后，任务会在你设定的时段内大致相同的时间运行。

[了解按时间的计划如何处理时区](#schedules_timezones)。

## 创建计划

通过对话创建计划

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在文本框下方，点击 **Task**（任务）。
3. 在文本框中，描述你想安排的任务。
   - 例如：
     - 「每天早上 7 点，翻看我的邮件、日历和 Drive，告诉我今天该优先做什么。」
     - 「每当我收到经理发来、给我布置了待办事项的邮件，帮我处理该事项并起草回复。」
   - 要指定使用某个已有的技能（skill），输入 `/`，开始输入技能名称，然后选中该技能。如果它处于关闭状态，你可以把它打开。[进一步了解技能](https://support.google.com/gemini/answer/17094296)。
4. 点击「提交」![](images/img-02-c4d89f.png)。

用空白模板创建按时间的计划

手动创建计划的选项只适用于在某个具体时间或大致时段运行的计划。要让任务在具体时间运行、且一天运行多次，你需要 Google AI Pro 或 Ultra 订阅。

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在侧边栏，点击 **Scheduled**（已排期）![](images/img-03-74e6c3.png)。
3. 在 Scheduled 页面，点击「创建已排期任务」![](images/img-04-440f9d.png)。
4. 为计划输入名称。
5. 在「Plan」下，输入该任务的指令。
6. 选择你希望任务运行的时间。
7. 完成后，点击 **Create**（创建）。计划会保存到你的「Active」（活跃）列表。

**提示：** 要测试新建的计划，把鼠标悬停在计划上，然后依次点击「更多」![](images/img-05-53995d.png) ![然后](images/img-06-bfcdbc.png) **Run now**（立即运行）![](images/img-07-b49f50.png)。

## 管理你的计划

跟踪计划的运行状态，并随需求变化修改设置。

找到你的计划并查看状态

你可以在任务线程的工作面板中找到属于该任务的计划列表。

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在侧边栏，点击你想查看或管理的任务所在线程。
3. 要显示任务线程的工作面板，点线程顶部的进度标签。在这里，你可以查看属于该任务的所有计划。

你可以在 Scheduled 页面找到所有任务中存在的全部计划。

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在侧边栏，点击 **Scheduled**（已排期）![](images/img-03-74e6c3.png)。
3. 查看按以下分区整理的计划：
   - **Active（活跃）：** 正在运行或等待运行的计划。
   - **Paused（已暂停）：** 你临时暂停的计划。
   - **Completed（已完成）：** 已运行完毕的计划。已完成的计划只能删除。

编辑计划

**重要：** 如果你想编辑某个计划，可以在相关的任务线程中让 Gemini 来改。如果找不到相关的任务线程，你也可以在 Scheduled 页面编辑计划。

#### 第 1 步：前往 Scheduled 页面

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在侧边栏，点击 **Scheduled**（已排期）![](images/img-03-74e6c3.png)。

#### 第 2 步：选择编辑计划的方式

**用 Gemini 编辑：**

1. 在 Scheduled 页面，把鼠标悬停在你想编辑的计划上。
2. 点击「前往聊天」![](images/img-08-ef3b3f.png)。
3. 在线程中，告诉 Gemini 你想做哪些修改。

**直接编辑计划：**

1. 在 Scheduled 页面，点击你想编辑的计划。
2. 修改计划，比如它何时运行及其指令。
3. 完成后，点击 **Save**（保存）。

**提示：** 要编辑非按时间的计划的触发器，前往带该计划的任务线程，告诉 Gemini 你想做的修改。

暂停或恢复计划

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在侧边栏，点击 **Scheduled**（已排期）![](images/img-03-74e6c3.png)。
3. 点击你想暂停或恢复的计划，进入其详情页。
4. 在顶部，依次点击「更多」![](images/img-05-53995d.png) ![然后](images/img-06-bfcdbc.png) **Pause**（暂停）![](images/img-09-ba979f.png) 或 **Resume**（恢复）![](images/img-10-1de8b2.png)。

删除计划

**重要：** 如果你删除某个任务线程，也会删除该线程中的所有计划。

1. 在你的电脑上，前往 [gemini.google.com](https://gemini.google.com)。
   - 在 Mac 上，你也可以打开 Gemini 应用 ![](images/img-01-4a5c21.png)。
2. 在侧边栏，点击 **Scheduled**（已排期）![](images/img-03-74e6c3.png)。
3. 把鼠标悬停在你想删除的计划上。
4. 依次点击「更多」![](images/img-05-53995d.png) ![然后](images/img-06-bfcdbc.png) **Delete**（删除）![](images/img-11-23ae4d.png)。

## 解决问题

我无法创建或开启计划

你可能出于以下几种原因无法创建或开启计划。

- **已达到活跃计划上限：** 目前，任务可拥有的活跃计划上限为：有 Google AI Pro 或 Ultra 时 50 个，有 Google AI Plus 或没有订阅时 10 个。达到上限后若要创建或恢复计划，请先暂停或删除一个已有的计划。
- **计划已完成：** 计划被标记为完成后，你无法编辑或恢复它，只能删除。
- **缺少必填项：** 如果你用模板创建计划，但无法选择「创建」，请确认已填写所有部分：计划名称、运行时间，以及任务指令。

为什么我的计划没有按时运行，或者根本没有运行？

计划可能因以下原因没有运行：

- **达到使用量上限：** Gemini Apps 有基于算力的使用量上限，它决定你能与 Gemini 工具和功能交互到什么程度。如果在计划该运行的时候你已达上限，计划就不会运行。达到使用量上限时，其他功能也可能不可用。[进一步了解 Gemini Apps 中的限额](https://support.google.com/gemini/answer/16275805)。
- **达到并发任务上限：** 同一时间你最多可以有 15 个任务在运行。如果当前已有 15 个任务在运行，计划就不会运行。
- **计划运行时间会有浮动：** 已排期任务的运行时间是大致的，未必正好在满足时间或事件条件的那一刻运行。
- **高流量时延迟：** Gemini Apps 活动量大幅增加时，已排期任务可能会延迟。

## 常见问题

任务、计划和技能有什么区别？

为了充分利用任务，了解支撑其逻辑的三个基本构件会很有帮助：任务、计划和技能。可以把它们理解为做什么、何时做和怎么做。

**任务是你的高层目标。** 它代表你想让 Gemini 为你管理的一个完整项目或目标。

- **示例：** 「规划并管理我去伦敦的商务旅行。」

**计划让你把任务交给** Gemini，让它们在后台自动运行。你告诉 Gemini 做什么、什么时候做。任务可以安排在某个具体日期和时间运行，也可以安排在某事件发生时运行。

- **示例：** 「每天早上 8 点（条件），给我一份 AI 新闻的更新（任务）」
- **示例：** 「当我的航班延误时（条件），通知我，并提议对行程做出调整（任务）。」

**提示：** 任务中的计划不同于 Gemini 聊天中的已排期操作。[了解如何在 Gemini Apps 中安排操作](https://support.google.com/gemini/answer/16316416)。

**技能是一组可复用的指令和额外背景信息。** 它教 Gemini 如何完成某项具体任务、使用哪些工具。你可以指定任务或计划的操作应使用哪个技能。当技能与任务相关时，Gemini 也可以自动使用它。

- **示例：** 同时使用「Travel Booking」（旅行预订）技能和「Gmail Writing」（Gmail 写作）技能，重新预订房间并发送确认。

总之，你定义任务（你想要什么）、设置计划（何时发生），并提供技能（如何完成），来完成工作。

如果我关闭任务模式，我的计划会怎样？

如果你关闭任务模式，你已有的计划会自动暂停。

如果我更换时区，按时间的计划会怎样运作？

Gemini 在云端运行，而不是在你的手机或电脑上。这意味着即使你的设备关机，它也会继续工作。

**计划如何跨时区运作**

- **固定时区：** 当你在 Gemini 应用中创建按时间的计划（比如每日摘要）时，它被锁定在创建地点的时区。
- **旅行：** 即使你旅行到不同的时区，你的计划仍会按原先安排的时间运行。
- **更新计划：** 如果你搬到新地点，想让日常安排适应新的本地时间，只需让 Gemini「按我的新时区编辑计划」。

## 相关资源

- [在 Gemini Apps 中管理你的任务与工作流](https://support.google.com/gemini/answer/17094507)
- [在 Gemini Apps 中查找和管理你的任务](https://support.google.com/gemini/answer/17094196)
- [为 Gemini Apps 创建和管理技能](https://support.google.com/gemini/answer/17094296)
