---
title: "Scout 现为 Autopilot：微软常驻智能体究竟如何工作"
linkTitle: "CIAOPS：数据边界"
date: 2026-10-27
originalTitle: "Scout, Now Autopilot: How Microsoft’s Always-On Agent Really Works"
sourceUrl: "https://blog.ciaops.com/2026/10/27/scout-now-autopilot-how-microsofts-always-on-agent-really-works/"
author: "directorcia"
publisher: "CIAOPS"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-10
tags: [安全, 隐私, 运行环境]
products: [microsoft-autopilot]
dateNote: "页面同时显示 October 27, 2026 与 October 15, 2026 两个日期，日期取地址中的 2026-10-27"
---

{{< source-info >}}

**收录说明**：面向 MSP 与中小企业的个人技术博客，作者署名 directorcia，以官方文档为依据做独立分析。直接下载；删去了分享按钮、标签列表与作者卡片，题图收入 images/。待翻译。

**内容摘要**：作者说明 Scout 于 2026 年 6 月在 Build 上推出，9 月 25 日产品本身更名为 Autopilot，但文档仍称 Scout，故文中沿用此名。当前 Frontier 版是面向 Windows 11 和 macOS 的桌面应用，可在批准的工作区文件夹中读写文件、运行 shell 命令、驱动浏览器，并连接 Outlook、Teams、SharePoint Lists 以及 OneDrive 等文件；常驻能力来自两种后台模式：每 15 到 120 分钟执行一次检查提示的 Heartbeat，以及按计划或触发条件运行的 Automations。文中引用 Responsible AI FAQ 称，该桌面应用的模型交互经由 GitHub Copilot 处理，数据驻留、保留、敏感度标签执行和 eDiscovery 等 Microsoft 365 保护不适用于这部分处理，所以管理员必须做声明。获取条件包括 Frontier、Intune 策略、声明表单和每位用户一个 GitHub Copilot Business 或 Enterprise 席位；作者还称微软说明 Autopilot 采用 usage-based billing 而非固定的 Copilot 许可。

**保留理由**：这篇从 MSP 和中小企业管理员角度梳理了启用前提和权限暴露风险（用户可访问的范围会被智能体全部遍历），并给出试点做法建议，管理视角在其他材料中少见。
