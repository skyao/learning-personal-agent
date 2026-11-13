---
title: "智能体处处碰壁：谁在封堵智能体，还有什么路可走"
linkTitle: "谁在封堵智能体"
date: 2026-11-06
originalTitle: "Your AI Agent Hits a Wall: Who Is Blocking Agents, and What Still Works"
sourceUrl: "https://www.allthingsmuse.com/articles/agent-blocking-guide/"
author: "Icarus"
publisher: "All Things Muse"
basedOn: "CNBC、《华尔街日报》（经 Gizmodo 摘要）、Bloomberg TV、TechCrunch 等报道"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-08
tags: [连接器, 商业与规模, 安全]
---

{{< source-info >}}

**收录说明**：直接下载。去掉了两张 Jolly 插画与文中「The parallel move north of the border」栏目。原文全文存于本目录的 original.md，网站上不显示，已翻译。本文汇总转述 CNBC、《华尔街日报》（经 Gizmodo 摘要）、Bloomberg TV、TechCrunch 等多家报道，属二手报道。

**内容摘要**：文章综述银行与零售商对 Muse 等 AI 智能体的封堵：摩根大通首席执行官杰米·戴蒙在 10 月 13 日三季度财报电话会上表示，不会让任意外部智能体在其系统内操作，该行确认封堵外部智能体为零售客户采取行动，但余额仍可通过获授权的 Plaid 与开放银行连接器查看。查尔斯·施瓦布随后跟进，首席执行官里克·沃斯特称该公司封堵包括 Muse 在内的主要外部智能体转移客户资金，每周拦截数十次尝试，同时计划通过自有模型上下文协议服务器让外部模型查询余额与做研究，但不涉及资金转移。加拿大方面，加拿大皇家银行于 10 月 27 日率先通知员工封堵第三方个人 AI 智能体，多伦多道明银行、蒙特利尔银行、丰业银行与加拿大帝国商业银行在一天内跟进，加拿大国家银行表示正在关注。零售方面，亚马逊在 9 月以访问方式与客户使用条款不一致及安全与隐私担忧为由封堵 Muse 购物，并要求 Meta 将亚马逊从 Muse 购物体验中移除；CNBC 报道的 Billions Network 对 51 家美国大型零售商的审计发现，明确限制智能体的有 5 家，其中被点名的包括亚马逊、Kohl’s 与 Neiman Marcus。审计还发现，51 家中有 37 家主要因旧的反机器人规则而非明确的 AI 智能体政策封堵购物智能体，只有 11 家对 AI 智能体有明确立场，且 51 家中没有一家提供经核实的智能体完成购买的途径。

**保留理由**：汇总了银行与零售商两条线的封堵时间线与具体口径，并以 51 家零售商审计数据区分了有意封堵与旧规则误伤，可作为智能体落地受阻范围与原因的出处。

---

银行和零售商正把 Meta 的 Muse 等 AI 智能体挡在账户和结账流程之外，但大多数零售商的封堵其实是旧反机器人规则的意外结果。以下是封堵者、智能体仍能做什么，以及获授权访问应当是什么样子。

银行说智能体不能碰客户的钱。零售商说智能体不能结账。一项针对 51 家美国大型零售商的审计发现，大多数封堵根本没有被决定过。

## 银行先划下界线

[JPMorgan Chase](/articles/jpmorgan-blocks-ai-agents-muse-accounts/)，美国最大的银行，率先行动。首席执行官杰米·戴蒙在 10 月 13 日的第三季度财报电话会上告诉分析师，该行不会让「随便哪个……外部智能体」在其系统内操作。一位女发言人证实，该行阻止外部智能体为零售客户采取行动，但余额仍可通过获授权的 Plaid 与开放银行连接器查看。转账、付账单或在账户内采取任何操作都被禁止。

[Charles Schwab](/articles/charles-schwab-blocks-muse-client-money/) 数日后跟进。首席执行官里克·沃斯特对 Bloomberg TV 表示，Schwab 阻止包括 Muse 在内的主要外部智能体转移客户资金，公司每周会拦下「几十次」尝试。Schwab 并未完全切断外部 AI：该券商计划通过其自有的模型上下文协议（Model Context Protocol，MCP）服务器连接外部模型，采用公司设定的认证规则，用于查询余额和研究，但不涉及任何资金转移。

加拿大最大的几家银行随后步调一致地行动。加拿大皇家银行率先行动，在 10 月 27 日通知员工将阻止第三方个人 AI 智能体访问网上银行和其他需认证的服务，备忘录称智能体是「不可接受的客户风险」。多伦多道明银行、蒙特利尔银行、丰业银行与加拿大帝国商业银行在一天内跟进；加拿大国家银行表示正在关注此事。逐家银行的完整时间线见[我们对加拿大银行这一行动的记述](/articles/canadian-banks-block-ai-agents-muse/)。

## 有意说不的零售商

亚马逊在 9 月阻止 Muse 在其网站购物，称该智能体的访问方式与其客户使用条款不一致，并援引了关于智能体处理客户凭证的安全与隐私担忧。据 CNBC 报道，亚马逊随后要求 Meta 将亚马逊从 Muse 购物体验中移除；首席执行官 [Andy Jassy 在 10 月 29 日的财报电话会上告诉投资者](/articles/amazon-jassy-shopping-agents-not-great/)，外部购物智能体「仍不够好」。亚马逊在封堵其他智能体的同时，运营着自己的购物智能体 Alexa for Shopping。

Kohl's 与 Neiman Marcus 是 CNBC 点名的另外两家明确限制智能体的零售商，这一信息出自 [CNBC 11 月 1 日报道的、身份验证公司 Billions Network 对 51 家美国大型零售商的审计](/articles/banks-retailers-block-ai-agents-cnbc-audit/)。审计发现五家零售商明确限制智能体；CNBC 点名了其中三家。《华尔街日报》（由 Gizmodo 摘要）报道，Tapestry 与 Kohl's 拒绝让智能体完成购买，Chewy 与 Neiman Marcus 封堵部分智能体。据[TechCrunch 的报道](/articles/muse-websites-blocking-agents/)，Delta 不让智能体购买机票。

## 被封堵的智能体还能做什么，不能做什么

本指南中的每一家机构都划了同一条线：可以看，不可以动。被封堵的智能体可以通过获授权的连接器查询余额、研究产品和浏览，但不能转移资金、发送资金、支付账单、执行交易或完成购买。在 Schwab，智能体可以通过公司自有渠道查看余额和做研究，只有机构会采取行动。JPMorgan 通过 Plaid 划下同样的界线。在 Billions Network 审计的 51 家零售商中，没有一家为智能体提供了完成购买的经核实途径。

## 大多数零售封堵是意外

在 Billions Network 审查其公开访问规则的 51 家美国大型零售商中，有 37 家封堵购物智能体主要是出于意外——它们依靠的是为阻止抓取程序和自动化流量而写的旧机器人规则，而非明确的 AI 智能体政策。51 家中只有 11 家对 AI 智能体有过明确立场。Billions Network 联合创始人兼首席执行官 Evin McMullen 对 CNBC 表示，审计中的大多数零售商根本没有就 AI 智能体做出决定。

真人验证检查——即保护网站免受垃圾信息侵扰的「点击证明你是人」按钮——可能在结账过程中让智能体验证失败，并将其踢出交易。Walmart 对 TechCrunch 表示，它对 Muse 的封堵并非有意：该公司与 Muse 是合作伙伴。智能体也很难被识别：[Cequence 发现](/articles/cequence-muse-agent-traffic-identity-study/) Muse 不在其流量中标明身份，而 [DataDome 发现](/articles/datadome-muse-29-million-requests/) 其样本中 99.3% 的 Muse 请求来自云基础设施，因此仅靠 user-agent 字符串封堵机器人的网站，无法可靠地区分 Muse 请求与其他云流量。

该审计读取的是公开规则，而非技术执行的证据：公开的限制本身并不能证明智能体在实践中被多彻底地封堵。

## 获授权访问应当是什么样子

McMullen 的答案是采用一种验证方法，让合法智能体可以被识别，而不是用一刀切的机器人封堵把智能体和抓取程序一并拦住。埃森哲全球银行业负责人 Michael Abbott 对 CNBC 表示，试图封堵智能体的银行和零售商有失去希望获得智能体辅助购物与银行服务的客户的风险，它们应当转而开发让获授权智能体与其交互的安全方式。

Cequence 首席执行官 Ameya Talwalkar 用一句话概括了中间路线：「彻底封堵智能体会把客户拒之门外，而全部放行是大多数安全团队无法承担的风险。」他公司的答案是 Agent Trust，它依据受信任的签发方注册表验证智能体身份，并逐请求应用策略。DataDome 的建议方向相同：按功能而非厂商对智能体分类，为表单、登录、购物车和结账设定明确规则，并在 user-agent 字符串之外验证身份。

可行的模式已经存在。Schwab 的模型上下文协议服务器让公司掌控认证，同时允许外部智能体读取余额和做研究。Walmart 与 OpenAI 及其他公司合作，通过获批途径开展智能体购物，并允许用户创建专用的智能体资料，使 AI 智能体完成的购买保持独立。Meta 的答案则是它正与 Sierra 以及 Walmart、Stripe、Shopify 等合作伙伴共同开发的开放式智能体对智能体标准。就连 JPMorgan 也通过一位发言人表示，它支持通过开放银行提供商进行安全的数据共享，并致力于安全地实现智能体连接。

有一个数字能说明还有多远的路要走：审计中的 51 家零售商里，没有任何一家提供经核实的智能体完成购买途径。
