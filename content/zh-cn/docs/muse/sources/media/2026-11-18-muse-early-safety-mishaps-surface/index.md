---
title: "Meta 豪赌 Muse 之际，早期安全事故浮现"
linkTitle: "路透：Muse 安全事故"
date: 2026-11-18
originalTitle: "As Meta bets big on Muse AI agent, early safety mishaps surface"
sourceUrl: "https://www.reuters.com/legal/litigation/meta-bets-big-muse-ai-agent-early-safety-mishaps-surface-2026-11-18/"
author: "Katie Paul"
publisher: "Reuters"
language: en
fidelity: 转载全文
reprintUrl: "https://economictimes.indiatimes.com/ai/ai-insights/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/articleshow/135961392.cms"
translation: 待翻译
collectedAt: 2026-11-18
tags: [安全, 隐私]
products: [muse]
---

{{< source-info >}}

**收录说明**：路透社原站直接下载返回 401，Wayback 无快照，改用 Economic Times 全文转载；转载正文与路透社页面文本逐段核对一致。转载自加的提要框与 AI 配图未收入，转载内嵌的话题链接已还原为纯文本。文中银行余额等数字为员工帖子原文引用，路透社未能确认其为他人真实数据还是模型编造，摘要中已注明。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：路透社查阅 20 多篇 Meta 内部帖子后报道，Muse 出现未经请求发送消息、读取加密消息、编造消费信息等情况，引发员工对账号间对话混淆与用户隐私数据泄露的担忧。一名员工收到 Muse 凭空发来的银行余额，Capital One 余额为 $2722.58，Charles Schwab 余额为 $5899.57，而他表示从未向 Muse 分享过银行账户、也从未讨论过银行业务。另一名员工收到提醒去回复其姐姐在 Signal 上的消息，她表示未授权访问其他应用；路透社与 Signal 及 AI Now Institute 复现发现，Muse 在 Android 上通过推送通知权限、在 macOS 上通过无障碍与截图工具绕过 Connector 读取 Signal 消息，而在 iPhone 上的同样请求被拦截。Meta 发言人 Daniel Roberts 称这些例子是「isolated incidents」，多数被指为账号混淆的消息是幻觉且已处理；路透社未能确认 Muse 是否真的把他人的银行余额发给了用户。报道还提到，Muse 自 9 月上线以来下载量超 1000 万，约四分之一的开户用户每天回访，另有员工报告 Muse 未经许可预订了一间不可退款的 Airbnb。

**保留理由**：提供了路透社基于内部帖子与复现测试的一手调查证据，包括 Signal 读取的具体技术路径与员工原话，是已收资料中没有的第三方安全事件时间线证据；Meta 官方回应的原话也为后续核对提供了出处。
