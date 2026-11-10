---
title: "Meta Muse 开源吗？开放了什么，没开放什么"
linkTitle: "Meta Muse 开源吗"
date: 2026-11-05
originalTitle: "Is Meta Muse open source? What is open, and what is not"
sourceUrl: "https://personalagentbench.com/is-meta-muse-open-source/"
altUrls: ["https://personalagentbench.com/zh-cn/is-meta-muse-open-source/"]
author: "未署名"
publisher: "Personal Agent Bench"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-07
dateNote: "页面只标注 article:modified_time 2026-11-05，未见发布日期；文中以 11 月 5 日为截至日期"
tags: [开放与价格, 模型, 运行环境]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载后用 extract.py 抽取；删去页首多语言链接、目录与文末「More on Muse」站内推荐及分享按钮；站内相对链接已改为绝对地址。未署名，发布方为 Personal Agent Bench（JSON-LD 发布机构为 Zentor）；文中关于 Mac 应用「自 9 月 17 日起」的说法未附发布公告或版本号，照录。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：结论是 Muse 产品本身不开源：Muse agent、用户访问它的应用及 Meta 云端为每位用户配置的 Linux 虚拟机全部封闭，模型的情况则混杂。Muse Spark Open 于 10 月 15 日发布，是 Muse Spark 的开放权重版本，共 8160 亿参数（420 亿激活参数），采用 Meta 自有的 Muse Model License（非开源许可），要求标注「Built with Muse Spark Open」，年收入合计超过 2000 万美元的模型即服务商须先通知 Meta 并另签协议；Meta 未说明它是 Muse agent 实际使用的模型。Muse Wonder 于 10 月 12 日发布，仅通过 API 托管，模型卡未提及发布权重，截至 11 月 5 日 Meta 未发布任何 Wonder 权重；Hugging Face 上自称 meta-01 的账号创建的 muse-wonder 仓库截至 11 月 5 日仍无模型文件，且该账号并非 Meta 官方发布账号 meta-models。Muse Glimmer 30B 于 8 月 9 日以 Apache 2.0 许可发布开放权重，由 Muse Spark 蒸馏而来，可在消费级硬件上运行，但并非 Meta 所称 Muse 运行的模型；Muse Gadgets SDK 于 10 月 2 日以 Apache 2.0 开源，但每个小设备配对都需要 Meta 发放的 token；文末另介绍 OpenMuse（MIT 许可）与 nanoMuse（GPL-3.0-or-later）两个与 Meta 无关的开源替代项目。

**保留理由**：本篇对 Muse 各层（agent／应用／云端 VM、Spark／Spark Open、Wonder、Glimmer、Gadgets）的开源状态做了逐层核查与区分，并附自家 teardown 实测（触及请求结构与 246 个方法的权限表）及 Hugging Face 假冒账号核查，提供了「能否自行运行 Muse」这一问题的系统性判定依据。

---

## Meta Muse 开源吗？开放了什么，没开放什么

Meta Muse 开源吗？产品不开源。Muse agent、你用来访问它的应用，以及它在 Meta 云上运行的那台 Linux 机器，全部封闭。模型的情况则是混杂的。10 月 15 日 Meta 发布了 Muse Spark Open，它称之为 Muse Spark 的开放权重版本，采用它自己的、带商业条件的许可。Muse Wonder 于 10 月 12 日宣布，并将为更多 Muse 功能提供支持，但没有公开权重。Meta 没有说 Spark Open 就是 Muse agent 运行所用的模型。

那么「Meta Muse 开源」并不是一个空洞的搜索词，因为 Meta 确实开放了三样带 Muse 名字的东西：一套用来打造与 Muse 对话的小设备的工具包，2026 年 10 月 2 日发布；一个名为 Muse Glimmer 的 300 亿参数模型，8 月以开放权重发布；以及 10 月的 Muse Spark Open。它们没有一个能让你自己运行 Muse。本页逐层梳理，说明每个答案的出处，并指出两个专为做「Muse 所不是的东西」而建的开源项目。

- Muse agent、它的应用和它的每用户云虚拟机是封闭的。Meta 公开描述过这套设计，[我们的拆解](https://personalagentbench.com/agents/muse/)也从外部考察过它，但没有公布任何代码。
- Muse Spark 是 Muse 发布时所用的模型，通过 API 提供。10 月 15 日 Meta 还发布了 Muse Spark Open，一个 8160 亿参数的开放权重模型，采用其 Muse Model License，而那不是开源许可。Meta 没有说它就是 Muse agent 内部所用的模型。
- Muse Wonder 于 10 月 12 日宣布，并将为更多 Muse 功能提供动力，仅通过 API 提供。Meta 的模型卡没有提到发布权重，截至 11 月 5 日 Meta 也没有发布任何权重。
- Muse Glimmer 30B 以 Apache 2.0 开放权重，由 Muse Spark 蒸馏而来，为在你自己的硬件上运行而打造。它是一个独立的模型，不是 Meta 所说 Muse 运行所用的那个。
- Muse Gadgets 以 Apache 2.0 开源，但每个小设备配对都需要 Meta 的 token，所以它扩展 Muse，而不是取代 Muse。

## Meta Muse 开源吗？逐层给出答案

Muse 这个名字涵盖若干层，每一层有各自的答案。

- **应用。** iOS、Android、网页、WhatsApp，以及自 9 月 17 日起的 Mac 应用。封闭。
- **agent 及其机器。** 每位用户在 Meta 云中获得一台 Linux 虚拟机，agent、它的工具，以及 Meta 称为 Sentinel 的守门人运行在上面。封闭。Meta 公布了这套设计的详细说明，但没有公布代码。
- **模型。** Meta 的[发布帖](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)说 Muse「由 Muse Spark 驱动」，Meta 的[安全说明](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)点名的是 Muse Spark 1.3。10 月 12 日 Meta 表示 Muse Wonder 很快会为更多 Muse 功能提供动力，订阅用户优先。Wonder 没有公开权重。Spark 现在有了一个开放权重版本 Muse Spark Open，但 Meta 没有说产品用的就是它。
- **Muse Code。** Meta 独立的终端编程 agent，从 [dev.meta.ai](https://dev.meta.ai/docs/muse-code) 安装。Meta 于 [2026 年 8 月 31 日宣布其结束测试](https://dev.meta.ai/resources/blog/muse-code-new-plans-and-features)。它的[公开 SDK](https://github.com/meta-models/muse-code-sdk)采用 MIT 许可，但该仓库明确不含宿主二进制文件；这并不能证明完整的 agent 运行时是开源的。

- **它周边的设备。** [Muse Gadgets SDK](https://github.com/facebookincubator/muse-gadget-sdk)以 Apache 2.0 开源。

另外，同一家族里还有两个开放权重模型，Muse Glimmer 30B 和 Muse Spark Open。Meta 都没有点名它们是 Muse 产品背后的模型。

所以简短的答案是：运行 Muse 你需要的东西是封闭的，开源的东西都在它的边缘。

## Meta Muse 的 agent 与虚拟机：封闭，但公开描述过

让 Muse 成为 Muse 的部分是 agent：一段长对话、以文件形式保存的记忆、它可以调用的工具，以及挡在一切离开这台机器的东西前面的闸门。所有这些都运行在 Meta 为每位用户配置的虚拟机上，Meta 称之为 Muse Secure VM。这套运行时没有任何部分以源码形式公布。

Meta 公布的是异常详细的描述。安全说明解释了：第二个 agent「Sentinel」是唯一能批准连接器操作或放行网络流量的东西；agent 使用的是替身凭据，在批准后于网络边缘被换成真实凭据；批准请求直接送到你的应用，而不是经由对话。它还说到，目前 Meta 员工对你数据的访问是靠政策限制，而非在技术上使其不可能，并且计划在以后提供加密的 Muse Confidential VM。

公布的设计不是开源。你无法阅读执行这套设计的代码、无法自己运行它，也无法检查你正在对话的那个构建是否与描述相符。我们的 [Muse 拆解](https://personalagentbench.com/agents/muse/)最远只到了请求结构和 246 个方法的权限表，并列出了它够不到的东西，首先就是运行时实际发给模型的每一个请求。

## Muse Spark 与 Muse Spark Open：托管，以及自 10 月起的一个开放权重版本

Muse Spark 是 Meta 发布帖所称的「迄今为止最强的模型」，也是 Meta 在发布帖和安全说明中都为 Muse 点名的模型。你可以通过 API 调用 Spark 模型。[OpenRouter 的 Meta 页面](https://openrouter.ai/meta)在 2026 年 11 月 5 日列出了 Muse Spark 1.1、1.2 和 1.3，以及作为托管模型的开放权重版 Spark Open，按 token 计价，与其他托管模型一样。

10 月 15 日 Meta [介绍了 Muse Spark Open](https://research.meta.ai/blog/muse-spark-open)，称之为 Muse Spark 的开放权重版本，并把权重放到 [Hugging Face](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) 上。模型卡描述的是一个混合专家模型，总参数 8160 亿、激活参数 420 亿，上下文 100 万 token，输入支持文本、图像、视频和音频，输出为文本。它说这个版本做了额外的安全后训练，以便在没有 Meta 自己的护栏的情况下运行时更难被滥用。Meta 的帖子还列出 Amazon SageMaker AI、Google Cloud Model Garden 和 Microsoft Foundry 作为获取权重的渠道，以及七家托管 API 提供商，其中包括 OpenRouter 和 Together AI。

权重附带条件。许可为 Meta 自有的 Muse Model License，不是开源许可。基于该模型构建的任何东西都必须显示「Built with Muse Spark Open」。如果一家公司把该模型作为服务提供给他人，且其与关联方在任何 12 个月期间的合计总收入超过 2000 万美元，则须先通知 Meta 并另签协议。使用须遵循 Meta 的使用政策，下载前有一个表单，要求填写你的法定姓名、出生日期和组织。它也不是家庭项目：模型卡给出的压缩权重约为 700 GB 显存，全精度版本约为 2 TB，Meta 的帖子说它运行在两台搭载 M5 Ultra 芯片的 Mac Studio 上。

这次发布推翻了此前释放过的相反信号。5 月，[Implicator 报道](https://www.implicator.ai/alex-wang-says-muse-spark-is-not-ready-for-open-source/)称，负责 Meta AI 工作的 Alexandr Wang 说 Muse Spark 触发了安全检查，使其不适合开源。8 月，[Constellation Research 报道](https://www.constellationr.com/insights/news/meta-releases-open-weight-muse-glimmer-model-open-muse-spark-12-tap)称 Wang 说过 Muse Spark 1.2 会有一个开放权重版本。Meta 的帖子和模型卡都没有说 Spark Open 是基于哪个 Spark 版本构建的，也都没有说它就是 Muse agent 运行的模型；就产品而言，Meta 点名的是 Spark，并在其安全说明中点名 Spark 1.3。

这对任何希望复现 Muse 的人来说很重要。Spark Open 给你的是一个你可以托管的大型 Meta 模型，而不是 agent、它的工具、它的守门人，也不是它的虚拟机，还不一定是产品所调用的那个确切模型。

## Muse Wonder：更新的模型，且封闭

10 月 12 日 Meta [宣布 Muse Wonder](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)有两个版本，Muse Wonder 和 Muse Wonder Full，并称它们是迄今为止最强的模型。根据 Meta 的[研究文章](https://research.meta.ai/blog/muse-wonder)，Muse Wonder 现在可以通过 Meta Model API 调用，并可在 Muse Code 中使用，Muse Wonder Full 只对 Muse Code 订阅用户开放，而 Wonder「很快将为 Muse 中的体验提供动力」，订阅用户优先。Meta 没有给出免费账户的日期。

这些都不涉及权重。[模型卡](https://research.meta.ai/static/muse-wonder-model-card)列出 100 万 token 上下文，输入文本、图像、视频和音频，输出文本。关于权重，它只说 Meta 在开发和部署期间依据其权重安全计划对权重加以保护。公告和模型卡都没有提到发布权重。11 月 5 日，[OpenRouter](https://openrouter.ai/meta) 将 Muse Wonder 列为托管模型，每 100 万输入 token 4 美元、每 100 万输出 token 20 美元，与 Spark API 模型相同的托管方式，价格更高。

有一件事要留意。公告数小时后，一个自称 meta-01 的 Hugging Face 账号创建了名为 muse-wonder 的仓库。11 月 5 日它仍不含任何模型文件，而该账号并非以 meta-models 名义发布的 Meta Superintelligence Labs。meta-models 账号列出了 Glimmer 和 Spark Open，没有 Wonder。「Muse Wonder 权重」的下载链接并不代表 Meta 开放了什么。

Meta 还说会用 Muse Wonder 为所有使用 Muse 的人构建专门的模型。这是关于把同等水平的能力带给所有 Muse 用户，不是开放权重的承诺。Glimmer 是通过蒸馏从 Spark 而来，Spark 现在有了开放权重版本，但 Meta 没有说 Wonder 会不会产出任何开放的东西。

## Muse Glimmer：Meta Muse 家族中的小型开放权重模型

[Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) 是 Meta 两个开放权重 Muse 模型中较小的那个。Meta Superintelligence Labs 于 2026 年 8 月 9 日在 Hugging Face 上以 Apache 2.0 许可发布，下载不设门槛。

模型卡描述的是一个约 296 亿参数的稠密模型，内置图像编码器，由 Muse Spark 蒸馏而来，「专为消费级硬件上的自主 agent 任务而打造」。量化到约 4 位后，语言模型不到 20 GB，模型卡列出的目标配置从 24 GB 到 64 GB 显存。它点名工具使用、故障恢复和多步规划是训练目标，并说它可以配合 [OpenClaw](https://personalagentbench.com/openclaw-security/) 和 [Hermes Agent](https://personalagentbench.com/hermes-agent/) 等开放 agent 框架使用。

两点提醒。第一，Glimmer 不是 Meta 所说 Muse 运行所用的模型；发布帖和安全说明点名的都是 Spark。在家里运行 Glimmer 得到的是同一实验室出品的一个能力不错的开放模型，而不是 Muse 的副本。第二，「开放权重」不等于开放训练。模型卡说训练数据包括公开可得的数据、授权数据和来自 Meta 产品与服务的信息，而这些数据一概没有发布。

对很多人来说，Glimmer 仍是这个问题最有用的答案，因为 Spark Open 需要数百 GB 显存或两台顶配 Mac Studio。如果你想要的是一个 Meta 训练的、能在你已有硬件上跑 agent 任务的模型，那就是它。我们的[运行环境](https://personalagentbench.com/where-it-runs/)页面把托管 agent 与你自己运行的 agent 并列，像这样的模型就该归到那里。

## Muse Gadgets：Meta Muse 本身的开源部分

引发早期多数「Meta Muse 开源」标题的发布是 [Muse Gadgets](https://github.com/facebookincubator/muse-gadget-sdk)，2026 年 10 月 2 日由 Meta 在 GitHub 上以 facebookincubator 组织发布。

它包含两套设备 SDK。一套是面向现成 ESP32 开发板的固件，这样一块带屏幕、扬声器或若干传感器的小板就能向 Muse 显示图像、播放音频或上报读数。另一套是面向树莓派或任何闲置 Linux 机器的服务，这样你可以添加自己的命令，让 Muse 在上面跑杂活。在 Muse 应用的设备设置里打开开发者模式后，小设备就能与 iOS 和 Android 上的 Muse 应用配对。Meta 的 README 对风险态度轻松，并把变砖的开发板和失效的保修列为副作用。

安装方面，请遵循官方 [ESP32 快速入门](https://github.com/facebookincubator/muse-gadget-sdk/blob/main/esp32/README.md)或 [Linux 说明](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/linux)。配对前请获取 SDK token 并阅读条款。

代码采用 Apache 2.0，少数第三方文件适用各自的许可，另有一项例外：动画化身不在覆盖范围内。更大的限制在配对环节。每个小设备都需要 Meta 的 SDK token，并受 Meta 单独的 Gadget SDK 条款约束。所以 Muse Gadgets 的开源，是指你可以阅读和修改设备端。它并不能让 Muse 变得可移植：一个背后没有 Muse 账号的小设备，没有任何东西可对话。

## Meta Muse 的开源替代品

如果搜索背后的问题是「我能不能拥有一个自己运行的、类似 Muse 的东西」，有两个项目就是专门为此而建，而它们做了相反的选择。

来自 CopilotKit 的 [OpenMuse](https://personalagentbench.com/openmuse/) 于 9 月 15 日以 MIT 许可发布。它运行在你控制的服务器上，带一个持久化浏览器和一个可选的 Linux 工作区，应用是通往那台服务器的窗口。我们是阅读其源码，而不是探测它。我们发现的隐患是，对话持久化依赖一项托管的 CopilotKit 服务，而 MIT 许可并不覆盖它。

来自浙江大学一个小团队的 [nanoMuse](https://personalagentbench.com/nanomuse/) 于 9 月下旬以 GPL-3.0-or-later 上了 GitHub。它把完整的 agent 放到你每一台设备上，而不是一台服务器上一个 agent，在 Android 和电脑上它可以通过屏幕操作其他应用；Meta Muse 也有一个 Mac 应用，可以在某些 Mac 应用里操作。它的论文坦承，它缺少 Muse 的每用户虚拟机以及随之而来的硬安全边界。

两者都与 Meta 无关，都没有经过我们的考察，而且都很年轻。它们各自在本站有一页，说明哪些是公开的、哪些仍未知。

## 一个开源的 Meta Muse 会改变什么

这里主张开放的理由并不抽象。个人 agent 掌握你的收件箱、日历和一份关于你的书面档案，并在你不在时据此行动。人们最想知道的关于这样东西的问题——它究竟发送什么、保留什么、支付前的闸门是否真的守得住——恰恰是最难从外部弄清的问题。

我们自己的工作显示了这一差距。在 Muse 上，我们能描述请求的形态和权限表，但从未见过一个请求离开那台机器。[OpenMuse](https://personalagentbench.com/open-source-personal-agents/#openmuse) 的公开仓库可以被检查；我们没有检查其托管持久化的内部实现，也没有确认每一个数据目的地。这都不是对哪个更安全的判决，但只有其中一个能被任何愿意查看的人检查。

我们的 [Muse 拆解](https://personalagentbench.com/agents/muse/)描述了一台每用户 Linux 虚拟机，模型请求在其中组装，而 Meta 的安全说明比多数厂商公布的更详细。开放设备套件和两个模型是实实在在的步骤。你实际对话的那个 agent，以及它运行的那台机器，仍然属于 Meta。

## 常见问题

**Meta Muse 开源吗？** 不开源。Muse agent、它的应用和它运行所在的云虚拟机都是封闭的，Muse Wonder 也没有公开权重。Meta 开源了 Muse Gadgets SDK，并发布过两个开放权重模型：8 月的 Muse Glimmer 30B 和 2026 年 10 月 15 日的 Muse Spark Open，后者采用带商业条件的许可。

**Muse Spark 开源吗？** 部分开源，且不是采用开源许可。Spark 模型通过托管 API 提供，2026 年 10 月 15 日 Meta 发布了 Muse Spark Open，一个 8160 亿参数的开放权重版本，采用其 Muse Model License，要求署名，且大型模型即服务企业须另签协议。Meta 没有说它是 Muse agent 使用的模型。由 Spark 蒸馏而来的 Muse Glimmer 30B 是更小的开放权重选项。

**Muse Wonder 开源吗？** 不开源。Meta 于 2026 年 10 月 12 日宣布 Muse Wonder 和 Muse Wonder Full 为托管模型，可通过 Meta Model API 和 Muse Code 访问。模型卡没有提到发布权重，Hugging Face 上的 muse-wonder 仓库在 11 月 5 日仍是空的，且属于一个并非 Meta 的账号。

**Muse Glimmer 是什么？** 来自 Meta Superintelligence Labs 的一个约 300 亿参数的开放权重模型，2026 年 8 月以 Apache 2.0 发布，为 agent 任务而建，设计为在消费级硬件上运行。它不是 Meta 所说驱动 Muse 应用的模型。

**Muse Gadgets 是什么？** 一套开源 SDK，2026 年 10 月 2 日发布，用于在 ESP32 开发板或 Linux 电脑上构建能与你的 Muse 配对的小设备。每个小设备都需要 Meta 的 token 才能配对。

**我能自行托管 Meta Muse 吗？** 不能。agent 只在 Meta 的基础设施上运行。如果你想要形状相同、由你自己运行的东西，[OpenMuse](https://personalagentbench.com/openmuse/) 和 [nanoMuse](https://personalagentbench.com/nanomuse/) 是两个形状相同的独立开源项目；[源码对比](https://personalagentbench.com/open-source-personal-agents/)涵盖它们的实现限制及其他选项。

**OpenMuse 是 Meta 做的吗？** 不是。[OpenMuse](https://personalagentbench.com/openmuse/) 来自 CopilotKit，[nanoMuse](https://personalagentbench.com/nanomuse/) 来自一个独立的大学团队。它们的名字不能说明与 Meta 有关联，也不能说明维护者选择这些名字的理由。
