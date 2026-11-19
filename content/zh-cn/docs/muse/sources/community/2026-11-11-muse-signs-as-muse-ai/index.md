---
title: "Muse 现在以 muse.ai 签名"
linkTitle: "Muse 改以 muse.ai 签名"
date: 2026-11-11
originalTitle: "Meta's Muse Now Signs as Muse.ai: What an AI Agent's Identity Switch Means for Web Bot Auth"
sourceUrl: "https://datadome.co/threat-research/meta-muse-now-signs-as-muse-ai/"
author: "Jerome Segura"
publisher: "DataDome"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-19
tags: [安全]
products: [muse]
---

{{< source-info >}}

**收录说明**：原站对直接下载返回 403，改由浏览器保存页面 PDF 后转文本；PDF 中 cookie 横幅与正文重叠的一段，据 PDF 内嵌坐标层分离还原，并与页面文本抓取结果核对无误；两张数据图已本地化；删去页首推广、作者简介、文末相关推荐与“预约演示”推广段；文内指向另一篇 DataDome 文章的链接已删去，该篇另收。

**内容摘要**：DataDome 观察到，Muse 在 11 月 7 日（周六，太平洋时间午夜前后）开始把部分请求的 Web Bot Auth 签名从 Meta 的 meta.com 密钥目录切换到自有的 muse.ai 密钥目录，约一天半内新旧签名各占一半，至 11 月 9 日（周一）完成切换，此后只用 muse.ai 签名。切换期间 Muse 的签名流量总量保持平稳，新旧目录重叠约 60 小时；但并非所有请求都带签名，截至 11 月 10 日仍约有一半请求无签名。Web Bot Auth 的机制是：客户端用私钥按 HTTP Message Signatures（RFC 9421）签署每条 HTTP 请求，并在 Signature-Agent 头中指向 `/.well-known/http-message-signatures-directory` 下的公钥目录；与可随意复制的用户代理字符串不同，没有私钥就无法伪造有效签名。文章指出，只信任 meta.com 的验证方自 11 月 9 日起会把 Muse 的请求视为未验证；Meta 此举开创了「一个产品一个签名身份」的模式，而 Muse 是目前使用最广泛的 agentic browser，其签名方式的变化会影响网站收到的很大一部分 AI 智能体流量。

**保留理由**：这篇提供了 Muse 从 meta.com 切换到自有 muse.ai 签名身份的完整时间线与切换期间的流量实测数据，包括约 60 小时的重叠窗口和截至 11 月 10 日约半数请求仍无签名的情况，是关于 Muse 身份标识变化的一手观测记录。
