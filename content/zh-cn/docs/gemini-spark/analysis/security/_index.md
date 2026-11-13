---
title: "Gemini Spark：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Spark 的防护以逐项确认为主：发送、修改删除、购买、提交表单、用 Google 登录都要用户确认，另有敏感信息检查和接管模式；官方明确承认提示注入风险，并说用户监督是最重要的防线。截至 2026-11-10 没有已披露的漏洞。
---

## 概要

- 权限模型是逐项确认：发送通信、修改或删除数据、购买、金融交易、提交网页表单、用 Google 登录，每次都要用户确认；即使设成「始终允许」，非常敏感的操作仍每次都问。例外是 Google Tasks 私密任务的批量操作，可以不经确认。
- 模型之外的防护有：敏感信息检查（向网站或应用分享健康、财务、证件号前暂停）、接管模式（输入密码和付款信息时交给用户）、提交后展示计划与进度、浏览只限于与任务相关的网站。资料中没有类似 Muse Sentinel 的独立审查模型。
- 凭证不经过对话：官方要求不要在任务线程里输入登录和付款信息；但本地 Chrome 下 Spark 经许可可以用密码管理器里保存的登录信息。对这一点的评价两极：Top5Apps 称其为「品类中最宽松的默认设置」，Freistyle AI 则在推荐表中称 Google 的「确认规则最清楚」。
- 官方帮助页详细列出提示注入的后果（外泄私人信息、转发邮件、运行恶意命令），并承认这些防护「并不保证能防范所有风险」，离线运行的计划可能无法阻止非预期操作。
- 截至 2026-11-10 的资料中没有已披露的漏洞、安全事件或漏洞赏金；10 月的表格写入故障是平台策略检查误拦，不是安全事件。

## 每次都要确认的操作

截至 2026-11-10 的帮助页（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）：

- **每次确认**：发送通信、修改或删除数据、购买、金融交易、填写并提交网页表单、使用 Google 登录。即使权限偏好设为始终允许，「非常敏感的操作每次都需要你的许可」。
- **文档编辑**：编辑共享的文档、表格、幻灯片前，用户要审阅并确认计划的修改。
- **例外**：可以「在未经你确认的情况下对 Google Tasks 中的私密任务执行批量操作」。
- **拒绝**：用户拒绝某项操作时，Gemini 停下且不会尝试其他方式完成。
- **网页浏览**：本地 Chrome 首次使用要授权，之后每项涉及浏览的任务都先请求确认。

其他场景的确认规则与此一致：自定义 MCP 应用的任何写入操作都要手动确认（[帮助：自定义应用]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-custom-apps" >}})）；相册任务在创建共享相册、发邮件前请求许可（[帮助：相册工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-google-photos-workflows" >}})）；Mac 上永久删除文件、向第三方发送或共享文件前请求许可（[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})）。

官方的这套规则从发布起就有：I/O 发布稿称在「花钱或发送电子邮件等高风险操作前先征求你的意见」（[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})），Chrome 集成稿称在付款等敏感操作上「把任务交还给你」（[Chrome 集成]({{< relref "/docs/gemini-spark/sources/official/2026-07-30-spark-chrome" >}})），产品页称「在采取重大行动前先与你确认」（[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})）。

## 模型之外的防护

帮助页列出的其他防护（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）：

- **敏感信息检查**：向网站或关联应用分享健康、财务、政府证件号等信息前，「Gemini 会暂停并请求你的许可」。
- **禁止任务识别**：帮助页列有这一项，未展开说明。
- **接管模式**：输入密码或付款详情时由用户接管浏览器，直接在网页上输入。
- **透明**：提交任务后展示计划和进度。
- **浏览范围**：限制在与任务相关的网站和操作，部分是为了对抗提示注入。

官方同时写明这些措施「并不保证能防范所有风险」，「你的主动监督是防范风险最重要的方式」（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。产品页 FAQ 末尾的提示是「检查回答。密切监督，必要时打断」（[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})）。

第三方的对照：iThome 列出 Muse 有独立的 Sentinel 哨兵智能体、Dots 有 Auto-review，Spark 则是高风险操作要求明确同意（[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})）。Datawhale 综述与鸿煊转述官方称 Spark 「仍是实验早期功能」，并提到 DeepMind AI Control Roadmap 的异步监控研究，两篇都没有注明出处（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。

## 凭证：不进对话，但可用密码管理器

- 官方建议不要把登录信息、付款详情输入任务线程，需要时接管浏览器直接在网页输入（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）；Mac 帮助页同样要求不在任务对话里输入登录、付款信息（[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})）。
- 本地 Chrome 下，Gemini 可访问与用户相同的网站，包括已登录网站，经许可可以用密码管理器中的登录信息（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})、[Chrome 集成]({{< relref "/docs/gemini-spark/sources/official/2026-07-30-spark-chrome" >}})）。
- 远程浏览器的 Cookie 保存在云端供后续会话使用（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。

对这套设计，第三方评价相反：

| 评价 | 理由 | 资料 |
| --- | --- | --- |
| 「该品类中最宽松的默认设置」 | 确认发送和购买，但会使用用户保存的密码 | [Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}}) |
| 「Google 的确认规则最清楚」（推荐表中的理由） | 发送、删除、购买、付款、表单、Google 登录都要确认，密码与付款详情交回用户输入；但同一作者给各家的安全与数据说明排序时，把 Microsoft 和 OpenAI 排在最前，称 Google「说清楚的是：Keep Activity 意味着训练与人工审核」 | [Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}}) |

## 官方承认的提示注入风险

帮助页举出的例子是：网页或文件中的恶意指令可能让智能体取出邮件或文档中的私人信息发布到公开网站、把 Gmail 邮件发到外部服务、运行恶意命令实现「持久的数据外泄」；建议删除远程浏览器数据、清除代码执行历史，避免安排敏感任务，并提醒「如果计划在你离线时运行，你可能无法阻止 Gemini 完成非预期的操作」（[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})）。

WIRED 引用了帮助页的提示注入示例，认为「仅这条免责声明就足以让大多数用户不去尝试」，并不建议让 Spark 访问整个收件箱（[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})）。Datawhale 综述称 Muse、Dots、Spark 的公开资料都没有宣称已彻底解决提示注入（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。

Mac 上的风险另有说明：Gemini 可以永久删除文件或向第三方发送、共享文件；不要加入敏感或丢失不起的文件；公共云盘加入「已连接的文件夹」后，Gemini 可访问、编辑、共享、删除其中文件（[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})）。

推断：离线运行的计划与「用户监督是最重要的防线」之间存在张力。持续执行是 Spark 的卖点，但官方把最后一道防线放在用户实时监督上；计划在用户离线时运行，确认卡片只能等用户回来，或者对 Google Tasks 私密任务这类例外直接执行。

## 事件与漏洞

截至 2026-11-10 的资料中，没有 Spark 的漏洞披露、安全事件报道或漏洞赏金信息，也没有独立安全审计。

2026-10-13 起的表格写入故障中，Spark 的写入在执行前被「Blocking policy check」拦截；楼主分析是平台策略层的回归，不是 Sheets API 授权问题，10-16 回报已修复（[开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}})）。这是策略检查误拦正常操作，说明 Spark 的写入在执行前要经过一层策略检查，但资料没有这层检查的官方说明。

The Verge 实测中 Spark 请求访问通讯录，作者拒绝后任务仍完成；作者提醒必须检查输出，因为 Spark 会从个人信息中提取内容发给认识的人，风险更高（[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})）。

## 资料缺口

- 「禁止任务识别」「策略检查」的具体机制；是否有独立于主模型的审查层。
- 漏洞赏金是否覆盖 Spark；第三方安全研究或红队测试。
- 本地 Chrome 使用保存的密码时，每个网站是否单独授权。
- Google Tasks 私密任务批量操作免确认的理由。

## 主要资料

- 官方：[帮助：任务与工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-and-workflows" >}})（确认清单、防护、提示注入）；[帮助：Mac 上的任务]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-tasks-on-mac" >}})；[帮助：自定义应用]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-custom-apps" >}})；[帮助：相册工作流]({{< relref "/docs/gemini-spark/sources/official/2026-11-05-help-google-photos-workflows" >}})；[I/O 发布稿]({{< relref "/docs/gemini-spark/sources/official/2026-05-19-next-evolution-gemini-app" >}})、[Chrome 集成]({{< relref "/docs/gemini-spark/sources/official/2026-07-30-spark-chrome" >}})、[产品页]({{< relref "/docs/gemini-spark/sources/official/2026-10-11-spark-product-page" >}})。
- 媒体：[WIRED 上手]({{< relref "/docs/gemini-spark/sources/media/2026-05-29-wired-spark-hands-on" >}})；[The Verge 上手]({{< relref "/docs/gemini-spark/sources/media/2026-06-01-verge-spark-hands-on" >}})；[iThome 五款比较]({{< relref "/docs/industry/sources/media/2026-10-02-ithome-five-proactive-agents" >}})。
- 社区：[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})、[Freistyle AI 小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})（相反的评价）；[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})；[开发者论坛：表格写入失败]({{< relref "/docs/gemini-spark/sources/community/2026-10-13-google-dev-forum-sheets-blocked" >}})。
