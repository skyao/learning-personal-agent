---
title: "Fingerprint 称可识别未表明身份的 Muse 流量"
linkTitle: "Fingerprint 识别流量"
date: 2026-11-06
originalTitle: "Fingerprint Says It Can Now Spot Muse Traffic That Doesn't Identify Itself"
sourceUrl: "https://www.allthingsmuse.com/articles/fingerprint-detects-undeclared-muse-traffic/"
author: "Icarus"
publisher: "All Things Muse"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-09
tags: [安全]
---

{{< source-info >}}

**收录说明**：直接下载。去掉了首图 Jolly 插画与文中的「Earlier coverage」栏目。Fingerprint 的公告见正文中的 BusinessWire 链接。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：Fingerprint 于 11 月 5 日宣布扩大机器人检测，可识别其推断为 Meta Muse 的网络流量，覆盖范围同时包括 Spear Street 的 Instinct 与 xAI 的 Grok Bot，三者均被描述为不表明身份运行。Fingerprint 称 Muse“provides no verifiable identity, alters its browser fingerprint and suppresses the standard automation flags that traditional bot detection tools rely on”，其研究团队在 Muse 于 9 月发布约两周后上线了针对该流量的检测，随后在一家大型银行的登录流程中发现了 Muse 活动，而该银行的其他安全厂商未能发现，银行未具名。文中补充了一处限定：DataDome 发现 Meta 自 10 月 12 日前后开始在部分 Muse 请求上测试 Web Bot Auth 签名，签署量小且在增长，Meta 未公开确认，Fingerprint 的公告未提及此事。Fingerprint 还称 2026 年过半网络流量已非人类，其报告发现 79% 的金融机构曾发现冒充 AI 助手的恶意机器人或爬虫，但 79% 这一数字来自对其金融服务客户的调查，而非对开放网络的测量。

**保留理由**：已收资料中尚无 Fingerprint 这家厂商对 Muse 的检测视角，也无 Muse 出现在银行登录流程中的记录；本篇补上了「未表明身份的 Muse 流量可被第三方推断识别」这一环节，与同轮收录的 DataDome 流量统计、Web Bot Auth 签名测试两篇形成对照。

---

Fingerprint 的机器人检测现在可以标记其推断为 Meta Muse 的流量；该厂商称，Muse 不提供可验证的身份，并压制通常的自动化标记。它称在一家大型银行的登录流程中发现了 Muse 活动。

设备智能厂商 Fingerprint 表示，其机器人检测现在可以识别它推断为 Meta Muse 的网络流量，尽管该智能体访问网站时并不表明自己的身份。该公司[于 11 月 5 日宣布扩大检测范围](https://www.businesswire.com/news/home/20261104999557/en/Fingerprint-Expands-Bot-Detection-to-Uncover-Hidden-Muse-Instinct-and-Grok-Bot-Traffic-as-AI-Agents-Increasingly-Conceal-Their-Identities)，覆盖 Muse，以及 Spear Street 的 Instinct 和 xAI 的 Grok Bot；Fingerprint 称这三个智能体都在不声明身份的情况下运行。

据 Fingerprint 称，Muse「不提供可验证的身份，会改变其浏览器指纹，并压制传统机器人检测工具所依赖的标准自动化标记」。该公司称，其研究团队在 Muse 于 9 月发布约两周后上线了针对推断为 Muse 的流量的检测，随后在一家大型银行的登录流程中发现了 Muse 活动，而该银行的其他安全厂商未能标记。Fingerprint 未点名该银行。

## 网站为何在意智能体是否表明身份

无法识别访客的网站无法决定如何处置它。银行和零售商在过去两个月里逐一做出这一决定：[加拿大银行采取行动封堵 AI 智能体](https://www.allthingsmuse.com/articles/canadian-banks-block-ai-agents-muse/)、[JPMorgan 采取行动封堵外部智能体进入客户账户](https://www.allthingsmuse.com/articles/jpmorgan-blocks-ai-agents-muse-accounts/)，以及 [The RealReal 在 Muse 让其商品无法购买后收紧了机器人防御](https://www.allthingsmuse.com/articles/the-realreal-tightens-bot-defenses-against-muse/)。共同点是身份识别。带有可验证签名的请求可以按其本身情况被允许、限流或封堵。完全无法识别的请求则迫使网站在封堵所有自动化与不加检查地放行之间做粗放的选择。

[DataDome 统计到 9 月 22 日至 10 月 3 日期间其网络上有 2910 万次 Muse 请求](https://www.allthingsmuse.com/articles/datadome-muse-29-million-requests/)，使 Muse 占其 9 月所见全部智能体浏览器请求的三分之一。Fingerprint 补充说，2026 年全部网络流量中超过一半已不再是人类，其最近的报告发现 79% 的金融机构曾发现冒充 AI 助手的恶意机器人或爬虫。这两个数字都是 Fingerprint 自己的，而 79% 这一数字来自对其金融服务客户的调查，而非对开放网络的测量。

## 已签名流量带来的那点复杂情况

Fingerprint 将 Muse 描述为没有可验证身份的智能体，这一点需要一处限定。DataDome 的威胁研究负责人[在 10 月下旬发现，Meta 已自约 10 月 12 日起开始在一些 Muse 网络请求上测试 Web Bot Auth 签名](https://www.allthingsmuse.com/articles/meta-muse-web-bot-auth-signed-requests/)。已签名的量很小且在增长，Meta 尚未公开确认该测试。Fingerprint 的发布稿没有提到这一点。

这两项发现并存而不相互矛盾。小规模的签名测试不会改变 Muse 流量的大体情况：这些流量到达时未签名，并且按 Fingerprint 的说法，会主动压制那些本可将其标记为自动化的标记。在 Meta 为其智能体发出的大部分内容签名、或公开表示打算这样做之前，像 Fingerprint 这样的厂商只能从浏览器、设备、网络和行为信号中推断身份，并为每项判定标注高、中或低置信度分数。

## 另外两个智能体

据 Fingerprint 称，Spear Street 的餐厅预订智能体 Instinct 使用人类凭证登录网站，包括通过短信向用户索取多因素认证码，而不对其流量签名。在 CNN 报道的一个案例中，Instinct 代表某位用户每小时向预订平台 Resy 发送数百次请求，该账户被停用。

Fingerprint 称，Grok Bot 过去通过用 Web Bot Auth 签署请求来表明自己，但在 10 月 9 日前后停止了这一做法。「越来越多的 AI 智能体在访问网站时不披露身份，而一些过去会披露的，比如 Grok Bot，已经停止披露，」Fingerprint 首席执行官 Dan Pinto 在公告中说。

对这三个智能体的检测现已通过 Fingerprint 的机器人检测产品提供，途径包括其 JavaScript 代理、服务器 API、规则引擎和 MCP 服务器。对于正在决定是否放行智能体的网站，Fingerprint 的卖点是：它们可以对未声明身份的智能体会话限流，使其无法比人类用户更快地刷新或交易；或在某个会话进入登录流程时触发追加认证，而不是直接封堵每一个自动访客。
