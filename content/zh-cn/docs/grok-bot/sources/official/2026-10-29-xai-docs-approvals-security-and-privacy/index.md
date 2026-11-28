---
title: "文档（docs.x.ai）：审批、安全与隐私"
linkTitle: "docs.x.ai：审批、安全与隐私"
date: 2026-10-29
originalTitle: "Approvals, security, and privacy"
sourceUrl: "https://docs.x.ai/grok-bot/approvals-security-and-privacy"
author: "未署名"
publisher: "SpaceXSI（Grok Bot 文档，docs.x.ai）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
updatedAt: 2026-11-23
dateNote: "文档不标发布日期；日期取页面结构化数据中的最后修改时间（2026-10-29T00:00:00Z）；2026-11-28 发现原文更新：Shared Bots 改称 Team Bots；已有 20 条允许规则时「总是允许」改为替换最旧一条；新增聊天中 Bot 可看到 Vault 所存银行卡的号码和安全码以便结账"
tags: [安全, 隐私]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 有两套官方文档：cursor.com 上的一套已在 2026-11-05 收入，这一页属于 docs.x.ai 上的另一套（SpaceXSI Docs）。直接下载站点提供的 Markdown 版本，去掉了文首的分组标签。旧笔记 learning-ai-agent 引用过这一页，2026-11-06 复核后收入。cursor.com 的安全文档面向管理员，这页面向用户，重合不多。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：Auto Review 默认开启，用模型判断哪些操作需要用户确认；审批卡有 **Allow once**、**Always allow**、**Deny** 三种选择，**Always allow** 会存成规则，拒绝后 Bot 在用户发新消息前不会再尝试。从聊天发起的审批卡一直等待，后台任务发起的卡 30 分钟后过期。自定义规则「Allow automatically」「Ask first」各最多 20 条，每条最多 1,000 字符；已有 20 条允许规则时，卡上的 **Always allow** 会替换最旧的一条。Vault 中的登录和 Secure Form 的值填入页面时不给模型看，但在 Grok Bot 应用的聊天里，Bot 能看到 Vault 中所存银行卡的号码和安全码，用于结账。在用户本地电脑上执行命令默认 **Ask every time**，每台桌面单独设置，团队管理员可设上限。文档明确说云端电脑由用户名下所有 Bot 共用，分享 Bot 也不是安全边界；Team Bot 里所有者添加的应用、密钥、技能和文件对每位队友的聊天都生效；删除 Bot 不会清除共享电脑上的文件。

**保留理由**：给出了用户侧审批机制的具体规则（超时、规则数量、默认值），以及官方自己承认的安全边界。
