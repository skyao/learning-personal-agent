---
title: "poppy.json 里到底写什么：对照 1.0 规范与验证器实测"
linkTitle: "poppy.json 内容核查"
date: 2026-11-15
originalTitle: "Inside poppy.json: What a Business Actually Publishes for Poppy 1.0, Checked on personalagentprotocol.org and the Validator Itself"
sourceUrl: "https://museexplained.com/guide/inside-poppy-json-what-a-business-publishes-poppy-1-0/"
author: "Marvin Jones"
publisher: "Muse Explained"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-16
tags: [连接器, 实测评测]
products: [muse]
dateNote: "JSON-LD 标注 datePublished 与 dateModified 均为 2026-11-16（UTC 日期），页面正文核查记录均为 11 月 15 日，按页面实际发布日记为 11-15。"
---

{{< source-info >}}

**收录说明**：直接下载；无图片。作者全文通读了 Poppy 1.0 规范第 3 节、指南、扩展页面与企业实施工具包，并对规范自带的示例文档离线运行了工具包里的验证器。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：本文是 Muse Explained 站的 Poppy 落地核查第二篇：作者于 2026 年 11 月 15 日全文通读了 Poppy 1.0 规范第 3 节、指南、扩展页面与企业实施工具包，并对规范自带的示例文档离线运行了工具包里的验证器。按规范第 3.1 节字段表，poppy.json 只有两个必填字段——protocol_version 与 organization——另须至少提供 agent、apis、web 三种渠道之一。离线验证结果为 Foundation 里程碑 7 项通过、0 项失败、7 项跳过，跳过的是需要联网的检查。同日核查发现，协议自家演示站点（含其 poppy.json 与协议检查器）均返回 Not Found，且截至 11 月 15 日仍无 Muse 内出现 Poppy 行为的实证，也无 Mercury、Synchrony、土耳其航空或 Shopify 以自家名义发布的公告。Mediated Sign-In 定于 2027 年 3 月 17 日退役，作者定于 11 月 23 日再次核查上述未决事项与首个真实企业 poppy.json。

**保留理由**：已收资料已有 Sierra 与 Muse 两份 11 月 13 日官方公告、allthingsmuse 的实施细节和本站 Part 1 的落地核查台账，但均未逐条核对规范原文或实际运行验证器。本篇逐项读了规范第 3 节与实施工具包并离线跑了验证器，给出了 poppy.json 字段规则与验证器实测结果，是已收资料中没有的一手核查。
