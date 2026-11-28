---
title: "文档：安全 FAQ"
linkTitle: "文档：安全 FAQ"
date: 2026-11-05
originalTitle: "Grok Bot security FAQ"
sourceUrl: "https://docs.x.ai/grok-bot/security-faq"
altUrls: ["https://cursor.com/docs/grok-bot/security-faq"]
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-12
dateNote: "文档不标日期，取收集日期；2026-11-28 发现原文更新：新增「只屏蔽几个网站」问答（Allow All Sites Except These，至多 50 个主机名，尽力而为）；推理钩子改称只检查模型输入；Shared Bot 改称 Team Bot，xAI 模型改称 SpaceXSI"
tags: [安全, 隐私, 运行环境]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：2026-11 起 cursor.com 的 Grok Bot 文档地址 308 跳转到 docs.x.ai 的同名页，2026-11-28 起改按 docs.x.ai 的 Markdown 版本存档，去掉了文首的分组标签和文末的相关页面列表。以下为首次收录时的说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：这是安全评审常问问题的答案汇编。隔离：每个用户一台独立的 Firecracker microVM，同一用户的所有 Bot 共用该计算机；Bot 没有自己的身份，不能超出登录成员的权限。网络：Network Controls 仅限 Enterprise，可设允许列表，也可选 Allow All Sites Except These，列出至多 50 个主机名（含子域），覆盖 shell、浏览器、WebFetch 和 MCP 服务器，但只是尽力而为、不是安全边界；计算机使用共享静态出口 IP，无专用 IP；无法在客户自有边界内部署，也不支持自带镜像，只能运行在 Cursor 托管云端。审批与日志：Auto Review 在开启强制时检查 shell、应用调用、计算机使用、自动化写入和委派；推理钩子（Enterprise beta）只检查模型输入、不检查动作；审计日志、Action Recording（默认关闭）和 OpenTelemetry 导出均为 Enterprise 专有。模型：团队模型允许列表不管 Grok Bot，没有面向客户的模型选择器；计算机位于美国，Anysphere 持有 ISO/IEC 27001 和 42001 认证。

**保留理由**：以问答形式汇总了安全评审的要点，可快速核对哪些控制是 Enterprise 专有、哪些不支持。
