---
title: "文档：配置 TLS 检查代理"
linkTitle: "文档：TLS 检查代理"
date: 2026-11-05
originalTitle: "Configure TLS-inspecting proxies"
sourceUrl: "https://cursor.com/docs/grok-bot/proxies"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [运行环境, 设备]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：桌面应用从成员设备连到两处：Cursor API（*.cursor.sh）和成员托管计算机的嵌套主机名（*.*.cursorvm.com）。带 TLS 检查的安全网关（如 Zscaler）常放行前者而破坏后者，表现为计算机设置挂起，聊天有时仍可用。文中列出必须放行的域名模式，其中 *.*.cursorvm.com 必需，只配 *.cursorvm.com 仍会失败；这些域名还要豁免 TLS 检查并关闭响应缓冲，且要应用到包括离网在内的所有配置。验证办法包括用 curl 查看证书签发方应为 Amazon RSA、用 nslookup 查计算机主机名、测试流式输出。文末区分了四种相近的控制：设备到 Cursor 的路径、计算机可访问的目的地（网络策略）、经桌面转出、在计算机上安装网络客户端。

**保留理由**：明确了客户端到托管计算机的连接路径和常见故障原因，也从侧面说明计算机是通过独立主机名与应用相连的。
