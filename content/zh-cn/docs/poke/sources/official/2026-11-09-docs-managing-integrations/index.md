---
title: "Poke 文档：管理集成"
linkTitle: "管理集成"
date: 2026-11-09
originalTitle: "Managing Integrations"
sourceUrl: "https://poke.com/docs/managing-integrations"
author: "未署名"
publisher: "The Interaction Company of California"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-09
tags: [连接器]
products: [poke]
dateNote: "帮助文档页没有标注发布或更新日期，取收集日期（美东）"
---

{{< source-info >}}

**收录说明**：Poke 帮助文档，直接下载后抽取。已翻译。

**内容摘要**：集成让 Poke 连接用户的应用和服务，连接后可通过自然对话读取信息并执行操作。最简单的方式是使用 Recipe，即处理集成并给出初始行为的预制模板；poke.com/recipes 上列有 Linear、Todoist、Notion、Asana、GitHub、DeepWiki、Sentry、Vercel、Netlify、Supabase、Ramp、Webflow 等。用户点击 Get Started 后按提示完成 OAuth 或 API key 授权，并可在 poke.com/integrations 查看、断开（Disconnect from Poke）或重连（Retry/Refresh Connection）。对未提供 Recipe 的服务，可在 poke.com/integrations/new 填写名称、MCP Server URL 和可选 API Key 接入任意 MCP 兼容服务器。

**保留理由**：给出集成的用户侧管理流程（授权、断开、重连）和自定义 MCP 入口，是连接器与用户控制的官方细节。

---

管理集成

## 概述

集成让你把自己喜欢的应用和服务连接到 Poke。连接后，Poke 可以通过自然对话访问信息并在各应用和服务中执行操作。

添加集成最简单的方式是使用 **Recipe**——一个预制模板，它处理集成的接入，并给 Poke 一个有价值的初始行为（例如「每天早上总结分配给我的 Linear 议题」）。

## 添加集成

### 浏览 Recipe

前往 [poke.com/recipes](https://poke.com/recipes) 浏览所有第一方和经批准的第三方 recipe。你会找到热门服务的预制 recipe：

- **Linear** - 自动化议题与项目管理
- **Todoist** - 创建和编辑任务与项目
- **Notion** - 读写页面和数据库
- **Asana** - 管理任务与项目工作流
- **GitHub** - 管理代码与仓库
- **DeepWiki** - 搜索和浏览文档
- **Sentry** - 追踪错误与性能
- **Vercel** - 部署和管理 Web 应用
- **Netlify** - 部署和管理 Web 应用
- **Supabase** - 管理数据库和后端服务
- **Ramp** - 分析支出和财务数据
- **Webflow** - 以可视化方式设计和部署网站
- 更多即将推出！

按类别筛选，或搜索你想要的服务。

### 使用 Recipe

打开一个 recipe 并点击 **Get Started**。Poke 会引导你完成任何认证步骤（OAuth、API key 等），并为你连接底层集成。

### 开始使用

你的集成现已激活！试着这样问 Poke：

- 「我今天在 Linear 和 Todoist 里有什么到期的事？」
- 「我的作品集网站上一次 Vercel 部署是什么时候？」
- 「我上一笔 Ramp 交易是多少钱？」
- 「pull request #123 的状态如何？」
- 「创建一个 Notion 页面，总结本周的待办事项」
- 「在 DeepWiki 中查找关于 React hooks 的文档」
- 或者你已连接的集成支持的任何其他事情！

## 管理你的集成

访问 [poke.com/integrations](https://poke.com/integrations) 查看并管理你已连接的一切。

### 查看已连接的集成

1. 前往 [poke.com/integrations](https://poke.com/integrations)
2. 查看所有活动集成和已连接账户
3. 选择一个以查看更多详情或管理它

### 断开集成

1. 前往 [poke.com/integrations](https://poke.com/integrations)
2. 找到该集成
3. 点击它
4. 点击「Disconnect from Poke」

### 重连或刷新

如果某个集成停止工作：

1. 前往 [poke.com/integrations](https://poke.com/integrations)
2. 留意错误指示
3. 点击该集成
4. 点击「Retry Connection」或「Refresh Connection」
5. 如有需要，重新认证

## 自定义集成（进阶）

如果你想要的服务没有以 Recipe 形式提供，你可以直接连接任何兼容 MCP 的服务器：

1. 前往 [poke.com/integrations/new](https://poke.com/integrations/new)
2. 输入集成的**名称**
3. 输入 **MCP 服务器 URL**（例如 `https://mcp.example.com/sse`）
4. 如果该服务需要认证，添加 **API Key**（可选）
5. 点击 **Create Integration**

如果你提供了 API key，它将被用于认证。除非你的集成需要它，否则请留空。

## 使用集成的提示

**要具体** - 提及集成名称或功能，以确保它被调用。

**从简单开始** - 先连接一两个集成，了解它们如何工作，然后再添加更多。

**保持更新** - 如果某个集成停止工作，在断开/重连之前先尝试刷新它。
