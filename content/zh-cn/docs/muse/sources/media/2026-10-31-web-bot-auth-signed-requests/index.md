---
title: "Meta 在悄悄给部分 Muse 请求签名，DataDome 发现"
linkTitle: "Muse 请求悄悄签名"
date: 2026-10-31
originalTitle: "Meta Is Quietly Signing Some Muse Web Requests, DataDome Finds"
sourceUrl: "https://www.allthingsmuse.com/articles/meta-muse-web-bot-auth-signed-requests/"
author: "Icarus"
publisher: "All Things Muse"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-09
tags: [安全]
---

{{< source-info >}}

**收录说明**：直接下载。去掉了首图 Jolly 插画与文中的「Earlier coverage」栏目。发表日期在窗口外（10 月 31 日），本轮经 Cloudflare 立场文件一文内链发现，属首报回填。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：DataDome 威胁研究副总裁 Jérôme Segura 在 10 月 30 日的 LinkedIn 帖子中称，Meta 自 10 月 12 日前后开始悄悄测试 Web Bot Auth，“since around Oct. 12”，签署请求覆盖 Meta-WebIndexer 与 Muse 至少两个 agent，签署量在逐步增加；Meta 未公开确认，其公开爬虫文档未提及 Web Bot Auth、HTTP message signatures 或签名密钥目录。Web Bot Auth 是 HTTP Message Signatures 的应用形式，该标准作为 RFC 9421 于 2024 年 2 月发布、由 Cloudflare 于 2025 年 5 月提议，签署方在请求中附加 Signature、Signature-Input、Signature-Agent 三个头，接收方从固定路径发布的目录取公钥验签。Muse 自 9 月 8 日美国上线以来存在身份问题：上线两周内 Amazon 以其浏览时不表明身份等理由将其屏蔽；DataDome Q3 报告称 Muse 不表明身份，同时统计其 9 月 22 日至 10 月 3 日间产生 2910 万次请求、占 9 月智能体浏览器流量的 33%。架构上，每个 Muse 用户的 agent 运行在各自的云虚拟机内并内置完整浏览器，Q3 样本中 99.3% 的 Muse 请求来自云与内容分发基础设施，其中 Cloudflare 占 81.2%、Fastly 占 18.1%，仅 0.6% 来自消费级互联网服务商。局限在于，Segura 称签署量相对较小，帖子未给出数量、占比及两个 agent 之间的分布；DataDome 已为客户增加对 Meta Web Bot Auth 请求的验证支持，但 Meta 签署大部分流量或公开表态之前，网站面对的是可验证与不可验证两类 Meta 流量。

**保留理由**：本篇是仓库中首篇记录 Muse 流量获得可验证身份（签名测试）的资料，提供了 Web Bot Auth 机制与 RFC 9421 的出处，并与 DataDome「Muse 不表明身份」的 Q3 结论形成时间线对照（测量窗口 9 月 22 日–10 月 3 日，签署始于 10 月 12 日前后）。

---

DataDome 的威胁研究负责人称，Meta 在 10 月 12 日前后开始在 Muse 与 Meta-WebIndexer 流量上测试 Web Bot Auth 签名，首次让网站有了验证 Muse 流量的方式。

据机器人管理公司 DataDome 称，Meta 已开始为其 Muse 个人智能体发出的一部分网络请求附加密码学签名，这是一次未公开宣布的测试，将首次让网站有办法验证 Muse 流量。这一发现来自 DataDome 威胁研究副总裁 Jérôme Segura，他在 10 月 30 日的 LinkedIn 帖子中描述了这一观察，[PPC Land](https://ppc.land/metas-muse-agent-gains-a-signed-id-in-a-quiet-test-datadome-finds/) 对此作了报道。

Segura 写道，Meta「自 10 月 12 日前后」开始悄悄测试 Web Bot Auth，并一直在增加至少两个 agent 的签名请求量：Meta-WebIndexer 与 Muse。他补充说，据他所知没有公开或官方公告，签名请求起初可能带有 Meta-ExternalTest 的 user-agent 标签。Meta 未公开确认这一测试，其公开爬虫文档也未提及 Web Bot Auth、HTTP 消息签名或签名密钥目录。

Web Bot Auth 是 HTTP 消息签名（HTTP Message Signatures）的一个应用形式，该标准于 2024 年 2 月作为 RFC 9421 发布，由 Cloudflare 于 2025 年 5 月提出。签署方智能体会在每个请求中附加 Signature、Signature-Input 与 Signature-Agent 头。接收网站或其前置的安全厂商会从固定路径发布的目录中获取运营方的公钥，并用其校验签名。若校验通过，说明请求来自持有私钥的一方。若未通过，该请求就是冒充者发出的，或格式有误。

## Muse 为何难以识别

自 9 月 8 日在美国上线以来，Muse 一直存在身份问题。两周内，亚马逊就阻止该智能体在 Amazon.com 上购物，据 GeekWire 报道，亚马逊列出的不满之一是该智能体浏览时不表明身份。DataDome 自己的第三季度报告把 Muse 描述为一个[不表明自身身份](https://www.allthingsmuse.com/articles/datadome-muse-29-million-requests/)的 agent，同时统计出 9 月 22 日至 10 月 3 日期间 DataDome 网络上有 2910 万次 Muse 请求，并称 Muse 占 9 月全部智能体浏览器请求的 33%。

困难部分源于架构。每个 Muse 用户的 agent 都运行在自己的云虚拟机中，内部带有完整浏览器，因此 Muse 的行为像是从数据中心而非用户手机运行的计算机使用型 agent。在 DataDome 的第三季度样本中，99.3% 的 Muse 请求来自云与内容分发基础设施，其中 Cloudflare 占 81.2%、Fastly 占 18.1%，仅 0.6% 来自消费级互联网服务商。Meta 的文档告诉网站运营方，通过爬虫在 Meta 自己网络上的来源来识别其声明过的爬虫，即查询注册在 Meta 自治系统 AS32934 下的前缀。从 Cloudflare 和 Fastly 地址发出的流量，无论由谁发送，都无法通过这项检查。对于按 Muse 这种方式构建的 agent，密码学签名是现成的验证途径，而且不依赖请求来自何处。

零售商和银行一直在逐一决定是否放智能体进来：Walmart 在 10 月推出了按智能体区分的资料，而 [The RealReal 在 Muse 让其商品列表无法访问后加强了机器人防御](https://www.allthingsmuse.com/articles/the-realreal-tightens-bot-defenses-against-muse/)，JPMorgan 则着手阻止外部智能体访问客户账户。无论哪种决定，前提都是首先能够识别该智能体。携带有效签名的 Muse 请求可以被允许、限速或封堵，而不是靠启发式规则碰运气抓到或漏掉。未签名的请求则做不到这一点。

## 仍未知的部分

这一发现有其局限。Segura 称签署量相对较小，他的帖子没有给出数量、占比，也没有给出两个 agent 之间的分布。DataDome 表示已为其客户增加对 Meta Web Bot Auth 请求的验证支持，但在 Meta 为其 agent 发出的大部分流量签名、或公开表示有此意图之前，网站面对的是两类 Meta 流量：一类可以验证，另一类更大且无法验证。

公开记录中还缺少若干其他事实。Meta 的文档未披露其密钥目录的发布位置。Meta-ExternalAgent、Meta-ExternalFetcher 或 Meta-ExternalAds 是否会签名尚不清楚。Meta-ExternalTest 是否会出现在 Meta 的爬虫列表中，还是试验期间的临时标签，也不明确。「测试」一词是 Segura 从流量中推断的，并非 Meta 给出的说法。

签名也只解决了一半问题。它说明请求由谁发出，却不说明为何发出，也不说明该 agent 会如何行事。Segura 这样表述：「随着 Muse 这样的 AI agent 开始为真实的人浏览和购物，企业需要知道哪些可以信任。签名请求验证一个 agent 确实是它声称的那一方。身份是全局中的关键一环，与意图（该 agent 实际想做什么）结合，企业就能欢迎合法 agent，把冒充者挡在外面。」

Meta 不会是第一个为 agent 流量签名的大型运营方，但会属于一个小群体。Arkose Labs 把 OpenAI 的 ChatGPT agent 描述为唯一大规模签名的 agent，后者第三季度有 78.4% 的会话带有签名。Google 表示正以身份 agent.bot.goog 试验该协议，并且只对一部分请求签名。Amazon Bedrock AgentCore 使用服务密钥为浏览器流量签名。

DataDome 于 10 月 15 日发布的第三季度报告称 Muse 不表明自身身份，而 Segura 的帖子称签名始于 10 月 12 日前后。两者并不冲突：DataDome 对 Muse 的测量窗口为 9 月 22 日至 10 月 3 日，在 Segura 给出的起始日期之前一周多就已结束，而签署量此后一直较小并在增长。

值得关注的是，Meta 是否会在 11 月 20 日其涵盖爬虫的修订商业条款生效之前记录签名，以及签名占比是否会从一次小规模测试成长为默认做法。在那之前，这个故事范围不大但真实：Muse——那个不打招呼就从云里出现、不说自己是谁的 agent——已开始在至少部分请求中携带身份标识，而决定是否放它进来的网站终于有了可以核查的东西。
