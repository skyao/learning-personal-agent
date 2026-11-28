---
title: "Grok Bot 共生：把手机的到达与离开事件接进 Bot"
linkTitle: "Timeline：Bot 共生"
date: 2026-11-21
originalTitle: "Grok Bot symbiosis"
sourceUrl: "https://timeline.place/guides/grok-bot-symbiosis"
author: "Marcel Marais"
publisher: "Timeline"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
dateNote: "日期取页面元数据的发布日期"
tags: [实测评测, 持续执行, 连接器]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：直接下载；去掉了作者头像和文首、文末的 Timeline 下载推广框，以及文末的「More guides」列表。文中两个交互图表（按周切换的提醒分布、按时间切换的地点示例）在静态页面里只能取到默认状态，按默认状态存档，图中的应用图标已去掉、保留文字。作者是 iPhone 位置历史应用 Timeline 的开发者，文中的 webhook 与 MCP 服务来自自家产品，文末链接到自家的设置向导。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：作者把 iPhone 上的到达与离开事件通过 webhook 送给 Grok Bot，让它按地点和时间自行处理杂事：周五 12:18 离开办公室后，Bot 把 Slack 状态设为“Out for lunch”到 13:15、把两个 PR rebase 到 main 并重跑不稳定的 CI；进超市时给出海鲈鱼配茴香的购物清单；进健身房时读取笔记、查 Google Health 并把卧推加到 82.5 kg。第一周因提示过宽，通知过多，改成“不匹配任何规则就不发消息”后，一周 34 个停留点中 28 个无通知、6 个发消息。作者划定的界线：可撤销的准备工作可以自动做，发给他人的邮件、合并到 main、花钱仍需本人确认；原始 GPS 轨迹不送云端，只送解析后的停留点和笔记。

**保留理由**：长期使用主动型 Bot 的第一手日常用例，附带如何压低通知噪声和划定自动化边界的做法。
