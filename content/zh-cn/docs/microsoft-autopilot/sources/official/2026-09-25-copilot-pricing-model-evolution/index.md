---
title: "Copilot 定价模式的演进：按用户订阅加用量计费"
linkTitle: "Copilot 定价演进"
date: 2026-09-25
originalTitle: "Evolution of the Copilot pricing model"
sourceUrl: "https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/evolution-of-the-copilot-pricing-model/4559416"
altUrls: ["https://aka.ms/Sept25/EvolvingModel"]
author: "Nicole Herskowitz"
publisher: "Microsoft Tech Community（Microsoft Copilot Blog）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-14
tags: [开放与价格, 商业与规模]
products: [microsoft-autopilot]
updatedAt: "2026-09-28"
dateNote: "JSON-LD datePublished 为 9/25/2026，dateModified 为 9/28/2026；页面标 Version 7.0"
---

{{< source-info >}}

**收录说明**：微软 2026-09-25 官方博客中「定价细节」所链接的 aka.ms/Sept25/EvolvingModel 跳转到这篇 Tech Community 博文，直接下载。删去了作者卡片、标签、关注提示等页面元素。已翻译。

**内容摘要**：博文称 Copilot 定价将把可预测的按用户定价与用量计费（UBB）结合。「日常 AI」由 Copilot 用户订阅许可（USL）覆盖，按用户每月计价，Auto 按准确度、速度和成本路由，GPT-5.6 和 Sonnet 5 包含在内，Opus 5 等新模型带限额纳入；达到上限时可改用 Auto 或转用 credits。「高级 AI」指交给 AI 代办的工作，文中列举 Cowork、Code、Autopilot 以及 Fable、Astra 等前沿模型，这些以 Copilot Credits 按 UBB 计费，且须先有 USL。企业客户的 UBB 服务在管理员于 Microsoft 365 管理中心创建支出策略前保持关闭、不产生计费；文中还列出 FinOps 新能力（成本管理覆盖 Code 与 Managed Runtime、按组管理模型、Cowork 消耗洞察、Graph API 管理策略、终端用户查看 credits）。文末称部分能力会先在 UBB 上线，之后随成本下降移入 USL。

**保留理由**：09-25 官方博客对计费只有一句话，这篇给出 USL 与 UBB 的划分（Autopilot 归入 UBB、须有 USL）、支出策略默认关闭以及预算与 FinOps 控制的细节，是 Autopilot 计费口径的官方出处。

---

你需要知道 AI 要花多少钱，这样才能做规划和管理。这是合理的要求。随着 AI 越来越具备 agent 能力，我们承诺为日常 AI（everyday AI）提供可预测的价值，同时也让那些价值更高、运行成本也更高的最先进 AI 体验成为可能。因此，Copilot 的定价正在演进，把可预测的按用户定价与用量计费（usage-based pricing）结合起来。

## 日常 AI（Everyday AI）

日常 AI 是你提供给全体员工的部分。它由 Copilot 用户订阅许可（user subscription license，USL）覆盖，按用户每月计价（也就是多年来你购买软件的方式），你已有的价值不会有任何变化。

我们有意这样定价。有些厂商把日常 AI 工作放在计量表上。我们认为这样不划算，因为当每项任务都有计量表时，公司可能会限制使用，只有一部分人能用上 AI。我们认为每个人都应该能用。

*Microsoft 内部分析，2026 年 9 月。成本对比针对两类用户画像、共 40 条提示词建模，每条提示词测试 10 次：日常 AI 用户（15 条提示词：9 条 Chat，6 条分布在 Word、Excel 和 PowerPoint）和高级 AI 用户（25 条提示词：5 条 Cowork，加上 20 条日常工作提示词：11 条 Chat，9 条分布在 Word、Excel 和 PowerPoint，其中基于应用的任务比例更高，以反映高级用户在 Microsoft 365 应用中更广泛地使用 AI）。Copilot 的 Chat 和 Microsoft 365 应用使用 Auto；Copilot Cowork 使用 Opus 5 和 GPT-5.6 Sol，推理强度为 high。Claude 的 Chat 使用 Opus 5，推理强度为 medium，Microsoft 365 加载项使用 extended thinking，Claude Cowork 使用 Opus 5，推理强度为 high。ChatGPT 的 Chat 和 Microsoft 365 加载项使用 GPT-5.6 Sol，推理强度为 medium，ChatGPT Work 使用 GPT-5.6 Sol，推理强度为 high。Copilot 的成本按订阅标价计算，其中 Copilot Cowork 的成本按基于模型、上下文、工具和运行时长的可变费率计算。Claude 和 ChatGPT 的成本按分析时公开可得的标价和 API 费率建模。成本不含折扣、促销、协商价格和其他特殊定价。实际结果可能因客户的使用情况、配置、定价和其他因素而不同。*

固定价格适合日常 AI，原因在于我们所说的饱和（saturation）：到了某个点之后，更强的模型不再改变结果，因为这项任务本来就不需要它。把会议记录整理成要点、总结同事发来的文档，这类任务都是饱和的。

Copilot 模型选择器中的 Auto 就是围绕这个想法构建的。使用 Auto 时，它会在每次请求中权衡准确度、速度和成本，路由到最适合这项工作的模型和推理强度。你不用考虑选哪个模型，就能**以固定价格获得最佳质量**。如果你更想自己选，也可以，因为模型选择是 USL 的一部分。GPT-5.6 和 Sonnet 5 已包含在内，Opus 5 这样的新模型将带限额地包含在内。

USL 一直带有合理使用（fair use）条款，这一点不会改变。我们设置用量上限，是为了让绝大多数人永远不会触及上限。对于用量最大的用户，触及上限并不等于撞墙。你会先收到明确的提醒，然后有一个选择：把模型选择切换为 Auto（无需额外付费），或者改用 credits。

USL 是 Copilot 的基础，我们仍然承诺不断为它增加更多日常价值。

## 高级 AI（Advanced AI）

高级 AI 是你交出去让 AI 代办的工作：运行数小时的 agent、无人监督的工作流、由 agent 承担大部分工作的重构后的业务流程。比如一个整个下午都在运行的多步骤财务模型。Cowork、Code、Autopilot，SharePoint 等应用中新的高级体验，以及 Fable 和 Astra 这样的前沿模型。当你需要尽可能好的质量，或某项任务的最佳模型时，这类工作按用量计费（usage-based billing，UBB）运行，使用 Copilot Credits。UBB 建立在 USL 之上，访问这些能力需要有 USL。

USL 和 UBB 都运行在来自多家实验室的模型上。目前指的是 OpenAI 和 Anthropic，更多实验室和开放权重模型即将加入。好处不止于多一个选择。不同实验室的模型各有所长，彼此互补。

可以把我们的商业模式想成插电式混合动力。USL 是电池：以固定的月费覆盖你大部分的行驶。UBB 是油箱：当某项任务需要的续航超出电池所能提供的范围时，它就在那里。选择权在你，逐项任务来定。

## FinOps

一切由你掌控。UBB 能力在产品中可见，因为我们希望每个人都能看到 Copilot 能做什么。对于企业客户，UBB 服务保持关闭，直到管理员在 Microsoft 365 管理中心创建支出策略（spending policy）；在此之前不会产生任何计费。

决策就在支出策略里做出。管理员在租户和组级别设置预算，包括组策略内的用户级上限，并在支出达到阈值时设置提醒。当有人接近上限时会发生什么由你决定：给出警告、提供申请更多额度的途径，或者如果你希望用户完全看不到，也可以不弹任何提示。

支出与你的组织的对应方式，和预算中的其他部分一样。如果你通过 Azure 订阅或资源组管理部门成本，就可以把用量分配到对应的订阅或资源组，让 AI 出现在该团队其他支出所在的同一个地方。报告也遵循同样的逻辑，按用户、组、工作负载、策略和付款方式拆分。

我们在倾听客户的意见，并快速改进 FinOps。今天，我们推出更多能力，让 AI 支出更容易理解、管理和优化：

- **更多工作负载纳入成本管理：** 成本管理现在在 Cowork 和 Work IQ API 之外，还覆盖 Code 和 Managed Runtime，Copilot Studio 的 agent 将在 10 月加入。之后还会有更多 AI 工作负载。
- **管理模型选择：** 为不同的组定制可访问的模型系列，让管理员能把合适的模型匹配给合适的用户或场景，使产生的价值最大化。正在 Cowork 中推出，并计划扩展到更多工作负载。
- **Cowork 的消耗洞察：** 查看哪些场景在驱动 credit 消耗以及产出了什么，以便你决定在哪里维持、扩大或优化。
- **通过 API 以编程方式管理策略：** 使用 Microsoft Graph API，在你自己选用的商业智能和 FinOps 工具中大规模管理支出策略。这有助于组织在已有的系统和流程中实现自动化。
- **面向终端用户的支出可见性：** 你的员工可以直接在 Microsoft Copilot 中查看 credit 用量、剩余 credits 和用量历史，自行管理自己的使用。

更多信息，请[见此处](https://aka.ms/finopsforai/optimization)。

## 接下来

模型在不断变得更好、更高效，因此一些能力会先从 UBB 开始，随着经济性允许再移入 USL。有时它们起初会带着用量限额出现，这能让人们比原本更早用上它们。

大多数客户已经在把 Copilot 用于日常工作。当你把更复杂的工作交出去时，请把总成本与其他替代方案做比较，就像你对待任何其他为完成工作而做的投入那样。

要了解新的 Copilot，请[见此处](https://aka.ms/AA13g7uq)。
