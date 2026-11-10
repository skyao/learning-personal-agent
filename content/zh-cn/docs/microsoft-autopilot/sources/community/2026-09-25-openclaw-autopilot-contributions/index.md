---
title: "Microsoft Autopilot 基于 OpenClaw，贡献是双向的"
linkTitle: "OpenClaw：上游贡献"
date: 2026-09-25
originalTitle: "Microsoft Autopilot is built on OpenClaw. The contributions go both ways."
sourceUrl: "https://openclaw.ai/blog/microsoft-autopilot-openclaw/"
author: "Graham McBain"
publisher: "OpenClaw Blog"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-10
tags: [安全, 运行环境]
products: [microsoft-autopilot]
---

{{< source-info >}}

**收录说明**：开源项目 OpenClaw 的官方博客（发布方不是微软），在 Autopilot 改名当天发布，列举微软向 OpenClaw 上游的贡献。直接下载；删去了「All posts」返回链接与作者头像，题图收入 images/，文中嵌入的 X 帖子按页面文字照录。已翻译。

**内容摘要**：OpenClaw 项目博客在 2026 年 9 月 25 日称，Autopilot 是此前 Microsoft Scout 的新名称，其基础是 OpenClaw；Omar Shahine 的原话是：「我们在 @openclaw 上构建 Autopilot，并与 @steipete 和 OpenClaw Foundation 合作，使它成为出色的企业级运行时。」文章列出微软人员的上游贡献：Gio Della-Libera 的 Policy 插件让运营者描述要求、与实际配置比对并生成记录，后续扩展到模型提供方、网络、MCP 服务器和密钥配置，Shahine 另贡献了消息路由检查。Windows 方面包括原生 Windows 伴侣的引导式设置、WinUI 聊天、内联命令批准，以及 Paul Campbell 提供的 MXC 沙箱后端；可靠性方面包括让排队的用户请求优先于后台任务、修复可能挂起 Gateway 的调度器、区分「确定未运行」与「结果未知」的命令；安全方面包括在执行批准提示中对密钥脱敏。文中还说，并非每个微软人员的贡献都必然是 Autopilot 功能或公司赞助项目。

**保留理由**：这篇给出了 Scout/Autopilot 回馈 OpenClaw 上游的具体贡献清单和贡献者，是政策合规、Windows 支持和可靠性修复的公开记录，其他材料只有笼统的承诺。

---

Microsoft Autopilot 基于 OpenClaw 构建。贡献是双向的。

从政策合规和原生 Windows 支持，到更可靠的日常交互，Microsoft 的贡献者正在帮助为所有人构建 OpenClaw。

![一个友好的回形针角色，长着龙虾钳，在笔记本电脑旁主动提出帮你处理工作。](images/img-01-036b49.png)

Microsoft 今天推出了 Autopilot，作为其新 Copilot 体验的一部分：一个常驻、主动的个人智能体，即使你不在也会持续工作。它的基础是 OpenClaw。

领导构建该产品的 Omar Shahine [直言不讳](https://x.com/OmarShahine/status/2103480227561079264)：

> 「我们在 @openclaw 上构建 Autopilot，与 @steipete 和 OpenClaw Foundation 合作，使它成为出色的企业级运行时。」

> 今天我们宣布 Microsoft Autopilot 预览版正在向首批客户推出——「Autopilot 是一个常驻、主动的个人智能体，即使你不在也会持续工作」\
>
> 已经有一段时间没向大家更新我们在构建什么了。首先，Scout 现在…… [pic.twitter.com/ZdGHQDn7Ll](https://t.co/ZdGHQDn7Ll)
>
> —— Omar Shahine (@OmarShahine) [2026 年 9 月 25 日](https://x.com/OmarShahine/status/2103480227561079264?ref_src=twsrc%5Etfw)

Autopilot 是今年早些时候宣布的 Microsoft Scout 的新名称。Microsoft 的[发布文章](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)称，Autopilot 将在本月底扩展到私有预览。

对 OpenClaw 社区来说，故事还有另一部分值得强调：回馈上游的改进。

Microsoft 的承诺在其公开公告和整个项目贡献者的工作中都清晰可见。这些工作涵盖检查智能体的安全配置、构建原生 Windows 体验，以及让日常智能体交互更可靠。

## 让智能体的配置可检查

采用个人智能体的组织需要回答一些实际问题。启用了哪些通信渠道？它能使用哪些模型提供方？它能访问什么？它的配置是否仍符合组织预期的规则？

在其[最初的 Scout 公告](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)中，Microsoft 做出了明确承诺：

> 「我们正在直接向 OpenClaw 上游贡献政策合规功能。」

Gio Della-Libera 的上游工作让这一承诺有了具体形式。OpenClaw 的 [Policy 插件](https://github.com/openclaw/openclaw/pull/80407)让运营者描述要求、将其与实际配置比对，并生成结果记录。后续贡献将这些检查扩展到[模型提供方、网络和 MCP 服务器](https://github.com/openclaw/openclaw/pull/80783)、[密钥与身份验证配置](https://github.com/openclaw/openclaw/pull/81974)，以及智能体环境的其他部分。

Omar 还贡献了[消息路由检查](https://github.com/openclaw/openclaw/pull/111087)，让运营者可以测试有代表性的传入对话是否会到达预期的智能体。

这些检查让运营者能够验证智能体的配置，并在其不再符合要求时发现。

## 在 Windows 上的一流家园

基金会与 Microsoft 的 Windows 团队还描述了一项[长期合作](https://openclaw.ai/blog/introducing-openclaw-foundation)，旨在让 Windows 成为 OpenClaw 的首要平台。

你可以在[原生 Windows 伴侣](https://github.com/openclaw/openclaw-windows-node)中看到这种合作。

Scott Hanselman 的贡献包括[引导式设置体验](https://github.com/openclaw/openclaw-windows-node/pull/201)，以及持续的可靠性和发布工作。Régis Brid 贡献了[原生 WinUI 聊天](https://github.com/openclaw/openclaw-windows-node/pull/315)和[内联命令批准](https://github.com/openclaw/openclaw-windows-node/pull/751)。Barbara Kudiess 在原生界面、[模型选择](https://github.com/openclaw/openclaw-windows-node/pull/877)、批准和沙箱集成方面做了工作。Caleb Eden 的贡献帮助原生聊天正确[显示用户和智能体的媒体内容](https://github.com/openclaw/openclaw-windows-node/pull/1119)。

界面之下也有重要工作。Paul Campbell 为受支持的 Windows 环境贡献了 [MXC 沙箱后端](https://github.com/openclaw/openclaw/pull/97086)。它与伴侣应用自身的沙箱集成一起，为运营者提供了另一种使用 Microsoft 执行容器技术约束智能体命令执行的方式。

这些实际改进带来了更简单的设置、更清晰的交互，以及对智能体能做什么的更多控制。

## 为持续工作的智能体提供可靠性

一个常驻智能体必须处理的远不止一次成功的演示。它必须在后台任务、重启、长对话和故障中保持有用。

Galin Iliev 的贡献包括[让排队的用户请求优先于后台工作](https://github.com/openclaw/openclaw/pull/82765)、修复[可能挂起 Gateway 的调度器行为](https://github.com/openclaw/openclaw/pull/142741)，以及改进[数据库恢复期间的响应性](https://github.com/openclaw/openclaw/pull/151581)。他最近的[流式补全修复](https://github.com/openclaw/openclaw/pull/156144)防止同一 Codex 回复在其流式标识符与补全标识符不同时在对话历史中出现两次。

Eduardo Piva 贡献了[防止上下文压缩后重复工具循环](https://github.com/openclaw/openclaw/pull/77555)的保护措施，以及[减少会话存储内存保留](https://github.com/openclaw/openclaw/pull/84693)的工作。

Omar 的贡献包括另一个微妙但重要的区分：[确定从未运行过的命令不同于结果未知的命令](https://github.com/openclaw/openclaw/pull/117276)。当智能体无法判断某个操作是否执行时，盲目重复可能使问题更糟。这项上游更改保留了这种不确定性，并告知智能体不要自动重新运行它。

正是这些细节，帮助智能体从令人印象深刻的东西变成人们可以依赖的东西。

## 更好的集成，更安全的日常交互

即使是最小的贡献，也能在日常使用中带来明显改进。

Gio 的 [Microsoft Teams 表情回应修复](https://github.com/openclaw/openclaw/pull/151382)让智能体可以对自己当前正在回复的消息做出回应，而无需复制内部消息 ID。该更改保留了当前对话与另一对话之间的边界。

Pengfei Ni 贡献了[执行批准提示中的密钥脱敏](https://github.com/openclaw/openclaw/pull/64790)，帮助避免可识别的 API 密钥、令牌和密码出现在聊天中显示的命令文本里。请求许可不应不必要地暴露凭据。

Kunal Karmakar 改进了 [Azure OpenAI 提供方支持](https://github.com/openclaw/openclaw/pull/50851)，将 Azure 端点接入相应的 Responses 实现，使已配置的智能体和工具能正确使用它们。

连同 Eduardo 的记忆保留工作和 Galin 的重复回复修复，这些边际改进在用户体验上产生了巨大影响。

## 超越单一产品的改进

这个贡献故事中最具人情味的部分之一，是 Omar 在消息传递方面的工作。他的上游更改包括 [iMessage 批准](https://github.com/openclaw/openclaw/pull/85952)、[原生投票](https://github.com/openclaw/openclaw/pull/98421)，以及[让回复留在正确的对话中](https://github.com/openclaw/openclaw/pull/133499)。

这项工作也让 Apple 设备上的 OpenClaw 用户受益。它提醒我们，一个共享项目可以跨平台改进，即使各公司在其上构建不同的产品。

并非 Microsoft 的每个人的每项贡献都必然是 Autopilot 功能或公司赞助的项目。公开记录显示的是大量回馈给 OpenClaw 的工作，以及 Microsoft 对上游协作的明确承诺。

Peter Steinberger 在 6 月宣布这项合作时表示欢迎：

> 能与 Microsoft 合作把 claw 带入企业，真是莫大的荣幸！<https://t.co/1psejBcL7S>
>
> —— Peter Steinberger 🦞 (@steipete) [2026 年 6 月 2 日](https://x.com/steipete/status/2061874084649025728?ref_src=twsrc%5Etfw)

感谢 Omar、Gio、Scott、Barbara、Paul、Galin、Eduardo、Pengfei、Kunal、Régis、Caleb，以及其他共同构建这一切的贡献者和维护者。

OpenClaw 仍然是用于构建和定制强大智能体的开放基础设施，既可用于个人用途，也可用于组织用途。Microsoft 的 Autopilot 是一个有前景的可能性示例，我们感谢那些通过上游工作让这个平台对所有人更有用的贡献者。
