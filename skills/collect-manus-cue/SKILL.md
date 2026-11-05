---
name: collect-manus-cue
description: 收集 Manus Cue（Manus / Butterfly Effect）的资料时使用：Cue 的官方渠道、抓取方法、收录范围与已知问题。与 collect-sources 配合使用，通用流程与页面规则见 collect-sources。
---

# 收集 Manus Cue 资料

通用流程、页面模板与翻译规则见 `skills/collect-sources/SKILL.md`。本文件只记录 Manus Cue 特有的内容；与通用规则冲突时，以本文件为准。

## 状态

| 项目 | 值 |
| --- | --- |
| 产品目录 | `content/zh-cn/docs/manus-cue/` |
| 发布日期 | 2026-09-28（与 Manus 2.0 同日，抢先体验，凭邀请码） |
| 最后收集日期 | 2026-11-05（第一轮：官方 7 篇、媒体 2 篇、社区 1 篇；其中 5 篇是对照旧笔记 learning-ai-agent 的 Cue 资料索引补收的） |
| 实测材料 | 没有：旧笔记 learning-ai-agent 的 `agents/personal/cue/` 是 2026-10-21 至 10-26 的资料阅读与实验方案，作者注明没有账号实测，不迁入 |

从一开始就按新流程：外文原文存 `original.md`，资料页只写摘要与保留理由，不翻译。

## 背景

- Manus 的运营公司是新加坡的 Butterfly Effect Pte. Ltd.。Meta 于 2025-12 宣布收购 Manus，2026 年被中国监管叫停，Manus 于 2026-09-01 宣布恢复独立运营。报道中常把 Cue 定位为与 Meta Muse 竞争的产品。
- Cue 与 Manus 共用基础设施，但是独立应用、独立域名（`cue.im`），与 Manus Studio（原 Manus 桌面版）分开。Manus 侧边栏的「Agents (Cue!)」标签是现有 Manus 用户的入口。

## 收录范围

- 收：Cue 本身的发布、帮助、应用商店说明，以及专门写 Cue 的报道和实测。
- Manus 2.0 的综合资料（发布文、帮助页）只节选 Cue 部分；Cascade、Manus Studio、Video Editor、Game Dev、Cloud Computer、Remote Control 等 Manus 本体功能不收。
- 早于 Cue 的「Manus Agents」（Telegram、Slack、LINE 中的 Manus 智能体，帮助中心 2026-02 至 04 的文章）不算 Cue 资料，不收。
- Manus 的安全漏洞报道（Salt Labs 的邮件提示注入、Aurascape 的 SilentBridge、CodeAnt 的共享项目注入等）针对的是 Manus 本体，不提 Cue，不收；以后若有针对 Cue 的安全报道再收。
- Manus 融资、与 Meta 的交易等公司新闻不单独收。

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| Manus 博客 | `manus.im/blog/<slug>`；sitemap `manus.im/sitemap.xml` | 发布文 | 直接下载。页面是 Next.js，正文以 Markdown 形式内嵌在 RSC 数据（`self.__next_f.push`）中，比静态 HTML 完整（静态 HTML 缺文末 Availability 一段）；发布与修改时间取内嵌数据的 `createdAt` / `updatedAt` 秒数 |
| Manus 帮助中心 | `help.manus.im/en/`（Intercom）；分类「Manus 2.0」`/en/collections/19763651-manus-2-0` | Cue 说明 | 直接下载，`ld:dateModified` 作日期；截图是带签名参数的 Intercom 地址，要立即下载 |
| Cue 官网 | `cue.im` | 首页、下载、反馈 | 首页是 Vite 单页应用，文字和六十多个示例任务都在 `/assets/home-*.js` 包里，没有浏览器无法按页面原样取文，2026-11-05 未收；sitemap 只有首页和 `/feedback` |
| Google Play | `play.google.com/store/apps/details?id=ai.manus.agents&hl=en` | 应用介绍 | 直接下载，取 `[data-g-id=description]`；页面随版本更新，日期取「Updated on」 |
| App Store | `apps.apple.com/us/app/cue-by-manus/id6808613358` | 应用介绍、内购价格 | 直接下载；内购列表（各国号码、Cue Pro、Cue Max、Cloud Computer）是目前唯一的官方标价，页面不写计费周期；版本号几乎每天更新 |

- `help.cue.im`、`docs.cue.im` 不存在（2026-11-05）。
- 帮助中心里讲 Cue 的内容大多不在分类列表中，而是散在通用文章里的「Cue」小节（会员定价、Skills、取消订阅、退款、Mail Manus、账号删除、数据保留），另有专讲 Cue 的「Can I connect multiple messaging agents at once in Cue?」。分类列表找不到时，用网页检索 `site:help.manus.im Cue`，或对照旧笔记 learning-ai-agent 的 `agents/personal/cue/references/`。
- 帮助中心和博客有中文版（`help.manus.im/zh-CN/…`、`manus.im/zh-cn/blog/…`），按同一内容的不同语言版本处理，记入 `altUrls`。
- 以后检查新官方资料：Manus 博客列表与 Wayback CDX（`url=manus.im/blog/&matchType=prefix`），帮助中心各分类中带「Cue」的文章。

## 媒体与社区检索

- 英文检索词：`"Manus Cue"`、`"Cue by Manus"`、`Cue app Manus agents phone number wallet`
- 中文检索词：`Manus Cue 实测`、`Cue 个人Agent 体验`、`Manus 2.0 Cue`
- Hacker News 上几乎没有讨论（2026-11-05 只有 cue.im 和发布文的两三条低分帖）。
- 中文实测多发在微信公众号和 X 长文，原文通常取不到，要找完整转载（投资界、新浪财经、觉醒AI知识库等）并填 `reprintUrl` 或在 `dateNote` 说明。
- 「Cue」是常见词，检索时要带 Manus。

## 媒体与社区的判断记录

已收的不再列出（以 `sourceUrl` 去重）。

| 资料 | 判断 |
| --- | --- |
| The Next Web（Ana Maria Constantin，2026-09-29） | 不收：Cue 部分只复述发布文 |
| InfoWorld「Meta's ex launches agent rival to Meta's Muse」（2026-09-29） | 不收：Cue 部分只复述发布文，分析师评论针对 Manus 2.0 的企业用途；Computerworld 同文 |
| Siècle Digital（2026-09-30，法文） | 不收：复述发布文 |
| implicator.ai（2026-09-28） | 不收：付费墙，只取到导语 |
| 爱范儿（2026-09-29，36氪欧洲站转载） | 不收：大部分写 Manus 与 Meta 的资本经过，Cue 部分复述发布文（另提到首批限 1000 人） |
| 36氪「Manus回来了，可Agent的战场已经挤满对手」（李炤锋，2026-09-30，投资界转载） | 不收：Cue 只有一两句体验，主体是国内竞争格局 |
| 特工宇宙「Manus 团队新产品发布，Cue 一手体验！」（2026-09-29，53AI 转载） | 不收：转载被截断（需登录看剩余 30%），体验只有一个发票整理的例子 |
| 「Muse 之后又来新选手？Manus 新产品 Cue 的第一轮实测」（腾讯云开发者社区） | 暂不收：页面有反爬脚本，Wayback 没有快照；原文若在微信公众号可另找转载 |
| 腾讯新闻「Manus 2.0发布，亮点是能替你接电话的个人Agent “Cue”」、搜狐两篇 | 暂不收：腾讯新闻返回 501，搜狐返回 403 |
| 53AI「Manus 2.0发布：Agent有独立电脑和钱包」（博主「哈基米的AI进化史」） | 不收：转述，号码价格无出处 |
| zentor.ai「What Is Manus Cue?」（2026-10-02） | 不收：工具站博客，带自家产品推广；有一个很小的群聊交接测试（Mac 版，10-01），同类观察已收在 xiangxiang103 的实测中 |
| cellcog.ai「Cue by Manus: What It Is, Invite Code and Price」（2026-10-09） | 不收：卖 AI 员工产品的厂商博客，只汇总官方页面；其中 Google Play 旧版文字的引用已记入 Google Play 页的 `dateNote` |
| myclaw.ai「Cue by Manus Review」（2026-10-10） | 不收：标题称「Tested」但没有自测，汇总二手说法，带 OpenClaw 托管广告；号码 9.99 美元/月的说法无出处，与 xiangxiang103 实测的 0.99 美元/月冲突 |
| nerdheadz、buildfastwithai、aitoolsreview、toolworthy、tooldirectory、aiidelist、rzlt、bazaarlink、bit.fan、ai-tldr、stable-learn、today.ai 等 | 不收：SEO 或工具站博客，复述发布文 |
| Product Hunt「Cue by Manus」 | 暂不收：返回 403 |
| Bloomberg 关于 Manus 估值与中国团队的报道 | 不收：公司新闻，不专门写 Cue |
| 字母AI「Manus这次，直接冲着“人”去了」（袁心玥，2026-09-29，36氪授权发布） | 不收：复述发布文和肖弘的说法（已收在财经涂鸦一篇中），其余是评论 |
| Manus 博客「Context Engineering for AI Agents: Lessons from Building Manus」（2025-07-18） | 不收：讲 Manus 本体的智能体工程，早于 Cue，不提 Cue |
| 帮助中心：取消订阅、退款、Mail Manus、账号删除、数据保留中的 Cue 小节 | 不收：账号与计费操作类内容。要点：取消号码订阅与退款是两个步骤；发布初期已用和未用的号码都可退款；智能体邮箱在 Manus 的 Settings > Email 中删除；Cue 与 Manus 共用同一账号和数据，不能只删除 Cue 账号 |

## 已知问题

- 电话号码价格：App Store 内购列表（2026-11-05）各国号码均为 9.99 美元；xiangxiang103 在发布次日看到美国号码 0.99 美元/月，53AI 博主称首批 0.99 美元、之后 9.99 美元，可能是早期优惠。App Store 还列出 Cue Pro 100 美元、Cue Max 200 美元与 2000 美元、Cloud Computer 39 美元，不写计费周期；应用介绍说获得资格后免费附带 Plus。
- Google Play 介绍文字会随版本改动（例如 10-08 版写「depending on availability」，11-04 版已删）。

## 命名约定

- Manus 博客：`<日期>-<slug>`；帮助页：`<修改日期>-help-<slug>`；应用商店：`<更新日期>-google-play-listing`。
- 中文媒体与社区：`<日期>-<媒体或作者拼音/账号>-<关键词>`。
