---
title: "Poke 文档：Poke API"
linkTitle: "Poke API"
date: 2026-11-09
originalTitle: "Poke API"
sourceUrl: "https://poke.com/docs/api"
author: "未署名"
publisher: "The Interaction Company of California"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-09
tags: [连接器, 持续执行]
products: [poke]
dateNote: "帮助文档页没有标注发布或更新日期，取收集日期（美东）"
---

{{< source-info >}}

**收录说明**：Poke 帮助文档，直接下载后抽取。已翻译。

**内容摘要**：Poke API 允许从应用、脚本和自动化工具以编程方式向 Poke 发消息，这些消息由 Poke 处理，可完全访问邮件、日历、提醒和已连接的集成，效果与用户亲自发短信相同。用法是向 POST https://poke.com/api/v1/inbound/api-message 发送带 Bearer API key 的 JSON，整个 body 会作为上下文转发给 agent；API key 在 Kitchen 的 API Keys 中创建，只显示一次。旧端点 inbound-sms/webhook 已弃用，只接受 pk_ 开头的 V1 key，新端点需要 V2 key。文档给出浏览器扩展、GitHub Action 部署失败告警、Typeform/CRM 事件、VS Code 扩展等触发示例，并建议用环境变量保存 key、可建多个 key、泄露即吊销。消息到达后，Poke 评估请求、决定使用哪些工具（邮件、日历、Notion/Whoop 等集成）、执行并回复。

**保留理由**：说明外部事件如何触发 Poke 执行，是“事件驱动的持续运行”和 API key 凭证管理的官方细节。

---

Poke API

## 概述

Poke API 允许你从应用、脚本和自动化工具中以编程方式发送消息。通过 API 发送的消息由 Poke 处理，可完全访问邮件、日历、提醒和已连接的集成。

**用例：**

- 桌面工具和浏览器扩展
- 自动化触发器（CI/CD、webhook、监控）
- 事件驱动的工作流（GitHub Actions、定时任务）
- 桥接没有原生集成的服务

## 工作原理

你的脚本/工具 → Poke API → 你的助手接收 → 执行动作

消息会出现在你的 Poke 对话中，并像你亲自发短信一样被处理——只是它是通过编程方式触发的。

## 获取你的 API key

### 打开 Kitchen

前往 [Kitchen](https://poke.com/kitchen) 并导航到 **API Keys**。

### 创建 API key

点击 **Add API Key** 并命名（例如「Desktop Tools」或「GitHub Actions」）。妥善保管——任何拿到你 key 的人都能向你的 Poke 发送消息。

### 保存它

立即复制——你不会再看到它。把它存进密码管理器或环境变量。

旧端点 `POST /api/v1/inbound-sms/webhook` 已弃用。它只能配合在 Poke app（Settings → Advanced）中创建的 V1 API key（以 `pk_` 开头）使用。

新端点 `/api/v1/inbound/api-message` 需要在 [Kitchen](https://poke.com/kitchen) 中创建的 **V2 API key**。现有的 `pk_` key 不能用于新端点——你必须在 Kitchen 中创建新的 key。

## 发送消息

```
POST https://poke.com/api/v1/inbound/api-message
```

**请求头：**

- `Authorization: Bearer YOUR_API_KEY`
- `Content-Type: application/json`

**请求体：**

任意 JSON 对象。整个 body 会作为上下文转发给你的 agent。

```
{
  "message": "Your instruction or question here"
}
```

### 快速示例

```
curl 'https://poke.com/api/v1/inbound/api-message' \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"message": "Email the team our Q1 numbers and schedule a review call next week"}'
```

```
import requests
import os
 
API_KEY = os.environ['POKE_API_KEY']
 
requests.post(
    'https://poke.com/api/v1/inbound/api-message',
    headers={
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    },
    json={'message': 'Your instruction here'}
)
```

```
const response = await fetch("https://poke.com/api/v1/inbound/api-message", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.POKE_API_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    message: "Your instruction here",
  }),
});
```

### 响应

```
{
  "success": true,
  "message": "Message sent successfully"
}
```

**`success`** *(boolean)* —— 消息是否已送达你的 Poke

## 何时使用

### 桌面捕获

你在笔记本电脑上，在浏览器或 IDE 里工作。你想把某些东西发给 Poke，又不想掏出手机。

**示例：浏览器扩展**

```
// Select text on webpage → right-click → "Send to Poke"
const selectedText = window.getSelection().toString();
const pageUrl = window.location.href;
 
fetch("https://poke.com/api/v1/inbound/api-message", {
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
  method: "POST",
  body: JSON.stringify({
    message: `Summarize this article and email key points to my team:\n\n${selectedText}\n\nSource: ${pageUrl}`,
  }),
});
```

### 事件驱动的自动化

GitHub、CI/CD 流水线或监控工具等服务可以在有事发生时触发 Poke。

**示例：部署失败时的 GitHub Action**

```
# .github/workflows/deploy.yml
- name: Alert via Poke
  if: failure()
  run: |
    curl 'https://poke.com/api/v1/inbound/api-message' \
      -H "Authorization: Bearer ${{ secrets.POKE_API_KEY }}" \
      -H "Content-Type: application/json" \
      -d "{\"message\": \"Deploy failed: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}. Create incident ticket and notify on-call.\"}"
```

### 桥接未集成的服务

任何能 POST webhook 的服务都可以委托给 Poke——无需等待原生集成。

**示例：Typeform 提交 → Poke**

```
// Typeform webhook handler
app.post("/typeform-webhook", async (req, res) => {
  const { name, email, company } = req.body.form_response.answers;
 
  await fetch("https://poke.com/api/v1/inbound/api-message", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${process.env.POKE_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: `New lead: ${name} from ${company}. Research their company, draft personalized follow-up email, and add meeting to my calendar next week.`,
    }),
  });
 
  res.sendStatus(200);
});
```

**示例：自定义 CRM 事件**

```
# When deal closes in your CRM
def on_deal_closed(customer_info):
    message = f"""
    {customer_info['name']} just closed!
 
    - Send onboarding email with login details
    - Schedule kickoff call for next week
    - Create project in Notion
    - Set 30/60/90 day check-in reminders
    """
 
    requests.post(
        'https://poke.com/api/v1/inbound/api-message',
        headers={'Authorization': f'Bearer {POKE_API_KEY}', 'Content-Type': 'application/json'},
        json={'message': message}
    )
```

### 上下文丰富的指令

传入 URL、选区内容、ID 或结构化数据，让你的指令立即可执行。

**示例：VS Code 扩展**

```
// Send selected code with error context
const selection = editor.document.getText(editor.selection);
const filePath = editor.document.fileName;
const error = diagnostics[0].message;
 
await fetch("https://poke.com/api/v1/inbound/api-message", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    message: `Debug this error:\n\nFile: ${filePath}\nError: ${error}\n\nCode:\n${selection}`,
  }),
});
```

## 提示

**使用环境变量**——把 API key 存在 `POKE_API_KEY` 中，而不是硬编码。

**具体一些**——「给 John 发邮件谈 Q1 评审，建议周二或周三」比「联系 John」效果更好。

**带上上下文**——传入 URL、文件路径或选区，让 Poke 知道要对什么采取行动。

**先测试**——在构建自动化之前先发送 `{"message": "test"}`。

## 故障排查

### 401 Unauthorized

**你的 API key 无效或缺失。**

检查：

1. Authorization 请求头：`Bearer YOUR_KEY`（注意「Bearer」后的空格）
2. key 未在 Settings 中被吊销
3. key 中没有多余的空格或换行

### 消息没有出现

- 确认响应显示 `"success": true`
- 检查你的 Poke app（刷新对话）
- 试一个简单测试：`{"message": "test"}`
- 检查 app 中的通知设置

### 频率限制

如果你触发了频率限制，可以考虑：

- 把多个请求合并到一条消息中
- 在自动化消息之间加入延迟
- 为不同的自动化创建不同的 API key

## 安全

妥善保管你的 API key。使用环境变量，绝不要把 key 提交到 Git，一旦泄露立即吊销。你可以创建多个 API key——如果其中一个泄露，只需吊销那个 key。

## 接下来会发生什么

当你的消息到达时，Poke 会：

1. 评估你在要求什么
2. 决定使用哪些工具（邮件、日历，以及 Notion/Whoop 等集成）
3. 采取行动并回复你
