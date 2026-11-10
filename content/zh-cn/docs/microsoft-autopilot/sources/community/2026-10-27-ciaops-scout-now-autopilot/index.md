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
translation: 已翻译
collectedAt: 2026-11-10
tags: [安全, 隐私, 运行环境]
products: [microsoft-autopilot]
dateNote: "页面同时显示 October 27, 2026 与 October 15, 2026 两个日期，日期取地址中的 2026-10-27"
---

{{< source-info >}}

**收录说明**：面向 MSP 与中小企业的个人技术博客，作者署名 directorcia，以官方文档为依据做独立分析。直接下载；删去了分享按钮、标签列表与作者卡片，题图收入 images/。已翻译。

**内容摘要**：作者说明 Scout 于 2026 年 6 月在 Build 上推出，9 月 25 日产品本身更名为 Autopilot，但文档仍称 Scout，故文中沿用此名。当前 Frontier 版是面向 Windows 11 和 macOS 的桌面应用，可在批准的工作区文件夹中读写文件、运行 shell 命令、驱动浏览器，并连接 Outlook、Teams、SharePoint Lists 以及 OneDrive 等文件；常驻能力来自两种后台模式：每 15 到 120 分钟执行一次检查提示的 Heartbeat，以及按计划或触发条件运行的 Automations。文中引用 Responsible AI FAQ 称，该桌面应用的模型交互经由 GitHub Copilot 处理，数据驻留、保留、敏感度标签执行和 eDiscovery 等 Microsoft 365 保护不适用于这部分处理，所以管理员必须做声明。获取条件包括 Frontier、Intune 策略、声明表单和每位用户一个 GitHub Copilot Business 或 Enterprise 席位；作者还称微软说明 Autopilot 采用 usage-based billing 而非固定的 Copilot 许可。

**保留理由**：这篇从 MSP 和中小企业管理员角度梳理了启用前提和权限暴露风险（用户可访问的范围会被智能体全部遍历），并给出试点做法建议，管理视角在其他材料中少见。

---

Scout 现为 Autopilot：微软常驻智能体究竟如何工作
![漫画：一名女子站在一叠文件上，用双筒望远镜眺望，并引导同事们向前](images/img-01-b17da2.png)

我用过的大多数工作场所 AI 仍然礼貌地坐在那里，等我输入点什么。Microsoft Scout 不一样，而这正是我认为 MSP 和中小企业需要在业务部门有人去找下载链接之前弄清楚它如何工作的原因。

先做点必要的说明。微软 2026 年 6 月在 Build 上把 Scout 作为其第一个「Autopilot」智能体推出。9 月 25 日，它把产品本身更名为 Autopilot，并称其「此前名为 Scout」。是的，和 Windows Autopilot 这个设备预配服务同名，两者毫无关系。文档仍然说 Scout，所以我也这么说。

## 所以它究竟是什么？

Scout 是一个代表你工作、无需你每次提示的智能体。当前的 Frontier 版本是面向 Windows 11 和 macOS 的桌面应用。你在聊天中描述一项任务，Scout 挑选它需要的工具，可见地走完各个步骤，在敏感操作上暂停等待你批准，然后交回结果或把文件保存到你的工作区。

工具才是有意思的部分。Scout 可以在已批准的工作区文件夹中读写文件、运行 shell 命令、驱动浏览器填写表单，并连接 Microsoft 365。这涵盖 Outlook 邮件和日历、Teams 聊天、会议和转录、SharePoint 列表，以及 OneDrive、SharePoint 和 Teams 中的文件。它创建 Word、Excel 和 PowerPoint 文件，记住你的偏好，还能启动并行的子智能体。

让它「常驻在线」的是两种后台模式。Heartbeat 在你离开时每 15 到 120 分钟运行一次检查提示，Automations 则按你定义的日程或触发器运行。9 月的公告更进一步：Autopilot 变为云端托管，在你的租户内拥有自己的身份、记忆和工作区，你可以在 Teams、Outlook 和文档中像同事一样 @提及它。

在底层，它构建于开源 OpenClaw 之上，微软在此基础上加入了 Entra 身份和访问控制。

## 权限问题才是你需要留意的地方

Scout 以用户现有的 Microsoft 365 权限运作。用户看不到的，它也看不到。这听起来让人安心，直到你想起我见过多少中小企业租户在 SharePoint 上到处散落着宽泛的共享链接。一个不知疲倦地遍历用户所能触及的一切的智能体，会比任何审计员更快地发现你的过度共享。

微软自己的 Responsible AI FAQ 里埋着一个更细的细节。在 Frontier 桌面应用中，模型交互通过 GitHub Copilot 处理，适用单独的条款。发生这种情况时，某些 Microsoft 365 保护——例如数据驻留、保留、敏感度标签执行和 eDiscovery——不适用于该处理。这就是管理员必须在任何人使用它之前完成声明的原因。在你勾选那个框之前，先读读那一页。

获取访问权限是刻意设计得繁琐的。你需要在 Microsoft 365 管理中心开启 Frontier、在设备上应用 Intune 策略、提交声明表单，并为每位用户准备一个 GitHub Copilot Business 或 Enterprise 席位。缺任何一项，登录都会失败且没有明确提示，这会带来很有「娱乐性」的 helpdesk 工单。

## 我会怎么做

把这当作面向少数技术能力较强人员的试点，而不是全面推广。先清理权限和共享。保持批准提示开启，抵制点「始终允许」的诱惑。把 heartbeat 和自动化权限严格收紧，因为它们是在无人注视时运行的。还要仔细做预算：微软说 Autopilot 按 usage-based billing 运行，而不是固定的 Copilot 许可证。

我真的认为，能把事情跟到底的智能体是未来的方向。但一个会行动的助手与一个只回答问题的助手是完全不同的物种。在这里做得好的组织，会是那些意识到治理必须在智能体到来之前就绪、而不是之后的组织。

来源：[Microsoft Scout 概述（Microsoft Learn）](https://learn.microsoft.com/en-us/microsoft-scout/overview)、[Responsible AI FAQ](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq)、[管理员访问概述](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)、[推出带有 Home、Code 和 Autopilot 的新 Copilot](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)
