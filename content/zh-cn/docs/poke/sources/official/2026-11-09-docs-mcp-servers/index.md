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
translation: 已翻译
collectedAt: 2026-11-09
tags: [连接器, 安全]
products: [poke]
dateNote: "帮助文档页没有标注发布或更新日期，取收集日期（美东）"
---

{{< source-info >}}

**收录说明**：Poke 帮助文档，直接下载后抽取。已翻译。

**内容摘要**：Poke 支持 Model Context Protocol 服务器，接入后可在对话中发现并调用其暴露的工具。接入方式有三种：网页 poke.com/integrations/new、CLI（mcp add、tunnel，本地服务器经隧道转发端口）和预填链接；对不支持 Dynamic Client Registration (DCR) 的 OAuth 服务器，可用 --client-id/--client-secret，或经 Kitchen 建模板和 recipe。文档称做 recipe 可在日后更新服务器 URL，并从安装用户的 MCP 使用中获得收入。Poke 向服务器的每个请求带 Authorization: Bearer 头和 X-Poke-User-Id 头，后者可用于按用户限流、按用户范围返回数据和审计日志；工具会在连接创建或重新认证时自动同步，也可手动重新同步。

**保留理由**：给出 Poke 发给第三方服务器的认证与用户标识细节，是凭证传递和审计能力的官方出处。

---

MCP 服务器

## 概述

Poke 支持 [Model Context Protocol (MCP)](https://modelcontextprotocol.io) 服务器，让你可以用自定义工具和数据源扩展 Poke。当你连接一个 MCP 服务器后，Poke 可以在对话中发现并调用它暴露的工具。

## 连接 MCP 服务器

你可以通过三种方式把 MCP 服务器连接到 Poke：

### 通过网页应用

### 前往 Integrations

访问 [poke.com/integrations/new](https://poke.com/integrations/new)。

### 输入服务器详情

提供一个**名称**和 **MCP 服务器 URL**（例如 `https://mcp.example.com/sse`）。如需要，添加 **API Key**。

### 创建

点击 **Create Integration**。Poke 将连接并发现可用的工具。

### 通过 CLI

```
# Remote MCP server
npx poke@latest mcp add https://mcp.example.com/sse -n "My Server"
 
# With API key authentication
npx poke@latest mcp add https://mcp.example.com/sse -n "My Server" -k "sk-your-api-key"
 
# Local server via tunnel
npx poke@latest tunnel http://localhost:3000/mcp -n "Local Dev MCP"
 
# Tunnel with OAuth client credentials (for servers without DCR)
npx poke@latest tunnel http://localhost:3000/mcp -n "My OAuth Server" --client-id "your-id" --client-secret "your-secret"
```

隧道会转发你的本地端口，使 Poke 能够访问它。先启动你的 MCP 服务器，再运行隧道命令。隧道会一直保持活动，直到你按下 `Ctrl+C`。

### 通过预填链接

如果你在构建供他人使用的集成，考虑[创建 recipe](https://poke.com/docs/creating-recipes)，而不是分享一个原始的预填链接。使用 recipe，你可以在日后更新服务器 URL 或配置，而无需让用户重新添加集成；同时，你还能从安装你 recipe 的用户使用 MCP 中获得收入。

你可以创建一个预填集成表单的链接，便于与他人分享设置说明：

```
https://poke.com/integrations/new?name=My%20Server&url=https://mcp.example.com/sse&apiKey=sk-your-api-key
```

| 参数 | 说明 | 是否必需 |
| --- | --- | --- |
| `name` | 集成显示名称 | 否 |
| `url` | MCP 服务器 URL | 否 |
| `apiKey` | 用于认证的 API key | 否 |

所有参数都是可选的——提供的任何值都会预填到表单中，用户可以在提交前修改。

### 不支持动态客户端注册的 OAuth 服务器

如果你的 MCP 服务器要求 OAuth，但不支持[动态客户端注册（Dynamic Client Registration，DCR）](https://datatracker.ietf.org/doc/html/rfc7591)，你可以通过两种方式提供客户端 ID 和密钥：

**通过 CLI：**把 `--client-id` 和 `--client-secret` 传给 `tunnel` 命令（见上文）。

**通过 Kitchen：**适用于无需隧道的托管服务器：

### 创建模板

前往 [poke.com/kitchen](https://poke.com/kitchen) 并点击 **New Template**。输入 MCP 服务器 URL，以及 OAuth 的 **Client ID** 和 **Client Secret**。

### 创建 Recipe

创建一个 recipe，把刚设置好的模板作为必需的集成包含进去。

### 添加集成

通过该 recipe 安装集成。Poke 会为每位连接的用户处理 OAuth 流程。

支持动态客户端注册（DCR）的 MCP 服务器可自动工作。只需通过网页应用或 CLI 添加它们。上述流程仅在 OAuth 服务器不支持 DCR 时才需要。

## Poke 向你的服务器发送什么

当 Poke 向你的 MCP 服务器发起请求时，会包含以下内容：

### 认证

如果你配置了 API key 或 OAuth 凭证，Poke 会在每个请求中带上 `Authorization` 头。

```
Authorization: Bearer {access_token}
```

### 用户标识

Poke 会在每个请求中带上 `X-Poke-User-Id` 头。这是发起请求的 Poke 用户的唯一标识符。

```
X-Poke-User-Id: 00000000-0000-0000-0000-000000000000
```

你可以将这个头用于：

- **按用户限流**
- **按用户范围的数据访问**：根据提问的用户不同返回不同结果
- **审计日志**：追踪每个请求由哪个用户触发

### 请求示例

```
POST /mcp HTTP/1.1
Host: mcp.example.com
Authorization: Bearer {access_token}
X-Poke-User-Id: 00000000-0000-0000-0000-000000000000
Content-Type: application/json
```

## 构建 MCP 服务器

任何实现了 [MCP 规范](https://modelcontextprotocol.io) 的服务器都能与 Poke 配合工作。常用框架包括：

- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

你的服务器暴露**工具（tools）**，Poke 可以发现并调用它们。每个工具都有名称、描述和输入 schema，Poke 用它们来决定何时以及如何调用工具。

你可以随时从集成页面或通过调用同步端点重新同步服务器的工具列表。Poke 也会在首次创建连接或重新认证时自动同步工具。
