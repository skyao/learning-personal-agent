---
title: "The Register：不再只是 Copilot，微软的 AI 想接管方向盘"
linkTitle: "The Register 06-03"
date: 2026-06-03
originalTitle: "No longer just a Copilot, Microsoft's AI wants to take the wheel"
sourceUrl: "https://www.theregister.com/ai-and-ml/2026/06/03/no-longer-just-a-copilot-microsofts-ai-wants-to-take-the-wheel/5250718"
altUrls: []
author: "Brandon Vigliarolo"
publisher: "The Register"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-14
tags: [发布, 安全]
products: [microsoft-autopilot]
---

{{< source-info >}}

**收录说明**：直接下载。删去了署名与发布时间行（已在来源信息中）、正文中的广告位和文末标签；保留了副标题。第一轮收集（2026-11-10）曾因「只复述公告」放弃，2026-11-14 按分析一侧的资料缺口改为收录：文中写明向微软询问安全细节未获回复，是 dSebastien 综述所转述说法的原文。已翻译。

**内容摘要**：The Register 报道微软在 Build 上宣布「Autopilot」这一新的 agent 类别，首个 agent 是 Scout，并引用公告称它跨云、桌面和网页连接 Teams、Outlook、OneDrive、SharePoint 以及聊天、邮件、日历、联系人。文章转述 Omar Shahine 的说法：Autopilot agent 有自己的身份，在组织设定的访问控制内自主行动，并绑定 Entra 身份以便把活动归属到具体用户的 Scout。文章指出 Scout 号称企业级安全，同时由安全声誉不佳的 OpenClaw 驱动，微软没有说明对常见 AI 攻击还有哪些防护，向微软询问安全细节截稿前未获回复。文中还写到 Scout 只向「select group of customers」和 Frontier 参与者预览，Frontier 用户须是 GitHub Copilot 订阅者，而 GitHub Copilot 刚转为用量计费。

**保留理由**：这是 dSebastien 综述中 The Register 安全质疑（防护不明、微软未回应）的原文，也是发布时媒体对 GitHub Copilot 订阅门槛与用量计费成本的记录。


---

始终在线的 agent 承诺让工作不断向前推进，前提是你信任它处理几乎所有事情

让开吧，Copilot：Microsoft 正在推出一类名为「Autopilot」的新型 agentic AI，首个 agent 是 Scout。不难猜到 Microsoft 期望这些东西如何运作：时刻盯着你的一举一动，并在后台采取行动，据称是为了简化你的工作日。

Microsoft 周二在 Microsoft Build 上[宣布](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)了 Autopilot 和首个 Autopilot agent Scout，称它及未来的其他 Autopilot 是「自主工作的始终在线 agent（always-on agents that work autonomously）」，在后台保持活跃，以「了解工作如何在你的应用和系统之间完成」，并且可以「无需每次都被提示就采取行动」。

例如，Scout 可以在用户需要时通过 Teams 与之交互，但除了用户需要直接向它查询的情况之外，它始终在那里。

「它跨云、桌面和网页运行，连接 Teams、Outlook、OneDrive 和 SharePoint，以及驱动你一天工作的数据，包括聊天、电子邮件、日历和联系人，」Microsoft Scout 公司副总裁 Omar Shahine 在公告中写道。

据 Shahine 说，Autopilot agent 据称有自己的身份，并能在组织对其活动设定的约束内自主行动（组织可以设置访问控制）。Shahine 说，让 Autopilot 以自动驾驶方式运行「创造了一种更持久的方式来保持工作运转，即使你的注意力在别处，工作也能继续」。

比如说，你需要安排一次会议：Scout 可以自行处理日程安排并考虑时区；它可以标出它认为对用户特别重要的会议，并生成它认为用户在预定时间之前需要准备的材料。Scout 还可以识别临近的截止日期，在用户日历上预留时间，让他们处理某个特定项目，「发现风险，比如停滞的决策」，基本上就像一个工作保姆，对每一件需要完成的小事都高度敏感，替你安排一天。

希望你的新 Microsoft 保姆机器人比它的前任 Copilot [更可靠](https://www.theregister.com/software/2026/04/02/even-microsoft-know-copilot-cant-be-trusted/5221005)，Microsoft 自己就警告 Copilot 的输出可能并不总是准确。

## 准备好迎接你环境中一个爪形的漏洞

「Microsoft Scout 以企业级安全与控制构建，因此从第一天起就可以在你的组织中被信任，」Shahine 在发布说明中写道，紧接着就指出它由 OpenClaw 驱动，而 OpenClaw 的[安全声誉](https://www.theregister.com/security/2026/02/03/diy-ai-bot-farm-openclaw-is-a-security-dumpster-fire/4136886)和[替用户做出糟糕决定](https://www.theregister.com/software/2026/05/05/british-mathematician-hands-openclaw-agent-a-credit-card/5228654)的记录都算不上出色。（译注：标题原文为 "a Claw-shaped hole"，其中 Claw 对应 OpenClaw 的名字。）

Microsoft 声称，Scout 以及它将来发布的任何 Autopilot agent 都绑定到一个 Entra 身份，使其在企业环境中的活动可以归属到某个特定人员的 Scout agent，并表示它在组织设定的访问控制范围内行动，但尚不清楚还包含哪些针对常见 AI 攻击手段的其他保护。

## 更多背景

- [### Microsoft Copilot 要劫持你的浏览器……为了你自己的方便](/software/2026/03/05/copilot-swallows-your-browser-youre-welcome/4599126)
- [### Microsoft 给 Copilot 刷了一层新漆，把烦人的按钮藏了起来](/ai-ml/2026/05/29/microsoft-slaps-new-coat-of-paint-on-copilot-buries-annoying-button/5248442)
- [### Microsoft 让 Copilot 在 Office 里更容易唤起，更难忽视](/personal-tech/2026/05/12/microsoft-makes-copilot-easier-to-summon-harder-to-ignore-in-office/5238612)
- [### Windows 11 上的 Copilot Vision 向 Microsoft 服务器发送数据](/software/2025/07/23/copilot-vision-on-windows-11-sends-data-to-microsoft-servers/271063)

正如我们此前指出的，[让 AI agent 做出其运营者从未想要的行为](https://www.theregister.com/special-features/2026/03/23/ai-agents-are-gullible-and-easy-to-turn-into-your-minions/5222765)往往出奇地容易，而[恶意网页可以注入提示词](https://www.theregister.com/security/2026/02/10/ai-agents-can-spill-secrets-via-malicious-link-previews/4606257)，诱使它们泄露敏感信息；这两种情况下，这类攻击都可以在没有任何用户直接交互的情况下发起。

我们向 Microsoft 询问了有关 Autopilot 和 Scout 安全方面的更多细节，但在截稿前没有收到回复。

另外值得注意的是，Microsoft Scout 的访问范围非常有限，只有「选定的一批客户」（select group of customers）获得预览访问权限，此外还有参与 Frontier 计划的组织，该计划让他们提前使用 Copilot 和其他 Microsoft AI 功能。

还有一点需要注意：Frontier 参与者只有是 GitHub Copilot 订阅者，才能获得 Scout 预览。GitHub Copilot 最近转向了按用量计费的模式，账单[飙升](https://www.theregister.com/ai-and-ml/2026/06/02/github-copilot-users-threaten-exit-as-metered-billing-kicks-in/5249826)，所以如果你选择尝试，也要预料 Microsoft 的账单会上涨。®
