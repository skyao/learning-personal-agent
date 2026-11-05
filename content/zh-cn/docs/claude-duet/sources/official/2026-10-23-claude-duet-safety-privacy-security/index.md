---
title: "Claude Duet 的安全、隐私与安全性"
linkTitle: "安全、隐私与安全性"
date: 2026-10-23
originalTitle: "Claude Duet Safety, Privacy, and Security"
sourceUrl: "https://claude.com/resources/articles/claude-duet-safety-privacy-and-security"
author: "未署名"
publisher: "Anthropic"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
tags: [安全, 隐私, 运行环境]
products: [claude-duet]
---

{{< source-info >}}

（收集说明：直接下载；去掉了分类与阅读时长信息栏和文末的相关文章推荐；4 张示意图（审批流程、信息去向、浏览器边界、凭证路径）及首图已下载，其中 1 张超过 600 KB 的已缩小。原文全文存于本目录的 original.md，网站上不显示，待翻译。）

**收集者摘要**：文章说明 Claude Duet 的三条设计原则：对用户及他人在连接应用中分享的信息审慎处理、用户掌控其代理行为、模型永远看不到用户凭证。审批方面，发送敏感消息、付款等操作前会弹出审批卡，另有一个基于 Claude Code auto mode 分类器扩展而来、在模型之外运行的检查判断操作是否符合用户意图；买卖证券、账户间转账、访问他人账户等即使批准也不允许，付款使用限定商户和金额的一次性卡。信息方面，新的安全分类器在每条消息发出前检查敏感信息，按「绝不分享」等等级处理，拦截后可改写再请用户批准。凭证方面，密码在用户设备上加密、只在专用云端浏览器机器上解密，登录令牌沿用 Claude Managed Agents 的设计；浏览器运行在独立虚拟机中，模型只能通过固定命令操控，并以专门的 User-Agent 和公开的 IP 地址表明自己是智能体。文末介绍了 Safeguards 团队的评估、红队测试、外部审计和漏洞赏金计划。

**保留理由**：官方对 Claude Duet 权限、审批、敏感信息与凭证隔离设计最完整的说明，是分析其用户控制机制的核心资料。
