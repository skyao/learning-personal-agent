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
| 最后收集日期 | 2026-11-05（美东；第一轮：官方 1 篇、媒体 5 篇） |
| 实测材料 | 没有：旧笔记 learning-ai-agent 没有 Instinct 目录 |

## 背景

- 旧金山初创公司，正式名称 Spear Street Technology, Inc.；创始人兼 CEO Noah Shinn，前 Sierra 研究科学家（Reflexion 论文第一作者、τ-bench 合著者）。
- 产品没有独立 App：用户通过短信、iMessage、WhatsApp 或电话交互，网页工作区在 `app.instinct.com`；智能体使用自己的虚拟手机和电脑执行任务。
- 2026-09 起陆续宣布的功能：电话礼宾（Concierge，09-16 前后）、Instinct-to-Instinct 信任网络与 iMessage 位置共享（09-28 C 轮公告）、群聊（10-05 早期访问，10-27 起对所有 iMessage 用户开放，据二手报道）。这些公告多发在 X 上，原帖取不到时以可靠媒体的转述为准。

## 收录范围

- 收：Instinct 的官方页面与公告、专门写 Instinct 的报道和实测、创始人的访谈（有文字稿或节目页文字时）。
- 法律文档（`/privacy-policy`、`/terms`）按 tracking.md 不收；报道中引用的条款内容照常保留。
- 只报融资数字的快讯不收；C 轮公告原文取不到，暂以 SiliconANGLE 的转述为准（它保留了公告中的产品信息）。
- 中文资料多为编译和评论（见判断记录），没有一手实测时不收。

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| 官网 | `instinct.com`（早期为 `instinct.co`） | 首页一段介绍 | 直接下载，首页文字在静态 HTML 中；`/blog`、`/faq` 返回空的应用壳，`sitemap.xml` 只有首页，`docs.`、`help.` 子域不存在（2026-11-05） |
| Business Wire | `businesswire.com/news/home/20260928153437/en/...`（C 轮公告） | 融资与新功能 | businesswire.com 返回 403；北欧分发平台（via.tt.se 等）站内检索不可用，Wayback 查询当时返回 429，以后再试 |
| X | 公司与 Noah Shinn（@noahrshinn）的帖子 | 功能公告 | 不能直接抓取；只在可靠媒体转述或嵌入时引用 |
| 播客 | Colossus「Invest Like the Best」第 493 期 `colossus.com/episode/instinct-the-personal-agent/` | 创始人长访谈 | 节目页可直接下载；完整文字稿需要登录，只公开开头一段，按节目页文字收（节选）。Colossus 的节目地址可从 `colossus.com/podcast_episode-sitemap*.xml` 查 |

## 媒体与社区检索

- 英文检索词：`Instinct AI agent`、`Instinct Noah Shinn`、`Instinct personal assistant iMessage`
- 「Instinct」是常见词，检索时要带 AI、agent 或 Noah Shinn。
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

## 命名约定

- 官方：`<日期>-instinct-<页面>`；媒体：`<日期>-<媒体>-<关键词>`，例如 `2026-08-24-techcrunch-privacy-security`。
