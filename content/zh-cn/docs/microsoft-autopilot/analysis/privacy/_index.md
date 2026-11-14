---
title: "Microsoft Autopilot：隐私"
linkTitle: "隐私"
weight: 90
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-10
description: >
  Scout 的隐私关键点是数据会离开 Microsoft 365：模型调用经 GitHub Copilot 处理，可能传给第三方模型提供方，数据驻留、保留、敏感度标签强制、eDiscovery 等保护不适用，因此管理员须单独声明选择加入。官方称不用用户数据训练模型；Autopilot 的对应条款截至 11-10 未发布。
---

## 概要

- 官方写明，经 GitHub Copilot 处理时，提示、内容及相关数据可能传至第三方模型提供方，数据驻留承诺、保留策略、敏感度标签强制、eDiscovery 等 Microsoft 365 保护不适用。
- 这一数据路径是管理员必须明确声明、选择加入的原因，是 Frontier 注册之外的额外关口。
- 数据分三处存放：会话与记忆在用户的 OneDrive（租户内），自动化指令和工具输出在本机，模型处理受 GitHub 客户协议约束。
- 官方称 Scout 不使用用户数据训练 AI 模型；数据主体的访问、删除、更正、可移植性请求按微软隐私标准支持。
- 美国政府云（GCC、GCC High、DoD）和主权云不可用；没有 Scout 专属的国家或地区列表。
- 社区作者认为不能假定 EU Data Boundary 覆盖 Scout 的模型调用；Autopilot 的对应条款尚未发布。

## 数据离开 Microsoft 365

消息中心通告与管理员访问概览写明：预览体验包含 Microsoft 365 之外的数据路径（如基于 GitHub 的推理），可能涉及对客户数据的额外处理，「要求管理员明确声明」（[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})、[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})）。

负责任 AI FAQ 说得更具体：经 GitHub Copilot 处理时，提示、内容及相关数据可能传至第三方模型提供方；「某些 Microsoft 365 保护——例如数据驻留承诺、保留策略、敏感度标签强制执行、eDiscovery 和其他合规控制——不适用于该处理」（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})）。FAQ 补充这一处理受组织的 GitHub 客户协议和 GitHub 通用隐私声明约束，并适用 GitHub 的贸易管制要求（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。CIAOPS 和 dSebastien 都把这一段作为部署前必须读的条款转述（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

## 数据存放与用途

| 数据 | 存放位置 | 覆盖的条款 | 来源 |
| --- | --- | --- | --- |
| 会话、记忆 | 用户的 OneDrive | Microsoft DPA、Purview 下的 OneDrive 控制 | [负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}}) |
| 自动化指令、工具输出 | 本机设备 | 不受 Microsoft 365 DPA 覆盖 | [负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}}) |
| 本地文件 | 工作区或授权目录，留在本机 | — | [负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}}) |
| 模型处理的提示与内容 | GitHub Copilot 及第三方模型提供方 | GitHub 客户协议 | [Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}}) |
| 诊断日志 | `~/.copilot/m-diagnostics.jsonl`，仅在启用应用内诊断后存在 | — | [托管设备排障]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-01-scout-managed-troubleshoot" >}}) |

负责任 AI FAQ 称「Microsoft Scout 不使用你的数据训练 AI 模型」，支持访问、删除、更正和可移植性请求（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})）。用户可在设置中查看和删除记忆（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。

## 他人的信息

资料没有说明对方同意机制。可见的设计有：文件共享只给登录的指定人员，不建匿名或公开链接（[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})）；Heartbeat 外发的消息只用通用内容，「绝不使用私有数据」（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。Command Line 对谈中 Werner 举的难题是：不能在取消会议时把个人信息发给整串邮件的收件人（[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})）。

## 地区与监管

FAQ 写明 Scout 不适用于美国政府云（GCC、GCC High、DoD）及主权和国家云；没有 Scout 专属的支持国家或地区列表，可用性由 Frontier 注册和管理员控制决定，正式发布后可能变化（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。各模型提供方也可能限制某些地区使用（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）。

社区作者称，考虑到 GitHub Copilot 的处理路径，「我不会假定 EU Data Boundary 覆盖了 Scout 的模型调用」；Microsoft 365 保护是否适用于 Autopilot、Autopilot 的对应条款都还没有文档（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

推断：对数据驻留有要求的组织（欧盟、受监管行业），Scout 预览版的主要障碍不在 Microsoft 365 一侧，而在 GitHub 一侧的模型处理；9 月转向云端托管的 Autopilot 是否改变这条路径，是判断它能否进入这些组织的关键，目前没有资料。

## 资料缺口

- Autopilot 的隐私条款、数据驻留与保存期限。
- GitHub 一侧模型处理的保存期限，以及第三方模型提供方名单。
- 欧盟等地区的专门说明。

## 主要资料

- 官方：[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})（数据离开 Microsoft 365、存放位置、不训练）；[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})（GitHub 客户协议、地区）；[消息中心 MC1332811]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-mc1332811-introducing-scout" >}})、[管理员：访问概览]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-admin-access-overview" >}})（管理员声明）；[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[与 Microsoft 365 协作]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-work-with-microsoft-365" >}})、[托管设备排障]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-01-scout-managed-troubleshoot" >}})、[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}})。
- 社区：[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})（条款解读与欧盟顾虑）。
