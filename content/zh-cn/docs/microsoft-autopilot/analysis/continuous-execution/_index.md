---
title: "Microsoft Autopilot：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-14
sourcesUntil: 2026-11-10
description: >
  Scout 的持续执行有两种机制：按 15 分钟到 2 小时间隔运行的 Heartbeat，和按时间表或条件触发的 Automations；后台权限比交互式对话更严，桌面版设备休眠时暂停。9 月的 Autopilot 改为「给名字、角色、目标」的长期角色。
---

## 概要

- Heartbeat 是自主后台模式，按 15 分钟、30 分钟、1 小时或 2 小时的间隔运行用户写好的提示词，可限定工作日与工作时间。
- Automations 是独立任务，按时间表或条件触发，可设为一次性；可暂停、编辑、查看历史，也能从 GitHub 仓库导入定义。
- 后台运行使用比交互式对话更严的权限：Heartbeat 外发消息只用通用内容，通常需批准的操作会被跳过。管理员可整体禁用两者。
- 桌面版依赖设备在线，休眠时自动化暂停（社区实测）。
- 9 月更名后，官方把 Autopilot 写成长期持有角色与目标的「数字队友」，监视频道、跟进线程、数天后重拾项目；这种形态没有文档。

## Heartbeat：定期检入

FAQ 与使用指南给出设置项：提示词（每次检入做什么，如分拣收件箱、检查日程冲突）、间隔（15 分钟、30 分钟、1 小时或 2 小时）、工作日和工作时间（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})、[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。Heartbeat 面板显示最近的检入日志。

Heartbeat 有独立的权限策略，通常更严：外发的邮件、Teams 消息「只使用通用内容——绝不使用私有数据」；暂定的日历事件视为忙碌；通常需批准的操作在 Heartbeat 下被跳过。用户可在面板中自定义这套权限（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。负责任 AI FAQ 建议把后台权限与交互权限分开配置（[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})）。

## Automations：时间表、条件、一次性

Automations 的触发类型是 Schedule 或 Condition（条件为真时触发，需设检查频率），可勾选 One-shot（运行一次后停用），并单独设置推理强度与上下文大小；可启用/禁用、编辑、查看历史、删除，并可从 GitHub 仓库导入定义（[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})）。8 月更新加入了自动化运行时会话过期的就地恢复（[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})）。TestingCatalog 称其为内置的「类似 Zapier 的编排」（[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})）。

管理员可用策略 `DisableHeartbeat`、`DisableWorkflows` 分别禁用两者（[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})）。社区作者建议把 heartbeat 和自动化权限严格收紧，因为它们在无人注视时运行（[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})）。

## 实际用例

| 来源 | 用例 | 性质 |
| --- | --- | --- |
| [Build 直播]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-build-live-scout" >}}) | 每天早上监控 GitHub 讨论，找出各应用功能负责人并开 Teams 聊天跟踪；设置外出回复时自行推算日期、检查冲突、创建时间块 | 微软员工自述 |
| [Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}}) | 每天四次检查是否还有需要关注的事；CRM 管道检查（浏览器导航、检查商机、导出到 SharePoint、发 Teams 消息）端到端完成 | 社区实测 |
| [Scout 发布稿]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-introducing-microsoft-scout" >}})、[OpenClaw 进入企业]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-openclaw-goes-enterprise-scout" >}}) | 跨时区协调会议、识别交付物并在日历预留时间、发现停滞的决策 | 官方宣称 |

## 桌面版的限制

社区作者指出，桌面版要求机器保持运行，设备休眠时自动化暂停；云端版当时为有限访问，可不依赖设备运行（[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})）。FAQ 说明连接中断时工作暂停、恢复后继续（[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})）；社区综述把「连接断开会使工作中断」列为已记录的局限（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

## 9 月：从定时任务到长期角色

更名文章称：给 Autopilot 一个名字、角色和目标，它监视频道、跟进线程、运行周期性工作，「在数天后重新拾起一个项目，无需等待提示」；示例是搭建并管理完整的供应商评审流程。「你设定目标和边界；Autopilot 处理其余的事」（[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})）。同文中主动起草、提出日程变更的 Today 属于 Copilot Home，不是 Autopilot。iThome 称其触发方式为文字、@mention 或预设任务（[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。社区作者的区分是：Cowork 端到端完成一项任务后交回，Autopilot 长期持有一个角色和一个目标（[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})）。

发布前，GeekWire 转述 Shahine 的设想：Lobster 提出可采取的行动方案并等待用户批准，而非持续被提示（[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})）。

推断：Scout 的持续执行是「用户写提示词 + 定时器」，主动性的边界由权限策略划定；Autopilot 的宣传转向「目标驱动」，但如何控制打扰频率、任务数量与时长上限，资料都没有给出。

## 资料缺口

- 自动化数量、运行时长、并发上限；失败重试策略。
- Autopilot 云端版的触发机制和主动联系用户的频率控制。
- 长期（数周以上）运行的稳定性报告。

## 主要资料

- 官方：[使用 Scout]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-use" >}})、[Scout 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-faq" >}})（Heartbeat 与 Automations 设置）；[负责任 AI 常见问题]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-responsible-ai-faq" >}})、[组策略管理]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-manage-group-policy" >}})（后台权限与禁用）；[新功能]({{< relref "/docs/microsoft-autopilot/sources/official/2026-08-21-scout-whats-new" >}})；[Build 直播]({{< relref "/docs/microsoft-autopilot/sources/official/2026-06-02-build-live-scout" >}})；[新版 Copilot 与 Autopilot 发布]({{< relref "/docs/microsoft-autopilot/sources/official/2026-09-25-new-copilot-home-code-autopilot" >}})（长期角色）。
- 媒体：[TestingCatalog]({{< relref "/docs/microsoft-autopilot/sources/media/2026-06-05-testingcatalog-scout-frontier" >}})、[GeekWire 05-04]({{< relref "/docs/microsoft-autopilot/sources/media/2026-05-04-geekwire-openclaw-team-personal-assistant" >}})。
- 社区：[Copilot at Work]({{< relref "/docs/microsoft-autopilot/sources/community/2026-06-06-copilotatwork-scout-not-just-assistant" >}})（用例与休眠限制）；[CIAOPS]({{< relref "/docs/microsoft-autopilot/sources/community/2026-10-27-ciaops-scout-now-autopilot" >}})、[dSebastien]({{< relref "/docs/microsoft-autopilot/sources/community/2026-11-04-dsebastien-microsoft-autopilot" >}})。
- industry：[iThome 五大主动型 Agent 比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
