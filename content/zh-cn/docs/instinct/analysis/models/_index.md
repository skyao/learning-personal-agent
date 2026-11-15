---
title: "Instinct：模型"
linkTitle: "模型"
weight: 70
analyzedAt: 2026-11-15
sourcesUntil: 2026-11-13
description: >
  Instinct 没有披露底层用哪些模型。创始人称自研了「混合推理与分发管线」，效果接近 Opus 5 级别，后台任务批处理使吞吐提高 3 到 8 倍，蒸馏与剪枝再省 30% 到 50%，并称这是坚持免费的前提。这些都是创始人自述，没有评测数据。
---

## 概要

- 底层模型没有披露。SiliconANGLE 只推断它基于计算机使用（computer use）范式。
- 创始人称自研「混合推理与分发管线」，综合效能「极其逼近 Opus 5 级别」，成本远低于直接调用前沿模型 API。
- 降本的两个手段：后台任务批处理和自研调度，单点吞吐提高 3 到 8 倍；针对专有场景的蒸馏与剪枝，再省 30% 到 50%。
- 创始人把这套管线当作免费模式的前提：全部依赖前沿模型的同步调用，成本不可承受。
- 以上数字都出自创始人的访谈和播客，资料库中没有第三方评测。

## 没有披露的底层模型

资料库中没有任何一篇写明 Instinct 用的是哪家、哪个模型。SiliconANGLE 根据公司「像人类一样使用设备」的说法，推断其核心基于计算机使用范式，这是报道方的推断（[SiliconANGLE：C 轮与新功能]({{< relref "/docs/instinct/sources/media/2026-09-28-siliconangle-series-c" >}})）。潮涌AI 提到创始人 Noah Shinn 与姚顺雨合著过 Reflexion 论文，这是智能体领域较早的论文之一（[潮涌AI：全球 Top15]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})），但这说明的是创始人背景，不是产品用了什么模型。

用户能否选择模型、是否按任务切换模型，资料都没有说明。

## 自研推理管线：创始人的说法

创始人在 Z Finance 整理的访谈中称，Instinct 自研了一套「综合效能极其逼近 Opus 5 级别顶尖模型的混合推理与分发管线」，成本远低于直接调用前沿模型 API；如果全部依赖前沿模型 API，单次同步调用的成本不可承受，所以自研管线是个人智能体能免费普及的前提（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）。

他给出的降本方式有两层（[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})）：

| 手段 | 创始人称的效果 |
| --- | --- |
| 后台任务批处理，加自研推理调度 | 单点吞吐提升 3 到 8 倍 |
| 针对专有场景的端到端蒸馏与剪枝 | 再省下 30% 到 50% 冗余 |

Z Finance 另一篇写 Today AI 的文章转述了同一套说法：Instinct 自建「异构的混合推理与任务调度管线」，不全量依赖上游商业大模型的实时接口，后台任务推迟到低谷时段，用低价的点存算力异步批处理，同一份算力的吞吐提高 3 到 8 倍；文章称 Instinct 是在推理调度层寻找算力套利，对照的是 Meta 在预训练阶段给 Muse 埋入代理能力（[Z Finance：齐俊元与伪命题]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})）。该文称 Instinct 是这批产品里「最早在工程上尝试破局」的（[Z Finance：齐俊元与伪命题]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})）。

推断：「接近 Opus 5 级别」很可能指的是多个模型组合后的任务表现，而非单个自研模型的能力，因为访谈说的是「混合推理与分发管线」。资料没有说明对比用的任务和指标，这句话不能当作能力评测结论。

## 成本的外部估算

行业资料里与 Instinct 有关的成本数字只有一条：海外独角兽社群讨论转述从业者的估计，Muse 和 Instinct 每名用户每天约需 1 到 5 美元，未给出处（[海外独角兽：PA 社群讨论]({{< relref "/docs/industry/sources/community/2026-10-23-haiwaidujiaoshou-discussion" >}})）。同一讨论认为，掌握自有模型和算力的厂商可以通过蒸馏小模型进一步控制成本（[海外独角兽：PA 社群讨论]({{< relref "/docs/industry/sources/community/2026-10-23-haiwaidujiaoshou-discussion" >}})）。甲子光年转述 a16z 的估算，充分使用的个人智能体每用户每天成本可能高达 20 美元（[甲子光年：是不是好生意]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})）。

算力采购和开放节奏见 [运行环境]({{< relref "/docs/instinct/analysis/runtime" >}})，免费模式与商业化见 [商业与规模]({{< relref "/docs/instinct/analysis/business" >}})。

## 资料缺口

- 底层用了哪些模型，是否有自训或微调的模型。
- 「接近 Opus 5 级别」的对比任务、指标和测试方。
- 实际的单用户推理成本，以及批处理对响应速度的影响（Top5Apps 只提到满负荷时回复变慢）。

## 主要资料

- 媒体：[Z Finance：齐俊元与伪命题]({{< relref "/docs/industry/sources/media/2026-10-21-zfinance-qi-junyuan-today" >}})，转述播客中的推理调度与点存算力；[SiliconANGLE：C 轮与新功能]({{< relref "/docs/instinct/sources/media/2026-09-28-siliconangle-series-c" >}})，计算机使用范式的推断；[甲子光年：是不是好生意]({{< relref "/docs/industry/sources/media/2026-10-26-jazzyear-personal-agent-business" >}})，a16z 成本估算。
- 社区：[Z Finance：Noah Shinn 访谈]({{< relref "/docs/instinct/sources/community/2026-09-30-zfinance-noah-shinn-interview" >}})，创始人对推理管线和降本数字的自述；[海外独角兽：PA 社群讨论]({{< relref "/docs/industry/sources/community/2026-10-23-haiwaidujiaoshou-discussion" >}})，每用户每天 1 到 5 美元的估计；[潮涌AI：全球 Top15]({{< relref "/docs/industry/sources/community/2026-10-19-chaoyong-top15" >}})，创始人背景。
