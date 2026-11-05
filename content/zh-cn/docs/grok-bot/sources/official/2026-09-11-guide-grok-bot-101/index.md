---
title: "指南：Grok Bot 入门 101"
linkTitle: "指南：Grok Bot 101"
date: 2026-09-11
originalTitle: "Grok Bot 101"
sourceUrl: "https://x.ai/bot/guides/grok-bot-101"
reprintUrl: "https://web.archive.org/web/20261017234251/https://x.ai/bot/guides/grok-bot-101"
author: "Matt Palmer"
publisher: "SpaceXAI（xAI）"
language: en
fidelity: 转载全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "x.ai 对自动访问返回 403，依据 Wayback 快照 20261017234251；日期取页面结构化数据的 datePublished"
tags: [实测评测, 运行环境, 安全, 连接器]
products: [grok-bot]
---

{{< source-info >}}

（收集说明：x.ai 对自动访问返回 403，原文依据 Internet Archive 快照存档；去掉了「Back to news」链接、下载与联系销售按钮和文末「Try Grok Bot today」推广区，视频改为一行链接。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

## 收集者摘要

Matt Palmer 以 SpaceXSI 开发者关系岗位的使用方式介绍 Grok Bot：它是带云端计算机的智能体，有桌面、文件系统、终端和应用，可当远程桌面操作。Bot 的设置只有名称、头衔、描述三项；遇到验证码或 2FA 时把桌面交还给用户，也可发安全表单收密码或 API 密钥。权限用自然语言写在设置里，另有一个审查智能体对提议的动作选择允许、阻止或升级给用户；他提醒在一个 Bot 里登录的网站，其他 Bot 也能访问。他演示多 Bot 链、个人 CRM（用 Notion）、健身教练 Bot、用外层智能体给 Cursor 云端智能体写提示，以及跨 Slack、Notion、GitHub 的搜索。

## 保留理由

以第一人称写出实际搭建流程和日常用法，尤其是权限用提示而非代码配置、共享登录的说明，是理解个人用法的好材料。
