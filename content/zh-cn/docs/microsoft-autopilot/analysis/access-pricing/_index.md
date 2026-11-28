---
title: "Microsoft Autopilot：开放与价格"
linkTitle: "开放与价格"
weight: 100
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 自 2026-11-17 起以 Frontier 预览向美国部分合格客户分阶段推出，没有正式可用日期；需要 Microsoft 365 Copilot 许可证，用量另按 Copilot Credits 计费（「Copilot 许可证不含 Autopilot 用量」），必须被含 Autopilot 的支出策略覆盖；Copilot Credits 单价与最终打包方案官方称 GA 前公布。Scout 时期的 GitHub Copilot 席位与 Intune 策略前提不再出现。
---

## 概要

- 开放：2026-11-17 起在 Frontier 分阶段推出，租户启用前给管理员 24 小时通知；初期限于美国部分合格客户，针对英语优化；「正式可用时间将另行确认」（[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）。
- 前提：Microsoft 365 工作或学校账户、Microsoft 365 Copilot 许可证、加入 Frontier；默认关闭，管理员要完成三步——给用户开 Frontier、建含 Autopilot 的支出策略、在 Agents 中激活 Autopilot (Frontier)（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。Scout 时期的 GitHub Copilot 席位和 Intune 访问策略不再列入。
- 计费：按 Copilot Credits 用量计费（UBB），「Copilot 许可证不含 Autopilot 用量」；UBB 建立在每用户订阅（USL）之上，须先有 USL（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）。
- 价格没有公布：资料中没有 Copilot Credits 单价或 Autopilot 的典型消耗，产品页称最终定价与打包方案在 GA 前公布（[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。唯一的单价参照仍是社区文章所称 Cowork 每个 Copilot Credit 0.01 美元（见下文「更名前」）。
- 额度用完或不在支出策略覆盖内时，Autopilot 静默停止，不向用户解释；用户界面不显示已用或剩余额度（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。
- 2027 年 1 月底起，UBB 入口对有 Microsoft 365 Copilot 许可证的用户默认可见，无支出策略的用户看到「Request access」；这不自动启用计费（[消息中心 MC1546354]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-09-mc1546354-ubb-discoverability" >}})）。

## 2026-11：Frontier 预览，美国优先

| 日期 | 状态 | 资料 |
| --- | --- | --- |
| 2026-09-25 | 消息中心通告：Autopilot（此前称 Scout）采用用量计费，符合条件的用户需有 Microsoft 365 Copilot 许可证和支出策略；推出时间待更新 | [消息中心 MC1479277]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-mc1479277-new-copilot-autopilot" >}}) |
| 2026-09-25 | Fortune：Autopilot 将进入「限制更多的用户测试阶段」，能否广泛推出取决于测试者评价 | [Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}}) |
| 2026-10-30 | 十月汇总：Autopilot 11 月向 Frontier 推出 | [Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}}) |
| 2026-11-17 | Ignite：在 Frontier 分阶段推出，租户启用前给管理员 24 小时通知；无 GA 日期 | [消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}}) |
| 2026-11-28 | 产品页：经 Frontier 向拥有 Microsoft Copilot、Agent 365 和按用量计费策略的客户推出；最终定价 GA 前公布 | [Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}}) |

可用性初期限于美国部分符合条件的 Frontier 客户，新 Frontier 租户陆续推出（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。管理员文档提醒「仅加入 Frontier 并不会启用每一项预览功能」，预览可能不会正式发布（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。TestingCatalog 转述 Shahine 称当天以公开预览发布（[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）。UC Today 11-18 称 Autopilot 没有 GA 日期、没有公布价格，并称微软未说明是否需要 Microsoft 365 Copilot 许可证或消耗 Copilot Credits（[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})），这与同期 Learn 要求页的写法不符。

## 前提与激活

| 层面 | 要求 | 来源 |
| --- | --- | --- |
| 账户 | Microsoft 365 工作或学校账户，不支持个人账户 | [Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}}) |
| 许可证 | Microsoft 365 Copilot 许可证，并开启消费计费 | [Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}}) |
| 计划 | 加入 Frontier 预览并接受预览条款 | [管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 计费 | 被含 Autopilot 的支出策略覆盖 | [管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}}) |
| 安全能力 | Entra Agent ID、MXC（Intune Plan 1 或 E3）、审计日志为必需（见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})） | [Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}}) |
| Agent 365 | 产品页与 Redmondmag 列为前提；要求页只列为成本管理等能力的来源 | [Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}}) |

管理员激活分三步，「每一步都是必需的」：在管理中心 Copilot > 设置 > Copilot Frontier 中给用户开访问；在成本管理中建含 Autopilot 的支出策略；在 Agents > All agents 中用激活向导启用 Autopilot (Frontier)，向导依次是选择用户、支出策略、安全策略、接受权限、记忆与个性化、查看并激活（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。用户随后在 Copilot 的 Home 中创建，每人一个（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）。排查访问时检查 Frontier 分配、许可证、激活范围、支出策略与剩余额度、允许的代理和 AI 提供方设置，「不要让用户反复创建代理」（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。

## 按 Copilot Credits 计费

9 月的定价博文把 Copilot 分成两层：「日常 AI」由每用户月费的 USL 覆盖，「高级 AI」（Cowork、Code、Autopilot、前沿模型）按用量计费，用 Copilot Credits，且「UBB 建立在 USL 之上，访问这些能力需要有 USL」（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）。微软用插电式混合动力作比：USL 是电池，UBB 是油箱，部分能力先从 UBB 开始，「随着经济性允许再移入 USL」（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）；Copilot 博客也称会把越来越多的能力移入订阅许可证（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。企业客户的 UBB 在管理员创建支出策略前保持关闭，「在此之前不会产生任何计费」（[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})）。

支出策略（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）：在 Copilot > 成本管理 > 配置 > 支出策略中添加，范围为所有用户或指定组，勾选 Autopilot；可设每月限额、每用户限额或两者，加邮件提醒；付款方式为按用量付费的 Azure 订阅或预付 Copilot Credits；用户属于多项策略时以限额最高的为准。Agent 365 成本管理覆盖 Cowork、Code、Autopilot、Work IQ API 等按用量计费的服务（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。

用户一侧几乎看不到计费：使用页顶部有「Credits in use」指示器，但不显示已用或剩余数量，要问管理员；不在策略覆盖内或策略达上限时，Autopilot 不运行自动化和监控、不响应新请求，也不解释原因，自动化可能显示为已暂停（[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。

价格数字仍是空白：资料中没有 Copilot Credits 的单价，也没有 Autopilot 每任务或每月的典型消耗；产品页称「最终定价与打包方案将在正式发布（GA）前公布」（[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})），Redmondmag 同说（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。The Register 6 月就预料微软账单会上涨（[The Register]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-register-copilot-take-the-wheel" >}})）。作为对照，同期 Today Brief 的每日刷新包含在 Microsoft 365 Copilot 许可证中，Today Feed 全天更新需要 Copilot Credits（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})）。

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

## 更名前：Scout 的开放与计费（2026-06 至 2026-09）

以下为 2026-11-14 分析的内容。GitHub Copilot 席位、Intune 访问策略、声明表单等是 Scout 桌面版的前提；11 月的 Autopilot 文档改为 Microsoft 365 Copilot 许可证加支出策略。

### 开放范围的变化

| 日期 | 状态 | 资料 |
| --- | --- | --- |
| 2026-06-02 | Build 发布，以早期实验版向 Frontier 组织和一批私有预览客户提供；正式可用时间另行通知 | [Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})、[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}}) |
| 2026-06-05 | 桌面客户端开始向 Frontier 组织推出；任何人可下载，进入取决于组织管理员批准 | [TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}}) |
| 2026-09-25 | 更名 Autopilot，「将在本月底扩展到私有预览」 | [新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}}) |
| 2026-11-04 | 社区综述：私有预览自 9 月底，无正式可用日期 | [dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}}) |

Learn 文档每页标为预发布文档，称预览功能「可能不会正式发布」（[Scout 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-overview" >}})、[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})）。iThome 把 Autopilot 记为「2026 年 9 月进入私有预览版」（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})），没有提 6 月的 Frontier 实验版。

### 进入的关口

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

### 预览期的计费：GitHub 额度

管理员访问概览与消息中心通告写明 Scout 使用 GitHub 账户做令牌计费，GitHub Copilot 用于 AI 额度消耗和计费（[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})、[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})）。Semafor 报道预览期间 Scout 消耗客户 GitHub Copilot 商业版和企业版订阅的月度额度，「这两档分别为每席位每月 19 美元和 39 美元，且可购买更多额度」；Shahine 未透露正式收费方式（[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})）。Computerworld 称微软未说明 Scout 包含在 Microsoft 365 Copilot 订阅中还是单独收费（[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})）。

### 9 月：按用量计费

更名文章称「Cowork、Code 和 Autopilot 这些新的长时间运行智能体能力，以及 Astra 和 Fable 等前沿模型，都运行在 UBB 上」，与 Chat/Office 中 Copilot 的用户订阅许可证（USL）相对；定价细节指向外部链接，资料库未收（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。同文介绍 Agent 365 的成本管理：管理员可通过 API 设支出策略、把额度请求导入审批流程，最终用户可在 Copilot 中查看额度使用和余额（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。iThome 同样称 Autopilot 按用量计价，企业可设支出政策与限额（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。

社区作者建议仔细做预算，因为 Autopilot 按用量计费而非固定许可（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）；dSebastien 称 UBB 价格未公布，Autopilot 是否保留 GitHub Copilot 要求未知，并明确不收录聚合站「30 美元席位加第二笔用量费用」之类的说法（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

作为对照，同属 Microsoft 365 的 Copilot Cowork 于 2026-06-16 正式可用，需 Microsoft 365 Copilot 许可证，按任务以 Copilot Credits 计费，每个 0.01 美元（[六款智能体小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。

## 资料缺口

- Copilot Credits 单价、Autopilot 每任务或每月的典型消耗、最终打包方案（官方称 GA 前公布）。
- GA 时间；美国以外的开放计划。
- Agent 365 是否为必需前提（产品页与要求页说法不一）。
- 原 Scout 桌面版用户的迁移与计费变化。

## 主要资料

- 官方：[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})、[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})、[管理员：Intune 部署]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-18-scout-admin-intune-setup" >}})（访问关口）；[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})（开放范围与计费路径）；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（私有预览与 UBB）；[Scout 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-overview" >}})。
- 媒体：[Semafor]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-semafor-scout-openclaw" >}})（GitHub 额度与价格）；[Computerworld]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-02-computerworld-scout-autonomous-agent" >}})、[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})、[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})。
- 社区：[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})、[六款智能体小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})（Cowork 价格对照）。
- 2026-11 新增官方：[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})（前提与激活）；[Copilot 定价模式演进]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-copilot-pricing-model-evolution" >}})、[消息中心 MC1479277]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-mc1479277-new-copilot-autopilot" >}})（USL 与 UBB）；[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})（推出时间与定价状态）；[消息中心 MC1546354]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-09-mc1546354-ubb-discoverability" >}})（2027 年默认可见）；[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})。
- 2026-11 新增媒体：[Fortune]({{< relref "/docs/microsoft-autopilot/sources/media/2026-09-25-fortune-copilot-super-app" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})、[The Register]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-register-copilot-take-the-wheel" >}})、[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[The Neuron 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-neuron-ignite-autopilot-today" >}})。
- industry：[UC Today]({{< relref "/docs/industry/sources/media/2026-11-18-uctoday-autopilot-vs-personal-agents" >}})（11-18 无价格无 GA）；[六款智能体用量上限对照]({{< relref "/docs/industry/sources/media/2026-11-15-ai-agent-usage-limits-compared" >}})（消费级 Copilot 对照）。
