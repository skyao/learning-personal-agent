---
title: "Microsoft Autopilot：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 的上下文来自用户已有权限内的 Microsoft 365 数据，首次设置时熟悉过去 30 天的邮件、会议、聊天和文件；记忆分对话、个人、工作区三类，以文件形式存在用户 OneDrive 的 lobster.repo（Git 仓库）中，可查看、修正、删除、导出，但本版本不能关闭，删除对话不删记忆。
---

## 概要

- 数据来源是用户 Microsoft 365 账户本来就能访问的 Teams、Outlook、OneDrive、SharePoint 内容，经 Microsoft IQ / Work IQ 获取，不需手动连接；Autopilot 不扩大用户的访问范围。
- 首次设置时，Autopilot 熟悉用户有权访问的过去 30 天邮件、会议、聊天和文件，期间不发送或更改任何内容；就绪后用户审阅它推断出的人员、职责和周期性承诺。
- 记忆分三类：对话记忆、关于所有者的个人记忆、工作区记忆；以 MEMORY.md、USER.md、每日笔记等文件形式存在，统一放在用户 OneDrive 中名为 `lobster.repo` 的 Git 仓库里。
- 用户可查看、修正、删除、导出记忆，但本版本记忆不能关闭，Microsoft 365 Copilot 的个性化设置不适用；删除对话不删记忆，忘记记忆也不删旧消息和导出文件。
- 官方反复声明记忆「不是完整回忆，也不是访问数据的权限」。

## 上下文：用户已有的 Microsoft 365 权限

应用卡写明 Autopilot 通过可用工具使用用户有权访问的 Teams、Outlook、OneDrive、SharePoint 信息，「不会扩大用户对 Microsoft 365 数据的访问范围」（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。Tech Community 博文与 TestingCatalog 称它建立在 Microsoft IQ 之上，不需要手动连接工具（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})）；Copilot 博客称它由 Work IQ 驱动，在现有权限范围内理解组织如何运作（[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。

社区作者在 Scout 时期就提醒，用户能触及的一切都会被智能体遍历，SharePoint 的过度共享会因此暴露（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。

## 首次设置：读过去 30 天

产品页称首次设置时，Autopilot 针对用户已有访问权限的过去 30 天邮件、会议、聊天和文件进行熟悉，了解优先级、偏好和工作风格，期间不发送或更改任何内容（[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})）；Redmondmag 所引演示说法相同（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。入门页称就绪后用户审阅它推断出的人员、职责和周期性承诺，可确认（Looks good）、修改或重置（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})）。

## 三类记忆，存在 lobster.repo

记忆页与管理员文档列出三类记忆：对话记忆、关于用户的个人记忆、针对其工作的工作区记忆（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。记忆以文件形式存在，如 MEMORY.md、USER.md、每日笔记，「文件名和可用记录在预览期间可能变化」；用户可要求它展示保存的内容及来源（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})）。

「Autopilot 把你的记忆和会话保存在 OneDrive 中一个名为 lobster.repo 的文件里」，内部是含历史版本的 Git 仓库；Windows 上的导出脚本可下载最新文件、完整 Git 历史和说明文件（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。对话和个人工作保存在用户 OneDrive，任务临时文件完成后不保留（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})）。

推断：`lobster.repo` 沿用了发布前原型 Lobster 的名字（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})、[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})），MEMORY.md、USER.md 的文件式记忆也与 OpenClaw 一类开源智能体的做法相近；文档虽不再提 OpenClaw，存储结构仍可见其来源。

## 查看、修正、删除、导出

| 操作 | 做法与限制 | 来源 |
| --- | --- | --- |
| 查看、修正、删除 | Settings > Memory >「Review what [name] knows」；或在私人对话中要求展示、修正、忘记（如「忘掉我正在做 Project X」） | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 关闭 | 本版本无法关闭；Microsoft 365 Copilot 的个性化设置不适用 | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}}) |
| 删除对话 | 列表中删除只移出列表，存储记录保留；要永久删须让它删除指定会话并确认；删除对话不删记忆 | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}}) |
| 忘记记忆 | 不删除更早的聊天消息或导出文件 | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| Teams 中改消息 | 编辑或删除消息会同步到 Autopilot 的对话副本 | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}}) |
| 导出 | 记忆或对话导出为 JSON 存到 OneDrive，保存需经批准卡；导出是快照，可能不带敏感度标签 | [Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}}) |

应用卡区分了几种记录：工作上下文、对话历史、已保存记忆、导出文件互不相同；「记忆不是完整回忆，也不是访问数据的权限」，记忆和技能指令不授予权限（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。删除的合规口径与管理员导出见[隐私]({{< relref "/docs/microsoft-autopilot/analysis/privacy" >}})。

十月汇总提到 Purview 数据生命周期管理可为 Microsoft Copilot 记忆配置保留（[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})），而管理员文档称 eDiscovery 与保留不适用于 Autopilot 会话（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。推断：Copilot 通用记忆的保留策略不覆盖 Autopilot 的 lobster.repo。

## 「也需要忘掉」

发布前的官方对谈中，Jakob Werner 描述分层记忆：常用的相关性上升，不用的随时间消退，而不是无限增长的日记；Omar Shahine 以孩子年龄不更新为例，说明事实需随时间变化（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。这是设计理念，现有文档没有说明消退机制是否实现。

## 资料缺口

- 记忆的数量上限、消退机制是否实现。
- 30 天初始熟悉读取的具体范围，是否可排除某些邮箱或站点。
- lobster.repo 在用户离职、许可证收回后的处理。
- Microsoft IQ / Work IQ 为 Autopilot 索引的范围与刷新频率。

## 主要资料

- 官方：[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})（三类记忆、lobster.repo、删除与导出）；[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[使用 Autopilot]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-use" >}})、[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})（不可关闭、记忆不是权限）；[Autopilot 产品页]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-28-autopilot-product-page" >}})、[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})（30 天初始熟悉、就绪审阅）；[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})；[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})（遗忘的设计理念）。
- 媒体：[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})、[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})。
- 社区：[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})。
