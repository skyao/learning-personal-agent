---
title: "Microsoft Autopilot：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 保存对话、个人、工作区三类记忆，以 MEMORY.md、USER.md 等文件形式存在用户 OneDrive 的 lobster.repo（Git 仓库）中；首次设置时熟悉过去 30 天可访问的邮件、会议、聊天和文件；记忆可查看、修正、删除、导出，但本版本不能关闭，删除对话不删记忆。上下文来源仍是用户已有权限内的 Microsoft 365 数据。
---

## 概要

- Autopilot 保存三类记忆：对话记忆、关于所有者的个人记忆、为其工作的工作区记忆；记忆以文件形式存在（如 MEMORY.md、USER.md、每日笔记），文件名在预览期可能变化（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。
- 记忆和会话存在用户 OneDrive 中一个名为 `lobster.repo` 的文件里，内部是带历史版本的 Git 仓库，可用 Windows 上的脚本导出完整副本（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。延续了 Scout 存 OneDrive 的做法。
- 首次设置时，Autopilot 熟悉用户有权访问的过去 30 天邮件、会议、聊天和文件，不发送或更改任何内容（[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。
- 用户可在 Settings > Memory 查看、修正、删除，也可在私人对话中要求忘记或导出为 JSON；但本版本记忆无法关闭，Microsoft 365 Copilot 的个性化设置不适用，删除对话不删记忆，忘记记忆也不删旧消息和导出文件（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。
- 官方反复声明记忆不是完整回忆、也不是访问数据的权限；Autopilot 不扩大用户对 Microsoft 365 数据的访问范围（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

## 2026-11：三类记忆，存在 lobster.repo

记忆页与管理员文档列出三类记忆：对话记忆、关于用户的个人记忆、针对其工作的工作区记忆（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。记忆以文件形式存在，如 MEMORY.md、USER.md、每日笔记，「文件名和可用记录在预览期间可能变化」；用户可要求它展示保存的内容及来源（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})）。

存放位置：「Autopilot 把你的记忆和会话保存在 OneDrive 中一个名为 lobster.repo 的文件里」，内部是 Git 仓库，含历史版本（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})）。导出脚本（Windows 上的 Lobster-Export.zip）生成最新文件、完整 Git 历史和说明文件（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})）；管理员版导出见[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})。FAQ 写明对话和个人工作保存在用户 OneDrive，任务临时文件完成后不保留（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。

推断：`lobster.repo` 与发布前原型 Lobster 同名，MEMORY.md、USER.md 的文件式记忆也与 OpenClaw 一类开源智能体的做法相近；更名后的文档虽不提 OpenClaw，存储结构仍可见其来源。

## 首次设置读过去 30 天

产品页称首次设置时，Autopilot 针对用户已有访问权限的过去 30 天邮件、会议、聊天和文件进行熟悉，了解优先级、偏好和工作风格，期间不发送或更改任何内容（[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})）；Redmondmag 所引演示说法相同（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。入门页说就绪后用户审阅它推断出的人员、职责和周期性承诺，可确认、修改或重置（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})）。Tech Community 博文与 TestingCatalog 称它建立在 Microsoft IQ 之上，不需要手动连接工具（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）。

数据范围仍以用户权限为界：Autopilot 通过可用工具使用用户有权访问的 Teams、Outlook、OneDrive、SharePoint 信息，「不会扩大用户对 Microsoft 365 数据的访问范围」（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

## 查看、修正、删除、导出

| 操作 | 做法与限制 | 来源 |
| --- | --- | --- |
| 查看、修正、删除 | Settings > Memory >「Review what [name] knows」；或在私人对话中要求展示、修正、忘记（如「忘掉我正在做 Project X」） | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 关闭 | 本版本无法关闭；Microsoft 365 Copilot 的个性化设置不适用 | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}}) |
| 删除对话 | 列表中删除只移出列表，存储记录保留，要永久删须让它删除指定会话并确认；删除对话不删记忆 | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}}) |
| 忘记记忆 | 不删除更早的聊天消息或导出文件 | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| Teams 中改消息 | 编辑或删除消息会同步到 Autopilot 的对话副本 | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 导出 | 记忆或对话导出为 JSON 存到 OneDrive，保存需经批准卡；导出是快照，可能不带敏感度标签 | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}}) |

应用卡区分了几种记录：工作上下文、对话历史、已保存记忆、导出文件互不相同；「记忆不是完整回忆，也不是访问数据的权限」，记忆和技能指令不授予权限（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

十月汇总提到 Purview 数据生命周期管理可为 Microsoft Copilot 记忆配置保留（[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})），而管理员文档称 eDiscovery 与保留不适用于 Autopilot 会话（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。推断：Copilot 通用记忆的保留策略不覆盖 Autopilot 的 lobster.repo。

## 更名前：Scout 的记忆（2026-06 至 2026-09）

以下为 2026-11-14 分析的内容。Scout 的会话与记忆同样存在 OneDrive，Autopilot 沿用了这一点，并增加了不可关闭、三类记忆、30 天初始熟悉等新说明。

### 数据来源：用户已有的 Microsoft 365 权限

入门页说明，在设置中「Sign in to Microsoft 365」后，Scout 可访问邮件、日历、Teams、OneDrive 等，WorkIQ connectivity 默认开启（[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})）。「与 Microsoft 365 协作」页列出完整范围，并说明范围受已连接账户的访问权限限制（[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})）。官方称 Work IQ 是 Scout 的上下文引擎，学习用户工作方式中的人、文件和模式（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[Build 直播]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-build-live-scout" >}})）。9 月更名后的 Autopilot 改称基于 Microsoft IQ，在租户内拥有自己的记忆（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。

社区作者提醒，用户能触及的一切都会被智能体遍历，SharePoint 的过度共享会因此暴露（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。

### 记忆如何形成、存放与删除

使用指南写明（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）：

- 记忆跨会话持久保存，Scout 在工作时主动保存重要信息，「你无需开口要求」。
- 每条记忆记录来源：会话推断、导入或外部；外部来源（邮件、网页消息）的记忆「当作数据而非指令」，据此行动前与用户确认。
- 用户可在设置的记忆部分查看并删除记忆。

会话历史可搜索（如「我上周做了什么」），可恢复旧对话；7 月起会话历史按设备存放在 OneDrive，「每台设备保留自己的对话」（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})）。长对话可按需压缩，上下文窗口大小可选到「Max」，每个自动化可单独设置（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。

负责任 AI FAQ 说明存放位置：会话和记忆数据在用户的 OneDrive，受 Microsoft DPA 与 Purview 下的 OneDrive 控制覆盖；自动化指令和工具输出存在本机，不受该 DPA 覆盖（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})）。

会话还会跟踪 MIP 敏感度标签：读到带标签内容后，会话的敏感度级别升高并在界面显示（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})，见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})）。

### 「也需要忘掉」

Command Line 对谈中，Jakob Werner 描述分层记忆：常用的相关性上升，不用的随时间消退，而不是无限增长的日记；Omar Shahine 以 ChatGPT 记忆里孩子年龄不更新为例，说明事实需随时间变化（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。这是设计理念的表述，文档没有说明消退的具体机制。

Build 时 Nadella 称用户「完全掌控其上下文和记忆」（[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})）。The Neuron 记录的演示中，Scout 识别日历冲突后询问是移动会议还是保护个人时间，并记住该偏好（[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})）。

### 跨设备

工作区 skill 通过云同步跨设备同步，其余 skill 留在本机（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）；会话历史各设备分开。社区作者 6 月（0.22 版）报告个性设置尚不能同步、重装后部分设置不保留（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。

## 资料缺口

- 记忆的数量上限、消退机制（Scout 时期访谈提过「遗忘」）是否实现。
- 30 天初始熟悉读取了哪些具体数据、是否可选择排除。
- lobster.repo 在用户离职、许可证收回后的处理；管理员不能代删时的实际流程。
- Microsoft IQ / Work IQ 为 Autopilot 索引的范围与刷新频率。

## 主要资料

- 官方：[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})（记忆来源标注、查看删除）；[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})（存放位置）；[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})、[入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-get-started" >}})（数据范围与授权）；[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})（遗忘的设计理念）；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})。
- 媒体：[TechRadar]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-03-techradar-scout-first-autopilot" >}})、[The Neuron]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-08-neuron-scout-openclaw-moment" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})、[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})。
- 2026-11 新增官方：[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})（三类记忆、lobster.repo、删除与导出）；[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})（不可关闭、记忆不是权限）；[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})（30 天初始熟悉、就绪审阅）；[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})。
- 2026-11 新增媒体：[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})、[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})。
