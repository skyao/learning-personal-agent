---
title: "Muse 占 AI 智能体请求的 59%，新签名密钥与 Meta 的 5 把无一相同"
linkTitle: "Muse 占智能体请求 59%"
date: 2026-11-15
originalTitle: "Meta's Muse Sends 59% of AI Agent Requests; Its New Signing Keys Share 0 of Meta's 5"
sourceUrl: "https://saaslinkbuilding.com/blog/meta-muse-web-bot-auth-verification/"
author: "Vibhu Dhariwal"
publisher: "SaaS Link Building"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-19
tags: [安全]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载全文；删去文末 About、联系方式与“更多文章”等推广区块；四家密钥目录签名有效期点图已本地化。发布方 SaaS Link Building 是 SEO/外链机构，作者为该机构联合创始人兼 CTO；文中核查方法与时间戳均有写明，请求量数字引自 HUMAN 与 DataDome。本轮未能从本机独立复核 muse.ai 密钥目录（直接下载失败、浏览器受限），meta.com 一侧核对确为 5 把密钥，与文中一致。页面 <title> 为 How to Verify Meta Muse's Web Bot Auth Signatures，正文标题以显示的 H1 为准。

**内容摘要**：根据 HUMAN 10 月份的智能体流量报告（11 月 9 日发布），Muse 在 HUMAN 保护的网站上占 AI 智能体请求的 59%，较 9 月上升 19 个百分点，流量环比接近翻两番，请求量为 ChatGPT Agent 的 3.7 倍；Meta 与 OpenAI 合计约占智能体请求的 90%，85.2% 的智能体请求流向产品页与搜索页。11 月 7 日至 9 日期间，Muse 把请求签名的签名身份从 www.meta.com 的密钥目录迁移到新的 muse.ai 目录，两把签名器并行约一天半（约 60 小时过渡期），此后只以 https://muse.ai 签名；作者于 11 月 15 日实取四个智能体密钥目录并做 Ed25519 验证，发现 muse.ai 的 2 把密钥与 www.meta.com 的 5 把无一相同，四个目录的响应签名全部验证通过。DataDome 于 11 月 10 日报告称，约一半 Muse 请求未带签名，可能是分阶段推出的结果；Meta 9 月 8 日的安全文章称 Muse 浏览时“将呈现为用户本人的活动”，Cequence 10 月称 Muse 以标准 Chrome 浏览器经消费级 VPN 呈现、靠行为而非身份信号被识别，且文中引用的来源均未给出可供 robots.txt 匹配的 user-agent 标识。对比还发现：chatgpt.com 单把密钥的有效期为每次取文时刻起正好七天滚动过期、响应标为 no-store；agent.bot.goog 的 5 把密钥用六字符标签而非 JWK SHA-256 thumbprint；openai.com、claude.ai、www.anthropic.com、www.perplexity.ai、x.ai、grok.com 均未找到密钥目录。方法论一节写明：作者于 2026 年 11 月 15 日 05:19 UTC 通过 HTTPS 请求各站点的 /.well-known/http-message-signatures-directory，对返回 JSON 密钥集的四个目录计数密钥、计算 thumbprint 并比对 kid、跨目录比对公钥、记录 Cache-Control，并以 Ed25519 验证全部九个目录响应签名；作者未观测真实请求，请求量数字引自 HUMAN 与 DataDome。

**保留理由**：这篇是已收资料里没有的独立实测：作者 11 月 15 日实取四个智能体密钥目录并完成 Ed25519 验证，给出 muse.ai 与 www.meta.com 密钥零重合、chatgpt.com 七天滚动过期、Google 六字符标签等可直接复核的原始数据，并附 RFC 9421 验签示例；同时记录了 Muse 仍有一半请求未签名、无法用 robots.txt 封禁的现状。
