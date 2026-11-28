---
title: "文档（docs.x.ai）：创建与管理 Bot"
linkTitle: "docs.x.ai：Bot 的创建与管理"
date: 2026-10-28
originalTitle: "Create and manage Bots"
sourceUrl: "https://docs.x.ai/grok-bot/bots"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-28T00:00:00Z）；2026-11-28 发现原文更新：Shared Bots 改称 Team Bots；删除分工建议章节（改指向 How Grok Bot works）；新增删除 Bot 会同时删除其分享的模板；Team Bot 学到的内容需所有者或 Manager 批准"
tags: [记忆与上下文, 功能更新]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 文档「Work」一页讲到 Bot 的部分与这页有重合，这页更细。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：Bot 被定义为有名字、职责、独立会话并会积累上下文的长期 AI 队友；何时需要单独的 Bot，文档指向 How Grok Bot works 一页。主 Bot（primary）会主动找用户并协调其他 Bot，Team Bot 不能当主 Bot；个人 Bot 没有描述和 **Bot settings** 页，行为要在聊天里调整，Team Bot 仍有描述，由所有者或 Manager 在 **About** 下编辑。Bot 可以做成模板分享，公开链接带身份、描述、技能和例程，不带电脑、登录和历史；删除 Bot 会清掉它的会话、记忆、例程和附件，同时删除它分享过的模板，使链接失效，共享电脑上的文件和登录则会留下。记忆由 Bot 自行决定何时保存，各 Bot 的记忆相互独立，只有姓名、时区等少数事实全账号共享；没有记忆管理界面，查看、纠正、删除都靠聊天，Team Bot 学到的内容要经所有者或 Manager 批准，也可以在 Settings 里从其他助手导入记忆到主 Bot。

**保留理由**：官方对多 Bot 分工、主 Bot 和记忆范围的说明，尤其是「记忆按 Bot 隔离、少数事实共享、没有记忆界面」这几点。
