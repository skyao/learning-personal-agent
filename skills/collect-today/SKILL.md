---
name: collect-today
description: 收集 Today AI（齐俊元创办的初创公司）的资料时使用：Today 的官方渠道、抓取方法、收录范围与已知问题。与 collect-sources 配合使用，通用流程与页面规则见 collect-sources。
---

# 收集 Today AI 资料

通用流程、页面模板与翻译规则见 `skills/collect-sources/SKILL.md`。本文件只记录 Today 特有的内容；与通用规则冲突时，以本文件为准。

## 状态

| 项目 | 值 |
| --- | --- |
| 产品目录 | `content/zh-cn/docs/today/` |
| 发布日期 | 国际版（today.ai）2026-09 初开始公测（品玩 09-09 的体验稿；官方博客 2026-08-03 起已发文）；国内版（todayai.cn）2026-09 下旬上线（报道有 09-24、09-25 两种说法） |
| 最后收集日期 | 2026-11-28（美东；增量：官方 3 篇——国际版首页、国内版首页（均为 11 月改版后的新首页）、美国区 App Store 页（含 Pro/Pro+/Ultra 内购价格）；社区 1 篇——K姐研究社 09-30 上手文（此前漏收，经 AI工具集 转载页找到原文）；智能涌现「十个核心问题」补 36氪英文版 altUrls，晚点访谈补网易转载 altUrls；`today.ai/articles/` 整段失效（博客、能力页、集成页均返回 409），本轮无法检查博客新文章；Chrome 扩展中国版 11-25 更新到 2026.11.24.26，说明文字未变，不更新页面）；2026-11-10（增量：博客列表最新仍为 10-27；能力页、集成页用 auto 抽取失败，本轮未比对）；2026-11-06（美东；补收用户发来的公众号文章：媒体 2 篇、社区 1 篇）；2026-11-05（美东；第一轮：官方 8 篇、媒体 4 篇，其中 9 篇是旧笔记 learning-ai-agent 的 Today 资料索引引用过的） |
| 实测材料 | 没有：旧笔记的 `agents/personal/today/` 是 2026-11-02 的资料阅读与验证方案，作者注明没有注册、订阅或安装，不迁入 |

## 背景

- 创始人齐俊元（英文署名 Junyuan），曾创办 Teambition，之后在阿里（阿里云盘）、飞书和字节（豆包 PC 端）负责产品。报道称他 2014 年就买下 today.ai 域名。
- 据虎嗅 2026-10-28 的融资报道，Today AI 是上海徐汇的汇翮智能旗下产品，Chrome 扩展的开发者署名为 TODAY AI PTE. LTD.（新加坡）。2026-10-21 宣布首轮融资超过 2 亿美元（IDG、腾讯、五源、蚂蚁、红杉中国、传音等）。
- 两套服务分开：国际站 today.ai 与国内站 todayai.cn 的账号、插件、连接器、套餐都不同，资料要分别标明是哪一边的。

## 收录范围

- 收：Today 的产品说明、功能发布、能力与集成页、浏览器插件和应用商店说明，以及专门写 Today 的报道、实测和团队访谈。
- 官方博客中讲 Today 本身的文章收；占博客多数的 SEO 指南不收，包括介绍竞品的「What is Claude Duet / Grok Bot / Instinct / Manus Cue / Meta Muse / OpenAI Dots / Town AI」、通用指南（best AI personal assistants、how to use AI as personal assistant、AI daily briefing、meeting notes、email calendar privacy、what should AI agent remember、why AI agents need cloud computers、personal agent landscape、personal AI agent use cases、benchmarks explained、Gemini personal assistant、assistant vs agent、personal agent vs work agent 等）。这些文章是厂商写的竞品或品类科普，不是 Today 的一手资料；以后若出现讲 Today 自身机制的段落再个别判断。
- 法律文档（中国服务协议、国际服务条款、两份隐私政策）按 tracking.md 不收。
- 融资快讯、公司新闻（新浪「累计完成超2亿美元融资」、智东西「腾讯联手蚂蚁…」及搜狐转载、格隆汇、融中财经「豆包天才90后，融了13亿」、EqualOcean 英文稿、虎嗅「上海徐汇两家个人Agent公司完成天使轮融资」、36氪「传音投资Today AI」）不收；融资信息已在智能涌现的团队访谈中。

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| 首页 | 国际版 `today.ai/`，国内版 `todayai.cn/` | 产品定位、记忆与主动服务、能力概述；国内版顶部有新用户福利 | 直接下载，`extract.py <html> body`；删页首「Log in / Download」导航，唯一的一级标题降为正文；图片把 `_next/image` 的 `w=3840` 改成 `w=1080` 再下载，基准地址写 `https://today.ai`（结尾不带斜杠，否则拼出 `//today.ai/...` 下载失败）。2026-11-28 起收 |
| App Store（美国区） | `apps.apple.com/us/app/id6760608312`（Today: Personal AI Assistant，开发者 Today AI PTE. LTD.） | 应用介绍、内购价格、版本记录 | 简介用 `itunes.apple.com/lookup?id=6760608312&country=us` 的 `description`；信息栏、内购、版本记录从页面内嵌数据取（`"$kind":"Annotation"`、`textPair`、`TitledParagraph`）。2026-11-26 版 1.28.0 |
| Google Play | `play.google.com/store/apps/details?id=ai.today.android.app` | 应用介绍 | 与 App Store 介绍基本相同，只多几处 SEO 措辞（「daily planner」等），记入 App Store 页的 `altUrls`，不单独收 |
| 支持页 | `today.ai/support`、`todayai.cn/support?language=zh` | 联系方式与常见问题 | 2026-11-28 未收：只有联系邮箱、登录与删号说明、「目前支持 iOS 和 macOS 与 Web」一句，按边缘资料不收 |
| 博客 | `today.ai/articles/blog/<slug>`，中文版 `today.ai/articles/zh-Hans/blog/<slug>`；列表 `/articles/blog` | 产品说明、功能发布、SEO 指南 | 直接下载，`extract.py auto` 可用；JSON-LD 有 `datePublished`、`dateModified`。没有 sitemap |
| 能力页、集成页 | `today.ai/articles/zh-Hans/capabilities`、`/integrations` | 能力与连接器清单 | `auto` 只抽到一小块，用选择器 `body` 再删页首导航和页尾行动号召；集成页中文版的条目说明是英文，几十个 logo 不下载 |
| 场景页 | `/articles/recording`、`/finance`、`/healthcare` 及子页 | 落地页 | 2026-11-05 未收：营销页，内容与能力页、博客重复 |
| Chrome 扩展 | 中国版 `chromewebstore.google.com/detail/edkhmdfegifiidpkfifcoiafjgbopggj`；国际版另有「Today AI」 | 插件说明、隐私披露 | 直接下载，`extract.py auto`，按「概述」「详情」「隐私权」三节取；国际版扩展 2026-11-05 未收 |
| 国内站 | `todayai.cn/landing` | 首页 | 单页应用，静态 HTML 几乎没有文字，未收；`todayai.cn/sitemap.xml` 不存在 |
| 下载页 | `today.ai/downloads` | 桌面安装包（`releases.today.ai`） | 只有下载链接，不收 |

- App Store：应用名是「Today: Personal AI Assistant」，按「Today AI」检索找不到（2026-11-05），按「Today AI personal」能找到（2026-11-28）。Product Hunt 返回 403。
- **`today.ai/articles/` 整段失效（2026-11-28 发现）**：博客列表、文章、能力页、集成页都返回 409，正文是 Cloudflare「Error code: 1001」和 Vercel「DEPLOYMENT_NOT_FOUND」，`sitemap.xml` 也一样；首页、`/downloads`、`/support` 正常。Wayback 上 `today.ai/articles*` 最近的快照是 2026-10-10。已收的博客、能力页、集成页保持原样。下一轮先看这些地址是否恢复或搬到了新路径；首页改版后的能力介绍已收为首页一篇。
- 中英文博客同日发布、内容相同，按同一内容的不同语言版本处理：以中文版为 `sourceUrl`，英文版记入 `altUrls`，`language: zh`，不需要翻译。中文版读来像由英文译出，但页面不说明原文语言，在收录说明里注明。

## 媒体与社区检索

- 中文检索词：`Today AI 齐俊元`、`Today AI 实测`、`todayai.cn`、`Today 个人智能体`
- 英文检索词：`"Today.ai" personal agent`、`Today AI Junyuan Qi`
- 「Today」是常见词，检索时要带「AI」「齐俊元」或域名。
- 中文报道多发在微信公众号（极客公园、Founder Park、智能涌现、量子位），再由虎嗅、36氪、智源社区、新浪转载；按惯例取转载并填 `reprintUrl`。智源社区（hub.baai.ac.cn）的转载页把 Founder Park 的文章标成「极客公园」，以文末署名为准。

## 媒体与社区的判断记录

已收的不再列出（以 `sourceUrl`、`reprintUrl`、`altUrls` 去重）。

| 资料 | 判断 |
| --- | --- |
| 量子位「豆包PC端前负责人，创业Agent操作系统」（闻乐，2026-09-25，智源社区转载） | 不收：上线快讯，以创始人经历和官网介绍为主，没有实测 |
| 人人都是产品经理「豆包前负责人，又做了个AI」（怪哥，2026-09-25） | 不收：评论文，实测例子转述自品玩的体验稿 |
| aicoin「Dialogue Today AI」（2026-09-23） | 不收：聚合站上的机翻文章，原文（某人拜访 Today 团队的中文帖子）未找到 |
| 融资与公司新闻（见收录范围） | 不收 |
| 什么值得买「AI助理还没学会干活，先学会了管人：实测融资2亿的Today」（2026-11-20） | 不收：约 2000 字，内容是转述小红书、知乎上的用户吐槽（推送不能关、连接器调不动、Token 消耗快），没有作者自己的实测，也没有附原帖链接 |
| 前途科技 accesspath.com「实测国产个人AI助手Today」（2026-10-09） | 不收：页面写明「编译自 极客公园」，是已收极客公园十天实测的改写 |
| AI工具集 ai-bot.cn「Today AI 实测」（2026-10-08） | 不收转载：文末注明原文是公众号「K姐研究社」09-30 的文章，已收原文 |
| MarkTechPost「Best Personal AI Agents in 2026」（2026-11-22） | 不收：横评，Today 只出现两次，没有独立信息 |

## 已知问题

- 博客文章的 `dateModified` 多为 2026-09-15（批量修改），按 `updatedAt` 记录。
- 能力页与集成页没有日期，取收集日期；内容会变（旧笔记 11-02 记录集成 55 项，11-05 仍为 55 项），发现变化时覆盖原页面。
- 虎嗅转载中的动图可能超过 600 KB，按规则改为链接。

## 命名约定

- 博客：`<datePublished>-<英文 slug>`；能力页、集成页：`<收集日期>-capabilities` / `-integrations`；扩展：`<更新日期>-chrome-extension-<china|intl>`。
- 中文媒体：`<日期>-<媒体拼音/英文>-<关键词>`，例如 `2026-10-08-geekpark-today-ten-days`。
