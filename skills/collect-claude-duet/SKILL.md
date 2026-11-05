---
name: collect-claude-duet
description: 收集 Claude Duet（Anthropic）的资料时使用：Claude Duet 的官方渠道、抓取方法、收录范围与已知问题。与 collect-sources 配合使用，通用流程与页面规则见 collect-sources。
---

# 收集 Claude Duet 资料

通用流程、页面模板与翻译规则见 `skills/collect-sources/SKILL.md`。本文件只记录 Claude Duet 特有的内容；与通用规则冲突时，以本文件为准。

## 状态

| 项目 | 值 |
| --- | --- |
| 产品目录 | `content/zh-cn/docs/claude-duet/` |
| 发布日期 | 2026-10-21（研究预览，美国 Pro、Max、Ultra，候补名单） |
| 最后收集日期 | 2026-11-05（第一轮完成：官方 7 篇、社区 2 篇；媒体没有符合条件的；行业综合中另有 4 篇涉及 Claude Duet） |
| 实测材料 | 用户确认没有（2026-11-05） |

从一开始就按新流程：原文存 `original.md`，资料页只写摘要与保留理由，不翻译。

## 收录范围

- Anthropic 的 Claude Duet 应用（研究预览）及其官方说明、帮助文档、发布说明条目。
- 同名的开源 GitHub 项目「claude-duet」与 Anthropic 无关，不收。
- Claude 本身、Claude Code、Cowork、Claude in Chrome 的资料不收；只有在说明 Claude Duet 如何复用它们（如 auto mode 分类器、Managed Agents 的凭证设计）时，作为背景在摘要中提及，不单独收。
- 模型资料（Claude Opus 5.5 系统卡等）按 collect-sources 的「模型资料的收录原则」判断：Claude Duet 固定使用 Opus 5.5，但系统卡若没有专门写 Claude Duet，不收。

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| claude.com 文章 | `claude.com/resources/articles/<slug>`；用 `claude.com/sitemap.xml` 查找含 duet 的地址 | 发布文、安全隐私文 | 直接下载；正文到「## Related articles」为止，去掉分类、日期、阅读时长信息栏 |
| 产品页 | `claude.com/product/claude-duet` | 定位、连接器、模拟对话、FAQ | 直接下载；FAQ 的问题在 `<button>` 中，`extract.py` 会删掉 button，抽取前先 unwrap |
| 帮助中心 | `support.claude.com/en/articles/<id>`；搜索 `support.claude.com/en/?q=duet` | 入门、Link、Shop Pay 等 | 直接下载；日期取结构化数据的 `dateModified` |
| 发布说明 | `support.claude.com/en/articles/12138966-release-notes` | 只收 Claude Duet 条目，每条一页，`fidelity: 节选` | 直接下载 |

anthropic.com 的 news 下没有 Claude Duet 页面（`/news/claude-duet` 返回 404），发布文在 claude.com。

## 媒体与社区检索

- 英文检索词：`"Claude Duet"`、`Anthropic Claude Duet agent`、`Claude Duet review`
- 中文检索词：`Claude Duet`、`Anthropic 主动 智能体`
- 「Duet」是常见词，检索时要带上 Claude 或 Anthropic。
- 检索结果里聚合站和 SEO 站很多（如 tech-insider.org、各种多语言转述站），按 source-types.md 判断，不收。
- 社区讨论可用 Hacker News 的 Algolia 接口检索：`hn.algolia.com/api/v1/search?query=%22Claude%20Duet%22&tags=story`；讨论区本身不收，用来发现被讨论的博客文章。

## 已知问题

- 发布说明条目只写「Pro and Max plans」，发布文、帮助文档和产品页写「Pro, Max, and Ultra」。
- 发布文文首有 2026-10-23 加入的说明框，链接到当天发布的安全隐私文。

## 媒体与社区的判断记录

已收的不再列出（以 `sourceUrl` 去重）。以下是判断过、没有收或待处理的，避免下一轮重复判断。

| 资料 | 判断 |
| --- | --- |
| The Verge「Anthropic takes on Muse with Claude Duet」（Jay Peters，2026-10-21）、9to5Google、MacRumors、BetaNews 的发布报道 | 不收：复述发布文，没有新信息 |
| Reuters「Anthropic unveils Claude Duet AI agent app」（2026-10-21） | 暂不收：原站返回 401，Wayback 没有快照；需要时请用户在浏览器中复制正文 |
| Inc.「I Tried Claude Duet. Its Best Feature Is Knowing When to Stop」（Jason Aten） | 暂不收：上手实测，值得收，但原站返回 403、Wayback 没有快照；需要时请用户在浏览器中复制正文 |
| runtimewire.com「Claude Duet uses Claude Code Routines for scheduled check-ins」 | 不收：约 180 词的转述，标题的说法在正文中没有依据，引用的「VentureBeast first-look」找不到 |
| 中文、日文媒体（INSIDE、iThome、TechNews 科技新报、财联社、凤凰科技、Gizmodo Japan 等）与各语言转述站 | 暂不收：据检索摘要判断为复述发布文，未逐篇打开核实；下一轮如有时间可抽查 |
| botsinproduction.com「I built a Claude Duet by hand a year ago」 | 未细看：Hacker News 上 1 分，暂不收 |
| myclaw.ai、eesel.ai、mindstudio.ai、DataCamp 等的「review」「explained」文章 | 不收：厂商或工具站的博客；myclaw.ai 自述依据发布周材料而非实测，其余据检索摘要判断，未逐篇打开 |

## 命名约定

- 帮助中心：`<日期>-help-<关键词>`；发布说明：`<日期>-relnotes-<关键词>`；产品页：`<收集日期>-product-page`。
