---
title: "Microsoft Autopilot：商业与规模"
linkTitle: "商业与规模"
weight: 110
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 仍没有公开的用户数、组织数或收入；商业上它是 Microsoft 365 Copilot 许可证之上的按用量收费项，由 Agent 365 的成本管理与业务分析承接。微软称它是「首个面向个人生产力的企业级长时运行智能体」，并把支撑它的身份与邮箱能力开放给其他智能体。
---

## 概要

- 规模数据仍只有发布前的内部数字（2026-05-01 每天超过 3,000 名内部用户）；Ignite 前后的资料没有 Autopilot 的用户、组织或付费数。
- 新闻手册称它是「微软首个面向个人生产力的企业级长时运行智能体」，驻留在组织租户中（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。Shahine 在推文中称团队「7 个月零 11 天前」还是零人零代码（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）。
- 商业模式：叠加在 Microsoft 365 Copilot 许可证（USL）之上，另按 Copilot Credits 收费（UBB），由管理员支出策略设限；微软称部分能力会随成本下降移入订阅（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。
- Agent 365 承接治理与 FinOps：成本管理覆盖 Autopilot，Business Analytics 以成功率、满意度、受助时长衡量价值（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})）。
- 背景数字都属于 Copilot 整体：Fortune 称 7 月付费席位超过 3,000 万；Copilot 博客称近 80% 的《财富》500 强使用 Cowork（[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。

## 2026-11：首个企业级长时运行个人智能体

新闻手册把 Autopilot 与 Home、Auto、Office in Copilot、Code、Managed Runtime 并列为「新的 Copilot」，称其为「微软首个面向个人生产力的企业级长时运行智能体」（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。Fortune 9 月报道，Nadella 以新 Copilot 赢得订阅、防止生产力产品被新一代 AI 对手边缘化，统一 Copilot 团队由 Jacob Andreou 负责（[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})）。TestingCatalog 转述 Shahine 的推文：「7 个月零 11 天前，我们团队还是零人、零行代码」（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）。

Tech Community 博文称微软把支撑 Autopilot 的能力开放给产品组合中其他受支持的智能体，如 Sales Development Agent 和 Copilot Studio 智能体，可配备自己的邮箱地址和受保护的 Microsoft 365 资源（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})）。

推断：从这一表述看，Autopilot 的「身份 + 邮箱 + 云端计算机」被当作平台能力，而不只是一个产品；它的商业价值可能更多体现在带动 Copilot 许可证与 Copilot Credits 的消耗上。

## 收费方式：许可证之上的用量

| 层 | 内容 | 来源 |
| --- | --- | --- |
| USL | Microsoft 365 Copilot 每用户月费，「日常 AI」；Autopilot 的前提 | [Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}}) |
| UBB | Copilot Credits 计量；Autopilot、Cowork、Code、前沿模型 | [Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 治理 | Agent 365 成本管理：支出策略、限额、提醒、控制可用模型；Business Analytics 以完成的工作而非 token 衡量投资 | [Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}}) |

微软称日常 AI 不放在计量表上，理由是计量会让公司限制使用，「我们认为每个人都应该能用」（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）。十月汇总称借助 Agent 365，组织可以了解谁在使用 Autopilot、评估风险、衡量业务价值以指导推广（[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})）。Redmondmag 认为组织可能部署数百甚至数千个全天候运行的智能体，支出可见性因此重要（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。

## Copilot 整体的数字

| 数字 | 口径与时间 | 来源 |
| --- | --- | --- |
| 付费席位超过 3,000 万，净增席位环比翻倍 | Microsoft 365 Copilot，微软 7 月所称 | [Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}}) |
| 近 80% 的《财富》500 强使用 Cowork；Lilly 超过 5,000 人每月使用 Cowork | 微软 Ignite 博客 | [Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}}) |
| 质量相当时比 Claude 便宜 84%、比 ChatGPT 便宜 63%（日常用户） | 微软引 GigaOm 报告，厂商引用 | [Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}}) |

这些都不是 Autopilot 的数字。

## 竞争与评价

The Neuron 把 Autopilot 看作微软对 Muse、Dots、Grok Bot、Claude Duet 等个人智能体的回应，优势在于离工作近（Microsoft 365 数据与权限），关心的是它需要多少照看（[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})）。UC Today 认为身份是买方的分界线，各家都缺客户证据，并提醒不要把 Frontier 推出误当成可买的产品（[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})）。TestingCatalog 作者认为微软借此超过了 Google（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）。The Register 6 月称其为「工作保姆」，预料账单上涨（[The Register]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-register-copilot-take-the-wheel" >}})）。

## 更名前：起源与早期判断（2026-05 至 2026-11）

以下为 2026-11-14 分析的内容。

### 起源：一个 OpenClaw 业余项目

官方对谈讲述了来历：Shahine 业余用 OpenClaw 做了个人助手 Lobster，向 Microsoft AI Accelerator 小组演示后转任 CVP，负责「Project Lobster」，把 OpenClaw 带到 Microsoft 365 和云端；Jakob Werner 的桌面端智能体 Clawpilot 几周内被数千名员工下载，后与 Shahine 的团队合流（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。GeekWire 补充：2 月 26 日的演示、3 月 31 日的新角色，团队名 Ocean 11、少数几人、每人运行自己的 Lobster（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。Shahine 此前领导 Word 团队，在微软超过 25 年（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）。

Shahine 的动机是：现有的 Copilot Tasks（消费者预览）与 Copilot Cowork（企业）都不是全天候代用户工作、触及真实生活的助手，「正是这一空白促使他把目标对准知识工作者」（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。

社区作者称 Scout「用 57 天构建」，文中没有出处（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。

### 规模数据

| 数字 | 口径与时间 | 来源 |
| --- | --- | --- |
| 每日超过 3,000 名用户（一周前 100） | 微软内部测试 ClawPilot，截至 2026-05-01 | [GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}}) |
| 数千名员工下载 | 内部原型 Clawpilot，未给时间 | [OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}}) |

对外开放后的用户数、组织数、付费数，资料中都没有。

### 依附的订阅：Microsoft 365 Copilot 与 GitHub Copilot

Computerworld 提到 Microsoft 365 Copilot 面向大型企业标价每用户每月 30 美元，1 月时约 3% 的 Microsoft 365 客户付费、有 1,500 万付费用户，随后升至 2,000 万；并称微软一直难以让企业相信它值得额外付费（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。dSebastien 转述 Fortune 称 7 月有 3,000 万个付费 Microsoft 365 Copilot 席位（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。这些是 Copilot 整体的数字，不是 Scout 的。

Scout 的前提包括 GitHub Copilot 席位，令牌用量经 GitHub 计费（[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})）；Semafor 称预览期间消耗 GitHub Copilot 额度，并指出「最大的问题是成本」，包括微软自身在内的公司已开始削减 AI 支出（[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})）。9 月后改为按用量计费，见[开放与价格]({{< relref "/docs/microsoft-autopilot/analysis/access-pricing" >}})。

推断：Scout 预览期借用 GitHub Copilot 的计费与模型通道，省去了单独的计费体系；代价是用户要同时持有 Microsoft 365 与 GitHub 两套许可，这也是进入门槛高的原因之一。

### 战略：新 Copilot 的三分之一

9 月 25 日的文章把新 Copilot 分为 Home、Code、Autopilot 三部分，以 Microsoft IQ 为统一智能层，配插件注册表与 FinOps for AI；Ignite（11 月 17 日至 20 日）将分享更多信息（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。Build 时 Nadella 称 Autopilots 是「企业级的 Claws」（[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})）。

dSebastien 汇总的反响（均为转述）：Gizmodo 对 Copilot「一连串短命的改名」持怀疑；Fortune 称这是对 Copilot 产品泛滥的修正；Bloomberg 标题称微软借 Copilot 重启放弃个人 AI 聊天机器人竞赛（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。社区作者还指出名字与设备预配服务 Windows Autopilot 撞名（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})、[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。

The Neuron 的作者观点是，Scout 是检验大型组织是否允许智能体成为工作中持久参与者的测试案例，微软的身份、权限、合规基因是优势（[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})）。

### 与 OpenClaw 的关系

微软 6 月称向 OpenClaw 上游贡献策略合规功能（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）。dSebastien 转述 OpenClaw 博客：2026-07-08 OpenClaw 基金会亮相时，微软被列为「直接向上游贡献」的伙伴，而非捐赠者（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。OpenClaw 博客自己声明，并非每项微软员工的贡献都是 Autopilot 功能或公司赞助项目（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。社区作者的概括是：运行时开放，身份、策略、计费和 Microsoft 365 数据仍归微软（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

## 资料缺口

- Autopilot 的用户数、组织数、付费数；Copilot Credits 收入口径。
- 单个 Autopilot 的典型成本。
- 能力开放给其他智能体的产品化计划。

## 主要资料

- 官方：[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})（起源）；[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})；[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（新 Copilot 战略）。
- 媒体：[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})（内部规模与动机）；[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})（Copilot 付费背景）；[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})、[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})、[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})。
- 社区：[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})（反响汇总）；[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})、[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})。
- 2026-11 新增官方：[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})（定位与 Copilot 数字）；[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})（收费方式）；[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})。
- 2026-11 新增媒体：[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})、[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})、[The Register]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-register-copilot-take-the-wheel" >}})。
- industry：[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})。
