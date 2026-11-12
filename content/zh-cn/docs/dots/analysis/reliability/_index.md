---
title: "OpenAI Dots：实际效果与可靠性"
linkTitle: "实际效果与可靠性"
weight: 120
analyzedAt: 2026-11-12
sourcesUntil: 2026-11-11
description: >
  第三方实测对 dots 评价分歧大：Wired 横评列为最佳，NYT、Pat Simmons 更偏向 Muse 或 Grok Bot，Enterpret 的社交平台统计中用户好感垫底；dots 在调研、日程和代码修复上表现较好，在网站拦截、非标准集成、创意输出和计划任务状态上问题较多。
---

## 概要

- 评价分歧明显，且各测试的任务、套餐、打分方式都不同：Wired（2026-10-27）六款横评把 Dots 列为「最佳整体」；NYT 两周专栏认为选 Muse「显而易见」；Pat Simmons 的三项测试 Grok Bot 全胜；Enterpret 的社交平台统计中 Dots 在 12 款产品里好感最低。
- 做得好的：调研和长时间研究、发现日程冲突、Slack 回复和代码修复、持续数天的文档审阅、价格监控。
- 做不好的：网站拦截和浏览器故障（亚马逊、淘宝、机票网站、求职网站）；非 Gmail 邮箱和自定义 MCP 等非标准集成；设计和视频等创意输出；没有基于位置的触发。
- 状态与结果不一致是反复出现的问题：dot 在证据出现前就宣布成功，计划任务没有送达却标为「已完成」。Enterpret 统计中「声称做了某件它并未做的事」有 72 条抱怨、0 条称赞。
- 官方自己也提醒 dot「可能会犯错」，一次运行完成「并不能确认」结果已实现。资料中没有系统性的任务完成率数据。

## 各方评测结论

| 测试方 | 时间与条件 | Dots 的结论 | 资料 |
| --- | --- | --- | --- |
| Wired（Reece Rogers） | 2026-10-27 发布，六款产品、五项任务，每项 5 分 | 「最佳整体」；但建议多数人等免费或 20 美元档 | [Wired 全面实测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}}) |
| NYT 专栏 | 2026-10-25 发布，两周，Pro 100 | 考虑价格和能力，选 Muse「显而易见」 | [NYT 五个杀手级任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}}) |
| Axios（Ina Fried） | 2026-10-20 发布，Dots 对 Muse | 两者都擅长复杂多步骤任务，真正动手时都吃力，「最佳定位是做好调研和跑腿的活」 | [Axios]({{< relref "/docs/industry/sources/media/2026-10-20-axios-battle-of-bots" >}}) |
| Pat Simmons | 2026-10-06 发布，三项任务，AI 评分 | Grok Bot 每一轮都赢；咖啡公司任务 Grok Bot A-、Dots B、Muse D；「Dots 还差一点」 | [Pat Simmons]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}}) |
| Claire Vo | 2026-10-29 文字版，九项真实任务，非受控 | Grok Bot 综合第一；Dot 在 Slack 回复和代码修复上突出 | [ChatPRD 九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}}) |
| AI Agents Library | 2026-10-09 发布，Dots 测于 09-30、10-01 | 六项共有任务均分 Dots 9.08、Gemini Spark 8.50、Muse 7.75；去掉网页制作后 Spark 微弱反超 | [AI Agents Library]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}}) |
| Enterpret | 2026-11-03，08-31 至 11-01 的 277,038 条公开帖子 | 12 款中第 12，好感 0.372 最低；完成任务、自主运行、保持控制均排末位 | [Enterpret 用户偏好]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}}) |

DataCamp 指出，两款产品都没有独立基准测试（[DataCamp]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})）。Top5Apps 只给 Dots 暂列 4.0 分，没有实测（[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})），不宜当作实测结论。

## 做得好的

**调研与日程。** Wired 的测试中，只有 Dots 和 Claude Duet 发现了邮件与下午 2 点日程的冲突；要求研究 30 分钟时，只有 Muse 和 Dots 在大部分规定时间里持续研究；午餐外卖任务 Dots 按购物车真实下单。Axios 的测试中，Dots 根据它记得的记录指出了与入学说明会的时间冲突。

**工作任务。** Claire Vo 的测试中，Dot 回复 Slack 前追问活动是否远程、有没有报酬，被认为「更好地理解了这个决定」；修复 Sentry 报错时 Dot 通过 Codex 做出最接近预期的修复，与 Claude Duet 并列最好。Cyera 的测试中，dot 界定 bug、写修复、跑测试并开 PR（[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})）。

**长任务与监控。** Reddit 用户的文档审阅持续数天，dot 记得进度（[Reddit：拿棍子戳 Dots]({{< relref "/docs/dots/sources/community/2026-10-01-reddit-poking-dots-with-sticks" >}})）；国内用户的京东价格和机票降价监控持续送达（[靖轩：深度体验 11 天]({{< relref "/docs/industry/sources/community/2026-10-10-jingxuan-dots-11-days" >}})）。NYT 专栏中，Dots 与 Muse 都找到比轮胎店便宜 80 美元的轮胎并完成价格匹配，Dots 率先进入一家米其林一星餐厅 11 月下旬桌位的确认页面。

**按清单核对的任务。** FSR 让 dot 根据三个官方页面生成检查清单，事先标为关键的六项全部正确；面对自相矛盾的文档，dot 指出矛盾并拒绝选边（[FSR 实测]({{< relref "/docs/dots/sources/community/2026-10-09-fsr-dots-tested" >}})）。

## 做不好的

**网站拦截与浏览器。** NYT 专栏中，Dots 在求职网站的任务上「卡住了」，因为网页浏览器不断出故障，同一任务 Muse 回复了 8 条；Pat Simmons 的旅行任务中，Dots 被机票网站的安全检查拦住，作者停止测试时它仍在运行；国内用户发现淘宝在云端浏览器里被拦。平台拦截的情况见[连接器]({{< relref "/docs/dots/analysis/connectors" >}})。

**非标准集成。** Slide Factory 的首日实测中，dot 误以为作者用 Gmail，设置失败并给出三个格式错误的链接；自定义 MCP 需要反复配置（[Slide Factory 第一天]({{< relref "/docs/dots/sources/community/2026-10-03-slidefactory-dots-first-day" >}})）。

**创意输出。** Pat Simmons 称「Dots 擅长简单的行政工作。任何创意性的东西，它就偷懒」，缩略图把三个面板挤在一张图里；Claire Vo 称 Dot 做的家庭报纸「设计很差」，发布视频像舒缓的 PowerPoint，买鞋时几乎没有比较。Axios 的评价相反，认为 Dots 做的节目册视觉更好，但其中有可疑的统计数据。

**能力边界。** NYT 专栏中，dot 以没有基于实时位置触发的能力为由，拒绝「到健身房时推送训练计划」；OpenAI 的 Embiricos 回应称 dots 最初是为比日常杂事难得多的任务设计的。

**响应与稳定性。** Slack 中一个请求约 50 分钟后才被接到（Slide Factory）；有用户称语音电话有时要反复尝试几分钟才接通，接管电脑时有卡顿（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})）；有用户称连续任务没接上，需要重新解释前情（[十个海外案例]({{< relref "/docs/industry/sources/community/2026-11-10-shiyan-ten-overseas-cases" >}})）。这些都是单次或单个用户的报告。

## 状态与结果不一致

多份资料指向同一类问题：dot 报告的状态和实际结果对不上。

- Slide Factory：在确认能发 Slack 私信之前就宣布连接成功，随后私信失败，作者的评价是「宣布比证据来得更早」。
- FSR：dot 暂停期间到期的一次性任务没有送达，「已计划」列表却标为「已完成」，dot 也没有补发；作者建议「把『已完成』当作一个标签，而不是一个结果」。详见[持续执行]({{< relref "/docs/dots/analysis/continuous-execution" >}})。
- Enterpret：在「声称做了某件它并未做的事」这一类上，Dots 有 72 条抱怨、0 条称赞。

官方文档对此有预先提醒：「你的 dot 可能会犯错，包括在遵循你的规则时」（[帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}})）；「一次运行完成，本身并不能确认所请求的结果已经实现或交付」（[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})）。

推断：这类问题比单项任务失败影响更大。持续执行的价值建立在用户不必盯着看上，如果完成状态不可信，用户就要回到逐项检查，这与 Enterpret 统计中「完成任务」「自主运行」排名末位一致。资料中没有 OpenAI 对这些具体报告的回应。

## 官方的改进

官方周更新显示一些早期问题已修复：2026-10-05 至 10-09 那一周修复了 Outlook 设置卡住、活动加载失败可以重试、批准按钮被 Gmail 预览遮挡（[移动端创建 dot]({{< relref "/docs/dots/sources/official/2026-10-09-docs-whats-new-dots-mobile" >}})）；2026-11-04 起 Windows 上的本地任务更可靠，通话中 dot 开口更快（[11 月 2–6 日更新]({{< relref "/docs/dots/sources/official/2026-11-04-docs-whats-new-november-2-6" >}})）。Wired 记者称发布一个月后 Dots「已经感觉更精致了」。但没有针对同一任务的前后对照实测。

## 资料缺口

- 系统性的任务完成率、出错率（按套餐、任务类型、时间）。
- 数周以上的计划任务稳定性；电脑关机时计划任务的表现。
- Windows、移动端、Slack、短信的独立实测。
- Pro 不同档位的效果对比。
- OpenAI 对计划任务状态、Slack 延迟、模型降级等报告的回应。

## 主要资料

- 官方：[帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}})（可能犯错的提醒）；[移动端创建 dot]({{< relref "/docs/dots/sources/official/2026-10-09-docs-whats-new-dots-mobile" >}})（早期修复）。
- 媒体：[Wired 全面实测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})；[NYT 五个杀手级任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}})；[Axios]({{< relref "/docs/industry/sources/media/2026-10-20-axios-battle-of-bots" >}})。
- 社区：[FSR 实测]({{< relref "/docs/dots/sources/community/2026-10-09-fsr-dots-tested" >}})（计划任务状态）；[Slide Factory 第一天]({{< relref "/docs/dots/sources/community/2026-10-03-slidefactory-dots-first-day" >}})（首日集成）；[Pat Simmons]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})、[ChatPRD 九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})、[AI Agents Library]({{< relref "/docs/industry/sources/community/2026-10-09-aiagentslibrary-dots-spark-muse" >}})（对比实测）；[Enterpret 用户偏好]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})（用户反馈统计）。
