---
title: "从 Muse 直接调用其他 AI 的方法——用 CLI 使用 Claude Code、Antigravity 与 Gemini API"
linkTitle: "用 CLI 调用其他 AI"
date: 2026-11-25
originalTitle: "Museから他のAIを直接呼ぶ方法 ―― Claude Code・Antigravity・Gemini APIをCLIで使う"
sourceUrl: "https://muse.emma-muse.com/articles/cli-ai-bridge"
author: "えま"
publisher: "えまのMuse活用ガイド"
language: ja
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-25
tags: [运行环境, 连接器]
products: [muse]
dateNote: "按日本时间记 2026-11-25；三条路线的实测程度不同，见摘要"
---

{{< source-info >}}

**收录说明**：直接下载（div.article-body 容器）；三 CLI 结构图已下载到 images/ 并本地化。

**内容摘要**：文章介绍如何利用 Muse 自带的终端安装其他 AI 的 CLI 工具，在作业途中用命令直接调用其他 AI 的回答，三条入口分别是 Google 账号登录的 Antigravity CLI、API 密钥使用的 Gemini API CLI 与 Anthropic 的 Claude Code。路线一 Antigravity CLI 有实测：agy models 列出 Gemini 4 Hydrogen、Gemini 3.8 Flash，以及 Claude Sonnet 4.6、Claude Opus 4.6、GPT-OSS 120B；首都提问约 7 秒返回、退出码 0，JSON 调用中计算题答案“51”与 status=SUCCESS、约 2.2 秒、合计 10,161 token 一并返回，指定 Claude Sonnet 4.6 提问约 1.7 秒得到“Claude Sonnet 4.6”的回答。作者在登录最后阶段遇到认证码交换通信超时、失败 2 次，改用环境变量 GODEBUG=http2client=0 把 HTTP/2 固定为 HTTP/1.1 后第 3 次完成登录，并注明这可能是其环境特有的问题。路线二 Gemini API CLI 只实测到 dry-run：gemini-api generate 加 --dry-run 显示了将发送的请求（URL 与含 gemini-4-hydrogen 的正文），不通信、以退出码 0 结束，实际生成调用未做，因为作者环境中的 Gemini API 密钥以注入方式提供、无法流用至该 CLI。路线三 Claude Code 只有步骤介绍、未实测：需 Claude Pro、Max、Ultra、Team、Enterprise 之一或 Console（API）账号，免费 claude.ai 套餐不能使用 Claude Code，作者环境中没有 Claude 侧的认证手段；另据官方仓库说明，Gemini CLI 的个人免费枠与 Google AI Pro／Ultra 用途已于 2026 年 6 月 18 日迁移至 Antigravity CLI。

**保留理由**：这是日本社区作者在自己环境中实测 Muse 终端调用其他 AI 的记录，三条路线的实测程度逐一写明且附有具体耗时与 token 数，是 Muse 与其他 AI 协作用法的少有的一手实测。
