---
title: "采购场景实测：Haggle Bot 找到超过 10 万美元节省"
linkTitle: "内部用例：采购"
date: 2026-09-04
originalTitle: "Setting Grok Bot loose on procurement"
sourceUrl: "https://x.ai/news/grok-bot-procurement"
reprintUrl: "https://web.archive.org/web/20261014104622/https://x.ai/news/grok-bot-procurement"
author: "未署名"
publisher: "SpaceXAI（xAI）"
language: en
fidelity: 转载全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "x.ai 对自动访问返回 403，依据 Wayback 快照 20261014104622；日期取页面结构化数据的 datePublished"
tags: [实测评测, 安全, 连接器]
products: [grok-bot]
---

{{< source-info >}}

（收集说明：x.ai 对自动访问返回 403，原文依据 Internet Archive 快照存档；去掉了「Back to news」链接、下载与联系销售按钮和文末「Try Grok Bot today」推广区，视频改为一行链接。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

**收集者摘要**：xAI 内部建了名为 Haggle Bot 的采购 Bot，让它读取供应商支出、合同和用量数据，用市场价格和竞品报价找出节省并准备谈判，目前已识别出超过 10 万美元的直接节省。它接入 Slack、Notion、Drive、Gmail、Hex 和 Ramp，整理出约 125 个在用供应商的工作图。文中给出完整系统提示，把权限分成可随时做、每次需经运营者明确同意、绝不做三档，发给供应商的内容每次都要运营者明确同意，签约、购买、承诺付款则绝不允许。案例有：一款产品 43 个付费席位 90 天内无活动，节省 14,220 美元；另一产品每年 85,662 美元闲置 SKU；周度办公用品订单从 14,629 美元降到 6,143 美元，降幅 58%。作者称给供应商写邮件仍需人工修改语气。

**保留理由**：这是一个把 Bot 放进具体岗位的详细案例，系统提示和权限三档设定可直接对照 Grok Bot 如何用自然语言规定审批边界。
