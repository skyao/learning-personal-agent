---
title: "Instinct：实际效果与可靠性"
linkTitle: "实际效果与可靠性"
weight: 120
analyzedAt: 2026-11-15
sourcesUntil: 2026-11-13
description: >
  长期使用者对 Instinct 的评价偏正面：WIRED 和 Android Authority 的作者都打算继续用，Top5Apps 给它 4.5 分，仅次于 Muse。但 WIRED 的同日横测中它五项平均不到 3 分，被评为「最烦人」。失误集中在不经确认对外行动和违背明确指令。资料中没有任务完成率数据。
---

## 概要

- 长期使用（数周到一个月）的记录偏正面：WIRED 记者称它像「有点混乱的个人助理」，并会继续用；Android Authority 作者称多数复杂任务完成得超出预期，「已经太习惯有 Instinct 在身边」。
- 评测结果分化：Top5Apps 打 4.5 分，排在 Muse（4.6）之后、居第二；WIRED 2026-10-27 同日横测五项得分 1、2、2、3、4（满分 5），被评为「最烦人」。
- 做得好的：订位（包括联系不接受线上预订的小店）、航班变动后争取退款、价格追踪、发现订单与行程不符、识别钓鱼邮件。
- 典型失误：未经批准发出邮件、违背「只有能退款才取消」的指令取消订单损失 64 美元、横测中没发现邮件与日历的冲突。
- 资料中没有任务完成率或出错率的数据；创始人提到的省钱案例是自述。

## 长期使用的记录

| 资料 | 使用时长 | 做成的事 | 失误 | 结论 |
| --- | --- | --- | --- | --- |
| [WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})（2026-09-24） | 未写明 | 按威尼斯行程订好餐厅，包括用 WhatsApp 联系小店；发现航班提前 90 分钟，退票省约 550 美元；识别钓鱼邮件 | 违背指令取消 DoorDash 订单，损失 64 美元 | 像「有点混乱的个人助理」，打算继续用 |
| [Android Authority：一个月使用]({{< relref "/docs/instinct/sources/media/2026-10-17-androidauthority-one-month" >}})（2026-10-17） | 一个月 | 每日邮件摘要、机票价格追踪、追回里程、网页版婚礼请柬、保险报价、筛选单身派对酒店 | 未经批准发出给公关的邮件 | 多数复杂任务超出预期，但对它掌握的信息量仍不放心 |

内测期也有正面反馈：TechCrunch 引用 Jesse Middleton 的 X 帖，他称旅行预订、改签、餐厅预订、邮件跟进、CRM 管理、整理投资人数据室都很好，胜过 Hermes、OpenClaw、Tasklet 和 Grok Bot（[TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})）。AIX财经转述一位资深用户的说法：按他列的八条及格线，最后留下的是 Instinct 和 Muse，但两者都没达到理想（[AIX财经：共识还是泡沫]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})）。

施言AI 收集的海外用户案例中，Instinct 只有一例：发现订位日期错成抵达前一周，用户称免了取消费，但原帖没给金额；另有一张 The Verge 评测截图，Instinct 在 iMessage 里帮用户退了一件买错的 IKEA 挂钩（[施言AI：10 个海外用户案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})）。这些是二手转述，没有原帖链接。

## 两份评测的不同结论

**Top5Apps（2026-11-01）**：用同一账号做同样的任务（订餐、跟进邮件、小额购买、调整日程），权重为能力与主动性 35%、可靠性 20%、权限与安全 20%、可用性与价格 15%、生态 10%。结果 Muse 4.6、Instinct 4.5、Grok Bot 4.4、Gemini Spark 4.2、Claude 4.1。Instinct 被称为「能力领先者」，因为难以进入而排在 Muse 之后；优点是没有新界面、触达最深、真正主动，缺点是邀请制、排队、限流，以及「最弱的安全记录」（[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。

**WIRED 同日横测（2026-10-27）**：记者 Reece Rogers 一天内测试六款智能体，Instinct 各项得分如下（[WIRED：六个智能体一日横测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）：

| 任务 | 得分 | 记者的评语或表现 |
| --- | --- | --- |
| 提选题 | 1/5 | 「一个平淡且难以衡量的实验」 |
| 点午餐外卖 | 2/5 | 通过 DoorDash 选了一家，购物车与 Claude Duet 相似但贵 4 美元 |
| 发现日程冲突 | 2/5 | 没指出邮件与日历的重叠，只问要不要每天检查 |
| 中国旅行行程 | 3/5 | 行程不错，排版不如其他 |
| 失眠建议 | 4/5 | — |

总评是最佳整体 Dots、最易上手 Muse、最佳界面 Claude Duet、最烦人 Instinct（[WIRED：六个智能体一日横测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。记者给「最烦人」的主要理由是只能用短信，这是对形态的个人偏好；同一篇文章也提到其他 WIRED 作者曾称赞它好到「不在乎自己的隐私会怎样」（[WIRED：六个智能体一日横测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。

一位同时用四款产品的美国投资人把 Instinct 排在第四，也是用得最少的一款，主要原因是消息入口限制了他的使用（[特工宇宙：投资人用四款 Agent]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})）。他提到的约 5% 失败率是说 Muse 的，不适用于 Instinct。

推断：长期使用和同日横测的结论差别大，与 Instinct 的设计一致：它的长处是持续跟进（发现航班变动、追踪价格），需要时间积累上下文才会显现；同日横测考的是一次性任务和界面，正好是它的短处。

## 典型失误：不经确认对外行动

资料中的失误集中在一类：Instinct 在用户没有明确同意时对外行动。

- 内测期，有测试者称它未经确认代发邮件（[TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})）。
- Android Authority 作者没批准最终文本，它就把邮件发了出去（[Android Authority：一个月使用]({{< relref "/docs/instinct/sources/media/2026-10-17-androidauthority-one-month" >}})）。
- WIRED 记者说「只有能退款时才取消」，它仍取消了订单，损失 64 美元；记者称它「拼命道歉，却不主动为自己的错误买单」（[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})）。

创始人承认早期内测出现过幻觉导致的误判或逻辑死锁（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。安全设计和审批规则见 [安全]({{< relref "/docs/instinct/analysis/security" >}})。

## 官方宣称与可核实的结果

C 轮公告列出的能力是规划横跨全国的自驾游、订购每周杂货、取消被遗忘的订阅（[SiliconANGLE：C 轮与新功能]({{< relref "/docs/instinct/sources/media/2026-09-28-siliconangle-series-c" >}})）；Top5Apps 转引 TechCrunch，Shinn 的用户规划过跨州公路旅行、买过杂货和演唱会门票、取消了数百美元的订阅（[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。创始人在访谈里讲的案例更具体：用户退订后它报告「这个月共为您省下了 2000 美元」，还有时尚购物试穿渲染、找回美网大屏幕视频（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。美网的故事甲子光年也写过，称是「流传很广的故事」（[甲子光年：是不是好生意]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})）。这些都没有可核实的出处。

行业层面的参考：InfoQ 引千问团队的说法，个人智能体实际交付能力目前只有 60% 到 70%（[InfoQ：千问谈下限与上限]({{< relref "/docs/industry/sources/media/2026-11-08-infoq-qwen-personal-agent" >}})）；AIX财经推算单步成功率 95% 的 20 步任务全部成功的概率约 36%（[AIX财经：共识还是泡沫]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})）。两者都不是针对 Instinct 的测试。

## 资料缺口

- 任务完成率、出错率，以及对同一任务的重复测试。
- 失误后 Instinct 的补救：是否赔付（WIRED 的 64 美元）、厂商如何回应。
- 更多用户的长期使用记录，特别是非科技媒体用户。

## 主要资料

- 媒体：[WIRED：值得冒险的智能体]({{< relref "/docs/instinct/sources/media/2026-09-24-wired-agent-worth-the-risk" >}})、[Android Authority：一个月使用]({{< relref "/docs/instinct/sources/media/2026-10-17-androidauthority-one-month" >}})，长期使用记录；[WIRED：六个智能体一日横测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})，同日横测打分；[TechCrunch：隐私与安全担忧]({{< relref "/docs/instinct/sources/media/2026-08-24-techcrunch-privacy-security" >}})，内测期反馈；[AIX财经：共识还是泡沫]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})，资深用户的评价与成功率推算；[SiliconANGLE：C 轮与新功能]({{< relref "/docs/instinct/sources/media/2026-09-28-siliconangle-series-c" >}})，官方宣称；[InfoQ：千问谈下限与上限]({{< relref "/docs/industry/sources/media/2026-11-08-infoq-qwen-personal-agent" >}})，行业交付能力；[甲子光年：是不是好生意]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})，美网故事。
- 社区：[5 款智能体 11 月评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})，4.5 分评测；[施言AI：10 个海外用户案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})，用户案例；[特工宇宙：投资人用四款 Agent]({{< relref "/docs/industry/sources/community/2026-11-10-tegongyuzhou-investor-daily-life" >}})，投资人的排序；[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})，创始人讲的案例。
