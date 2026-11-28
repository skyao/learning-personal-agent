---
name: collect-instinct
description: 收集 Instinct（Spear Street Technology，创始人 Noah Shinn）的资料时使用：Instinct 的官方渠道、抓取方法、收录范围与已知问题。与 collect-sources 配合使用，通用流程与页面规则见 collect-sources。
---

# 收集 Instinct 资料

通用流程、页面模板与翻译规则见 `skills/collect-sources/SKILL.md`。本文件只记录 Instinct 特有的内容；与通用规则冲突时，以本文件为准。

## 状态

| 项目 | 值 |
| --- | --- |
| 产品目录 | `content/zh-cn/docs/instinct/` |
| 时间线 | 2025 年创立；2026-02 起私人测试（邀请制，至 2026-11 仍未公开开放）；2026-08 下旬在湾区走红，08-27 前后 2.5 亿美元 B 轮（25 亿美元估值）；09-28 宣布 10 亿美元 C 轮（100 亿美元估值） |
| 最后收集日期 | 2026-11-28（10:16 轮次：无新资料；TechCrunch 标签最新仍为 11-21 短信合集（已在 industry 更新），Verge 10/11 月 sitemap 无新文，官网博客仍无帖子）；2026-11-28（美东；增量：媒体 3 篇——TechCrunch 专属邮箱（09-09）、Instinct Selections 商品推荐（09-30）、The Verge Allison Johnson 上手实测（10-09），都是此前检索漏掉的；官网首页原文更新（入口改为「Text Instinct」）；补查 11 月：合作方公告 2 篇——Zocdoc 预约挂号合作新闻稿（10-29，Wayback 快照）、Plaid 金融账户连接博客（11-18））；2026-11-10（增量：补收媒体 1 篇——TechCrunch 群聊上线（10-05）；社区 1 篇——Z Finance 的 Noah Shinn 访谈中文整理（09-30），两篇都是第一轮检索漏掉的）；2026-11-05（美东；第一轮：官方 1 篇、媒体 5 篇） |
| 实测材料 | 没有：旧笔记 learning-ai-agent 没有 Instinct 目录 |

## 背景

- 旧金山初创公司，正式名称 Spear Street Technology, Inc.；创始人兼 CEO Noah Shinn，前 Sierra 研究科学家（Reflexion 论文第一作者、τ-bench 合著者）。
- 产品没有独立 App：用户通过短信、iMessage、WhatsApp 或电话交互，网页工作区在 `app.instinct.com`；智能体使用自己的虚拟手机和电脑执行任务。
- 2026-09 起陆续宣布的功能：专属邮箱（09-08，`mail.instinct.com` 领取）、Instinct Selections 人工策展的商品推荐（09-29 前后，引起部分用户反感）、电话礼宾（Concierge，09-16 前后）、Instinct-to-Instinct 信任网络与 iMessage 位置共享（09-28 C 轮公告）、群聊（10-05 早期访问，10-27 起对所有 iMessage 用户开放，据二手报道）。这些公告多发在 X 上，原帖取不到时以可靠媒体的转述为准。
- 合作接入：Stripe 支付（2026-08）、1Password 登录（2026-09）、Zocdoc 预约挂号（10-29 公告，经 Zocdoc 的 MCP server；Instinct 方署名为首席商务官 Ben Schwerin）、Plaid 只读金融账户（11-18）。
- 2026-11-01 WhatsApp 渠道中断约半天，Noah Shinn 11-02 解释为己方配置错误导致向某服务商的付款中断；只见到聚合站报道（analyticsinsight、newsbytes、officechai、theoutpost 等），未收。

## 收录范围

- 收：Instinct 的官方页面与公告、专门写 Instinct 的报道和实测、创始人的访谈（有文字稿或节目页文字时）。
- 法律文档（`/privacy-policy`、`/terms`）按 tracking.md 不收；报道中引用的条款内容照常保留。
- 只报融资数字的快讯不收；C 轮公告原文取不到，暂以 SiliconANGLE 的转述为准（它保留了公告中的产品信息）。
- 中文资料多为编译和评论（见判断记录），没有一手实测时不收。

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| 官网 | `instinct.com`（早期为 `instinct.co`） | 首页一段介绍 | 直接下载，首页文字在静态 HTML 中；`/blog`、`/faq` 返回空的应用壳，`sitemap.xml` 只有首页，`docs.`、`help.` 子域不存在（2026-11-05）。2026-11-28：sitemap 增加 `/blog`（「No posts yet」）、`/status`（脚本渲染，静态 HTML 只有「Checking Instinct's status…」）、`/acceptable-use-policy`（法律文档，不收）；以后先看 `/blog` 有没有文章。首页比对时，新抽取结果的一级标题带粗体、示例旁有图标，与存档写法不同，不算实质变化 |
| Business Wire | `businesswire.com/news/home/20260928153437/en/...`（C 轮公告） | 融资与新功能 | businesswire.com 返回 403；北欧分发平台（via.tt.se 等）站内检索不可用，Wayback 查询当时返回 429，以后再试 |
| X | 公司与 Noah Shinn（@noahrshinn）的帖子 | 功能公告 | 不能直接抓取；只在可靠媒体转述或嵌入时引用 |
| 合作方公告 | Plaid 博客 `plaid.com/blog/`、Zocdoc 新闻室 `zocdoc.com/about/news/` 等 | 接入合作的一手公告，常带合作方披露的使用数据 | 按第三方公司博客的先例（Sierra、DataDome）放 `community/`。Plaid 可直接下载；Zocdoc 原站返回 403，用 Wayback 快照（转载全文） |
| 播客 | Colossus「Invest Like the Best」第 493 期 `colossus.com/episode/instinct-the-personal-agent/` | 创始人长访谈 | 节目页可直接下载；完整文字稿需要登录，只公开开头一段，按节目页文字收（节选）。Colossus 的节目地址可从 `colossus.com/podcast_episode-sitemap*.xml` 查 |

## 媒体与社区检索

- 英文检索词：`Instinct AI agent`、`Instinct Noah Shinn`、`Instinct personal assistant iMessage`
- **11 月以后 Instinct 自己几乎不发公告，新动态多由合作方发布**：检索要加 `Instinct partnership`、`Instinct Plaid`、`Instinct Zocdoc` 这类词，并看行业媒体（医疗的 Fierce Healthcare、HLTH，金融的 PYMNTS、FF News）。2026-11-28 第一遍只按产品名检索，漏掉了 Zocdoc 和 Plaid 两篇，用户追问后补查才找到。
- 「Instinct」是常见词，检索时要带 AI、agent 或 Noah Shinn。
- **TechCrunch 标签 RSS** `techcrunch.com/tag/instinct/feed/` 一次列出全部 Instinct 稿件的标题与日期（2026-11-28 用它发现了两篇漏收；尾部混有 2008–2009 年同名手机的旧稿，忽略）。
- The Verge 月度 sitemap `theverge.com/sitemaps/entries/<年>/<月>` 可直接下载，`grep instinct` 找稿件地址。
- WIRED 文章地址可从月度 sitemap 查：`wired.com/sitemap-<年>-<月>.xml`，`grep instinct` 或标题关键词。
- 检索结果中大量是 SEO 与聚合站（eesel、vellum、usecarly、layer3labs、aisuperior、andrew.ooo、runtimewire、letsdatascience、aiweekly 等），不收。

## 媒体与社区的判断记录

已收的不再列出。

| 资料 | 判断 |
| --- | --- |
| WSJ「The latest viral AI assistant rocketing across Silicon Valley」（2026-08） | 暂不收：付费墙；TechCrunch 已转述其中 Instinct 的回应 |
| Business Insider 对 Noah Shinn 的人物报道、The Information 的融资报道 | 暂不收：付费墙 |
| Fortune「Noah Shinn Instinct…」（2026-09-30，转述播客：年交易额接近 10 亿美元、旅行占约一半） | 暂不收：返回 403；播客节目页已收 |
| SiliconANGLE「Instinct reportedly raising $250M」（Maria Deutscher，08-27） | 不收：融资快讯，转述 WSJ |
| t3n「KI-Agent mit Kreditkarte」（Marvin Fuhrmann，09-20，德文） | 不收：两分钟短文，转述测试者在 X 上的说法 |
| WIRED「Uncanny Valley」播客（含 Instinct 一段） | 不收：多话题节目，Instinct 部分已有 Zoë Schiffer 的文字稿件 |
| 人人都是产品经理「Instinct，硅谷突然爆火的 AI 私人助理」（09-04）、新浪/澎湃「00后做的Instinct，凭什么33天估值破百亿」（10-11）、虎嗅（10-10）、人人都是产品经理「当 AI 真的开始懂你」（10-02） | 不收：编译与评论，没有一手实测 |
| 凤凰网「阑夕」对 Invest Like the Best 节目的要点整理（09-30） | 不收：二手转述；节目页已收 |
| runtimewire 关于群聊、Mac 应用、专属号码的短讯 | 不收：聚合站；以后找到官方或可靠媒体的一手报道再收 |

## 已知问题

- 融资数字各家说法不一（例如 Dealroom 写 64.7 亿美元估值），以公司公告和可靠媒体为准。
- C 轮公告原文待补：取得后收为官方资料，SiliconANGLE 一篇保留。

## 2026-11-10 增量收集

12 个产品在同一会话里一次跑完（用户 2026-11-10 要求；「一个产品一个会话」的规则保留）。

| 资料 | 判断 |
| --- | --- |
| TechCrunch「Instinct brings its AI agent to group chats」（Sarah Perez，10-05） | 收：群聊功能的一手报道，含 Noah Shinn 关于授权与隔离的说明 |
| Z Finance「对话 Instinct 创始人」（人人都是产品经理，09-30） | 收：Colossus 访谈的中文整理，是能读到的最完整文字版本 |
| Skift「A Viral AI Bot Just Showed Travel What Frictionless Actually Means」（09-04） | 不收：旅游业评论，约 400 词 |
| Built In「What Is Instinct AI?」（10-21） | 不收：解说文，复述公开资料 |
| Cybernews「Instinct AI agent invites hit eBay」（09-30） | 不收：邀请码在 eBay 卖 93 至 200 多美元，其余是对隐私问题的转述 |
| the-ai-corner「Instinct Went From $2.5B to $10B in a Month」（10-09） | 不收：增长评论 |
| runtimewire 的 Mac 应用、共享文件稿，aiweekly 的 BI 人物报道转述 | 不收：聚合站 |
| App Store id6761189540（检索结果中与 Instinct 同列） | 未核实：美区 iTunes 查询为空 |

## 2026-11-28 增量收集

| 资料 | 判断 |
| --- | --- |
| TechCrunch「Viral AI assistant Instinct now has its own email address」（Sarah Perez，09-09） | 收：专属邮箱功能的一手报道，含 Shinn 的 X 帖与 1Password、Stripe 合作 |
| TechCrunch「Instinct's new product recommendations are giving some users the ick」（Sarah Perez，09-30） | 收：Instinct Selections 上线与用户反应 |
| The Verge「Instinct was the buzziest AI agent around — can it survive Muse?」（Allison Johnson，10-09） | 收：一手实测，含 Shinn 的邮件回答（免费期、无 App 的考虑） |
| TechCrunch「Viral AI agent Instinct raises $1B Series C at a $10B valuation」（Sarah Perez，09-28） | 不收：融资稿；公告里的产品信息 SiliconANGLE 一篇已有 |
| TechCrunch「Viral AI startup Instinct has raised $350M at a $2.5B valuation」（08-27） | 不收：融资快讯 |
| TechCrunch「Instinct founder said more than 50% of transactions on the platform are travel-related」（Ivan Mehta，09-29） | 不收：转述 Colossus 播客，节目页与中文整理已收 |
| TechCrunch「The ugly economics of consumer AI」（Russell Brandom，09-30） | 不收：行业评论，Instinct 只是例子之一 |
| TechCrunch「Meta and Instinct are racing to build your AI assistant. Wabi has a different idea.」（10-22） | 不收：写 Wabi |
| The Verge「Zuck accelerated Muse launch in response to Instinct.」（Thomas Ricker，10-09，短讯）、Vergecast「How much should you tell your AI agent?」（10-06） | 不收：短讯转述；多话题播客 |
| WhatsApp 中断（11-01/02）各稿 | 不收：只有聚合站 |
| every.to 多产品横评、Business Insider Japan「2610-ai-agents-muse-dot-instinct-test-review」、HackerNoon 两篇多产品比较 | 属行业综合，留给行业综合检索判断 |
| 补查：Zocdoc 新闻稿「Zocdoc Brings Seamless, Real-Time Appointment Booking to Instinct」（10-29） | 收（community）：合作方一手公告；原站 403，按 Wayback 20261116 快照收 |
| 补查：Plaid 博客「Instinct gets the full financial picture with Plaid」（Kathleen McGuirk，11-18） | 收（community）：合作方一手公告，含接入后的使用数据 |
| Fierce Healthcare「Zocdoc opens infrastructure to AI agents, launches partnership with Instinct」（11-02） | 不收：主要写 Zocdoc 向所有智能体开放，Instinct 部分复述新闻稿；Healthcare Dive、MobiHealthNews 返回 403，HLTH 是短讯 |
| PYMNTS、FF News、artiverse 等 Plaid 合作稿 | 不收：复述 Plaid 博客 |
| Instinct 使用条款 11-17 修订（据 katteb、myclaw 转述：目前免费，保留以后收费的权利） | 不收：法律文档；有可靠媒体报道条款变化时再收 |
| 新加坡 CSA 等机构关于个人 AI 智能体的提示（11-06） | 属行业综合，留给行业综合检索 |
| letsdatascience、progressiverobot、runtimewire、dapta、cellcog、hundredlabs、myclaw、eesel 等 | 不收：聚合站与 SEO 站 |

## 命名约定

- 官方：`<日期>-instinct-<页面>`；媒体：`<日期>-<媒体>-<关键词>`，例如 `2026-08-24-techcrunch-privacy-security`。
