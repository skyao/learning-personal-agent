---
title: "OpenClaw 走向企业：Scout 从个人项目到企业级个人智能体"
linkTitle: "Command Line 对谈"
date: 2026-06-02
originalTitle: "Microsoft Scout: From personal project to enterprise-ready personal agent"
sourceUrl: "https://commandline.microsoft.com/project-lobster-openclaw-personal-ai-assistant-enterprise-secure/"
author: "Lisa Brown Jaloza"
publisher: "Microsoft（Command Line）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [发布, 记忆与上下文, 安全]
products: [microsoft-autopilot]
updatedAt: "2026-06-03"
---

{{< source-info >}}

**收录说明**：微软官方博客 Command Line 的文章，记录 Omar Shahine 与 Jakob Werner 关于 Project Lobster 与 Microsoft Scout 的对谈。直接下载；删去了分享按钮和文末「Next Stop」推荐阅读；页面内嵌的 YouTube 视频写为占位行，位置在引出对谈的段落之后。已翻译。

**内容摘要**：Command Line 刊出 Omar Shahine 与 Jakob Werner 的对谈（2026.06.02）：Shahine 业余用 OpenClaw 做了个人助手 Lobster，它有自己的 Apple ID 和邮箱，最初拆成三个智能体，八周后增至九个常驻智能体；向 Microsoft AI Accelerator 小组演示后，他转任 CVP，负责「Project Lobster」。Werner 的桌面端智能体在内部称为「Clawpilot」，几周内被数千名微软员工下载，后与 Shahine 的团队合流。企业化方面，文中称所有软件包经由经过签名的微软供应链引入，每次工具调用、模型请求和网络跳转都由零信任运行时中介，智能体容器被视为不受信任，并由 Agent 365 提供统一控制平面、Purview 提供合规与 DLP 信号。记忆方面，Shahine 说：「就像它需要记住一些事情，它也需要忘掉一些事情。」Werner 则设计了分层记忆，不常用的内容会随时间消退，常用的则相关性上升。

**保留理由**：这是产品团队两位核心成员的第一手对谈，交代了 Scout 的起源（Lobster 与 Clawpilot 合流）、团队工作方式，以及记忆设计和企业安全取舍的思路，是其他材料没有的内部视角。

---

Microsoft Scout：从个人项目到企业级个人智能体

Omar Shahine 与 Jakob Werner 畅谈如何构建一个常驻运行、企业级安全的个人 AI 智能体。

作者：[![](images/img-01-0c9134.webp)Command Line 团队](https://commandline.microsoft.com/author/command-line-team)![](images/img-01-0c9134.webp)Command Line 编辑团队

2026.06.02

今年早些时候，[OpenClaw](https://openclaw.ai/) 的演示似乎随处可见，不过其中许多充其量只是一场很酷的派对把戏（「看，我的智能体订了一份披萨」）。但这让在 Microsoft 工作多年的 Omar Shahine 开始思考：claw 实际上能有多有用？

答案是：非常有用。Shahine 利用业余时间创建了 [Lobster](https://www.omarknows.ai/p/meet-lobster-my-personal-ai-assistant)，这是一个基于 OpenClaw 构建的个人 AI 助手。它有自己的 Apple ID 和电子邮件地址，因此他可以从任何有 iMessage 的设备上给它发消息。他最初把 Lobster 拆成三个智能体，每个都有自己的安全配置文件和工具访问权限（八周后，这个数字增加到九个常驻智能体）。Lobster 处理旅行事务，提前主动发送家庭提醒，并且总体上帮助 Shahine 和他的家人保持井井有条、把事情做完。在向 Microsoft 的 AI Accelerator 小组展示 Lobster 之后，这为 Shahine 赢得了一份[新工作](https://www.omarknows.ai/p/lobster-got-hired)：作为被命名为「Project Lobster」的项目的 CVP，把 OpenClaw 带到 [M365](https://www.office.com/) 和云端。

与此同时，Microsoft 技术员工（Member of Technical Staff）Jakob Werner 正在推进一个类似但有所不同的想法：一个受 OpenClaw 启发、基于桌面应用的智能体。目标是交付一个强大的、企业级安全的个人 AI 助手，让 Microsoft 内部的任何人都能使用。仅仅几周内，内部称为「Clawpilot」的产品就已被数千名 Microsoft 员工下载，这个社区还在继续壮大。

当 Shahine 开始组建一支由热情建设者组成的小团队时——自然就是「Ocean's 11」——Werner 很快加入了他们的行列。两人最近在华盛顿州雷德蒙德（Redmond, Washington）相聚，交流构建这些常驻运行的自主智能体的心得，以及如何应对企业安全、智能体记忆等领域。

[视频：Microsoft Scout：从个人项目到企业级个人智能体](https://www.youtube.com/watch?v=nyhXB9Y7uLM)

## 拥抱开源精神

Project Lobster 团队代表了 Microsoft 内部一种由 AI 进步推动的新型工作方式。这是一个紧密的小团队，偏好异步协作。团队普遍反对开会。每个人都向代码库贡献代码，包括 Shahine。团队中没有传统的行政助理：每位成员整天都在积极使用原型，以便在构建技术的同时完全沉浸其中。团队周围甚至还有一个不断壮大的开源社区，其情形与 Microsoft 墙外开源项目中所见相似。

「我在公司内部从未见过一个项目，有这么多人带着自己的想法和代码出现，并实际投入工作提交 PR，」Shahine 说。

> >
> 「我在公司内部从未见过一个项目，有这么多人带着自己的想法出现。」

事实上，Project Lobster 在内部引发的热情如此之高，以至于团队在早期构建阶段收到了大量拉取请求（PR），他们逐一审查，以确定这些 PR 是否达到进入产品的标准。甚至 Shahine 的一些改动也未能入选。焦点必须始终放在产品的核心目标上：创造一个用于工作的常驻个人智能体。一个能学习你的目标、适应你的日常工作模式、结合上下文行动的 AI 助手，它能在问题浮现之前识别问题，让项目保持正轨，并在无需持续输入的情况下推动结果。一个能察觉日历排得过满并在本周开始前提出具体调整建议的智能体，或者能识别某项决策陷入停滞并起草有针对性的跟进、为其解除阻塞的智能体。

「我们必须判断某个 PR 是否会改变产品的核心想法——而这种审查的速度是人的速度，不是 AI 的速度，」Werner 指出。「现在任何人都能极快地提交 PR。我们正在努力帮助社区，并教会贡献者如何审查 PR。」

这项工作最初只是一个内部实验，但很快变成了以客户为中心的努力，并最终促成了 [Microsoft Scout](https://aka.ms/ProjectLobster-Blog) 的推出——一个由 OpenClaw 开源技术驱动的常驻个人智能体。

## 从实验到企业级产品

Microsoft Scout 自主运行——拥有自己的身份——代表你行动。它跨云、桌面和 Web 浏览器工作，因此可以连接你使用的各个界面——Teams、Outlook、OneDrive 和 SharePoint——以及工作所在的系统，包括电子邮件、日历和联系人。

与野外常见的普通 claw 不同，Microsoft Scout 将 OpenClaw 代码与企业身份、治理和安全相结合。每个软件包都通过经过策管、签名的 Microsoft 供应链引入，每次工具调用、模型请求和网络跳转都由零信任运行时中介——智能体的容器被视为不受信任，由 Microsoft 控制身份、令牌和策略，并将其置于容器之外。借助 Agent 365，管理员获得单一控制平面，Microsoft Purview 则为安全团队提供他们已从其他 M365 界面获得的相同合规与 DLP 信号。

「这是一个极其强大的工具，」Werner 承认。「要做到企业级安全，我们需要确保数据治理正确、隐私正确，并且它不会取消一场会议，然后把你的所有个人信息发送到那串邮件里。如果我把我的智能体派给你，它不应该告诉你关于我的一切。这些方面是可以控制的，但我们也必须以平衡的方式来做，不能把可能性限制到一无所有。」

这是值得做出的取舍。借助 Microsoft 久经考验的企业安全产品，以及该领域持续的研究和创新，团队拥有了应对这一挑战的坚实基础。

## 智能体记忆的作用

一个常驻的个人 AI 智能体要真正有用，就需要主动——而这需要由 Work IQ 提供支持的上下文。随着时间推移，Microsoft Scout 会理解你的工作方式，使用与你相同的生产力工具，并在无需持续提示的情况下替你分担事务。它学习你的目标，适应你的日常工作模式，并有意图地行动。与以往的技术浪潮不同，这是真正个性化的软件。这具有变革性，但并非没有取舍。

「OpenClaw、Claude Code、GitHub Copilot CLI，这些都是智能体编码框架，它们基本上就是在记忆——像人一样把事情写下来，」Shahine 指出。「它们像写日记一样把事情写下来。但就像它需要记住一些事情，它也需要忘掉一些事情。」

> >
> 「就像它需要记住一些事情，它也需要忘掉一些事情。」

举例来说，Shahine 回溯了 ChatGPT 引入记忆功能的时候。他花了一些时间告诉 ChatGPT 他的女儿 17 岁，而儿子 13 岁。但一年后，这些信息仍然静止不变。系统没有「某些事实需要随时间变化，而其他信息——比如你的名字——会保持完全不变」的概念。

「在设计阶段，我在思考人以及人如何记忆事物，」Werner 说。「我会忘记无关的事情，因为我没有用到它们。所以我构建了一个系统：如果我要反复使用某样东西，它就会留下来。但如果我不经常使用，我希望系统忘掉它。我不想要一本无限的日记，对吧？所以记忆有某种层次，如果不使用，它会随时间消失。与此同时，其他记忆的相关性会随着你使用得越多而增长。」

## 形成新的引力中心

两人最初联手时，Werner 向 Shahine 介绍了引力的概念——这是他运作所依据的框架。

「要打造真正出色的产品，我认为我无法独自完成，」Werner 解释道。「我们需要与他人协作。但如何影响他人与我们协作？我使用并试图灌输给团队的心态就是引力。我们构建某样东西，并让它产生巨大的影响力——不是功能数量上的，而是影响力上的——这样当令人兴奋的新想法出现时，人们会想要尝试加入我们工作的引力，而不是分散注意力。」

「在新职位宣布之前，我其实不太明白你在说什么，」Shahine 承认。「但从那以后，我收到了成百上千条消息，来自想要帮忙的人、想要学习的人、想要向我展示他们成果的人，还有想知道我们正在构建的东西何时能拿到手的客户。这可以用很多别的词来形容——用户拉动、信号——但你的引力箴言现在真的引起了我的共鸣。」

---

Microsoft 员工已经在使用早期的 Microsoft Scout 桌面体验。我们构建它，是为了了解常驻智能体在真实工作中如何呈现，我们看到它承担起协调工作、更早暴露风险，并在无需持续提示的情况下让工作持续推进。

我们现在正把这一早期体验扩展到 Frontier 组织。Microsoft Scout 通过 [Frontier](https://www.microsoft.com/en-us/microsoft-365-copilot/frontier-program) 以实验性版本提供，让客户有机会探索它如何融入自己的工作流。

访问需要 Frontier 注册、Intune 策略配置和选择加入的声明。拥有 GitHub Copilot 许可证的用户随后可以下载并安装该体验。[了解更多](https://aka.ms/ProjectLobster-Blog)。
