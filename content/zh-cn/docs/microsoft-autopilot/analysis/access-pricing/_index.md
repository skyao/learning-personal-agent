---
title: "Microsoft Autopilot：开放与价格"
linkTitle: "开放与价格"
weight: 100
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-10
description: >
  截至 2026-11-10，Autopilot 没有公开定价，也没有正式可用日期：Scout 2026-06-02 起以实验版向 Frontier 组织开放，需四到五道关口；预览期间用量从 GitHub Copilot 额度扣除。9 月后改为私有预览、按用量计费，价格未公布。
---

## 概要

- 只面向企业：需要 Microsoft 365 工作或学校账户，不支持个人账户。
- 进入要过几道关口：管理员开启 Frontier 访问、设备下发 Intune 策略、提交选择加入的声明表单、每位用户一个 GitHub Copilot Business 或 Enterprise 席位；Learn 文档还要求 Microsoft 365 Copilot 许可证。缺一项登录就失败，且产品内不提示原因。
- 预览期间的计费走 GitHub：令牌用量通过 GitHub 账户计费。据 Semafor，用量从 GitHub Copilot 商业版（每席位每月 19 美元）和企业版（39 美元）的月度额度中扣除。
- 2026-09-25 起 Autopilot 与 Cowork、Code 一起按用量计费（UBB），与 Copilot 的每用户订阅分开；具体价格未在资料中出现。
- 开放节奏：6 月 Frontier 实验版 → 9 月底私有预览；政府云和主权云不可用。

## 开放范围的变化

| 日期 | 状态 | 资料 |
| --- | --- | --- |
| 2026-06-02 | Build 发布，以早期实验版向 Frontier 组织和一批私有预览客户提供；正式可用时间另行通知 | [Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})、[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}}) |
| 2026-06-05 | 桌面客户端开始向 Frontier 组织推出；任何人可下载，进入取决于组织管理员批准 | [TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}}) |
| 2026-09-25 | 更名 Autopilot，「将在本月底扩展到私有预览」 | [新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}}) |
| 2026-11-04 | 社区综述：私有预览自 9 月底，无正式可用日期 | [dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}}) |

Learn 文档每页标为预发布文档，称预览功能「可能不会正式发布」（[Scout 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-overview" >}})、[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})）。iThome 把 Autopilot 记为「2026 年 9 月进入私有预览版」（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})），没有提 6 月的 Frontier 实验版。

## 进入的关口

管理员访问概览把前提分成两道（[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})）：

1. Microsoft 365 管理中心的 Frontier 访问：No access、All users 或 Specific users，保存后约三小时生效。
2. Intune 策略（Windows 的 `AllowScoutFrontierAccess`，未配置时用户可能看到 waitlist 画面，见 [管理员：Intune 部署]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-18-scout-admin-intune-setup" >}})）、Frontier 组织注册声明表单、GitHub Copilot 席位；组织或企业策略须允许 GitHub Copilot app（2026-07-27 起 app 1.1 有独立策略）。

入门页的用户前提：Microsoft 365 工作或学校账户（不支持个人账户）、Microsoft 365 Copilot 许可证、GitHub Copilot Business 或 Enterprise 席位（[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})）。各方列出的前提不完全一致：

| 来源 | Frontier | Intune | 声明 | GitHub Copilot 席位 | Microsoft 365 Copilot 许可证 |
| --- | --- | --- | --- | --- | --- |
| [入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})、[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}}) | 是 | 是 | 是 | 是 | 是（入门页） |
| [The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}}) | 是 | 是 | 是 | 是 | 未列 |
| [CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}}) | 是 | 是 | 是 | 是 | 未列 |
| [dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}}) | 是 | 是 | 是 | 是 | 是 |

CIAOPS 与管理员文档都指出，缺任何一项登录都会失败且没有明确提示（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})）。

## 预览期的计费：GitHub 额度

管理员访问概览与消息中心通告写明 Scout 使用 GitHub 账户做令牌计费，GitHub Copilot 用于 AI 额度消耗和计费（[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})、[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})）。Semafor 报道预览期间 Scout 消耗客户 GitHub Copilot 商业版和企业版订阅的月度额度，「这两档分别为每席位每月 19 美元和 39 美元，且可购买更多额度」；Shahine 未透露正式收费方式（[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})）。Computerworld 称微软未说明 Scout 包含在 Microsoft 365 Copilot 订阅中还是单独收费（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。

## 9 月：按用量计费

更名文章称「Cowork、Code 和 Autopilot 这些新的长时间运行智能体能力，以及 Astra 和 Fable 等前沿模型，都运行在 UBB 上」，与 Chat/Office 中 Copilot 的用户订阅许可证（USL）相对；定价细节指向外部链接，资料库未收（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。同文介绍 Agent 365 的成本管理：管理员可通过 API 设支出策略、把额度请求导入审批流程，最终用户可在 Copilot 中查看额度使用和余额（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。iThome 同样称 Autopilot 按用量计价，企业可设支出政策与限额（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。

社区作者建议仔细做预算，因为 Autopilot 按用量计费而非固定许可（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）；dSebastien 称 UBB 价格未公布，Autopilot 是否保留 GitHub Copilot 要求未知，并明确不收录聚合站「30 美元席位加第二笔用量费用」之类的说法（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

作为对照，同属 Microsoft 365 的 Copilot Cowork 于 2026-06-16 正式可用，需 Microsoft 365 Copilot 许可证，按任务以 Copilot Credits 计费，每个 0.01 美元（[六款智能体小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。

## 资料缺口

- UBB 的单价、每个 Autopilot 的典型月用量；与 Microsoft 365 Copilot 许可证的关系。
- Autopilot 是否仍需 GitHub Copilot 席位；正式可用时间与地区。
- 9 月博文所链接的定价说明（aka.ms 链接）。

## 主要资料

- 官方：[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})、[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})、[管理员：Intune 部署]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-18-scout-admin-intune-setup" >}})（访问关口）；[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})（开放范围与计费路径）；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（私有预览与 UBB）；[Scout 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-overview" >}})。
- 媒体：[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})（GitHub 额度与价格）；[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})、[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})、[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})。
- 社区：[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})、[六款智能体小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})（Cowork 价格对照）。
