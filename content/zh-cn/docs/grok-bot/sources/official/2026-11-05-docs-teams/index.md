---
title: "文档：面向 Teams 和 Enterprise 的 Grok Bot"
linkTitle: "文档：Teams 与 Enterprise"
date: 2026-11-05
originalTitle: "Grok Bot for Teams and Enterprise"
sourceUrl: "https://cursor.com/docs/grok-bot/teams"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [安全, 开放与价格, 运行环境, 商业与规模]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：这是管理员部署指南。Teams 套餐默认开启且无法关闭，Enterprise 由管理员开启，并可用「Manage Group Access」限定用户组；Privacy Mode (Legacy) 会完全阻止 Grok Bot。架构上，Grok Bot 是在每用户一个 Firecracker microVM 中运行的计算机使用智能体，桌面和移动端只是聊天、审核与审批的瘦客户端。管理控制涵盖云端智能体委派、模板公开分享、共享 Bot、Agent Email、连接器策略、本地执行上限，以及 Enterprise 专有的网络控制、Team Setup Scripts、Team Secrets、强制 Auto-review、Action Recording、审计日志、OpenTelemetry 导出、数据保留（Bot 60 至 365 天、计算机与消息 30 至 365 天）和成员计算机管理。用户组设置只放宽、不收紧（网络策略除外）；文末给出推荐的安全基线配置，并说明目前没有单独的 Grok Bot 支出上限。

**保留理由**：汇总了团队与企业版各控制项的归属与默认值，并给出推荐配置，是对照看 Teams 与 Enterprise 能力差异的主要资料。
