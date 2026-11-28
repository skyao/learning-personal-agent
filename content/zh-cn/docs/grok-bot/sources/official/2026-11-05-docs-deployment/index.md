---
title: "文档：向组织部署 Grok Bot"
linkTitle: "文档：组织部署"
date: 2026-11-05
originalTitle: "Deploy Grok Bot to your organization"
sourceUrl: "https://docs.x.ai/grok-bot/deployment"
altUrls: ["https://cursor.com/docs/grok-bot/deployment"]
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标日期，取收集日期；2026-11-28 发现原文更新：Linux 的 .deb/.rpm 安装在 Update required 界面直接给出 apt/dnf 升级命令；仓库暂无新版时改提示下载最新包；其余主要是措辞与版式调整，并新增相关页面列表"
tags: [运行环境, 设备]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：2026-11 起 cursor.com 的 Grok Bot 文档地址 308 跳转到 docs.x.ai 的同名页，2026-11-28 起改按 docs.x.ai 的 Markdown 版本存档，去掉了文首的分组标签和文末的相关页面列表。以下为首次收录时的说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：IT 团队用现有设备管理工具部署 Grok Bot 桌面应用：macOS（.dmg）、Windows（Setup .exe，按用户安装，可 /S 静默安装）、Linux（.deb、.rpm、AppImage），iPhone 需 iOS 18 以上，Android 需 9 以上。托管计算机是云端的 Linux 机器，每位成员一台，不加入 MDM，Enterprise 团队可通过 Team Setup Scripts 安装自有工具。应用无法由管理员关闭更新，成员可关闭 **Automatic updates**，但仍会收到新版提示；低于最低版本或超过最大期限的旧版会显示 **Update required**，两项限制远程设置且不公布；Linux 的 .deb/.rpm 安装由包管理器更新，该界面会显示升级命令（apt 或 dnf），仓库没有新版时改为提示下载最新包。托管计算机的镜像由系统维护，新镜像出现时会在后台逐步重建空闲计算机；Enterprise 管理员可以批量重建。登录用 Cursor 账号和 SSO，没有单独的 Grok Bot 登录。

**保留理由**：讲清了客户端只是聊天、审核和审批的瘦客户端，工作都在托管计算机上，以及版本与镜像更新的规则，对研究其运行架构和企业落地门槛有用。
