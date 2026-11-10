---
name: collect-grok-bot
description: 收集 Grok Bot（SpaceXAI / xAI，经 Cursor 交付）的资料时使用：Grok Bot 的官方渠道、抓取方法、收录范围与已知问题。与 collect-sources 配合使用，通用流程与页面规则见 collect-sources。
---

# 收集 Grok Bot 资料

通用流程、页面模板与翻译规则见 `skills/collect-sources/SKILL.md`。本文件只记录 Grok Bot 特有的内容；与通用规则冲突时，以本文件为准。

## 状态

| 项目 | 值 |
| --- | --- |
| 产品目录 | `content/zh-cn/docs/grok-bot/` |
| 发布日期 | 2026-08-11（beta） |
| 最后收集日期 | 2026-11-10（增量：更新日志更新到 v0.79.3（11-06），目录改为 2026-11-06-changelog，译文只覆盖到 v0.78.1、新增部分待补译；Cursor 文档 teams 与帮助页 shared-bots 原文更新，旧译文移除待重译；x.ai 新闻无新的 Grok Bot 稿件）；2026-11-06（第一轮 2026-11-05：官方 36 篇、媒体 3 篇、社区 5 篇；2026-11-06 对照旧笔记补收官方 11 篇：docs.x.ai 文档 10 篇、更新日志 1 篇） |
| 实测材料 | 用户确认没有（2026-11-05） |

从一开始就按新流程：原文存 `original.md`，资料页只写摘要与保留理由，不翻译。

## 背景

- xAI 于 2026-02 被 SpaceX 收购，资料中公司名先后写作 xAI、SpaceXAI、SpaceXSI（「Super Intelligence」部门），照录原文。
- Cursor 于 2026-08-14 并入 SpaceXSI。Grok Bot 的账号、下载、计费都走 Cursor 的基础设施，所以官方资料分在 x.ai 和 cursor.com 两处。
- 文档有两套：`cursor.com/docs/grok-bot` 与 `docs.x.ai/grok-bot`（「SpaceXSI Docs」）。两边同名页内容大致相同，docs.x.ai 另有一批讲用户操作与机制的页面，cursor.com 没有。第一轮只查了 cursor.com，漏掉了 docs.x.ai，2026-11-06 对照旧笔记时补上。

## 收录范围

收录范围由用户 2026-11-05 确定为「核心集」：

- 收：x.ai 新闻中所有 Grok Bot 专稿（含发布、套餐、企业版、设计、内部用例）；Cursor 上的 Grok Bot 文档全部；docs.x.ai 上 cursor.com 没有的文档页；更新日志 `x.ai/changelog/bot`（整页一篇，每轮更新）；帮助页中讲机制的（套餐、模型、密钥、例程、共享 Bot、连接应用、Bot 邮箱、群聊）；通用指南（101、for Work、模板）。
- 不收：按岗位的指南（营销、销售、SDR、法务、招聘、移动开发、绩效营销、售后、支持、设计、工程等）；账号操作类帮助页（登录、删除账号、移动端购买、获取帮助、onboarding、how-to、pages、edit-bot、computer-recovery、mobile）；产品页 `x.ai/bot`（FAQ 的问题和价格表由脚本加载取不到，剩下的信息文档和帮助页都有）。
- Grok 模型（Grok 4.6、4.7 等）、Grok Build（编码智能体）、Cursor Origin 不收，除非资料专门讲它们在 Grok Bot 中的用法。
- 开源的「类 Grok Bot」项目（Open Bot、Gawkbot、Linubot、OpenMausBot 等）不收。

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| x.ai 新闻 | `x.ai/news/<slug>`；列表 `x.ai/news` | 发布、套餐、企业版、内部用例 | x.ai 对自动访问返回 403，用 Wayback 快照（`fidelity: 转载全文`）；列表页快照可列出全部文章与日期；也可用 CDX 接口 `url=x.ai/news/&matchType=prefix` 查新文章 |
| x.ai 指南 | `x.ai/bot/guides/<slug>`；列表 `x.ai/bot/guides` | 用法指南，多数按岗位 | 同上，用 Wayback；`/bot/guides/<分类>`（design、sales 等）是分类页，不是文章 |
| Cursor 文档 | `cursor.com/docs/grok-bot/<page>` | 概览、开始、工作方式、安全、部署、身份、网络等 14 页 | 直接下载；不标日期，取收集日期 |
| docs.x.ai 文档 | `docs.x.ai/grok-bot/<page>`；目录见任一页侧栏 | 约 25 页，分 Start、Work with Grok Bot、Manage and protect、Help 四组 | 直接下载；每页有 Markdown 版本（地址加 `.md`），直接存原文；结构化数据有 `dateModified`，作为 `date` |
| 更新日志 | `x.ai/changelog/bot`（有 RSS：`/changelog/bot/rss.xml`） | 每个版本的 New、Improved、Fixed 条目 | 原站 403，用 Wayback 快照；快照是 gzip 压缩的，先解压；`extract.py <html> 'section.pb-24'` 取全部版本（auto 只取到最新一版）；行尾的「Teams」「Enterprise」角标和「Requires Grok Bot x.y or later」提示用 sed 整理 |
| Cursor 帮助 | `cursor.com/help/grok-bot/<page>`；索引 `cursor.com/help/grok-bot` | 约 25 页 | 直接下载 |

- x.ai 新闻页的正文从 H1 之后开始，到「## Try Grok Bot today」为止；去掉「Back to news」、下载与联系销售按钮，视频占位 `[](….mp4)` 改为链接行。脚本加载的交互组件（如发布文中按团队展开的示例）静态页面里没有，标「（以下内容无法获取）」。
- Cursor 文档与帮助页的正文到「## Related…」或「## Was this article helpful?」为止。折叠式 FAQ 的问题文字在标题里的 `<button>` 中，`extract.py` 已在 2026-11-05 改为保留这类按钮的文字。
- 部分内部用例文章的截图是 4K 以上的 PNG（单张 5–10 MB），下载后必须用 `shrink_images.py` 缩小。

## 媒体与社区检索

- 英文检索词：`"Grok Bot"`、`Grok Bot xAI agent`、`Grok Bot review`
- 「Grok」「bot」都是常见词，Grok 聊天机器人本身的评测很多，检索时要用带引号的「Grok Bot」。
- Hacker News 的 Algolia 接口是发现社区文章最有效的渠道：`hn.algolia.com/api/v1/search?query=%22Grok%20Bot%22&tags=story`。
- 检索结果里有大量「Grok Bot review」「explained」类 SEO 文章和工具站博客，不收。

## 媒体与社区的判断记录

已收的不再列出（以 `sourceUrl` 去重）。

| 资料 | 判断 |
| --- | --- |
| Techdirt「Whoops: Grok Bot Spills Tech CEO's Bank Data In Public Slack」（Karl Bode，2026-10-19） | 不收：评论文章，转述已收的 Cybernews 报道 |
| Forbes、The Next Web、GadgetReview 关于 Musk 称成本过高的报道（2026-11-02） | 不收：与已收的 TechCrunch 报道同一事件，未见新信息（据标题与 HN 列表判断，未逐篇打开） |
| x.ai 指南「How I run multiple teams of Grok Bots」 | 暂不收：属于核心集，但 Wayback 没有快照、原站 403 |
| Lee Robinson 关于 Grok Bot 实现的演讲（视频） | 不收：没有官方文字稿；已收的 Peter Piekarczyk 文章依据该演讲整理 |
| botsinproduction、aliakbarfakhri.com、buildfastwithai、stork.ai、layer3labs 等的「review」 | 不收：SEO 或工具站博客 |
| Elon Musk 的 X 帖子（连接银行账户「we will make you whole」、Grok Bot 将使用 Opus 5.5 等） | 不单独收：已在收录的报道中引用 |

## 对照旧笔记的判断（2026-11-06）

旧笔记 learning-ai-agent 的 Grok Bot 部分引用而本笔记没有的来源，逐条判断如下：

| 资料 | 判断 |
| --- | --- |
| docs.x.ai 的 bots、chat-and-collaboration、computer-and-apps、files-and-results、skills-routines-and-automations、tag-on-x、vault、settings-and-notifications、approvals-security-and-privacy、faq | 收：cursor.com 没有对应页，或只有内容差别很大的旧版（settings 与 cursor.com 的 settings 重合约一半，vault 与帮助页 secrets 重合约一半，都另收一篇） |
| docs.x.ai 的 overview、get-started、use-cases、deployment、security、security-faq、teams-and-enterprises、shared-bots、proxies、private-networks、inference-hooks、identity-and-access、computers | 不另收：与已收的 cursor.com 页内容基本相同（词序列重合 69%–98%），地址补进对应页面的 `altUrls` |
| docs.x.ai 的 mobile、troubleshooting | 不收：移动端操作与故障排查，按收录范围属于操作类 |
| 更新日志 `x.ai/changelog/bot` | 收：Wayback 快照（2026-11-04），v0.17.0（08-12）至 v0.78.1（10-27） |
| iThome「五大科技巨頭主動型Agent大比較」（王宏仁，2026-10-02） | 收入 industry/media：比较 Spark、Autopilot、dots、Grok Bot、Muse 五款 |
| Dash Security「Dash Launches Runtime Protection for Grok Bot」（2026-10-19） | 不收：安全厂商推广自家产品，Grok Bot 一侧的机制在已收的 inference hooks 文档中 |
| Stripe 与 Anthropic 的新闻稿 | 讲 Claude Duet，收在 claude-duet 目录 |

## 2026-11-10 增量收集

12 个产品在同一会话里一次跑完（用户 2026-11-10 要求；「一个产品一个会话」的规则保留）。

| 资料 | 判断 |
| --- | --- |
| x.ai 直接下载 | 2026-11-10 起 `x.ai/news`、`x.ai/changelog/bot` 与 RSS 用浏览器标识可以直接下载（200），不再需要 Wayback。更新日志抽取后要整理：日期行「November 6, 2026Nov 6, 2026」去重；条目末尾的「Teams」「Enterprise」角标改为「[Teams]」；「0.75.2+Requires Grok Bot 0.75.2 or later」改为「(Requires Grok Bot 0.75.2 or later)」 |
| Cursor 文档 teams | 原文更新：新增管理员的 Bot sharing 设置（Everyone / Admins only），以及 Slack 中未关联账号的成员使用共享 Bot |
| 帮助页 shared-bots | 原文更新：共享范围扩到组织，新增发布草稿、复制链接、浏览共享 Bot、学到的内容需审核、共享连接器 |
| 其余 Cursor 文档与帮助页 | 比对只差页尾链接，未覆盖 |
| ryandoser.com「Best Personal AI Agent: Grok Bot vs Muse vs Dots vs Duet」（10-28，更新 11-09） | 不收：在已收的 Claire Vo 基准测试上整理，无自己的实测 |

## 命名约定

- x.ai 新闻：`<日期>-<slug>`；指南：`<日期>-guide-<关键词>`；Cursor 文档：`<收集日期>-docs-<页名>`；docs.x.ai 文档：`<dateModified 日期>-xai-docs-<页名>`；更新日志：`<最新条目日期>-changelog`；帮助页：`<收集日期>-help-<页名>`。
