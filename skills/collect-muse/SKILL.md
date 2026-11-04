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
| 最后收集日期 | —（首轮收集进行中） |

## 收录范围

「Muse」既是 Meta 个人 AI 智能体产品的名字，也是 Meta 模型家族的名字。只收与 Muse 个人智能体产品相关的资料：

| 资料 | 是否收录 |
| --- | --- |
| Muse 产品的发布、更新、地区上线、帮助文档、安全设计、条款 | 收录 |
| Muse for Small Business、Muse 眼镜端、Muse for Windows / Mac、Gadgets 与设备接入 | 收录 |
| 模型资料 | 按 collect-sources 的「模型资料的收录原则」逐篇判断：明确说明为 Muse 优化、用于驱动 Muse，或说明 Muse 运行时如何选择模型的才收 |
| Muse Code（终端编程智能体）、Muse Image / Muse Video（生成模型）、Meta Enterprise Platform | 不收 |

模型家族中各篇的判断结果记在下面，避免下一轮重复判断：

| 模型资料 | 判断 |
| --- | --- |
| （逐篇补充） | |

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| Meta Newsroom | `about.fb.com/news/`（AI 标签：`about.fb.com/news/tag/ai/`） | 发布、地区上线、Connect、小企业 | 直接下载 |
| Meta Newsroom 日文版 | `about.fb.com/ja/news/` | 日本上线等日本专属公告 | 直接下载；日文资料同样全文翻译 |
| Muse 博客 | `muse.ai/blog` | 设计、安全、赏金回顾 | 直接下载；列表页可取全部文章链接 |
| 设计文章 | `introducing.muse.ai` | 我们如何设计 Muse | 直接下载 |
| 安全文章 | `security.muse.ai` | 我们如何将安全构建进 Muse | 直接下载 |
| Meta 研究博客 | `research.meta.ai/blog/` | 模型发布、实时 Avatar 等技术文章 | 直接下载；先按「收录范围」判断 |
| 模型卡 | `research.meta.ai/static/` | 模型卡 PDF | 下载 PDF 后抽取文本 |
| Meta 帮助中心 | `www.meta.com/help/superintelligence/<编号>/` | Muse 帮助文档，约 14 篇以上 | 正文由脚本渲染，见「已知问题」 |
| 订阅帮助 | `www.meta.com/help/subscriptions/<编号>/` | Muse 订阅 | 同帮助中心 |
| 眼镜帮助 | `www.meta.com/help/ai-glasses/<编号>/` | 眼镜端 Muse Beta | 同帮助中心 |
| 产品页 | `ai.meta.com/muse/` | 产品功能介绍 | 直接下载 |
| 连接器开发指南 | `platform.muse.ai/docs` | 自定义连接器规范 | 直接下载 |
| Gadgets | `gadgets.muse.ai`、`github.com/facebookincubator/muse-gadget-sdk` | 设备接入 | 直接下载；仓库收 README 与文档，不收代码 |
| 漏洞赏金 | `bugbounty.meta.com/payout-guidelines/muse/` | Muse 赏金规则 | 直接下载 |
| 条款 | `agent.meta.ai/terms` | Muse 服务条款 | 直接下载 |

## 媒体与社区检索

- 英文检索词：`Meta Muse agent`、`Muse personal AI agent`、`Muse Secure VM`、`Muse Sentinel`
- 中文检索词：`Meta Muse 智能体`、`Muse 个人智能体`、`Meta Muse 实测`
- 检索时排除与产品无关的同名结果：Muse 乐队、muse.ai 早期的视频托管服务、其他名为 Muse 的应用。

## 已知问题

### 帮助中心

- 正文由脚本渲染，直接下载的 HTML 里没有正文，也没有文章列表。
- 取正文：用网页抓取工具读取，要求逐字返回全文；抽查两三句关键句，与检索结果中的原文对照。
- 取日期：直接下载的 HTML 中有 JSON-LD，含 `dateCreated` 与 `dateModified`。`date` 用 `dateModified`，`dateNote` 记下 `dateCreated` 与页面显示的相对时间（如「Updated: 8 weeks ago」）。部分页面的 `dateCreated` 早于产品发布日期，照录即可。
- 找文章：帮助中心首页不能列出文章，用限定 `meta.com` 的检索逐个主题查找。同一篇文章有 `/help/superintelligence/`、`/help/artificial-intelligence/`、`/en-gb/help/...` 等多个地址，编号相同即为同一篇；`sourceUrl` 用 `/help/superintelligence/<编号>/`，其他地址不必列入 `altUrls`，按编号去重。
- 已知文章（2026-11-04 盘点，编号）：入门 1331373868832401、Artifacts 2074655449783957、指导与批准 1385290430137537、Mac 1126304576638594、提醒与计划任务 1484325780075655、数据管理 2225571704857152、个性与记忆 995796179982326、技能 2797651547267109、连接器 1687253048996149、浏览网页 2124746764949121、付款 1436362127544482、隐私与安全 1047255454427887、订阅 1021145227643680 与 1625680452306909、帮助中心首页 1303670544995562。

### Meta Newsroom（about.fb.com）

- 页首的「要点」（Takeaways）框不在 `<article>` 容器内，只抽 `<article>` 会漏掉；要单独抽取，放在正文之前。
- 页面顺序为：标题、头部视频、要点框、正文。视频是 `<video>` 标签，`<source>` 中有 mp4 地址，按占位行保存。
- `article:published_time` 与 `article:modified_time` 分别对应 `date` 与 `updatedAt`。
- 作者字段为站点编辑账号（如 heathera），不是署名作者，不填入 `author`。

### 同一篇文章的多个官方地址

| 文章 | 地址 |
| --- | --- |
| 我们如何设计 Muse | `introducing.muse.ai`、`muse.ai/blog/how-we-designed-muse` |
| 我们如何将安全构建进 Muse | `security.muse.ai`、`research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse`、`muse.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse` |

收录时 `sourceUrl` 取发布稿中链接的地址，其余写入 `altUrls`。

### introducing.muse.ai

- 图片地址形如 `/_next/image?url=...`，直接下载 `/_next/static/immutable/media/<文件名>` 即可得到原图；保存时去掉文件名中的哈希后缀。
- 页首视频「Muse organizing everyday life」由脚本加载，取不到视频地址，用封面图加指向页面的占位行。

## 命名约定

- 帮助文档 slug 以 `help-` 开头，例如 `2026-09-08-help-guidance-and-approval`。
- 日文资料 slug 用英文意译。
