---
title: "OpenClaw 走向企业：Scout 从个人项目到企业级个人智能体"
linkTitle: "Command Line 对谈"
date: 2026-06-02
originalTitle: "Microsoft Scout: From personal project to enterprise-ready personal agent"
sourceUrl: "https://commandline.microsoft.com/project-lobster-openclaw-personal-ai-assistant-enterprise-secure/"
author: "Lisa Brown Jaloza"
publisher: "Microsoft（Command Line）"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-10
tags: [发布, 记忆与上下文, 安全]
products: [microsoft-autopilot]
updatedAt: "2026-06-03"
---

{{< source-info >}}

**收录说明**：微软官方博客 Command Line 的文章，记录 Omar Shahine 与 Jakob Werner 关于 Project Lobster 与 Microsoft Scout 的对谈。直接下载；删去了分享按钮和文末「Next Stop」推荐阅读；页面内嵌的 YouTube 视频写为占位行，位置在引出对谈的段落之后。待翻译。

**内容摘要**：Command Line 刊出 Omar Shahine 与 Jakob Werner 的对谈（2026.06.02）：Shahine 业余用 OpenClaw 做了个人助手 Lobster，它有自己的 Apple ID 和邮箱，最初拆成三个智能体，八周后增至九个常驻智能体；向 Microsoft AI Accelerator 小组演示后，他转任 CVP，负责「Project Lobster」。Werner 的桌面端智能体在内部称为「Clawpilot」，几周内被数千名微软员工下载，后与 Shahine 的团队合流。企业化方面，文中称所有软件包经由经过签名的微软供应链引入，每次工具调用、模型请求和网络跳转都由零信任运行时中介，智能体容器被视为不受信任，并由 Agent 365 提供统一控制平面、Purview 提供合规与 DLP 信号。记忆方面，Shahine 说：「就像它需要记住一些事情，它也需要忘掉一些事情。」Werner 则设计了分层记忆，不常用的内容会随时间消退，常用的则相关性上升。

**保留理由**：这是产品团队两位核心成员的第一手对谈，交代了 Scout 的起源（Lobster 与 Clawpilot 合流）、团队工作方式，以及记忆设计和企业安全取舍的思路，是其他材料没有的内部视角。
