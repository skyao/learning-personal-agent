---
title: "个人智能体协议 Poppy 1.0 发布，面向全部 Muse 用户与所有 Shopify 商店"
linkTitle: "Poppy 1.0 发布"
date: 2026-11-13
originalTitle: "Personal Agent Protocol Reaches Version 1.0, Live for All Muse Users and Every Shopify Store"
sourceUrl: "https://www.allthingsmuse.com/articles/poppy-personal-agent-protocol-1-0/"
author: "Icarus"
publisher: "All Things Muse"
basedOn: "Sierra 官方博客《Releasing Personal Agent Protocol 1.0》，2026-11-13"
basedOnUrl: "https://sierra.ai/blog/releasing-poppy"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-13
tags: [发布, 连接器, 商业与规模]
products: [muse]
dateNote: "页面显示 2026 年 11 月 13 日，元数据 article:published_time 为 2026-11-14T00:06:00Z（美东 11 月 13 日 19:06）。"
---

{{< source-info >}}

**收录说明**：直接下载。去掉了首图与文中两张 Jolly 插画及站内推荐卡片。原文全文存于本目录的 original.md，网站上不显示，已翻译。Sierra 官方发布稿与 muse.ai 官方博客稿已于本轮之前收录，本文主要转述 Sierra 发布稿，属二手报道，规范细节、合作伙伴名单与落地案例以已收录的 Sierra 原稿为准。

**内容摘要**：Sierra 于 11 月 13 日发布 Poppy 1.0，Muse 现会在访问的每个网站上首先查找 Poppy，每个 Shopify 商店都会自动发布 Poppy 文件，设计合作伙伴总数已超过 100 家。Poppy 1.0 之前经过了五周的设计合作伙伴实测，可分阶段采用，并细化了对 MCP、OpenAPI、UCP 等现有标准的使用方式，扩展了企业向智能体提供指引与收集反馈的能力，还引入了扩展机制，Shopify 共同撰写了商务扩展。企业在域名下的 /.well-known/poppy.json 路径发布 poppy.json 文件，认证走 OAuth，用户可控制并随时管理智能体的访问权限，Sierra 还发布了带验证器的实施工具包。本次新增 60 家设计合作伙伴，总数超过 100 家，新成员包括 Affirm、Agoda、Cisco、Delta Air Lines、Hyatt、Intuit、Salesforce、Twilio、Wayfair、Wix 与 Zoom；Shopify 业务遍及 175 多个国家，每个商店自动发布 Poppy 文件且默认已支持 UCP。首批已上线的合作方包括 Mercury、Synchrony 与 Turkish Airlines：Mercury 用户可让智能体查余额、审交易、分类支出并发起付款或转账（须经账户审批政策），Turkish Airlines 支持查票价、航班状态与里程升舱，Synchrony 的工作尚处探索阶段，潜在覆盖超过 500,000 个商户网点。

**保留理由**：这是资料库中关于 Poppy 1.0 规范细节、设计伙伴规模与首批落地场景最完整的一篇报道，提供了官方发布稿之外的实施细节与商家实例；与 10 月协议预告的收录形成「预告—正式版」的完整链条。

---

Sierra 于 11 月 13 日发布了 Poppy 1.0。Muse 现在会在它访问的每个网站上首先查找 Poppy，每家 Shopify 商店都会自动发布一个 Poppy 文件，现在有超过 100 家公司是设计合作伙伴。

个人智能体协议（Personal Agent Protocol），即 Poppy，于周四[达到 1.0 版](https://sierra.ai/blog/releasing-poppy)。Poppy 现已对所有使用 Muse 的人开启，Muse 会自动在它访问的每个网站上首先查找 Poppy。Shopify 已为其平台上的每个商家启用 Poppy。

Poppy 定义了代表某个人行事的个人智能体如何通过企业的业务智能体、网站或 API 与公司连接。Sierra 和 Meta 上个月首次宣布了这一标准，设计合作伙伴包括 Genesys、Instinct、NiCE、Rocket、Shopify、Stripe 和 Walmart，该预告见[10 月关于个人智能体协议的公告报道](https://www.allthingsmuse.com/articles/meta-sierra-personal-agent-protocol/)。

## 1.0 版有哪些变化

1.0 版之前，设计合作伙伴用了五周时间，在真实网站、API 和智能体上测试草案。公司现在可以分阶段采用该协议，从基础部分开始，随时间逐步增加能力。此次发布细化了 Poppy 如何使用 MCP、OpenAPI 和 UCP 等现有标准。它扩展了公司向智能体提供指引、并从智能体收集反馈的方式，并引入了扩展（extension）机制，使各行业可以在不改变核心协议的情况下在其上构建。Shopify 共同撰写了商务扩展（commerce extension）。

按规范，公司在其域名的 /.well-known/poppy.json 路径下发布一个 poppy.json 文件。认证通过 OAuth 进行，因此客户可以控制个人智能体能做什么、不能做什么，并可以随时间管理该访问权限。Sierra 发布了一套带验证器（validator）的实施工具包（implementation kit），公司可用它检查自己的设置。

任何公司现在都可以自行实施 Poppy。随这次发布，有 60 家新公司加入成为设计合作伙伴。总数现在超过 100 家。新合作伙伴包括 Affirm、Agoda、Cisco、Delta Air Lines、Hyatt、Intuit、Salesforce、Twilio、Wayfair、Wix 和 Zoom。

## Shopify 商店自动获得 Poppy

Shopify 在 175 多个国家运营，现在每家 Shopify 商店都会自动发布一个 Poppy 文件，所以商家不需要额外的实施工作。每家 Shopify 商店默认已支持通用商务协议（Universal Commerce Protocol，UCP）。

这两个协议处理一次访问的不同部分。UCP 负责购物本身，例如查找商品、装满购物车和结账。Poppy 负责在此之前发生的事，即智能体来到一家商店、表明身份、并了解自己被允许做什么。商务扩展让智能体可以以访客身份购物，或用客户的账户登录。它要求智能体在某些操作前询问客户，并且与 UCP Ask 相连，使购物者的智能体可以直接与商店的智能体对话。

## 首批上线的使用

Mercury、Synchrony 和土耳其航空（Turkish Airlines）是目前已通过 Poppy 上线的合作伙伴之一。Mercury 的客户可以让个人智能体查询余额、查看近期交易、对支出分类，并使预算和收据保持最新。客户还可以让智能体发起付款或转账，Mercury 会在发出任何内容之前，让请求先通过账户的审批政策。

土耳其航空让个人智能体可以查询票价、航班状态和中途停留，并凭预订参考号和姓氏调出预订。Miles&Smiles 会员可以让智能体查找商务舱升舱，客户在付款前批准。该航空公司正在努力让会员无需离开对话即可完成购买。

Synchrony 的工作是探索性的。它研究个人智能体如何在考虑可负担性以及相关的 Synchrony 优惠和融资的同时帮助客户找到产品，潜在可用于超过 500,000 个商户网点的网络。

## 为什么身份识别对 Muse 很重要

在企业无法分辨智能体是谁、被允许做什么的地方，智能体的访问遇到了阻力。这个问题在别处已造成直接封禁，包括[加拿大的银行阻止 AI 智能体访问客户账户](https://www.allthingsmuse.com/articles/canadian-banks-block-ai-agents-muse/)，以及[摩根大通（JPMorgan）不让外部智能体进入客户账户](https://www.allthingsmuse.com/articles/jpmorgan-blocks-ai-agents-muse-accounts/)。Poppy 为企业提供了一种标准方式，在智能体行动之前回答这些问题：智能体表明身份，企业说明有哪些可用，客户通过 OAuth 授权账户访问。

对 Muse 用户来说，实际的变化是即时而悄然的。Muse 现在在它访问的每个网站上都先检查 Poppy，所以访问 Shopify 商店或其他 Poppy 网站时，一开始就是身份识别和声明的权限，而不是智能体以未表明身份的访客身份浏览。
