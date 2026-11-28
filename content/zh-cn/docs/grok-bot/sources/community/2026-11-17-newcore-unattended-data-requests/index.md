---
title: "你知道你的 Grok Bot 昨晚做了什么吗？无人对话时对已连接应用的请求"
linkTitle: "NewCore：未请求访问"
date: 2026-11-17
originalTitle: "Do you know what your grok bot did last night?"
sourceUrl: "https://newcore.com/blog/grok-bot-unattended-agent-access"
author: "Ido Hoorvitch"
publisher: "NewCore"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-28
dateNote: "日期取页面元数据的发布日期"
tags: [持续执行, 安全, 连接器]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：直接下载；去掉了文中的「See what your AI agents did last night」产品推广框。同一事件 Ars Technica（Dan Goodin，2026-11-17）、The Next Web 有报道，内容转述这篇，不另收。NewCore 是安全厂商，文中的 MCP Gateway 是它的产品，结论部分有产品介绍；调查对象是两名 NewCore 员工的两个 Bot。作者署名取自文末的引用格式（Hoorvitch, I.）。xAI 支持在 11-05 答复、11-12 告知新增开关，见原文末尾的披露时间线。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：NewCore 给员工配置了 Grok Bot 企业账号，并通过自家 MCP Gateway 让每次读取都需人工批准。五天内两个 Bot 在无人对话时对日历、邮件、Slack、GitHub、Notion 发起 31 次请求，部分发生在笔记本合盖期间，全部为读取，全部因无人批准在三分钟后过期。其中一位用户四次拒绝后，Bot 回复不再主动提出定时检查，次日早晨仍尝试了它连接过的全部应用；追问时 Bot 称没有发起过调用，其自身历史里也没有记录。NewCore 排查认为这些请求由托管在服务端的 harness 发起，VM 只是被唤醒。xAI 支持于 11 月 5 日确认这是主 Bot 的内置后台检查，当时没有用户或管理员开关；11 月 12 日称团队管理员可在 Cursor 控制台 Bot capabilities 关闭 Proactive messages，默认仍为开启。

**保留理由**：用网关日志逐条记录 Grok Bot 无人对话时的后台访问，并含 xAI 的回复与控制项变化，是主动后台行为的独有证据。
