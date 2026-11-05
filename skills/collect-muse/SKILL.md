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
| 最后收集日期 | 2026-11-05（第一阶段完成：官方、媒体、社区、实测；行业综合横评为「仅链接」占位） |

## 收录范围

「Muse」既是 Meta 个人 AI 智能体产品的名字，也是 Meta 模型家族的名字。只收与 Muse 个人智能体产品相关的资料：

| 资料 | 是否收录 |
| --- | --- |
| Muse 产品的发布、更新、地区上线、帮助文档、安全设计、条款 | 收录 |
| Muse for Small Business、Muse 眼镜端、Muse for Windows / Mac、Gadgets 与设备接入 | 收录 |
| 模型资料 | 按 collect-sources 的「模型资料的收录原则」逐篇判断：明确说明为 Muse 优化、用于驱动 Muse，或说明 Muse 运行时如何选择模型的才收 |
| Muse Code（终端编程智能体）、Muse Image / Muse Video（生成模型）、Meta Enterprise Platform | 不收 |
| 法律文档：Muse 服务条款、Muse 隐私政策、连接器平台条款、Gadget SDK 条款、眼镜自定义唤醒名隐私声明 | 不收（用户 2026-11-04 决定，见 collect-sources 的「不收的资料类型」） |
| 边缘资料：订阅中心的 6 篇子文章、Wonder 模型卡 PDF、Gadget SDK 子目录 README | 不收（用户 2026-11-04 决定） |

模型家族中各篇的判断结果记在下面，避免下一轮重复判断：

| 模型资料 | 判断 |
| --- | --- |
| Muse Wonder 新闻稿（about.fb.com，2026-10-12） | 收：说明将驱动 Muse，并为个人智能体处理私人信息做了训练 |
| Muse Wonder 研究博客（research.meta.ai，2026-10-12） | 收：同上，另说明将用于 artifact 生成 |
| Muse Wonder 模型卡 PDF | 待定：评估以模型为主，含 MemoryBench、FocusBench；待用户确认 |
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
| Meta Newsroom 日文版 | `about.fb.com/ja/news/` | 日本上线等日本专属公告 | 直接下载；日文资料同样全文翻译 |
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
| 多产品横评（WIRED、纽约时报、Axios、Claire Vo、Pat Simmons、AI Agents Library、CNBC 2026-09-30） | 已放入行业综合，暂为「仅链接」，待统一补全文 |
| David Senra 播客对 Alexandr Wang 的访谈 | 不收：无文字稿（音视频规则，用户 2026-11-05 决定） |
| Zuckerberg 在 Sources 播客的访谈（sources.news） | 已收：按节目页文字收录，不含完整访谈 |
| 纽约时报 The Daily 播客「Call My A.I. Agent」（Eli Tan） | 不收：无文字稿 |
| The Verge 关于 Muse 文件系统与夜间回顾的报道 | 已收；同时收了一手来源 mouse.dev（Peter James）和后续「分享功能恢复」 |
| Hunter Brook「Dox for me, O Muse」 | 已收 |
| Marketplace 住址事件 | 已收卫报报道（Business Insider 首发但有付费墙）；Malwarebytes 转述、EPIC 评论不收；Surfshark 数据收集分析页日期异常，不收 |
| 人物档案事件 | WIRED 2026-10-03 原文已收；Medianama 二手报道保留（用户 2026-11-05 决定；其转述的是 TIME，内容不完全重合）；TIME 原文仍无法读取 |
| Future Society「Muse, in its own files」（futuresociety.ch/muse-findings） | 已收：页面自标「由 AI 生成」，但每条发现附 VM 文件引文；发现列表取自 report_data.json |
| Wardle 在 Objective by the Sea v9 的演讲 | 已建「仅链接」占位页，会后补全 |
| Tom's Guide、Engadget、DataCamp 等 Muse 与 Dots 对比文 | 行业综合候选，待统一处理 |
| The Information 人形机器人 Max 报道（2026-10-31，付费墙）与 Engadget 转述（2026-11-01） | Engadget 版不收：抓取到的正文未提及 Muse；一手报道付费墙未读，改收下行 NDTV 版 |
| NDTV「Zuckerberg Wants To Give AI A Body」（2026-11-02） | 收：媒体类，全文翻译，basedOn 填 The Information；Max 定位为 Muse 的潜在实体形态，Max 2 自 9 月开发中，Meta 称仅内部研究、无销售计划 |

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
- 正文中的幻灯片（`div.jetpack-slideshow`）把引语做成图片，文字在 `data-gallery` 属性的 JSON 里（每项的 `alt`）。逐张下载图片，引语按替代文本翻译成引用块；替代文本为空的，看图转录，并加译注说明。
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

### about.fb.com 抽取脚本

`scripts/extract_fb.py <html>` 依次输出标题、日期、要点框、正文，并把视频和幻灯片引语替换为 `[VIDEO ...]`、`[IMG 地址 | 替代文本]` 标记。

## 命名约定

- 帮助文档 slug 以 `help-` 开头，例如 `2026-09-08-help-guidance-and-approval`。
- 日文资料 slug 用英文意译。
