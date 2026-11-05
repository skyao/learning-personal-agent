---
name: collect-dots
description: 收集 OpenAI dots（ChatGPT 中始终在线的个人智能体）的资料时使用：dots 的官方渠道、抓取方法、收录范围与已知问题。与 collect-sources 配合使用，通用流程与页面规则见 collect-sources。
---

# 收集 Dots 资料

通用流程、页面模板与翻译规则见 `skills/collect-sources/SKILL.md`。本文件只记录 Dots 特有的内容；与通用规则冲突时，以本文件为准。

## 状态

| 项目 | 值 |
| --- | --- |
| 产品目录 | `content/zh-cn/docs/dots/` |
| 发布日期 | 2026-09-29（OpenAI DevDay 2026 前后发布） |
| 最后收集日期 | —（首轮收集进行中） |
| 实测材料 | 用户确认没有（2026-11-05） |

## 收录范围

产品名在官方文档中写作小写的「dots」，单个称「your dot」。只收 dots 产品本身的资料。

| 资料 | 是否收录 |
| --- | --- |
| dots 的发布、帮助文档、learn.chatgpt.com 上的 dots 文档、安全设计 | 收录 |
| 企业文档中专门针对 dots 的页面：dots-security、dots-admin-guide、cloud-local-access（标题含 dots） | 收录 |
| ChatGPT Work 的通用企业文档（agent-security、chatgpt-work-cloud-security、chatgpt-work-local-security、usage-and-cost 等） | 不收：几乎不涉及 dots |
| 模型资料（GPT-6 Astra、GPT-6.1 Terra 的发布文与系统卡） | 按 collect-sources 的「模型资料的收录原则」逐篇判断；dots 文档写明 dots 会在不同工作部分调用不同模型 |
| Codex、ChatGPT Work、ChatGPT agent 本身 | 不收 |

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| ChatGPT Learn 文档 | `learn.chatgpt.com/docs/dots`、`/docs/dots/<子页>`；同一页面也可经 `/codex/dots/...` 和 `developers.openai.com/codex/dots` 访问 | 用户文档 6 页：认识 dots、入门、任务与记忆、控制、计算机与应用、消息渠道 | 直接下载；`sourceUrl` 用 canonical 的 `/docs/...` 地址，其余写入 `altUrls` |
| ChatGPT Learn 企业文档 | `learn.chatgpt.com/codex/enterprise/<页>` | dots-security、dots-admin-guide、cloud-local-access | 直接下载 |
| OpenAI 官网 | `openai.com/index/` | 发布文、安全文、DevDay 回顾、模型发布 | 直接下载返回 403，用网页抓取工具 |
| 帮助中心 | `help.openai.com/en/articles/<编号>`；有官方简体中文版 `/zh-hans-cn/` | 入门、隐私安全 FAQ；发布说明中的 dots 条目 | 直接下载返回 403，用网页抓取工具 |
| 部署安全中心 | `deploymentsafety.openai.com` | 模型系统卡 | 直接下载 |
| 开发者社区 | `community.openai.com` | OpenAI 员工发布的更新帖 | 待查 |

## 媒体与社区检索

- 英文检索词：`OpenAI dots agent`、`ChatGPT dots always-on agent`、`"your dot" ChatGPT`
- 中文检索词：`OpenAI dots 智能体`、`ChatGPT dots`
- 「dots」是常见词，检索时要带上 OpenAI 或 ChatGPT。

## 已知问题

### learn.chatgpt.com

- 页面不标日期，也没有结构化日期，`date` 取收集日期。
- 页面夹带界面示意组件（模拟聊天、浏览器、Slack 窗口），抽取后是零散文字，整理为「（界面示意：……）」段落并翻译其中的文字。
- 示例提示在页面中以卡片和可复制文本各出现一次，只保留一次。
- 页内相对链接 `/codex/...` 改为 `https://learn.chatgpt.com/codex/...`。
- 图片在 `/images/codex/dots/` 下，直接下载。

## 命名约定

- learn.chatgpt.com 的文档 slug 以 `docs-` 开头，例如 `2026-11-05-docs-meet-dots`。
- 帮助中心文章 slug 以 `help-` 开头。
