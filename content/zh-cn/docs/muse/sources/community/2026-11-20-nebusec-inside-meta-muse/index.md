---
title: "深入 Meta Muse：浏览器、Sentinel 与共享内核边界"
linkTitle: "Muse 内部架构剖析"
date: 2026-11-20
originalTitle: "Inside Meta Muse: Browser, Sentinel and the Shared-Kernel Boundary"
sourceUrl: "https://nebusec.ai/research/inside-meta-muse/"
author: "NebuSec 研究团队"
publisher: "NebuSec"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-21
tags: [安全, 运行环境]
products: [muse]
dateNote: "页面 ld:datePublished 为 2026-11-20T00:00:00Z。"
---

{{< source-info >}}

**收录说明**：直接下载；三张配图（请求路由架构图、审批提示截图、权限设置截图）已本地化；文中的代码块与命令输出照录。本篇为同站《Hacking Muse: Stealing Private Chats Through Browser Use》一文的技术详解，本轮另收。

**内容摘要**：技术详解：每位用户的智能体运行在 2 vCPU、8 GiB 的 Cloud Hypervisor 虚拟机内的 systemd-nspawn 容器中，容器内 UID/GID 0 映射到虚拟机中的 131072；hatch-safety、Sentinel 与 hatch-authd 三项服务运行在容器之外，凭据以替代令牌形式交给智能体、由 Sentinel 在出站时换成真实凭据。Muse 有四种浏览器后端，研究针对的是容器内随智能体运行的 Chromium：10 月初仍为 152 版，存在多个可用的公开 V8 漏洞，且 PDF 导出进程关闭了 IPC 沙箱，单个渲染器漏洞即可在容器内执行代码。Sentinel 按读/写分类出站请求，无正文的 GET、HEAD、OPTIONS 可静默放行，并以解码筛查、熵阈值、模型审查与流量预算检查内容，研究者在其规则内完成了无提示外传。内核为定制的 Ubuntu Linux 7.0，若干加固选项被关闭，自动漏洞利用生成框架的成功率超过 99.9%；逃逸后可达持久存储、凭据库与 Sentinel，虚拟机本身还有独立的公网 IPv6 地址可直接出网；未突破 Cloud Hypervisor 到宿主机。

**保留理由**：对 Muse 运行环境迄今最深入的独立架构剖析，披露了容器内外服务划分、四种浏览器后端、Sentinel 策略细节与内核配置等官方未公开的实现细节，与已收官方安全文章、iFynx 解析互为对照。
