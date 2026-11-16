---
title: "AMD 称 EPYC 芯片为 Muse 的计算环境提供动力"
linkTitle: "AMD EPYC 支撑 Muse"
date: 2026-10-28
originalTitle: "AMD's EPYC Chips Power Muse as AMD Deepens Its Meta Partnership and Invests $1 Billion"
sourceUrl: "https://www.allthingsmuse.com/articles/amd-meta-muse-epyc-helios-partnership/"
author: "Icarus"
publisher: "All Things Muse"
basedOn: "AMD 2026-10-27 公告"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-12
tags: [运行环境, 商业与规模]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载。去掉了首图 Jolly 插画与站内 NVIDIA 报道推荐卡片。原文全文存于本目录的 original.md，网站上不显示，已翻译。内容转述 AMD 2026-10-27 的公告，属二手。

**内容摘要**：AMD 于 10 月 27 日宣布，其 EPYC 处理器为 Muse 专属计算环境提供动力，首批 Helios 机架系统已在 Meta 安装并测试，AMD 还将向 Meta 的股权融资投资 10 亿美元。AMD 称 Meta 已部署数百万颗多代 EPYC 处理器，是第六代 EPYC 的首批客户，双方还在合作代号为 Verano 的下一代处理器。AMD 称其技术为 Meta 模型提供发布当日支持，包括运行于 Instinct GPU 的 Muse Spark Open 与运行于 Ryzen AI PC 和 Radeon GPU 的 Muse Glimmer。AMD 首席执行官 Lisa Su 与 Meta 首席执行官 Mark Zuckerberg 均在公告中发言，Zuckerberg 称 AMD 是建设前沿模型算力的关键伙伴。

**保留理由**：首次披露 Muse 专属计算环境运行在 AMD EPYC 处理器上，并给出 Muse Spark Open 与 Muse Glimmer 各自对应的 AMD 硬件平台，是已收资料中关于 Muse 底层算力来源的直接出处。


---

AMD 于 10 月 27 日宣布，其 EPYC 处理器为 Meta 的 Muse 智能体背后的计算环境提供动力，其首批 Helios 系统正在运行…
AMD 于 10 月 27 日宣布，其 EPYC 处理器为 Meta 的 Muse 个人智能体背后的专属计算环境提供动力，这是与 Meta 扩大战略合作的一部分，合作涵盖处理器、图形芯片、网络、系统和软件。AMD 还表示，其首批 Helios 机架级系统已在 Meta 安装并正在测试，并且将向 Meta 的股权融资投资 10 亿美元。

Muse 这一细节是一份更广泛的基础设施公告的一部分。AMD 表示，Meta 已部署数百万颗多代 EPYC 处理器，并且是其第六代 EPYC CPU 的首批客户，两家公司还在合作未来几代产品，包括一个代号为 Verano 的处理器系列。AMD 的 Instinct GPU 已在 Meta 的基础设施中投入生产，用于训练、排序和推荐工作负载，Meta 是 Instinct MI450 架构的早期定义客户，一款针对 Meta 工作负载优化的定制 Instinct GPU 也在路上。

## 对 Muse 模型家族的发布当日支持

AMD 表示，其技术为 Meta 的模型提供发布当日（day-0）支持，包括运行在 Instinct GPU 上的 Muse Spark Open，以及运行在 Ryzen AI PC 和 Radeon GPU 上的 Muse Glimmer。两家公司还通过 PyTorch 在 ROCm 软件上合作，因此开发者可以在 AMD GPU 上使用 Meta 的模型，而无需等待发布后的支持。一项相关的软件合作涵盖大规模 AI 训练，包括在 Instinct MI350X GPU 上优化推荐模型，并为其他开发者向 PyTorch、Triton 和 ROCm 贡献改进。

AMD 首席执行官 Lisa Su 称这一公告是在多年联合设计工作基础上规模的提升。「Meta 是 AMD 的战略合作伙伴，我们通过多年深入的技术合作建立了这一伙伴关系——从为 Meta 基础设施提供动力的 EPYC 处理器，到支持其 AI 工作负载的 Instinct GPU 和开放软件，」Su 说。「随着 Helios 现已在 Meta 运行，我们正在把这一伙伴关系带入超级智能时代的新规模。」

Meta 首席执行官 Mark Zuckerberg 表示，AMD 在其前沿模型背后的算力建设中扮演着重要角色。「AMD 一直是建设运行我们前沿模型的算力的关键合作伙伴，」Zuckerberg 说。「我们正在对算力进行大规模投资，这将使我们能够把个人超级智能带给每个人，而 AMD 在其中扮演着重要角色。」

## 一项并行的芯片合作

[NVIDIA 与 Meta 于 10 月 27 日扩大了他们在 Muse 上的合作](/articles/nvidia-meta-muse-partnership-3-billion/)，包括在推理与训练性能方面的联合工作，以及 NVIDIA 对 Meta 股权融资的 30 亿美元投资。Meta 在 10 月 21 日的第三季度财报电话会上表示，[Muse 用户已超过 1000 万](/articles/muse-10m-users-earnings-call/)，并且该公司正在为建设 AI 基础设施筹集其历史上最大的一笔资金。

AMD 只把 Helios 系统更广泛的部署描述为将在不久的将来到来。这笔 10 亿美元的投资是 Meta 股权融资的一部分。这一公告背后的硬件关系是直接的：该智能体的专属计算环境运行在 AMD EPYC 处理器上，而 Meta 的下一代前沿模型将在发布当日就获得 AMD 的支持。
