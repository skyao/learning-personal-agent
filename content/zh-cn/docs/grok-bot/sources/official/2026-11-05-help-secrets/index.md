---
title: "帮助：安全保存秘密"
linkTitle: "帮助：保存密钥"
date: 2026-11-05
originalTitle: "Store secrets securely"
sourceUrl: "https://cursor.com/help/grok-bot/secrets"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [安全, 隐私, 连接器]
products: [grok-bot]
---

{{< source-info >}}

（收集说明：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

**收集者摘要**：Vault 保存登录、卡和联系信息，让 Bot 能登录、结账而不看到密码、卡号和安全码；它能看到联系信息和保存了哪些登录。Vault 适用于整个账号，保存的内容对所有 Bot 可用，不能限定给某个 Bot，也不支持共享 Bot。新建账号时若让 Bot 自己选密码，由 Vault 生成并保存，Bot 看不到。文中明确：保存卡片后没有设置能要求每次使用都批准，想逐次批准就不要保存卡；API 密钥等通过遮蔽的安全秘密卡输入，不写入聊天；共享 Bot 的秘密仅显示名称与说明，对其所有队友的聊天都生效。保存的值只写不读，Recover、Reset 和计算机更新会清除安装的应用和包，写进文件里的秘密可能随之消失，但用安全卡、Secrets 或 Vault 保存的不受影响。

**保留理由**：清楚给出凭证、卡和 API 密钥的处理方式及限制，尤其是保存卡后不再逐次批准这一点，对研究凭证处理很重要。
