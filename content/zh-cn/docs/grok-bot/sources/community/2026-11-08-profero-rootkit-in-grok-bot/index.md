---
title: "Grok Bot 内置的 Rootkit：沙箱里的一条命令如何变成远程 root"
linkTitle: "Profero：内置 Rootkit"
date: 2026-11-08
originalTitle: "The Rootkit Built Into Grok Bot"
sourceUrl: "https://profero.io/blog/the-rootkit-built-into-grok-bot"
author: "Omri Segev Moyal"
publisher: "Profero"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
dateNote: "日期取页面元数据的发布日期"
tags: [安全, 运行环境]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：直接下载；去掉了文末的相关文章列表。作者是安全公司 Profero 的研究员，据文中所述，测试起因是一家客户在上线前请他们评估，账号为自费购买；2026-08-24 向 xAI 和运营沙箱基础设施的 Cursor 报告，文中称除 Cursor 漏洞赏金平台的自动回复外没有收到回复，文章略去了标识符、令牌、签名密钥和概念验证代码。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：Profero 测试了 Grok Bot 的云端沙箱：沙箱内无特权的 agent 用户可经无认证的 Docker API 取得所在 VM 的 root，从 VM 磁盘读出每账号令牌和长期凭据，再配合所有沙箱共用的静态口令 `local`，从互联网任意位置在沙箱内执行命令、读写账号保存的全部文件，并在令牌轮换后继续截获新令牌。文章另列五个入口：监督服务无密码、每次启动写入免密 sudo、浏览器 cookie 明文保存、Chrome 调试端口无认证、浏览器扩展签名私钥在镜像里。向厂商提交的 8 个漏洞中列出 7 个，CVSS 3.1 最高 9.6；两个月、240 多个新沙箱构建之后，链条上的问题均未修复。文末给出采用方和基础设施建设方的建议，并说明为何在首次报告 75 天后公开。

**保留理由**：Grok Bot 沙箱隔离与凭据处理的一手安全分析，含逐步复现、CVSS 评分和完整披露时间线，其他资料中没有。
