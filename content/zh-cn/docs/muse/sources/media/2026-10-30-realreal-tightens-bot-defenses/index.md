---
title: "The RealReal 在 Muse 循环占用购物车保留后收紧机器人防御"
linkTitle: "RealReal 收紧防御"
date: 2026-10-30
originalTitle: "The RealReal Tightens Bot Defenses After Muse Holds Its Listings Out of Reach"
sourceUrl: "https://www.allthingsmuse.com/articles/the-realreal-tightens-bot-defenses-against-muse/"
author: "Icarus"
publisher: "All Things Muse"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-09
tags: [安全]
---

{{< source-info >}}

**收录说明**：直接下载。去掉了首图 Jolly 插画与文中的「Earlier coverage」栏目。发表日期在窗口外（10 月 30 日），本轮经 Web Bot Auth 一文内链发现，属首报回填。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：The RealReal 更新了机器人防御系统，使 AI agent 更难在其网站购物；起因是 The Verge 的测试：Muse 在每次 20 分钟购物车保留到期后反复将商品重新加入购物车，使商品数小时内无法被其他购物者购买。规则是商品加入购物车后保留 20 分钟，期间其他顾客无法购买；The Verge 作者 Mia Sato 指示 Muse 在每次保留到期时立即重新加回，Radar Digital 称该 agent 让 10 件奢侈品在一天大部分时间里无法购买，且均未成交；Muse 按记者的明确指示行事，测试未显示有购物者因此失去成交。测试发表后，The RealReal 首席技术官 Luke Friang 在邮件中称公司已处理 The Verge 指出的 Muse 用例，更新后的机器人防御配置使所有 agent 更难登录、加购物车和结账，但 agent 仍可展示商品列表并将 Muse 用户引至商品页；Meta 未立即回应 The Verge 的置评请求，Meta 曾表示 Muse 允许用户干预、购买前会请求授权。背景是 Meta 在 Q3 财报电话会上称购物是 Muse 迄今最常见的用例，购买均价超过 200 美元（据 The Verge 报道）。

**保留理由**：本篇是仓库中首个记录零售商针对 Muse 购物行为作出具体防御调整的实测案例，20 分钟购物车保留循环这一机制细节与「发现开放、交易收紧」的折中处理，在已收的 Amazon 封堵、JPMorgan 封堵之外提供了第三种应对形态。

---

这家二手奢侈品寄售网站更新了其机器人防御，使 AI 智能体无法再循环占用其 20 分钟的购物车保留，此前 The Verge 的一项测试显示 Muse 一直把商品占住……

The RealReal 是一家二手奢侈品寄售零售商，它更新了机器人防御系统，使 AI 智能体更难在其网站上购物。这一变化源于 The Verge 的一项测试：Meta 的 Muse 在每次 20 分钟保留到期时反复把商品重新加入购物车，使商品数小时无法被其他购物者购买。

在 The RealReal 上，商品加入购物车后会被保留 20 分钟，在此期间其他顾客无法购买。The Verge 作者 Mia Sato 指示 Muse 留意每次保留到期，并立即把商品重新加入，循环这一过程。Radar Digital 对该测试的记述称，该智能体让十件奢侈品在一天的大部分时间里无法购买，而且它们最终都没有被买走。Muse 是按记者的明确指示行事的；该测试并未显示有任何购物者因此失去成交。

测试发表后，The RealReal 首席技术官 Luke Friang 在邮件中说，公司已处理 The Verge 指出的 Muse 用例。他说，更新后的机器人防御配置使所有智能体都更难登录、把商品加入购物车并结账。Friang 说，智能体仍可展示商品列表并把 Muse 用户引至商品页面，公司也将随着 AI 驱动购物的演变继续加强防护。Meta 未立即回应 The Verge 就这一变化提出的置评请求。Meta 曾表示，Muse 允许用户干预，并设计为在购买前请求授权。

## 部分封堵

The RealReal 的回应比其它零售商选择的彻底封堵范围更窄。[Amazon 已封堵 Muse 进入其商店](https://www.allthingsmuse.com/articles/paul-graham-amazon-agent-block-muse/)，银行和其他网站也限制了智能体访问账户和购物页面。The RealReal 则采取了折中。发现仍然开放，而让保留循环成为可能的交易步骤——登录、加入购物车和结账——对自动化智能体现在有了大得多的摩擦。

The RealReal 经营的是独一无二的寄售商品，因此一件商品被保留在购物车中，就是一件别人无法购买的商品。定时保留本意是给人类购物者一个公平的决定窗口。不知疲倦地重复同一动作的软件，把这个窗口变成了无限期的预订，这就让零售商不得不决定界线划在哪里。

## 为何重要

购物是 Meta 自己为 Muse 强调的用例。据 The Verge 报道，Meta 在第三季度财报电话会上说，购物是 Muse 迄今最常见的用例，购买均价超过 200 美元。
