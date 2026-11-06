---
title: "文档（docs.x.ai）：电脑与应用"
linkTitle: "docs.x.ai：电脑与应用"
date: 2026-10-28
originalTitle: "Use the computer and apps"
sourceUrl: "https://docs.x.ai/grok-bot/computer-and-apps"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-06
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）"
tags: [运行环境, 连接器, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。帮助页「连接应用」「Bot 邮箱」与这页部分重合。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：每个用户有一台云端电脑，名下所有 Bot 共用，Cookie、文件和命令行凭据都共享；每个 Bot 有自己的屏幕，但屏幕不是安全边界，不同用户之间则是硬件隔离。登录依次尝试 Vault、1Password 和聊天内的安全表单，遇到 SSO、通行密钥、验证码和银行卡验证时请用户接管；付款可以用 Vault 中的卡、安全表单，或 Link、X Money 钱包。应用连接的 OAuth 令牌存在连接器后端，不落到电脑上。Bot 邮箱地址形如 `name@mail.grokbot.com`，每人一个，不能改名或删除；例程发出的邮件都先成草稿，没有无人值守的发送。文档还给出工作目录 `/workspace` 的持久化规则，以及 Update、Recover、Reset 三种恢复操作的对照。

**保留理由**：这是 Grok Bot「一人一台共享电脑」运行模型最集中的说明，连带讲清了登录、付款和邮箱的边界。
