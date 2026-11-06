---
title: "Gemini Spark 无法写入任何 Google 表格：sheets_agent:call 被策略检查拦截"
linkTitle: "开发者论坛：表格写入故障"
date: 2026-10-13
originalTitle: "Gemini Spark cannot write to any Google Sheets — sheets_agent:call blocked by policy check"
sourceUrl: "https://discuss.google.dev/t/gemini-spark-cannot-write-to-any-google-sheets-sheets-agent-call-blocked-by-policy-check/404155"
author: "vailon 等"
publisher: "Google Developer forums"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "首帖 2026-10-13，楼主 2026-10-16 回报问题已修复"
tags: [实测评测, 安全]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：Google 开发者论坛 Google Workspace Developers 版块的问答帖，收入楼主 vailon 的首帖与 4 条跟进，以及 Abel、DHolloway、Desmond_Lang、Edward_Chu、Jeremy_LaKosh 等用户的回复；论坛页尾的推荐话题未收入。旧笔记 learning-ai-agent 的 Gemini Spark 资料索引引用过这篇。原文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：楼主（个人账号，人在香港）报告 Spark 能读取所有表格，但对任何已有的 Google 表格的写入都会失败，包括设为「知道链接的任何人可编辑」的表格；重新连接 Workspace 也无效。Spark 显示失败的内部工具是 sheets_agent:call，错误为「Failed to verify file permissions: Blocking policy check failed … [PERMISSION_DENIED]」。楼主转述工程团队的答复：在表格中编辑应使用 Sheets 里的 Gemini 侧边栏，而不是独立的 Gemini 应用；其他用户回复遇到相同错误，有人认为「blocking policy check」位于 Gemini 的执行前检查层而不是 Sheets API，可能与账号资格或灰度有关。10 月 16 日楼主回报写入已恢复正常（测试于香港时间 10:14，环境为 Gemini Spark / Tasks 模式），并建议在智能体工具调用失败时自动上报遥测、在聊天中一键提交问题、修复后通知用户。

**保留理由**：用户一手记录的平台侧故障和恢复，并保留了内部工具名与错误信息，说明了 Spark 工具调用和权限检查的一角。
