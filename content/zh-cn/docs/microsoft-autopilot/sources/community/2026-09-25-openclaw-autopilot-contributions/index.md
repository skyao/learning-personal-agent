---
title: "Microsoft Autopilot 基于 OpenClaw，贡献是双向的"
linkTitle: "OpenClaw：上游贡献"
date: 2026-09-25
originalTitle: "Microsoft Autopilot is built on OpenClaw. The contributions go both ways."
sourceUrl: "https://openclaw.ai/blog/microsoft-autopilot-openclaw/"
author: "Graham McBain"
publisher: "OpenClaw Blog"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-10
tags: [安全, 运行环境]
products: [microsoft-autopilot]
---

{{< source-info >}}

**收录说明**：开源项目 OpenClaw 的官方博客（发布方不是微软），在 Autopilot 改名当天发布，列举微软向 OpenClaw 上游的贡献。直接下载；删去了「All posts」返回链接与作者头像，题图收入 images/，文中嵌入的 X 帖子按页面文字照录。待翻译。

**内容摘要**：OpenClaw 项目博客在 2026 年 9 月 25 日称，Autopilot 是此前 Microsoft Scout 的新名称，其基础是 OpenClaw；Omar Shahine 的原话是：「我们在 @openclaw 上构建 Autopilot，并与 @steipete 和 OpenClaw Foundation 合作，使它成为出色的企业级运行时。」文章列出微软人员的上游贡献：Gio Della-Libera 的 Policy 插件让运营者描述要求、与实际配置比对并生成记录，后续扩展到模型提供方、网络、MCP 服务器和密钥配置，Shahine 另贡献了消息路由检查。Windows 方面包括原生 Windows 伴侣的引导式设置、WinUI 聊天、内联命令批准，以及 Paul Campbell 提供的 MXC 沙箱后端；可靠性方面包括让排队的用户请求优先于后台任务、修复可能挂起 Gateway 的调度器、区分「确定未运行」与「结果未知」的命令；安全方面包括在执行批准提示中对密钥脱敏。文中还说，并非每个微软人员的贡献都必然是 Autopilot 功能或公司赞助项目。

**保留理由**：这篇给出了 Scout/Autopilot 回馈 OpenClaw 上游的具体贡献清单和贡献者，是政策合规、Windows 支持和可靠性修复的公开记录，其他材料只有笼统的承诺。
