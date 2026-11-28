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
| 最后收集日期 | 2026-11-28（美东；增量：入门帮助页（11-26 修改）与产品页原文更新——开放地区扩大到印度、印度尼西亚、巴西、日本，入门页可由现有用户邀请、不再提 Team，按新版覆盖、旧译文移除待重译；新收官方 1 篇（托管浏览器如何标识自己的帮助页）、社区 2 篇（No Code MBA 上手、Natalie Walls 第一天）、行业综合 1 篇（AgentConnect 架构比较）；发布说明 11 月仍无 Duet 条目）；2026-11-10（增量：官方渠道无新稿，发布说明 11 月没有 Duet 条目；入门帮助页原文更新，按新版覆盖，旧译文移除待重译；媒体与社区未见新资料）；2026-11-06（第一轮 2026-11-05：官方 7 篇、社区 2 篇；2026-11-06 对照旧笔记补收官方 1 篇、社区 2 篇，行业综合 2 篇；媒体仍没有符合条件的） |
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
| 合作方新闻稿 | 如 `stripe.com/newsroom/news/anthropic-and-stripe` | 合作方为 Claude Duet 发布的集成公告，含 Anthropic 方的引语 | 直接下载；放 `official/`，`publisher` 写合作方 |
| 发布说明 | `support.claude.com/en/articles/12138966-release-notes` | 只收 Claude Duet 条目，每条一页，`fidelity: 节选` | 直接下载 |

- claude.com 的 sitemap 里按「duet」过滤只能找到 Duet 专属文章。不点名 Duet 的通用文章（如 2026-11-13 的「Building always-on agents」）不会出现，要在检索结果和他人文章的参考文献里留意；按收录范围，没写 Duet 的不收。
- 帮助中心搜索 `?q=duet` 会列出只顺带提到 Duet 的通用帮助页（如 Personal Finance、托管浏览器标识）。逐篇用 `grep -i duet` 看提到的分量再判断。

anthropic.com 的 news 下没有 Claude Duet 页面（`/news/claude-duet` 返回 404），发布文在 claude.com。

## 媒体与社区检索

- 英文检索词：`"Claude Duet"`、`Anthropic Claude Duet agent`、`Claude Duet review`
- 中文检索词：`Claude Duet`、`Anthropic 主动 智能体`
- 「Duet」是常见词，检索时要带上 Claude 或 Anthropic。
- 检索结果里聚合站和 SEO 站很多（如 tech-insider.org、各种多语言转述站），按 source-types.md 判断，不收。
- 社区讨论可用 Hacker News 的 Algolia 接口检索：`hn.algolia.com/api/v1/search?query=%22Claude%20Duet%22&tags=story`；讨论区本身不收，用来发现被讨论的博客文章。

## 已知问题

- 发布说明条目只写「Pro and Max plans」，发布文、帮助文档和产品页写「Pro, Max, and Ultra」。
- 2026-11-28 起，入门帮助页写「isn't available on Enterprise plans yet」，不再提 Team；产品页 FAQ 仍写「Team and Enterprise plans are not included yet」。两处照录，不互相改。
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

## 对照旧笔记的判断（2026-11-06）

旧笔记 learning-ai-agent 的 Claude Duet 部分引用而本笔记没有的来源，逐条判断如下（上表已列的 Inc.、MacRumors 不重复）：

| 资料 | 判断 |
| --- | --- |
| Stripe「Stripe and Anthropic help entrepreneurs run their business inside Claude Duet」（2026-10-21） | 收：Link 钱包与 Stripe MCP 接入 Claude Duet 的官方说明 |
| Chris Alarcon「Claude Duet (2026): My First Day, Access, and Your Limits」（2026-10-29） | 收：Max 套餐第一天的上手记录；文首记有 10-30 的套餐改名（Max 5x 改为 Max，Max 20x 改为 Ultra） |
| ChatPRD「Claude Duet Is Beautiful. That Doesn't Make It My Go-To Agent.」（Claire Vo，2026-10-26） | 收：多项任务实测。Lenny's Newsletter 的同期节目页只是节目列表，不另收 |
| coocolab「Claude Duet 實測：我花 10 小時玩透」（Jimmy，2026-11-03） | 不收：标题说九件事，正文只列五点，大量卡片式套话，具体操作少，判断为 SEO 写法 |
| ChatPRD「Grok vs. Dot vs. Muse vs. Claude Duet」（Claire Vo，2026-10-29） | 收入 industry/community |
| 掘金「六周四家巨头入场：主动式 Agent 的架构长什么样？」 | 不收：转述官方说明，无实测 |
| TechTimes「Claude Duet Passed Safety Review, Then Accessed Georgia Paywall…」（2026-10-26） | 不收：事件出自 Axios，原文说是 Anthropic 内部统计项目中的 Claude，并非 Claude Duet，标题把两者混在一起；其余是对官方安全文的转述 |
| 帮助中心的记忆、用量限制、limit reset、连接器、Cowork 与 chat 页 | 不收：通用帮助页，讲 Claude Duet 的只有一两句，入门帮助页已写明（可搜索过往对话、共用记忆） |
| dnyuz「I tested every major AI agent for a day」 | 已收：是 WIRED 原文的转载，industry 中已收 WIRED 原文 |
| 帮助中心入门页的中文版 | 补进入门帮助页的 `altUrls` |
| claude.com/pricing、LinkedIn 套餐改名帖 | 不收：定价页没有提到 Claude Duet；改名的事实见 Chris Alarcon 一文 |
| Anthropic research 的 auto mode、Managed Agents、prompt injection、trustworthy agents 文章 | 不收：按收录范围只作背景 |
| Hacker News 讨论（item 50186455） | 不收：讨论区，所讨论的是已收的发布文 |
| nerdschalk、VentureBeast first-look、aiagentslibrary 的 Duet 评测、HUMAN Security「Sightline detects Claude Duet」 | 暂不收：原站 403 或只由脚本加载，Wayback 没有快照；HUMAN Security 的文章可能有新信息，需要时请用户在浏览器中复制 |
| YouTube 视频 3 个 | 不收：没有文字稿 |

## 2026-11-10 增量收集

12 个产品在同一会话里一次跑完（用户 2026-11-10 要求；「一个产品一个会话」的规则保留）。

| 资料 | 判断 |
| --- | --- |
| 入门帮助页 17631495 | 原文更新：限额重置改为按套餐发放（Pro 三次，Max 与 Ultra 一次），有效期改到 2026-12-15，新增「Claude Duet 中不提供 Personal Finance」 |
| 产品页 | 比对只差连接器 logo 文字，未覆盖 |
| Link by Stripe、Shop Pay 帮助页 | 未变 |

## 2026-11-28 增量收集

| 资料 | 判断 |
| --- | --- |
| 入门帮助页 17631495 | 原文更新（dateModified 2026-11-26）：开放地区加印度、印度尼西亚、巴西、日本；邀请可来自现有用户；不再提 Team；删去 Microsoft 365 一句。覆盖原文，移除旧译文 |
| 产品页 | 原文更新：页首与 FAQ 的开放地区同上，其余不变；改 original.md 的两句，移除旧译文 |
| 帮助页 18234133「How do Anthropic-hosted browsers identify themselves…」（11-04） | 收：点名 Claude Duet，说明它的托管浏览器带 `Claude-Agent` 标识，IP 公布在 `claude.com/.well-known/sail` |
| 帮助页 18185620「Use Personal Finance in Claude」 | 不收：只有一句「Claude Duet 中不提供 Personal Finance」，入门页已有 |
| claude.com「Building always-on agents」（William Hu，2026-11-13） | 不收：Claude Platform 的开发者最佳实践，全文不提 Claude Duet。若用户想收进 industry，可再议 |
| No Code MBA「Claude Duet Review: What Happened When I Set It Up」（11-11） | 收：第一次设置的上手记录（导入、频道、Tasks、固定模型）；站点是课程与通讯站，文末有联盟链接声明 |
| Natalie Walls「My First Day with Claude Duet」（11-13） | 收：第一天的多项实测（迁移数据库、邮件替代方案、购物车停在结账），记了 $20 套餐用掉约 75% 的周限额；文末说明文章由 Claude 起草、作者审阅 |
| AgentConnect「How always-on agents split routing, execution, and permissions」（11-23） | 收入 industry/community：比较 dsh-superagent、Grok Bot、Claude Duet 等的路由与权限设计，含 Duet 预览账号的观察；作者是自家编排产品的团队，收录说明写明。有官方中文版，填 `altUrls` |
| Every「Vibe Check: Duet—Anthropic's Always-on Agent」（10-21，11-15 修改） | 暂不收：付费墙，静态页只有约 600 词的开头；Every 自述获得了提前试用。需要时请用户在浏览器中复制 |
| TechCrunch「Claude Duet app is Anthropic's bet on agents」（Ivan Mehta，10-22） | 不收：复述发布文；唯一的新说法是「面向专业人士和小企业」，没有引语 |
| techbytes.app「Claude's Duet agent is a little neurotic…」（11-14） | 不收：无第一人称，像是对他人上手报道的转写，没有出处 |
| VKTR、CXOToday、promptzone、kompozy.io、ai.joaoqueiros.com | 不收：发布复述或评论、聚合摘要、工具站评分页（kompozy 的 datePublished 写 2026-05-21，早于发布）、YouTube 视频的二手总结 |

## 命名约定

- 帮助中心：`<日期>-help-<关键词>`；发布说明：`<日期>-relnotes-<关键词>`；产品页：`<收集日期>-product-page`。
