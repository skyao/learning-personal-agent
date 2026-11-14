---
title: "Microsoft Autopilot：商业与规模"
linkTitle: "商业与规模"
weight: 110
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-10
description: >
  Autopilot 没有公开的用户数或收入数据，唯一的规模数字是发布前内部测试「每天超过 3,000 名用户」。它起于一位副总裁的 OpenClaw 业余项目，商业上依附 Microsoft 365 Copilot 与 GitHub Copilot 的企业订阅，9 月后并入按用量计费的新 Copilot。
---

## 概要

- 规模数据只有内部数字：据 GeekWire，截至 2026-05-01，微软内部每天有超过 3,000 名用户测试基于 OpenClaw 的 ClawPilot，一周前为 100 人；官方称内部原型几周内被「数千名」员工下载。正式上线后的用户数、付费数没有资料。
- 起源是 CVP Omar Shahine 用 OpenClaw 搭的个人助手 Lobster，团队名 Ocean 11，人数很少。
- 商业模式不独立：预览期间消耗 GitHub Copilot 额度，9 月后与 Cowork、Code 一起按用量计费，与 Copilot 的每用户订阅分开。
- 背景是 Microsoft 365 Copilot 的付费推广：Computerworld 称微软一直难以让企业相信 Copilot 值得额外付费；不同来源给出的付费用户数为不同时点（1,500 万、2,000 万、3,000 万席位）。
- 战略上，9 月的新 Copilot 把 Autopilot 放进 Home、Code、Autopilot 三分结构；微软与 OpenClaw 的关系是向上游贡献代码。

## 起源：一个 OpenClaw 业余项目

官方对谈讲述了来历：Shahine 业余用 OpenClaw 做了个人助手 Lobster，向 Microsoft AI Accelerator 小组演示后转任 CVP，负责「Project Lobster」，把 OpenClaw 带到 Microsoft 365 和云端；Jakob Werner 的桌面端智能体 Clawpilot 几周内被数千名员工下载，后与 Shahine 的团队合流（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。GeekWire 补充：2 月 26 日的演示、3 月 31 日的新角色，团队名 Ocean 11、少数几人、每人运行自己的 Lobster（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。Shahine 此前领导 Word 团队，在微软超过 25 年（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）。

Shahine 的动机是：现有的 Copilot Tasks（消费者预览）与 Copilot Cowork（企业）都不是全天候代用户工作、触及真实生活的助手，「正是这一空白促使他把目标对准知识工作者」（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。

社区作者称 Scout「用 57 天构建」，文中没有出处（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。

## 规模数据

| 数字 | 口径与时间 | 来源 |
| --- | --- | --- |
| 每日超过 3,000 名用户（一周前 100） | 微软内部测试 ClawPilot，截至 2026-05-01 | [GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}}) |
| 数千名员工下载 | 内部原型 Clawpilot，未给时间 | [OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}}) |

对外开放后的用户数、组织数、付费数，资料中都没有。

## 依附的订阅：Microsoft 365 Copilot 与 GitHub Copilot

Computerworld 提到 Microsoft 365 Copilot 面向大型企业标价每用户每月 30 美元，1 月时约 3% 的 Microsoft 365 客户付费、有 1,500 万付费用户，随后升至 2,000 万；并称微软一直难以让企业相信它值得额外付费（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。dSebastien 转述 Fortune 称 7 月有 3,000 万个付费 Microsoft 365 Copilot 席位（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。这些是 Copilot 整体的数字，不是 Scout 的。

Scout 的前提包括 GitHub Copilot 席位，令牌用量经 GitHub 计费（[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})）；Semafor 称预览期间消耗 GitHub Copilot 额度，并指出「最大的问题是成本」，包括微软自身在内的公司已开始削减 AI 支出（[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})）。9 月后改为按用量计费，见[开放与价格]({{< relref "/docs/microsoft-autopilot/analysis/access-pricing" >}})。

推断：Scout 预览期借用 GitHub Copilot 的计费与模型通道，省去了单独的计费体系；代价是用户要同时持有 Microsoft 365 与 GitHub 两套许可，这也是进入门槛高的原因之一。

## 战略：新 Copilot 的三分之一

9 月 25 日的文章把新 Copilot 分为 Home、Code、Autopilot 三部分，以 Microsoft IQ 为统一智能层，配插件注册表与 FinOps for AI；Ignite（11 月 17 日至 20 日）将分享更多信息（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。Build 时 Nadella 称 Autopilots 是「企业级的 Claws」（[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})）。

dSebastien 汇总的反响（均为转述）：Gizmodo 对 Copilot「一连串短命的改名」持怀疑；Fortune 称这是对 Copilot 产品泛滥的修正；Bloomberg 标题称微软借 Copilot 重启放弃个人 AI 聊天机器人竞赛（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。社区作者还指出名字与设备预配服务 Windows Autopilot 撞名（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})、[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。

The Neuron 的作者观点是，Scout 是检验大型组织是否允许智能体成为工作中持久参与者的测试案例，微软的身份、权限、合规基因是优势（[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})）。

## 与 OpenClaw 的关系

微软 6 月称向 OpenClaw 上游贡献策略合规功能（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})）。dSebastien 转述 OpenClaw 博客：2026-07-08 OpenClaw 基金会亮相时，微软被列为「直接向上游贡献」的伙伴，而非捐赠者（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。OpenClaw 博客自己声明，并非每项微软员工的贡献都是 Autopilot 功能或公司赞助项目（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）。社区作者的概括是：运行时开放，身份、策略、计费和 Microsoft 365 数据仍归微软（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

## 资料缺口

- 正式上线后的用户数、组织数、付费数；Autopilot 的收入口径。
- 单个 Autopilot 的成本结构与用量。
- 微软对 OpenClaw 基金会的投入方式。

## 主要资料

- 官方：[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})（起源）；[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})；[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（新 Copilot 战略）。
- 媒体：[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})（内部规模与动机）；[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})（Copilot 付费背景）；[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})、[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})、[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})。
- 社区：[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})（反响汇总）；[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})、[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})。
