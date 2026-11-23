---
title: "Muse 的沃尔玛连接器把问题交给 Sparky，购物车留给自己"
linkTitle: "沃尔玛连接器与 Sparky 分工"
date: 2026-11-22
originalTitle: "Muse's Walmart connector sends questions to Sparky and keeps the cart to itself"
sourceUrl: "https://news.sulat.com/2026/11/22/walmart-muse-sparky-connector/"
author: "JP Caparas"
publisher: "Sulat AI & Tech News"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-23
tags: [连接器, 安全]
products: [muse]
dateNote: "发布方时区为新西兰（+13:00），时间戳 2026-11-22T11:45:00+13:00 相当于 UTC 11 月 21 日 22:45、美东 11 月 21 日 17:45。"
---

{{< source-info >}}

**收录说明**：本文为 Sulat AI & Tech News 2026 年 11 月 22 日文章（作者 JP Caparas），2026 年 11 月 23 日直接下载全文（L2），三张配图已本地化到页面 `images/`（L38、L78、L84）。全文依据电商作者 Juozas Kaziukėnas 11 月 21 日 X 帖截图的转录与分析：截图显示 Muse 用自有工具改动购物车，只把问题发给沃尔玛自有购物智能体 Sparky（L4、L20）。文中条款解读系转述 UCP Checker 与 eesel 对沃尔玛智能体条款的解读，作者自述未能直接打开沃尔玛条款页（L52、L130）。另注：此点不在原文内，为本轮交叉注记——Kaziukėnas 本人 11 月 23 日已修正说法：Muse 似乎不会用 Sparky 处理有意义的客户账户交互、暂无 agent-to-agent commerce、相关交互未获证实，阅读本文时应以该修正为准。

**内容摘要**：Kaziukėnas 11 月 21 日发布的截图显示，Muse 将通过沃尔玛的 MCP 获取商品、创建购物车并下单，而向 Sparky 咨询「订单、门店、政策与比较」类问题；他称沃尔玛与 Muse 即将推出他所说的首个 agent-to-agent 的 agentic commerce 集成，但作者未能从任何一家公司找到上线日期（L6）。截图中的指示写明：「Use ask_sparky for Walmart questions, such as orders, stores, policies and comparisons. Sparky is Walmart's own agent: it answers questions and changes nothing. Change the cart only with update_cart and remove_item_from_cart, and never ask Sparky to add to, change or check out a cart.」（L20）。文中还转述 UCP Checker 与 eesel 的解读：在网关内注册的智能体可在购物者设定的额度内自主结账，其他智能体则在每次结账前遇到「Human Consent Gate」；网关页面称访问「仅限邀请」且「可随时暂停」（L52）。Muse 与沃尔玛构成双重审批：Muse 将下单列为「sensitive write」，每次都要用户确认且不可设为「Always allow」，CNBC 10 月 3 日报道称 Muse 会在结账前出示含订单详情的审批卡；沃尔玛方面默认须经客户批准，可在消费限额内放行，限额示例为 50 美元、100 美元、200 美元（L62、L64、L66–L72）。

**保留理由**：本文是目前对 Muse–沃尔玛连接器分工（Sparky 只答问、Muse 自有工具改购物车）最细致的公开拆解，并附有截图转录与双重审批规则对照，是理解该集成的关键社区一手分析；但其核心依据仅为一张截图，且条款部分为二手转述，需与 Kaziukėnas 本人 11 月 23 日的修正一并阅读。
