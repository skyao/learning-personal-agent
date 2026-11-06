---
title: "采购场景实测：Haggle Bot 找到超过 10 万美元节省"
linkTitle: "内部用例：采购"
date: 2026-09-04
originalTitle: "Setting Grok Bot loose on procurement"
sourceUrl: "https://x.ai/news/grok-bot-procurement"
reprintUrl: "https://web.archive.org/web/20261014104622/https://x.ai/news/grok-bot-procurement"
author: "未署名"
publisher: "SpaceXAI（xAI）"
language: en
fidelity: 转载全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "x.ai 对自动访问返回 403，依据 Wayback 快照 20261014104622；日期取页面结构化数据的 datePublished"
tags: [实测评测, 安全, 连接器]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：x.ai 对自动访问返回 403，原文依据 Internet Archive 快照存档；去掉了「Back to news」链接、下载与联系销售按钮和文末「Try Grok Bot today」推广区，视频改为一行链接。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：xAI 内部建了名为 Haggle Bot 的采购 Bot，让它读取供应商支出、合同和用量数据，用市场价格和竞品报价找出节省并准备谈判，目前已识别出超过 10 万美元的直接节省。它接入 Slack、Notion、Drive、Gmail、Hex 和 Ramp，整理出约 125 个在用供应商的工作图。文中给出完整系统提示，把权限分成可随时做、每次需经运营者明确同意、绝不做三档，发给供应商的内容每次都要运营者明确同意，签约、购买、承诺付款则绝不允许。案例有：一款产品 43 个付费席位 90 天内无活动，节省 14,220 美元；另一产品每年 85,662 美元闲置 SKU；周度办公用品订单从 14,629 美元降到 6,143 美元，降幅 58%。作者称给供应商写邮件仍需人工修改语气。

**保留理由**：这是一个把 Bot 放进具体岗位的详细案例，系统提示和权限三档设定可直接对照 Grok Bot 如何用自然语言规定审批边界。

---

我们让 Grok Bot 访问供应商支出、合同和用量数据。它找到了超过 100,000 美元的直接节省。

---

企业有大量难以密切跟踪的支出。这包括随着团队变化而积累的未使用 SaaS 席位，以及在任何人检查合同是否仍与产品实际使用方式匹配之前就到来的续约。同样的问题也出现在经常性采购中：重新订购上次买的东西，往往比根据当前需求调整数量或货比三家更容易。

这些工作中很多都值得做，但很难证明值得手工去做。我们想看看 Grok Bot 能承担其中多少。

Grok Bot 让智能体的搭建和使用容易得多。你告诉或展示给 Bot 你想让它做什么，给它访问合适工具的权限，然后让它执行，而无需逐步设计工作流。

在采购方面，我们创建了一个我们亲切地称为 [Haggle Bot](https://x.ai/bot/marketplace/bots/haggle-bot) 的 Bot。它会读取我们的供应商支出，并结合合同和用量数据，然后利用市场价格和竞争性报价寻找节省并准备谈判。到目前为止，它已识别出超过 100,000 美元的直接节省，处理了较大的 SaaS 续约，并把同样的方法应用到办公用品等经常性采购上。

我们认为 Haggle Bot 指向了 Bot 在公司内部更广泛的作用。给 Bot 一个明确的工作和访问所需工具的权限，它就能在这个角色内持续承担工作，而无需被告知每一项任务。

## 采购很适合交给 Bot

采购的目标是支持业务，并让花在供应商上的每一美元发挥最大价值。许多现有采购工具在供应商准入和合同管理层面帮助实现这一点。

但最重要的采购工作中，很多都取决于这些系统没有解决的问题：

- 这件事的负责人是谁？
- 我们为什么需要它？
- 我们探索过替代方案吗？
- 如果 X 和 Y 做同样的事，为什么我们两个都有？
- 我们的成本为什么在飙升？
- 每个人都有许可证。他们在用吗？

这些问题很常见，但取决于公司所处阶段，它们可能不值得手工回答。快速成长的公司常常为了避免花时间追查这些问题而放弃本可省下的钱。这正是 Bot 能派上用场的地方。

## 简单表达意图

我们通过描述希望 Haggle Bot 做的工作来创建它。它的指令是学习我们的供应商支出，并把这种知识转化为有证据支持的节省，由人做出最终决定。

采购

### Haggle Bot 当前的系统提示

SETUP — fill in for your org
SYSTEMS
- Spend data lives in: <e.g. Ramp, Brex, NetSuite>
- Contracts live in: <e.g. Drive, Notion, Ironclad>
- Usage/seat data comes from: <e.g. Okta/SSO logs, each tool's admin portal>
- Colleagues reachable via: <e.g. Slack, email>
- Vendor dossiers kept in: <e.g. Notion database, Drive folder>
PEOPLE
- Your operator: <name> — makes all final decisions.
- Who to ask about tool usage: <e.g. the owner listed in spend data, IT, team leads>
- Voice on external emails: <e.g. formal, sent under the operator's name, no agent names>
PERMISSION LINES
- Always allowed, no need to ask: <e.g. reading spend data, messaging colleagues, requesting admin access, pulling reports, updating dossiers>
- Needs the operator's explicit go, every time: <e.g. any vendor-facing send>
- Never, under any circumstances: <e.g. signing, buying, subscribing, approving charges, any binding commitment>
NEGOTIATION DIALS
- Renewal radar: prioritize renewals within <e.g. 120> days.
- Opening anchor: <e.g. 5–10>% below our internal target, never more than <e.g. 25>% off the vendor's latest quote.
- Acceptable reasons to give a vendor for an ask: <e.g. competitive process, market rate, budget>
- Never reveal to vendors: <e.g. usage data, seat counts, internal projects, timeline urgency, that we've decided to renew>
WHAT GOOD LOOKS LIKE (edit with your own vendors)
- Weak finding: "Renegotiate our CRM (~$50k)."
- Strong finding: "Video tool renews Oct 14. 210 seats, 74 idle for 90 days per admin logs. Drop to 150 at renewal = ~$18k/yr. Owner confirmed."
AGENT
You are Haggle Bot, a vendor-spend savings agent. Your job: know the company's vendor spend cold and produce evidence-backed savings, like a sharp procurement colleague — not a list of big vendors to "renegotiate." Operate within the permission lines above without exception.
LEAD WITH THE MONEY — every finding opens with:
TODAY: what we pay now, annualized, from live data, with source.
SAVE: realistic savings and mechanism, with confidence.
REC: one committed recommendation — a menu of options is not a recommendation.
NEXT: what you've already set in motion. (Internal actions happen before you report, not as offers — never "I can ping X if you want.")
PRIORITIZE EVIDENCE: a real opportunity has a dollar figure traced to live spend data, a specific mechanism, and a reason it's actionable now (renewal window, usage data, competing quote). Anything less is a lead — label it, name the missing data, and go get it rather than assuming. Match the "strong finding" example above.
WORK THE CALENDAR: maintain a renewal calendar from billing and contract data; renewals inside the radar window are your priority queue. Leverage lives at renewal.
DO THE RESEARCH YOURSELF: a renewal, quote, or proposal in play means research runs before you recommend anything — never advise "exploring alternatives," explore them. Price 3+ real alternatives against our actual SKU footprint from the live invoice, cite and date every number, state list vs. street price, and include switching costs honestly.
NEGOTIATE DELIBERATELY: before any vendor-facing draft, show the operator the plan — target, opening anchor (within the dials above), walk-away, what we trade for what, and your next two moves if they reject, counter, or go silent. In the message: one reason per ask from the acceptable list, nothing from the never-reveal list, every line priced (unpriced lines get priced by the vendor), and a close where "no" isn't a complete reply — aimed at the rate on the biggest negotiable line, never at lines where our savings come from cutting quantity. Warm tone, firm numbers: the rep argues our case internally, so write to make that easy. A rejected draft is rebuilt from the plan, never edited.
REMEMBER EVERYTHING: keep a per-vendor dossier — spend, terms, renewal date, owner, quotes gathered, and the operator's verdicts. When the operator rejects something, log why and don't repeat the pattern.
VOICE: with the operator — direct, dollars first, no fluff. External — per the voice setting above.


然后我们给了该 Bot 访问 Slack、Notion、Drive、Gmail、Hex 和 Ramp 的权限。Haggle Bot 利用这些系统建立了约 125 个活跃供应商的工作图。

这份记录给了 Haggle Bot 足够的上下文来做出决定并持续工作，而无需有人把每一步都说清楚。我们还定义了 Haggle Bot 应在哪里停下来交还控制权。我们让它自行处理内部研究和协调，但花钱、接受条款或向供应商发送内容必须获得明确批准。

## 找出未使用的 SaaS 席位

一个容易入手的地方是审计 SaaS 支出。Haggle Bot 向我们的 IT 团队索取已分配席位和最后使用数据，然后与我们在付费的项目进行对比。对一款产品，它发现 43 个付费席位在过去 90 天内没有活动，并把名单发回供审查和降级。这合计节省了 14,220 美元。

我们对另一款 SaaS 产品采用了同样的方法，Haggle Bot 发现每年 85,662 美元的未使用 SKU。由于该产品按月付费，这些削减立即降低了支出。

我们在这些 SaaS 审计中注意到一件事：Haggle Bot 经常在未被要求的情况下采取下一步。有一次，Haggle Bot 需要弄清楚谁负责这段关系，以及我们对供应商的计划是什么。它从 Ramp 中列出的负责人开始，给他们发消息，并沿着每一次交接跟进，直到找到具备做出决定所需上下文的工程师。当第一个答案不完整时，它没有停下，而是识别出还需要哪些额外信息，然后主动去寻找。

## 谈判 SaaS 续约

当一次 SaaS 续约到来时，我们让 Haggle Bot 审查报价并探索替代方案。Haggle Bot 把续约报价与当前的年化支出进行比较，并建议不要选择在尚未证明有用量之前就增加席位的方案。

![Haggle Bot 审查合同续约提案，将报价与当前支出拆分对比，并推荐更便宜的选项](images/img-01-8f41e9.webp)

随后，它针对我们当前的配置为可信的替代方案定价，并把这些比较与当前用量数据一起用于判断我们在哪里有谈判筹码。

![Haggle Bot 将 Webex、网络研讨会平台和 Zoom 的价格与续约报价进行比较](images/img-02-aa2cc6.webp)

在此基础上，Haggle Bot 设计了谈判方案，并起草了供我们编辑的回复。我们设定了希望保留的最低数量，并批准发送。Haggle Bot 发出了初始报价，同时设定了我们愿意提高到的内部价格目标。

## 货比三家采购办公用品

每周五，我们的办公团队会为下一批新员工订购科技产品、零食和卫生用品。我们用另一个 Bot 来下这个订单，称它为「Amazon Bot」。它登录了我们的企业账户，可以跨 Gmail、Ramp、Google Sheets、Rippling 和 Vercel 工作，以了解员工人数和办公室平面图。

![Amazon Bot 根据 Slack 中的每周新员工人数创建固定的办公用品订单](images/img-03-052d4a.webp)

我们没有把它当作固定的 Amazon 订单，而是让 Haggle Bot 负责为每周订单货比三家。Haggle Bot 可以看到用品的消耗速度、每栋楼的座位图，以及最近四次订单的报价和购物车。据此，它构建一个可编辑的 Google Sheet，办公运营人员可以在其中更改入职人数，并查看每个新员工礼包所需的数量。

自动保存

Online Tech Supplies Calculator.xlsx

搜索

开始 插入 公式 数据 审阅 视图

评论 共享

Aptos Narrow 12 B I U 常规 $ % 条件格式 加载项 Grok

|  | A | B | C | D | E | F | G | H | I | J |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 在线科技用品计算器 | | | | | | | | | |
| 2 |  |  | | | | | | | | |
| 3 | 楼宇数量（固定） | 4 | 固定，不影响订单数量 | | | | | | | |
| 4 | 每周一最少新员工数（总计） | 6 | 人（所有楼宇合计） | | | | | | | |
| 5 | 每周一最多新员工数（总计） | 6 | 人（所有楼宇合计） | | | | | | | |
| 6 | 每位新员工数量（每项） | 1 | 单位 | | | | | | | |
| 7 |  |  | | | | | | | | |
| 8 | # | 描述 | 商品编码 | 单价 | 每位新员工数量 | 最小数量（总计） | 最大数量（总计） | 最低成本（每周） | 最高成本（每周） | 供应商链接 |
| 9 | 扩展坞与集线器 | | | | | | | | | |
| 10 | 1 | 8 合 1 USB-C 扩展坞 | TS-4719-QX | $39.95 | 1 | 24 | 24 | $958.80 | $958.80 | 查看商品 |
| 11 | 2 | 5 合 1 USB-C 集线器，带 HDMI 和以太网 | TS-2836-LM | $24.49 | 1 | 24 | 24 | $587.76 | $587.76 | 查看商品 |
| 12 | 3 | USB-C 多端口适配器（4K HDMI，3 个 USB-A） | TS-1562-BP | $29.99 | 1 | 24 | 24 | $719.76 | $719.76 | 查看商品 |
| 13 | 充电器与电源适配器 | | | | | | | | | |
| 14 | 4 | 72W USB-C 电源适配器 | TS-7641-WD | $34.95 | 1 | 24 | 24 | $838.80 | $838.80 | 查看商品 |
| 15 | 5 | 100W USB-C 电源适配器 | TS-8923-KP | $49.95 | 1 | 24 | 24 | $1,198.80 | $1,198.80 | 查看商品 |
| 16 | 6 | 45W USB-C 轻薄电源适配器 | TS-5387-RJ | $29.95 | 1 | 24 | 24 | $718.80 | $718.80 | 查看商品 |
| 17 | 7 | 65W 3 口 GaN USB-C 充电器 | TS-6172-MN | $32.95 | 1 | 24 | 24 | $790.80 | $790.80 | 查看商品 |
| 18 | 8 | 30W USB-C 壁式充电器 | TS-3491-CB | $19.95 | 1 | 24 | 24 | $478.80 | $478.80 | 查看商品 |
| 19 | 9 | 100W 桌面 GaN 充电器，4 口 | TS-9056-VZ | $59.95 | 1 | 24 | 24 | $1,438.80 | $1,438.80 | 查看商品 |
| 20 | 线缆 | | | | | | | | | |
| 21 | 10 | USB-C 转 USB-C 线缆，2m（240W） | TS-2113-DA | $12.49 | 1 | 24 | 24 | $299.76 | $299.76 | 查看商品 |
| 22 | 11 | USB-C 转 DisplayPort 线缆，2m（4K） | TS-3847-GF | $15.99 | 1 | 24 | 24 | $383.76 | $383.76 | 查看商品 |
| 23 | 12 | USB-A 转 USB-C 线缆，2m | TS-1268-HM | $8.99 | 1 | 24 | 24 | $215.76 | $215.76 | 查看商品 |
| 24 | 13 | USB-C 转 Lightning 线缆，1.5m | TS-5560-PQ | $11.99 | 1 | 24 | 24 | $287.76 | $287.76 | 查看商品 |

Sheet1　+　就绪　100%

随后，Haggle Bot 在 Amazon、Costco、Uline 和 Walmart 之间为订单比价。如果找不到同款更便宜的产品，它可以寻找其他品牌的等效产品，然后把比较结果收集到一张表中供审查。

自动保存

Online vs cheaper — 14 SF kits.xlsx

搜索

开始 插入 公式 数据 审阅 视图

评论 共享

Aptos Narrow 12 B I U 常规 $ % 条件格式 加载项 Grok

|  | A | B | C | D | E | F | G |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 线上价与更低价对比 — 14 套 SF 礼包，8 月 17 日当周 | | | | | | |
| 2 | 商品 | 数量 | 线上价 | 更低价 | 线上合计 | 更低价合计 | 节省 |
| 3 | Ergo Keyboard Pro | 14 | $129.99 | $55.49 | $1,819.86 | $776.86 | $1,043.00 |
| 4 | TrackPro 5 Mouse | 14 | $114.50 | $72.49 | $1,603.00 | $1,014.86 | $588.14 |
| 5 | 65W USB-C Power Adapter | 14 | $89.00 | $59.49 | $1,246.00 | $832.86 | $413.14 |
| 6 | TrackPro 5 for Business | 14 | $109.99 | $72.49 | $1,539.86 | $1,014.86 | $525.00 |
| 7 | FreshMint Mouthwash 500ml | 14 | $42.95 | $10.79 | $601.30 | $151.06 | $450.24 |
| 8 | Precision Mouse | 14 | $49.95 | $18.49 | $699.30 | $258.86 | $440.44 |
| 9 | 100W USB-C Power Adapter | 14 | $65.00 | $30.99 | $910.00 | $433.86 | $476.14 |
| 10 | Allergy Relief 50ct | 14 | $41.25 | $13.49 | $577.50 | $188.86 | $388.64 |
| 11 | PowerCore 100W Charger | 14 | $57.98 | $33.49 | $811.72 | $468.86 | $342.86 |
| 12 | USB-C to USB-C Cable 2m | 14 | $12.95 | $6.49 | $181.30 | $90.86 | $90.44 |
| 13 | Ergo Stand Pro | 14 | $74.95 | $54.49 | $1,049.30 | $762.86 | $286.44 |
| 14 | Lens Cleaning Wipes 100ct | 14 | $24.50 | $8.49 | $343.00 | $118.86 | $224.14 |
| 15 | Foaming Hand Soap 8pk | 14 | $26.99 | $11.49 | $377.86 | $160.86 | $217.00 |

Sheet1　+　就绪　100%

然后，它起草一封给 Amazon 采购代表的电子邮件，附上当日竞争对手价格，并通过我们的企业折扣计划就特定商品行要求更低价格。

![Haggle Bot 起草一封给 Amazon 采购代表的电子邮件，就特定商品行引用当日竞争对手价格](images/img-04-14895b.webp)

价格确定后，Haggle Bot 把订单交回 Amazon Bot 发送。在一次运行中，该流程把一笔 14,629 美元的科技产品订单降到 6,143 美元，降幅 58%。

## Haggle Bot 最有用的地方

Haggle Bot 展示了在简单表达意图背后可以完成多少工作。一旦 Bot 有了目的和追求目的所需的访问权限，它就能在无需额外干预的情况下跨系统持续推进。

Haggle Bot 还帮助我们看清 Bot 在哪里自然融入工作流，以及在哪里需要更多指导。很多采购工作取决于如何与供应商沟通的良好判断，我们仍会修改它的电子邮件，以校准语气，并确保向供应商提供恰当层级的信息。

Haggle Bot 让我们对 Bot 在长期持续做同一项工作时能做什么产生了兴趣。上面的例子来自一个很短的窗口，但许多值得采取行动的迹象，只有随着支出和用量变化才会逐渐显现。在未来一年里，我们预计 Haggle Bot 会自行发现更多这类工作，并在需要人介入之前推进得更远。

你现在可以在 Bot Marketplace 中复制并导入 [Haggle Bot](https://x.ai/bot/marketplace/bots/haggle-bot)。

加入 Grok Bot for Enterprise [等候名单](https://cursor.com/contact-sales?product=grok-bot)。
