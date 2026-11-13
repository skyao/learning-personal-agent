---
title: "Claude Duet：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Claude Duet 的「主动」由每天的晨报和每隔几小时一次的账号巡检构成，用户等待批准期间它先做完其余部分；官方把主动联系当作与 Claude 的核心区别，但多名评测者认为它的跟进偏安静，大部分事情仍需提示。
---

## 概要

- 官方把主动性当作 Duet 与 Claude 的核心区别：「Claude 等你打开对话，Claude Duet 会来找你。」形式是每天早上一份简报，之后保持安静，只在需要时发消息。
- 巡检按固定间隔进行，官方称每隔几小时一次，理由是不停检查会更快耗尽套餐限额；紧急事项可能在两次检查之间到达。频率和关注点可由用户指定，官方称仍在测试何时发消息的判断。
- 任务在「任务（Tasks）」标签页里跟踪，只有用户能把任务标记为完成；用户暂时无法批准时，Duet 先完成其余部分，之后回来请求批准。用户不在时运行的例程享有同样的审批防护。
- 实测评价分化：WIRED 测试中 Duet 和 Dots 是仅有的两个主动发现日程冲突的智能体；但 Claire Vo、Aakash、Alarcon 都认为它跟进不足，交出去的任务没有再被提起，大部分功能要靠提示。
- 资料没有给出任务数量、时长等上限，也没有长期（数周以上）运行的记录。

## 晨报与每隔几小时的巡检

发布稿称 Duet 每天早上根据已连接应用中最重要的事项发一份简报，白天持续留意，只在需要时发消息；它每隔几小时检查一次已连接账号，「因为不停检查会更快耗尽你套餐的限额」；用户也可以告诉它想了解什么、多久一次（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。帮助文档的写法是「按固定间隔检查你的账号，因此紧急事项可能在两次检查之间到达」，并把起草回复、发送工作更新、跟进沉寂的线程列为它一天中的工作（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。产品页用「Claude 等你打开对话，Claude Duet 会来找你」概括与 Claude 的区别（[产品页]({{< relref "/docs/claude-duet/sources/official/2026-11-05-product-page" >}})）。

官方承认判断仍在调整：Duet 可能误读一段对话或误判什么才算紧急，何时发消息的判断会根据测试者反馈调整（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。

后台检查计入用量：晨报、例行检查都按与聊天相同的费率消耗五小时和每周限额（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})，详见[开放与价格]({{< relref "/docs/claude-duet/analysis/access-pricing" >}})）。生活有变量的评论指出，用户看到的一条提醒前面可能已经发生了许多次检查，越主动的助理越要决定什么值得查、多久查一次（[生活有变量]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}})）。

官方给出的例子都来自试用者：小企业主 Jess 的晨报中，Duet 未被要求就指出她日历上的一场房产展示排错了日期（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。产品页上「每天早上 5:30 刷新」的 Marlo Pulse 页面和晨报画面是模拟示例，不是实测（[产品页]({{< relref "/docs/claude-duet/sources/official/2026-11-05-product-page" >}})）。

## 任务的生命周期与审批

帮助文档和安全文章描述的任务流程：

- 任务（Tasks）标签页显示进行中的工作，突出需要用户输入的任务；每个任务有自己的页面，用户可以在进行中引导它（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})、[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。
- Duet 可以提示某个任务已完成，但只有用户能把任务标记为完成（同上）。
- 用户暂时无法批准时，Duet 完成任务的其余部分，之后回来请求批准（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。
- 用户不在时运行的例程（routines）享有同样的审批防护；付款或转账、删除订单、创建账号等步骤不受「别再问我」规则覆盖，无论批准过多少次（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})，详见[安全]({{< relref "/docs/claude-duet/analysis/security" >}})）。

Aakash 把这一套描述为「每日心跳」：每天早上的简报列出各频道待办、夜间做了什么和今天可能想做什么，并附按钮选项，任务卡带检查清单（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。

## 实测：发现问题较好，推进和跟进较弱

| 资料 | 观察 |
| --- | --- |
| [WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})（媒体一手，发布约一天后） | 日程冲突：在冲突发生前几小时指出，但没找到替代方案，4/5；只有 Dots 和 Duet 主动发现了冲突。半夜的开放式检查 2/5，回应是重提午餐订单和工作项目 |
| [Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})（TestFlight 早期版本） | 把买勇士队球票交给 Duet 后没有再被提醒，最终没有买成；「Duet 跟踪了任务，但没有把我带回来解决它」 |
| [Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}}) | 认为 Instinct 更主动；评测 Duet 时「它的大部分功能都需要提示」 |
| [Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}}) | 让 Duet 主动挑任务，它选中保险比价跟进，但因没有待办事项只做了总结、没有推进；转述 Reddit 用户称「自动化工作流的实际自主性非常少」、每项任务都要新建导致任务膨胀 |
| [施言：十个海外案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})（转述 Reddit） | 用户让 Duet 每天早上 6 点按简历搜索岗位，推荐中有三个岗位不存在；投递时卡在 Cloudflare 验证码 |

推断：Duet 的主动性目前主要体现在「发现」：晨报和巡检把需要关注的事带到用户面前。对已交出的任务，它缺少按状态主动回来找用户的机制。Claire Vo 希望的是「工作已就绪、权限受阻、需要决定」这类具体的打断，这是她的建议，不是 Duet 已有的能力（[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})）。巡检频率受套餐用量约束，也限制了它能有多及时。

## 资料缺口

- 例程（routines）、定时任务的创建方式、数量与时长上限，失败重试的规则。
- 除定时巡检外是否有事件触发（如新邮件到达即处理）。
- 巡检的具体间隔，用户能否调整、调整后如何计费。
- 数周以上的长期使用记录。

## 主要资料

- 官方：[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})（晨报、巡检间隔、判断仍在调整）、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})（固定间隔、任务标签页、等待批准）、[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})（例程的审批防护）、[产品页]({{< relref "/docs/claude-duet/sources/official/2026-11-05-product-page" >}})（与 Claude 的区别，模拟示例）
- 媒体：[WIRED：六款智能体]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})（日程冲突与开放式检查）
- 社区：[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})、[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})、[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})（跟进与主动性）、[生活有变量]({{< relref "/docs/industry/sources/community/2026-10-30-shenghuoyoubianliang-big-tech-defense" >}})（巡检成本）、[施言：十个海外案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})（岗位搜索案例，二手）
