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
translation: 待翻译
collectedAt: 2026-11-07
dateNote: "页面只标注 article:modified_time 2026-11-05，未见发布日期；文中以 11 月 5 日为截至日期"
tags: [开放与价格, 模型, 运行环境]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载后用 extract.py 抽取；删去页首多语言链接、目录与文末「More on Muse」站内推荐及分享按钮；站内相对链接已改为绝对地址。未署名，发布方为 Personal Agent Bench（JSON-LD 发布机构为 Zentor）；文中关于 Mac 应用「自 9 月 17 日起」的说法未附发布公告或版本号，照录。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：结论是 Muse 产品本身不开源：Muse agent、用户访问它的应用及 Meta 云端为每位用户配置的 Linux 虚拟机全部封闭，模型的情况则混杂。Muse Spark Open 于 10 月 15 日发布，是 Muse Spark 的开放权重版本，共 8160 亿参数（420 亿激活参数），采用 Meta 自有的 Muse Model License（非开源许可），要求标注「Built with Muse Spark Open」，年收入合计超过 2000 万美元的模型即服务商须先通知 Meta 并另签协议；Meta 未说明它是 Muse agent 实际使用的模型。Muse Wonder 于 10 月 12 日发布，仅通过 API 托管，模型卡未提及发布权重，截至 11 月 5 日 Meta 未发布任何 Wonder 权重；Hugging Face 上自称 meta-01 的账号创建的 muse-wonder 仓库截至 11 月 5 日仍无模型文件，且该账号并非 Meta 官方发布账号 meta-models。Muse Glimmer 30B 于 8 月 9 日以 Apache 2.0 许可发布开放权重，由 Muse Spark 蒸馏而来，可在消费级硬件上运行，但并非 Meta 所称 Muse 运行的模型；Muse Gadgets SDK 于 10 月 2 日以 Apache 2.0 开源，但每个小设备配对都需要 Meta 发放的 token；文末另介绍 OpenMuse（MIT 许可）与 nanoMuse（GPL-3.0-or-later）两个与 Meta 无关的开源替代项目。

**保留理由**：本篇对 Muse 各层（agent／应用／云端 VM、Spark／Spark Open、Wonder、Glimmer、Gadgets）的开源状态做了逐层核查与区分，并附自家 teardown 实测（触及请求结构与 246 个方法的权限表）及 Hugging Face 假冒账号核查，提供了「能否自行运行 Muse」这一问题的系统性判定依据。
