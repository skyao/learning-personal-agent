---
title: "六款个人智能体对比：小企业该先试哪一款"
linkTitle: "六款智能体对比"
date: 2026-11-05
originalTitle: "AI Agents Compared: Which One Should a Small Business Try First? (2026)"
sourceUrl: "https://freistyle.ai/blog/ai-agents-compared-small-business"
author: "Dominic Frei"
publisher: "Freistyle AI"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-06
tags: [开放与价格, 安全, 实测评测]
products: [dots, claude-duet, muse, grok-bot, gemini-spark, microsoft-autopilot]
---

{{< source-info >}}

**收录说明**：直接下载。去掉了站内推荐工具、订阅提示与相关文章栏目。文中称 Muse「仅限美国」，与事实不符（当时 Muse 已在加拿大、日本、新加坡上线，见已收页面），照录原文。作者在文末声明 Freistyle AI 参加 Anthropic 的创业计划（获免费 Claude 额度）。文中亦覆盖 Gemini Tasks 与 Copilot Cowork，Copilot Cowork 未纳入跟踪清单。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：作者依据各厂商 10 月 27–28 日的官方公告、帮助与定价页，对比六款个人智能体（dots、Duet、Gemini Tasks、Muse、Grok Bot、Copilot Cowork）在可用地区、账号类型、套餐价格、训练数据使用、审批规则与凭证存放上的差异。多数小企业目前用不上多数产品，地区与账号限制先排除了大半；作者的建议是选已有所用数据的那一款，先以只读任务试一周，发送、付款与删除一律保留审批。按作者 15 年企业安全背景的判断，Microsoft 与 OpenAI 的说明最完整，Meta 凭 Sentinel 设计紧随其后，Google 的 Tasks 要求开启活动记录（含训练与人工抽查），xAI 公布的资料最少。

**保留理由**：同一时期少有的六产品横向对照，以“能否用上”为切入点系统比较了各家的准入、定价与数据治理，并附可操作的一周试用流程；Muse 部分的 Sentinel 与审计说明与已收官方资料相互印证。

---

来自 OpenAI、Anthropic、Google、Meta、xAI 与 Microsoft 的六款常驻智能体（always-on agent）：它们能做什么、今天谁能用上、它们会如何处理你的数据，以及如何安全地配置其中之一。

作者：Dominic Frei · 2026 年 11 月 5 日 · 阅读时长 16 分钟

要点

- 2026 年有六款常驻 AI 智能体发布或进入小企业视野：ChatGPT dots（OpenAI，9 月 29 日）、Claude Duet（Anthropic，10 月 21 日）、Gemini 中的 Tasks（Google，原名 Spark）、Muse 与 Muse for Small Business（Meta，9 月）、Grok Bot（xAI，8 月）以及 Copilot Cowork（Microsoft，6 月）。六款都运行在自己的云电脑上，你合上笔记本电脑它们仍会继续工作。
- 其中大多数目前对大多数小企业还不可用。Duet 是面向 Claude Pro 和 Max 的美国候补名单。Muse 仅限美国。Gemini 中的 Tasks 需要个人账号，且不在 EEA（欧洲经济区）、瑞士、英国或尼日利亚提供。dots 先在符合条件的市场面向 ChatGPT Pro 与 Business Premium 推出。Cowork 需要 Microsoft 365 Copilot 许可证。
- 每家厂商都说自己的智能体在发送、付款或删除之前会先询问。它们的差别在于你的数据会怎样：OpenAI 与 Microsoft 默认不用企业工作区内容训练，Meta 允许你退出，Google 的 Tasks 要求开启活动记录（Keep Activity），而 xAI 的 Bot 页面完全没有数据说明。
- 合适的第一款智能体，是那个就住在你业务已经在的地方的智能体：Gmail 与 Google Workspace 指向 Gemini 中的 Tasks，Instagram 与 WhatsApp 指向 Muse，Microsoft 365 指向 Cowork，ChatGPT 指向 dots。先交给它一项只读工作，并让每一次发送都保留在你的审批之后。

AI 智能体（AI agent）是一种助手：它在自己的云电脑上工作，连接你的应用，在你做别的事情时持续推进，而不是一次只回答一个问题。2026 年，每家主要 AI 公司都推出了一款：OpenAI 的 dots、Anthropic 的 Claude Duet、Google 的 Gemini 中的 Tasks、Meta 的 Muse、xAI 的 Grok Bot 与 Microsoft 的 Copilot Cowork。对小企业来说，有用的问题是：你究竟能用上哪一款——因为地区、账号类型与套餐今天就把大多数产品排除在外——以及哪些工作可以最先安全地交出去。简短的回答是：选那个就住在你业务已经在的地方的智能体，给它一项只读工作做一周，并让每一次发送、付款与删除都保留在你的审批之后。

我在 2026 年 10 月 27 日至 28 日之间读了每家公司的公告、帮助页与定价页。六家公司、六款产品，所以我读的时候有些内容已经变了，等你读到的时候有些还会再变。

## 什么才是 AI 智能体，它和聊天机器人有什么不同？

聊天机器人只回答。智能体会动手去做，而且是在你不在的时候做。本文中的智能体与大多数人使用的聊天窗口有四点不同：

- 自己的电脑。OpenAI 的 dots、Claude Duet、Muse 与 Grok Bot 各运行在一台带自己浏览器的云机器上。Gemini 中的 Tasks 与 Copilot Cowork 也运行在云中。你的笔记本电脑可以合上。
- 连接的应用。智能体在你连接之后会读取你的收件箱、日历、文件、店铺或 CRM，并能在其中操作。
- 目标而非问题。你交给它「盯着我的收件箱并起草回复」或「下周约好三家供应商」，它会一步步推进。
- 审批。每家厂商都说自己的智能体在敏感操作（如发送、付款或删除）之前会停下并询问你。

最后一点就是风险的全貌。一个会读取你邮件的智能体，会暴露在你邮件中的一切之下，包括骗子藏在某条消息里的指令。OWASP 将提示注入（prompt injection）列为 AI 应用的头号风险（[OWASP](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)），Google 自己的帮助页也警告说，网站、邮件或文档可能含有隐藏指令，让智能体分享你的私人信息，或把你的邮件发送到外部服务（[Google Help](https://support.google.com/gemini/answer/17094507?hl=en)）。下文每一节都请记住这一点。

## 六款智能体一览

| 智能体 | 厂商 | 发布时间 | 今天谁能用 | 付费多少 |
| --- | --- | --- | --- | --- |
| dots | OpenAI | 2026 年 9 月 29 日 | 符合条件的市场中已启用管理员权限的 ChatGPT Pro、Business Premium 与 Enterprise | 首个 dot 已包含：Pro 每月 100 美元起；Business Premium 每用户每月 125 美元，或按年付费 100 美元 |
| Claude Duet | Anthropic | 2026 年 10 月 21 日，研究预览 | 美国通过候补名单的 Claude Pro 与 Max 订阅用户 | 包含在套餐用量内：Pro 每月 20 美元（按年 17 美元），Max 100 美元起 |
| Tasks in Gemini | Google | 2026 年 5 月以 Spark 之名推出，后更名为 Task | AI Pro 或 Ultra 上的个人 Google 账号；不在 EEA、瑞士、英国或尼日利亚提供 | Google AI Pro 每月 19.99 美元，Ultra 99.99 美元起 |
| Muse 与 Muse for Small Business | Meta | 2026 年 9 月 8 日与 9 月 29 日 | 仅限美国；在 Muse 应用或 WhatsApp 中给它发消息 | 多数用途免费；付费套餐 Power 每月 20 美元、Maximum 每月 100 美元 |
| Grok Bot | xAI | 2026 年 8 月 11 日，beta | Premium、Super、Ultra 与 Teams 套餐；提供 macOS、Windows、Linux 与 iOS 应用 | Premium 每月 30 美元，Super 100 美元，Ultra 200 美元，Teams 每用户 30 美元起 |
| Copilot Cowork | Microsoft | 2026 年 6 月 16 日 | 持有 Microsoft 365 Copilot 许可证并由管理员开启的企业 | 在许可证之外：按任务以 Copilot Credits 计费，每个 0.01 美元 |

价格为美国价格，来自各公司自己的定价页或公告页，核对于 2026 年 10 月 27 日与 28 日。xAI 在 10 月更改了套餐名称，因此名称可能与你在别处看到的不同。

## 每一款能为企业做什么

### ChatGPT dots

OpenAI 将 dots 描述为常驻智能体，拥有自己的云电脑与浏览器，可通过插件连接 4,000 多个应用，你可以从 ChatGPT、Slack 或 Teams 给它发消息或通话。dot 会逐渐了解你的偏好，并在后台做 OpenAI 所称的主动研究（proactive research），使用的是无法发送消息或更改内容的只读工具。它自带一套规则，规定何时行动、何时询问，你可以用自定义规则（Custom Rules）补充自己的规则，还有一个自动复核步骤会检查可能影响你账户的操作。OpenAI 自己举的例子是一位早期测试者，其 dot 发现了一张未发送的发票，准备好它，并在获批后发出（[OpenAI，2026 年 9 月](https://openai.com/index/introducing-dots/)）。

首个 dot 包含在 ChatGPT Pro 或 Business Premium 套餐中，与它的对话不计入你的用量上限。Business Premium 席位每用户每月 125 美元，或按年付费 100 美元，用量是标准 25 美元席位的五倍（[OpenAI，2026 年 8 月](https://openai.com/index/premium-seats-chatgpt-business/)）。如果你用的是 Plus，你有用于一次性浏览任务的「agent mode」，但没有 dot。OpenAI 自己的警告同样适用：dots 仍可能出错，所以要复核有后果的工作。

### Claude Duet

Claude Duet 是一个独立应用，Claude 在其中作为主动型智能体工作：早间简报，你的收件箱、日历与后续跟进，构建仪表盘这类更大的任务，以及在需要决策时给你发消息。它运行在自己的云电脑上，使用你已连接的应用（Anthropic 列出 6,000 多个连接器与插件，包括 Gmail、Google Calendar、Slack 与 Stripe），并在发送消息或付款等敏感操作前请求批准。登录与审批都在云电脑上完成，因此模型看不到你的凭证（[Anthropic](https://claude.com/product/claude-duet)）。

它是面向美国 Claude Pro 与 Max 订阅用户、通过候补名单开放的研究预览，支持 iOS、Android 与 claude.ai，由 Opus 5.5 驱动，其用量从你现有套餐中扣除。Team 与 Enterprise 套餐尚未包含在内。Anthropic 自己提示的注意事项是：它可能误读某个对话串，或误判什么算紧急。对美国以外的企业来说，它是一个观察项，而不是一个选项。

### Gemini 中的 Tasks

Google 的这款智能体 2026 年 5 月以 Spark 之名推出，现在叫 Task，位于 Gemini 应用中的 Chat/Task 切换之后。它处理邮件、日历、Docs 与 Drive，可按计划一次运行最多 15 项任务，自 7 月起能在美国于 Chrome 中浏览。它需要 Google AI Pro 或 Ultra 套餐、个人 Google 账号、开启 Keep Activity 并主动选择加入 Personal Intelligence，且在 EEA、尼日利亚、瑞士或英国不可用（[Google Help](https://support.google.com/gemini/answer/17094507?hl=en)）。它在发送、更改或删除数据，购买、付款或提交表单之前会询问，并把密码与付款详情交回给你。

个人账号这条规定，是对使用 Google Workspace 的企业而言的症结所在。我在[Gemini 中的 Tasks 指南](https://freistyle.ai/blog/gemini-spark-for-small-business)里梳理了其条件、数据条款与一次 7 天测试，也在 [Gemini 的新企业中心](https://freistyle.ai/blog/gemini-business-hub-small-business)里梳理了 Google 10 月新增的那个独立企业中心。

### Meta Muse 与 Muse for Small Business

Muse 是 Meta 的个人智能体，2026 年 9 月 8 日在美国上线，覆盖 iOS、Android、muse.ai 与 WhatsApp。它运行在 Meta 所称的 Muse Secure VM 上——一台带有自己浏览器的专用云电脑，旁边还有一个独立的 Sentinel 智能体，Muse 发往互联网的任何内容都须经它批准。Muse 在发送邮件或购物等敏感操作前会与你确认，保留审计记录，且看不到你的密码或付款方式。你可以选择不让自己的交互被用于训练 Meta 的模型（[Meta，2026 年 9 月 8 日](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)）。

三周后 Meta 推出 Muse for Small Business：你给它一个目标，比如寻找新客户，它会用你的 Facebook 与 Instagram 企业账号、你的 Meta 广告账户，以及 Shopify、QuickBooks、Stripe、Canva、Klaviyo、Notion、Slack、Zoom 等的连接器朝这个目标推进。Meta 举的例子包括：依据销售与活动数据制定增长计划、整理收件箱、依据广告表现起草营销活动，以及每月检查账目中的异常开支。未经你批准，它不会发布、发送或花费任何东西；Meta 说它在多数需求下免费，用量更大则有订阅套餐（[Meta，2026 年 9 月 29 日](https://about.fb.com/news/2026/09/introducing-muse-small-business/)）。Meta 的帮助页列出付费套餐为 Power 每月 20 美元、Maximum 每月 100 美元（[Meta Help Center](https://www.meta.com/help/subscriptions/1021145227643680/)）。如果你的客户在 Instagram 找到你、在 WhatsApp 给你发消息，那么这就是为你打造的智能体——等它覆盖到你所在的国家。

### Grok Bot

来自 xAI 的 Grok Bot 是六款中最像「同事」的一款。你创建有明确职责的 Bot，每个都运行在自己的云电脑上，它们登录你的工具，并通过界面操作网站与应用，包括那些没有官方连接的应用。给 Bot 演示一次工作流程，它就会把它存为例程（routine）；多个 Bot 可以共享一个对话串，互相转交工作，并把决策上报给你。xAI 自己举的例子包括销售外联、依据通话记录更新 CRM、从邮件处理发票以及复现 bug（[xAI，2026 年 8 月](https://x.ai/news/introducing-grok-bot)）。桌面应用有 macOS、Windows 与 Linux 版，另有 iOS 版（[xAI](https://x.ai/bot)）。

在 xAI 的定价页上，Grok Bot 从每月 30 美元的 Premium 套餐起包含在内，Super（100 美元）与 Ultra（200 美元）增加用量，Teams 每用户 30 美元起，含集中计费与单点登录（[xAI](https://x.ai/pricing)）。有两点需要留意。Bot 页面完全没有说明你的数据如何处理，这在六款中并不常见；而一个用你的凭证登录网站的 Bot，是这里最强大、也最少约束的设置。在 xAI 公布数据条款之前，我会让它远离任何含客户数据的东西。

### Microsoft Copilot Cowork，以及 Autopilot

Cowork 是 Microsoft 用于在 Microsoft 365 内完成多步骤工作的智能体：你描述这项工作，它在云中跨你的文件、邮件与已连接应用运行，并返回一个完成的结果。它于 2026 年 6 月 16 日在全球正式可用，发布时运行在 Anthropic 的模型上，并处于 Microsoft 365 的信任边界之内，具备审计日志、敏感度标签与 eDiscovery。它默认关闭，由管理员开启；在 Microsoft 365 Copilot 许可证之外，按任务以 Copilot Credits 计费，每个 credit 0.01 美元，并可按租户、组与用户设置支出上限（[Microsoft，2026 年 6 月](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)）。

Microsoft 的常驻个人智能体于 2026 年 6 月 2 日以 Scout 之名推出，9 月更名为 Autopilot，它跨 Teams 与 Outlook 安排会议、标记停滞的决策，并为交付物预留时间。它面向 Frontier 组织进行私密预览，构建于开源项目 OpenClaw 之上（[Microsoft，2026 年 6 月](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)）。对使用 Microsoft 365 的小企业来说，Cowork 是现在就能用的那一个，而在任何人按下开始之前，它的计费就需要设置支出上限。

## 今天实际谁能用上它们？

比发布文章所暗示的要少。这是我会在读其他任何内容之前先看的表。

| 智能体 | 地区 | 账号类型 | 套餐 |
| --- | --- | --- | --- |
| dots | OpenAI 未列出的「符合条件市场」 | 个人 Pro，或 Business / Enterprise 工作区 | Pro、Business Premium、Enterprise beta |
| Claude Duet | 美国，候补名单 | 个人 Claude 账号 | Pro 或 Max |
| Tasks in Gemini | 不在 EEA、瑞士、英国或尼日利亚 | 仅个人 Google 账号，不含 Workspace 账号 | AI Pro 或 Ultra |
| Muse | 美国 | 个人；小企业版连接企业账号 | 免费或付费 |
| Grok Bot | xAI 未说明 | 个人，或 Teams | Premium 及以上 |
| Copilot Cowork | 全球 | Microsoft 365 企业租户 | Microsoft 365 Copilot 许可证，需管理员启用 |

瑞士或欧盟的企业只剩下 Copilot Cowork、Grok Bot，以及在符合条件的市场中的 dots。这并非偶然：那些读取你邮件、代表你行动的智能体，正是欧盟关于 AI 透明度与数据保护的规则最常触及的对象，而六家厂商中有三家选择了等待。

## 你的数据会怎样？

这是六款差异最大的地方，也是企业最该花时间阅读的地方。

| 智能体 | 用你的数据训练 | 行动前审批 | 你的密码存放在哪 |
| --- | --- | --- | --- |
| dots | 默认不用 Business、Enterprise 与 Edu 工作区内容训练；个人套餐中你可在设置里控制；主动研究不做直接训练 | 内置规则加自定义规则与自动复核；密码更改始终由你掌握 | 已保存的密码用于登录，但不暴露给模型 |
| Claude Duet | Duet 页面未说明；面向消费者的 Claude 套餐会让你选择聊天是否用于训练模型 | 在发送或付款等敏感操作前询问 | 登录发生在云电脑上，而不在模型中 |
| Tasks in Gemini | 必须开启 Keep Activity：Google 用活动数据改进服务（包括训练），并有部分人工审核，被审核的聊天最多保留 3 年 | 发送、删除、购买、付款、表单以及「使用 Google 登录」均需确认 | 你在浏览器中自行输入登录与付款详情 |
| Muse | 你可以选择退出训练；Meta 说 Muse 数据不会与其广告系统共享 | Sentinel 批准互联网访问；Muse 在发送或购买前询问 | 存放在 Secure VM 上；Muse 看不到 |
| Grok Bot | Bot 页面与公告中均未说明 | 「在需要时请求批准」 | Bot 登录你的工具；未公布细节 |
| Copilot Cowork | 受 Microsoft 365 控制措施治理：审计、保留、敏感度标签、eDiscovery | 正式可用公告中未描述；管理员支出上限，默认关闭 | 在你的 Microsoft 365 租户内 |

来源：上文各节链接的厂商页面。「未说明」是指我在 2026 年 10 月 28 日无法在厂商自己的页面上找到，并不是说厂商对你的数据做了什么坏事。

以我 15 年企业安全领域的经验看：写得最清楚的两家是 Microsoft（因为企业客户要求如此）和 OpenAI 的 dots 页面，Meta 凭 Sentinel 的设计紧随其后。Google 也说得很清楚，但它说清楚的是：Keep Activity 意味着训练与人工审核。xAI 公布的最少。对企业来说，这个顺序也是我会放心托付客户数据的顺序，而那份「绝不」清单对六款都适用：客户的个人信息与付款详情、密码、合同，以及客户以保密方式交给你的任何东西，都应排除在外。

## 用平实的话说，如何配置 AI 智能体

产品名不同，配置流程却一样。对六款中的任何一款，都是六步、约一小时：

1. 先选账号，而不是选智能体。凡是有企业套餐或工作区的地方就用它（ChatGPT Business、Microsoft 365，以及 Duet 支持后的 Claude Team 套餐），因为那些套餐默认不用你的数据训练。只有在只支持个人账号时（如 Gemini 中的 Tasks），才用一个与私人生活无关的账号。
2. 只连接一个应用，若智能体允许则设为只读。邮件通常是第一个应用。Meta 允许你只授予读取权限，或读取与发送权限；OpenAI 的主动研究在设计上就是只读的。第一天不要连接你的会计软件或广告账户。
3. 在第一个任务之前先设规则。每款智能体都有设置页，规定它能独自做什么。写下你会给新助理写的那三条规则：起草但不发送、绝不付款、绝不删除。OpenAI 称之为自定义规则；Meta 的 Sentinel 与 Google 的确认机制会替你完成其中一部分。
4. 给它一项有明确终点的工作。「每天早上总结新的客户邮件，并起草回复供我发送」是一项工作。「帮我把业务做好」只是一个愿望。
5. 一周内每天查看日志。六款都保留智能体所做之事的记录（OpenAI 的 Activity View、Meta 的审计记录、Microsoft 的审计日志、Google 的任务对话串）。去读它。数一数你重写了多少份草稿、它弄错了什么，以及它做了哪些你没要求的事。
6. 每次只扩大一步，或者停下。如果这一周干净无事，就加上日历。如果它在没有你的情况下发送、更改或花费了任何东西，当天就断开它，回到只做草稿。

快速见效

在你连接任何东西之前，打开你的已发送文件夹，数一数这一周的例行邮件：确认、约时间、「谢谢，收到了」。如果每天不足半小时，你暂时不需要智能体，一条好的提示词就够了。超过这个量，就在与你账号匹配的智能体上做一周只做草稿的试用，值得一试。

## 未经你批准，智能体绝不应该做什么？

发送、发布、付款、签字、删除，以及更改任何客户能看到的东西。六家厂商都说自己的智能体对其中大多数会停下，所以要检查的设置是：没有人把这些停点关掉。阅读、整理、总结与起草在第一天就可以放心交出去。发送与预约要等只做草稿的一周干净通过之后，一次只改一项。付款、签字、银行信息与受 NDA 约束的客户数据仍由人掌握，何况每家厂商本来就会把付款这一步交回给你。[一页式 AI 政策模板](https://freistyle.ai/blog/ai-policy-template-small-business)的第 5 节可以把它变成你团队可以签字的规则。

## 小企业该先试哪一款智能体？

选那个已经拥有你数据的，因为连接它就是全部的工作。

| 如果你的业务主要活在…… | 先试 | 原因 |
| --- | --- | --- |
| 在欧盟与英国之外、使用个人账号的 Gmail、日历与 Docs | Gemini 中的 Tasks | 它已经在你的应用里，而且 Google 的确认规则最清楚 |
| Google Workspace（工作账号） | 等待，或者如果你同时使用 Microsoft 365 就用 Copilot Cowork | Tasks 尚不支持工作账号 |
| 持有 Copilot 许可证的 Microsoft 365 | Copilot Cowork，并设好支出上限 | 在你租户现有的控制之内 |
| ChatGPT Business 或 Pro | dots | 首个 dot 已包含；工作区内容默认不用于训练 |
| 在美国、经营 Instagram、Facebook、WhatsApp 以及 Shopify 或 Stripe 店铺 | Muse for Small Business | 围绕这些连接器打造，任何发送或花费之前都需批准 |
| 在美国使用 Claude Pro 或 Max | 加入 Duet 候补名单 | 研究预览；尚不适用于欧盟 |
| 销售团队主要活在 CRM 中并且想要自主性 | Grok Bot，等数据条款公布之后 | 能力最强，文档最少 |

如果这些行都不适用，你暂时不需要智能体。在你已经付费的助手里用一条清晰的提示词，就能覆盖大多数例行回复，我的[给创业者的五条提示词](https://freistyle.ai/blog/ai-prompts-for-entrepreneurs)可以作为一个起点。

带有厂商核实价格的更完整工具清单，见[2026 年小企业最佳 AI 工具](https://freistyle.ai/blog/best-ai-tools-small-business-2026)。

## 常见问题

### AI 智能体与聊天机器人有什么区别？

聊天机器人一次回答一个问题。智能体运行在自己的云电脑上，连接你的应用，在你不在时朝一个目标推进，并在敏感操作前询问你。ChatGPT dots、Claude Duet、Gemini 中的 Tasks、Muse、Grok Bot 与 Copilot Cowork 在这个意义上都是智能体。

### 哪款 AI 智能体最适合小企业？

选那个已经拥有你数据的。对欧盟与英国之外、以 Gmail 为主的企业，是 Gemini 中的 Tasks；对美国以 Instagram 与 WhatsApp 为主的企业，是 Muse for Small Business；对 Microsoft 365，是 Copilot Cowork；对 ChatGPT Pro 或 Business Premium，是 dots。Claude Duet 是美国候补名单，Grok Bot 尚未公布其数据条款。

### 我能在 Plus 套餐上使用 ChatGPT dots 吗？

截至 2026 年 10 月还不能。dots 正在符合条件的市场向 Pro、Business Premium 以及由管理员启用的 Enterprise 工作区逐步推出。Plus 包含用于一次性浏览任务的「agent mode」。在 Pro 与 Business Premium 中，首个 dot 免费包含在内。

### Claude Duet 在欧洲可用吗？

不可用。Anthropic 于 2026 年 10 月 21 日以候补名单方式开放研究预览，面向美国的 Claude Pro 与 Max 订阅用户，覆盖 iOS、Android 与 claude.ai。Team 与 Enterprise 套餐尚未包含在内。

### AI 智能体会用我的企业数据做训练吗？

取决于厂商与套餐。OpenAI 默认不用 Business、Enterprise 或 Edu 工作区内容训练。Microsoft 的 Cowork 留在你的 Microsoft 365 控制之内。Meta 允许你退出。Google 的 Tasks 要求开启 Keep Activity，这允许训练与部分人工审核。xAI 的 Grok Bot 页面没有说明。

### AI 智能体要花多少钱？

从零到每月几百美元不等。Muse 在多数用途下免费。Gemini 中的 Tasks 随每月 19.99 美元的 Google AI Pro 提供。Grok Bot 从 xAI 每月 30 美元的 Premium 套餐起。Claude Duet 使用每月 20 美元的 Pro 或 100 美元以上的 Max 套餐。dots 需要每月 100 美元起的 ChatGPT Pro，或 125 美元的 Business Premium 席位。Copilot Cowork 在 Copilot 许可证之外按任务以每个 credit 0.01 美元计费。

### 未经批准，AI 智能体绝不应该做什么？

发送、发布、付款、签字、删除，或更改任何客户能看到的东西。每家厂商都说自己的智能体对其中大多数会停下。让这些停点保持开启，从只做草稿开始，并在第一周每天查看智能体的活动日志。

## 接下来怎么做

在「先试」表里找到你那一行，在一个企业账号上用一款只读应用配置好那一款智能体，让它在发送任何东西之前先做一周草稿。如果这一周干净无事，就扩大一步。如果你希望先把规则为团队写下来，上面那份政策模板大约需要一小时。

披露：Freistyle AI 参与 Anthropic 的创业计划，该计划为这家企业提供免费的 Claude 额度。上文的定价与功能来自各公司自己的页面。

*借助 AI 工具研究，由 [Dominic](https://freistyle.ai/about) 撰写并核实事实。*

### 来源

1. [OpenAI，Introducing dots（2026 年 9 月 29 日）](https://openai.com/index/introducing-dots/)
2. [OpenAI，ChatGPT Business 的高级席位（2026 年 8 月 10 日，2026 年 8 月 25 日更新）](https://openai.com/index/premium-seats-chatgpt-business/)
3. [OpenAI，ChatGPT 定价](https://chatgpt.com/pricing/)
4. [Anthropic，Claude Duet | 你的个人 AI 助手（访问于 2026 年 10 月 28 日）](https://claude.com/product/claude-duet)
5. [Anthropic，Claude 定价](https://claude.com/pricing)
6. [Google Gemini Apps Help，在 Gemini Apps 中管理你的任务与工作流（访问于 2026 年 10 月 28 日）](https://support.google.com/gemini/answer/17094507?hl=en)
7. [Google，Google AI 套餐与定价](https://gemini.google/subscriptions/)
8. [Meta，推出 Muse，一款个人 AI 智能体（2026 年 9 月 8 日）](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)
9. [Meta，未来属于每个人：Muse for Small Business（2026 年 9 月 29 日）](https://about.fb.com/news/2026/09/introducing-muse-small-business/)
10. [Meta Help Center，关于 Muse 订阅（访问于 2026 年 10 月 28 日）](https://www.meta.com/help/subscriptions/1021145227643680/)
11. [xAI，推出 Grok Bot（2026 年 8 月 11 日）](https://x.ai/news/introducing-grok-bot)
12. [xAI，能完成工作的 AI 队友 | Grok Bot（访问于 2026 年 10 月 28 日）](https://x.ai/bot)
13. [xAI，定价（访问于 2026 年 10 月 28 日）](https://x.ai/pricing)
14. [Microsoft，Copilot Cowork 现已正式可用（2026 年 6 月 16 日）](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)
15. [Microsoft，推出 Microsoft Scout：你的常驻个人智能体（2026 年 6 月 2 日；2026 年 9 月 25 日更名为 Autopilot）](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)
16. [OWASP GenAI Security Project，LLM01:2025 提示注入](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
