---
title: "Redmondmag：微软开始推出 Autopilot"
linkTitle: "Redmondmag 11-20"
date: 2026-11-20
originalTitle: "Microsoft Begins Rolling Out Autopilot, Its Always-On Personal AI Agent"
sourceUrl: "https://redmondmag.com/articles/2026/11/20/microsoft-begins-rolling-out-autopilot.aspx"
altUrls: []
author: "Chris Paoli"
publisher: "Redmondmag"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [发布, 安全, 开放与价格, 运行环境]
products: [microsoft-autopilot]
---

{{< source-info >}}

**收录说明**：直接下载；自动抽取取不到正文，改按 `#article` 容器抽取，从「Key Takeaways」起，删去了作者简介与站内推荐。已翻译。

**内容摘要**：文章报道 Microsoft 在 Ignite 2026 上开始向 Frontier 客户推出 Autopilot，并说明它与 Copilot Cowork 的区别：Cowork 完成单个多步任务，Autopilot 管理没有明确终点的持续职责。Principal product manager Adam Sheppard 在 Microsoft Mechanics 演示中说 Autopilot 在云端运行，关机后仍继续工作。设置时 Autopilot 会审阅过去 30 天可访问的沟通与文件，此过程不修改文件或发消息；它通过 Agent 365 获得身份，用 Work IQ 提供组织上下文，并可用 IT 批准的插件扩展能力。Microsoft 365 管理中心新增 Autopilot 专区，管理员可管理访问、选择会话仅限云端或可在受管设备本地运行、配置自动批准，并查看采用率、花费、会话与模型工具使用。Autopilot 需要 Microsoft Copilot、Agent 365 和 usage-based billing policy，按 Copilot Credits 计费，最终定价与打包将在 GA 前公布。

**保留理由**：包含 Adam Sheppard 演示的一手细节（运费延误处理、浏览器中填报费用并请求审批）和管理中心新设置（云端或本地会话、自动批准、报表）的媒体转述。同时给出 Autopilot 与 Cowork 的区别，以及 30 天回看与最终定价待定的说法。

---

### 要点

- Microsoft Autopilot 开始向 Frontier 客户推出，引入始终在线的个人 AI 智能体。
- 与 Copilot Cowork 不同，Autopilot 使用专用的云资源自主管理持续进行的工作职责。
- Microsoft 365 管理员可以管理 Autopilot 的访问权限、安全策略、基于用量的计费和支出。

在本周的 Ignite 2026 上，微软开始推出 Autopilot——一款旨在独立处理员工工作环境中持续职责的个人 AI 智能体。Autopilot 于今年早些时候首次推出，现在正向参与 Microsoft Frontier 计划的客户开放。

与传统的 Copilot 交互不同——用户输入提示词然后等待回应——Autopilot 围绕更长期的目标来设计。用户可以给它分配跨越数天甚至数周的职责，而无需不断查看或提供额外指令。

「你的 Autopilot 在云端运行，所以即使你关掉笔记本电脑，它也会继续工作」，Autopilot 首席产品经理 Adam Sheppard 在[周五发布的 Microsoft Mechanics 演示](https://techcommunity.microsoft.com/blog/microsoftmechanicsblog/introducing-autopilot-your-personal-and-proactive-agent/4575030)中说。

举个 Autopilot 能做什么的例子：一位负责产品发布的员工可以让 Autopilot 监控沟通、跟踪供应商承诺并标记潜在延误。该智能体还可以发送每日进度报告，并识别在即将到来的截止日期前需要做出的决定。

这正是 Autopilot 与微软的 Copilot Cowork 不同之处。Cowork 旨在完成单个多步任务，而 Autopilot 可以管理未必有明确终点的持续职责。

上手不需要写任何代码。员工在 Copilot 应用内创建并命名自己的智能体，然后描述希望它们完成什么。

在设置期间，Autopilot 会审阅过去 30 天可访问的工作沟通与文件，以更好地理解员工的职责、优先级和工作关系。这个初始过程不会修改文件或发送消息。

每个 Autopilot 都通过 Microsoft Agent 365 获得自己的身份，并拥有专用的云计算资源。Microsoft Work IQ 提供组织上下文，而经 IT 批准的插件可以把智能体的能力扩展到微软自家应用之外。

而且员工与智能体互动并不局限于 Copilot。他们可以把智能体带入 Teams 对话，同事也可以在那里与智能体互动。

在周五的演示中，Sheppard 展示了一个 Autopilot 如何通过准备一份说明问题的文档并安排与相关员工的会议，来帮助解决一次潜在的运输延误。

Autopilot 还可以直接与基于浏览器的业务应用交互。在另一个演示中，该智能体从员工的收件箱收集收据，填写费用报告，并在提交前请求批准。

当然，给员工配备自己的自主 AI 智能体，也给 IT 部门带来了一套新的责任。

微软表示，Autopilot 在既有的租户安全边界和组织访问策略内运行。

「它只做你要求它做的事」，Sheppard 说。

微软在 Microsoft 365 管理中心新增了专门的 Autopilot 区块，管理员可以在那里管理员工访问权限，并审阅希望创建自己智能体的用户所提交的请求。

IT 团队还可以决定智能体会话是仅限于云端，还是允许在受管设备上本地运行。其他设置则决定某些智能体操作是否可以自动批准。

报表工具让管理员可以看到采用率、支出、会话活动，以及员工智能体正在使用哪些 AI 模型和工具。

当组织开始部署数百甚至数千个全天候运行的智能体时，这种支出的可见性可能尤为重要。与偶尔向 Copilot 求助的员工不同，这些智能体可能在无人主动交互的情况下定期消耗资源。

[Autopilot](https://www.microsoft.com/en-us/copilot/features/autopilot) 需要 Microsoft Copilot、Agent 365 以及基于用量的计费策略。组织通过 Copilot Credits 为消耗付费，管理员可以设定预算来帮助控制成本。

微软尚未公布最终定价与打包方案，该公司表示会在正式发布（general availability）前分享。
