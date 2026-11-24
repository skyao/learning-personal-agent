---
title: "土耳其航空开门、美联航关门之后：从智能体一侧读 Poppy 1.0"
linkTitle: "从智能体一侧读 Poppy 1.0"
date: 2026-11-20
originalTitle: "Turkish Opened the Gate the Day After United Locked It — Reading Poppy 1.0 From the Agent Side of the Counter"
sourceUrl: "https://muleai.io/blog/2026-11-20-turkish-opened-the-gate-united-locked/"
author: "Mule"
publisher: "Mule AI"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-24
tags: [连接器, 安全]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载后用 extract.py 抽取；删去分类、标签、空目录与文末分享链接；文中伪代码照录原文；无图片。原文全文存于本目录 original.md，网站上不显示，待翻译。

**内容摘要**：2026 年 11 月 13 日 Sierra 发布个人智能体协议 Poppy 1.0，土耳其航空随之上线：可查票价与航班状态、凭预订号与姓氏调取预订、查找升舱，付款前需顾客批准；Mercury 的部署也遵循同一模式，查余额与交易放行、支付与转账先走账户审批。作者指出，协议本身是发现与接入协商层，建立在 MCP、OpenAPI 与 UCP 之上，以 OAuth 做认证、并以 Shopify 起草的商业扩展连接 UCP；真正的分量在分发：Meta 的 Muse 访问网站时会优先查找 Poppy 文件，Shopify 已为平台全部商家自动发布，64 家新设计伙伴使总数超过 100 家。作者同时质疑，预订号加姓氏只是可猜测的弱口令，负责任的部署应按层级分别威胁建模、把一切状态变更放在同意钩子之后、按智能体身份而非 IP 限流，并在上线前用真实智能体做测试。作者的结论是，Poppy 协议本身不大，八成意义在于 Muse 优先查找与百万店面默认发布——标准靠预装取胜。

**保留理由**：自称运营浏览器工具的智能体一方写下的独立解读，含土耳其航空与 Mercury 的部署细节与按层级的安全批评，并给出"标准靠预装取胜"的判断，是已收 Sierra 公告与 JTS 实地核查之外的第三方分析视角。
