---
title: "Muse 里面有什么？"
linkTitle: "Muse 沙箱剖析"
date: 2026-09-01
originalTitle: "What's in a Muse?"
sourceUrl: "https://rohanadwankar.github.io/posts/sandbox2.html"
author: "Rohan Adwankar"
publisher: "Rohan Adwankar（个人博客）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-21
tags: [运行环境, 安全]
products: [muse]
dateNote: "页面未标发布日期；仅知发表于 2026 年 9 月（文中观测日期为 9 月 11 日），按当月 01 日记；CSA 研究札记引作 September 2026。本轮经 CSA 引文发现后回填。"
---

{{< source-info >}}

**收录说明**：直接下载；经 CSA 研究札记引文发现回填；文中的两处一级标题式强调段按规则改为引用块；页面未标发布日期，见 dateNote。

**内容摘要**：个人博客对 Muse 沙箱的独立技术剖析：对照 Cloud Hypervisor 与 Firecracker 两种虚拟机监视器的差异，实测记录虚拟机的启动、滚动更新与生命周期管理，指出重启即替换整台虚拟机、虚拟机监视器不随 guest 重启存活；核查 metaaivm.com 与出站路径，记录 2026 年 8 月 15 日 cli.github.com 触发的全网人工审批风暴等 egress 细节；文中多处结论注明为实测而非推断，并区分了已验证与未验证的部分。

**保留理由**：对 Muse 运行时沙箱少有的独立实测剖析，含虚拟机监视器、启动与出站的一手观测，与已收官方安全文章、iFynx 解析及 NebuSec 技术详解互为对照；经本轮 CSA 引文发现后回填。
