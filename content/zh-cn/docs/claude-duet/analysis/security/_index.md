---
title: "Claude Duet：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Claude Duet 的安全设计是官方资料中写得最细的部分：发送、付款、删除前出审批卡，模型之外另有两个分类器分别检查操作意图和外发内容，凭证从不进入智能体所在的机器，证券交易、转账等即使批准也不做；截至 2026-11-12 资料中没有披露的漏洞或事件。
---

## 概要

- 官方列出三条原则：审慎处理用户及他人在连接应用中分享的信息，用户始终掌控代表其采取的行动，Duet 永远看不到密码、浏览器 Cookie、登录令牌。整套设计建立在模型的安全训练和 Claude Code、Claude Managed Agents 已有的防护之上。
- 审批分三层：一般敏感操作出审批卡，可由「别再问我」放行；付款或转账、删除订单、创建账号无论批准过多少次都要再问；买卖证券、账户间转账、访问他人账号即使批准也不做。用户不在时运行的例程同样适用。
- 模型之外有两道自动检查：一个基于 Claude Code auto mode 分类器扩展的检查，判断每次操作是否符合用户意图；一个新的安全分类器检查每条外发消息，凭证、完整卡号和账号、政府证件号「绝不分享」，健康、财务等信息需用户同意。
- 凭证三种处理：密码在手机上加密、只在浏览器机器上解密；登录令牌在智能体机器上只是占位符，由机器外的代理填入；付款用限定商户和金额的一次性卡。
- 官方自己承认的问题：审批疲劳是「严重问题」、批准频率仍在调整；分类器会漏判或误标；对提示注入「没有任何防御是完美的」。评测者的体验印证了审批偏多：一次横评中 Duet 请求权限 4 次，其他智能体各 1 次。
- 测试与披露：内部评估、红队、有源码访问的外部渗透测试，纳入 HackerOne 上的公开漏洞赏金计划。资料库中没有 Duet 的漏洞或安全事件报道，但 Duet 上线时间短、开放面窄，也没有独立的安全审计。

## 三条原则与两层基础

安全文章称 Duet 建立在两层保护之上：Claude 模型本身的安全训练，以及 Claude Code、Claude Managed Agents 等产品中已有的防护；在此之上新增了针对跨账号工作和代表用户行事的保护。三条原则是：审慎处理用户及他人在连接应用中分享的信息；用户始终掌控 Duet 代表其采取的行动；Duet 永远看不到用户的密码、浏览器 Cookie、登录令牌等凭证（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。发布稿称 Duet 借鉴了同样指导 Claude Code、Claude in Chrome 的可信智能体框架（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。

## 审批的三个层级

| 层级 | 包括 | 资料 |
| --- | --- | --- |
| 需要批准 | 发送可能敏感的消息、付款、签署文件、删除；审批卡展示操作、目的地和内容（含每位收件人） | [安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})、[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}}) |
| 每次都要再问 | 付款或转账、删除订单、创建账号，不受「别再问我」规则覆盖，「无论你批准过多少次」 | [安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}}) |
| 即使批准也禁止 | 买卖证券、账户间转账等银行操作、访问他人账号 | [安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}}) |

用户不在时运行的例程（routines）享有同样的防护；用户暂时无法批准时，Duet 先做完其余部分，之后再回来请求批准（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。

官方承认审批疲劳是「一个严重问题，因为过多的请求会让人养成随手点过的习惯」，批准频率会继续调整（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。实测中审批确实偏多：ChatPRD 的九项任务横评里，Duet 请求权限 4 次，其他每个智能体只请求 1 次，作者认为「反复的批准请求会把委派变成监督」，并称 Muse 用侧边栏处理权限请求是有用的设计（[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。Aakash 的观察是正面的：Duet 起草的每封邮件、对发帖队列的每次改动都等他同意，它标出六条最糟的已排期帖子，但在他发话前没有改动任何东西（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。

## 模型之外的两道自动检查

- **操作意图检查**：每次操作的同时运行一项独立的自动检查，建立在 Claude Code 的 auto mode 分类器之上，评估操作是否符合用户的意图；它在从事工作的模型之外运行，页面中的隐藏指令无法影响它（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。发布稿的说法是 Duet 的操作「由自动模式分类器批准」（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。
- **外发内容检查**：一个新的安全分类器，与主模型分开运行，检查 Duet 即将发送的每条消息。两级规则：「绝不分享」，包括登录凭证、完整银行卡号和账号、政府身份证件号，即使用户要求也不行；「分享需同意」，包括健康、财务等信息，用户自己的请求即构成同意。被拦截的消息可以改写后交用户批准。官方承认它偶尔会漏掉某些内容，或把无害的消息标记出来（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。官方举的场景是给团队发每周回顾时，不应包含绩效评估对话这类私人细节（同上）。

与 Muse 对照，LaoZhang AI 的对照表称 Muse 有独立的 Sentinel 智能体，Duet 则是自动模式分类器加第二个分类器（[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})）；财经网科技把 Duet 的「读取、起草、准备」与「发送、付款、签署」之分，与蚂蚁灵光的 APASS、Muse 的 Sentinel 并列比较（[财经网科技]({{< relref "/docs/industry/sources/media/2026-11-06-caijingwang-transaction-management" >}})）。详见 [Muse：安全]({{< relref "/docs/muse/analysis/security" >}})。

## 凭证不进入智能体所在的机器

| 凭证 | 处理方式 | 资料 |
| --- | --- | --- |
| 网站密码 | 用户在 Claude 应用内的表单输入，用只存在于云端浏览器机器上的单次密钥加密，加密后原样传给浏览器填入网站；模型看不到、无法保存。登录表单只在应用内、只在用户请求登录时出现，绝不以链接、短信、邮件或 claude.ai 以外的网站出现 | [安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}}) |
| 登录令牌 | 沿用 Claude Managed Agents 的设计：真实令牌不进入智能体工作的机器，机器上是占位符，机器之外的代理在发请求时填入真实值 | [安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})、[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}}) |
| Cookie、网站代码 | 留在浏览器机器上，不进入 Duet 的记忆 | [安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}}) |
| 付款卡 | 每次购买用仅对该次有效、限定商户和金额的一次性卡；Duet 只看到卡类型、后四位、有效期、账单地址，看不到完整卡号或银行账号 | [安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})、[帮助：Link]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-link-by-stripe-with-claude-duet" >}})、[帮助：Shop Pay]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-shop-pay-with-claude-duet" >}}) |

1Password 登录「很快」提供，截至 2026-11-12 未见上线（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。fig.blue 认为 Duet 不存储凭证、劝阻用户交出凭证，比 Muse 的凭证存储更稳妥（[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})，资料作者观点）。

推断：把浏览器放在单独的虚拟机、只让智能体用固定命令操作，是这套凭证隔离的前提：密码在浏览器机器上解密，令牌在机器外填入，智能体所在的机器上始终没有真实凭证。用户看不到、不能接管浏览器，可能与此有关（见[运行环境]({{< relref "/docs/claude-duet/analysis/runtime" >}})）。

## 付款的批准与争议处理

- Link：每次购买前询问；用户在 Link 应用中批准最高金额之前不提交付款，所选付款方式上可能先有临时授权，商家完成购买后才最终扣款；不支持定期付款；失败的购买可能暂时显示为待处理（[帮助：Link]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-link-by-stripe-with-claude-duet" >}})）。
- Shop Pay：每次购买前询问，用户点「Review in Shop Pay」批准，使用限定于已批准金额的一次性卡（[帮助：Shop Pay]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-shop-pay-with-claude-duet" >}})）。
- 争议分工：订单、配送、退货找商店；钱包账户和扣款问题找 Link 或 Shop 支持；Duet 选错商品、店铺、数量找 Claude 支持，可直接在聊天中告诉 Duet 转交；发现不认识的购买，应拒绝待批请求、断开 Link 并联系 Link 支持（[帮助：Link]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-link-by-stripe-with-claude-duet" >}})、[帮助：Shop Pay]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-shop-pay-with-claude-duet" >}})）。

Top5Apps 转述 Link 的智能体条款称，用户要为智能体的购买负责，「无论那些交易是否出于你的本意」，智能体交易被排除在未授权交易保护之外；该文点名的是 Muse、Grok Bot、Instinct，没有点名 Duet（[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。推断：Duet 也用 Link 付款，这一条款可能同样适用，但资料没有证实。

## 提示注入与自我标识

官方称 Duet 被构建为把读到的邮件、网页内容当作信息而非指令，采用了浏览器使用研究中的提示注入防护，但「没有任何防御是完美的」，提醒用户审阅它的草稿和审批请求（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})、[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。

Duet 的浏览器请求带独特的 User-Agent 标头，所用公共 IP 地址公开，便于网站识别；上线前 Anthropic 联系了几家大型网站给予阻止的选择，其中一些选择了阻止（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。

## 测试与漏洞披露

官方称 Safeguards 团队按日常任务构建评估，每项三个版本：无害版、注入指令版、诱使越权版，与真实使用的影子流量（shadow traffic）一同运行；红队测试了泄露信息、未经批准行动、遵循恶意提示词；一家有源码访问的外部渗透测试公司做了测试，针对云端浏览器和登录表单的后续工作仍在进行；Duet 在 Anthropic 于 HackerOne 上的公开漏洞赏金计划范围内（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})、[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。发布稿 2026-10-23 在文首加注，称仍在继续开发和加强这些保护（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。

截至 2026-11-12 的资料，没有关于 Duet 的漏洞、安全事件或厂商回应的报道。PM九筒称，隐藏凭证与防范提示注入这两项，只有 Muse、Dots、Duet 的官方页面写得比较具体（[PM九筒：什么是 Personal Agent]({{< relref "/docs/industry/sources/community/2026-10-28-pmjiutong-what-is-personal-agent" >}})）。

推断：Duet 没有事件记录，不能直接说明它更安全。它上线约三周，只对受邀的美国付费用户开放，用户不能接触浏览器和运行环境，研究者可以检验的面比 Muse 小得多（对照 [Muse：安全]({{< relref "/docs/muse/analysis/security" >}})）。

## 资料缺口

- 外部渗透测试的结论、测试方，以及对云端浏览器和登录表单后续工作的结果。
- 两个分类器的误判、漏判率；内部评估的结果数字。
- Link 智能体条款对 Duet 用户的适用情况。
- 选择阻止 Duet 的网站名单。
- 独立安全研究者对 Duet 的测试。

## 主要资料

- 官方：[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})（原则、审批层级、分类器、凭证、测试）、[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})（可信智能体框架、渗透测试）、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})（禁止事项、提示注入）、[帮助：Link]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-link-by-stripe-with-claude-duet" >}})、[帮助：Shop Pay]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-shop-pay-with-claude-duet" >}})（付款批准与争议）
- 媒体：[财经网科技]({{< relref "/docs/industry/sources/media/2026-11-06-caijingwang-transaction-management" >}})（与 APASS、Sentinel 对比）
- 社区：[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})（审批次数）、[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})（审批体验）、[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})（凭证观点）、[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})（与 Muse 对照）、[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})（Link 条款）、[PM九筒：什么是 Personal Agent]({{< relref "/docs/industry/sources/community/2026-10-28-pmjiutong-what-is-personal-agent" >}})
