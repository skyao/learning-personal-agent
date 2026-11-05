---
name: collect-dots
description: 收集 OpenAI dots（ChatGPT 中始终在线的个人智能体）的资料时使用：dots 的官方渠道、抓取方法、收录范围与已知问题。与 collect-sources 配合使用，通用流程与页面规则见 collect-sources。
---

# 收集 Dots 资料

通用流程、页面模板与翻译规则见 `skills/collect-sources/SKILL.md`。本文件只记录 Dots 特有的内容；与通用规则冲突时，以本文件为准。

## 状态

| 项目 | 值 |
| --- | --- |
| 产品目录 | `content/zh-cn/docs/dots/` |
| 发布日期 | 2026-09-29（OpenAI DevDay 2026 前后发布） |
| 最后收集日期 | 2026-11-05（第一轮完成：官方、媒体、社区。遗留：Reddit「I spent a day poking dots with sticks」待用户手工保存后翻译；WIRED 发布前报道「OpenAI is developing a persistent AI agent」待查） |
| 实测材料 | 用户确认没有（2026-11-05） |

## 收录范围

产品名在官方文档中写作小写的「dots」，单个称「your dot」。只收 dots 产品本身的资料。

| 资料 | 是否收录 |
| --- | --- |
| dots 的发布、帮助文档、learn.chatgpt.com 上的 dots 文档、安全设计 | 收录 |
| 企业文档中专门针对 dots 的页面：dots-security、dots-admin-guide、cloud-local-access（标题含 dots） | 收录 |
| ChatGPT Work 的通用企业文档（agent-security、chatgpt-work-cloud-security、chatgpt-work-local-security、usage-and-cost 等） | 不收：几乎不涉及 dots |
| 模型资料（GPT-6 Astra、GPT-6.1 Terra 的发布文与系统卡） | 按 collect-sources 的「模型资料的收录原则」逐篇判断；dots 文档写明 dots 会在不同工作部分调用不同模型。判断结果见下文「逐篇判断」 |
| ChatGPT 发布说明 | 只按「节选」收其中的 dots 条目，每条一页，date 取条目所在日期 |
| Codex、ChatGPT Work、ChatGPT agent 本身 | 不收 |

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| ChatGPT Learn 文档 | `learn.chatgpt.com/docs/dots`、`/docs/dots/<子页>`；同一页面也可经 `/codex/dots/...` 和 `developers.openai.com/codex/dots` 访问 | 用户文档 6 页：认识 dots、入门、任务与记忆、控制、计算机与应用、消息渠道 | 直接下载；`sourceUrl` 用 canonical 的 `/docs/...` 地址，其余写入 `altUrls` |
| ChatGPT Learn「What's new」 | `learn.chatgpt.com/docs/whats-new/dots-<月>-<日>-2026`；栏目首页 `/docs/whats-new` | dots 专稿（每篇一页）；另有每周汇总和 DevDay 页 | 直接下载；每周汇总与 DevDay 页中的 dots 部分只是专稿和发布文的摘要，不收 |
| ChatGPT Learn 企业文档 | `learn.chatgpt.com/codex/enterprise/<页>` | dots-security、dots-admin-guide、cloud-local-access | 直接下载 |
| OpenAI 官网 | `openai.com/index/` | 发布文、安全文、DevDay 回顾、模型发布 | 直接下载和网页抓取工具都返回 403；改用 Wayback 快照（见 collect-sources 的 source-page.md） |
| 帮助中心 | `help.openai.com/en/articles/<编号>`；有官方简体中文版 `/zh-hans-cn/` | 入门 20001530、隐私安全 FAQ 20001529、工作区管理 20001554；发布说明中的 dots 条目 | 直接下载和网页抓取工具都返回 403；改用 Wayback 快照 |
| 部署安全中心 | `deploymentsafety.openai.com` | 模型系统卡 | 直接下载 |
| 开发者社区 | `community.openai.com`，有「Dots」分类；搜索接口 `/search.json?q=...`，帖子 `/t/<id>.json` | 用户的 bug 报告、功能请求；OpenAI_Support 的回复；版主 VeitB（Leader，非员工）转帖官方更新 | 直接下载；用户主页 `/u/<name>.json` 的 `title` 可区分「OpenAI Staff」与社区版主 |

## 社区论坛的收录规则

community.openai.com 的 Dots 分类帖子量大，以 bug 报告和功能请求为主。用户 2026-11-04 决定：

- 只收与模型原则直接相关的帖子，即用户实测观察到 dots 运行时使用了哪个模型、模型如何切换的帖子。归 `community/`，全文翻译，收集说明写明作者身份、有无官方回复。
- 其余 bug 报告、功能请求一律不收，即使其中透露了实现机制（工具名、授权规则、子智能体上限等）。这类机制等媒体或研究者写成文章后再收。
- 版主或员工转帖的官方更新不收，改收原始出处。

已判断的帖子：

| 帖子 | 判断 |
| --- | --- |
| rabbitdaisuke「OpenAI is A/B testing a downgrade of dots to GPT-6.1 Sol Low」（10-16，1406784） | 收 |
| cryptocean「Written dot-to-Work instructions blocked as untrusted delegated authorization」（10-19，1407667） | 不收：机制类 bug 报告 |
| SylvesterX「Subagent Limits, Task Cleanup, and Permission Recovery Issues」（10-01，1402568） | 不收：机制类 bug 报告 |
| 2018wzh「Dot cannot resume after safety pause: HTTP 409」（10-02，1402937） | 不收：bug 报告 |
| speedbot「Verifying ChatGPT Dot provenance in MCP requests」（10-02） | 不收：提问，无回复 |
| theweathersobreezy「Scaling Dots to 1B users & some tips」（10-27） | 不收：功能建议 |

## 媒体与社区检索

- 英文检索词：`OpenAI dots agent`、`ChatGPT dots always-on agent`、`"your dot" ChatGPT`
- 中文检索词：`OpenAI dots 智能体`、`ChatGPT dots`
- 「dots」是常见词，检索时要带上 OpenAI 或 ChatGPT。

## 媒体与社区的判断记录

已收的不再列出（以 `sourceUrl` 去重）。以下是判断过、没有收或待处理的，避免下一轮重复判断。

| 资料 | 判断 |
| --- | --- |
| TechCrunch、TechRadar、BGR、PYMNTS、Decrypt、INSIDE（繁中）等发布报道 | 不收：复述发布文；发布报道只收 CNBC 直播稿中的 dots 条目（有 Altman、Friar 原话） |
| WIRED「OpenAI’s Dots Are Always-On AI Agents」（09-29） | 不收：复述发布文，新信息仅订餐演示与短信候补名单 |
| WIRED「The Battle to Be Your Personal AI Agent Is Here」（09-30） | 跨产品，已在 industry 建仅链接页 |
| GPT-6.1 Astra 被搁置（WSJ 一手，Engadget、Yahoo、Zvi、The Hacker News、CNBC 转述） | 不收：报道称该模型原计划用于 ChatGPT 与 Codex，未说明与 dots 的关系；把两者挂钩的只有 SEO 站点 |
| IT之家「dots 首次公开演示卡壳」（经凤凰网） | 不收：现场事件短讯，不涉及技术实现 |
| Flavio Copes「A deep dive into OpenAI dots」 | 不收：逐节复述官方文档，无实测 |
| cedrickchee 的 GitHub gist「I tried OpenAI Dots」 | 不收：简短观点，实测信息只有一条（云端计算机为 Linux，预装 Blender） |
| The Neuron「My First Day With OpenAI Dots」（Corey Noles） | 不收：主观体验为主，技术细节转引官方文档 |
| preuve.ai、ai.joaoqueiros.com（Pat Simmons 视频转写）、animaapp、aiagentslibrary、orcarouter、explainx、mindstudio、eesel、composio、datacamp、promptessor、beam.ai 等 | 不收：营销、聚合或 SEO 站点 |
| The Information「OpenAI Announces ‘Dots’ Agents」简报 | 不收：付费墙（403），无法读取 |
| future-stack-reviews.com「ChatGPT Dots, Tested」（Takashi Fujino，10-09） | 已收节选：页首测试概况与第 05、06、10 节（用户 2026-11-04 决定）；其余各节是模板、FAQ 与文档转述 |
| Reddit r/OpenAI「I spent a day poking dots with sticks」（1wuznlr） | 待用户手工保存：直接访问 403，Wayback 快照只有空壳页；Slide Factory 一文转述了其要点。用户保存后按社区资料全文翻译 |
| X 用户 ChrisUniverse 的「dot 擅自给市政府发邮件」帖（2026-10-02） | 不收：没有实证（一手帖无法读取，只有 orcarouter、explainx 转述，OpenAI 未确认），按 collect-sources 的「没有实证的说法」规则处理（用户 2026-11-04 决定） |
| WIRED「OpenAI is developing a persistent AI agent」（发布前报道） | 线索，待查 |

## 已知问题

### learn.chatgpt.com

- 页面不标日期，也没有结构化日期，`date` 取收集日期。
- 页面夹带界面示意组件（模拟聊天、浏览器、Slack 窗口），抽取后是零散文字，整理为「（界面示意：……）」段落并翻译其中的文字。
- 示例提示在页面中以卡片和可复制文本各出现一次，只保留一次。
- 页内相对链接 `/codex/...` 改为 `https://learn.chatgpt.com/codex/...`。
- 图片在 `/images/codex/dots/` 下，直接下载。

## 逐篇判断

| 资料 | 结论 | 理由 |
| --- | --- | --- |
| GPT-6 Astra 系统卡（deploymentsafety.openai.com/gpt-6-astra） | 节选收第 12 节「Dots」 | 2026-09-29 新增的 dots 专章，评估 dots 运行框架、时间预算、确认策略与自动审查；正文其余部分是模型本身的评估，不收 |
| GPT-6.1 Terra 发布文 | 不收 | 全文不提 dots |
| DevDay 2026 回顾 | 不收 | 20 多条公告中 dots 只有一条两句话，内容与发布文开头重复 |
| 发布说明「Meet your dot」（09-29）与「Texting your dot」（10-28） | 节选收 | 前者含首月用量不计额度的说明；后者是短信功能上线，含第三方服务商 Linq |
| 系统卡正文中的模型评估、Sol、Luna 附录 | 不收 | 模型资料，与 dots 无直接关系 |
| learn.chatgpt.com/docs/changelog | 不收 | 正文没有 dots 条目，只在导航中出现 |
| What's new 专稿 dots-october-9-2026、dots-october-28-2026 | 收 | 官方更新；10-28 篇比发布说明多出渠道选择与批准链接的说明 |
| 社区论坛 VeitB「Fresh dots updates」（10-09） | 不收 | 版主转帖，原文即 What's new 专稿 |
| 社区论坛 VeitB「Dots are now available in the EU on Business and Enterprise plans」（10-28） | 不收 | 转引 X 上 Thomas Ricouard 的帖子；learn 文档 Access 一节已写明 Business Premium 与 Enterprise「正在全球推出」 |
| 社区论坛 vc-openai「About the Dots category」 | 不收 | 分类说明，无内容 |

系统卡页面是单页长文，正文链接用 `#section.N` 锚点和 `/gpt-6-astra/<章节>` 路径，收录时都改为 `https://deploymentsafety.openai.com/...` 绝对地址；图在 `/data/eval-sets/gpt-6-astra/assets/images/dots-N.png`，可直接下载。

## 命名约定

- learn.chatgpt.com 的文档 slug 以 `docs-` 开头，例如 `2026-11-05-docs-meet-dots`。
- 帮助中心文章 slug 以 `help-` 开头。
- What's new 专稿 slug 以 `docs-whats-new-` 开头，日期取 slug 中的日期。
- 发布说明节选 slug 以 `relnotes-` 开头，例如 `2026-10-28-relnotes-texting-your-dot`。
