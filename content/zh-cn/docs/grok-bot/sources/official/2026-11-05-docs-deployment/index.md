---
title: "文档：向组织部署 Grok Bot"
linkTitle: "文档：组织部署"
date: 2026-11-05
originalTitle: "Deploy Grok Bot to your organization"
sourceUrl: "https://cursor.com/docs/grok-bot/deployment"
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

**内容摘要**：IT 团队用现有设备管理工具部署 Grok Bot 桌面应用：macOS（.dmg）、Windows（Setup .exe，按用户安装，可 /S 静默安装）、Linux（.deb、.rpm、AppImage），iPhone 需 iOS 18 以上，Android 需 9 以上。托管计算机是 Cursor 云端的 Linux 机器，每位成员一台，不加入 MDM，企业版可通过 Team Setup Scripts 安装自有工具。应用无法由管理员关闭更新，成员可关闭自动更新，但仍会收到新版提示；低于最低版本或超过最大期限的旧版会显示「Update required」，两项限制由 Cursor 远程设置且不公布。托管计算机的镜像由 Cursor 维护，新镜像出现时会在后台逐步重建空闲计算机；管理员可以在企业版里批量重建。登录用 Cursor 账号和 SSO，没有单独的 Grok Bot 登录。

**保留理由**：讲清了客户端只是聊天、审核和审批的瘦客户端，工作都在托管计算机上，以及版本与镜像更新的规则，对研究其运行架构和企业落地门槛有用。
