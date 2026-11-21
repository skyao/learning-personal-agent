---
title: "如何检测 Meta 的 Muse AI 智能体"
linkTitle: "检测 Muse 请求"
date: 2026-10-14
originalTitle: "How to detect Meta's Muse AI agent"
sourceUrl: "https://arcjet.com/learn/how-to-detect-metas-muse-ai-agent"
author: "Arcjet"
publisher: "Arcjet"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-21
tags: [运行环境, 安全]
products: [muse]
updatedAt: 2026-11-16
dateNote: "页面标注发表 2026-10-14、更新 2026-11-16。"
---

{{< source-info >}}

**收录说明**：直接下载；代码示例中的行号为网页渲染残留，已去掉；文末 Arcjet 产品推广一节已删去；发布方为机器人检测厂商 Arcjet，文中检测数据来自其自家平台流量，产品相关章节据此理解。

**内容摘要**：文章介绍两种验证 Muse 请求的方法：Web Bot Auth（密钥目录位于 muse.ai/.well-known/http-message-signatures-directory）与 Personal Agent Protocol（Poppy，client_id 为 https://muse.ai/poppy/agent.json），Arcjet 将验证通过的请求报告为机器人 META_MUSE，证据为 SIGNATURE，Poppy 会话的 delegated 字段为 true。未带签名或会话的 Muse 请求与普通 Chrome on Linux 请求无异：User-Agent 称 Chrome 154 on Linux（2026 年 9 月 22 日进入稳定版），无智能体名称，观测到的请求来自美国移动网络而非云厂商，须结合 SwiftShader 软件渲染与 ARM 架构客户端提示两项浏览器环境信号识别，且单凭其中一项不足以判定。Arcjet 平台流量的分析显示，Muse 浏览器典型配置为 Chrome 154、client-hint 架构 arm、经 ANGLE 的 SwiftShader 渲染、6 个逻辑 CPU、约 16 GB 设备内存（有时 8 GB）、通常 1920×1080 屏幕，作者提醒不要按 CPU 核数、内存或屏幕尺寸写规则，因为这些值并不稳定。网站可通过发布 /.well-known/poppy.json 接受 Muse 会话：Muse 经授权服务器以 OAuth 登录，Arcjet 验证 Poppy-Session 令牌后报告 delegated 为 true，但会话只证明请求来自 Muse 且代表某位用户，不表明该用户批准了具体操作，购买等不可逆操作仍需网站自行核对。作者建议把仅供真人使用的表单拒之门外并引导智能体走 API，同时保持速率限制，Arcjet 以 console.dev 订阅表单为例演示了以 detectBot 规则拒绝表单提交并返回 API 指引的做法。

**保留理由**：提供了识别与接纳 Muse 请求的完整技术方法，包括签名验证、浏览器指纹组合与 Poppy 会话处理，是已收资料中唯一系统讲解服务端如何检测 Muse 的实操指南。
