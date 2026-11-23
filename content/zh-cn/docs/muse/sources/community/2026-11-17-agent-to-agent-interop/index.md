---
title: "智能体即将开始互相对话，先问清对面是谁"
linkTitle: "智能体间互操作"
date: 2026-11-17
originalTitle: "Your Agent Is About to Start Talking to Other Agents. Ask Who Is on the Other End"
sourceUrl: "https://aihomebuilding.com/stories/muse-agent-to-agent-mcp-a2a-2026"
author: "Jake Kowalski"
publisher: "AI Home Building"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-18
tags: [连接器, 安全]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载后用 extract.py 抽取全文；首图为装饰性照片，未收入；站内相对链接已改为绝对地址。文中未提及 Meta 11 月 13 日发布的 Poppy 协议。作者声明未做一手测试，MCP 搭建耗时引自 Parallel 的测试；「无原生支持」的表述指公开文档中未见相关内容。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：Muse 目前只会四层互操作协议中的一层：可在对话中要求接入 MCP 服务器，由它在自己的虚拟机里写客户端、经 streamable HTTP 连接并保存为可复用技能，Parallel 的独立测试显示一次消息、不到一分钟即可完成；但 Muse 没有原生 A2A 客户端，也未公布增加计划，无法直接给另一个智能体发消息，只能通过 MCP 服务器上的共享留言板间接交换，对 Google 的 AP2 与 UCP 也未公布支持。作者以一次芝加哥出差为例数出三道信任边界：航司智能体、支付智能体、日历确认各由不同公司经手，只有第一跳是用户点名批准的；并引用 Ars Technica 10 月报道、MCPInspect（833 个有漏洞的 MCP 服务器）、OX Security（Anthropic 官方 MCP 工具包命令注入漏洞）与 OWASP 2026 agentic 十大风险中的 ASI07，说明指令可在智能体间传递。文末给出三问测试：对方智能体是谁建的、它能拿用户数据做什么、它撒谎时怎么办，并建议让 Muse 在花钱前逐个点名它委托过的智能体、逐个出示返回结果。

**保留理由**：把 Muse 置于 MCP、A2A、AP2、UCP 四层互操作协议中逐项核对，指出 Muse 只通 MCP、其余三层均无原生支持，并以三跳信任边界与多起公开漏洞为据给出可操作的三问测试，是已收 Poppy 协议资料之外、关于智能体间互操作与安全的独立分析。
