---
title: "Claude Duet：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Claude Duet 沿用 Claude 的连接器与插件生态（官方称 6,000 多个），付款则通过只在 Duet 中提供的 Link 与 Shop Pay 两个钱包；评测者认为它在 Claude 连接器之内好用，出了这个范围基本做不了事。
---

## 概要

- Duet 没有自己的连接器体系，直接使用用户在 Claude 中已连接的连接器和插件；官方称可用 Claude Marketplace 中「6,000 多个连接器和插件」。在一处断开，两处都断开。
- 没有连接器的网站，Duet 用云端自己的浏览器操作；登录 1Password 中保存的账号、Shopify 更丰富的可视化编辑器，截至 2026-11-12 的资料仍是「即将推出」。
- 付款是 Duet 独有的部分：Stripe 的 Link 与 Shopify 的 Shop Pay 两个钱包只在 Duet 中提供，不在连接器目录里，每笔购买用一次性卡。Shopify 10 月 28 日把 Shop Pay 结账开放给智能体，Duet 是首批四个之一。
- 官方资料之间有不一致：产品页的连接器列表有 Microsoft/Office 365，帮助文档写明 Microsoft 365 尚不可用，Slack 在 Duet 中也有使用限制。
- 评测者的共同判断：在 Gmail、日历、Slack、CRM、GitHub 等 Claude 连接器之内，Duet 拉数据快、读和起草好；在这之外（打电话、LinkedIn、被封锁的购物网站），它基本停住。

## 沿用 Claude 的连接器与插件

帮助文档称 Duet 支持用户在 Claude 中连接的连接器，例如 Gmail、Google Calendar、Google Drive、Slack、QuickBooks、HubSpot、Docusign 和 Calendly；每个连接都由用户自己发起，可以随时断开（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。安全文章称在一处关闭连接会在两处都关闭（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。Duet 也支持插件（例如小企业插件），并可以推荐适合的插件（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。

发布稿称 Duet 可使用 Claude Marketplace 中 6,000 多个连接器和插件，并举了一串经营类的例子：用 Gmail 和 Slack 补回复、在 QuickBooks 或 Stripe 中查未付发票并起草提醒、用 Gusto 准备并运行薪资、在 LinkedIn 发布招聘、用 Docusign 发协议、在 HubSpot 起草跟进、用 Canva 做社交媒体素材、用 Shopify 搭建与管理店铺（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。产品页同样写「6,000 多个」，列出 Stripe、1Password、Shopify、Gmail、Slack、QuickBooks、Docusign、Google Drive、HubSpot、Gusto、Microsoft/Office 365、Notion、Canva、Ramp 等（[产品页]({{< relref "/docs/claude-duet/sources/official/2026-11-05-product-page" >}})）。

AIX财经把 Duet 的 6,000 多个与 Dots 的 4,000 多款应用并列（[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})）。aiagentslibrary 提醒，连接器数量大不等于具体工作流被支持（[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）。

## 官方资料之间的不一致

| 说法 | 资料 |
| --- | --- |
| 连接器列表含 Microsoft / Office 365 | [产品页]({{< relref "/docs/claude-duet/sources/official/2026-11-05-product-page" >}})（2026-11-05 快照） |
| Microsoft 365 尚不可用；有些连接器（如 Slack）在 Duet 中有使用限制 | [帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}}) |

aiagentslibrary 和 Alarcon 都注意到了这一点（[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})、[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})）。LaoZhang AI 据此建议工作在 Microsoft 365 上的用户选别家（[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})）。Slack 的具体限制没有资料说明。

## 没有连接器时用云端浏览器

对没有连接器的网站，Duet 用云端自己的浏览器（[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。登录时密码在应用内的表单中输入，不进入聊天，也不被模型看到（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})，详见[安全]({{< relref "/docs/claude-duet/analysis/security" >}})）。发布稿称「即将推出」两项：经用户许可，用 1Password 中保存的登录信息登录网站；Shopify 更丰富的可视化编辑器（[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})）。

官方称上线前联系了几家大型网站，给它们阻止 Duet 访问的选择，「其中一些选择了这样做」；浏览器请求带独特的 User-Agent，所用公共 IP 地址也公开（[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})）。资料没有说明是哪些网站。ChatPRD 的买鞋任务中，Duet「反复遇到被封锁的购物网站」（[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。

## 付款：只在 Duet 中提供的 Link 与 Shop Pay

Stripe 新闻稿称，Anthropic 把 Link 的智能体钱包和 Stripe MCP 集成进 Duet：Link 用于付款，Stripe MCP 用于开发票和付款链接、管理商品和价格、分析收入、办理退款；Link 已为 200 多个个人智能体提供支付，包括 Muse、Grok Bot 和 Instinct（[Stripe 新闻稿]({{< relref "/docs/claude-duet/sources/official/2026-10-21-stripe-link-and-stripe-mcp" >}})，合作方自述）。

帮助文档写明两个钱包的位置和范围：

- Link 与 Shop Pay 内置于 Duet，不列在连接器目录中，在 Duet 头像菜单的付款选项里连接；Shop Pay 在移动端也可以从推荐连接器列表中选（[帮助：Link]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-link-by-stripe-with-claude-duet" >}})、[帮助：Shop Pay]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-shop-pay-with-claude-duet" >}})）。
- 它们与 Stripe、Shopify 连接器是两回事，可以分别使用（同上，[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})）。
- 只在 Duet 中可用，Claude、Cowork、Claude Code 中都不能用；限美国的 Pro、Max、Ultra 套餐，Link 另要求美国的付款方式；Link 不支持定期付款（[帮助：Link]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-link-by-stripe-with-claude-duet" >}})、[帮助：Shop Pay]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-shop-pay-with-claude-duet" >}})）。
- 有些网站会阻止 Duet 付款，用户批准后商家仍可能拒绝结账，此时用户可能要自己完成购买（同上）。

付款的审批与一次性卡机制见[安全]({{< relref "/docs/claude-duet/analysis/security" >}})。

Shop Pay 一侧，据 All Things Muse 转述 The Defiant，Shopify 在 10 月 28 日的 Fall '26 版中把 Shop Pay 结账开放给智能体，可用于非 Shopify 商店，首批智能体是 Muse、Claude Duet、Grok Bot 和 Instinct（[All Things Muse：Shop Pay]({{< relref "/docs/industry/sources/media/2026-10-31-allthingsmuse-shop-pay-off-platform" >}})，二手）。同文称 Shopify 面向智能体的连接器支持九个智能体，列出的是「Claude」，没有说明是否包括 Duet。

推断：Anthropic 没有自建支付，而是把付款交给 Stripe 和 Shopify 两个已经服务多家个人智能体的钱包。这样 Duet 的付款能力与 Muse、Grok Bot、Instinct 处在同一套基础设施上，差别主要在审批界面和限制（如禁止证券交易、转账）。Anthropic CTO Rahul Patil 在 Stripe 新闻稿中称，把 Duet 的购买建立在 Link 之上「让人们对每一美元都保持掌控」（[Stripe 新闻稿]({{< relref "/docs/claude-duet/sources/official/2026-10-21-stripe-link-and-stripe-mcp" >}})）。

## 评测：连接器之内好用，之外停住

- Claire Vo 的销售管道任务中，Duet 已能访问 Slack、邮件和 CRM，「可以很快地拉取那些数据」，用手机在 Google Docs 里做出了尚可的演示文稿，但没有按要求使用 Figma 和品牌字体（[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})）。
- ChatPRD 的 Figma 缩略图任务中，Duet 通过 Figma MCP 把新内容放进了现有模板；做发布视频时请求使用 ElevenLabs MCP 生成配音（[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。
- Aakash 把 GitHub 代码仓库挂到频道上，称这在常规 Claude 中没有；fig.blue 也提到仓库访问按频道限定（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})、[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})）。
- Aakash 的总体判断是 Duet「在 Claude 之外就停住」：没有 Link 或 Shop Pay 时不能付款，不能用 LinkedIn，不能打电话，Muse、Instinct 则能替用户打电话；它「主要在阅读和起草回复方面帮助了我，而在采取行动方面很吃力」（[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})）。
- aiagentslibrary 指出，Muse 直连 Facebook 页面、Instagram 专业账户和 Meta 广告账户，Duet 的发布材料没有确认对等的 Meta 直连；Claude 市场里有第三方连接器（如 Metricool），能否在 Duet 中完成发布流程「尚未测试」（[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})）。

AIX财经的解释是，模型公司从工作场景切入，因为工作软件大多开放接口，生活中订餐、出行、购物的入口和支付握在平台手里（[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})，资料作者观点）。

## 资料缺口

- Slack 在 Duet 中的具体限制；Microsoft 365 的上线计划，产品页与帮助文档的不一致何时、如何消除。
- 上线前选择阻止 Duet 的网站名单。
- 1Password 登录、Shopify 可视化编辑器的上线时间。
- 第三方开发者为 Duet 专门开发连接器或插件的途径（资料只说沿用 Claude Marketplace）。
- 连接器授权失效时的处理。

## 主要资料

- 官方：[推出 Claude Duet]({{< relref "/docs/claude-duet/sources/official/2026-10-21-introducing-claude-duet" >}})（6,000 多个、示例、即将推出）、[帮助：开始使用]({{< relref "/docs/claude-duet/sources/official/2026-10-30-help-get-started-with-claude-duet" >}})（连接器清单、Microsoft 365 与 Slack 限制）、[产品页]({{< relref "/docs/claude-duet/sources/official/2026-11-05-product-page" >}})（连接器列表）、[帮助：Link]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-link-by-stripe-with-claude-duet" >}})、[帮助：Shop Pay]({{< relref "/docs/claude-duet/sources/official/2026-11-04-help-shop-pay-with-claude-duet" >}})（钱包位置与范围）、[Stripe 新闻稿]({{< relref "/docs/claude-duet/sources/official/2026-10-21-stripe-link-and-stripe-mcp" >}})（Link 与 Stripe MCP）、[安全、隐私与安全性]({{< relref "/docs/claude-duet/sources/official/2026-10-23-claude-duet-safety-privacy-security" >}})（网站可选择阻止）
- 媒体：[All Things Muse：Shop Pay]({{< relref "/docs/industry/sources/media/2026-10-31-allthingsmuse-shop-pay-off-platform" >}})（首批智能体，转述 The Defiant）、[AIX财经]({{< relref "/docs/industry/sources/media/2026-11-05-aixcaijing-consensus-or-bubble" >}})（连接器数量对比、工作场景）
- 社区：[Aakash 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-31-aakash-claude-duet-review" >}})、[Claire Vo 评测]({{< relref "/docs/claude-duet/sources/community/2026-10-26-chatprd-claire-vo-duet-review" >}})、[ChatPRD：九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})、[fig.blue]({{< relref "/docs/claude-duet/sources/community/2026-10-29-figblue-duet-is-the-future" >}})、[aiagentslibrary：Duet 与 Muse]({{< relref "/docs/industry/sources/community/2026-10-22-aiagentslibrary-duet-vs-muse" >}})、[Alarcon：第一天]({{< relref "/docs/claude-duet/sources/community/2026-10-29-chris-alarcon-first-day" >}})、[LaoZhang：入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})
