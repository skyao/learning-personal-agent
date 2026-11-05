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
| 最后收集日期 | 2026-11-05（第一轮完成：官方 36 篇、媒体 3 篇、社区 5 篇） |
| 实测材料 | 用户确认没有（2026-11-05） |

从一开始就按新流程：原文存 `original.md`，资料页只写摘要与保留理由，不翻译。

## 背景

- xAI 于 2026-02 被 SpaceX 收购，资料中公司名先后写作 xAI、SpaceXAI、SpaceXSI（「Super Intelligence」部门），照录原文。
- Cursor 于 2026-08-14 并入 SpaceXSI。Grok Bot 的账号、下载、文档、帮助、计费都走 Cursor 的基础设施，所以官方资料分在 x.ai 和 cursor.com 两处。

## 收录范围

收录范围由用户 2026-11-05 确定为「核心集」：

- 收：x.ai 新闻中所有 Grok Bot 专稿（含发布、套餐、企业版、设计、内部用例）；Cursor 上的 Grok Bot 文档全部；帮助页中讲机制的（套餐、模型、密钥、例程、共享 Bot、连接应用、Bot 邮箱、群聊）；通用指南（101、for Work、模板）。
- 不收：按岗位的指南（营销、销售、SDR、法务、招聘、移动开发、绩效营销、售后、支持、设计、工程等）；账号操作类帮助页（登录、删除账号、移动端购买、获取帮助、onboarding、how-to、pages、edit-bot、computer-recovery、mobile）；产品页 `x.ai/bot`（FAQ 的问题和价格表由脚本加载取不到，剩下的信息文档和帮助页都有）。
- Grok 模型（Grok 4.6、4.7 等）、Grok Build（编码智能体）、Cursor Origin 不收，除非资料专门讲它们在 Grok Bot 中的用法。
- 开源的「类 Grok Bot」项目（Open Bot、Gawkbot、Linubot、OpenMausBot 等）不收。

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| x.ai 新闻 | `x.ai/news/<slug>`；列表 `x.ai/news` | 发布、套餐、企业版、内部用例 | x.ai 对自动访问返回 403，用 Wayback 快照（`fidelity: 转载全文`）；列表页快照可列出全部文章与日期；也可用 CDX 接口 `url=x.ai/news/&matchType=prefix` 查新文章 |
| x.ai 指南 | `x.ai/bot/guides/<slug>`；列表 `x.ai/bot/guides` | 用法指南，多数按岗位 | 同上，用 Wayback；`/bot/guides/<分类>`（design、sales 等）是分类页，不是文章 |
| Cursor 文档 | `cursor.com/docs/grok-bot/<page>` | 概览、开始、工作方式、安全、部署、身份、网络等 14 页 | 直接下载；不标日期，取收集日期 |
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

## 命名约定

- x.ai 新闻：`<日期>-<slug>`；指南：`<日期>-guide-<关键词>`；Cursor 文档：`<收集日期>-docs-<页名>`；帮助页：`<收集日期>-help-<页名>`。
