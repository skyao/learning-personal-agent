---
name: collect-poke
description: 收集 Poke（The Interaction Company of California，2026-07 起加入 Cognition）的资料时使用：Poke 的官方渠道、抓取方法、收录范围与已知问题。与 collect-sources 配合使用，通用流程与页面规则见 collect-sources。
---

# 收集 Poke 资料

通用流程、页面模板与翻译规则见 `skills/collect-sources/SKILL.md`。本文件只记录 Poke 特有的内容；与通用规则冲突时，以本文件为准。

## 状态

| 项目 | 值 |
| --- | --- |
| 产品目录 | `content/zh-cn/docs/poke/`（2026-11-09 建立） |
| 时间线 | 2025-09-08 公开发布并宣布 1500 万美元种子轮（General Catalyst 领投，估值 1 亿美元；据官方新闻稿与领投方文章）；2026-03 TechCrunch 称「publicly launched in March」，与 2025-09 的发布说法并存，按原文照录不作判断；2026-04-08 TechCrunch 报道追加 1000 万美元、投后估值 3 亿美元；2026-06-04 成为首个获准上 Apple Messages for Business 的 AI 智能体；2026-07-23 Cognition 宣布「welcoming」The Interaction Company，产品照常运营；2026-11-17 发布说明与首页推广 Cognition 的 Devin Bots（在 Apple Messages 上向 Poke 争取免费额度） |
| 最后收集日期 | 2026-11-28（美东；增量：官方 2 篇原文更新——发布说明页首新增 11-17「Devin Bots」条目、首页横幅改为「Introducing Devin Bots」并新增推广卡片，均改回待翻译；其余 10 个官方页面无实质变化；媒体与社区未见 11 月新报道）；2026-11-10（增量：官网、价格页与文档比对无实质变化；媒体未见 11 月新报道）；2026-11-09（美东；第一轮：官方 13 篇、媒体 4 篇、社区 1 篇，industry 1 篇；旧笔记 learning-ai-agent 的 Poke 资料索引已逐条对照，隐私声明按 tracking.md 不收） |

## 背景

- 帕洛阿尔托初创公司 The Interaction Company of California，创始人 Marvin von Hagen、Felix Schlegel。Cognition（Devin 的开发商）公告没有明说是收购；poke.com 写的是「Poke is joining Cognition」。
- 没有独立 App：通过 iMessage、SMS、WhatsApp（部分市场）、Telegram 交互。
- 接入 Gmail、Google Calendar、Outlook、Notion、Asana、Linear、Todoist、Granola、GitHub、Strava 等；能起草和发送邮件、整理收件箱、建提醒；有记忆，会主动发消息。开发者可在 Poke Kitchen 自建 recipe 与集成。
- 价格（2026-11-06 官网）：Free $0；Pro $19/月（前沿模型、后台实时自动化）；Ultra $199/月（每次操作用前沿模型，超出额度按量付费）。
- 官网首页没有说明权限、审批与对外通信的控制设计，第一轮收集时到帮助文档或 FAQ 中找。

## 收录范围

- 收：poke.com 的官方页面与公告、帮助文档、Cognition 关于 Poke 的公告、专门写 Poke 的报道和实测、创始人访谈（有文字稿或节目页文字时）。
- 法律文档按 tracking.md 不收。
- 首页的用户推荐语是宣传材料，不作为实测证据。
- Cognition 把 Poke 的风格带到 Devin 的资料：只讲 Devin 编程能力的不收；明确说明 Poke 产品变化的收。

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| 官网 | `poke.com`（首页、`/pricing`、`/faq`） | 产品介绍、集成、价格、常见问题 | curl 直接下载即可（Next.js 静态渲染） |
| 帮助文档 | `poke.com/docs/*` | 欢迎页、Managing Integrations、Merging Accounts、Creating Recipes、MCP Servers、API、Release Notes、Usage & Resets | curl 直接下载；`poke.com/llms.txt` 列出文档页（但漏了 `usage-and-resets`）；没有 sitemap 和 robots.txt |
| 新闻稿 | WebWire `ViewPressRel.asp?aId=343533` | 2025-09-08 发布新闻稿 | 页面是 Windows-1252 编码，先 `iconv -f windows-1252 -t utf-8` 再抽取 |
| Cognition 博客 | `cognition.com/blog/interaction` | 2026-07-23 加入 Cognition 的公告 | curl 直接下载 |
| Poke Kitchen | `poke.com/kitchen` | 开发者 recipe、API key | 需要登录，不收；说明见文档 Creating Recipes 与 API |
| Devin Bots 推广页 | `poke.com/bots` | 2026-11 的限时活动：在 Apple Messages 上向 Poke 说明想法，争取 Devin Bot 免费额度 | 不收（见「已知问题」） |
| X 账号 | `x.com/interaction` | 发布公告（如 2026-03 上线、2026-06-04 Apple Messages） | X 不能自动读取，不收；需要时引用报道中的嵌入推文 |

## 媒体与社区检索

- 英文检索词：`Poke AI assistant`、`Poke iMessage agent`、`poke.com Interaction Company`、`Poke Cognition`
- 中文检索词：`Poke AI 助理`、`Poke 短信 智能体`
- 「Poke」是常见词（还有 poke 菜品、Facebook 的 poke 功能），检索时要带 AI、iMessage 或 Interaction。
- 重点媒体：TechCrunch 的 Sarah Perez（2026-04-08、06-04、07-24 三篇都是她写的）。TechCrunch 的短信类智能体合集（Lauren Forristal）会持续更新、换日期地址（10-03、10-10、10-24），已收入 industry。
- 检索结果中有大量 SEO 与聚合站（dealroom、aidirectory、poster.ly、theaiagentindex、neuronfeed、runtimewire、justthink 等），不收。

## 已知问题

- 文档页、首页、价格页、FAQ 都没有标发布或更新日期，`date` 取收集日期。Release Notes 的 `date` 取最新条目的日期（与 grok-bot 更新日志的做法一致）。
- 首页有桌面版和手机版两套重复的头图区块，抽取后只保留一套；首页的用户推文推荐照录，但它们是宣传材料。
- 价格页的套餐对比表用 SVG 图标（`aria-label="Included"`）表示包含，抽取前先把图标换成「✓」，否则表格是空的。
- TechCrunch 的短地址 `?p=3110530` 会跳到 04-08 那篇，不是 06-04 的 Apple 报道；06-04 的正式地址是 `2026/06/04/apple-approves-poke-as-the-first-ai-agent-on-its-messages-for-business-platform/`。这篇文末有更正：Poke 付费的对象是它的消息服务商，不是 Apple。
- TechCrunch 短信智能体合集的原地址现在返回 404，取自 Wayback 快照。
- Product Hunt 上 Gabe Perez 的一周评测（2025-09）：原站返回 403，Wayback 只有一个快照，下载时返回 404，未收。
- Sources with Alex Heath 的播客（2026-04-09，有 Marvin von Hagen 访谈）没有文字稿，节目页也几乎不谈 Poke，不收。
- 中文报道多是编译（智东西/新浪、IT之家、iThome），复述 TechCrunch，不收。9to5Mac、AppleInsider 的 06-04 报道复述官方公告，不收。
- Unite.AI 评测有多语言机器翻译版（`/zh-cn/`、`/ja/` 等），收英文原文，中文版记入 `altUrls`。
- 第三方「研究」页（rywalker.com/research/poke）只是在复述官网和 FAQ，没有新信息，不收。

## 比对已收页面

- 官方页面（文档 7 页、首页、价格、FAQ、Cognition 公告）用一个脚本批量下载、`extract.py` 抽取，再与 `original.md` 去掉开头两行后比对。新抽取结果有三类格式差异，不是原文变化，比对前先归一化：标题带站内锚点链接（`## [标题](#锚点)`，用 `sed -E 's/^(#+) \[(.*)\]\(#[^)]*\)$/\1 \2/'` 去掉）、页面标题是一级标题（存档里已降为普通文本）、站内链接是相对地址（存档里已改成绝对地址）；x.com 链接的 `?s=20` 是跟踪参数，存档里已去掉。
- 首页的桌面版、手机版头图和推文轮播重复，存档只留一份；比对时去掉标题符号、图片和链接地址，只比文字行，差异集中在头部几行时，在存档原位置手工插入新内容，不整页重存。价格页新抽取结果多出手机版套餐切换区块（内容与对比表重复），也不算变化。
- 2026-11-28 判断记录：发布说明 11-17 条目只在页首追加，保留旧译文、只补译新增；首页新增内容在中间（横幅替换、头图后的卡片），按 source-page.md 删去旧译文、整页重译。`poke.com/bots` 推广页主要介绍 Devin Bots 的编程与浏览器能力，跟 Poke 相关的只有「Convince Poke how many free credits you deserve. Available on Apple Messages only.」一句，按「只讲 Devin 的不收」处理，这次活动由发布说明与首页的更新记录。`docs.devin.ai/work-with-devin/bots/imessage.md`（Devin Bot 的 iMessage 接入）不提 Poke，不收。媒体检索只见 6–7 月旧报道的复述（letsdatascience、startupfortune、gadgethacks、beebom、mezha 等），不收。

## 命名约定

- 目录名用 `poke`。
