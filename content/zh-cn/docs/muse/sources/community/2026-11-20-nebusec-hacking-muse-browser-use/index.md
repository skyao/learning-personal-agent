---
title: "黑进 Muse：经浏览器窃取私人对话"
linkTitle: "黑进 Muse 窃取对话"
date: 2026-11-20
originalTitle: "Hacking Muse: Stealing Private Chats Through Browser Use"
sourceUrl: "https://nebusec.ai/research/meta-muse-credential-exposure/"
author: "NebuSec 研究团队"
publisher: "NebuSec"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-21
tags: [安全, 隐私]
products: [muse]
dateNote: "页面 ld:datePublished 为 2026-11-20T00:00:00Z。"
---

{{< source-info >}}

**收录说明**：直接下载；删去文首指向技术详解的站内推广卡片；演示视频改为占位行（附原文视频地址）；配图一张已本地化。技术细节见同站另一篇《Inside Meta Muse: Browser, Sentinel and the Shared-Kernel Boundary》，本轮另收。截至本轮，Meta 未就此研究公开表态（据 The Hacker News 与 All Things Muse 11 月 21 日报道）。

**内容摘要**：安全研究机构 NebuSec 于 11 月 20 日发布研究：恶意网页经 Muse 内置的 Chromium 浏览器（用于生成 PDF 与文档）取得智能体运行容器内的代码执行；利用 Sentinel 对出站请求分类与检查的弱点，在不触发审批提示的情况下把用户的对话历史与存储记忆外传到外部服务器，还能篡改记忆与对话记录；随后用 Linux 内核漏洞逃出容器，取得用户虚拟机的 root 权限，进而接触持久存储、安全凭据库与 Sentinel 本身。攻击只停留在单个用户的虚拟机内，未突破到底层宿主机或其他用户的机器。研究称，全部漏洞在发布前已向 Muse 团队报告并修复。

**保留理由**：首次披露针对 Muse 云端运行环境本身的完整攻击链实测（浏览器→Sentinel 绕过→内核逃逸→凭据库），含 Sentinel 策略细节，是已收 Wardle macOS 漏洞与路透社安全调查之后最实质的安全事件一手来源。
