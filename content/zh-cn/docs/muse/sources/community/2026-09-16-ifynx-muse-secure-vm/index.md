---
title: "Muse Secure VM 与 Confidential VM 解析"
linkTitle: "Secure VM 解析"
date: 2026-09-16
originalTitle: "Meta Muse Secure VM & Confidential VM Explained"
sourceUrl: "https://ifynx.com/blog/meta-muse-personal-ai-agent-secure-vm/"
author: "未署名"
publisher: "iFynx"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-06
updatedAt: 2026-11-02
dateNote: "页面元数据发布 2026-09-16；正文以 2026-11-02 为现状时点（Confidential VM 未发布），当月曾更新"
tags: [运行环境, 安全, 隐私]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载返回 403，改用网页抓取工具取得全文，关键句已与检索结果对照；无配图。原文 9 月 16 日发布，11 月 2 日前后更新（加入 Confidential VM 设置页传闻与现状时点），date 取发布日期、updatedAt 记 2026-11-02。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：作者解析 Muse 的安全架构：每位用户独享一台云虚拟机（Secure VM），内有独立的运行单元、浏览器与连接凭证；Sentinel 单独审批一切对外流量，authd 以替身令牌代替真实凭证，连接器调用在权限分离的工作进程中进行。Confidential VM 计划用用户独掌的密钥加密整台虚拟机、使 Meta 也无法访问，但截至 11 月 2 日尚未发布，源码已交审计方；10 月 20 日有报道称其设置页已在 Muse 网页版部分建成。作者强调，Secure VM 防的是其他用户与智能体本身，运营方的访问目前靠制度约束而非密码学手段。

**保留理由**：独立技术分析，把 Secure VM 与 Confidential VM 的区别归结为“制度隔离不等于机密计算”，并记录了 10 月 20 日 Confidential VM 设置页传闻这一已收资料没有的新线索。
