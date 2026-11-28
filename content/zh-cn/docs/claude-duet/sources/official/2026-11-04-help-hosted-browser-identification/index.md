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
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "帮助文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-11-04T22:04:37Z）"
tags: [运行环境, 安全]
products: [claude-duet]
---

{{< source-info >}}

**收录说明**：直接下载。帮助中心搜索「duet」时发现，正文第一句点名 Claude Duet。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：帮助中心面向网站所有者的说明：Claude Duet 等部分 Claude 产品可以用 Anthropic 托管的浏览器按用户指示完成任务，称为 agentic browser use，与 `ClaudeBot`、`Claude-User`、`Claude-SearchBot` 这些爬虫和抓取器不同。这类流量来自运行在 Anthropic 基础设施上的真实浏览器，User-Agent 是浏览器自身的标头加上 `Claude-Agent` 标记，页面建议只匹配这个标记。IP 地址发布在 `claude.com/.well-known/sail` 的 `Claude-Agent` 条目下，格式见 IETF 草案 draft-kelley-webbotauth-sail-00；任何人都能伪造 User-Agent，所以要核对来源 IP。允许或禁止这类流量，决定用户能否让 Claude 服务在该网站上完成任务，与对爬虫的设置相互独立。

**保留理由**：说明了 Claude Duet 的浏览器在哪里运行、怎样向网站表明身份，这些执行环境细节在发布文和入门帮助页里都没有。

---

部分 Claude 产品（包括 **[Claude Duet](https://claude.com/product/claude-duet)**）可以使用由 Anthropic 托管的浏览器，按用户的指示完成任务。这称为 agent 浏览器使用（agentic browser use）。本文说明网站所有者如何识别这类 agent 浏览器使用产生的流量，并选择是否允许这类流量。

agent 浏览器使用与 Anthropic 的机器人（爬虫和抓取器，包括 `ClaudeBot`、`Claude-User` 和 `Claude-SearchBot`）不同。要了解这些机器人，请参阅**[Anthropic 是否会抓取网络数据，网站所有者如何阻止该爬虫？](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)**

## 如何识别 agent 浏览器流量

**User-Agent：** 请求来自运行在 Anthropic 基础设施上的真实浏览器。请求会带上浏览器自身的 `User-Agent` 标头，并额外加入 `Claude-Agent` 标记，表明该浏览器正由一个托管的 Claude agent 驱动。

例如：

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko;  
compatible; Claude-Agent/1.0) Chrome/154.0.0.0 Safari/537.36
```

这个字符串的其他部分可能变化，所以请匹配 `Claude-Agent` 标记，而不是匹配整个字符串。

**IP 地址：** 这类流量来自发布在 **<https://claude.com/.well-known/sail>** 的 IP 地址，列在 `Claude-Agent` 条目下。这些地址可能随时间变化，因此我们建议从这个文件自动更新你的规则，而不是把它们写死。

任何人都可以发送相同的 `User-Agent` 标头，所以在断定流量为真实流量之前，务必检查它确实来自所列 IP 之一。关于发布格式的技术细节和使用它的注意事项，请参阅 **[draft-kelley-webbotauth-sail-00](https://www.ietf.org/archive/id/draft-kelley-webbotauth-sail-00.html)**。这还不是标准，因此可能随时间演变。

允许或不允许这类流量，将决定你的用户能否要求他们使用的 Claude 服务借助这类 agent 浏览器在你的网站上完成任务。你对 Anthropic 机器人（爬虫和抓取器）的设置是独立的，**[可以单独管理](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)**。
