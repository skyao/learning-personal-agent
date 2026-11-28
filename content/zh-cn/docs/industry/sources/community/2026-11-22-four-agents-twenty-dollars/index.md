---
title: "20 美元，四家智能体，工作量天差地别"
linkTitle: "20 美元四智能体对比"
date: 2026-11-22
originalTitle: "Four Agents, One $20 Bill, and Very Different Amounts of Work"
sourceUrl: "https://aihomebuilding.com/stories/muse-vs-chatgpt-claude-gemini-personal-agent-2026"
author: "Jake Kowalski"
publisher: "AI Home Building"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-22
tags: [开放与价格, 持续执行]
products: [muse, claude-duet, gemini-spark]
---

{{< source-info >}}

**收录说明**：直接下载全文，原文全文存于本目录的 original.md，网站上不显示，已翻译。文中比较的 ChatGPT Work 是 ChatGPT 应用内的智能体模式，并非 OpenAI 的 dots 产品，products 仅列 muse、claude-duet、gemini-spark。作者声明未对 ChatGPT Work、Claude、Gemini 做一手实测，所有结论来自厂商文档与经核对的二手报道；“每项重任务消耗 500 万 token”仅为示意假设，非实测数字。文中的四产品对照表按原文保留。

**内容摘要**：文章以 20 美元档为比较基准，对比 Muse、ChatGPT Work、Claude、Gemini 四款个人智能体的计量方式：Muse Power 每周 5 亿 token（约合每月 20 亿）、ChatGPT Plus 每月 40 条 agent 消息、Claude Pro 以五小时会话加每周上限计量且与日常对话共用额度、未公布消息或任务数，Gemini 则自 2026 年 11 月 17 日起在美国及加拿大、澳大利亚、印度、日本、韩国免费提供每日一次定时任务。按作者的换算，ChatGPT 一个每日定时任务约消耗 30 条消息，基本占满整月额度；而即使按每项重任务消耗 500 万 token 的示意假设估算，Muse 每周额度也可支撑约 100 项重任务、每月约 400 项。Gemini 免费的代价是最多 10 个有效定时任务、定时提示在设定时间一小时内执行（作者引用的实测称早上 7 点的简报可能 8 点才到），且仅限个人 Google 账号使用；其 19.99 美元/月的 Pro 档增加每小时定时及 Gmail 与新闻触发器。功能层面，Muse 是四者中唯一自带常驻电脑（Secure VM，含终端、文件系统与实时 Chromium 浏览器）的一款，并于 2026 年 11 月 12 日为付费用户增加了向美国商家拨打电话的能力，由首席 AI 官 Alexandr Wang 宣布。作者明确限定方法：未对 ChatGPT Work、Claude、Gemini 做一手实测，且结论是应按计量结构与自身生态选产品，而非按功能清单。

**保留理由**：四款主流个人智能体同价位计量方式的罕见正面横向对比，含对照表与明确的方法限定；其中 Muse 每周 5 亿 token 与电话代打、Gemini 免费定时任务等事实与 Muse 跟踪直接相关，且“按计量结构选型”的结论对理解 Muse 的定价竞争力有参考价值。

---

你有二十美元。四家公司想要它，而四家都在卖你同一句话：一个在你睡觉时干活儿的个人智能体。Meta 称它为 Muse，OpenAI 称它为 ChatGPT Work，Anthropic 称它为 Claude。Google 称之为 Gemini 里的「tasks（任务）」，它以前叫 Spark——这告诉你，在你还没读完价目表之前，这个市场跑得有多快。

同样的价格。同样的承诺。实际能干多少活却天差地别，因为四家的计量方式不一样，而计量方式正是这笔交易成败所在。一家按周卖你 token，一家按月卖你消息条数，一家卖你五小时会话——你下午聊天也会从里面扣。还有一家刚在美国把整件事变成免费，代价是你早上 7 点就会感受到：你的简报 8 点才到。

所以我读的是文档——不是发布会的主题演讲，而是帮助页面和定价页面，那些用小字印着限制的页面——并且做了四家厂商都不会替你做的那个计算：二十美元到底买到什么，用唯一对过日子的人有意义的单位来量，也就是无需你盯着也会发生的定时任务。

## 先算账，再挑吉祥物

从 ChatGPT Plus 开始，因为它的计量最诚实，也最残酷。OpenAI 自己的帮助中心说 Plus 每月有 40 条智能体消息，每一次独立的智能体调用都计入这个数字，包括定时任务内部的调用。一个每日定时任务——早晨简报、收件箱清扫、日历检查——每月大约消耗 30 次调用。这样全月你让智能体做的其他所有事只剩 10 条消息，也就是说一个每日任务就吃掉了整份订阅。第二个每日任务放不下，而且不跳到 Pro（现在每月 100 美元起）就无法多买消息。

Muse Power 同样是二十美元，但按 token 计量：每周 5 亿 Muse token，约合每月 20 亿，见 Meta 的订阅帮助页面。Meta 没有公布从 token 到完成任务的换算，其用量页面直说：一个任务消耗多少随功能、请求和模型层级而异，且没有任何固定用量能保证固定产出。所以没有一个诚实的人能告诉你 5 亿 token 究竟能买多少个任务，但规模仍然说明问题。即使你假设一个重度的定时任务——大量浏览和推理——消耗 500 万 token，一周的额度也能覆盖 100 个这样的任务。ChatGPT 给你每月 40 次调用，而 Muse 每月大约能给 400 个重任务留出空间——如果这个 token 估算成立的话，而这个估算是刻意给得宽松的。

Claude Pro 也是二十美元，其计量是四者中最不透明的。Anthropic 以五小时会话加每周上限的方式出售用量，而你的定时任务与下午的聊天从同一个池子里取用。每月 100 美元的 Max 得到 Pro 用量的五倍，200 美元的 Ultra 得到十倍，但 Anthropic 在任何地方都没有公布消息数或任务数，所以在 Claude 上给定时工作做预算，就是在一个厂商不肯印出来的数字上猜。这不是产品的缺陷，而是价签的缺陷，而且很要紧，因为跑每日报告的人需要知道那份报告到 28 号还能不能跑。

Gemini 完全打破了这个模式，因为 2026 年 11 月 17 日，Google 在美国以及加拿大、澳大利亚、印度、日本和韩国把 Gemini 里的 tasks 变成免费，并包含每天一次的定时。每月 19.99 美元的 Google AI Pro 增加每小时定时以及 Gmail 和新闻触发器。一份每日早晨简报——现存最常见的定时任务——目前在 Gemini 上花费零美元。这是市场上最便宜的定时任务，整整便宜二十美元一个月。

没有代价的免费是不存在的，而 Gemini 的代价很具体。你最多有 10 个生效的定时动作。Google 说定时提示在你设定时间的一小时内运行，而不是在你设定的那一分钟——一位实测者发现，这意味着早上 7 点的简报可能 8 点才到，赶早会就没用了。而且任务只在个人 Google 账号上运行，所以收件箱在公司或学校账号上的人完全被挡在门外。便宜，但只在 Google 家里，而且只在你不在意智能体迟到一个小时的前提下。

继续之前还有一个数字：在每月 100 美元那一档，四家中有三家正好汇合到每年 1200 美元——Muse Maximum、ChatGPT Pro 100 和 Claude Max——所以真正的选择在 20 美元档，而不是 100 美元档。Gemini Ultra 的定价本文未核实，宁可不写也不猜。

## 同样的价格，四台不同的机器

价格是一个轴。智能体实际建立在什么之上是另一个轴，而在这里四家分得更开。

Muse 是四者中唯一自带常驻电脑的——一台含终端、文件系统和实时 Chromium 浏览器的 Secure VM，外加技能、定时工作和消息界面。它不借你的笔记本电脑，也不要求你一直开着一个桌面应用。2026 年 11 月 12 日，Meta 为付费订阅者增加了向美国商家拨打外线电话的能力，由首席 AI 官 Alexandr Wang 宣布，所以 Muse 现在可以代你给餐厅或 DMV 办事处打电话。二十美元档没有对手提供这样一台常驻机器。

ChatGPT Work 是办公室机器。OpenAI 于 2026 年 7 月 9 日砍掉了 Atlas 浏览器，把整个东西折进一个桌面应用，含 Chat、Work 和 Codex 三种模式，由 GPT-5.6 驱动。Work 从你连接的各个应用收集材料，做成成品幻灯片、表格和文档，并且可以在一个项目上连续待几个小时。它的云浏览器保留自己的登录状态，与你自己的浏览器分开；需要登录时，智能体暂停，把浏览器交给你接手，你输入密码时截图关闭。就产出精致的成品工作物而言，这个对比里没有别的能与之相比；就配给之紧而言，也没有别的能与之相比。

Claude 是谨慎的那个，而在这里「谨慎」是褒义，虽然它同时也是一道速度限制。Anthropic 自 2026 年 9 月 16 日起把 Cowork 智能体模式并入 Claude，其自家文档说智能体优先用连接器，其次用浏览器，最后才动用你的屏幕。桌面应用里的计算机使用仍处于 beta。每个付费计划都附带 Claude Code，这使 Claude 成为本组中对工作存放在文件和代码里的人最好的智能体。定时任务在云端运行，合上笔记本也行，除了需要本地文件或应用的任务。

Gemini 是本地的那个，住在大多数人已经拥有的 Google 账号里，通过一次连接读取 Gmail、Calendar、Drive 和 Docs；自 2026 年 11 月 19 日起，Mac 版 Gemini 应用可以在一个隔离的后台窗口中跨本地应用自动化杂务，关键操作前有实时预览和批准。Google 还增加了给商家打电话，以及在设定的消费上限内用 Google Pay 结账。如果你的生活本来就是一个 Google 账号，Gemini 就是你和工作之间距离最短的那个智能体。

| 20 美元档 | Muse | ChatGPT Work | Claude | Gemini |
| --- | --- | --- | --- | --- |
| 月费 | 20 美元（Power） | 20 美元（Plus） | 20 美元（Pro） | 美国 0 美元 / Pro 19.99 美元 |
| 工作量如何计量 | 每周 5 亿 token | 每月 40 条智能体消息 | 五小时会话，与聊天共用 | 10 个生效动作；每日免费，每小时需 Pro |
| 免费档能做智能体工作吗 | 能，上限未公布 | 不能，智能体模式付费 | 不能，定时仅限付费 | 能，每天一次定时 |
| 定时工作 | 有 | 有，每日/每周/每月 | 有，每小时/每日/每周 | 有 |
| 自有常驻电脑 | 有，Secure VM | 云浏览器；本地使用可选 | 云端；本地需开着桌面应用 | 云端；本地应用需 Mac 应用 |
| 代你给商家打电话 | 有，付费美国用户，2026-11-12 | 智能体文档中无 | 无 | 有，美国 |
| 购物 | 有，钱包结账 | 通过浏览器，由你登录 | 通过浏览器/连接器 | 在你设定的上限内用 Google Pay |

## 今晚该做什么

按计量和你的地盘来选，而不是按本周的功能清单。如果你想让一打后台任务跑起来，Muse 的 token 额度是唯一不按消息配给的二十美元。如果你生活在 Google Workspace 里，只想要一份早晨简报，Gemini 免费就能做，在别处为同样的简报付二十美元等于捐款。如果你的工作是文档和幻灯片，ChatGPT Work 产出的成品最好，但要为 40 条消息的上限做预算——这意味着一个每日任务，几乎什么也剩不下——或者接受跳到每月 100 美元的 Pro。如果你的工作是代码和文件，Claude 是谨慎的选择，而你应该在承诺之前测试一周的定时任务是否会与下午的聊天相撞，因为共用池让这种相撞直到发生前都不可见。

而且在订阅任何一家之前，做一个不花钱的测试。安排一个每日任务——早晨简报或收件箱清扫——观察它一周。数一数它实际跑成了几个早晨、有几次需要你、以及按厂商计量的那种货币花了多少。那一周告诉你的，比任何对比文章都多，包括这一篇。

## 为什么这个对比可能为时过早

这是对上述一切的最强反驳，以全力陈述。四款产品在过去六周里都有实质变化：Gemini 在 11 月 17 日转为免费，Muse 在 11 月 12 日增加了打电话，Claude 在同一天完成 Cowork 的合并。ChatGPT Pro 在 10 月拆成三个档位，而 9 月新付 200 美元的订阅者在同样价格下拿到了更低的额度。按今天的表格选型的买家，可能买的是上个月的产品；一张在 11 月 22 日准确的表格，到 1 月就可能出错——这恰恰说明整个练习是对一条河的快照，而不是一条路的地图。

这个反驳是公道的，它也正是在本文的建议围绕计量和地盘、而不是每六周就变一次的功能清单的原因。每周 5 亿 token 的额度和每月 40 条消息的上限，是公司如何为算力收费的结构性事实，它们比功能清单变得慢。选结构，不选演示；在续订前重新核对价格，因为这个市场唯一不变的是同样工作的价格持续下降，而今天最便宜的厂商，可能正是昨天刚改了交易条件的那一家。

## 我们未核实的内容

本文所在新闻室没有对 ChatGPT Work、Claude 或 Gemini 做任何一手测试。所有说法都来自厂商文档和经厂商页面核对的二手报道，这意味着任务质量对比——哪个智能体真能独立完成一次混乱的预订——不在本文范围内。Muse 的 token 到任务换算无法从公开文档核实，「每项任务 500 万 token」是示意性假设，已如此标明，不是实测数字。Claude 的会话上限未以具体数字公布，所以它在算账一节的对应行是缺口，不是数字。Gemini Ultra 的定价未核实，故排除而非估算。这个市场的价格随时可能变动，ChatGPT Pro 在 2026 年 9 月价格不变却削减额度就是证明。在你付款那天查厂商的定价页，而不是读这篇文章那天。

## 资料来源

[Meta，「介绍 Muse：世界上第一个为所有人打造的个人 AI 智能体」](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)，about.fb.com，2026 年 9 月 8 日。[Meta，Muse 订阅帮助页面](https://www.meta.com/help/superintelligence/)，2026 年 11 月访问（Power 每月 20 美元，每周 5 亿 token；Maximum 每月 100 美元，每周 30 亿 token）。[OpenAI 帮助中心，「ChatGPT agent」](https://help.openai.com/en/articles/11752874-chatgpt-agent)，2026 年 11 月访问（Plus 每月 40 条消息；Pro 400 条；定时；watch 模式；接管浏览器）。[ppc.land，「OpenAI 砍掉 Atlas 浏览器，折入新的 ChatGPT Work 智能体」](https://ppc.land/openai-kills-atlas-browser-folds-it-into-new-chatgpt-work-agent/)，2026 年 7 月 9 日。[howtoai.com，「Claude 定价：Free、Pro、Max、Team 与 Enterprise 计划」](https://howtoai.com/claude-pricing/)，2026 年 11 月 21 日对照 claude.com 与 Anthropic 帮助页面核查。[tailkits.com，「Claude：Anthropic 面向文件、浏览器与定时任务的 AI 智能体」](https://tailkits.com/tools/claude/)，2026 年 11 月 12 日。[Google，「在 Gemini 应用中用定时动作提前规划」](https://support.google.com/gemini/thread/351172872/new-feature-alert-plan-ahead-with-scheduled-actions-in-the-gemini-app?hl=en)，Gemini Apps 社区。[Justin McKelvey，「Gemini Spark：它做什么、多少钱、去了哪里」](https://justinmckelvey.com/blog/gemini-spark)，2026 年 11 月 20 日更新。[MakeUseOf，「一个 Gemini 提示替换了我早晨的邮件、日历和 Drive 例行流程」](https://www.makeuseof.com/gemini-morning-briefing-gmail-calendar-drive/)，2026 年 11 月 8 日。[Mejba Ahmed，「Gemini Spark：Google 的主动式 AI 智能体实测」](https://www.mejba.me/blog/gemini-spark-proactive-ai-agent)，2026 年 5 月 31 日。
