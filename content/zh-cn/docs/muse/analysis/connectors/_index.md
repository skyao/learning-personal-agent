---
title: "Meta Muse：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Muse 以 Meta 审核的目录连接器为主，自定义连接器和云端浏览器兜底；生态从发布时的几十家扩展到购物、旅行、小企业和各地区本地服务，但用浏览器代替用户访问网站的路线遭到亚马逊、银行等平台方拦截，Meta 转向协议与定向合作。
---

## 概要

- Muse 接外部服务有四条路径：Meta 与服务方联合开发、审核上架的目录连接器；用户让 Muse 现场生成、Meta 不审查的自定义连接器；没有连接器时用 VM 内的浏览器操作网站；通过 Mac、安卓手机、Gadget 硬件接入本地应用和设备。
- 授权按连接器逐个管理，读写分离，许多连接器可设为只读；平台连接器默认「首次使用时询问」，非敏感工具可改为「始终允许」。官方称凭据由独立服务保管、智能体看不到，连接器操作须经 Sentinel 放行。
- 生态扩张很快：9 月 8 日发布时「几十家合作伙伴」加整个 Shopify 商品目录；9 月 23 日 Connect 加入 10 家零售商和 Expedia、Instacart 等；9 月 29 日小企业版接入 Slack、QuickBooks 等；日本、新加坡、墨西哥上线时各有本地连接器；11 月 Expedia、Uber Courier 陆续上线。
- 连接器平台对第三方开放，据 Alexandr Wang 称不到一周收到超过 1,500 份申请。2026-11-04 收集的开发者指南要求连接器在 Muse 内「完成任务」，目前不批准转账、下单等金融资金流动工具。
- 浏览器路线的代价是与平台方冲突：亚马逊 9 月 20 日屏蔽 Muse，嘉信理财、摩根大通、加拿大五大银行相继拦截；Muse 流量起初不表明身份。Meta 的回应是与 Sierra 等共同开发 Personal Agent Protocol，并定向与零售商合作。

## 四条接入路径

**目录连接器。** 帮助中心把连接器定义为 Muse 与 Meta 或第三方应用、服务之间的连接，可以在对话中说「Connect my Gmail」，也可以在「设置 > 连接器」中授权；账户中心里的 Facebook、Instagram、Threads 会自动连接（[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})）。官方安全博客称，每个连接器都与服务提供方「密切合作来集成他们的 API」，并编写 SKILL 说明；内置连接器的代码由 privsep 执行，OAuth 令牌存在用户自己的 VM 而不是 Meta 的集中式基础设施（[官方安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。帮助文档区分了「技能」和「连接器」：技能由 Meta 开发、自动可用，连接器需要用户授权外部服务（[帮助：技能]({{< relref "/docs/muse/sources/official/2026-09-08-help-skills" >}})）。

**自定义连接器。** 对目录里没有的服务，Muse 会引导用户创建自定义连接器，可能需要获取该服务的 API 信息并存入安全凭证存储（Secure Credentials Store）。帮助中心写明「Meta 不审查自定义连接器，也不审查它们如何使用你的信息」（[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})）。Engadget 实测中，Notion 就是靠 Muse 分步指引手动接通的（[Engadget 入门]({{< relref "/docs/muse/sources/media/2026-09-12-engadget-getting-started-muse" >}})）。用户 2026-10-12 的 VM 探索记录了 Muse 的自述：自定义连接器用 MCP SDK 或 API 文档现场生成，存为 Skill（[VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。这部分是 Muse 的自述，没有官方文档印证。

**浏览器兜底。** 没有连接器的网站，Muse 用 VM 内的浏览器操作；X、Threads 等由 Muse 用自己的浏览器登录后发布，Instagram 则走官方 API（[村长七天自动化]({{< relref "/docs/muse/sources/community/2026-10-03-cunzhang-seven-day-automation" >}})）。海峡时报称，新加坡没有直接集成的服务，Muse 仍可浏览网页订餐位、比价（[海峡时报]({{< relref "/docs/muse/sources/media/2026-10-28-straits-times-muse-singapore" >}})）。这条路径正是后文平台冲突的来源。

**本地设备。** Mac 上 Muse 可以读取本地应用，帮助文档同样写明「Meta 不审查这些应用」（[帮助：Mac]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})）；Apple Health、Android SMS 等连接器的权限要在设备设置中管理（[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})）。硬件方面，Meta 在 GitHub 开源了 muse-gadget-sdk（[The Verge 自制 Gadget]({{< relref "/docs/muse/sources/media/2026-10-31-verge-diy-muse-charm" >}})）；涂鸦的 Tuya Cloud Devices Skill 用一个 API 密钥经涂鸦云控制设备，收录说明称它已于 2026-11-10 合并进该仓库（[涂鸦 Skill]({{< relref "/docs/muse/sources/community/2026-11-12-tuya-cloud-devices-skill" >}})）。设备与渠道的细节见[设备]({{< relref "/docs/muse/analysis/devices" >}})。

## 连接器清单的扩张

| 日期 | 新增 | 资料 |
| --- | --- | --- |
| 2026-09-08 | 发布时「几十家合作伙伴」，可访问整个 Shopify 商品目录；付款用 Stripe 的 Link；Shop Pay、1Password「即将推出」 | [推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})、[Connect 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}}) |
| 2026-09-23 | 零售：Walmart、Best Buy、American Eagle Outfitters、DICK'S Sporting Goods、Fanatics、Gap、Michael Kors、Sephora、Ulta、Wayfair；付款：Shop Pay、PayPal；Expedia 即将推出；Instacart；工作类：Notion、Granola、GitHub、Box | [Connect 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})、[TechCrunch]({{< relref "/docs/muse/sources/media/2026-09-23-techcrunch-everything-new-muse" >}}) |
| 2026-09-29 | Muse for Small Business：Asana、Box、Canva、Dropbox、Figma、Granola、HighLevel、Intuit QuickBooks、Klaviyo、Lovable、Notion、Shopify、Slack、Stripe、Zoom，及 Facebook 公共主页、Instagram 专业账户、Meta 广告账户 | [小企业版]({{< relref "/docs/muse/sources/official/2026-09-29-muse-for-small-business" >}}) |
| 2026-10-23 | 日本：Gmail、Google 日历、Instagram、Stripe、Shopify、Trip.com、Agoda、Klook；Mercari、Money Forward ME、Ticket Pia「正在推进」 | [日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}}) |
| 2026-10-27 | 新加坡：Shopee、Lazada、Grab、ShopBack、新加坡航空、Agoda、Klook、Trip.com，「逐步推出」 | [新加坡上线]({{< relref "/docs/muse/sources/official/2026-10-27-singapore-launch" >}}) |
| 2026-10-28 | Shopify Fall '26 发布：Shop Pay 结账可在 Muse 内完成，并首次延伸到 Shopify 之外的商店，用 Visa、Mastercard、Discover 的卡组织令牌付款，商家无需新集成；据转述 The Defiant，首批接入的智能体是 Muse、Claude Duet、Grok Bot、Instinct；每笔购买由用户点「允许」，Shopify 称卡号不交给智能体 | [All Things Muse：Shop Pay 进入 Muse]({{< relref "/docs/industry/sources/media/2026-10-31-allthingsmuse-shop-pay-off-platform" >}}) |
| 2026-11-05 | 墨西哥：Cinépolis、Coppel、Despegar、Kavak、Kueski、Liverpool、Rappi，将逐步启用 | [墨西哥上线]({{< relref "/docs/muse/sources/media/2026-11-05-muse-launches-mexico" >}}) |
| 约 2026-11-04 | Expedia 连接在美国上线，距宣布约六周；支持自然语言搜索和预订酒店，不支持取消或改订 | [Skift：Expedia]({{< relref "/docs/muse/sources/media/2026-11-09-skift-expedia-live-on-muse" >}}) |
| 2026-11-10 | Uber 称 Muse 可在聊天内安排 Uber Courier 快递 | [Uber Courier]({{< relref "/docs/muse/sources/media/2026-11-10-uber-courier-deliveries" >}}) |

清单的「宣布」与「可用」之间有落差。Instacart 帮助中心写明 Muse 订单的支付要回到 Instacart 应用完成，仅限美国，不支持内嵌结账、会员定价、优惠券、自提等（据[Instacart 购物车]({{< relref "/docs/muse/sources/media/2026-11-04-muse-instacart-shopping-cart" >}})转述帮助页）；同一篇转述的连接器文档截图要求 Muse 只显示商品小计、「绝不要编造最终总价」。日本、新加坡、墨西哥的本地连接器都标注逐步推出。有社区作者提醒，合作名单很长不等于每个用户当天都能调用（[ayaner：从产品到架构]({{< relref "/docs/industry/sources/community/2026-11-08-ayaner-product-to-architecture" >}})）。截至 2026-11-12 的资料，Meta 没有公布完整的连接器清单（[Top5Apps 排名]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。

用户的文件系统导出提供了另一种视角：VM 的 `/opt/hatch/skills/` 下约 68 个技能目录，作用域配置中还出现 Slack、Dropbox、Polymarket、Canva、Klaviyo 等当时未发布的连接器名（[Peter James 文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})）；另一份泄露 VM 的审查列出 Tessie（汽车）、Philips Hue、HealthEx、Duffel（航班预订中介）等技能，以及随镜像发布但未启用的 Meta Ads 连接器同意流程（[Future Society 引文核验]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。这两份是社区对 VM 内容的读取，说明的是镜像里有什么，不代表功能已向用户开放。

## 授权粒度：读写分离、首次询问

官方说法：

- 用户选择连接哪些应用、给多少访问权限，可以随时修改或断开（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})）。权限逐个连接器管理，可设为「部分操作需询问」或「始终询问」（[帮助：指导与批准]({{< relref "/docs/muse/sources/official/2026-09-08-help-guidance-and-approval" >}})）。
- 底层服务支持时 Muse 把读写权限分开，并提供比 OAuth 范围（scopes）更细的操作级控制（[官方安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。许多连接器可设为只读；连接邮件只让 Muse「搜索」邮件，除非用户要求，不会下载整个收件箱；有些连接器会主动推送，例如日程变化时日历连接器通知 Muse，这类连接器在连接前会标明（[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})）。
- 开发者指南把工具分为读取、写入、敏感写入三类，同时含读写的按写入处理，敏感写入每次都要批准；平台连接器的读写目前默认「首次使用时询问」（Ask on first use），非敏感工具用户可选「始终允许」；OAuth 连接时应尽量提供只读选项，「连接一个账户并不意味着授权了所有操作」（[连接器指南]({{< relref "/docs/muse/sources/official/2026-11-04-connector-guidelines" >}})）。

实测与之相符：用户 2026-10-12 的探索中，Gmail 读邮件被允许、发邮件需要询问，OAuth 范围不足时 Muse 给出补授权链接（[VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})）。社区讨论称连接器是「你要干什么事的时候，它才弹出对应的连接器」，一键确认（[聚 AI 讨论]({{< relref "/docs/muse/sources/community/2026-10-04-juai-muse-discussion" >}})）；有测评者记录 Muse 在任务中途按需连接了 Google Calendar（[AI Agents Library：Duet 对比 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）。

两处值得注意的边界：

- 断开连接器只停止数据交换，之前取得的信息可能仍留在 Muse 的记忆和对话历史里（[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})），详见[隐私]({{< relref "/docs/muse/analysis/privacy" >}})。
- 「始终允许」的含义容易被误解。卫报报道的案例中，用户在 Marketplace 场景点了「始终允许」，以为之后仍会收到批准请求，结果 Muse 以他的名义把家庭住址发给了买家；Meta 称将把这一选项说明得更清楚（[卫报]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}})）。

凭据与支付方面，官方称连接器凭据由独立服务保管并做凭证替代，Sentinel 是连接器操作和网络出站的唯一放行者（[官方安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）；付款用 Stripe 的 Link，Muse 看不到密码或付款方式，官方称 Muse 是首个受 Link 购买保障覆盖的智能体（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})）。这些机制的细节与已披露的问题见[安全]({{< relref "/docs/muse/analysis/security" >}})。

## 向第三方开放：连接器平台

Meta 在 9 月向开发者开放连接器构建，入口为 muse.ai/platform（[Top5Apps 排名]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})、[小企业版]({{< relref "/docs/muse/sources/official/2026-09-29-muse-for-small-business" >}})）。据 TechCrunch 对 Connect 演讲的报道，Alexandr Wang 称不到一周收到超过 1,500 份申请（[TechCrunch]({{< relref "/docs/muse/sources/media/2026-09-23-techcrunch-everything-new-muse" >}})）。社区讨论中有人称软件进入 Muse 连接器商店后股价「一天涨百分之十起步」（[聚 AI 讨论]({{< relref "/docs/muse/sources/community/2026-10-04-juai-muse-discussion" >}})），这是讨论者的说法，资料中没有出处。

开发者指南（2026-11-04 收集，页面无日期）的主要规定（[连接器指南]({{< relref "/docs/muse/sources/official/2026-11-04-connector-guidelines" >}})）：

| 方面 | 规定 |
| --- | --- |
| 准入 | 连接器须在获批工具范围内完成任务（搜索、价格、结账、确认、取消、退款等）；只把用户送去浏览器结账「不符合完成任务的要求」；仅包装公开页面不够 |
| 提交 | 提供 API 或 MCP 文档、测试账户，经企业验证和数据处理问卷，走 platform.muse.ai 门户 |
| 审核 | 风险评估、工具审核（只批准符合政策的工具）、端到端质量检查（含人工核实敏感写入每次需批准）；因提交量大不回复状态询问 |
| 金融 | 允许只读金融数据；目前不批准账户间转账、下达交易订单等资金流动工具 |
| 数据 | 不得二次使用、出售、用于无关广告或模型训练；安全事件 48 小时内通知 Meta |
| 展示 | 获批后出现在「设置 > 连接器」，推荐展示是单独的编辑决定，不保证排名或流量 |

用户层面，Muse 没有面向用户的技能商店。安卓安装包中管理连接器的代码叫 skills，共 647 个文件，界面上一律称「连接器」，「MCP」只出现在第三方提交连接器的送审表单里（[OpenClaw 拆解]({{< relref "/docs/muse/sources/community/2026-11-04-muse-openclaw-teardown" >}})）。AI Agents Library 称 Muse 没有文档记载的 SKILL.md 安装器，但在 10 月 8 日的测试中，Muse 主动提出把用户粘贴的工作流保存为可复用技能（[AI Agents Library：Duet 对比 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）；Pat Simmons 则称 Muse 技术上也能导入技能（[Pat Simmons 对比]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。两种说法并存，能否安装第三方技能取决于「安装」的定义。

推断：从开发者指南的准入条件看，Meta 想要的不是「把网站搬进 Muse」，而是让交易在 Muse 内闭环；这与 Instacart、Expedia 早期集成仍需回到对方应用支付或改订的现状有差距，说明多数集成还处在只读或半闭环阶段。

## 平台方的拦截与 Meta 的应对

**亚马逊。** 据 GeekWire，亚马逊 9 月 20 日（周日晚）屏蔽 Muse 在 Amazon.com 代购，用户看到「Continued access by an unauthorized AI agent violates Amazon's Conditions of Use」的弹窗；亚马逊发言人给出的理由是 Meta 未事先告知、智能体浏览时不表明身份、似乎会获取并存储顾客凭证，并已要求 Meta 把亚马逊从体验中移除（[GeekWire：亚马逊屏蔽]({{< relref "/docs/muse/sources/media/2026-09-20-geekwire-amazon-blocks-muse" >}})）。DataCamp 写作 9 月 21 日（[DataCamp 对比]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})）。中国新闻周刊称亚马逊先要求 Meta 主动把亚马逊排除在支持范围外，Meta 拒绝后才开始封堵（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})）。WIRED 的说法是亚马逊认为用户会更愿意用它自己的 Alexa 购物智能体，并称亚马逊在 10 月底的那一周承认预计会与外部智能体合作（[WIRED]({{< relref "/docs/muse/sources/media/2026-10-31-wired-muse-commerce-reality-check" >}})）。

**金融机构。** 嘉信理财 CEO Rick Wurster 称公司在拦截试图转移客户资金的未授权智能体，点名 Muse，外部 AI 可以查看余额和做研究，但不能转移资金（[Bloomberg：嘉信理财]({{< relref "/docs/muse/sources/media/2026-10-16-bloomberg-schwab-blocks-muse" >}})）。2026-10-27 加拿大皇家银行通知封堵第三方个人智能体，其余大银行数日内跟进（[加拿大银行封堵]({{< relref "/docs/muse/sources/media/2026-11-02-canada-banks-block-agents" >}})）。

**零售商的「无意封堵」。** 据 All Things Muse 转述 CNBC 11 月 1 日报道，Billions Network 审计 51 家美国大型零售商的公开规则：5 家明确限制智能体，37 家因针对爬虫的旧规则无意中封堵购物智能体，没有一家提供经核实的智能体购买渠道（[零售商审计]({{< relref "/docs/muse/sources/media/2026-11-02-retailers-block-agents-audit" >}})）。合作方也有摩擦：沃尔玛是 Meta 点名的合作伙伴，但有用户报告结账环节的人机验证拦住 Muse，沃尔玛对 TechCrunch 称并非有意（[Sitedex：给网站主]({{< relref "/docs/muse/sources/community/2026-11-01-sitedex-muse-for-site-owners" >}})）。36 氪汇总的被限制名单还包括 Yelp、eBay、达美航空、摩根大通等（[36 氪：智能体被拦]({{< relref "/docs/industry/sources/media/2026-10-21-36kr-agents-blocked" >}})）。

**身份问题。** 截至 2026-11-01，Meta 没有为 Muse 公布用户代理、IP 段或签名，面向网站主的爬虫清单里也没有 Muse（[Sitedex：给网站主]({{< relref "/docs/muse/sources/community/2026-11-01-sitedex-muse-for-site-owners" >}})）。DataDome 的 Jérôme Segura 称 Meta 自 10 月 12 日前后开始悄悄测试 Web Bot Auth，签名请求覆盖 Muse 等至少两个智能体，但量较小，Meta 未公开确认；DataDome 统计 9 月 22 日至 10 月 3 日 Muse 产生 2910 万次请求，占 9 月智能体浏览器流量的 33%（[DataDome：签名请求]({{< relref "/docs/muse/sources/media/2026-10-31-web-bot-auth-signed-requests" >}})）。

**Meta 的应对。** 一是表态：据 36 氪，Meta 10 月初发表声明称「拒绝个人Agent就等于拒绝其背后的客户」（[36 氪：智能体被拦]({{< relref "/docs/industry/sources/media/2026-10-21-36kr-agents-blocked" >}})）。二是协议：据爱信邦，10 月 7 日 Meta 联合 Sierra、Walmart、Stripe、Shopify 等宣布共同开发 Personal Agent Protocol，基于 OAuth，解决商家如何识别智能体、它代表谁、能做什么（[爱信邦]({{< relref "/docs/industry/sources/media/2026-10-12-aixinbang-do-people-need" >}})）；加拿大银行一文把它视为长期方案。三是定向合作：结账上，Shopify 商品走 Universal Commerce Protocol，其他商家用 Link 访客结账（据 [Muse 101：智能体购物]({{< relref "/docs/muse/sources/community/2026-11-04-muse-101-agentic-commerce" >}}) 转述 Retailgentic 等）；沃尔玛 10 月为智能体开设专门通道，每个智能体单独建档、设消费上限（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})）。

推断：Muse 的连接器策略呈双轨。合作方走目录连接器和协议，非合作方靠浏览器「代用户访问」。后者覆盖面广，但身份不透明、依赖用户凭据，正是亚马逊和银行给出的拦截理由。从 Web Bot Auth 测试和 Personal Agent Protocol 看，Meta 正在把浏览器流量也纳入可识别的体系，但截至 2026-11-12 的资料，两者都没有公开落地。

## 资料缺口

- 完整的连接器清单及各连接器的上线状态、地区可用性；宣布的 10 家零售商中实际已上线的有哪些。
- 自定义连接器的官方技术说明（是否基于 MCP、是否可分享），目前只有 Muse 的自述和帮助中心的一句话。
- 连接器平台的审核数据：获批数量、平均审核周期、被拒原因。
- Personal Agent Protocol 的规范文本、时间表与参与方的一手公告；Meta 对 Web Bot Auth 测试的确认。
- 亚马逊与 Meta 谈判的后续，以及 WIRED 所说亚马逊「预计与外部智能体合作」的一手出处。
- 交易抽佣或连接器分成：Expedia 称经济模式仍在制定，其他合作方没有披露（见[商业与规模]({{< relref "/docs/muse/analysis/business" >}})）。

## 主要资料

- 官方：[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})（授权、只读、自定义连接器不审查、断开后数据去向）；[官方安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})（privsep、OAuth 令牌存放、读写分离）；[连接器指南]({{< relref "/docs/muse/sources/official/2026-11-04-connector-guidelines" >}})（准入、审核、金融限制）；[Connect 全部发布]({{< relref "/docs/muse/sources/official/2026-09-23-connect-2026-everything-announced" >}})（新增零售商）；[小企业版]({{< relref "/docs/muse/sources/official/2026-09-29-muse-for-small-business" >}})（工作类连接器）；[日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})、[新加坡上线]({{< relref "/docs/muse/sources/official/2026-10-27-singapore-launch" >}})（本地连接器）。
- 媒体：[GeekWire：亚马逊屏蔽]({{< relref "/docs/muse/sources/media/2026-09-20-geekwire-amazon-blocks-muse" >}})；[WIRED]({{< relref "/docs/muse/sources/media/2026-10-31-wired-muse-commerce-reality-check" >}})（零售商合作与立场变化）；[Bloomberg：嘉信理财]({{< relref "/docs/muse/sources/media/2026-10-16-bloomberg-schwab-blocks-muse" >}})；[加拿大银行封堵]({{< relref "/docs/muse/sources/media/2026-11-02-canada-banks-block-agents" >}})；[零售商审计]({{< relref "/docs/muse/sources/media/2026-11-02-retailers-block-agents-audit" >}})；[DataDome：签名请求]({{< relref "/docs/muse/sources/media/2026-10-31-web-bot-auth-signed-requests" >}})；[Skift：Expedia]({{< relref "/docs/muse/sources/media/2026-11-09-skift-expedia-live-on-muse" >}})；[Instacart 购物车]({{< relref "/docs/muse/sources/media/2026-11-04-muse-instacart-shopping-cart" >}})；[TechCrunch]({{< relref "/docs/muse/sources/media/2026-09-23-techcrunch-everything-new-muse" >}})（1,500 份申请）；[卫报]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}})（「始终允许」案例）；[36 氪：智能体被拦]({{< relref "/docs/industry/sources/media/2026-10-21-36kr-agents-blocked" >}})。
- 社区：[Sitedex：给网站主]({{< relref "/docs/muse/sources/community/2026-11-01-sitedex-muse-for-site-owners" >}})（身份标识）；[Muse 101：智能体购物]({{< relref "/docs/muse/sources/community/2026-11-04-muse-101-agentic-commerce" >}})（结账协议）；[OpenClaw 拆解]({{< relref "/docs/muse/sources/community/2026-11-04-muse-openclaw-teardown" >}})（安装包中的 skills）；[Peter James 文件系统导出]({{< relref "/docs/muse/sources/community/2026-09-22-peter-james-muse-filesystem-export" >}})、[Future Society 引文核验]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})（VM 内的技能与未发布连接器）；[AI Agents Library：Duet 对比 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})（实测按需连接）。
- 实测：[VM 探索]({{< relref "/docs/muse/sources/exploration/2026-10-12-muse-vm-exploration" >}})（2026-10-12，Gmail 读写权限、自定义连接器自述）。
