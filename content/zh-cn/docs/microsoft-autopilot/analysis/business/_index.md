---
title: "Microsoft Autopilot：商业与规模"
linkTitle: "商业与规模"
weight: 110
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 没有公开的用户数、组织数或收入，唯一的规模数字是发布前内部测试「每天超过 3,000 名用户」。商业上它是 Microsoft 365 Copilot 许可证之上的按用量收费项，由 Agent 365 的成本管理与业务分析承接；微软称它是「首个面向个人生产力的企业级长时运行智能体」，起源是一位副总裁的 OpenClaw 业余项目。
---

## 概要

- 规模数据只有内部数字：据 GeekWire，截至 2026-05-01 微软内部每天有超过 3,000 名用户测试 ClawPilot（一周前 100）；对外推出后的用户、组织、付费数都没有。
- 新闻手册称 Autopilot 是「微软首个面向个人生产力的企业级长时运行智能体」；它与 Home、Code 等并列为 9 月发布的「新 Copilot」的一部分。
- 商业模式：叠加在 Microsoft 365 Copilot 许可证（USL）之上，另按 Copilot Credits 收费（UBB），由管理员支出策略设限；微软称部分能力会随成本下降移入订阅。
- Agent 365 承接治理与 FinOps：成本管理覆盖 Autopilot，Business Analytics 以成功率、满意度、受助时长衡量价值。
- 起源是 CVP Omar Shahine 用 OpenClaw 搭的个人助手 Lobster；Shahine 称团队「7 个月零 11 天前」还是零人零代码。
- 背景数字都属于 Copilot 整体：7 月付费席位超过 3,000 万，近 80% 的《财富》500 强使用 Cowork。

## 起源：一个 OpenClaw 业余项目

官方对谈讲述了来历：Shahine 业余用 OpenClaw 做了个人助手 Lobster，向 Microsoft AI Accelerator 小组演示后负责「Project Lobster」，把 OpenClaw 带到 Microsoft 365 和云端；Jakob Werner 的桌面端智能体 Clawpilot 几周内被数千名员工下载，后与 Shahine 的团队合流（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。GeekWire 补充 2 月 26 日的演示、3 月 31 日的新角色、团队名 Ocean 11 和每天超过 3,000 名内部用户（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。Shahine 的动机是现有的 Copilot Tasks 与 Copilot Cowork 都不是全天候代用户工作的助手（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。

2026-06-02 Build 以 Microsoft Scout 之名发布，Nadella 称 Autopilots 是「企业级的 Claws」（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})）；9 月 25 日更名 Autopilot，纳入新 Copilot（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）；11 月 17 日在 Ignite 上以云端形态向 Frontier 推出（[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})）。TestingCatalog 转述 Shahine 的推文：「7 个月零 11 天前，我们团队还是零人、零行代码」（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）。

与 OpenClaw 的关系：微软 6 月称向上游贡献策略合规功能（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）；OpenClaw 博客称 Autopilot 以 OpenClaw 为基础，并声明并非每项微软员工的贡献都是 Autopilot 功能（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。社区作者概括为运行时开放，身份、策略、计费和 Microsoft 365 数据仍归微软（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。11 月的 Autopilot 文档不再提 OpenClaw。

## 首个企业级长时运行个人智能体

新闻手册把 Autopilot 与 Home、Auto、Office in Copilot、Code、Managed Runtime 并列为「新的 Copilot」，称其为「微软首个面向个人生产力的企业级长时运行智能体」（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。Fortune 9 月报道，Nadella 以新 Copilot 赢得订阅、防止生产力产品被新一代 AI 对手边缘化，统一 Copilot 团队由 Jacob Andreou 负责（[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})）。

Tech Community 博文称微软把支撑 Autopilot 的能力开放给产品组合中其他受支持的智能体，如 Sales Development Agent 和 Copilot Studio 智能体，可配备自己的邮箱地址和受保护的 Microsoft 365 资源（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）。

推断：「身份 + 邮箱 + 云端计算机」被当作平台能力，而不只是一个产品；Autopilot 的商业价值可能更多体现在带动 Copilot 许可证与 Copilot Credits 的消耗上。

## 收费方式：许可证之上的用量

| 层 | 内容 | 来源 |
| --- | --- | --- |
| USL | Microsoft 365 Copilot 每用户月费，「日常 AI」；Autopilot 的前提 | [Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}}) |
| UBB | Copilot Credits 计量；Autopilot、Cowork、Code、前沿模型 | [Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 治理 | Agent 365 成本管理：支出策略、限额、提醒、控制可用模型；Business Analytics 以完成的工作而非 token 衡量投资 | [Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}}) |

微软称日常 AI 不放在计量表上，理由是计量会让公司限制使用，「我们认为每个人都应该能用」（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）。十月汇总称借助 Agent 365，组织可了解谁在使用 Autopilot、评估风险、衡量业务价值以指导推广（[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})）。Redmondmag 认为组织可能部署数百甚至数千个全天候运行的智能体，支出可见性因此重要（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。Semafor 在 6 月就指出「最大的问题是成本」（[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})）。

## 规模数据

| 数字 | 口径与时间 | 来源 |
| --- | --- | --- |
| 每日超过 3,000 名用户（一周前 100） | 微软内部测试 ClawPilot，截至 2026-05-01 | [GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}}) |
| 付费席位超过 3,000 万，净增席位环比翻倍 | Microsoft 365 Copilot 整体，微软 7 月所称 | [Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}}) |
| 1,500 万、后升至 2,000 万付费用户 | Microsoft 365 Copilot 整体，Computerworld 6 月所述 | [Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}}) |
| 近 80% 的《财富》500 强使用 Cowork；Lilly 超过 5,000 人每月使用 Cowork | 微软 Ignite 博客 | [Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}}) |
| 质量相当时比 Claude 便宜 84%、比 ChatGPT 便宜 63%（日常用户） | 微软引 GigaOm 报告，厂商引用 | [Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}}) |

除第一行外都不是 Autopilot 的数字。

## 竞争与评价

The Neuron 把 Autopilot 看作微软对 Muse、Dots、Grok Bot、Claude Duet 等个人智能体的回应，优势在于离工作近（Microsoft 365 数据与权限），关心的是它需要多少照看（[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})）。UC Today 认为身份是买方的分界线，各家都缺客户证据，并提醒不要把 Frontier 推出误当成可买的产品（[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})）。TestingCatalog 作者认为微软借此超过了 Google（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）。The Register 称其为「工作保姆」，预料账单上涨（[The Register]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-register-copilot-take-the-wheel" >}})）。dSebastien 汇总的反响中，Gizmodo 对 Copilot 反复改名持怀疑，Fortune 称这是对产品泛滥的修正（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）；名字还与设备预配服务 Windows Autopilot 撞名（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})、[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。

## 资料缺口

- Autopilot 的用户数、组织数、付费数；Copilot Credits 收入口径。
- 单个 Autopilot 的典型成本。
- 能力开放给其他智能体的产品化计划。

## 主要资料

- 官方：[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})（定位与 Copilot 数字）；[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})（收费方式）；[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})；[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})、[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（起源与沿革）。
- 媒体：[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})（内部规模与动机）；[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})、[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})、[The Register]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-register-copilot-take-the-wheel" >}})、[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})、[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})、[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})。
- 社区：[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})、[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})。
- industry：[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})。
