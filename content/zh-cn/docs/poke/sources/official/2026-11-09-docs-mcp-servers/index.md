---
title: "Poke 文档：MCP 服务器"
linkTitle: "MCP 服务器"
date: 2026-11-09
originalTitle: "MCP Servers"
sourceUrl: "https://poke.com/docs/mcp-servers"
author: "未署名"
publisher: "The Interaction Company of California"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-09
tags: [连接器, 安全]
products: [poke]
dateNote: "帮助文档页没有标注发布或更新日期，取收集日期（美东）"
---

{{< source-info >}}

**收录说明**：Poke 帮助文档，直接下载后抽取。待翻译。

**内容摘要**：Poke 支持 Model Context Protocol 服务器，接入后可在对话中发现并调用其暴露的工具。接入方式有三种：网页 poke.com/integrations/new、CLI（mcp add、tunnel，本地服务器经隧道转发端口）和预填链接；对不支持 Dynamic Client Registration (DCR) 的 OAuth 服务器，可用 --client-id/--client-secret，或经 Kitchen 建模板和 recipe。文档称做 recipe 可在日后更新服务器 URL，并从安装用户的 MCP 使用中获得收入。Poke 向服务器的每个请求带 Authorization: Bearer 头和 X-Poke-User-Id 头，后者可用于按用户限流、按用户范围返回数据和审计日志；工具会在连接创建或重新认证时自动同步，也可手动重新同步。

**保留理由**：给出 Poke 发给第三方服务器的认证与用户标识细节，是凭证传递和审计能力的官方出处。
