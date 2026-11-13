---
title: "Cloudflare 提议智能体身份新规则，以 Muse 为主要例证"
linkTitle: "Cloudflare 智能体身份规则"
date: 2026-11-09
originalTitle: "Cloudflare Proposes New Identity Rules for AI Agents, Naming Muse as the Leading Example"
sourceUrl: "https://www.allthingsmuse.com/articles/cloudflare-muse-agent-identity-paper/"
author: "Icarus"
publisher: "All Things Muse"
basedOn: "Cloudflare 立场文件；HUMAN、DataDome 的数据报告"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-09
tags: [安全]
---

{{< source-info >}}

**收录说明**：直接下载。去掉了首图 Jolly 插画与文中的「Earlier coverage」栏目。Cloudflare 立场文件原文见正文中的 blog.cloudflare.com 链接。原文全文存于本目录的 original.md，网站上不显示，已翻译。文中 72%、33% 等数字转引自 HUMAN、DataDome 的报告，属二手。

**内容摘要**：Cloudflare 于 11 月 5 日发表立场文件《Agents aren’t humans (but they kinda are)》（作者 Bryan Becker），认为当 AI agent 代表用户行动时，网站看到的是 agent 而非用户，出问题时由网站承担成本，并以 Meta 的 Muse 与 OpenAI 的 dots 作为例证。文件列出 14 项 agent 给网站带来的挑战，结论是在几乎每一项中网站都承担主要成本，并以虚构助手 Ezra 为四位客户跑腿的例子说明：商店只见到 Ezra，无法分辨订单属于哪位客户，客户对一笔购买提出异议时，商店须证明客户曾要求购买，但商店见到的只有 Ezra。文件提出 Intermediation Principle，认为用户与网站之间的业务关系及各方的安全责任不应因中介而改变，并据此提出四级用户身份体系，主张以 Web Bot Auth 让 agent 签署请求以便网站核验来源，同时呼吁无需用户标识符的限流方案 MOLE 与机器可读的 agent 权限声明，并发起 Trusted Agent Delegation 联盟向包括 IETF 在内的标准机构推进，但未公布该联盟的成员、日期与治理结构。Cloudflare 已向客户提供三项控制：把 personal assistant 列为独立流量类别的分析、仅在有广告的页面屏蔽特定 agent 的按 agent 访问策略，以及处于 early access 的 Account Abuse Protection，可显示登录或注册请求是否由 personal assistant 发起。文中引用 HUMAN 9 月下旬的数据称，Muse 占其网络 AI agent 请求日均 72%，为 ChatGPT Agent 的 5.2 倍，84% 的 Muse 请求指向商品与搜索页面；DataDome 第三季度报告称 Muse 占 9 月 agentic 浏览器请求的 33%，而当月仅统计了 9 天；同时提到 Meta 自约 10 月 12 日起已对部分 Muse 网络请求使用 Web Bot Auth 签名，受查的 51 家大型零售商中有 37 家因旧有反机器人规则意外屏蔽了 agent，加拿大的大型银行也在数日内相继屏蔽 agent 访问客户账户。

**保留理由**：本篇提供了关于 agent 身份与网站成本的第三方立场文件内容，包括 Web Bot Auth、MOLE 与 Trusted Agent Delegation 联盟的提议，以及 Muse 在 agent 流量中的占比数据与网站屏蔽 agent 的实例，这些内容在已收的官方发布与上线报道中没有。

---

Cloudflare 在 11 月 5 日发表的一份立场文件中主张，当 AI 智能体代表用户行动时，几乎在所有情况下承担成本的都是网站，并提出 Web Bot Auth、无需标识符的限流，以及一个新的 Trusted Agent Delegation 联盟，以把问题带到标准机构。

Cloudflare 于 11 月 5 日发表立场文件，主张当 AI 智能体代表用户行动时，另一端的网站看到的是智能体而非用户，出问题时由网站承担成本。这份由 Bryan Becker 撰写的文件[《Agents aren't humans (but they kinda are)》](https://blog.cloudflare.com/trusted-agent-delegation)以 Meta 的 Muse 和 OpenAI 的 dots 作为当前从事这类工作的个人智能体的例子。文件提出了一套身份标准，并成立一个新联盟 Trusted Agent Delegation，以把问题带到标准机构。

文件的核心主张是：智能体是中介，而网络针对中介的旧答案已不再适用。网站过去可以封堵中介流量，并要求用户停用该服务。Cloudflare 认为，一旦大多数流量都是智能体流量，这种做法就会失效，而智能体流量增长之快，可能在不久的将来超过传统的人类浏览。

## 十四个问题，一张账单

文件列出了智能体给网站带来的 14 项挑战，并得出结论：在几乎每一项中，网站都承担主要成本。它用一个名为 Ezra 的虚构个人助理来说明问题，Ezra 为四位客户跑腿。街角杂货店过去认识每位客户及其偏好；现在只有 Ezra 来，杂货店分不清哪份订单是谁的。当一位客户对 Ezra 的一笔购买提出异议时，商店必须证明客户要求过这笔购买，但商店唯一见过的人是 Ezra。

文件认为，同样的模式如今在 AI 智能体身上重演。一家银行看到来自一个持有一串密码的智能体的登录尝试，只能封禁该智能体，而这同时会封堵其背后的每一位合法用户。一家无法判断某笔购买是否获授权的商店只能自己吸收争议。一家文章被智能体摘要的出版方既得不到访问，也得不到广告曝光。智能体还会不断轮询、猛击昂贵的端点、耗尽免费试用和促销额度，因为它们从不疲倦，也从不面对限制人类用户的那些摩擦。

## Cloudflare 的提议

文件立足于它所谓的「中介原则」（Intermediation Principle）：用户与网站之间的业务关系，以及各参与方的安全责任，必须不计中介而得到维护。据此，它提出一个四级用户身份量表，从无身份，经会话标识符和账户标识符，到针对高风险操作的每用户唯一标识符；并主张以 Web Bot Auth 作为智能体签署请求的方式，使网站能够核验其来自哪个运营方。

它还呼吁通过一项名为 MOLE 的方案实现无需用户标识符的限流，并呼吁为网站提供一种机器可读的方式来声明智能体可以做什么，理由是 robots.txt 并非为此而建。Trusted Agent Delegation 联盟将把这些议题带到包括 IETF 在内的标准机构，尽管文件没有给出该联盟的成员、日期或治理结构。

有三项控制已向 Cloudflare 客户开放：把个人助理作为独立流量类别拆分的分析；可按智能体设置访问策略，仅在有广告的页面上封堵某个智能体；以及处于早期访问阶段的 Account Abuse Protection，可显示某次登录或注册请求是否由个人助理发起。Cloudflare 销售机器人管理产品，因此其诊断与产品线指向同一方向，[PPC Land](https://ppc.land/cloudflare-says-websites-pay-for-ai-agents-as-metas-muse-learns-to-talk/)在评述该文件时指出了这一点。

## 为什么 Muse 是测试案例

Muse 是大多数网站实际看到的智能体。机器人检测公司 HUMAN [在 9 月下旬发现](https://ppc.land/metas-muse-accounts-for-72-of-ai-agent-requests-human-finds/)，Muse 占其网络每日 AI 智能体请求的平均 72%，规模是 ChatGPT Agent 的 5.2 倍，其中 84% 的 Muse 请求指向商品与搜索页面。DataDome 的第三季度报告称，Muse 占 9 月智能体浏览器请求的 33%，而当月只测量了九天。

身份问题对 Muse 来说已经现实存在。Fingerprint 上周表示，其检测现在可以在某家大型银行的登录流程中[标记它推断为 Muse 的流量](https://www.allthingsmuse.com/articles/fingerprint-detects-undeclared-muse-traffic/)；DataDome 发现，Meta 自约 10 月 12 日起一直在悄悄[用 Web Bot Auth 为部分 Muse 网络请求签名](https://www.allthingsmuse.com/articles/meta-muse-web-bot-auth-signed-requests/)，而这正是 Cloudflare 偏好的标准。与此同时，网站一直用封堵来回应同样的不确定性：一次审计所查的 51 家大型零售商中有 37 家因旧的反机器人规则而无意中封堵了智能体，加拿大最大的几家银行[在数日内相继行动](https://www.allthingsmuse.com/articles/canadian-banks-block-ai-agents-muse/)，封堵智能体访问客户账户。

## 接下来

Cloudflare 表示将在 IETF 举行边会和工作坊，以推进该联盟的工作，并邀请运营方、身份公司、支付提供商、商家和出版方参与。
