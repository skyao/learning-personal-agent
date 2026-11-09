---
title: "Cloudflare 提议智能体身份新规则，以 Muse 为主要例证"
linkTitle: "Cloudflare 智能体身份规则"
date: 2026-11-09
originalTitle: "Cloudflare Proposes New Identity Rules for AI Agents, Naming Muse as the Leading Example"
sourceUrl: "https://www.allthingsmuse.com/articles/cloudflare-muse-agent-identity-paper/"
author: "Icarus"
publisher: "All Things Muse"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-09
tags: [安全]
---

{{< source-info >}}

**收录说明**：直接下载。去掉了首图 Jolly 插画与文中的「Earlier coverage」栏目。Cloudflare 立场文件原文见正文中的 blog.cloudflare.com 链接。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：Cloudflare 于 11 月 5 日发表立场文件《Agents aren’t humans (but they kinda are)》（作者 Bryan Becker），认为当 AI agent 代表用户行动时，网站看到的是 agent 而非用户，出问题时由网站承担成本，并以 Meta 的 Muse 与 OpenAI 的 dots 作为例证。文件列出 14 项 agent 给网站带来的挑战，结论是在几乎每一项中网站都承担主要成本，并以虚构助手 Ezra 为四位客户跑腿的例子说明：商店只见到 Ezra，无法分辨订单属于哪位客户，客户对一笔购买提出异议时，商店须证明客户曾要求购买，但商店见到的只有 Ezra。文件提出 Intermediation Principle，认为用户与网站之间的业务关系及各方的安全责任不应因中介而改变，并据此提出四级用户身份体系，主张以 Web Bot Auth 让 agent 签署请求以便网站核验来源，同时呼吁无需用户标识符的限流方案 MOLE 与机器可读的 agent 权限声明，并发起 Trusted Agent Delegation 联盟向包括 IETF 在内的标准机构推进，但未公布该联盟的成员、日期与治理结构。Cloudflare 已向客户提供三项控制：把 personal assistant 列为独立流量类别的分析、仅在有广告的页面屏蔽特定 agent 的按 agent 访问策略，以及处于 early access 的 Account Abuse Protection，可显示登录或注册请求是否由 personal assistant 发起。文中引用 HUMAN 9 月下旬的数据称，Muse 占其网络 AI agent 请求日均 72%，为 ChatGPT Agent 的 5.2 倍，84% 的 Muse 请求指向商品与搜索页面；DataDome 第三季度报告称 Muse 占 9 月 agentic 浏览器请求的 33%，而当月仅统计了 9 天；同时提到 Meta 自约 10 月 12 日起已对部分 Muse 网络请求使用 Web Bot Auth 签名，受查的 51 家大型零售商中有 37 家因旧有反机器人规则意外屏蔽了 agent，加拿大的大型银行也在数日内相继屏蔽 agent 访问客户账户。

**保留理由**：本篇提供了关于 agent 身份与网站成本的第三方立场文件内容，包括 Web Bot Auth、MOLE 与 Trusted Agent Delegation 联盟的提议，以及 Muse 在 agent 流量中的占比数据与网站屏蔽 agent 的实例，这些内容在已收的官方发布与上线报道中没有。
