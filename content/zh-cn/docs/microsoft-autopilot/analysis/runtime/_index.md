---
title: "Microsoft Autopilot：运行环境"
linkTitle: "运行环境"
weight: 10
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  截至 2026-11-28 的资料，Autopilot 运行在微软托管的云环境中，每个用户一个，有自己的远程计算机和工作区，与用户设备分离、无法访问本地文件夹或应用；唯一的本机触点是启用后借用户的 Edge 浏览器操作已登录站点。云端计算机的规格和底层基础设施没有文档。
---

## 概要

- Autopilot 是 Microsoft Copilot 中的常驻云端智能体，有自己的身份、记忆、远程计算机和工作区，在微软管理的云环境中运行；用户关掉应用、合上笔记本或关机后，工作照常继续。
- 云端计算机与本地设备分离，「无法访问本地文件夹或应用」，也无需在设备上安装任何代理。
- 唯一触及用户设备的是 Edge 浏览器模式：组织启用后，只在所有者的私人对话中、只在相关标签页内操作已登录站点，例程不用浏览器。
- 每人一个 Autopilot，创建后自动预配 10 到 30 分钟；工作区跨会话保留上下文，任务临时文件完成后不保留。
- 规格、持久化、并发、超时都没有文档；它与 Copilot Managed Runtime、Windows 365 for Agents 的关系也没有说明。MXC 隔离执行环境被列为必需能力，Redmondmag 称会话可设为在受管设备本地运行，两者与「无法访问本地」如何对应不清楚。

## 每人一台托管的云端计算机

Ignite 当天的消息中心通告把 Autopilot 定义为「常驻的、基于云的个人智能体」，有自己的账户与身份、存储和邮箱，「以及自己的远程计算机」（[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})）。FAQ 写明它在微软管理的云环境中运行，关闭 Copilot 应用、笔记本合上或关机都继续工作；工作区跨会话保留上下文，任务期间的临时文件完成后不保留（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})）。概述页称设备关机时仍能运行计划中的工作，前提是访问权限、审批和服务可用（[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})）。管理员文档称它「作为 Microsoft Copilot 的一部分在云端运行」，管理员可在 Agents > Autopilot (Frontier) > Instances 查看组织内的实例（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})）。

Tech Community 博文、TestingCatalog 和 Redmondmag 所引的 Microsoft Mechanics 演示都用「合上笔记本也继续工作」描述这一点（[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})、[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。应用卡把 Workspace 定义为可跨会话保留上下文的云端工作环境，独立于本地设备和交付物的发布位置；后台运行依赖 Microsoft 365 应用和所连服务的可用性，不保证不中断（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})）。

创建流程：在 Copilot 的 Home 中选名称和外观，审阅建议的起始例程，随后自动预配，需要 10 到 30 分钟，就绪时发邮件和 Teams 通知（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})）。每个启用的用户只能有一个（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）。设置标签页可看到它的名称、外观、记忆和「计算机」（[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})）。

## 不碰本机，只借 Edge

应用卡、要求页、FAQ 和 Edge 页都写明 Autopilot 无法访问用户设备上的本地文件夹或应用（[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})、[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})）。要求页称使用 Autopilot 无需在设备上单独安装代理，并提醒「不要把早期桌面预览的说明当作云端体验的设置要求」（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）——2026-06 至 09 的 Scout 预览是 Windows/Mac 桌面应用（[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})、[Scout 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-overview" >}})）。

十月新功能汇总另称 Autopilot 能「跨用户的本地文件和它自己的远程计算机运行」（[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})），与 11-17 之后的文档不一致；该页为第 5 版（11-13 修改），资料没有说明这一句是否是旧口径。

Edge 模式（[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})）：

| 项目 | 说明 |
| --- | --- |
| 前提 | 组织启用；Edge 已打开、以工作账户登录并连接 Autopilot；逐步推出 |
| 范围 | 只限所有者的私人对话（Copilot 或一对一 Teams 聊天）；只在对话涉及的标签页内操作，看不到其他标签页 |
| 不用浏览器 | 例程、共享对话（[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}}) 同说） |
| 数据 | 密码和 cookie 留在 Edge；读到的页面内容送云端模型处理 |
| 须批准的步骤 | 更改账户、结账付款、输入银行卡、永久删除、向外部站点提交个人信息（见[安全]({{< relref "/docs/microsoft-autopilot/analysis/security" >}})） |

Redmondmag 报道演示中 Autopilot 从收件箱收集收据、在浏览器里的业务应用中填费用报告并在提交前请求批准（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})）。

## 本地执行的两处线索

要求页把「隔离执行环境 Microsoft local (MXC)」（需 Intune Plan 1 或 Microsoft 365 E3）列为必需的安全能力（[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})）；新闻手册和 Copilot 博客把 MXC 描述为隔离设备上本地智能体的机制（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})）。Redmondmag 称 IT 可以决定智能体会话「仅限于云端，还是允许在受管设备上本地运行」（[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})），Learn 文档中没有这一设置。

推断：这两处说明 Autopilot 可能保留某种受管设备上的本地执行选项；但用户文档一致写「无法访问本地文件夹或应用」，资料不足以判断两者如何对应。

## 底层基础设施没有说明

新闻手册宣布 Copilot Managed Runtime 正式可用，托管 Copilot Code、Cowork、Copilot Studio 中创建的应用，列举对象中没有 Autopilot；Windows 365 for Agents 将在 Frontier 支持持久云 PC，用于「始终在线的个人智能体」，同样没有点名 Autopilot（[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})）。管理员与记忆文档的导出排障提到脚本会临时修改 hosts 文件中的 `cowork.local.microsoft.com` 条目（[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})）。

推断：`cowork.local` 域名提示 Autopilot 与 Cowork 可能共用部分底层服务；Managed Runtime 或 Windows 365 for Agents 是否就是它的「远程计算机」，资料没有说明，不能据此认定。

开源基础方面，OpenClaw 博客称 Autopilot 以 OpenClaw 为基础，并列出微软的上游贡献，如 MXC 沙箱后端、排队的用户请求优先于后台任务（[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})）；微软 6 月称 Scout 建立在 OpenClaw 之上（[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})），11 月的 Autopilot 文档不再提 OpenClaw（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}}) 在 11-04 已指出这一点）。存储文件名 `lobster.repo` 沿用了原型 Lobster 的名字（[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})）。

## 资料缺口

- 云端计算机的规格、持久化、休眠与回收、并发上限、超时；是否基于 Managed Runtime 或 Windows 365 for Agents。
- MXC 在 Autopilot 中隔离的是什么；「受管设备本地运行」的设置是否存在。
- 十月汇总「跨本地文件运行」一句的来历。
- 云端算力如何计入 Copilot Credits。

## 主要资料

- 官方：[消息中心 MC1557730]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-mc1557730-autopilot-frontier" >}})、[Autopilot 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-faq" >}})、[Autopilot 概述]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-24-autopilot-overview" >}})、[管理员配置]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-admin-configure" >}})、[应用卡]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-application-card" >}})（云端计算机与工作区）；[Autopilot 要求]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-requirements" >}})（无需安装、不访问本地、MXC）；[Edge 浏览器]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-edge" >}})（浏览器模式）；[Autopilot 入门]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-get-started" >}})（创建与预配）；[Copilot 十月新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-10-30-whats-new-copilot-october-2026" >}})（「跨本地文件」的说法）；[Ignite 新闻手册]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-ignite-2026-book-of-news" >}})、[Copilot 博客 Ignite 2026]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-copilot-at-ignite-2026" >}})（Managed Runtime、Windows 365 for Agents、MXC）；[Autopilot 记忆]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-memory" >}})；[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})、[Scout 概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-overview" >}})（Scout 桌面预览）；[Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})（OpenClaw 基础）。
- 媒体：[TestingCatalog 11-17]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-17-testingcatalog-autopilot-launch" >}})、[Redmondmag]({{< relref "/docs/microsoft-autopilot/sources/media/2026-11-20-redmondmag-autopilot-rollout" >}})（本地运行设置、演示）。
- 社区：[OpenClaw 贡献说明]({{< relref "/docs/microsoft-autopilot/sources/community/2026-09-25-openclaw-autopilot-contributions" >}})（上游贡献）、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})、[Tech Community 博文]({{< relref "/docs/microsoft-autopilot/sources/official/2026-11-17-autopilot-trusted-personal-teammate" >}})。
