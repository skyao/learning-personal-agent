---
title: "指南：Grok Bot 模板"
linkTitle: "指南：模板"
date: 2026-09-08
originalTitle: "Templates for Grok Bot"
sourceUrl: "https://x.ai/bot/guides/templates-for-grok-bot"
reprintUrl: "https://web.archive.org/web/20260928175955/https://x.ai/bot/guides/templates-for-grok-bot"
author: "Matt Palmer"
publisher: "SpaceXAI（xAI）"
language: en
fidelity: 转载全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "x.ai 对自动访问返回 403，依据 Wayback 快照 20260928175955；日期取页面结构化数据的 datePublished"
tags: [功能更新, 记忆与上下文, 安全]
products: [grok-bot]
---

{{< source-info >}}

（收集说明：x.ai 对自动访问返回 403，原文依据 Internet Archive 快照存档；去掉了「Back to news」链接、下载与联系销售按钮和文末「Try Grok Bot today」推广区，视频改为一行链接。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

## 收集者摘要

Matt Palmer 讲模板的用法：模板是 Bot 的「食谱」而不是克隆，打包的是 Bot 的指令、相关记忆、技能和指定插件，自定义代码和脚本、个人或内部记忆默认不包含。在设置里点「Share as Template」不会让 Bot 公开，只生成一个匿名的私有版本，之后可选择只给团队或生成公开链接。接收方点「Add to Grok Bot」，查看包含的上下文和集成后点「Add Bot」得到一个新副本；原有插件要重新安装，MCP 服务器等非标准插件不会带过来。文中提示模板不包含秘密，安装别人的模板要像评估技能或软件一样先看详情。

## 保留理由

说明 Bot 能怎么打包、分享，哪些内容会带走、哪些不会，对研究 Bot 的可迁移性和分享时的隐私处理有直接用处。
