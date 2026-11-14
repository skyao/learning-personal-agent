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
| 最后收集日期 | 2026-11-14（10:16 轮次：muse 5 篇——媒体 2 篇：The Verge eBay 封堵 Muse（11-10，11-12 更新）；allthingsmuse HUMAN 十月报告 Muse 占 59%（11-14）；社区 3 篇：aihomebuilding 眼镜端 beta 解析（11-09）、museexplained 手表核查（11-12）、museexplained 电话代打台账（11-14，印度 2027 年初窗口仅片段级）；官方渠道本轮无新稿：Newsroom AI 标签最新仍为 11-06 Spaces 稿，muse.ai/blog 最新仍为 11-13 Poppy 稿（已收），Meta 消费者博客经页面文本核对无 Muse 新稿，研究博客直接下载恢复 200，11 月仅 11-09 Ember（模型发布，不收）与 11-06 特化模型两篇）；2026-11-13（22:16 轮次：muse 4 篇——媒体 2 篇：allthingsmuse Chrome 扩展悄悄上架（11-13，★）、allthingsmuse Poppy 1.0 实施细节（11-13）；社区 2 篇：museexplained 日本 11-12 连接器核查（11-13）、allthingsmuse Peter Yang 十个工作流（10-14，回填）；官方渠道本轮无新稿：Newsroom AI 标签最新仍为 11-06 Spaces 稿，muse.ai/blog 最新仍为 11-13 Poppy 稿（已收），Meta 消费者博客无 Muse 新稿，研究博客经 live browser 核对 11 月仅 11-09 Ember（模型发布，不收）与 11-06 特化模型两篇）；2026-11-13（10:16 轮次：muse 5 篇——官方 1 篇：muse.ai/blog Poppy 1.0 发布（11-13，★）；媒体 2 篇：allthingsmuse 电话代打 beta 首报（10-05，回填）、Moneywise Stamos 密码警告（11-06，回填，Wayback 快照）；社区 2 篇：museexplained iMessage 事件详解（10-01，回填）、aihomebuilding 电话代打披露缺口法律分析（11-08）；industry 3 篇：Sierra Poppy 1.0 发布（11-13）、Sierra 协议首次发布（10-06，回填）、Substack PAP 深挖（10-10，回填）；官方渠道：Newsroom AI 标签最新仍为 11-06 Spaces 稿，muse.ai/blog 新增 Poppy 稿，Meta 消费者博客无 Muse 新稿，研究博客经 live browser 核对 11 月仅 11-09 Ember（模型发布，不收）与 11-06 特化模型两篇）；2026-11-12（22:16 轮次：muse 7 篇——媒体 7 篇：TechCrunch 电话代打付费开放（11-12，★）、Engadget 同事件（11-12，补充通话身份披露与 Schlicht 的 Volvo 通话复现）、allthingsmuse 同事件（11-12，补充测试时间线）；回填 4 篇：allthingsmuse 旅游业关注（10-31，转述 Travel Weekly，万豪/希尔顿表态）、四市场 App Store 排名（10-28，Appfigures）、AMD EPYC 支撑 Muse 算力（10-28）、NVIDIA 30 亿美元投资与 Muse 合作（10-27）；industry 2 篇：TechCrunch 9-17 Instinct 与 Muse 同日新增电话代打（回填）、allthingsmuse Shop Pay 店外结账（10-31，回填）；官方渠道本轮无新稿：Newsroom AI 标签最新仍为 11-06 Spaces 稿，muse.ai/blog 最新仍为 11-02 赏金回顾，Meta 消费者博客无 Muse 新稿，研究博客经 live browser 核对 11 月仅 11-09 Ember（模型发布，不收）与 11-06 特化模型两篇）；2026-11-12（10:16 轮次：muse 1 篇——社区：Tuya Cloud Devices 开源 Skill（11-12，PR Newswire 新闻稿全文；Skill 已于 11-10 以 PR #61 合并进 Meta 的 muse-gadget-sdk 仓库）；官方渠道本轮无新稿：Newsroom AI 标签最新仍为 11-06 Spaces 稿，muse.ai/blog 最新仍为 11-02 赏金回顾，Meta 消费者博客无 Muse 新稿，研究博客经 live browser 核对 11 月仅 11-09 Ember（模型发布，不收）与 11-06 特化模型两篇）；2026-11-11（22:16 轮次：muse 7 篇——媒体 6 篇：Skift Expedia 接入上线实测（11-09，节选，Skift Pro 付费墙截断）、TechCrunch 手表双平台（11-10，补 Sensor Tower 40 天 1000 万下载数据）、allthingsmuse Muse Mail 付费开放（11-10）、Uber Courier 接入（11-10）、Muse Mail 将全量开放（11-11，Wang 表态）、WIRED 购物商家侧核查（10-31，回填，★，经 DNYUZ 全文转载）；社区 1 篇：museexplained 非用户消息隐私（11-04，回填）；industry 1 篇：Skift 温德姆向 AI 订房智能体开放库存（10-22，节选，Skift Pro 付费墙截断）；官方渠道本轮无新稿：Newsroom AI 标签最新仍为 11-06 Spaces 稿，muse.ai/blog 最新仍为 11-02 赏金回顾，研究博客 11 月仅 11-09 Ember（模型发布，不收）与 11-06 特化模型两篇）；2026-11-10（10:16 轮次：muse 3 篇——雷峰网 OpenClaw 拆解（11-04，社区，★）、海峡时报新加坡上线（10-28，媒体）、36氪/字母榜汪滔访谈（10-12，媒体）；industry 2 篇——中国新闻周刊个人智能体综述（11-08）、36氪/智东西封堵专文（10-21）；官方渠道本轮无新稿：Newsroom AI 标签最新仍为 11-06 Spaces 稿，muse.ai/blog 最新仍为 11-02 赏金回顾，研究博客 11 月仅 11-09 Ember（模型发布，不收）与 11-06 特化模型两篇）；2026-11-10（增量：Newsroom AI 标签与 muse.ai/blog 无新稿；媒体只做了一次检索，未见 11-09 22:16 轮次之后的新报道）；2026-11-09（22:16 轮次：媒体 7 篇——The Hindu 印度订阅价首报（11-09）、MacRumors Apple Watch 首报（11-09）与 allthingsmuse 手表双平台（11-09），回填 4 篇：HUMAN 智能体流量 40%（11-05）、GameQuant 连续 32 天榜首（11-05）、撤下的取消关注广告（11-05，据 BI）、Barron's 购物智能体信任落差（11-05，二手）；官方渠道本轮无新稿）；2026-11-09（10:16 轮次：媒体 6 篇——The Times 英国上线首报（11-09）、allthingsmuse Cloudflare 立场文件（11-09）与 Fingerprint 检测（11-06），回填 3 篇：Web Bot Auth 签名（10-31）、DataDome 29M 请求（10-15）、The RealReal 收紧防御（10-30）；社区 1 篇——dev.to 特化模型解读（11-09）；官方渠道本轮无新稿）；2026-11-08（22:16 轮次：媒体 3 篇——allthingsmuse Threads 内置助手在开发（11-08）、头像跳舞分享（11-08）、头像分享现身网页端回填（10-25）；官方渠道本轮无新稿）；2026-11-08（10:16 轮次补跑：媒体 9 篇——ChainCatcher Wang 访谈整理（11-03）、36氪 Muse 商业化分析（10-27）、The Verge 50 美元自制 Muse Charm（10-31）、allthingsmuse 6 篇：Muse Mail 推出（11-06）与设置指南（11-07）、Spaces 演示详解（11-06）、封堵综述（11-06）与加拿大银行（11-02）、CNBC 零售商审计（11-02）；官方渠道本轮无新稿）；2026-11-07（22:16 轮次补跑：官方 Spaces 稿、研究博客特化模型（Active Memory/Focus，PSI 47%），媒体 TechCrunch 与 The Verge 的 Spaces 报道、allthingsmuse Instacart 自绘购物车报道（11-04），industry 收 Enterpret 12 款智能体用户排名（11-03）；另收用户发来的公众号文章：社区 1 篇，橘AI；对照旧笔记补收媒体 1 篇：Bloomberg 嘉信理财拦截 Muse；22:16 轮次补跑：官方语音稿、墨西哥上线、TechCrunch、The Verge、DataCamp 横评、Medium Muse 101 与六产品横评（仅链接待补原文）、coderlegion、PYMNTS Expedia、语音悄悄上线回填；本轮补跑：Yahoo 理财评测、iFynx Secure VM 解析，industry 收 freistyle 六产品横评、老张入门成本对比、Kunal 收件箱实测（仅链接）；发布稿西语版 11-05 墨西哥更新记入 altUrls；Medium Muse 101 与六产品横评已改用转载全文）；2026-11-07（10:16 轮次补跑：社区 personalagentbench Muse 开源逐层核查、museexplained 11 月 4 日 11 小时停运记录，媒体 allthingsmuse 下载量 1.7:1 第三方对比；官方无新稿）；2026-11-07（22:16 轮次补跑：社区 BetterClaw 隐私分析、Top5Apps 语音开启指南；媒体 FourWeekMBA Nikkei 无广告二手报道（10-24，Nikkei 原文付费墙）；industry 收 Top5Apps 五款实测横评（11-01）；官方渠道本轮无新稿）；2026-11-05（第一阶段完成：官方、媒体、社区、实测；行业综合横评为「仅链接」占位）。下一轮起按新流程：原文存 `original.md`，资料页只写摘要与保留理由，不翻译 |
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
| Meta Newsroom「Design the Muse App, Just for You」（2026-11-06） | 已收（2026-11-06）：官方，Spaces 上线；同时提到向 Muse 推送以 Wonder 训练的特化模型 |
| research.meta.ai「Bringing Specialized Models to Muse and Meta AI」（2026-11-06） | 已收（2026-11-06）：官方，特化模型推送；Active Memory/Focus 定义与三组对照数据（PSI 47% 对 38%、Active Memory 评估 90% 对 76%、日常任务完成率 +67%）；两张图表以 HTML 数据表形式呈现，已还原为简表 |
| TechCrunch「Meta introduces Spaces, a new way to collaborate with your Muse agent」（Lucas Ropek，2026-11-06） | 已收（2026-11-06）：媒体，Spaces 报道；含 Zuckerberg 的 X 帖与 1000 万用户（财报电话会）出处 |
| The Verge「Meta’s Muse AI can create custom ‘spaces’ for the version of the app you need right now」（Emma Roth，2026-11-06） | 已收（2026-11-06）：媒体，Spaces 报道；原站禁止直接下载，改由浏览器读取全文，关键句已用转载对照；文中无 Zuckerberg 引言；原站地址 theverge.com/tech/1028871/ |
| allthingsmuse「Muse Is Getting Shopping Carts It Renders Itself, Starting With Instacart, Report Says」（Icarus，2026-11-04） | 已收（2026-11-06）：媒体，据 Kaziukėnas 的 X 帖与连接器文档截图，Instacart 首批自绘购物车；明确标注未经 Meta 证实、无上线日期 |
| Enterpret「The 12 Personal AI Agents Users Actually Prefer in 2026, Ranked by 277,038 Posts」（2026-11-03） | 已收 industry 社区（2026-11-06）：27.7 万帖子的用户偏好排名，Muse 第一；Hermes Agent、Hark、Wabi、Fo 为新出现的产品名，列入候选产品等 Sky 决定 |
| Unite.AI Spaces 稿与 47% 稿、siliconreport、emergent.sh、technobezz、aiweekly、Digital Trends、iphoneincanada.ca、techsavvyed、theoutpost.ai 等（2026-11-06） | 不收：复述官方 11-06 两篇公告，无新信息 |
| 语音稿转述新增（etvbharat、News18、搜狐、2026-11-06） | 不收：只复述官方 11-05 语音公告（已收），无新信息；与表中已有语音稿转述行同判 |
| hrlens.io 两篇（mock interview、Spaces 求职，2026-11-06） | 不收：SEO 内容农场风格，无实测 |
| dev.to「Muse's 2nd feature in 2 days builds your apps for you」（frankchu，2026-11-06） | 不收：观点评论，无实测、无新事实 |
| explainx.ai Spaces 文与 Wonder 价格页（2026-11-06） | 不收：个人博客观点/价格整理，无实测；其中「67% 无方法」一点已由多家媒体指出，不另收 |
| zappiqai、squad.so、ansezz、analyticsmadesimple（Muse 解说/对比，10–11 月） | 不收：复述官方文档的解说/对比站，无实测与新信息 |
| monolithdesign.agency 三产品对比（2026-11-03） | 不收：复述厂商公告的商业对比，无实测；与已判不收的 ontheground 同类 |
| TechCrunch「After blocking Muse, Amazon now lets users text Alexa to help them shop」（2026-11-06） | 不收：Alexa 购物新闻，Muse 仅在标题背景中提及 |
| aiagentswatch、agentstacklist（价格/功能聚合页） | 不收：聚合页，无新报道 |
| aidedex 日本/海外指南、powerads 新加坡稿、halmob 商业指南（10–11 月） | 不收：复述官方文档的指南，无新信息 |
| Muse Spark 1.3 研究博客（2026-09-02） | 不收：模型发布，未说明与 Muse 产品的关系（与 Spark 1.1 同判） |
| 特化模型推送博客（research.meta.ai，2026-11-06） | 收：明确说明向 Muse 与 Meta AI 推送以 Wonder 训练的特化模型，含 Active Memory/Focus 在 Muse 中的表现与分数；注意：推送的是特化版而非 Wonder 本身，Wonder 本身仍按 10-12 公告先供订阅档。待 Sky 决定的「Wonder 模型切换事实」（aiagentslibrary 条目）仍悬而未决，不与此混同 |
| personalagentbench「Is Meta Muse open source? What is open, and what is not」（2026-11-05） | 已收（2026-11-07）：社区，独立分析；逐层核查 agent／应用／云端 VM、Spark／Spark Open、Wonder、Glimmer、Gadgets 的开源状态，含自家 teardown 实测（246 个方法的权限表）与 Hugging Face 假冒 muse-wonder 账号核查；简体中文版记入 altUrls。文中「自 9 月 17 日有 Mac 应用」一说未附发布公告或版本号，照录 |
| allthingsmuse「Muse Out-Downloaded ChatGPT 1.7 to 1 on the US App Store Last Week, Estimates Show」（Icarus，2026-11-04） | 已收（2026-11-07）：媒体，Wang 转发 Pablo Marti 图表，截至 10-29 当周 Muse 美国 App Store 预估下载 942K，ChatGPT 556K，约 1.7:1；数据为 FoxData 第三方预估（经 ASO World 印证），非 Meta 官方口径，文中已注明，不触发 ★（★ 要求官方披露的用户规模数据）。下载量对比图表已本地化 |
| museexplained.com「Is Muse Down? The Nov 4 Outage: 11 Hours, No Official Meta Post」（Marvin Jones，2026-11-06） | 已收（2026-11-07）：社区，服务异常记录；据 Instatus 追踪数据，11-04 14:00 UTC 至 11-05 01:00 UTC 停运 11 小时，峰值 304 报告/小时（101 倍于常态），生成故障加延迟，Meta 未发任何公告；另记 11-03 23:00 UTC 起 3 小时停运；以 IsItDownRightNow 交叉核对；全文明确标注数字为追踪器数据而非 Meta 数据，停运影响范围（多少账户）追踪器无法给出 |
| etvbharat / pondero.ai / kompozy.io / xenospectrum / asumetech 的 Spaces 与 Voice 稿（2026-11-06/07） | 不收：只复述官方 11-05/11-06 公告，无新信息 |
| shiftdelete.net 特化模型稿、joho-todai.com 特化模型日文稿（2026-11-06/07） | 不收：复述官方 11-06 研究博客，无新信息。（joho-todai 文中提到 10-26 MoneyForward ME 与 Muse 連携，该消息在窗口外（10-26），且为日本本地连接器公告，未另行追查） |
| aicoder.com Realtime Avatar 中文稿（2026-11-05） | 不收：复述研究博客与 @AIatMeta，无新信息；Realtime Avatar 研究博客本身已收（2026-09-23） |
| everyinfra.com「Muse Wonder API 做达人尽调」（2026-11-05） | 不收：Wonder 模型 API 的实测与定价核查，主题是模型 API 用法，与 Muse 个人智能体产品无直接关联，按模型资料收录原则不收 |
| agentsthatwork.ai「Cloud agent computers compared」（last verified 2026-11-07） | 不收：多产品云端 agent 电脑对照，为无固定发布日期的常更页面；Muse 一节只复述官方资料，且可用地区漏写日本（10-23）与墨西哥（11-05） |
| winzheng.com Spaces 稿（2026-11-07） | 不收：TechCrunch Spaces 报道的全文转载，原文已收 |
| newsbytesapp.com 特化模型稿（2026-11-07） | 不收：复述官方 11-06 研究博客，无新信息 |
| aiagentstore.ai / theanswerengine.news 每日 AI 新闻汇总（2026-11-07） | 不收：汇总页，无一手内容 |
| TIKR「Lisa Su: Meta's Muse Drew "Over 10 Million People" in 45 Days. Can Meta Charge Them?」（2026-11-07） | 不收：核心数据（1000 万用户、25% 日活、周活用户购物占比与客单价）出自已决定不收的 Q3 财报电话会；Lisa Su 在 Yahoo Finance 采访中的「45 天超 1000 万激活」为第三方转述，无超出电话会口径的新产品事实；余下为 Meta 股票估值分析。线索：文中称 Wang 对 Nikkei 表示 Muse 内无广告计划，下轮可找 Nikkei 一手报道核对（已核对：Nikkei 原文付费墙，改收 FourWeekMBA 二手报道，见本表） |
| BetterClaw「Is Meta Muse Safe? What the AI Agent Sees and Stores」（2026-11-06） | 已收（2026-11-07）：社区，隐私分析；对照 Meta 官方页面逐项核查权限、数据去向与训练默认设置，逐条检验 Paul Walsh 批评的成立程度，附 8 项收紧设置；发布方为竞品托管智能体厂商，文末有自家产品推广；5 张信息图已本地化 |
| Top5Apps「How to Turn On Muse Voice Mode」（2026-11-06） | 已收（2026-11-07）：社区，语音模式分步开启指南；iPhone 需 14.3 版，区分新旧语音图标与五种易混淆的语音功能，列出未能核实之处；两处 YouTube 嵌入改为视频占位行 |
| FourWeekMBA「Meta Takes Muse to Japan and Says It Will Stay Ad-Free」（2026-10-24，更新 10-27） | 已收（2026-11-07）：媒体，二手报道，basedOn Nikkei Asia 2026-10-23；Nikkei 原文付费墙，作者只读到英日两版开头，企业服务与购买佣金来自 Badawi 的 X 帖总结；原站对 curl 返回 JS 验证页 403，改用 WordPress REST API 取文；发表日期在窗口外，按上轮 TIKR 线索核对收录 |
| Top5Apps「Best Personal AI Agents: 5 Worth Trying [Reviewed Nov 2026]」（更新 2026-11-01） | 已收 industry 社区（2026-11-07）：同账号、同任务实测五款并打分，Muse 4.6 第一，另有 dots 等暂列；文中称 Muse 仅美加与免费额度每周 1 亿 tokens，已过时，照录；配图为 logo 与官网截图，未收；更新日在窗口外，属本轮检索发现的 11 月评测回填 |
| tofuads.com「Is Muse for Small Business worth connecting to my Meta ad account?」（约 2026-11-01/02） | 不收：更新日在窗口外（11-04 起）；内容为小企业广告账户分析，Meta 未说明 Muse 能否改广告账户，含 ads MCP server 信息 |
| hokai.io「Muse Review (2026)」（更新 2026-11-01） | 不收：常更页面，更新日在窗口外；内容主要为已收官方资料的整理，无一手实测 |
| BetterClaw「OpenAI Dots vs Meta Muse vs Grok Bot」（信息截至 2026-10-05） | 不收：内容已滞后，Muse 可用地区仍写仅美加，与 10-23 日本、10-27 新加坡、11-05 墨西哥上线不符；常更页面；同类三产品对照已有 freistyle 与老张两篇 |
| obpai.com「Best Personal Agents 2026」（2026-11-04） | 不收：编辑主观排名，无实测、无新信息 |
| magnets.tg「AI assistant ranking 2026」（2026-11-05） | 不收：评测对象为通用助手（ChatGPT、Gemini、Claude、Perplexity、DeepSeek、WAM Agents），不含跟踪产品；自家产品排第一 |
| bloks.dev「The best AI agent apps」（2026-11-06 前后） | 不收：以本地自托管应用为主，自家产品排第一；Muse 仅在 FAQ 提及 |
| life-topics.jp、finance.biggo.jp、neworder.co.jp、gihyo.jp 的 Spaces 与语音稿（2026-11-06/07） | 不收：只复述官方 11-05/11-06 两篇公告，无新信息 |
| derringtoncollaborativeai.com「Muse gets a voice, custom spaces, and a better memory」（2026-11-07） | 不收：三篇官方公告的简讯汇总，无新信息 |
| asumetech.com Spaces 稿（2026-11-07） | 不收：复述官方 11-06 Spaces 公告，无新信息 |
| smzdm.com「小扎『西瓜』模型口碑翻车实测」（2026-10-13）、虎嗅「花了几百亿美金……栽在一盏灯上」（2026-10-14） | 不收：Muse Wonder 模型资料，与 Muse 产品无直接关联；且在窗口外 |
| airosetta.com WIRED 六款横测中文转述（2026-10-29） | 不收：已收 WIRED 原文的转述，且在窗口外 |
| ChainCatcher「Meta 首席 AI 官：Muse 是怎麼做出來的？」（2026-11-03） | 收：媒体类，David Senra 访谈 Alexandr Wang 的繁体中文书面整理；访谈本身因无文字稿不收，本文含大量直接引语与新事实（2026 年 2 月一两周做出原型、七个月打磨、100 多项评估清单与发布门槛、模型与产品合计不到 200 人）；发表日期在窗口外一日，本轮检索新发现 |
| 36氪「Meta之后，大厂期待“Muse时刻”」（商业新研社商靖，2026-10-27） | 收：媒体类，Muse 商业化独立分析（AI ROI/交易抽佣模式）与国内大厂对照；核心数据引自财报电话会但文章本身为原创分析；原文为微信公众号「商业新研社」文章，36氪经授权转载，微信原文记入 altUrls；发表日期在窗口外，本轮检索新发现 |
| The Verge「I built an AI Tamagotchi before Meta could」（Sean Hollister，2026-10-31） | 收：媒体类，50 美元 Waveshare 开发板 + Claude Code 自制 Muse Charm 平替的一手实测；发表日期在窗口外，本轮经 allthingsmuse 周记线索发现；文中嵌入视频未在静态页面中找到地址，未收录 |
| allthingsmuse「Muse Mail, the Dedicated Email Address for Your Muse, Is Reaching More Users」（Icarus，2026-11-06） | 收：媒体类，Muse Mail 开始向更多用户推出的首报，用户截图为证；此前 TestingCatalog 9 月 18 日已发现未发布的 Mail 标签 |
| allthingsmuse「How to Set Up Your Muse Email」（Professor Muse，2026-11-07） | 收：媒体类，Muse Mail 设置指南；据 Aaron Makelky 的 X 帖截图核对流程，@muse.ai 地址格式引自 RuntimeWire 的应用静态检查，未经 Meta 证实 |
| allthingsmuse「Muse Spaces in Depth: What Meta's Demos Actually Show」（Icarus，2026-11-06） | 收：媒体类，逐段解析 Meta 的 Spaces 演示视频内容（家庭仪表盘、Jolly Mall、周末模式、花园笔记本）；演示视频以占位行保存，家庭仪表盘截图已本地化 |
| allthingsmuse「Your AI Agent Hits a Wall: Who Is Blocking Agents, and What Still Works」（Icarus，2026-11-06） | 收：媒体类，银行与零售商封堵智能体的综述；含 Billions Network 51 家零售商审计（37 家属误伤、零家提供可验证的智能体结账通道）、加拿大五大银行序列、Cequence 与 DataDome 的发现 |
| allthingsmuse「Canada's Biggest Banks Block AI Agents Like Muse From Customer Accounts」（Icarus，2026-11-02） | 收：媒体类，加拿大五大银行封堵的单篇首报；RBC 备忘录细节（Kazmi 与 Nielsen 署名、「不可接受的客户风险」、发言人证实）与各家表态；发表日期在窗口外，本轮经 blocking guide 内链发现 |
| allthingsmuse「Most Big Retailers Block AI Agents Without Meaning to, Audit Finds」（Icarus，2026-11-02） | 收：媒体类，CNBC 11 月 1 日报道的转述（basedOn 填 CNBC）；Billions Network 审计的完整数字与方法限定、JPMorgan 向 Plaid 收费、Warner 与 Sanders 的立法呼吁；发表日期在窗口外，本轮经 blocking guide 内链发现 |
| allthingsmuse「What Are Muse Spaces?」（Icarus，2026-11-06） | 不收：与已收的 Spaces 详解同主题、内容基本重合（官方公告与演示复述），FAQ 无新增信息 |
| allthingsmuse「What to Actually Do With Your Muse Email Once It's Live」（Professor Muse，2026-11-07） | 不收：与已收的设置指南同主题的用法建议，示例为虚构场景（Sam 装修厨房），无实测记录 |
| allthingsmuse「Muse for People Ops」（Professor Muse，2026-11-08）、「Muse for Creators and Podcasters」（2026-11-07） | 不收：提示词模板式用法课（Academy 系列），无真实执行记录，占位提示词与假设场景为主 |
| allthingsmuse「Building a Media Brand with Muse: Issue #6」（Icarus，2026-11-06） | 不收：站点自身运营周记，与 Muse 产品本身关系弱；提到的新闻均已收或另有来源 |
| 掘金「我让 AI 智能体替我干活的 30 个高频用法」（2026-10-27） | 不收：以推广邀请码为目的的用法清单，无可核查的实测过程与结果；所列功能多为官方已知功能的改写，部分说法（如 Muse Home Link 智能家居）无法核实 |
| Zacks 财报稿、etvbharat / pondero.ai / kompozy.io / asumetech 的 Spaces 与语音稿、mundoia.com.ar 特化模型稿、secnews.co.uk 赏金稿、datastudios.org Spaces 稿、storyboard18 Spaces 稿、toolscout-e2i.pages.dev 三公告汇总、trueseeker.com 语音核查页、global1.news 墨西哥上线稿（2026-11-06/07/08） | 不收：均为已收官方公告的复述或同一事件的二手报道，无新信息；global1.news 为 AI 辅助撰写的墨西哥新闻日报转述 |
| sumus.im「OpenAI Dots vs Meta Muse vs Grok Bot」（2026-11-04） | 不收：厂商自家产品对比页，内容据官方资料整理，无实测；Sumus 本身为团队向产品，列入候选产品等 Sky 决定 |
| metaflow.life「Dots vs Muse vs Grok Bot for Marketing」、openaimaster.com「Muse AI vs ChatGPT」（2026-11-07） | 不收：营销场景对比与案头整理，无实测，内容据官方资料；openaimaster 作者自承非实测、无 Muse 账号 |
| shipwithmuse.live「Meta Muse Email Triage」（约 9 月 27 日） | 不收：Connect 时期的连接器指南，邮件分诊内容已被帮助文档覆盖；Muse Mail 部分写于上线前 |
| deadsimple.email、agentmail.to、emailbump.com 的第三方 agent 邮箱指南（9 月） | 不收：第三方服务的自家产品指南，写于原生 Muse Mail 上线前；原生上线现由 allthingsmuse 覆盖 |
| allthingsmuse「Expedia Says Its Muse Integration Is Set to Go Live in the US」（2026-11-05） | 不收：与已收 PYMNTS 11-04 稿同一事件的转述；电话会实录称集成在电话会期间上线 |
| 研究博客新帖「Accelerating Scientific Research in Health Data Science with Muse Models」（10-28）、「Addressing Third-Party Testing Misconfiguration: Muse Spark 1.1」、「Introducing Muse Voice Transcribe」 | 不收：模型资料，与 Muse 产品无直接关联，按模型资料收录原则不收 |
| aiagentslibrary「Meta Muse Charm: Availability and Release」（2026-10-31） | 不收：Charm 未发售的状态整理页，无一手内容；其中「Meta 未公布价格与发售日」一点已由多方证实 |
| 新浪财经 9 月 11 日扎克伯格专访转述 | 不收：窗口外，Heath 专访原文已收 |
| dev.to「Meta's Muse Charm is a shell — the AI companion moat is the loop」（2026-11-01） | 不收：对 Hollister 一文的观点评论，无新事实 |
| hamidun.com、mylistingo.com、newsy-today.com、printingpressai.com、apexnews.com 等 Hollister 一文的转述（2026-10-31/11-01） | 不收：The Verge 原文已收的转述 |
| allthingsmuse「Threads Is Working on an In-App Muse Assistant, Researcher Reports」（Icarus，2026-11-08） | 收：媒体类，Jane Manchun Wong 在 X 上发布 Threads 内置 Muse 助手的开发线索（附界面截图），RuntimeWire 同日亦有报道；功能未发布、Meta 未宣布，文中已注明；已收资料中尚无 Threads 条目 |
| allthingsmuse「Muse Avatars Can Now Dance, and You Can Share the Clip to Instagram and WhatsApp」（Icarus，2026-11-08） | 收：媒体类，Alexandr Wang 在 X 上宣布头像跳舞与分享功能已上线；含完整操作流程、五段演示舞蹈曲目与分享渠道；头像分享选项 10 月下旬现身网页端的前情见同轮回填的 10-25 一篇 |
| allthingsmuse「Muse Avatar Sharing Surfaces in Web App, but It Is Not Live Yet」（Icarus，2026-10-25） | 收：媒体类，TestingCatalog 首报网页端未发布的头像 Share 选项（动态预览、可复制链接、四种预览状态）；发表日期在窗口外，本轮经 11-08 跳舞一文内链发现，属首报回填；该功能现已随跳舞流程上线 |
| RuntimeWire「Threads Muse assistant」同日报道（2026-11-08） | 不收：与已收 allthingsmuse 同事件、同为 Wong 的 X 帖的报道，不另收 |
| ppc.land 语音稿（2026-11-08 前后） | 不收：只复述官方 11-05 语音公告，无新信息 |
| blog.toolsnetwork.ai 语音稿（2026-11-05） | 不收：AI 生成的新闻简报，复述官方 11-05 语音公告，无新信息 |
| nieuws.llmnet.nl 特化模型稿（Ivo Donker，2026-11-08） | 不收：复述官方 11-06 研究博客，无新信息；文末注明由 Claude 撰写、据来源核对 |
| freshsynapse.com 特化模型稿（2026-11-07） | 不收：复述官方 11-06 研究博客，无实测 |
| agenticcommons.xyz 特化模型繁体稿（2026-11-08） | 不收：复述官方 11-06 研究博客的繁体中文解说，无新信息 |
| ventureatlas.org「Meta adds Spaces and specialized models to Muse」（2026-11-06） | 不收：自承为 AI 辅助汇编的二手汇总，非原创报道 |
| sofarbot.com 语音稿（2026-11-08） | 不收：AI 新闻站复述官方 11-05 语音公告，无新信息 |
| yayafa.com Unite.AI 特化模型日文稿（2026-11-07） | 不收：Unite.AI 复述稿的日文转述 |
| TechSifted「Meta Muse Review 2026」（2026-11-03） | 不收：案头整理式评测，打分与优缺点均据官方资料与财报电话会，无实测、无新事实；Wonder 消费者档情况已由官方 11-06 博客覆盖 |
| AIToolsReview「Meta Muse Agent Review: Secure VM, Sentinel, Pricing」（首发 2026-09-11，更新 10-13） | 不收：窗口外；案头整理、无实测；部分说法已过时（称仅限美国、无国际上线日期）或无法核实（称免费档需绑卡激活、Spark 1.3 顶级推理模式被扣留） |
| The Times「Meta preparing to launch Muse AI assistant in UK」（2026-11-09） | 已收（2026-11-09）：媒体，英国数周内上线首报，零售商合作、高管赴英、1100 万用户、免费+订阅与交易抽佣、CMA 与 ICO 表态；★（新地区上线、欧洲首站）。Retail Gazette 同日报道未另收；The Times 原站对直接下载返回机器人验证页、Wayback 无快照，正文经页面文本抓取取得并与检索索引摘录核对 |
| allthingsmuse「Cloudflare Proposes New Identity Rules for AI Agents, Naming Muse as the Leading Example」（Icarus，2026-11-09） | 已收（2026-11-09）：媒体，Cloudflare 11-05 立场文件，Muse 为主要例证；含 Web Bot Auth、MOLE、Trusted Agent Delegation 提议与 HUMAN 72%、DataDome 33%、Fingerprint、Web Bot Auth 签名等新信息 |
| dev.to「Meta Brings Muse Wonder's Memory and Focus to Everyone」（tng_thnhnhn，2026-11-09） | 已收（2026-11-09）：社区，对 11-06 特化模型推送的独立解读与批评（区分 Wonder 本身与特化版本，指出四项数字无基线、无方法、无模型身份） |
| allthingsmuse「Fingerprint Says It Can Now Spot Muse Traffic That Doesn't Identify Itself」（Icarus，2026-11-06） | 已收（2026-11-09）：媒体，Fingerprint 11-05 公告，可识别未表明身份的 Muse 流量，曾在某大银行登录流程中发现 Muse 活动；与 Web Bot Auth 签名测试一文互为限定 |
| allthingsmuse「Meta Is Quietly Signing Some Muse Web Requests, DataDome Finds」（Icarus，2026-10-31） | 已收回填（2026-11-09）：媒体，DataDome 发现 Meta 自 10-12 前后用 Web Bot Auth 签署部分 Muse 请求；发表日在窗口外，本轮经 Cloudflare 一文内链发现 |
| allthingsmuse「Muse Generated 29 Million Requests in 12 Days, DataDome Finds」（Icarus，2026-10-15） | 已收回填（2026-11-09）：媒体，DataDome Q3 报告，29.1M 请求、33%、99.3% 云来源、8.9% 敏感流程与日增长 4.4 倍；发表日在窗口外，本轮经 Web Bot Auth 一文内链发现 |
| allthingsmuse「The RealReal Tightens Bot Defenses After Muse Holds Its Listings Out of Reach」（Icarus，2026-10-30） | 已收回填（2026-11-09）：媒体，The Verge 实测 Muse 循环占用 20 分钟购物车保留，The RealReal 收紧防御（发现开放、交易收紧的折中处理）；发表日在窗口外，本轮经 Web Bot Auth 一文内链发现 |
| allthingsmuse「Muse for Event Planners」（2026-11-09） | 不收：Academy 提示词模板式用法课，无真实执行记录（与 People Ops、Creators 同判） |
| Pivot News 英国上线稿（Carlos Mendez，2026-11-09） | 不收：Retail Gazette 的二手转述，无新信息 |
| evermx.com「Meta Expands Muse Agent With Video Chat, Glasses, Charm」（更新 2026-11-09） | 不收：9 月 23 日 Connect 内容的回顾，无新信息 |
| crosswalk.to「Meta Muse: what it is, and how to connect it to other agents」（更新 2026-11-04） | 不收：agent 目录页，无一手内容；其中「Wonder 即将进入 Muse」与 11-06 特化模型博客不符 |
| postfa.st 社媒经理指南（2026-11-02 前后） | 不收：案头整理，未实测，部分说法已过时（称仅美加） |
| surff.io、breakorbit.ai、aidedex.com、aiwiz.uk、mausbot.com 英国可用性指南（9–10 月） | 不收：案头整理，均写于英国上线消息之前，现已过时 |
| IT之家/搜狐语音稿（2026-11-06）、IT之家特化模型稿（2026-11-07）、gihyo.jp、life-topics.jp、1ccf.com（2026-11-07） | 不收：只复述官方 11-05/11-06 两篇公告，无新信息 |
| etvbharat、pondero.ai、trueseeker.com 语音/Spaces 稿（2026-11-06/07） | 不收：复述官方 11-05/11-06 公告，无新信息（与表中已有同类行同判） |
| The Hindu「Meta sets India pricing for Muse AI agent ahead of launch」（Aroon Deep，2026-11-09） | 收：媒体类，印度订阅价首报（Power ₹1,799、Maximum ₹8,999），Meta 未回应询价；印度用户现处等候名单、经 VPN 注册与代付受限等当地准入细节；★（新地区定价，价格为 The Hindu 的发现、未经 Meta 证实） |
| MacRumors「Meta's Muse AI Agent Comes to Apple Watch」（Juli Clover，2026-11-09） | 收：媒体类，iOS 15.0 上线 Apple Watch 首报（发消息、听写、通话、表盘复杂功能）；★（新平台） |
| allthingsmuse「Muse Comes to Apple Watch and Wear OS」（Icarus，2026-11-09） | 收：媒体类，补 Wear OS 同步上线（Wang 的 X 帖）、15.0 版发布说明原文与订票截图；★（与 MacRumors 同一事件的新平台事实） |
| allthingsmuse「Muse Drove 40% of the Agentic Traffic One Security Firm Saw in September」（Icarus，2026-11-05） | 收回填：媒体类，Advertising Week 小组讨论，HUMAN 称 9 月 Muse 占其观测智能体流量的 40%，另有 209% 环比增长、62% 流向零售与旅游、结账更快与 DoorDash 咖啡实例 |
| allthingsmuse「Muse Held the No. 1 Spot on the US App Store for 32 Straight Days」（Icarus，2026-11-05） | 收回填：媒体类，GameQuant 日排名数据（9-18 至 10-19 连冠 32 天、评分与下载量估计）；GameQuant 的 Medium 原文直接下载失败、Wayback 无快照，basedOn 填 GameQuant |
| allthingsmuse「Meta Pulled a Muse Ad Promising to Show Who Unfollowed You on Instagram」（Icarus，2026-11-05） | 收回填：媒体类，据 Business Insider 2026-10-29 报道，Meta 撤下承诺可查 Instagram 取消关注者的广告，发言人证实已下架；BI 原文付费墙未读，basedOn 填 BI，原文地址未核实 |
| allthingsmuse「AI Shopping Agents Are Growing Fast. Most Shoppers Still Aren't Sold.」（Icarus，2026-11-05） | 收回填：媒体类，据 Barron's 报道，UBS 信任调查（17% 认为好主意、43% 认为不是）、Bain 5000 亿美元预测与推荐不透明等机制；Barron's 原文返回 401、Wayback 无快照，basedOn 填 Barron's |
| Muse Ember 研究博客（research.meta.ai，2026-11-09） | 不收：模型发布，全文未提及 Muse 产品（仅 Muse Code 与 Meta Model API 上线，`muse-ember-1.0`）；与 Spark 1.1/1.3 同判 |
| TechCrunch、Unite.AI、SiliconANGLE、AlphaSignal、CellCog、Interesting Engineering、cryptobriefing 的 Ember 稿（2026-11-09/10） | 不收：模型发布的媒体转述；Ember 本身不收 |
| allthingsmuse「Meta Releases Muse Ember」「Muse Ember, Wonder, and Spark 1.3 Arrive on Google Cloud」（2026-11-09） | 不收：模型发布与模型上云，均无 Muse 产品关联 |
| allthingsmuse「Muse to Launch in the UK Within Weeks」（2026-11-09）、bmmagazine、Pivot News 英国上线稿（2026-11-09） | 不收：已收 The Times 英国首报的转述，无新信息 |
| AppleInsider、world-today-journal.com、thedailytechfeed.com 的 Apple Watch 稿（2026-11-09/10） | 不收：与已收 MacRumors、allthingsmuse 同事件的转述（AppleInsider 兼带不建议安装的评论） |
| tryagentsonic.com「Meta Muse on Apple Watch or Galaxy Watch」（2026-09-27） | 不收：写于手表上线前，称无手表应用，已过时 |
| ppc.land Cloudflare 综述、unite.ai 语音稿、olly.social、CoAI、etvbharat、Sohu IT之家语音稿、blog.toolsnetwork.ai、pondero.ai（2026-11-05/08） | 不收：只复述官方 11-05/11-06 公告，无新信息 |
| IT之家/网易号、rollout.sagus.io 的 Muse Ember 中文与日文稿（2026-11-09/10） | 不收：模型发布的转述；Ember 本身不收 |
| drchaos.com「Meta Muse Wonder Review」（2026-11-05 前后） | 不收：Wonder 模型评测，与 Muse 产品无直接关联 |
| museexplained.com「Muse Voice is live」指南、agentcomparison.net 权限与安全整理（2026-11-06/07） | 不收：官方语音公告与帮助文档的整理，无实测、无新信息 |
| aitoolsreview.co.uk Spark 1.2 与 Glimmer 评测（2026-11 月） | 不收：模型与 Muse Code 内容，不在收录范围 |
| allthingsmuse Academy 系列新增：个人理财、招聘、求职（10 月底至 11 月初） | 不收：提示词模板式用法课，无真实执行记录（与 People Ops、Creators、Event Planners 同判） |
| allthingsmuse「Muse vs Meta AI」（2026-10-21） | 不收：产品对照解说，部分说法已过时（称仅美加），且在窗口外 |
| allthingsmuse「Agentic Commerce, Explained: How Muse Checks Out With Shop Pay」（2026-10-21） | 不收：购物结账解说，作者自购实例只有一段，其余为已收官方资料的整理；发表日在窗口外 |
| 微博 Sensor Tower 下载/留存帖（2026-10-21） | 不收：社交媒体单帖转述；下载量已有 FoxData 报道覆盖，留存数据无一手出处；且在窗口外 |
| OpenReplay「Meta Muse 初探」（2026-11-07，中英文两版） | 不收：复述官方文档的解说，核心内容已被已收官方安全文章与 iFynx Secure VM 分析覆盖，无实测与新信息；与已判不收的 analyticsmadesimple、squad.so 同类 |
| mautoblog「Meta Muse: the agent that books, pays and writes for you. Just not in Europe」（2026-11-07） | 不收：观点评论，作者自承未找到官方原因、GDPR 与 AI 法案只是推断；无实测、无新事实 |
| Zapier「Meta Muse AI agent: What It Is and How to Use It」（2026-09-30） | 不收：连接器厂商的入门指南，复述官方资料，无实测；与 analyticsmadesimple 同判 |
| shipwithmuse.live「What Is the Meta Muse Secure VM? Sentinel, Egress, Risks」（2026-09-24） | 不收：官方安全文章的整理加个别用户传闻，内容与已收官方安全文章及 iFynx 分析基本重合 |
| metamuseai.site「How Muse Works: Secure VM, Sentinel and Approvals」 | 不收：不知名站点、无署名，内容为官方资料整理，仅有的“实测”为一次按 Deny 的简单测试 |
| tech.news18a.com「Muse与Dot实测，洋Agent逛中国互联网」（2026-10-19，更新 11-10） | 不收：无署名、未具名测试者，无法核实测试过程与原始来源；图片走网易 CDN，疑为转载拼贴 |
| jxxy.net「Meta Muse 带娃 Agent 深度实测」（2026-10-29） | 不收：How I AI Claire Vo 一期节目的二手转述，该节目已收 industry 条目 |
| ai-indeed.com「Muse是什么软件？三个同名产品辨析与功能指南」（2026-10-22） | 不收：入门辨析，部分说法已过时（称仅美加） |
| StockWe 花旗研报转述「Meta最新推出的Muse Wonder系列AI应用产品」（2026-10-13） | 不收：Wonder 模型与股票分析，模型资料按收录原则不收 |
| aiec.fun「Meta最新AI代理Muse拆解，及它对使用Openclaw的启发」（约 2026-09-24） | 不收：个人博客长文，时间线有硬伤（如称 Muse Spark 发布于 2026-04-08），内容与已收 iFynx 分析重合 |
| allthingsmuse「Muse India Pricing Surfaces」（2026-11-10） | 不收：已收 The Hindu 印度定价首报的转述，无新信息 |
| allthingsmuse「Muse for Nonprofits and Fundraising」（2026-11-10）、「What to Build with Muse Spaces: 12 Ideas」（2026-11-07） | 不收：Academy 提示词模板式用法课与点子清单，无真实执行记录（与 People Ops、Creators、Event Planners 同判） |
| etvbharat 两篇（2026-11-10 AI 汇总、2026-11-07 Spaces 稿）、zeniteq 与 madrobot 的 Ember 稿（2026-11-09/10）、pondero.ai 语音稿、aiagentswatch 价格聚合页 | 不收：复述官方公告或模型发布转述，无新信息；Ember 按模型资料收录原则不收 |
| Skift 两篇（Expedia 接入 11-09、温德姆开放库存 10-22） | 收为「节选」：Skift Pro 付费墙截断，Wayback 无快照；缺失处已在原文标出 |
| WIRED「Muse 本可颠覆各行各业，但目前还没有」（2026-10-31） | 收为「转载全文」：WIRED 原文付费墙不可读，改用 DNYUZ 全文转载；Technologist Mag 转载缺 5 段，未采用；★（商家侧核查对照财报口径） |
| allthingsmuse「Coached by Muse: An 80-Point Goodbye」（2026-11-10） | 不收：幻想足球日记，无可核查的 Muse 执行记录（提示词/输出未展示） |
| allthingsmuse「Muse for Travel Pros」（2026-11-11） | 不收：Academy 提示词模板课，虚构客户（Alvarez 一家），无真实执行记录 |
| allthingsmuse 日本合作伙伴篇（2026-10-24） | 不收：合作为计划未上线，状态已由官方 10-23 日本上线页覆盖 |
| Medium「Is ShopBack available in Muse?」（Ronald，2026-11-10） | 不收：单用户未核实说法，称 ShopBack 连接器已在新加坡上线 |
| Mac Messages 同步事件（Inc. 专栏 Jason Aten，2026-09；187,462 行数据；Meta 否认；苹果 10-02 收紧 Full Disk Access） | 已收 museexplained 详解（2026-11-13）：Inc. 专栏原文仍未直接读到，TechCrunch 争议报道未另收；详解含 Singleton 纠正、静态拆解与后续同类投诉 |
| Mercari 连接器（museexplained 10-31） | 不收：2026-11-12 是 Mercari 财报日，不是连接器上线日；Meta 与 Mercari 未给连接器日期 |
| Ember 模型报道（madrobot、zeniteq、orcarouter Google Cloud 篇、dev.to 两篇、museexplained Ember 评分篇，11-09/10） | 不收：模型发布，无 Muse 产品关联，按模型资料收录原则不收 |
| Apple Watch 转述稿（aiweekly、pondero、nakoda、androidpure、aiaffairs、AppleInsider、world-today-journal、thedailytechfeed、ai-club.cn、搜狐/IT之家） | 不收：与已收 MacRumors、allthingsmuse、TechCrunch 同一事件，无新信息 |
| Zacks Q3 财报稿 | 不收：2026-11-04 已决定不收（用户决定） |
| explainx.ai Spaces「67% 宣称核查」 | 不收：2026-11-06 已判断不收 |
| ai.advalorem.io Muse 中小企业 playbook（2026-11-04） | 不收：播客配套文，无超出官方的新事实 |
| Tuya「Tuya Cloud Devices」开源 Skill（PR Newswire，2026-11-12） | 收：社区类，新闻稿全文；首个大型智能家居平台为 Muse 发布的 Gadgets Skill，API 密钥 + Thing Model 云端接入与安全边界；本轮核查 GitHub：PR #61 已于 11-10 合并进 Meta 的 muse-gadget-sdk 仓库 |
| allthingsmuse「Tuya Releases an Open-Source Skill That Lets Muse Control Smart Home Devices」（2026-11-12） | 不收：已收 PR Newswire 原文的转述；其引述 Unite.AI 的“PR #61 仍在审核”一说已过时（本轮核查：11-10 已合并） |
| Unite.AI「Tuya Connects Meta's Muse to Smart Home Devices Through Cloud APIs」（2026-11-12） | 不收：与已收 PR 新闻稿同一事件的转述；“PR #61 仍在审核”与 GitHub 记录不符 |
| allthingsmuse「Expedia Connector Is Live on Muse」（2026-11-10） | 不收：与已收 Skift 11-09 节选同一事件的转述 |
| allthingsmuse「Muse for Writers and Editors」（2026-11-12） | 不收：Academy 提示词模板式用法课，无真实执行记录 |
| museexplained「Muse Voice is live」指南（2026-11-06/07） | 不收：与已收官方 11-05 语音稿及 TechCrunch/The Verge 报道同一内容的操作整理，无一手实测任务；其“未说明事项”核对（无定价、无档位、无时长上限）记入本条；该站称 11-13 复查语音的眼镜端与非美上线 |
| museexplained「Muse Spaces Is Live」指南（2026-11-07） | 不收：与已收官方 11-06 Spaces 稿同一内容的整理，无一手实测；该站称 11-13 复查分享、数量上限与删除/数据问题 |
| museexplained「Expedia Is Live in Muse」（2026-11-09） | 不收：与已收 Skift 同一事件的二手整理；该站称 11-17 复查官方确认、第二家实测与机票上线 |
| 手表上线转述稿（igeeksblog、dataist.ai、techbriefly、business-standard、shorty-news、aiaffairs、nakoda、skimwire、pondero、relvehq、mymondayai，2026-11-10/11/12） | 不收：与已收 MacRumors、allthingsmuse、TechCrunch 同一事件，无新信息 |
| Medium「Your Personal AI Agents Want the Job」（Thomas E Doherty，2026-11-11） | 不收：多产品案头对照，无实测；Muse 可用地区写成仅美加，已过时 |
| Medium「Get 1 Billion Free Tokens on Meta Muse AI」（Noah Bourland，2026-11-10） | 不收：邀请码推广 |
| Medium「Meta Muse for Small Business」（2026-11-10） | 不收：官方资料整理，无实测 |
| rftuv.ai「Meta Muse Ember: AI Agents at a Third the Cost」（2026-11-10） | 不收：模型发布的转述；Ember 本身不收 |
| dev.to「What an LLM call actually costs in November 2026」（synap402，2026-11-11） | 不收：模型 API 价格，与 Muse 产品无直接关联 |
| IT之家语音稿（2026-11-06）、okyn、haiai123、himiao.ai 特化模型稿、pmer.cn 实战指南 | 不收：复述官方 11-05/11-06 两篇公告或官方资料整理，无新信息 |
| 老张「Muse Wonder Pricing and Subscription」（2026-11-06） | 不收：模型定价整理；其中“Power 档用户反映已切 Wonder”一说与待 Sky 决定的模型切换事实相关，不另行记录 |
| Muse Charm 现状指南（museexplained、aiagentslibrary、thedripwire、idevice、builtwithmuse 等） | 不收：均称 Meta 仍无价格与确切发售日，12 月目标未变，无新信息 |
| 英国/印度可用性指南（museaicodes、aidedex、proxycove、mausbot、aiagentslibrary，11 月） | 不收：案头整理，部分已过时（漏墨西哥上线）；英印均无新上线消息 |
| 字节跳动个人智能体（Bloomberg 2026-11-11：数周内推出，据称内部代号 Spell） | 候选产品：未命名、未确认是否出海、字节跳动未回应置评；等 Sky 决定是否纳入跟踪 |
| Mercari 2026-11-12 财报（FY2027.6 Q1，日本时间 15:30 发布） | 本轮检索未见财报提及 Muse 连接器上线，连接器仍无日期；museexplained 10-31 追踪页本身不另收 |
| TechCrunch「Muse can now place calls to US businesses — if you pay」（Sarah Perez，2026-11-12） | 收：媒体类，电话代打向美国付费用户开放首报；★（重大功能上线：主动任务能力升级）；订阅档位与 token 额度（$20/500M、$100/3B）为本轮唯一出处；另记 Muse Mail 将向免费档开放 |
| Engadget「Meta's Muse can now make calls on your behalf (if you have a paid subscription)」（Karissa Bell，2026-11-12） | 收：媒体类，同事件；补充 Muse 致电时说明是代人打来并正在录音、但不总明说自己是 AI，及 Schlicht 的 Volvo 经销商通话复现（等 15 分钟） |
| allthingsmuse「Muse Outbound Calling Is Now Available to Paid Subscribers in the US」（Icarus，2026-11-12） | 收：媒体类，同事件；补充测试时间线（8 月内测、9 月 16 日 beta 扩大至主动申请通知的用户、现已结束测试） |
| allthingsmuse「Travel Industry Watches Muse Closely as Marriott Sees Site Traffic and Hilton Eyes Direct Bookings」（Icarus，2026-10-31） | 收：媒体类，回填；转述 Travel Weekly 10-31 报道，basedOn 填 Travel Weekly（原文地址未在页面链接中找到）；万豪称 Muse 已出现在其平台（Drew Pinto，10-15 Truist 电话会）、希尔顿 CEO 在 Q3 电话会（10-27）看好智能体直销、Phocuswright 37%/38% 数据 |
| allthingsmuse「Muse Now Ranks Above ChatGPT on the iPhone Free Chart in All Four of Its Markets」（Icarus，2026-10-28） | 收：媒体类，回填；Appfigures 四市场榜单（日本/加拿大/新加坡第 1、美国第 3）；date 取页面显示 10 月 28 日，元数据为 2026-10-29T04:15:00Z |
| allthingsmuse「AMD's EPYC Chips Power Muse as AMD Deepens Its Meta Partnership and Invests $1 Billion」（Icarus，2026-10-28） | 收：媒体类，回填；EPYC 为 Muse 专属计算环境提供动力、首批 Helios 机架系统已在 Meta 安装测试、10 亿美元投资、代号 Verano 的下一代处理器 |
| allthingsmuse「NVIDIA Invests $3 Billion in Meta as the Two Companies Deepen Their Muse Partnership」（Icarus，2026-10-27） | 收：媒体类，回填；Muse 运行在 NVIDIA 基础设施上、Prometheus 超级集群（俄亥俄州新奥尔巴尼）用 NVIDIA GPU 训练 Muse 模型、扩大 Vera Rubin 部署、OpenShell/Sentry 仅在考虑中未承诺、30 亿美元投资 |
| TechCrunch「Rival AI agents, Instinct and Meta's Muse, both add the ability to make calls」（Ivan Mehta，2026-09-17） | 收 industry 媒体类，回填；电话代打测试阶段首报（Instinct Concierge 与 Muse 同日上线，Muse 先向主动要求打电话的用户开放）；经 11-12 TechCrunch 上线报道内链发现 |
| allthingsmuse「Shop Pay Now Checks Out Inside Muse, Including at Stores Outside Shopify」（Icarus，2026-10-31） | 收 industry 媒体类，回填；Shopify Fall '26 版把 Shop Pay 结账扩展到非 Shopify 商店，卡组织 token 支付（Visa/Mastercard/Discover，Amex 即将推出），首批四智能体为 Muse、Claude Duet、Grok Bot、Instinct，另有 Shop.md 技能；date 取页面显示 10 月 31 日，元数据为 2026-11-01T00:19:00Z |
| allthingsmuse「Shopify Partners With Meta's Muse to Enable Shop Pay Checkout on All Stores」（Icarus，2026-09-29） | 不收：9 月 21 日 Lütke 宣布的合作，核心事实已被 Connect 官方页覆盖；新增内容仅为股价反应（+7.3%）等市场花絮 |
| allthingsmuse「Conductor Will Keep Developing Inside Meta, Reversing Its Wind-Down」（2026-11-12） | 不收：编码智能体方向，属 Muse Code（与 11-04 收购稿同判） |
| startupfortune、finance.biggo.com、emergent.sh、gagadget、mezha.net、ua.news、dailyaibrief、standardtopic、techweekly.co.za、thetechstreetnow、news.bpdata、scoopfeeds 的电话代打稿（2026-11-12/13） | 不收：与已收 TechCrunch、Engadget 同事件的转述，无新信息；其中 startupfortune 对“是否可能转接真人客服”一点的存疑，11-12 两篇首报均未提及，仍悬而未决 |
| Business Standard 手表稿（2026-11-12）、aidailypost 印度定价稿（2026-11-10，更新 11-12） | 不收：与已收 MacRumors、allthingsmuse、The Hindu 同事件的转述，无新信息 |
| tech-insider.org「Meta Muse AI Agent: Free, $20 Power and $100 Maximum Tiers」（2026-09-09） | 不收：官方帮助页与公开资料的汇编指南，无一手实测与新信息 |
| BlockTempo 手表繁体稿（2026-11-10）、zglg.work、搜狐、凤凰网语音稿（2026-11-06） | 不收：与已收手表上线报道、官方 11-05 语音公告同一内容，无新信息 |
| allthingsmuse「Muse's Phone Call Beta Has the AI Agent Dialing US Businesses for You」（2026-10-05） | 已收（2026-11-13）：电话代打 beta 阶段的本站首报，9 月 16 日扩大测试、8 月内部测试、真人代打撤回 |
| makeuseof、powerads.group、gadgets360、dexerto、coinstats、techmymoney、cryptobriefing、the-decoder.com、techbriefly 的电话代打上线稿（2026-11-12/13） | 不收：与已收 TechCrunch、Engadget、allthingsmuse 同事件的转述，无新信息 |
| Unite.AI「Sierra Releases Poppy 1.0 With Shopify and Meta Muse Support」（2026-11-13） | 不收：Sierra 1.0 公告的转述；其中「规范与工具包标注为 draft 1.0」一点未另收 |
| devopsness.com「Personal Agent Protocol Explained」（约 2026-10-31） | 不收：草案阶段的解说，已过时；内容已被 Substack 深挖文覆盖 |
| crosswalk.to「Does Muse support Personal Agent Protocol (Poppy)?」（更新 2026-11-04） | 不收：agent 目录页，称「截至 10-18 无个人智能体上线协议」，已被 11-13 上线事实推翻 |
| allthingsmuse「Muse for Students」（2026-11-13） | 不收：Academy 提示词模板式用法课，无真实执行记录（与 People Ops、Creators 同判） |
| guijiagi.com「Meta Muse 上手表后的免费体验路径」（2026-11-12） | 不收：手表上线指南，称 11 月 11 日登陆（实际为 11 月 9/10 日），说法不准、无实测 |
| himiao.ai「Muse 有了自己的邮箱：@muse.ai 向美加付费用户开放」（2026-11-12） | 不收：已收 Muse Mail 报道的转述，无新信息 |
| ai-club.cn 手表稿（2026-11-11）与特化模型稿（2026-11-07） | 不收：TechCrunch 手表报道的编译与官方 11-06 研究博客的转述，无新信息 |
| ai-bio.cn、dian8dian.com 的 Muse Ember 稿（2026-11-10/11） | 不收：模型发布，Ember 本身不收 |
| aissignalhub.me 转 钛媒体「Personal AI 开战：Meta Muse 与蚂蚁灵光 2.0」（2026-11-12） | 不收：Muse 部分事实过时（称仅美加，漏日本/新加坡/墨西哥上线）；其中灵光 2.0 首周数据（2000 万用户）为灵光产品线索，不属本轮 |
| mausbot、museaicodes、aiagentslibrary、aidedex、heyhermes 的英国/印度可用性指南（11 月） | 不收：案头整理，均称英印无上线消息、无新信息，部分已过时（漏墨西哥上线） |
| OpenReplay「A First Look at Meta Muse」英文版 | 不收：与已判不收的中文版「Meta Muse 初探」同一篇，复述官方文档，无实测 |
| orcarouter.ai「Muse Agent Explained」（约 2026-09-29） | 不收：官方资料解说，无实测；窗口外 |
| cheers.tech「What Can Meta Muse Do for Home Service Businesses?」（2026-11-01） | 不收：面向家政商家的汇编指南，据官方与媒体资料整理，无一手实测 |
| bland.ai「Can Muse Make Phone Calls? Now It Can With Its Own Number」（2026-10 左右） | 不收：据 nullbot 新闻室转述的汇编，称功能仍限 beta，已过时（11-12 已转正式功能） |
| agentstacklist 电话代打页（2026-11-12） | 不收：聚合页，无一手内容 |
| winzheng.com「Meta disputes claim that Muse read a user's private messages」（2026-10-01，更新 11-14） | 不收：Inc. 事件的二手转述，无新信息；事件本身由 museexplained 详解覆盖 |
| vibegraveyard.ai 两篇（Mac Messages 同步、人类代打测试，2026-10-26） | 不收：事件摘要站，对 Inc. 事件与 404 Media 人类代打报道的二次整理；一手报道已收或由 museexplained 覆盖 |
| tech-insider.org「Meta Denies Muse AI Read 187K Messages」（2026-10-02） | 不收：Inc. 事件的二手整理，无新信息 |
| manifold.security Mac Messages 事件页（更新 2026-10-19） | 不收：事件台账式整理，称 Inc. 专栏未能打开；事件本身由 museexplained 详解覆盖 |
| tipranks Stamos 稿（2026-11-06） | 不收：与已收 Moneywise 同事件的转述，无新信息 |
| allthingsmuse「Building with Muse: 10 real Muse workflows from Peter Yang」（2026-10-14） | 已收（2026-11-13）：社区类，10 个真实工作流的文字 walkthrough 回填；Xfinity 电话实测有逐字引语，AT&T 与 Xfinity 两段有具体金额；视频以占位行保存 |

| allthingsmuse「Muse Is Now in Chrome: Meta Quietly Publishes a Browser Extension」（Icarus，2026-11-13） | 收：媒体类，Chrome 扩展悄悄上架的完整跟进报道，首报为 TestingCatalog；★（进入新平台：Chrome 侧边栏扩展，用用户自己的 Chrome 浏览） |
| allthingsmuse「Personal Agent Protocol Reaches Version 1.0, Live for All Muse Users and Every Shopify Store」（Icarus，2026-11-13） | 收：媒体类，Poppy 1.0 实施细节与首批落地（Mercury、Synchrony、土耳其航空），新增 60 家设计伙伴、总数超 100 家；官方 Sierra 稿与 muse.ai 博客稿已收 |
| museexplained「Japan's November 12 Check: Mercari and Ticket Pia in Muse Are Still Not Live, While Money Forward ME Is」（Marvin Jones，2026-11-13） | 收：社区类，按日期闭环的阴性核查；Mercari 11-12 财报材料未提 Muse，Money Forward ME 为唯一一手确认已上线的日本连接器，附只读限制与三项用途 |
| makeuseof、Digital Trends、gadgets360、powerads、aichatdaily、itmatterss、patrika71、Medium（christy.cs07）的电话代打上线稿（2026-11-13） | 不收：与已收 TechCrunch、Engadget、allthingsmuse 同事件的转述，无新信息；其中 gadgets360 称「限 Pixel 机主」一说与事实不符 |
| chenqiyuan.cn、nxrte.com、news.jp、pithwire、chosun、iphonemod、twaslnews 的电话代打稿（2026-11-13） | 不收：与已收 TechCrunch、Engadget 同事件的转述或编译，无新信息；chenqiyuan.cn 为 AI 情报聚合站 |
| zeniteq、aragonresearch 的 Ember 稿（2026-11-09/11） | 不收：模型发布，Ember 本身不收 |
| macobserver 手表稿（2026-11-10） | 不收：与已收 MacRumors、allthingsmuse、TechCrunch 同事件的转述，无新信息 |
| ai.advalorem.io「The 500 Million Muse」中小企业 playbook（2026-11-04） | 不收：播客配套文，无超出官方的新事实（与 11-12 轮次已判同类行同判） |
| odivend、pondero 语音稿（2026-11-06） | 不收：只复述官方 11-05 语音公告，无新信息 |
| undeniableprogress、icreat.ai、bitcomme 的 Poppy 1.0 稿（2026-11-13） | 不收：Sierra 发布稿的转述，其中 undeniableprogress 自标 AI 起草，无新信息 |
| descope「What Is Personal Agent Protocol」与「Joins Poppy as Design Partner」（2026-11-13） | 不收：厂商自家解说与设计伙伴公告；其中「支付、推送、附件仍为开放议题」一点记入本条 |
| monolithdesign、automationace、heybento、guidetoartificialintelligence、tryiro 的多产品横评（2026-11-03/05/09/10） | 不收：案头整理式横评，无一手实测；monolithdesign 已于 11-13 轮次判过；heybento 自承未做横向实测 |
| allthingsmuse「Muse for Students」（2026-11-13）、「Building a Media Brand with Muse: Issue #7」（2026-11-13） | 不收：Academy 提示词模板课与站点自身运营周记（与 People Ops、Creators 同判） |
| 英国上线转述稿 bmmagazine、thebusinesseconomic（2026-11-09） | 不收：已收 The Times 英国首报的转述，无新信息；本轮未见英国正式上线消息 |
| geekygoo「Meta's Muse can now make phone calls for you」（Amit Jalan，2026-11-14） | 不收：无实测的案头整理指南（作者明言未用过该功能），只复述 11-12 三篇首报，无新信息；与 Gemini Call for Me 的对照不含 Muse 新事实 |
| FourWeekMBA「Meta's Muse Now Calls Businesses for You, From $20 a Month」（2026-11-13） | 不收：与已收 TechCrunch、Engadget、allthingsmuse 同一事件的转述；新增仅自算的 token/美元比值，价格据帮助中心核对无误 |
| IT之家/凤凰网/新浪财经电话代打稿（2026-11-14） | 不收：TechCrunch 11-12 报道的转述，无新信息 |
| note.com 日文 Muse 指南（富永淳一，2026-11-14） | 不收：作者自承内容由 Muse 调查撰写、未全部核对，含事实错误（称仅 4 地、漏墨西哥上线） |
| museexplained「Meta's promise ledger, re-scored」（2026-11-03） | 不收：11 月 2 日状态汇总，关键结论（Wonder 未进应用等）已被 11-06 特化模型博客覆盖，已过时 |
| lapaasvoice「Meta Muse Spark 1.4 Leak」（2026-11-14） | 不收：模型泄露（RocksDB PR 15674 出现 muse-spark-1.4-internal），无 Muse 产品关联，按模型资料收录原则不收 |
| allthingsmuse「Muse for Home Life Admin」（2026-11-14） | 不收：Academy 提示词模板式用法课，无真实执行记录（与 People Ops、Creators 同判） |
| odivend 语音稿（2026-11-06 前后） | 不收：只复述官方 11-05 语音公告，无新信息 |
| powerads.group、ma-no.org、dealinnow.com 电话代打稿（2026-11-13） | 不收：与已收 TechCrunch、Engadget、allthingsmuse 同一事件的转述，无新信息 |
| zeniteq、mlq.ai、lapaasvoice、oossa、techbuzz、emergent、lenexa、wortins、europesays 等 eBay 转述稿（2026-11-10/11） | 不收：与已收 The Verge 原文同一事件的转述，无新信息；其中 aiseen.cloud 的 robots.txt 核对（meta-externalagent 被禁、搜索爬虫放行）未另收 |
| kju.ai 英国上线稿（2026-11-09） | 不收：11-09 报道的 AI 摘要转述；本轮未见英国正式上线消息 |
| dotsbot.co、winzheng.com 手表稿（2026-11-10/11） | 不收：与已收 MacRumors、allthingsmuse、TechCrunch 同一事件的转述或编译，无新信息 |
| blog.vinjo.co.in Gadgets SDK 稿（2026-10-17，11-14 转载） | 不收：窗口外；Gadgets SDK 已有官方文档与 Tuya 覆盖，无新信息 |
| etvbharat AI 汇总（2026-11-10） | 不收：汇总页，无一手内容；其中 ChatGPT Wallet 为 dots 线索，不属本轮 |
| The Verge eBay 封堵 Muse 报道（Mia Sato，2026-11-10，11-12 更新） | 已收（2026-11-14）：媒体类，一手报道 + 实测复现；原站禁止直接下载，改由浏览器保存页面 PDF 后转文本，标题发表时为「eBay appears to have shut the door on third-party AI agents」，11-12 更新后改为现标题 |
| allthingsmuse「Muse Accounted for 59% of Agentic Traffic One Security Firm Saw in October」（Icarus，2026-11-14） | 收：媒体类，HUMAN 十月报告首报（59%，9 月 40%）；首图与文内 Jolly 插画为装饰图，未收 |
| aihomebuilding「Muse Moved Onto Your Face」（Jake Kowalski，2026-11-09） | 收：社区类，眼镜端 beta 独立深度解析；作者未实测、10 月 13 日录音事件为单一样本未证实，摘要中已限定 |
| museexplained「Muse Is on Your Wrist」（Marvin Jones，2026-11-12） | 收：社区类，手表端核查台账；二手细节已标注未确认，11 月 19 日复查 |
| museexplained「Muse Can Now Call Businesses for You If You Pay」（Marvin Jones，2026-11-14） | 收：社区类，电话代打台账；印度 2027 年初窗口仅片段级，11 月 20 日复查 |


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
- 2026-11-06：研究博客列表页直接下载恢复（200），新帖 `/blog/specialized-models-for-muse-and-metaai`；文中图表以 HTML 数据表形式呈现，可直接抽取还原。
- 2026-11-08：研究博客列表页直接下载又返回 403，浏览器读取确认 11 月仅 11-06 特化模型一篇，无新帖。
- 2026-11-09：同上，直接下载 403，浏览器读取确认 11 月仅 11-06 特化模型一篇，无新帖。
- 2026-11-09（22:16 轮次）：列表页直接下载与 browser.open 均返回 403；经检索核对，11 月 9 日新帖仅 Muse Ember 一篇（模型发布，不收，见判断记录）。
- 2026-11-11（22:16 轮次）：同上，直接下载 403，browser.open 返回 403 后改用 live browser 读取，确认 11 月仅 11-09 Ember（模型发布，不收）与 11-06 特化模型两篇，无新帖。
- 2026-11-12（22:16 轮次）：同上，直接下载与 browser.open 均返回 403，改用 live browser 读取，确认 11 月仅 11-09 Ember（模型发布，不收）与 11-06 特化模型两篇，无新帖。
- 2026-11-12（10:16 轮次）：同上，直接下载与 browser.open 均返回 403，改用 live browser 读取，确认 11 月仅 11-09 Ember（模型发布，不收）与 11-06 特化模型两篇，无新帖。
- 2026-11-05 补跑：muse.ai/blog 列表页无新文章（最新仍为 11-02 赏金回顾）；Newsroom AI 标签页 11 月仅语音稿一篇。

### about.fb.com 抽取脚本

`scripts/extract_fb.py <html>` 依次输出标题、日期、要点框、正文，并把视频和幻灯片引语替换为 `[VIDEO ...]`、`[IMG 地址 | 替代文本]` 标记。

## 命名约定

- 帮助文档 slug 以 `help-` 开头，例如 `2026-09-08-help-guidance-and-approval`。
- 日文资料 slug 用英文意译。
