---
title: "深挖 Meta 的新协议 PAP：个人智能体如何与商家协作"
linkTitle: "PAP 协议深挖"
date: 2026-10-10
originalTitle: "A Deep Dive into Meta's New PAP (Personal Agent Protocol)"
sourceUrl: "https://gaoweichang.substack.com/p/a-deep-dive-into-metas-new-pap-personal"
author: "Gaowei Chang"
publisher: "Substack"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-13
tags: [连接器, 安全]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载。去掉了作者头像与订阅信息；文末协议关系图已本地化。作者为 ANP（Agent Network Protocol）开源社区创始人，文中多次以 ANP 作对照。本轮经 Poppy 1.0 报道回溯发现。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：作者通读 PAP 规范全文后，以「为下周去纽约出差订曼哈顿酒店、两晚总预算 600 美元以下」为例，分步演示 PAP 如何工作。酒店在官网标准地址 `/.well-known/poppy.json` 发布服务说明文件，Muse 通过搜索引擎找到酒店并读取该文件，再证明客户端身份、建立会话，先以未登录状态查询公开信息。用户在酒店自己的登录与授权页面登录，不把用户名密码交给 Muse，酒店发给 Muse 的是限定范围的访问令牌，授权可撤销；示例中酒店两晚含税总价 560 美元、含早餐、可在入住前一天免费取消。身份方案采用 OAuth 2.0 + CIMD + JWT + DPoP：CIMD 让个人智能体以 HTTPS URL 为标识并发布身份元数据文档，无需预先逐家注册客户端；DPoP 把令牌与智能体持有的私钥绑定，令牌被盗也无法直接使用。授权方案定义 `poppy:read` 与 `poppy:write` 两种默认权限，支持按需授权、可撤销，并把 API、MCP、商家智能体对话与网页操作统一到同一业务会话、同一套权限控制之下；可选的 Operations 扩展为每项具体业务操作生成唯一 ID、管理确认与执行状态。文中把 PAP 与 MCP、A2A、ANP 对比：MCP 解决模型接工具，A2A 解决两个智能体基于任务的交互，ANP 解决任意两个智能体在互联网上的互联，而 PAP 解决个人智能体与代表商家的智能体协作；PAP 目前不定义任意两个个人智能体之间的对等认证与通信。

**保留理由**：已收资料中唯一逐条拆解 PAP 规范技术细节的独立分析，身份（CIMD/DPoP）、授权（按需授权、跨渠道统一会话）与发现机制的说明在官方稿中没有同等深度，是理解协议实现方式的依据。
