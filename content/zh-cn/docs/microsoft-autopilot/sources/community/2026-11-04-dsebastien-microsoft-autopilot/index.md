---
title: "Microsoft Autopilot"
linkTitle: "dsebastien：时间线"
date: 2026-11-04
originalTitle: "Microsoft Autopilot"
sourceUrl: "https://www.dsebastien.net/microsoft-autopilot/"
author: "Sébastien Dubois"
publisher: "dsebastien.net"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [发布, 开放与价格, 运行环境]
products: [microsoft-autopilot]
---

{{< source-info >}}

**收录说明**：个人博客的条目式综述，梳理 Scout 到 Autopilot 的时间线并列出参考来源。直接下载；删去了作者卡片、订阅与社区推广区块、文末「Related」「Keep reading」，图片收入 images/。已翻译。

**内容摘要**：文章按时间线梳理 Scout 到 Autopilot：2026 年 3 月 31 日 Omar Shahine 转任负责 Microsoft 365 个人助手的新角色，5 月 4 日 GeekWire 报道内部已有 3,000 多名日活用户，6 月 2 日 Build 发布 Scout，9 月 25 日更名为 Autopilot，私有预览自月底开始。作者指出更名不只是改名：Scout 是面向 Windows 11 和 macOS 12 或更高版本的桌面应用，Autopilot 则是云端托管；Scout 的模型调用经由 GitHub Copilot，Responsible AI FAQ 称数据驻留、保留、敏感度标签执行和 eDiscovery 不适用于该处理路径，Autopilot 对应条款尚未发布。计费为 usage-based billing，未公布价格，也没有正式可用日期。作者的看法是：微软在底层采用 OpenClaw 是该领域最值得注意的事，每个智能体独立身份的做法正确，但数据路径令欧洲公司担忧；他还单列了文中信息的局限，如 Autopilot 的事实仅来自 9 月 25 日一篇微软博文加媒体报道，要求、价格和数据驻留条款均未发布。

**保留理由**：这篇汇总了 Scout 到 Autopilot 的时间线、两个形态的差异、需求与计费，以及哪些信息已确认、哪些仍未知，是理解更名前后差异和公开信息边界的整理性材料。

---

Microsoft Autopilot

简而言之

Microsoft Autopilot 是微软的「持续在线、主动且个人化的智能体，即使你不在也会继续工作」。你给它一个名字、一个角色和一个目标，它就会在你的 Microsoft 365 租户内工作，无需等待提示：它监视频道、跟进线程、运行周期性工作，并……

## 从 Scout 到 Autopilot

| 日期 | 发生了什么 |
| --- | --- |
| 2026 年初 | 据报道，Satya Nadella 曾把 OpenClaw 斥为类似「病毒」的安全风险（二手来源，经 GeekWire；未找到原始出处） |
| 2026 年 3 月 31 日 | Omar Shahine 转任新职，负责 Microsoft 365 的个人助手 |
| 2026 年 5 月 4 日 | GeekWire（Mary Jo Foley）报道「Project Lobster」/「ClawPilot」：一个基于 OpenClaw 的桌面环境，截至 5 月 1 日内部日活用户超过 3,000 人，而一周前只有 100 人 |
| 2026 年 6 月 2 日 | Build：Shahine 发布 Microsoft Scout，称其为名为「Autopilots」的新品类中的第一个智能体，「由 OpenClaw 开源技术驱动」。实验性 Frontier 版本，私有预览 |
| 2026 年 6 月 | OpenClaw 基金会与 Windows 团队宣布长期合作，让 Windows 成为一流的 OpenClaw 平台 |
| 2026 年 7 月 8 日 | OpenClaw 基金会正式亮相；微软被列为「直接向上游贡献」的伙伴（而非捐赠者） |
| 2026 年 7 月至 8 月 | Scout 每月发布：模型与推理控制、OneDrive 中的会话历史、To Do、SharePoint 列表、Outlook 规则、Teams 转录、会议室预订 |
| 2026 年 9 月 25 日 | Jared Spataro 的文章「推出带有 Home、Code 和 Autopilot 的新 Copilot」。Scout 变为 Autopilot，私有预览「在月底」。同日，OpenClaw 博客：「Microsoft Autopilot 构建于 OpenClaw。贡献是双向的。」 |
| 2026 年 11 月 17 日至 20 日 | Ignite，微软称将分享更多信息 |

更名改变的不只是名字。6 月时，「Autopilot」是一个品类，Scout 是其第一个成员。9 月时，Autopilot 成了产品本身。Scout 是面向 Windows 11 和 macOS 12 或更高版本的桌面应用；Autopilot 由云端托管，「在你睡觉时也继续工作」。桌面应用在新名字下是否保留，没有文档说明。

## 它能做什么

**Autopilot（9 月，云端）。** 它住在你的租户里，拥有「自己的身份、记忆、计算机和工作区」，以微软的工作数据（Microsoft IQ）为基础。你在 Teams、Outlook、聊天、频道和文档中 @提及它，「像同事一样」。它有一个头像，以及一个由你选择的名字。Fortune 举的例子：项目进展更新、跟踪决策与截止日期、提醒同事承诺的事项、收集准备材料、联系合作伙伴。

**Scout（6 月，桌面版）**，也就是文档仍在描述的那个：

- 跨时区安排会议，标记重要会议，准备材料，为交付物预留时间，发现卡住的决策等风险
- 读写文件、运行 shell 命令、自动化浏览器，并查询 Microsoft 365：Outlook 邮件和日历、Teams 聊天、频道、会议和转录、OneDrive、SharePoint、To Do、会议室预订、收件箱规则
- **Heartbeat**：工作时间内每 15、30、60 或 120 分钟一次的周期性提示，配有独立的、更严格的权限策略。**Automations**：按计划、按条件触发或一次性运行
- 子智能体（Explore、Task、Code review、Research、General-purpose）
- 面向 Word、Excel、PowerPoint 和 Loop 的内置技能，以及你自己的 `SKILL.md` 技能
- Co-Create：你和智能体同时编辑同一个文件
- 跨对话的记忆，会话历史按设备存放在 OneDrive

## 与 OpenClaw 的关系

Scout「由 OpenClaw 驱动」；OpenClaw 基金会说 Autopilot「运行在 OpenClaw 上」。微软自己 9 月的文章和 Learn 文档则完全没提 OpenClaw。

据 OpenClaw 博客，微软向上游贡献了：

- **策略一致性**：一个 Policy 插件，把运营者的要求与实际配置比对并记录结果。微软在 Build 上承诺了它；目前正在扩展到模型提供方、网络、MCP 服务器和密钥
- **Windows**：`openclaw-windows-node` 配套组件，带引导式设置、支持行内批准的原生聊天、模型选择，以及基于 [Microsoft eXecution Container (MXC)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Microsoft+eXecution+Container+(MXC)?ref=dsebastien.net) 的沙箱后端
- **可靠性**：队列优先级、调度器和数据库恢复的修复、防止压缩后重复工具循环的保护、降低会话存储内存占用，以及区分「确定没有运行」和「结果未知」的命令
- **集成与安全**：执行批准提示中的密钥脱敏、Azure OpenAI 提供方、iMessage 批准、原生投票、消息路由检查

OpenClaw 保留 MIT 许可证和非营利基金会。OpenClaw Enterprise（9 月 29 日）——始于 OpenAI 的常驻智能体控制平面——没有提到微软或 Autopilot，也没有任何迹象显示 Autopilot 使用它。

The New Stack 在 6 月时的说法是：微软「让智能体运行时免费」，并「把周围的一切都留下」。我认为这个解读是对的。运行时是开放的；身份、策略、计费和 Microsoft 365 数据仍归微软。

## 它在新 Copilot 中的位置

新 Copilot 有三部分：**Home**（聊天加 Cowork，最终会为你把工作路由到聊天、Cowork 或 Code）、**Code**（基于 [GitHub Copilot](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GitHub+Copilot) 技术构建的自然语言应用和仪表板）和 **Autopilot**。Nadella 称其为「工作的新 OS」。Fortune 将其解读为微软在收拾「一堆杂乱的 Copilot 产品」。彭博社的标题：微软「借 Copilot 重启放弃个人 AI 聊天机器人竞赛」。

微软用 Copilot Cowork 这样划线：Cowork 端到端完成一项任务（一份 RFP 回复、一个关账包）并交回结果。Autopilot 则长期持有一个角色和一个目标。

## 安全、身份与批准

- **自己的身份。** 每个智能体都运行在各自受治理的 Microsoft Entra 身份下，而不是共享服务账户。凭据限定在任务范围内，并在日志中脱敏（[AI Agent Identity](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Identity)）
- **组织限制。** 智能体只能访问组织批准的资源。敏感操作可以要求人工签字。Purview 数据丢失防护和敏感度标签在内容发送或写入之前生效
- **审计。** Fortune 提到明确的权限和完整审计日志。Nadella：「你观察到的一切都应当可由策略治理」
- **Scout 的批准**：批准（Approve）、始终允许（Always allow）或拒绝（Deny）；shell 命令分三级（自动批准、提示、拒绝），自动批准默认关闭；发送、共享和回复需要确认
- **提示注入**：电子邮件、网页和 Teams 消息会被标记为不可信的外部内容
- 微软称 Scout 不使用客户数据训练模型

### GitHub Copilot 的注意事项

Scout 的模型调用经由 GitHub Copilot，并继承 GitHub Copilot 的模型目录（微软、第三方和开源模型，包括中国厂商）。GitHub Copilot 管理员决定哪些模型可用。

微软自己的 Responsible AI FAQ 说清了后果：提示和内容可能离开 Microsoft 365，而**数据驻留、保留、敏感度标签执行和 eDiscovery 等** Microsoft 365 保护**不适用于**这部分处理。生成的内容可能不会继承标签。这就是为什么管理员在开启前必须签署一份声明。

这与发布文章里「Purview 已强制执行」的说法有些别扭。两者可以同时成立（标签在 Microsoft 365 操作上执行，而不在模型处理路径上），但你必须读 FAQ 才知道。至于 Autopilot，这些目前都还没有文档。

## 要求与许可

Scout 的要求：

- 加入微软的 Frontier 计划，一条允许登录的 Intune 策略，以及管理员声明
- 一个 Microsoft 365 工作或学校账户和一个 Microsoft 365 Copilot 许可证
- 一个 GitHub Copilot **Business 或 Enterprise** 席位，token 用量通过 GitHub 计费
- Windows 11+ 或 macOS 12+，并有本地管理员权限

在政府云（GCC、GCC High、DoD）或主权云中不可用。Autopilot 是否保留 GitHub Copilot 要求，**未知**。

## 价格与可用性

- **usage-based billing（按用量计费）**，与 Cowork、Code 和前沿模型并列。未公布价格。聊天和 Office 应用中的 Copilot 仍按每用户许可证
- 微软点名「Astra 和 Fable」为按用量计费提供的前沿模型。Autopilot 本身使用哪个模型没有说明。Fortune 称 Copilot 主要依赖 Anthropic 和 OpenAI 的模型，也使用 xAI 的 Grok
- **私有预览**自 2026 年 9 月底开始。Fortune 称其为「用户测试中限制更多的阶段」，没有正式可用日期
- **区域**：Scout 的可用性取决于 Frontier 注册，而非国家清单。没有针对欧盟的专门说明；考虑到 GitHub Copilot 的处理路径，我不会假定 EU Data Boundary 覆盖了 Scout 的模型调用。Autopilot 尚未发布任何信息

## 反响

- **The Register**：OpenClaw 安全声誉不佳、提示注入防御不明确（微软未回应）、可靠性问题、一个「盯着你一举一动」的智能体，以及 GitHub Copilot 额外的按量计费成本
- **Gizmodo**：对 Copilot「一连串短命的改名」、那「做作」的头像和「数字队友」的说法持怀疑态度；把这次整合解读为把更多数据拉进微软生态的途径
- **GeekWire** 指出了 Nadella「病毒」言论的讽刺之处，以及 Microsoft Defender 自己的指南：OpenClaw「应被视为带有持久凭据的不可信代码执行」
- **Fortune**：微软对 Copilot 产品泛滥的修正，7 月有 3,000 万个付费 Microsoft 365 Copilot 席位
- 这个名字与 Windows Autopilot——微软的设备预配服务——撞名。搜起来祝你好运

## 局限

Scout 已记录的局限：它可能误读模糊的指令，多步任务可能失败，过时的 Microsoft 365 数据可能产生错误答案。微软表示不要在必须保证准确性的场景（法律、医疗、金融）使用它。自定义技能不受微软验证。后台模式以更严格的权限运行。连接断开会使工作中断，而在缺少管理员步骤时，登录失败不会说明原因。

## 如何比较

在托管型智能体里，Autopilot 是个异类。它是唯一构建在开源运行时之上（且贡献回上游）的；是唯一每个智能体都有自己的目录身份（OpenAI 的 specialist dots 也有自己的身份，但仍处于企业试点）的；是唯一纯粹按用量计费的；而且它住在 Microsoft 365 的各种界面（Teams、Outlook、文档）里，而不是一个独立应用。[Dots](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dots+(AI)?ref=dsebastien.net)、[Meta Muse](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Meta+Muse)、[Grok Bot](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Grok+Bot)、[Gemini Task](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gemini+Spark) 和 [Claude Duet](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Duet) 都先面向个人销售。完整对比表在 [Claude Duet](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Duet) 中。

## 我的看法

微软在底层采用 OpenClaw，是整个品类里最有趣的事。它证明自托管运行时足以支撑企业产品，而那些贡献（策略检查、Windows 沙箱、可靠性修复）帮助了每一个运行 OpenClaw 的人。对于一个据说被微软自家 CEO 比作病毒的项目，还不错。

每个智能体独立身份也是正确的做法。一个以自己的账户行动、有自己的审计轨迹的智能体，远比一个「以你的身份行动」的智能体容易治理。

但数据路径让我担忧。如果模型调用经由 GitHub Copilot 运行，处在 Microsoft 365 的驻留和保留承诺之外，那么一家欧洲公司在开启它之前有真问题要回答。微软还没有发布 Autopilot 的条款，我会等它们。

从比利时看，它是少数没有公布欧洲排除条款的托管智能体之一。实践上，这意味着雇主需要有 Microsoft 365、Frontier 计划和预览邀请。

## 注意事项

- Autopilot 的事实来自一篇微软博文（9 月 25 日）加媒体报道。Learn 文档（8 月 21 日更新）仍在描述 Scout 这个桌面应用。Autopilot 的要求、价格、模型和数据驻留条款均未发布
- 只有 OpenClaw 博客说 Autopilot 运行在 OpenClaw 上；微软 9 月的文章没有提到这一点。我视其为可靠（基金会点名了微软的工程师），但它是单方面的
- 桌面还是云端：Scout 文档描述的是本地应用，6 月的文章说「跨云端、桌面和 Web」，9 月的文章描述的是云端智能体。很可能是更名时发生了架构变更
- Purview：6 月的文章说 DLP 和标签会强制执行；Responsible AI FAQ 说 Microsoft 365 保护不适用于 GitHub Copilot 的处理
- Scout 就是 GeekWire 描述的「Project Lobster」/「ClawPilot」，这点被强烈暗示（同一团队、同一负责人），但微软从未明说
- Nadella 的「病毒」引语是二手来源；我没有找到原始出处
- 关于 Autopilot 身份通过 Agent 365 授权、每智能体价格估算、10 月开始预览，以及「30 美元席位加第二笔用量费用」的说法，都来自聚合站或未取到全文的片段。未收录
- 「Astra 和 Fable」作为 Copilot 前沿模型：很可能与 [GPT-6 Astra](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GPT-6+Astra) 和 Anthropic 的 Fable 是同一批模型，未确认
- The New Stack 6 月的文章：我只有标题和片段

## 参考资料

- 微软官方博客，Jared Spataro，「推出带有 Home、Code 和 Autopilot 的新 Copilot」（2026 年 9 月 25 日）：[https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)
- Microsoft Copilot 博客，Omar Shahine，「推出 Microsoft Scout：你常驻在线的个人智能体」（2026 年 6 月 2 日）：[https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)
- Microsoft Learn，Microsoft Scout 文档：[https://learn.microsoft.com/en-us/microsoft-scout/](https://learn.microsoft.com/en-us/microsoft-scout/)
- Microsoft Learn，Scout 概述：[https://learn.microsoft.com/en-us/microsoft-scout/overview](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- Microsoft Learn，Scout 常见问题：[https://learn.microsoft.com/en-us/microsoft-scout/faq](https://learn.microsoft.com/en-us/microsoft-scout/faq)
- Microsoft Learn，Scout 新增功能：[https://learn.microsoft.com/en-us/microsoft-scout/whats-new](https://learn.microsoft.com/en-us/microsoft-scout/whats-new)
- Microsoft Learn，Scout 入门：[https://learn.microsoft.com/en-us/microsoft-scout/get-started](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- Microsoft Learn，Scout 负责任 AI 常见问题：[https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq)
- Microsoft Learn，Scout 管理员访问：[https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)
- OpenClaw 博客，Graham McBain，「Microsoft Autopilot 构建于 OpenClaw。贡献是双向的。」（2026 年 9 月 25 日）：[https://openclaw.ai/blog/microsoft-autopilot-openclaw](https://openclaw.ai/blog/microsoft-autopilot-openclaw)
- OpenClaw 博客，「推出 OpenClaw 基金会」（2026 年 7 月 8 日）：[https://openclaw.ai/blog/introducing-openclaw-foundation](https://openclaw.ai/blog/introducing-openclaw-foundation)
- OpenClaw 博客，「OpenClaw Enterprise」（2026 年 9 月 29 日）：[https://openclaw.ai/blog/openclaw-enterprise](https://openclaw.ai/blog/openclaw-enterprise)
- Thurrott，Build 2026 Scout 报道（2026 年 6 月 2 日）：[https://www.thurrott.com/a-i/336926/build-2026-microsoft-unveils-scout-personal-work-agent-and-new-in-house-ai-models](https://www.thurrott.com/a-i/336926/build-2026-microsoft-unveils-scout-personal-work-agent-and-new-in-house-ai-models)
- The Register（2026 年 6 月 3 日）：[https://www.theregister.com/a/5250718](https://www.theregister.com/a/5250718)
- Help Net Security（2026 年 6 月 3 日）：[https://www.helpnetsecurity.com/2026/06/03/microsoft-scout-personal-agent/](https://www.helpnetsecurity.com/2026/06/03/microsoft-scout-personal-agent/)
- The New Stack，「微软刚刚让智能体运行时免费了」（2026 年 6 月 7 日）：[https://thenewstack.io/microsoft-scout-openclaw-runtime/](https://thenewstack.io/microsoft-scout-openclaw-runtime/)
- Fortune（2026 年 9 月 25 日）：[https://fortune.com/2026/09/25/microsoft-unveils-copilot-super-app-targeting-business-users-with-ai-agents/](https://fortune.com/2026/09/25/microsoft-unveils-copilot-super-app-targeting-business-users-with-ai-agents/)
- Gizmodo（2026 年 9 月 25 日）：[https://gizmodo.com/microsoft-thinks-its-finally-figured-out-copilot-this-time-2000817460](https://gizmodo.com/microsoft-thinks-its-finally-figured-out-copilot-this-time-2000817460)
- Bloomberg（2026 年 9 月 25 日，付费墙）：[https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot](https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot)
- GeekWire，Mary Jo Foley（2026 年 5 月 4 日）：[https://www.geekwire.com/2026/microsofts-openclaw-team-takes-on-the-personal-assistant-challenge/](https://www.geekwire.com/2026/microsofts-openclaw-team-takes-on-the-personal-assistant-challenge/)
