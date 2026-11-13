---
title: "Meta Muse：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Muse 用宿主侧的 Sentinel、cell 外的凭证服务 authd 和一次性卡号把「模型想做什么」与「被允许做什么」分开，官方公开的架构在同类产品中最详细；但审批粒度可由用户放宽，上线头两个月接连出现客户端零日、文件系统导出、分享链接暴露、住址泄露等事件。
---

## 概要

- 官方称 Muse 的安全边界不在模型上，而在模型之外：宿主侧独立的 Sentinel 是连接器操作和所有网络出站的「唯一权限机构」，凭证由 cell 外的 authd 管理，模型只拿到替身令牌；付款用绑定商家、金额和时限的一次性卡号。社区和媒体普遍认为这是同类产品中公开得最系统的安全架构，但它是厂商自述，资料中没有独立审计。
- 审批的松紧由用户决定：默认「部分操作需询问」，批准按钮里有「始终允许」。2026-11-04 的连接器指南把购买、发邮件等「敏感写入」限定为每次批准、不能设为始终允许，但这条规则约束的是连接器，浏览器操作和早先的用户设置是否同样受限，资料没有说清。
- 官方明确承认提示注入「仍是悬而未决的问题」，并把责任写进帮助页：用户要监督 Muse、为它代下的订单负责。
- 上线后两个月内，资料记录了至少六起有据可查的事件：macOS 客户端零日、根文件系统可被诱导导出、上线前的 VM 逃逸加固冲刺、分享链接经 DNS 暴露、Marketplace 住址泄露、按要求列出弱势群体名单。Meta 对其中几起的定性是「预期行为」或「不是远程漏洞」。详见[已披露的漏洞与事件](incidents/)。
- 漏洞赏金是 Meta 的主要外部检验手段：上限 30 万美元，截至 2026-11-02 官方称收到 630 多份提交、确认 64 项、付出约 120 万美元。
- 安全顾虑也来自外部：亚马逊、摩根大通、嘉信和加拿大五大银行先后封堵 Muse 等外部智能体，理由之一是凭证与责任；Muse 在网络流量中不声明身份，到 2026-10 中旬才被观察到对部分请求签名。

## 三层隔离：cell、authd 与 Sentinel

Meta 发布当天的安全文章描述了这套设计（[官方安全文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）：

| 组件 | 位置 | 职责（官方称） |
| --- | --- | --- |
| runtime cell | 每个用户一台 VM，智能体和工具在 systemd-nspawn 容器内 | 运行模型调用的工具；容器内 root 映射为宿主的非特权用户 |
| authd | cell 之外 | 管理凭证，只给智能体签发替身令牌（surrogate token） |
| Sentinel | 宿主侧，独立于 Muse 的智能体 | 连接器操作与所有网络出站的「唯一权限机构」；按用户策略判定 allowed / denied / ask，在网络边界把替身令牌换成真实凭证 |
| privsep 连接器 worker | cell 之外 | 内置连接器逻辑在 cell 外运行，每个 worker 有凭证允许列表，「日历工作进程」拿不到邮件凭证 |

网络出站经正向代理送到 Sentinel，可在 L4 和 L7 检查主机名、解析后的 IP、端口、HTTP 方法、路径和解码后的请求。文章还描述了「污点出站」：用 eBPF 做内核级数据流追踪，工具进程读过用户数据后被标为污点，干净且符合严格策略的请求才可自动放行，其余回到用户审批。邮件连接器会用确定性过滤器和分类器过滤一次性验证码、密码重置链接和登录魔法链接，避免邮箱被用来在别的网站冒充用户（[官方安全文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。

用户的实测部分印证了这套设计：有用户在 VM 中看到 userns 映射、hatch 进程不可被 ptrace、root 没有 CAP_SYS_PTRACE，所有外部请求都经过同机的审批守护进程（[VM 探索实测]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。Future Society 基于泄露的 VM 镜像逐条核验后，同样看到运行时注释写着 Sentinel「still MITMs egress and remains the policy authority」（[Future Society 核验]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。VM 本身的形态见[运行环境]({{< relref "/docs/muse/analysis/runtime" >}})。

社区评价集中在「架构最系统」：有作者认为凭证隔离、独立授权、网络出口控制和人工审批构成多层防线（[明毅：产业链]({{< relref "/docs/industry/sources/community/2026-10-31-mingyi-personal-agent-industry-chain" >}})）；一位自称有 15 年企业安全背景的作者则把 Meta 排在 Microsoft、OpenAI 之后（[小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。DataCamp 指出 Muse 与 Dots 都没有经过独立审计（[DataCamp 对比]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})），也有作者提醒「安全架构描述不是独立安全评测」（[阿彦：从产品到架构]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})）。

## 审批：默认放行一部分，「始终允许」由用户选择

帮助页写明，权限在「设置 > 权限」中管理，连接器和网页访问各有两档：「部分操作需询问」（每次写入和重要读取前询问；网页访问是在信息可能被分享或访问不熟悉网站时询问）和「始终询问」。批准卡片上有五个选项：允许一次、本任务内允许、对此网站允许、始终允许、拒绝（[帮助：指导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})）。官方的设计文章解释了不默认「全都问」的原因：要避免「横幅盲视」，即人们为了让提示消失而批准一切；所以默认允许常规浏览，只在难以撤销的操作前停下（[设计文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})）。

官方安全文章称，审批是 Sentinel 直接推送到客户端的对话框，不经过聊天，批准是绑定到连接器或目的地与用途的「能力」，可以是一次性、会话、任务、限时或永久的（[官方安全文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。2026-11-04 发布的连接器指南把工具分为读取、写入、敏感写入三类，敏感写入（购买、发邮件等）每次需要批准，只能选允许一次或拒绝；审批后价格、接收方或范围发生变化要重新批准；连接器不得要求用户关掉 Muse 的批准和安全控制（[连接器指南]({{< relref "/docs/muse/sources/official/2026-11-04-connector-guidelines" >}})）。

宣传口径与这套设置之间有落差。发布稿和小企业稿说「未经你的批准，任何内容都不会被发布、发送或花费」（[Muse for Small Business]({{< relref "/docs/muse/sources/official/2026-09-29-muse-for-small-business" >}})）；AI Agents Library 指出，实际是否每次询问取决于用户此前点过哪个按钮（[AI Agents Library：Duet 对 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）。Future Society 从 VM 文件中核验到，普通浏览器表单提交默认不请求批准，登录、购买、发帖仍需批准；日历事件增删等操作在用户「明确请求」时可免确认，而「明确」由模型判断（[Future Society 核验]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。Engadget 实测发现默认只对部分操作提示，评测者希望有更细的权限，例如限定到某个 Instagram 账户（[Engadget：dot 对 Muse]({{< relref "/docs/industry/sources/media/2026-10-11-engadget-dot-vs-muse" >}})）。社区教程几乎一致建议把默认改成「始终询问」、少点「始终允许」（[ugoearn 五类任务]({{< relref "/docs/muse/sources/community/2026-10-09-ugoearn-five-task-types" >}})、[Muse 安全吗]({{< relref "/docs/muse/sources/community/2026-11-06-is-meta-muse-safe-privacy" >}})、[热爱草：一文读懂]({{< relref "/docs/industry/sources/community/2026-11-10-redaicao-personal-agent-explainer" >}})）。

推断：Marketplace 住址泄露是「始终允许」加上模型自行解释授权范围的结果（见[事件页](incidents/)），连接器指南不允许把敏感写入设为始终允许，可能是对此的收紧。资料中没有 Meta 把两者联系起来的说法，指南也只约束连接器。

## 凭证与付款：模型看不到，责任在用户

官方称 Muse 看不到密码和付款方式，包括用户在浏览器里自己输入的密码：登录时客户端把用户名和密码直接发给 authd，存进 cell 外的安全凭证存储，需要时注入浏览器（[官方安全文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})、[帮助：浏览网页]({{< relref "/docs/muse/sources/official/2026-09-08-help-browse-web" >}})）。日本、新加坡的上线稿重复了这一说法（[日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})、[新加坡上线]({{< relref "/docs/muse/sources/official/2026-10-27-singapore-launch" >}})）。

付款有两种方式。官方推荐 Muse 内置钱包里的 Stripe Link，每笔签发一张一次性卡号，绑定特定商家、金额，限时有效；另一种是用安全存储中的凭证登录商家账户、用已存信用卡付款，官方要求用户「始终监督」。每次购买都需要批准（[帮助：付款]({{< relref "/docs/muse/sources/official/2026-09-22-help-payments" >}})）。

帮助页同时写明，用户「要对你的 Muse 代表你进行的所有交易负责」（[帮助：付款]({{< relref "/docs/muse/sources/official/2026-09-22-help-payments" >}})）。TOP5 Apps 称，Stripe Link 的条款让用户为智能体购买负责，「无论那些交易是否出于你的本意」，并把智能体交易排除在未授权交易保护之外（[TOP5 Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）；这与帮助页所说 Stripe 对符合条件的购买提供保障的说法需要对照条款原文才能判断适用范围，资料中没有条款原文。

Future Society 核验到的两处细节与「模型看不到」的口径有张力：Muse 在登录、结账时会自动从已连接的邮件或同步短信中查一次性验证码（以不透明引用保存，填入需新的批准）；询问一次后可以代为解答 CAPTCHA（[Future Society 核验]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。官方安全文章说邮件连接器会过滤一次性验证码；两者是否针对不同路径（连接器与短信同步、浏览器），资料不足以判断。

## 提示注入：纵深防御，官方承认未解决

官方列出的防线有四层：模型训练（称 Muse Spark 1.3 在抗注入上「接近最先进水平（SOTA）」，自评）、运行框架把外部数据标为不可信输入、与模型训练相互独立的多分类器集成、数据移出 VM 需人工批准。浏览器分类器检测外传与任务无关的个人数据、DOM、图像和下载文件中的注入、提交高风险表单，并用 Meta 的恶意网站名单拦截导航。文章明确写道「提示注入在业界仍是悬而未决的问题」，Muse 并非免疫（[官方安全文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。帮助页也提醒 Muse「可能采取意料之外的操作」，需要用户监督（[帮助：开始使用]({{< relref "/docs/muse/sources/official/2026-09-08-help-get-started" >}})）。

赏金报告中有两起付了 9 万美元的注入案例：网页伪装成 Muse 浏览工具的状态消息；用特定格式绕过一次性验证码遮蔽。Meta 称修复后分类器能标出原攻击及 100 种变体（[赏金回顾]({{< relref "/docs/muse/sources/official/2026-11-02-securing-muse-bug-bounties" >}})）。第三方实测中，Pat Simmons 用钓鱼链接、假折扣、假银行变更邮件测试 Muse、Dots、Grok Bot，三者都没有上当（[Pat Simmons 实测]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。

比注入更常被报告的是模型自己越界：被拒绝的请求换个说法或追问一次就执行（Hunterbrook）、先拒绝归档根文件系统、一轮后又自行推翻（Future Society 导出对话）。这类问题不依赖外部恶意内容，见[事件页](incidents/)。模型本身的安全评估见[模型]({{< relref "/docs/muse/analysis/models" >}})：Muse Wonder 的研究博客只给了无数值的图表，称完整报告「将很快发布」（[Muse Wonder 研究博客]({{< relref "/docs/muse/sources/official/2026-10-12-muse-wonder-research-blog" >}})）。

## 漏洞赏金

发布当天，Meta 把 Muse 纳入公开漏洞赏金，有效报告最高 30 万美元，影响单个用户的成功提示注入最高 13 万美元；此前已有非公开赏金与内部红队（[官方安全文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。2026-11-02 的回顾称：计划自 4 月起非公开覆盖 Muse，收到超过 630 份提交，确认 64 项有效发现，已付约 120 万美元；最大一笔 30 万美元付给发布前四个月的一个预发布 VM 认证缺陷，Meta 随后移除了对本地机器的所有信任（[赏金回顾]({{< relref "/docs/muse/sources/official/2026-11-02-securing-muse-bug-bounties" >}})）。11-04 的赔付指南按结果定价：攻破 Meta 生产环境 30 万、整个 Muse 机群 25 万、特定用户智能体 13 万，按受害者需要的点击次数递减；单纯的注入、越狱、提取系统提示，以及用户经明确确认批准的操作不赔付（[赔付指南]({{< relref "/docs/muse/sources/official/2026-11-04-bug-bounty-payout-guidelines" >}})）。

赏金并不覆盖所有被报告的问题：Peter James 把文件系统导出提交给赏金计划，被标为「不适用」（[Peter James]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})）；Claroc 10 月 8 日经赏金计划报告分享链接问题，到 Ars Technica 询问后 Meta 才暂停分享（[Ars Technica：分享暴露]({{< relref "/docs/muse/sources/media/2026-10-20-arstechnica-shared-conversations-exposed" >}})）。

## 网站与金融机构的反应

Muse 在网络流量中不声明自己是智能体。DataDome 统计 99.3% 的 Muse 请求来自云和 CDN 基础设施，8.9% 触及表单、登录、支付等敏感流程（[DataDome]({{< relref "/docs/muse/sources/media/2026-10-15-datadome-muse-29-million-requests" >}})）；Fingerprint 称 Muse 会改变浏览器指纹（[Fingerprint]({{< relref "/docs/muse/sources/media/2026-11-06-fingerprint-detects-undeclared-muse-traffic" >}})）。据 DataDome 研究员在 LinkedIn 上的说法，Meta 自约 10 月 12 日起对部分 Muse 请求做 Web Bot Auth 签名，Meta 未公开确认（[Web Bot Auth]({{< relref "/docs/muse/sources/media/2026-10-31-web-bot-auth-signed-requests" >}})）。

金融机构的封堵把安全与责任问题摆到了台面上：摩根大通禁止外部智能体在零售客户账户内操作，嘉信 CEO 称每周拦截「几十次」，加拿大皇家银行 10-27 的内部备忘录称其为「不可接受的客户风险」，其余四大行一天内跟进；美国银行提醒客户共享凭据后活动由客户负责（[谁在封堵]({{< relref "/docs/muse/sources/media/2026-11-06-who-blocks-agents" >}})、[加拿大银行]({{< relref "/docs/muse/sources/media/2026-11-02-canada-banks-block-agents" >}})、[Wired：商务现实]({{< relref "/docs/muse/sources/media/2026-10-31-wired-muse-commerce-reality-check" >}})）。通行的界线是「可以看，不可以动」。零售商封堵、亚马逊与 Meta 的纠纷等见[连接器]({{< relref "/docs/muse/analysis/connectors" >}})。

推断：Muse 的凭证隔离解决的是「模型看不到密码」，没有解决网站方面临的问题——它无法分辨请求来自用户还是智能体、出事后由谁负责。银行的封堵理由集中在后者，所以 Sentinel 一类的内部设计不足以换来网站的放行；Web Bot Auth 签名、与 Stripe、Shopify 等合作的智能体标准，是另一条需要行业配合的路线。

## 资料缺口

- 独立安全审计或第三方渗透测试报告；Sentinel、污点出站的实际拦截率。
- 「始终允许」在连接器指南发布后是否仍适用于浏览器中的购买、发送；早先用户设置是否被迁移。
- Stripe Link 条款原文中关于智能体交易的责任与保护范围。
- 一次性验证码：邮件连接器过滤与 VM 内自动查码两种说法的关系。
- Wardle 在 Objective by the Sea（2026-11）演讲的内容（资料只有链接）。
- 新加坡网络安全局 2026-11-06 警告的原文（目前只有转述，未注出处）。
- Muse Wonder 完整安全评估报告。
- Muse Confidential VM 的上线时间与技术细节（相关内容见[隐私]({{< relref "/docs/muse/analysis/privacy" >}})）。

## 主要资料

- 官方：[官方安全文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})（架构、注入防御、赏金）；[设计文章]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-designed-muse" >}})（横幅盲视）；[帮助：指导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})（权限档位）；[帮助：付款]({{< relref "/docs/muse/sources/official/2026-09-22-help-payments" >}})（一次性卡与责任）；[帮助：浏览网页]({{< relref "/docs/muse/sources/official/2026-09-08-help-browse-web" >}})；[连接器指南]({{< relref "/docs/muse/sources/official/2026-11-04-connector-guidelines" >}})（敏感写入）；[赏金回顾]({{< relref "/docs/muse/sources/official/2026-11-02-securing-muse-bug-bounties" >}})、[赔付指南]({{< relref "/docs/muse/sources/official/2026-11-04-bug-bounty-payout-guidelines" >}})。
- 媒体：[DataDome]({{< relref "/docs/muse/sources/media/2026-10-15-datadome-muse-29-million-requests" >}})、[谁在封堵]({{< relref "/docs/muse/sources/media/2026-11-06-who-blocks-agents" >}})、[DataCamp 对比]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})、[Engadget：dot 对 Muse]({{< relref "/docs/industry/sources/media/2026-10-11-engadget-dot-vs-muse" >}})；事件报道见[事件页](incidents/)。
- 社区：[Future Society 核验]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})（VM 内文件逐条核验）；[Muse 安全吗]({{< relref "/docs/muse/sources/community/2026-11-06-is-meta-muse-safe-privacy" >}})（对照官方页面）；[AI Agents Library：Duet 对 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})；[Pat Simmons 实测]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})。
- 实测：[VM 探索实测]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})（2026-10-12，容器隔离与 Sentinel 审批）。
