---
title: "Poke 文档：创建 Recipe"
linkTitle: "创建 Recipe"
date: 2026-11-09
originalTitle: "Creating Recipes"
sourceUrl: "https://poke.com/docs/creating-recipes"
author: "未署名"
publisher: "The Interaction Company of California"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-09
tags: [连接器, 商业与规模]
products: [poke]
dateNote: "帮助文档页没有标注发布或更新日期，取收集日期（美东）"
---

{{< source-info >}}

**收录说明**：Poke 帮助文档，直接下载后抽取。已翻译。

**内容摘要**：Kitchen 是创建、发布和追踪自己 Poke recipe 的地方；一个 recipe 打包了引导上下文与首条消息行为、所需集成（MCP 模板）和分享/安装链接。向导中可设置名称、inputContext、prefilledFirstText，并选集成；支持本地凭证共享的集成可标记为共享，用户无需自行设置。已发布 recipe 的修改只影响新注册用户；发布后生成 referral 链接 poke.com/r/<referralCode> 并具备获得 payouts 的资格。页面还介绍 poke npm 包（需 Node.js 18+）的 login、mcp add、tunnel 与 --recipe 命令，tunnel 期间工具每 5 分钟自动同步，凭证存于 ~/.config/poke/credentials.json；Payouts 可查看唯一用户数与累计收益，收款目标为 Venmo。

**保留理由**：给出第三方开发者创建、分发 Recipe 并获得分成的机制与 CLI 细节，是 Poke 生态与商业模式的官方出处。

---

创建 Recipe

## 概述

Kitchen 是你创建、发布和追踪自己的 Poke recipe 的地方。

一个 recipe 打包了：

- 引导上下文与首条消息行为
- 所需的集成（MCP 模板）
- 供用户使用的分享/安装链接

## 开始之前

- 一个拥有 Kitchen 访问权限的 Poke 账户，位于 [poke.com/kitchen](https://poke.com/kitchen)
- 用于 CLI 工作流：Node.js 18+ 和 `poke` npm 包（通过 `npx poke@latest` 运行）

## 在 Kitchen 中创建 Recipe

### 打开向导

前往 [poke.com/kitchen](https://poke.com/kitchen) 并点击 **Create recipe**。

### 填写基本信息

设置 recipe 名称。描述是可选的。

### 配置引导

可选设置：

- **Poke 需要从用户那里获得什么上下文**（`inputContext`）
- **预填的首条消息**（`prefilledFirstText`）

### 选择集成

从选择器中选择所需的集成。

如果某个集成支持本地凭证共享，你可以将它标记为共享，这样用户就无需自行设置。

## 管理 Recipe

在 **Kitchen -> Recipes -> 你的 recipe** 中，你可以：

- 编辑引导上下文和预填的首条消息
- 更改所需集成和凭证共享设置

对于已发布的 recipe，更改只会影响新注册用户。

## 发布与分享

发布一个 recipe 会：

- 将其标记为 **Published**
- 生成一个推荐/分享链接
- 使其具备获得分成的资格

你通常会分享这样的链接：

- `https://poke.com/r/<referralCode>`

---

## `npx poke` 的作用

`poke` npm 包帮助你向账户中引入集成，并且配合 `--recipe` 可以引导出一个可分享的 recipe 流程。

包：[npmjs.com/package/poke](https://www.npmjs.com/package/poke)

### 1) 认证 CLI

```
npx poke@latest login
```

这会打开浏览器进行认证。在终端中输入显示的代码即可登录。

其他认证命令：

```
npx poke@latest logout   # Clear stored credentials
npx poke@latest whoami   # Display current user info
```

### 2) 添加或暴露 MCP 集成

```
# Remote MCP server
npx poke@latest mcp add https://mcp.example.com/sse -n "My Server"
 
# With API key authentication
npx poke@latest mcp add https://mcp.example.com/sse -n "My Server" -k "sk-your-api-key"
 
# Local MCP server over tunnel
# The tunnel only forwards the port — start your MCP server first, then tunnel it:
npx poke@latest tunnel http://localhost:3000/mcp -n "Local Dev MCP"
```

隧道**只转发本地端口**——它不会启动或管理 MCP 服务器本身。先启动你的服务器，再运行指向它的隧道命令。

隧道会一直保持活动，直到你按下 `Ctrl+C`。工具每 5 分钟自动同步一次。

然后打开 Kitchen，在你的 recipe 中选择该集成。

有些 MCP 服务器需要 OAuth，必须通过网页应用的集成流程添加，而不能通过 CLI。

### 3) 从 CLI 创建可分享的 recipe（`--recipe`）

```
npx poke@latest tunnel http://localhost:3000/mcp -n "Local Dev MCP" --recipe
```

使用 `--recipe` 时，CLI 会创建一个连接，并在终端返回 recipe 链接和二维码。之后可以在 Kitchen 中进一步管理该 recipe。

隧道必须保持活动，被分享的用户才能访问你的本地服务器。如果你停止隧道，连接将离线。

### CLI 配置

凭证存储在 `~/.config/poke/credentials.json`（如果设置了 `$XDG_CONFIG_HOME`，则为 `$XDG_CONFIG_HOME/poke/credentials.json`）。CLI 默认使用 `https://poke.com`，可通过环境变量覆盖：

| 变量 | 默认值 | 说明 |
| --- | --- | --- |
| `POKE_API` | `https://poke.com/api/v1` | 后端 API 基础 URL |
| `POKE_FRONTEND` | `https://poke.com` | 前端基础 URL |

---

## 分成与运营

Kitchen 还包含 **Payouts**，你可以在其中：

- 查看唯一用户总数和累计收益
- 设置你的收款目的地（Venmo 手机号/邮箱/账号）
- 查看收款历史
