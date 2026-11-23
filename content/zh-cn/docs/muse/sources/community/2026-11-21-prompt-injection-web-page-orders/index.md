---
title: "你让 Muse 读的网页，正在给它下指令"
linkTitle: "提示注入与 Muse"
date: 2026-11-21
originalTitle: "The Web Page You Asked Muse to Read Just Gave It Orders."
sourceUrl: "https://aihomebuilding.com/stories/muse-prompt-injection-web-talks-back-2026"
author: "Catherine Chen"
publisher: "AI Home Building"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-21
tags: [安全, 运行环境]
products: [muse]
dateNote: "页面 ld:datePublished 为 2026-11-21。"
---

{{< source-info >}}

**收录说明**：直接下载；作者在文末「What we did not verify」一节明确声明未对 Muse 本身做提示注入实测、未发现已公开的针对 Muse 的提示注入事件，AgentDojo 数据来自非 Muse 模型的基准。

**内容摘要**：文章指出，提示注入的根源在于模型无法区分指令与数据：用户指令与网页内容进入同一输入流，模型没有可靠办法判断哪句话该服从、哪句只是待读的文字，OWASP 将其列为 LLM 应用十大风险之首 LLM01:2025，NIST、MITRE（编号 AML.T0051）与 CWE（编号 CWE-1427）均有对应条目。文中回顾了一系列间接注入案例：2025 年 1 月一封邮件令 Microsoft 365 Copilot 外泄数据（EchoLeak，编号 CVE-2025-32711，2025 年 6 月修复）；2025 年 8 月藏在 Reddit 剧透标签后的指令劫持 Perplexity Comet，同月日历事件标题中的指令劫持 Google Gemini 助手；2026 年 10 月 1 日一封邮件令 Manus 执行攻击者代码并暴露 Gmail、Drive 与 GitHub 令牌，9 月 24 日至 10 月 13 日间 Salesforce Agentforce、GitLab AI Gateway 与 Roo Code 也先后出现类似案例。Brave 的演示显示，Mozilla Tabstack 在摘要网页时被隐藏指令 redirect 至攻击者表单并提交对话记录，而全本地运行的 macOS 自动补全助手 Cotypist 也会被本地文档中的指令操纵，说明本地部署本身并不能防御此类缺陷；Google 研究人员监测到 2025 年 11 月至 2026 年 2 月间网页中恶意提示注入载荷增加了 32%。作者认为 Muse 同时具备 Simon Willison 所说的「致命三要素」——访问私人数据、接触陌生人撰写的内容、拥有对外发送信息的通道：它读取 Gmail、文件、日历与开放网络，可发消息、致电美国商家、订票购物并在其虚拟机上运行 shell 命令。Meta 帮助页面称 Muse 以模型训练、自动检测系统与任务期间的访问限制等多层防护「帮助检测并抵御」此类攻击，凭据存放在模型看不到的安全凭据库中，重要权限与安全检查独立于模型运行，但未公布任何攻击成功率或基准数字；AgentDojo 97 项任务的基准显示，工具过滤可把某模型的攻击成功率从 57.69% 降至 6.84%，但正常任务成功率也从 69.0% 降至 41.49%，而重复攻击 25 次可把平均成功率从 57% 提升至 80%。

**保留理由**：提供了以 Muse 为落点的提示注入系统性长篇梳理，引用了 Meta 官方帮助页面的防护表述与 AgentDojo 等基准数据，是已收安全类资料中少有的完整论述。
