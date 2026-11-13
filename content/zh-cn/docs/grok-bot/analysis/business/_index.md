---
title: "Grok Bot：商业与规模"
linkTitle: "商业与规模"
weight: 110
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Grok Bot 不单独收费，捆绑在 X、Cursor 和 SuperGrok 的订阅里，用量超出部分按量计费，同时以 Team Bots 和 Enterprise 功能面向企业；规模数字只有官方的「数千家组织」「数百万个 Bot」和第三方的日活估计，Musk 在 2026-11-01 承认服务成本相对收入「高得不可持续」并收紧了用量。
---

## 概要

- Grok Bot 没有单独的订阅，随 The X Subscription、Cursor 订阅和 SuperGrok 捆绑提供，超出每周用量池的部分走预付额度；企业侧靠 Team Bots 和 Enterprise 专有功能（审计日志、Conversation Insights、推理钩子等）收费。
- 规模数据都不是官方的用户数或收入：官方只说「数千家组织采用」「过去几周创建了数百万个 Bot」；日活「9 月初不足 10 万、10 月底超过 60 万」出自第三方追踪，经财联社和中文自媒体转述。
- 成本压力有明确的一手记录：据 TechCrunch，Musk 2026-11-01 在 X 上称提供 Grok Bot 服务的成本相对收入「高得不可持续」，随后收紧了每周用量限制。
- 官方用大量内部用例（客服、采购、数据分析、销售）证明商业价值，数字都是厂商自述：客服工单量增长 175% 未加人手，采购找出超过 100,000 美元的节省。
- Grok Bot 依托 SpaceX 对 Cursor 的收购：账号、计费和文档都在 Cursor 体系内；SpaceX 文件称 AI 占公司收入 52%，但资料中没有 Grok Bot 单独的收入。

## 不单独收费，随订阅捆绑、超额按量计费

据多款产品成本对比文章引述的 xAI 文档，Grok Bot 没有单独的订阅，随 The X Subscription、Cursor 订阅或 SuperGrok 提供；在 The X Subscription 上，Grok Bot 与 Cursor、Grok app 共用同一个每周用量池，超出部分用预付额度按量计费。xAI 称 Premium 档带有「SuperGrok、Cursor Pro 和 X Premium+ 的权益，此前合计每月 90 美元」（[成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})）。官方帮助文档对用量只写「努力为你提供最佳的性价比」，用量取决于任务类型，不披露成本结构（[模型帮助]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-models" >}})）。各档价格和额度的细节见[开放与价格](../access-pricing/)。

团队方面，官方 FAQ 写明：自助 Cursor Teams 的每个成员自动获得 Grok Bot，「无需 Premium 席位或管理员申请」；The X Subscription 的团队每个付费席位都包含 Grok Bot（[xAI 文档 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})）。更新日志写明，队友使用 Team Bot「会从其自己的额度中扣除」（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

推断：把 Grok Bot 放进已有订阅，而不是单独定价，等于用它拉动 X、Cursor、SuperGrok 三条订阅的升级；多略功导的文章也提出同样的框架：不单独收费可以，但必须给平台带来收入增量（[多略功导]({{< relref "/docs/industry/sources/community/2026-11-08-duolue-business-essence" >}})）。资料中没有升级转化的数据，这一点无法验证。

## 企业版：Team Bots 与管理功能

Grok Bot 从一开始就同时面向个人和组织。官方 2026-09-03 的企业文章称，发布以来已有「数千家组织」采用，包括 Legora、Supermicro 和 ServiceTitan，并称过去几周创建了「数百万」个 Bot，使用最密集的场景在工程之外（[面向企业]({{< relref "/docs/grok-bot/sources/official/2026-09-03-grok-bot-for-enterprise" >}})）。这些是厂商的说法，没有给出口径。

Team Bots 是企业侧的核心形态：管理员可以发布、共享和限制 Bot，Enterprise 管理员能在 Conversation Insights 中看到团队最常用的 Grok Bot 用例（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。推理钩子只面向 Enterprise，用于接入第三方安全厂商（[推理钩子文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-inference-hooks" >}})）。官方 Team Bots 文章引用了两位客户：保险公司 Harper 的 CEO 称 24 小时内搭建的 Team Bot「从数百份保单中为客户节省了超过 120,000 美元」；Amplitude 的市场负责人称正为各个市场职能构建 Team Bot（[Team Bots]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}})）。

模板和 Marketplace 是另一条扩散路径：Bot 可以作为模板共享给团队或任何人；Marketplace 一度列出 Bot，后来改为专注插件，Bot 模板转到网页（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})、[模板指南]({{< relref "/docs/grok-bot/sources/official/2026-09-08-guide-templates" >}})）。资料中没有 Marketplace 的分成或收费安排。

## 厂商用内部用例证明价值

官方发布稿称 Grok Bot 最初是内部原型，「在整个公司迅速流行起来」（[官方发布]({{< relref "/docs/grok-bot/sources/official/2026-08-11-introducing-grok-bot" >}})）。据 Cybernews，Grok Bot「最初是为 SpaceXAI 内部使用而创建的」，用于对外销售、市场活动、办公运营和缺陷修复（[Cybernews]({{< relref "/docs/grok-bot/sources/media/2026-10-07-cybernews-bank-data-slack" >}})）。官方博客随后发了一系列内部用例，数字均为厂商自述，没有第三方核实：

| 场景 | 官方称的效果 | 资料 |
| --- | --- | --- |
| 客服 | Cursor 8 月 14 日并入 SpaceXSI 后，合并团队工单量增长 175%，未新增人手，否则可能要多招 200 人；传统 AI 客服每次解决收费 1 到 4 美元，他们每张工单约 0.20 到 0.30 美元；每天综合超过 20,000 条产品反馈 | [客服实践]({{< relref "/docs/grok-bot/sources/official/2026-09-22-grok-bot-customer-support" >}}) |
| 采购 | 找到超过 100,000 美元的直接节省；一款产品 43 个付费席位 90 天无活动，节省 14,220 美元；另一产品每年 85,662 美元闲置 SKU；办公用品订单从 14,629 美元降到 6,143 美元 | [采购实践]({{< relref "/docs/grok-bot/sources/official/2026-09-04-grok-bot-procurement" >}}) |
| 数据分析 | Data Bot 上周承担了约 70 小时原本落到数据科学团队的工作（作者估计） | [Data Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-02-data-bot" >}}) |
| 工程 | 一个五人团队每天发布超过 100 个 PR，几周内推出 Team Bots | [Team Bots]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}}) |

推断：这些文章的作用更接近企业销售材料，重点是「省人、省钱」的单位经济，而不是个人用户场景；这与多略功导的判断一致：数字员工在「职责明确、任务重复、结果容易验收」的场景更容易先成立（[多略功导]({{< relref "/docs/industry/sources/community/2026-11-08-duolue-business-essence" >}})）。

## 规模：只有第三方日活与官方的模糊说法

| 指标 | 数字 | 口径与出处 |
| --- | --- | --- |
| 组织数 | 「数千家组织」 | 官方，2026-09-03（[面向企业]({{< relref "/docs/grok-bot/sources/official/2026-09-03-grok-bot-for-enterprise" >}})） |
| Bot 数 | 「过去几周创建的数百万个 Bot」 | 官方，2026-09-03，同上 |
| 日活 | 9 月初不足 10 万，10 月 26 日超过 60 万 | 黑咖啡转述财联社 10 月 31 日报道（[黑咖啡]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})）；多略功导写作「据第三方追踪」「10 月底超过 60 万」（[多略功导]({{< relref "/docs/industry/sources/community/2026-11-08-duolue-business-essence" >}})） |
| 下载与付费 | 上线两个月全球下载 220 万+、周付费用户 80 万 | 自媒体科普文章，收录说明写明文中数字未给出处（[AI问消]({{< relref "/docs/industry/sources/community/2026-11-09-aiwenxiao-personal-agent-family-tree" >}})） |
| 用户讨论声量 | 声量份额 25.0%、好感 0.485、综合 57.9，12 款中第 3；直接比较中 69% 的帖子选 Grok Bot 而非 dots | Enterpret Feedback Bench，2026-08-31 至 11-01 共 277,038 条公开帖子；文中称其「高分来自触达」（[Enterpret]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})） |

两个日活数字同出一源（财联社 / 第三方追踪），不是相互独立的证据。「周付费用户 80 万」没有出处，日活 60 万与周付费 80 万放在一起也难以对上，不应采信。

增长的定性说法来自 Musk 本人：据 TechCrunch，他称 Grok Bot 拥有「我这辈子见过的产品中最快的增长」（[TechCrunch]({{< relref "/docs/grok-bot/sources/media/2026-11-02-techcrunch-throttles-limits" >}})）；多略功导称他 10 月 24 日在 X 上说智能体需求的增长速度超过他见过的任何增长，并强调「除了试用，它几乎没有免费层」（[多略功导]({{< relref "/docs/industry/sources/community/2026-11-08-duolue-business-essence" >}})）。

投放方面，AppGrowing 的广告数据显示 Grok Bot 已进入投放，但处在「稳定期」，素材迭代比 Muse 慢，以创作者证言和产品演示为主（[AppGrowing]({{< relref "/docs/industry/sources/community/2026-10-28-appgrowing-user-acquisition" >}})）。

## 成本「高得不可持续」与 2026-11-01 收紧用量

据 TechCrunch 2026-11-02 的报道，万圣节周末一些用户发现每周用量意外被用满，有用户报告从 50% 跳到 100%。Musk 周日（11-01）在 X 上回复用户时确认这不是故障，并写道：「相对收入而言，提供 Grok Bot 服务的成本高得不可持续」。截至报道时，Musk 未说明今后用量限额如何调整（[TechCrunch]({{< relref "/docs/grok-bot/sources/media/2026-11-02-techcrunch-throttles-limits" >}})）。Enterpret 的数据也显示，Grok Bot 用户「撞上了上限」，仅用量限制一项就占其用户全部发言的 14%，「为智能体付费」一项排名垫底（[Enterpret]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})）。

推断：捆绑定价让用户按订阅价获得常驻、可并行运行的多个 Bot，而成本随运行量增长；在没有独立定价的情况下，厂商能调的主要是用量池。11-01 的收紧说明这一机制已经触及上限。客服文章里每张工单 0.20 到 0.30 美元的说法是内部用例的成本，不能推及个人用户的整体成本。

## 背后的母公司：SpaceX、Cursor 与 X

据 TechCrunch，SpaceX 上月的文件称 AI 占公司收入的 52%，更名后的「Super Intelligence」部门实现了 4.31 亿美元利润，若不是与收购 Cursor 相关的 12 亿美元一次性成本，利润会更高（[TechCrunch]({{< relref "/docs/grok-bot/sources/media/2026-11-02-techcrunch-throttles-limits" >}})）。这一收入口径是整个 AI 业务，不是 Grok Bot 单独的数字。

官方客服文章写明 Cursor 于 8 月 14 日并入 SpaceXSI（[客服实践]({{< relref "/docs/grok-bot/sources/official/2026-09-22-grok-bot-customer-support" >}})）。程序员鱼皮的文章称 SpaceX 以 600 亿美元完成收购，Grok Bot 的账号、计费和云电脑都跑在 Cursor 体系上（[鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})），其中 600 亿美元的金额没有注明出处。

Musk 还在 2026-10-15 回复亚马逊拦截 Grok 购物 Bot 一事时说「也许我们应该创办一个亚马逊的竞争对手」；Not a Tesla App 写明这不是正式宣布（[Not a Tesla App]({{< relref "/docs/grok-bot/sources/media/2026-10-15-notateslaapp-amazon-blocked" >}})）。资料中没有 Grok Bot 交易抽佣或电商收入的任何信息。

## 对商业前景的看法

- 一位产品负责人在一手使用记录中称「这里护城河在哪里仍然非常不清楚」（[James Pember]({{< relref "/docs/grok-bot/sources/community/2026-10-04-james-pember-grok-bot-is-really-good" >}})）。
- 「AI应用与大模型」的文章认为，订阅之外能否形成交易收入、「能否覆盖持续运行的成本，仍是下一阶段的问题」（[AI应用与大模型]({{< relref "/docs/industry/sources/community/2026-11-01-aiyingyong-grok-muse-dots" >}})）。
- AIX财经把 Grok Bot 归为模型公司路线，认为它「与X深度结合，更适合内容、运营和调研任务」，并指出 Personal Agent 的推理成本可能高于编程 Agent（[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})）。

以上都是资料作者的观点，不是数据。

## 资料缺口

- 官方的用户数、日活、付费人数、Grok Bot 单独的收入；「数千家组织」「数百万个 Bot」的口径。
- 日活 10 万到 60 万的一手出处（财联社原报道及其数据来源）；「周付费用户 80 万」「下载 220 万+」的出处。
- 11-01 收紧用量后的官方说明：新限额、是否调价、是否有补偿。
- 单个用户的服务成本、各档订阅中 Grok Bot 的成本占比；Enterprise 定价。
- SpaceX 收购 Cursor 的金额与条款的一手出处；SpaceX 文件中 AI 收入的构成。
- 企业客户（Legora、Supermicro、ServiceTitan 等）的独立案例或采访。

## 主要资料

官方

- [官方发布]({{< relref "/docs/grok-bot/sources/official/2026-08-11-introducing-grok-bot" >}})：内部原型起源。
- [面向企业]({{< relref "/docs/grok-bot/sources/official/2026-09-03-grok-bot-for-enterprise" >}})：组织数、Bot 数、企业用例。
- [Team Bots]({{< relref "/docs/grok-bot/sources/official/2026-09-28-team-bots" >}})：客户引述、内部工程用例。
- [客服实践]({{< relref "/docs/grok-bot/sources/official/2026-09-22-grok-bot-customer-support" >}})、[采购实践]({{< relref "/docs/grok-bot/sources/official/2026-09-04-grok-bot-procurement" >}})、[Data Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-02-data-bot" >}})：内部用例与节省数字。
- [xAI 文档 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-faq" >}})、[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})、[推理钩子文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-inference-hooks" >}})：团队计费与 Enterprise 功能。

媒体

- [TechCrunch]({{< relref "/docs/grok-bot/sources/media/2026-11-02-techcrunch-throttles-limits" >}})：用量收紧、Musk 原话、SpaceX AI 收入。
- [Not a Tesla App]({{< relref "/docs/grok-bot/sources/media/2026-10-15-notateslaapp-amazon-blocked" >}})：Musk 关于亚马逊竞争对手的回复。
- [Cybernews]({{< relref "/docs/grok-bot/sources/media/2026-10-07-cybernews-bank-data-slack" >}})：产品的内部起源。

社区

- [成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})：捆绑方式与用量池。
- [黑咖啡]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})、[多略功导]({{< relref "/docs/industry/sources/community/2026-11-08-duolue-business-essence" >}})：日活转述与单位经济框架。
- [Enterpret]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})：用户讨论声量与用量限制抱怨。
- [AppGrowing]({{< relref "/docs/industry/sources/community/2026-10-28-appgrowing-user-acquisition" >}})：投放状态。
