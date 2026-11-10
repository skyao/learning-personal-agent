---
title: "在受管环境中排查 Microsoft Scout 问题"
linkTitle: "文档：受管环境排障"
date: 2026-09-01
originalTitle: "Troubleshoot Microsoft Scout in managed environments"
sourceUrl: "https://learn.microsoft.com/en-us/microsoft-scout/managed-troubleshoot"
author: "leeclontz"
publisher: "Microsoft Learn"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-10
tags: [运行环境, 安全]
products: [microsoft-autopilot]
updatedAt: "2026-09-01"
dateNote: "文档不标发布日期；日期取页面显示的最后更新日期（updated_at），页面元数据 ms.date 为 2026-08-31"
---

{{< source-info >}}

**收录说明**：Microsoft Learn 文档（Microsoft Scout 文档集，页面标为预发布文档），直接下载，取页面正文；删去了页首的「Read in English」「Edit」与登录提示、页尾的反馈与「Additional resources」区块，站内相对链接改为绝对地址。待翻译。

**内容摘要**：文档面向在加固 Windows 环境（代理、SSL/TLS 检查、Microsoft Defender、AppLocker/WDAC、VDI/RDP、非管理员用户）中部署 Scout 的 IT 和桌面工程师，以症状表开头。要点包括：Scout 有两个可执行文件（Scout app 与捆绑的 copilot.exe），许可和排除都要覆盖两者；Copilot 组件使用 githubcopilot.com 而非 github.com；代理解密 Copilot 端点会导致登录失败，需排除 TLS 检查。"Unable to verify access" 是因为读不到 AllowScoutFrontierAccess，而不是许可问题，可用 reg.exe 或 tenant-policy.json 回退方式处理。其余涉及 Defender/AppLocker 规则、VDI 下的 --disable-gpu、Citrix HDX、非持久 VDI、工作区位置和日志采集；若干做法为当前版本的变通办法。

**保留理由**：这是加固环境中登录失败、启动崩溃等问题的官方排障手册，含网络域名、AppLocker 规则和日志采集方法。
