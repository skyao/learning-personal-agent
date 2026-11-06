---
name: collect-muse
description: 收集 Meta Muse（Meta 的个人 AI 智能体）的资料时使用：Muse 的官方渠道、帮助中心的抓取方法、收录范围（与 Muse 模型家族的边界）与已知问题。与 collect-sources 配合使用，通用流程与页面规则见 collect-sources。
---

# 收集 Muse 资料

通用流程、页面模板与翻译规则见 `skills/collect-sources/SKILL.md`。本文件只记录 Muse 特有的内容；与通用规则冲突时，以本文件为准。

## 状态

| 项目 | 值 |
| --- | --- |
| 产品目录 | `content/zh-cn/docs/muse/` |
| 发布日期 | 2026-09-08（美国） |
| 最后收集日期 | 2026-11-06（另收用户发来的公众号文章：社区 1 篇，橘AI；对照旧笔记补收媒体 1 篇：Bloomberg 嘉信理财拦截 Muse；22:16 轮次补跑：官方语音稿、墨西哥上线、TechCrunch、The Verge、DataCamp 横评、Medium Muse 101 与六产品横评（仅链接待补原文）、coderlegion、PYMNTS Expedia、语音悄悄上线回填；本轮补跑：Yahoo 理财评测、iFynx Secure VM 解析，industry 收 freistyle 六产品横评、老张入门成本对比、Kunal 收件箱实测（仅链接）；发布稿西语版 11-05 墨西哥更新记入 altUrls；Medium Muse 101 与六产品横评已改用转载全文）；2026-11-05（第一阶段完成：官方、媒体、社区、实测；行业综合横评为「仅链接」占位）。下一轮起按新流程：原文存 `original.md`，资料页只写摘要与保留理由，不翻译 |
| 页面格式 | 与所有产品一致，见 collect-sources 的 source-page.md「页面正文」。第一阶段直接翻译的旧页面已于 2026-11-06 补上内容摘要、保留理由和分隔线（用户 2026-11-06 要求） |

## 收录范围

「Muse」既是 Meta 个人 AI 智能体产品的名字，也是 Meta 模型家族的名字。只收与 Muse 个人智能体产品相关的资料：

| 资料 | 是否收录 |
| --- | --- |
| Muse 产品的发布、更新、地区上线、帮助文档、安全设计、条款 | 收录 |
| Muse for Small Business、Muse 眼镜端、Muse for Windows / Mac、Gadgets 与设备接入 | 收录 |
| 模型资料 | 按 collect-sources 的「模型资料的收录原则」逐篇判断：明确说明为 Muse 优化、用于驱动 Muse，或说明 Muse 运行时如何选择模型的才收 |
| Muse Code（终端编程智能体）、Muse Image / Muse Video（生成模型）、Meta Enterprise Platform | 不收 |
| 法律文档：Muse 服务条款、Muse 隐私政策、连接器平台条款、Gadget SDK 条款、眼镜自定义唤醒名隐私声明 | 不收（用户 2026-11-04 决定，见 collect-sources 的「不收的资料类型」） |
| 边缘资料：订阅中心的 6 篇子文章、Gadget SDK 子目录 README | 不收（用户 2026-11-04 决定） |

模型家族中各篇的判断结果记在下面，避免下一轮重复判断：

| 模型资料 | 判断 |
| --- | --- |
| Muse Wonder 新闻稿（about.fb.com，2026-10-12） | 收：说明将驱动 Muse，并为个人智能体处理私人信息做了训练 |
| Muse Wonder 研究博客（research.meta.ai，2026-10-12） | 收：同上，另说明将用于 artifact 生成 |
| Muse Wonder 模型卡 PDF（`research.meta.ai/static/muse-wonder-model-card`，研究博客链接） | 收节选（用户 2026-11-05 决定）：只收模型概况、预期用途、个人与专业智能体一组基准的方法与分数、局限与使用条件；不收编码与通用基准、前沿风险评估、Trust and Safety、附录。分数表是 PDF 内嵌图片，用 pypdf 提取后转录 |
| Muse Realtime Avatar（research.meta.ai，2026-09-23） | 收：Muse 应用中的头像功能 |
| Muse Spark Open（research.meta.ai，2026-10-15） | 不收：全文未提及 Muse 产品 |
| Muse Glimmer（research.meta.ai，2026-08-10） | 不收：端侧开放模型，全文未提及 Muse 产品 |
| Ray-Ban Meta Audio 发布稿（about.fb.com，2026-09-23） | 不收：只有一句提到 Muse |
| Meta Enterprise Platform 发布稿（about.fb.com，2026-09-28） | 不收：企业平台，非 Muse 产品资料 |
| Building Windows for hybrid intelligence（微软 Windows 博客，2026-10-07） | 不收：Windows 平台公告，只有一句提到 Muse for Windows 即将推出 |

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| Meta Newsroom | `about.fb.com/news/`（AI 标签：`about.fb.com/news/tag/ai/`） | 发布、地区上线、Connect、小企业 | 直接下载 |
| Meta 消费者博客 | `www.meta.com/blog/` | 眼镜端、Connect 汇总等面向消费者的公告 | 直接下载；日期取页面显示日期 |
| Meta Newsroom 日文版 | `about.fb.com/ja/news/` | 日本上线等日本专属公告 | 直接下载；日文资料与英文一样按外文资料处理 |
| Muse 博客 | `muse.ai/blog` | 设计、安全、赏金回顾 | 直接下载；列表页可取全部文章链接 |
| 设计文章 | `introducing.muse.ai` | 我们如何设计 Muse | 直接下载 |
| 安全文章 | `security.muse.ai` | 我们如何将安全构建进 Muse | 直接下载 |
| Meta 研究博客 | `research.meta.ai/blog/` | 模型发布、实时 Avatar 等技术文章 | 直接下载；先按「收录范围」判断 |
| 模型卡 | `research.meta.ai/static/` | 模型卡 PDF | 下载 PDF 后抽取文本 |
| Meta 帮助中心 | `www.meta.com/help/superintelligence/<编号>/` | Muse 帮助文档，约 14 篇以上 | 正文由脚本渲染，见「已知问题」 |
| 订阅帮助 | `www.meta.com/help/subscriptions/<编号>/` | Muse 订阅 | 同帮助中心 |
| 眼镜帮助 | `www.meta.com/help/ai-glasses/<编号>/` | 眼镜端 Muse Beta | 同帮助中心 |
| 产品页 | `ai.meta.com/muse/` | 产品功能介绍 | 直接下载和抓取工具都只能拿到标题，需要能执行脚本的浏览器；2026-11-04 未收 |
| 连接器开发指南 | `platform.muse.ai/docs` | 自定义连接器规范 | 直接下载 |
| Gadgets | `gadgets.muse.ai`、`github.com/facebookincubator/muse-gadget-sdk` | 设备接入 | 直接下载；仓库收 README 与文档，不收代码 |
| 漏洞赏金 | `bugbounty.meta.com/payout-guidelines/muse/` | Muse 赏金规则 | 正文由脚本渲染，用抓取工具；金额阶梯以堆叠标签呈现，整理为表格并加译注 |
| 条款 | `agent.meta.ai/terms` | Muse 服务条款 | 直接下载 |

## 媒体与社区检索

- 英文检索词：`Meta Muse agent`、`Muse personal AI agent`、`Muse Secure VM`、`Muse Sentinel`
- 中文检索词：`Meta Muse 智能体`、`Muse 个人智能体`、`Meta Muse 实测`
- 检索时排除与产品无关的同名结果：Muse 乐队、muse.ai 早期的视频托管服务、其他名为 Muse 的应用。

## 媒体与社区的判断记录

已收的不再列出（以 `sourceUrl` 去重）。以下是判断过、没有收或待处理的，避免下一轮重复判断。

| 资料 | 判断 |
| --- | --- |
| Forkast（forkast.news）的 Sentinel 架构文与 macOS 后门文 | 不收：署名为「Forkast mind」，疑似 AI 批量写作；macOS 漏洞改收 Wardle 的原始披露 |
| Tech Jacks Solutions「What Is Meta Muse」 | 不收：聚合型 SEO 站点 |
| aiweekly.co、letsdatascience.com、gadgetreview、threatintel、madrobot 等 | 不收：转述聚合站 |
| Gizmodo、The Next Web、SiliconANGLE、The Decoder 等关于亚马逊屏蔽的报道 | 不收：一手报道是 GeekWire（已收） |
| IT之家对 Reuters、官方公告的转述（如人工客服、Gadgets、Windows、Wonder） | 不收：中文复述，无新信息 |
| DigitalToday 中文版、英文版（分享暂停、日本扩张） | 不收：复述 Ars Technica 与官方公告 |
| 人物档案事件（WIRED、TIME 原文无法读取） | 已收 Medianama 的二手报道并填写 `basedOn`（用户 2026-11-04 决定）；Malwarebytes、IBTimes、dig.watch 不再收 |
| Reuters 人工客服测试报道 | 不收（用户 2026-11-04 决定）；一手报道是 404 Media 2026-09-22 的「Meta Tests Muse AI Agent Calls…」，已收 |
| Fox News 情感陪伴报道、Subscription Insider 订阅管理分析 | 不收（用户 2026-11-04 决定） |
| Q3 2026 财报电话会 | 不收（用户 2026-11-04 决定） |
| CNBC「Humans are still doing the work behind some AI agents」（2026-10-31） | 放入行业综合（仅链接）：主体是 Dazzle、Duckbill 等创业公司，Muse 只有一段 |
| 多产品横评（WIRED、纽约时报、Axios、Claire Vo、Pat Simmons、AI Agents Library、CNBC 2026-09-30） | 已放入行业综合；2026-11-05 已补抓原文（original.md，待翻译），Claire Vo 只有节目页，缺访谈文字稿 |
| David Senra 播客对 Alexandr Wang 的访谈 | 不收：无文字稿（音视频规则，用户 2026-11-05 决定） |
| Zuckerberg 在 Sources 播客的访谈（sources.news） | 已收：按节目页文字收录，不含完整访谈 |
| 纽约时报 The Daily 播客「Call My A.I. Agent」（Eli Tan） | 不收：无文字稿 |
| The Verge 关于 Muse 文件系统与夜间回顾的报道 | 已收；同时收了一手来源 mouse.dev（Peter James）和后续「分享功能恢复」 |
| Hunter Brook「Dox for me, O Muse」 | 已收 |
| Marketplace 住址事件 | 已收卫报报道（Business Insider 首发但有付费墙）；Malwarebytes 转述、EPIC 评论不收；Surfshark 数据收集分析页日期异常，不收 |
| 人物档案事件 | WIRED 2026-10-03 原文已收；Medianama 二手报道保留（用户 2026-11-05 决定；其转述的是 TIME，内容不完全重合）；TIME 原文仍无法读取 |
| Future Society「Muse, in its own files」（futuresociety.ch/muse-findings） | 已收：页面自标「由 AI 生成」，但每条发现附 VM 文件引文；发现列表取自 report_data.json |
| Wardle 在 Objective by the Sea v9 的演讲 | 已建「仅链接」占位页，会后补全 |
| Tom's Guide「Meta Muse vs ChatGPT Dots」（2026-09-30）、Engadget「OpenAI Dot vs. Meta Muse」（2026-10-11） | 已收入行业综合（2026-11-05） |
| DataCamp「OpenAI Dots vs Meta Muse」（`datacamp.com/blog/openai-dots-vs-meta-muse`） | 已收（2026-11-05 补跑）：原站 403 已解除，直接下载全文；价格表称 Muse「仅限美国」，与 10 月 23 日日本、10 月 27 日新加坡上线不符，照录原文 |
| Meta Newsroom「Give Your Muse a Voice」（2026-11-05） | 已收（2026-11-05）：官方，实时语音与表情化身美国上线 |
| allthingsmuse「Muse Launches in Mexico」（2026-11-05） | 已收（2026-11-05）：媒体，墨西哥上线；官方首发为 Wang 与 @Muse 的 X 帖，Newsroom 英文站未见专门稿，但西语新闻中心 11 月 5 日在发布稿西语版追加了墨西哥上线更新（本地连接器另含 Walmart México），已记入发布稿页 altUrls 与本页收录说明 |
| TechCrunch「Meta says US users can now video chat with their Muse AI avatar」（Sarah Perez，2026-11-05） | 已收（2026-11-05）：媒体，语音视频聊天美国上线；补充 Wang 的 X 演示、Jolly 昵称、Charm 年底前发布 |
| The Verge「Muse has a voice mode now」（Jay Peters，2026-11-05） | 已收（2026-11-05）：媒体，iOS 上手实测；原文地址经站内搜索定位（theverge.com/tech/1028015/…），Daily Guardian 转载与原文逐段一致 |
| Medium「Muse 101」（Tim de Rosen，AIVO，2026-11-04） | 已收（2026-11-06 改用 AIVO Journal 全文转载，fidelity 转载全文，翻译已完成）：社区，独立分析（Three Gates 框架、投行预测验算）；Medium 403 且 Wayback 无快照；文末约 15% 为自家产品推广 |
| Medium「Proactive AI Agents in 2026」（Bishakh Ghosh，2026-11-03） | 已收（2026-11-06 改用 AIWithGhost 全文转载，fidelity 转载全文，翻译已完成）：industry 六产品横评，OpenClaw/Hermes 两节为实测；Medium 403 且 Wayback 无快照 |
| Medium「Claude Duet vs Muse vs dots」（Mike Written，AI Trends 24，2026-11-05） | 不收：二手拼贴、非实测；Muse 准入写成仅限美国，与 11-05 墨西哥上线冲突；无可核查出处，含占位符与自售广告 |
| coderlegion「One Config Key Was Enough」（Alessandro Pignati，2026-11-02） | 已收（2026-11-05）：社区，Wardle macOS 漏洞的独立分析（企业可见性缺口）；作者为 NeuralTrust 研究员，VentureBeat 引述为二手转述；默认抽取漏正文，取 div.qa-q-view-content 容器 |
| PYMNTS「Expedia Says Travelers Plan With AI Agents but Book Direct」（2026-11-04） | 已收节选（2026-11-05）：媒体，Expedia-Muse 集成预计美国上线；全文主题为 Expedia 财报，仅摘录 Muse 相关四段 |
| allthingsmuse「Live Voice Conversations With Muse Start Reaching Users」（2026-10-25） | 已收（2026-11-05）：媒体回填，10-24 语音悄悄上线首报；一手来源为 TestingCatalog 10-25 帖与 Gambrill 10-24 帖，本文据 FourWeekMBA 转述 |
| eWeek「Meta Muse $300,000 Bug Bounty Security Flaw Explained」（2026-11-05） | 不收：复述已收官方 11-02 赏金回顾，无新信息 |
| Lenny's Newsletter「How I AI: Grok vs. Dot vs. Muse vs. Duet」（2026-11-02） | 与已收 industry 条目 2026-10-28 Claire Vo 同一期节目，记为该条目的 altUrls，不另收；11-02 页含完整书面结论，日后可用于补全该条目 |
| The Information 人形机器人 Max 报道（2026-10-31，付费墙）与 Engadget 转述（2026-11-01） | Engadget 版不收：抓取到的正文未提及 Muse；一手报道付费墙未读，改收下行 NDTV 版 |
| NDTV「Zuckerberg Wants To Give AI A Body」（2026-11-02） | 收：媒体类，全文翻译，basedOn 填 The Information；Max 定位为 Muse 的潜在实体形态，Max 2 自 9 月开发中，Meta 称仅内部研究、无销售计划 |
| Engadget 上手指南「How to get started with Meta's new AI agent, Muse」（Karissa Bell，2026-09-12） | 已收（2026-11-05）：媒体类一手上手实测，含设置、权限、连接器操作细节与菜谱整理、旅行规划两项真实任务；三张作者截图已本地化，首图插画未收 |
| Tom's Guide「I used Muse to automate 10 tasks」（Elton Jones，2026-10-07） | 已收（2026-11-05）：媒体类，为期一周的 10 项持续执行实测，逐项给出提示词原文与结果；配图均为图库装饰图，未收 |
| Tom's Guide「I tested Meta Muse vs ChatGPT-6 with 5 prompts」（Amanda Caswell，2026-09-27，更新 09-28） | 已收（2026-11-05）：放入 industry，逐轮打分的实测对比，Muse 3-2 胜；配图均为图库装饰图，未收 |
| Sitedex「Meta Muse agent and your website」（2026-11-01） | 已收（2026-11-05）：社区类，独立核查 Meta 爬虫清单与 Web Bot Auth 密钥目录；文末推广自家 fetchcheck 的两处已去掉 |
| Medium「Meta Muse for Startups」（MyNextDeveloper，2026-11-05） | 不收：二手汇总，无新信息；提到的 Claroc、404 Media、Wardle、Marketplace 事件均已收 |
| AllThingsMuse 人形机器人 Max 报道（2026-11-02） | 不收：NDTV 已收的同一事件二手转述，无新信息 |
| Zacks「META Q3 Earnings Call Put Spotlight on Muse Growth」（2026-11-03） | 不收：财报电话会已决定不收（用户 2026-11-04 决定）；文中 1000 万用户、25% 日活等数据出自该电话会 |
| aiagentslibrary「Meta Muse Wonder: Who Gets Access」（约 2026-10-31） | 暂不收：聚合站；其中「Wonder 已用于 Muse 付费档、免费档仍为 Spark」一事源自 10 月 21 日财报电话会（已决定不收），是否记录这一模型切换事实待 Sky 决定 |
| 谢华健翻译资讯网 Muse Charm 稿（2026-11-05） | 不收：9 月 23 日 Connect 发布内容的滞后转述，Charm 已收于 Connect 官方页；该站为翻译聚合站 |
| johnmaartifacts Substack 四产品对比「Meta Muse vs. Grok Bot vs. Instinct vs. ChatGPT Dots」（约 2026-10-26） | 候选，未判断：同一周真实任务跑四款产品，但涉及 dots、Grok Bot、Instinct 等未纳入跟踪的产品，是否收 industry 待 Sky 决定 |
| Yahoo Finance「Meta's Muse says it can manage your money. Should you let it?」（Kendall Little，2026-09-25，更新 10-22） | 已收（2026-11-06）：媒体，理财功能评测 + ITRC 采访；Yahoo 直接访问被策略拦截，改用 Wayback 10-06 快照（9 月 25 日原版）转载全文；线上版 10-22 更新内容未收录，核对确认其中无 Schwab 相关内容 |
| iFynx「Meta Muse Secure VM & Confidential VM Explained」（2026-09-16，更新 11-02） | 已收（2026-11-06）：社区，Secure VM/Confidential VM 独立技术分析；直接下载 403，改用网页抓取工具取文；含 10 月 20 日 Confidential VM 设置页传闻 |
| Freistyle「AI Agents Compared: Dots, Duet, Gemini, Muse, Grok」（Dominic Frei，2026-11-05） | 已收（2026-11-06）：industry 社区，六产品横评（准入、价格、数据治理）；文中称 Muse「仅限美国」与事实不符，照录；作者声明参加 Anthropic 创业计划 |
| 老张「ChatGPT Dots vs Meta Muse vs Grok Bot vs Claude Duet: Entry Costs」（2026-10-01，更新 11-02） | 已收（2026-11-06）：industry 社区，四产品入门成本与用量规则对照；明言未做同任务实测，结论均据厂商公开文档 |
| Medium「Grokbot X Muse: The Inbox Test」（Kunal Ugale，2026-10-29，更新 10-31） | 已收「仅链接」（2026-11-06）：industry 社区，真实收件箱对照实测；Medium 403 且 Wayback 无快照，未找到完整转载；摘要依据搜索索引摘录，原文待补抓 |
| Meta 收购 Conductor（2026-11-04，Axios 首报） | 不收：编码智能体方向，团队加入 Meta Superintelligence Labs 做新界面，属 Muse Code，不收 |
| ontheground「Personal AI Agents Compared」（Haojun See，2026-11-03） | 不收：内容浅，仅复述厂商公告，无实测与独立分析；同类横评已有更详尽的 freistyle 与老张两篇 |
| Todd Phillips Substack「Agentic AI Factoid #3A: Indirect Prompt Injection」（2026-10-16） | 不收：法律伦理评论为主，Muse 内容（Marketplace 地址、#MuseMoneyChallenge）已收；提示注入分析在 3B 篇，不在本文 |
| X 单帖盲测四智能体（@AnalystAIlab，2026-10-27） | 不收：X 单帖，无全文页面；分数摘要（Grok Bot 邮件 96 分领先，Muse 四项均落后于 Grok Bot）记入本轮报告 |
| YouTube「Muse vs dots vs Grok Bot: The FREE One Almost Won」（2026-10-13） | 不收：视频，无文字稿（Grok Bot 44.5、dots 43.5、Muse 42.5，满分 47） |
| basinautomations「How I use Grok Bot to run my inbox and calendar」（2026-10-20） | 不收：以 Grok Bot 为主，Muse 仅据官方资料简述，不在跟踪清单 |
| 语音稿转述（Unite.AI、IT之家、BlockTempo、ezone、蕃新闻、techjuice 等，2026-11-05/06） | 不收：只复述官方 11-05 语音公告，无新信息 |
| secnews.co.uk 赏金转述（2026-11-04） | 不收：复述已收官方 11-02 赏金回顾，无新信息 |
| Infobae、Milenio、Expansión 等墨西哥上线西语转述（2026-11-05） | 不收：与已收 allthingsmuse 同事件，无新信息 |
| Muse Spark 1.1 发布博客（ai.meta.com，2026-11-05 前后） | 不收：模型发布，只说可在 Meta AI 应用中使用，没有说明与 Muse 产品的关系（已有判断，见对照旧笔记） |

## 对照旧笔记的判断（2026-11-06）

旧笔记 learning-ai-agent 的 Muse 部分引用而本笔记没有的来源，逐条判断如下（上表已判断的 Forkast、aiweekly、Tech Jacks、Gizmodo、TNW、IT之家转述、DigitalToday、Malwarebytes、dig.watch、Fox News、Subscription Insider、Reuters 人工客服、Muse Spark Open、Windows 博客、David Senra 访谈不重复）：

| 资料 | 判断 |
| --- | --- |
| Bloomberg「After JPMorgan, Charles Schwab blocks unauthorised AI agents…」（2026-10-16，经 Moneycontrol 转载） | 收入 media：嘉信理财 CEO 点名拦截 Muse；IT之家 10-19 的转述不收 |
| Muse Spark 1.1 发布博客（ai.meta.com） | 不收：模型发布，只说可在 Meta AI 应用中使用，没有说明与 Muse 产品的关系 |
| ai.meta.com/tools/muse | 不收：页面由脚本渲染，只有标题 |
| mathrubhumi「Muse AI agent faced security scare before launch」（10-08） | 不收：一手报道是已收的 404 Media |
| runtimewire「Muse has paid $1.2M in bug bounties」、David Singleton 的 X 帖（11-03） | 不收：官方赏金回顾已收 |
| OfficeChai 合作伙伴报道（Shopify、PayPal、Instacart、Expedia，09-23） | 不收：Connect 官方页已收 |
| Times of India、NewsBytes 的 Bill Gates 评价 | 不收：名人观点，无产品信息 |
| trade2spike「Muse Agent Says It Can Manage Your Money」（10-24） | 不收：转述 Yahoo Finance 10-22 的评测和身份盗窃资源中心的评论；Yahoo Finance 原文值得找，下一轮检索 |
| alphaforgeusa「An Agent's Memory Is a Database」 | 不收：评论 TIME 报道的观点文 |
| dev.to ifynx_studio 的 Secure VM 文章 | 不收：已删除（404） |
| 微信公众号文章 1 篇 | 按 source-types 的规则暂不处理 |
| IT之家其余 6 篇（亚马逊封禁、真人代拨电话、小企业版、Gadgets、Windows、Wonder） | 不收：均为转述，对应的一手资料已收 |

## 已知问题

### 帮助中心

- 正文由脚本渲染，直接下载的 HTML 里没有正文，也没有文章列表。
- 取正文：用网页抓取工具读取，要求逐字返回全文；抽查两三句关键句，与检索结果中的原文对照。
- 取日期：直接下载的 HTML 中有 JSON-LD，含 `dateCreated` 与 `dateModified`。`date` 用 `dateModified`，`dateNote` 记下 `dateCreated` 与页面显示的相对时间（如「Updated: 8 weeks ago」）。部分页面的 `dateCreated` 早于产品发布日期，照录即可。
- 找文章：帮助中心首页不能列出文章，用限定 `meta.com` 的检索逐个主题查找。同一篇文章有 `/help/superintelligence/`、`/help/artificial-intelligence/`、`/en-gb/help/...` 等多个地址，编号相同即为同一篇；`sourceUrl` 用 `/help/superintelligence/<编号>/`，其他地址不必列入 `altUrls`，按编号去重。
- 个别文章在 `/help/superintelligence/<编号>/` 下抓取只返回标题（如 Mac 一篇 1126304576638594），换成 `/help/artificial-intelligence/<编号>/` 即可；`sourceUrl` 仍写 superintelligence 路径，实际抓取的地址写入 `altUrls` 并在 `dateNote` 说明。
- 表格抓取后可能丢失单元格边界，按文字顺序还原为表格，并加译注说明。
- 已收（2026-11-04）：入门 1331373868832401、Artifacts 2074655449783957、指导与批准 1385290430137537、Mac 1126304576638594、提醒与计划任务 1484325780075655、数据管理 2225571704857152、个性与记忆 995796179982326、技能 2797651547267109、连接器 1687253048996149、浏览网页 2124746764949121、付款 1436362127544482、隐私与安全 1047255454427887、关于订阅 1021145227643680、订阅中心 1625680452306909、眼镜 Beta（ai-glasses）1391796469223757。
- 已知未收（订阅中心链接出的子文章，`/help/subscriptions/<编号>/`）：订阅 Muse 1627861775532967、管理订阅 28510110068583598、取消订阅 1348439670603568、被撤销的订阅 1754278722450348、购买额外令牌 28153473374286914、Meta 订阅计费 2534285893740819；帮助中心首页 1303670544995562。

### Meta Newsroom（about.fb.com）

- 页首的「要点」（Takeaways）框不在 `<article>` 容器内，只抽 `<article>` 会漏掉；要单独抽取，放在正文之前。
- 页面顺序为：标题、头部视频、要点框、正文。视频是 `<video>` 标签，`<source>` 中有 mp4 地址，按占位行保存。
- `date` 取页面标题下显示的日期。`article:published_time` 是 UTC 时间，可能比显示日期晚一天（例如新加坡上线稿显示 October 27，元数据为 10-28T00:00 UTC），两者不一致时在 `dateNote` 记下元数据。`article:modified_time` 对应 `updatedAt`。
- 正文中的幻灯片（`div.jetpack-slideshow`）把引语做成图片，文字在 `data-gallery` 属性的 JSON 里（每项的 `alt`）。逐张下载图片，在 `original.md` 中按替代文本写成引用块；替代文本为空的，看图转录，并在收录说明中写明。
- 图片下载时在地址后加 `?w=960` 取缩小版，原图通常每张数百 KB 到 1 MB。
- 链接中的跟踪参数（如 `srsltid=`）去掉，其余照录。
- 作者字段为站点编辑账号（如 heathera），不是署名作者，不填入 `author`。

### 同一篇文章的多个官方地址

| 文章 | 地址 |
| --- | --- |
| 我们如何设计 Muse | `introducing.muse.ai`、`muse.ai/blog/how-we-designed-muse` |
| 我们如何将安全构建进 Muse | `security.muse.ai`、`research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse`、`muse.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse` |

收录时 `sourceUrl` 取发布稿中链接的地址，其余写入 `altUrls`。

### introducing.muse.ai

- 图片地址形如 `/_next/image?url=...`。下载时用 `/_next/image?url=<编码后的路径>&w=1080&q=75`，并带请求头 `Accept: image/png,image/jpeg`，得到 1080 像素宽的 PNG 或 JPEG；原图可能有数 MB。保存时去掉文件名中的哈希后缀。muse.ai 的博客同样适用。
- 页首视频「Muse organizing everyday life」由脚本加载，取不到视频地址，用封面图加指向页面的占位行。

### research.meta.ai（研究博客）

- Next.js 页面。正文能直接抽取，但图表、基准表、演示视频由脚本渲染：静态 HTML 只有空的 `<figure>` 占位，图片路径和替代文本在内嵌的 RSC 数据里。用 `collect-sources/scripts/rsc_media.py` 取出，再用 `figures.py` 看占位的位置（每个占位前一段文字），按位置放回。
- 图片取浅色版：`/articles/<文章>/images/<名称>-light-v<n>.webp`；页首图在 `/articles/<文章>/hero/`。
- 标签页式演示（多个演示共用一个占位）写成一行占位加列表，列出每个标签和图注。
- 视频地址是带过期签名的 fbcdn 链接，占位行链接到文章页面。
- 文章页显示的日期和 `article:published_time` 一致。
- 2026-11-05：研究博客列表页（`research.meta.ai/blog/`）直接下载返回 403，浏览器因组织策略拦截；本轮改用检索核对，未发现 11 月 2 日之后的新文章。
- 2026-11-05 补跑：muse.ai/blog 列表页无新文章（最新仍为 11-02 赏金回顾）；Newsroom AI 标签页 11 月仅语音稿一篇。

### about.fb.com 抽取脚本

`scripts/extract_fb.py <html>` 依次输出标题、日期、要点框、正文，并把视频和幻灯片引语替换为 `[VIDEO ...]`、`[IMG 地址 | 替代文本]` 标记。

## 命名约定

- 帮助文档 slug 以 `help-` 开头，例如 `2026-09-08-help-guidance-and-approval`。
- 日文资料 slug 用英文意译。
