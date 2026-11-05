---
title: "文档：连接私有网络"
linkTitle: "文档：私有网络"
date: 2026-11-05
originalTitle: "Connect to private networks"
sourceUrl: "https://cursor.com/docs/grok-bot/private-networks"
author: "未署名"
publisher: "Cursor（Grok Bot 文档）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-05
dateNote: "文档不标日期，取收集日期"
tags: [运行环境, 安全]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：Grok Bot 的产品文档与帮助页由 Cursor 托管（Cursor 于 2026-08-14 并入 SpaceXSI）。直接下载；去掉了文末的相关页面列表与反馈按钮；折叠式 FAQ 的问题文字原在按钮中，抽取时已保留。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：Grok Bot 计算机运行在 Cursor 云端，通过共享的静态出口 IP 访问互联网，不提供每客户专用 IP。需要访问私有网络时有两种办法：把单个成员的流量经其桌面转出，使目标站点看到该设备的 IP（私有或 VPN 地址的站点仍默认被阻止）；或者用 Team Setup Scripts 在每台团队计算机上安装组织自己的网络客户端。后者仅限 Enterprise，脚本以计算机用户身份运行，计算机启动时和大约每天一次刷新时执行，单个脚本超时 30 分钟，凭据应存为 Team Secret 而不是写进脚本。文中以 Tailscale 作为已验证的配置（经内部出口节点），Cloudflare Tunnel 作为对比；Cursor 不安装、运营或监控这个客户端，也没有脚本结果的整体视图。网络策略是单独一层，仍然适用。

**保留理由**：说明托管计算机怎样接入企业内网、哪些由 Cursor 负责哪些由客户自己负责，对评估私有部署场景的限制有用。
