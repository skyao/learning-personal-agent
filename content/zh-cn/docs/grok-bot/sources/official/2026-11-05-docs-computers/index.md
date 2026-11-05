---
title: "文档：管理成员的计算机与数据"
linkTitle: "文档：管理计算机"
date: 2026-11-05
originalTitle: "Manage Grok Bot computers"
sourceUrl: "https://cursor.com/docs/grok-bot/computers"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [运行环境, 隐私, 安全]
products: [grok-bot]
---

{{< source-info >}}

（收集说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

## 收集者摘要

每个团队成员有一台托管计算机，其上的所有 Bot 都在这里工作。企业管理员可在 Cursor 控制台批量重建（Recreate）或终止（Terminate）成员的计算机，删除计算机及数据，或删除成员的全部 Grok Bot 数据；此功能仅限 Enterprise。重建和终止都保留成员的持久磁盘，重建时正在执行的 Bot 会在安全点暂停并在新计算机上继续，终止则让运行中的工作停止，下次发消息会在同一磁盘上新建计算机。删除计算机及数据一次最多 1,000 名成员，删除全部数据一次最多 100 名，均不可撤销并写入审计日志。还可设置保留期，在无人给成员的任何 Bot 发消息达 30 至 365 天后自动删除休眠的计算机，默认关闭且删除前不通知。

## 保留理由

写明了计算机重建、终止、删除的差别和数据保留规则，是了解云端计算机生命周期与持久磁盘的直接材料。
