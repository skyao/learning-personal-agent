---
title: "Microsoft Autopilot：开放与价格"
linkTitle: "开放与价格"
weight: 100
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 自 2026-11-17 起以 Frontier 预览向美国部分合格客户分阶段推出，没有正式可用日期；需要 Microsoft 365 Copilot 许可证，用量另按 Copilot Credits 计费（「Copilot 许可证不含 Autopilot 用量」），必须被含 Autopilot 的支出策略覆盖；Copilot Credits 单价与最终打包方案官方称 GA 前公布。
---

## 概要

- 开放：2026-11-17 起在 Frontier 分阶段推出，租户启用前给管理员 24 小时通知；初期限于美国部分合格客户，针对英语优化；「正式可用时间将另行确认」。
- 前提：Microsoft 365 工作或学校账户、Microsoft 365 Copilot 许可证、加入 Frontier；默认关闭，管理员须完成三步：给用户开 Frontier、建含 Autopilot 的支出策略、在 Agents 中激活 Autopilot (Frontier)。
- 计费：按 Copilot Credits 用量计费（UBB），「Copilot 许可证不含 Autopilot 用量」；UBB 建立在每用户订阅（USL）之上。
- 价格没有公布：资料中没有 Copilot Credits 单价或 Autopilot 的典型消耗，产品页称最终定价与打包方案在 GA 前公布。
- 用户一侧看不到余额；额度用完或不在支出策略覆盖内时，Autopilot 静默停止，不解释原因。
- 2027 年 1 月底起，UBB 入口对有 Microsoft 365 Copilot 许可证的用户默认可见，无支出策略的用户看到「Request access」；这不自动启用计费。

## 开放范围与节奏

| 日期 | 状态 | 资料 |
| --- | --- | --- |
| 2026-06-02 | 前身 Scout 以早期实验版向 Frontier 组织和一批私有预览客户提供 | [Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}}) |
| 2026-09-25 | 更名 Autopilot，「将在本月底扩展到私有预览」；消息中心通告称其采用用量计费，需 Microsoft 365 Copilot 许可证和支出策略 | [新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})、[消息中心 MC1479277]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-mc1479277-new-copilot-autopilot" >}}) |
| 2026-09-25 | Fortune：Autopilot 进入「限制更多的用户测试阶段」，能否广泛推出取决于测试者评价 | [Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}}) |
| 2026-10-30 | 十月汇总：Autopilot 11 月向 Frontier 推出 | [Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}}) |
| 2026-11-17 | Ignite：在 Frontier 分阶段推出，租户启用前给管理员 24 小时通知；无 GA 日期 | [消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}}) |
| 2026-11-28 | 产品页：经 Frontier 向拥有 Microsoft Copilot、Agent 365 和按用量计费策略的客户推出；最终定价 GA 前公布 | [Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}}) |

可用性初期限于美国部分符合条件的 Frontier 客户，新 Frontier 租户陆续推出（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。管理员文档提醒「仅加入 Frontier 并不会启用每一项预览功能」，预览功能可能不会正式发布（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。TestingCatalog 转述 Shahine 称当天以公开预览发布（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）。UC Today 11-18 称 Autopilot 没有 GA 日期、没有公布价格，并称微软未说明是否需要 Microsoft 365 Copilot 许可证或消耗 Copilot Credits（[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})），这与同期的 Learn 要求页不符。

## 前提与激活

| 层面 | 要求 | 来源 |
| --- | --- | --- |
| 账户 | Microsoft 365 工作或学校账户，不支持个人账户 | [Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}}) |
| 许可证 | Microsoft 365 Copilot 许可证，并开启消费计费 | [Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}}) |
| 计划 | 加入 Frontier 预览并接受预览条款 | [管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 计费 | 被含 Autopilot 的支出策略覆盖 | [管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}}) |
| 安全能力 | Entra Agent ID、MXC（Intune Plan 1 或 E3）、审计日志为必需，见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}}) | [Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}}) |
| Agent 365 | 产品页与 Redmondmag 列为前提；要求页只列为成本管理等能力的来源 | [Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}}) |

管理员激活分三步，「每一步都是必需的」：在管理中心 Copilot > 设置 > Copilot Frontier 中给用户开访问；在成本管理中建含 Autopilot 的支出策略；在 Agents > All agents 中用激活向导启用 Autopilot (Frontier)，向导依次为选择用户、支出策略、安全策略、接受权限、记忆与个性化、查看并激活（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。用户随后在 Copilot 的 Home 中创建，每人一个（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）。排查访问时检查 Frontier 分配、许可证、激活范围、支出策略与剩余额度、允许的代理和 AI 提供方设置，「不要让用户反复创建代理」（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。

## 按 Copilot Credits 计费

9 月的定价博文把 Copilot 分成两层：「日常 AI」由每用户月费的 USL 覆盖，「高级 AI」（Cowork、Code、Autopilot、前沿模型）按用量计费，用 Copilot Credits，且「UBB 建立在 USL 之上，访问这些能力需要有 USL」（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）。微软用插电式混合动力作比：USL 是电池，UBB 是油箱，部分能力先从 UBB 开始，「随着经济性允许再移入 USL」（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）；Copilot 博客也称会把越来越多的能力移入订阅许可证（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。企业客户的 UBB 在管理员创建支出策略前保持关闭，「在此之前不会产生任何计费」（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）。

支出策略在 Copilot > 成本管理 > 配置 > 支出策略中添加，范围为所有用户或指定组，勾选 Autopilot；可设每月限额、每用户限额或两者，加邮件提醒；付款方式为按用量付费的 Azure 订阅或预付 Copilot Credits；用户属于多项策略时以限额最高的为准（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。Agent 365 成本管理覆盖 Cowork、Code、Autopilot、Work IQ API 等按用量计费的服务（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。

用户一侧：使用页顶部有「Credits in use」指示器，但不显示已用或剩余数量，要问管理员；不在策略覆盖内或策略达上限时，Autopilot 不运行自动化和监控、不响应新请求，也不解释原因，自动化可能显示为已暂停（[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。

价格数字是空白：资料中没有 Copilot Credits 的单价，也没有 Autopilot 每任务或每月的典型消耗；产品页称「最终定价与打包方案将在正式发布（GA）前公布」（[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})），Redmondmag 同说（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。唯一的单价参照是社区文章所称同属 Microsoft 365 的 Copilot Cowork 每个 Copilot Credit 0.01 美元（[六款智能体小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。The Register 6 月预料微软账单会上涨（[The Register]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-register-copilot-take-the-wheel" >}})）；社区作者建议按用量计费仔细做预算（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。作为对照，同期 Today Brief 的每日刷新包含在 Microsoft 365 Copilot 许可证中，Today Feed 全天更新需要 Copilot Credits（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})）。

早期的 Scout 预览走另一套计费：令牌用量经 GitHub 账户计费，据 Semafor 从 GitHub Copilot 商业版（每席位每月 19 美元）和企业版（39 美元）的额度中扣除，访问还需 GitHub Copilot 席位与 Intune 策略（[Scout 管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})、[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})）；11 月的 Autopilot 前提不再提 GitHub。

## 2027 年 1 月起默认可见

消息中心 MC1546354（2026-11-09）宣布，Cowork、Code、Autopilot 等 UBB 入口将对有 Microsoft 365 Copilot 许可证的用户默认可见，没有适用支出策略的用户看到「Request access」或「Learn more」（[消息中心 MC1546354]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-09-mc1546354-ubb-discoverability" >}})）：

| 时间 | 变化 |
| --- | --- |
| 2026 年 11 月中旬 | 开放新管理设置「Access requests to usage-based billing experiences」 |
| 2026 年 12 月中旬 | 可加自定义指引 URL |
| 2027 年 1 月底 | 强制执行，退役旧设置；延期发布的客户为 2027 年 2 月底 |

通告写明「这一变更不会自动启用用量计费体验，也不会启动计费」，管理员可配置谁有资格请求访问（[消息中心 MC1546354]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-09-mc1546354-ubb-discoverability" >}})）。

## 与消费级 Copilot 的区别

All Things Muse 的用量对照只涉及消费级 Microsoft 365 套餐：Copilot 没有消费级的定时智能体功能，Premium（19.99 美元/月起）有 Researcher 和 Analyst 智能体，用 Standard/More/Extensive 等标签而不是数字计量，作者称之为「最不透明的定价」（[六款智能体用量上限对照]({{< relref "/docs/industry/sources/media/2026-11-15-ai-agent-usage-limits-compared" >}})）。这与企业版 Autopilot 不是同一商品。

## 资料缺口

- Copilot Credits 单价、Autopilot 每任务或每月的典型消耗、最终打包方案。
- GA 时间；美国以外的开放计划。
- Agent 365 是否为必需前提（产品页与要求页说法不一）。

## 主要资料

- 官方：[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})（前提与激活）；[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[消息中心 MC1479277]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-mc1479277-new-copilot-autopilot" >}})（USL 与 UBB）；[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（推出节奏与定价状态）；[消息中心 MC1546354]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-09-mc1546354-ubb-discoverability" >}})（2027 年默认可见）；[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})；[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})、[Scout 管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})（早期预览）。
- 媒体：[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})、[The Register]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-register-copilot-take-the-wheel" >}})、[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})、[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})。
- 社区：[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})。
- industry：[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})（11-18 无价格无 GA）；[六款智能体小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})（Cowork 单价）；[六款智能体用量上限对照]({{< relref "/docs/industry/sources/media/2026-11-15-ai-agent-usage-limits-compared" >}})（消费级 Copilot 对照）。
