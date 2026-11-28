---
title: "Anthropic 托管的浏览器代用户浏览网页时如何标识自己"
linkTitle: "帮助：托管浏览器标识"
date: 2026-11-04
originalTitle: "How do Anthropic-hosted browsers identify themselves when they browse the web on a user's behalf?"
sourceUrl: "https://support.claude.com/en/articles/18234133-how-do-anthropic-hosted-browsers-identify-themselves-when-they-browse-the-web-on-a-user-s-behalf"
author: "未署名"
publisher: "Anthropic"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
dateNote: "帮助文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-04T22:04:37Z）"
tags: [运行环境, 安全]
products: [claude-duet]
---

{{< source-info >}}

**收录说明**：直接下载。帮助中心搜索「duet」时发现，正文第一句点名 Claude Duet。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：帮助中心面向网站所有者的说明：Claude Duet 等部分 Claude 产品可以用 Anthropic 托管的浏览器按用户指示完成任务，称为 agentic browser use，与 `ClaudeBot`、`Claude-User`、`Claude-SearchBot` 这些爬虫和抓取器不同。这类流量来自运行在 Anthropic 基础设施上的真实浏览器，User-Agent 是浏览器自身的标头加上 `Claude-Agent` 标记，页面建议只匹配这个标记。IP 地址发布在 `claude.com/.well-known/sail` 的 `Claude-Agent` 条目下，格式见 IETF 草案 draft-kelley-webbotauth-sail-00；任何人都能伪造 User-Agent，所以要核对来源 IP。允许或禁止这类流量，决定用户能否让 Claude 服务在该网站上完成任务，与对爬虫的设置相互独立。

**保留理由**：说明了 Claude Duet 的浏览器在哪里运行、怎样向网站表明身份，这些执行环境细节在发布文和入门帮助页里都没有。
