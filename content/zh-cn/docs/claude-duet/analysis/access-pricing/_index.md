---
title: "Claude Duet：开放与价格"
linkTitle: "开放与价格"
weight: 100
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Claude Duet 是研究预览，只通过候补名单向美国的 Claude Pro、Max、Ultra 订阅者分批开放；不另收费，但晨报、巡检等后台工作与聊天共用五小时和每周限额，官方为此发放限额重置，口径在 11 月改过一次。
---

## 概要

- 开放范围是跟踪产品中最窄的一档：研究预览，美国的 Claude 账号，Pro、Max 或 Ultra 套餐，加上候补名单邀请；邀请分批发出，没有固定日期；Team、Enterprise 和美国以外地区都不在范围内。
- 研究预览期间不额外收费，入门成本就是 Claude Pro 每月 20 美元。代价在用量：Duet 按与聊天相同的费率计入五小时和每周限额，晨报、巡检等后台工作也计入，可能更早触顶。
- 官方发放限额重置作为补偿，口径改过一次：早期版本是每人一次、11 月 30 日前有效；2026-11-10 前后的帮助文档改为 Pro 三次、Max 与 Ultra 各一次，12 月 15 日前有效。
- 套餐名在预览期间变了：10 月 30 日 Max 5x 改名为 Max（每月 100 美元），Max 20x 改名为 Ultra（每月 200 美元），价格不变。10-21 的发布说明只写 Pro 和 Max，后来的官方页面都写 Pro、Max 和 Ultra。
- 官方没有公布预览期之后的定价，也没有公布每档能跑多少任务。

## 准入条件与候补名单

发布稿称研究预览从 2026-10-21 起通过候补名单开放，首先面向美国的 Pro、Max 和 Ultra 订阅者，轮到时会收到邮件（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。帮助文档列出的条件是 Pro、Max 或 Ultra 套餐，美国的 Claude 账号，候补名单邀请（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）：

- 填写姓名、邮箱、套餐和手机类型（iPhone 或 Android），可选填职业和最想先交给 Duet 做的事。
- 邀请分批发出，加入候补名单「并不保证具体日期」。
- 研究预览期间仅在美国提供；尚未在 Team 或 Enterprise 套餐中提供，计划以后引入。
- 候补名单所用邮箱要与 Claude 账号、手机上的 Apple 或 Google 账号一致，否则可能没有访问权限。

等待时间的个例：Alarcon 用 Max 套餐，加入候补名单八天后（2026-10-29）收到邀请，他认为用 Max 并没有更快（[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})）；Aakash 动用了在 Anthropic 的人脉才较快拿到（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。LaoZhang AI 称官方没有公布 Max、Ultra 用户是否更早受邀（[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})）。aiagentslibrary 提醒，Pro 和 Max 只给加入候补名单的资格，不要只为了 Duet 去买订阅（[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）。

Freistyle AI 认为，对美国以外的企业，Duet「是一个观察项，而不是一个选项」（[Freistyle AI：小企业六款对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。中国新闻周刊 11-08 的报道仍写 Duet「需要排队邀请」（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})）。

## 不另收费，但与聊天共用限额

帮助文档称，研究预览期间 Duet 包含在 Pro、Max、Ultra 套餐内，不额外收费；它按与 Claude 聊天相同的费率消耗套餐的五小时和每周限额，晨报、例行检查等后台工作也计入，因此可能比平时更早触顶（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。产品页的 FAQ 同样写明后台检查计入用量，较大的任务（如财务模型、演示文稿）消耗更多（[产品页]({{< relref "/docs/claude-duet/sources/official/2026-11-05-product-page" >}})）。发布稿解释巡检只是每隔几小时一次，因为不停检查会更快耗尽限额（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。

第三方整理的价格（均为社区资料据厂商价格页整理）：

| 套餐 | 月价 | 说明 | 资料 |
| --- | --- | --- | --- |
| Free | — | 不含 Duet | [aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}}) |
| Pro | 20 美元 | 按年付每月 17 美元（一次性 200 美元） | [LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})、[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}}) |
| Max（原 Max 5x） | 100 美元 | Alarcon 称每五小时和每周用量为 Pro 的 5 倍，含每月 100 美元 API 额度 | [Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}}) |
| Ultra（原 Max 20x） | 200 美元 | Alarcon 称每周限额为 Pro 的 10 倍、经核实没有五小时限额，含每月 200 美元 API 额度 | [Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}}) |

Max 与 Ultra 的限额倍数、API 额度出自 Alarcon 2026-11-01 对 Anthropic 定价的核对，官方 Duet 资料没有这些数字。

与其他跟踪产品的入门成本，LaoZhang AI 11 月 2 日的对照是：Muse 0 美元、受邀后的 Duet 20 美元、Grok Bot 30 美元、Dots 100 美元（[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})）。WIRED 的说法是 Duet 在「每月 20 美元的付费墙后」（[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。

用量实际有多大，资料只有零星说法：Alarcon 转述一位 Reddit 用户称「我一直在测试 Duet，用量大得离谱」，他自己第一天没看用量进度条，不给数字（[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})）。LaoZhang AI 指出官方没有公布各档能跑多少简报或任务，「不另收费」只描述预览期（[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})）。生活有变量认为 Duet 纳入现有套餐、共享额度，说明收费方式仍在探索（[生活有变量]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}})）。

## 限额重置：两个版本

| 版本 | 内容 | 资料 |
| --- | --- | --- |
| 早期（10-29 至 11-02 的第三方转述） | 获准加入后得到一次完整的限额重置，可用至 2026-11-30；在网页或桌面端 设置 > 用量 > 重置 中领取，手机应用不显示按钮 | [Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})、[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})、[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}}) |
| 2026-11-10 前后的帮助文档 | 按套餐区分：Pro 三次，Max 与 Ultra 各一次；补满五小时与每周限额，使用时机自选；未用的 2026-12-15 过期 | [帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}}) |

同一次帮助文档更新还写明 Duet 中不提供 Personal Finance（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。

推断：重置次数向 Pro 倾斜（三次对一次），说明 Pro 档的限额最容易被后台工作耗尽；官方用临时补偿而不是调整限额来应对，与「研究预览期间」的定位一致。

## 套餐更名与「Ultra」出现的时间

10 月 30 日，Anthropic 把 Max 5x 改名为 Max（每月 100 美元），Max 20x 改名为 Ultra（每月 200 美元），现有订阅者自动迁移，价格不变（[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})、[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})）。

Claude 发布说明 2026-10-21 的条目写的是「面向 Pro 和 Max 套餐」（[发布说明]({{< relref "/docs/claude-duet/sources/official/2026-10-21-relnotes-claude-duet-research-preview" >}})），发布稿、帮助文档、Link 与 Shop Pay 帮助页则写 Pro、Max 和 Ultra。推断：发布稿正文在 10-30 改名之后被改写过，其 `updatedAt`（10-23）没有反映这次改动（已记入 `progress.md` 资料页问题表）。生活有变量、aiagentslibrary 写于改名前后，只提 Pro 和 Max（[生活有变量]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}})、[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）。

## 资料缺口

- 研究预览结束后的定价；是否会单独收费或设专门档位。
- 每档套餐能支撑多少晨报、巡检和任务；后台工作的实际用量数据。
- 开放节奏：已发出多少邀请，Team、Enterprise 和美国以外地区的时间表。
- Max、Ultra 限额倍数和 API 额度的官方出处（目前只有 Alarcon 的核对）。

## 主要资料

- 官方：[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})（开放范围）、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})（准入条件、用量、限额重置新版）、[产品页]({{< relref "/docs/claude-duet/sources/official/2026-11-05-product-page" >}})（FAQ 中的用量说明）、[发布说明]({{< relref "/docs/claude-duet/sources/official/2026-10-21-relnotes-claude-duet-research-preview" >}})（只写 Pro 和 Max）
- 媒体：[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})、[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})
- 社区：[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})（等待时间、限额、更名）、[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})（入门成本对比）、[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})、[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})、[Freistyle AI：小企业六款对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})、[生活有变量]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}})
