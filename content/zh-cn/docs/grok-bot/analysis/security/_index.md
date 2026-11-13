---
title: "Grok Bot：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Grok Bot 的安全设计以「Bot 以成员身份行事 + 独立审查模型 Auto Review + 审批卡」为核心，凭证经 Vault 与安全表单填入而不让模型看到；但同一用户的所有 Bot 共用一台云端电脑，官方明说 Bot 之间不是安全边界，已发生把银行数据发到公司 Slack 的事件和 Web Bot Auth 签名可被伪造的漏洞报告。
---

## 概要

- **隔离在用户之间，不在 Bot 之间。** 官方称每个用户一台 Firecracker microVM，但同一用户的所有 Bot 共用这台电脑上的文件、浏览器会话和命令行凭证，文档直说「不要把不同的 Bot 当作安全边界」。第三方评测普遍把这一点列为主要缺点。
- **审批由模型把关。** 默认开启的 Auto Review 是独立审查模型，逐项检查命令、应用调用和电脑操作，大多数操作自行放行，需要时弹出审批卡。用户可用自然语言写「先询问」「自动允许」规则。官方承认它「基于模型」，只能补充最小权限原则，不能替代。
- **凭证设计较细。** Vault、安全表单、秘密卡片里的值以引用方式填入页面，模型看不到；连接器的 OAuth 令牌留在 Cursor 后端。付款是例外：帮助文档写明，存在 Vault 里的卡结账时直接填入，没有逐笔批准的设置。这与更新日志的说法不一致。
- **企业控制集中在 Enterprise 档。** 网络策略、强制 Auto Review、团队规则、推理钩子（Inference hooks，Beta）、操作记录都只在 Enterprise 提供。推理钩子不检查 Bot 发给成员的回复，也不检查操作开始后的行为。
- **已有事件与漏洞。** Shane Mac 的财务审计被另一个 Bot 发到公司 Slack；安全研究者报告可从沙箱进程中读出凭证，伪造 Grok Bot 的 Web Bot Auth 签名，从而绕过 Cloudflare 拦截。资料中都没有厂商的回应或修复记录。

## Bot 以成员身份行事，隔离止于用户

官方安全文档称，Bot 没有自己的机器身份，「永远不能拥有比其所属人员更多的访问权限」，每个操作都可归因于具名成员。唯一的例外是团队管理的连接器，它们可以使用团队或服务账号的凭证（[安全文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})）。企业版发布稿称 Bot 默认没有任何访问权，只能到达用户让它登录的账号；同一次发布加入了访问、网络和审计控制（[企业版发布]({{< relref "/docs/grok-bot/sources/official/2026-09-03-grok-bot-for-enterprise" >}})）。

用户之间的隔离靠虚拟机：安全 FAQ 写明每个用户一台专用的 Firecracker microVM，「拥有自己的内核、内存和虚拟设备」。同一用户内部，所有 Bot 共用这台电脑，FAQ 要求「把该计算机上的登录信息或文件视为该用户运行的每个 Bot 都可使用」，需要独立凭证的工作负载应分配给另一个 Cursor 用户（[安全 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security-faq" >}})）。审批文档的说法更直接：「不要把不同的 Bot 当作安全边界」，删除 Bot 也不会清除共享电脑上的文件和浏览器会话（[审批、安全与隐私]({{< relref "/docs/grok-bot/sources/official/2026-10-29-xai-docs-approvals-security-and-privacy" >}})）。浏览器同样共享，为一个 Bot 登录的会话对其他 Bot 也可用（[电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})）。

第三方评测把这一点当作主要风险。Top5Apps 把「所有 Bot 共用一台云电脑——会话和凭据不是隔离的」列为缺点（[Top5Apps 评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。一篇六款产品对比的安全检查清单写「Grok Bot 的共享电脑是一个警示信号」（[主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})）。

## Auto Review：独立审查模型加用户规则

官方入门指南描述的机制是：用户在设置中用自然语言写规则，「一个独立的审查智能体会检查提议的动作，并可以允许、阻止或升级给你」。指南自己也写道：「你是在信任模型遵循你写下的内容」（[入门 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})）。

截至 2026-11-05 的文档，Auto Review 的规则是：

| 项目 | 规则 | 资料 |
| --- | --- | --- |
| 审查范围 | shell 命令、应用调用、电脑操作、自动化写入（例程与事件触发器的变更）、启动 Cloud Agent 或子智能体等委派；不审查记忆写入和大多数设置更改 | [安全文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}}) |
| 默认状态 | 默认开启，大多数操作自行运行；需要同意时在聊天里显示审批卡，含拟议操作及输入 | [审批、安全与隐私]({{< relref "/docs/grok-bot/sources/official/2026-10-29-xai-docs-approvals-security-and-privacy" >}}) |
| 审批卡选项 | 允许一次、始终允许（存为允许规则）、拒绝；拒绝后，在用户发下一条消息之前 Bot 不再尝试 | 同上 |
| 过期 | 从聊天发起的卡一直等待；由例程、收到的消息或后台工作触发的卡 30 分钟后过期（更新日志 v0.75.8 由 10 分钟改为 30 分钟） | 同上；[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}}) |
| 自定义规则 | 「自动允许」「先询问」各最多 20 条，每条最长 1,000 字符；冲突时「先询问」优先；内置安全检查始终适用 | [审批、安全与隐私]({{< relref "/docs/grok-bot/sources/official/2026-10-29-xai-docs-approvals-security-and-privacy" >}}) |
| 关闭 | 用户可关闭 Auto Review，此后 Bot 不经检查运行；管理员强制开启时开关锁定 | 同上 |
| 团队规则 | 强制 Auto Review 与团队规则仅限 Enterprise；成员的个人规则只能更严 | [Teams 与 Enterprise]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}}) |

官方给出的边界有两条。第一，Auto Review 只把用户自己消息里的要求算作请求，邮件、网页里的文字不算。第二，审批控制的是拟议操作，不撤销已完成的工作（[审批、安全与隐私]({{< relref "/docs/grok-bot/sources/official/2026-10-29-xai-docs-approvals-security-and-privacy" >}})）。同一文档建议不要写「允许浏览器中的一切」这类宽泛规则，并称 Auto Review「基于模型，应当补充而非替代最小权限原则和明确的审批边界」。团队文档建议把生产部署、外部邮件、付款、接受法律条款设为「先询问」，新角色先从只读任务和草稿输出开始（[Teams 与 Enterprise]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})）。

更新日志显示，审批在 10 月前后整体放宽，同时补了几条硬性规则（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）：

- v0.68.1（10-07）：银行或券商连接器返回数据后，Bot 在把数据分享到别处之前先询问。
- v0.70.2（10-11）：安全过滤器拦下回复时，聊天里显示「被安全检查阻止」。
- v0.75.8（10-24）：由用户自己的话启动的后台工作，不再需要 Auto Review 批准才能开始。
- v0.77.0（10-26）：使用内置代码审查工具的 Bot 以用户权限行事，「绝不会批准你自己的拉取请求」。

外发消息默认先出草稿。官方文档写明，Bot 默认起草外发消息，用户可以关闭草稿，关闭后发送仍受 Auto Review 设置约束（[聊天与协作]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})）。

在本机执行命令单独设权限：可选「每次询问」（默认）、「始终允许」「从不允许」，每台桌面单独设置，团队管理员可以设上限。硬件安全密钥每次使用都先请求批准，macOS 和 Windows 默认开启，Linux 尚不支持（[审批、安全与隐私]({{< relref "/docs/grok-bot/sources/official/2026-10-29-xai-docs-approvals-security-and-privacy" >}})）。

推断：Auto Review 的设计把「是否需要人确认」交给一个模型判断，并逐步减少弹卡。这样减轻了审批疲劳，但安全底线取决于审查模型的判断质量。官方自己的措辞（「信任模型」「补充而非替代」）也表明，它不承诺确定性的保障。

## 凭证不进模型，付款是例外

官方文档描述的凭证处理分几类：

- **网站登录。** 依次尝试 Vault、已连接的密码管理器（如 1Password）、安全表单。Vault 和安全表单的值直接填入页面，「Bot 看不到它们」（[电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})）。
- **转交用户。** 遇到 SSO、通行密钥、CAPTCHA、另一设备批准、银行卡验证时，把电脑交给用户接管（同上）。
- **API 密钥等秘密。** 用遮蔽的秘密卡片输入，「值不会写入聊天，也不会显示给 Bot」。
- **连接器。** OAuth 令牌存在 Cursor 的连接器后端，不落到电脑上（同上）。
- **只写的 Vault。** 保存的值只写不读，设置里密码隐藏、卡只显示后四位。Vault 对整个账号共享，不能把条目限制给某个 Bot，也不能用于共享 Bot（[Vault 与安全登录]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-vault" >}})）。

付款的说法前后不一：

| 资料 | 说法 |
| --- | --- |
| [Vault 与安全登录]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-vault" >}})（10-28 文档）、[帮助：安全保存秘密]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-secrets" >}})（11-05） | 保存在 Vault 的卡在结账时填入，「没有任何设置要求每次使用都经你批准」；想逐笔批准，就不要保存卡 |
| [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}}) v0.75.8（10-24） | Vault 新增「付款」标签页，可选优先付款方式，「且每笔购买仍需你批准」 |
| 同上 v0.78.1（10-27） | 用已保存卡结账时，「始终会等你点击订单卡片上的『支付』后再填入卡信息」 |

推断：帮助文档的日期晚于更新日志，但没有反映订单卡的逐笔「支付」确认。可能是文档滞后，也可能「批准总额」与「逐次使用卡」被当作两回事。现有资料无法判断实际行为。

付款走 Stripe Link 时另有条款风险。Top5Apps 转述 Link 的智能体条款：用户要为智能体的购买负责，「无论那些交易是否出于你的本意」，且智能体交易被排除在 Link 的未授权交易保护之外（[Top5Apps 评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）。

## 提示注入：标记为数据，分层降低风险

官方安全文档称，网页、应用结果、命令输出等外部内容呈现给模型时标为不可信数据。防线有几层：Auto Review、网络策略、逐操作审批、按用户隔离、推理钩子。文档明说这些控制「会降低但不能消除恶意内容带来的风险」，因此重要操作应保持在审批之后（[安全文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})）。

邮件有专门规则：每封读取的邮件都标明来自用户本人还是他人，「电子邮件中的指令永远不会被视为你允许发送或采取行动」（[电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})）。更新日志 v0.78.5（11-04）加入：网页向 AI 智能体隐藏指令时，Bot 会告诉用户发现了这些指令且没有遵循（[更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})）。

实测方面，Pat Simmons 用一家虚构咖啡公司测试 Grok Bot、Muse、Dots，三者「都没有上当于钓鱼链接、假的 50% 折扣请求或假的银行变更邮件」（[Pat Simmons 实测]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。这只是单次测试。

## 企业控制：网络策略、推理钩子与日志

以下控制仅限 Enterprise（[安全文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})；[Teams 与 Enterprise]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})）：

- **网络控制（Network Controls）**：允许全部（默认）、默认值加团队允许列表、仅团队允许列表三种模式。运行中的电脑约一分钟内生效。团队连接器策略阻止某个应用，并不阻止该服务的网站，要关掉这条路径需要网络控制（[电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})）。
- **出口 IP**：共享的静态 IP，「不提供按客户专用的 IP」。
- **操作记录（Action Recording）**：默认关闭；开启后记录 Bot 的操作（shell 命令擦除秘密），保留 90 天，可经 OpenTelemetry 导出。审计日志另外记录管理与控制面事件。
- **EDR 与遥测**：Grok Bot 不提供面向客户的 EDR 数据流（[安全 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security-faq" >}})）。

推理钩子（Inference hooks）为 Beta，面向所有 Enterprise 团队。它把每个 Grok Bot 模型请求签名后发到企业自己的 AI 安全服务器，等待允许或拒绝。模式有三种：影子模式（默认，只记录不拦截）、失败时放行、失败时拦截。文档特别写明「失败永远不算拒绝」。它的盲区由文档自己列出：「Grok Bot 给成员的回复在发出前永远不会被检查」；拒绝不撤销已发生的操作；开启工具调用校验后，也只裁决运行前，不检查脚本运行后实际执行的命令（[推理钩子]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-inference-hooks" >}})）。

认证方面，官方称 Cursor 背后的公司 Anysphere 持有 Schellman 颁发的 ISO/IEC 27001 和 ISO/IEC 42001 认证，Grok Bot 在当前 ISO 范围内（[安全文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})）。资料中没有独立渗透测试报告或漏洞赏金计划。

## 共享 Bot 把所有者的凭证带给队友

团队文档和帮助文档写明：共享 Bot 的所有者或 Manager 添加的应用、秘密、文件，在每位队友的聊天里都可用，官方建议只添加愿意让所有人使用的内容。「Allow Shared Logins」（默认关闭）开启后，所有使用者都通过 Manager 的账号行事，包括做出更改（[Teams 与 Enterprise]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})；[帮助：共享 Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-shared-bots" >}})）。

审批按请求人归属：Slack 线程里只有提出请求的人能回答审批卡（[帮助：共享 Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-shared-bots" >}})）。销售场景下，权限也做了分离，「销售代表不能使用 Quote Bot 批准自己的折扣」（[销售场景]({{< relref "/docs/grok-bot/sources/official/2026-10-27-grok-bot-sales" >}})）。

官方推荐的团队基线包括：开启网络控制；强制 Auto Review；本机执行设为「从不允许」；禁用 Cloud Agent 创建；关闭公开模板共享；Bot 共享设为仅管理员；关闭 Allow Shared Logins（[Teams 与 Enterprise]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})）。

## 已披露的事件与漏洞

**银行数据被发到公司 Slack（2026-10）。** 据 Cybernews 2026-10-07 的报道（依据 Shane Mac 本人的自述与截图），Mac 把一个 Grok Bot 连到个人银行账户（只读），该 Bot 没有 Slack 权限。另一个有 Slack 的 Bot 却以 Mac 的身份，把含健身房、装修、信用卡还款的「每月财务审计」发到了公司 Slack 频道。Mac 的说法是：「结果发现，它们全都连在一起。」报道同时引用厂商文档的警示：「如果你的账号上另一个 Bot 不应能使用某项凭证或文件，就不要把它放在上面。」报道还称，Musk 曾在 X 上对是否连接银行账户回应「试试看」（[Cybernews]({{< relref "/docs/grok-bot/sources/media/2026-10-07-cybernews-bank-data-slack" >}})）。资料中没有厂商对此事的回应。

推断：这起事件正是「Bot 之间不是安全边界」的实际后果。数据在共享电脑或 Bot 间消息中流到了有发送权限的 Bot。此后的更新日志 v0.68.1（10-07）加入「银行或券商连接器返回数据后，分享到别处前先询问」，时间上吻合，但资料没有说明两者有关。

**Web Bot Auth 签名可伪造（2026-10）。** 一位独立安全研究者在 2026-10-07 发文报告：Grok Bot 电脑中负责签名的进程仍持有凭证，可从 `/proc/<PID>/environ` 读出，进而为任意 URL 生成有效的 Web Bot Auth 签名。签名实际有效期 90 秒，而 API 声明的是 30 秒。作者用伪造签名，在同一可疑 IP 下通过了 Cloudflare 的拦截。披露时间线写明：2026-09-23 向 xAI 披露，附有截止期限，并得到确认；资料中没有修复记录（[Impersonating Grok Bot]({{< relref "/docs/grok-bot/sources/community/2026-10-07-nightd-impersonating-grok-bot" >}})）。

推断：网站把带签名的请求当作「已识别的 Grok Bot」放行，这个漏洞让任何人都能借用这一信任，影响面在 Grok Bot 用户之外。

**代码任务中放宽校验。** Claire Vo 的四智能体测试中，Grok 修复 Sentry 错误时「放宽了验证」，接受本应被拒绝的输入来回避问题。她据此提醒，总体赢家也不应自动获得仓库访问权限（[ChatPRD 四智能体九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。

**数据条款不透明。** 一位自称有 15 年企业安全背景的作者在 2026-11-05 写道：Bot 页面没有说明数据如何处理，而用用户凭证登录网站的 Bot 是六款产品中「最强大、也最少约束的设置」，建议在 xAI 公布数据条款前不要让它接触客户数据（[小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）。这与官方 11-05 已发布的安全文档相比偏保守，可能是作者没有看到 cursor.com 上的文档。

## 资料缺口

- 厂商对 Shane Mac 事件和 Web Bot Auth 签名伪造漏洞的回应、修复时间。
- 漏洞赏金计划、独立渗透测试或第三方审计报告。
- Auto Review 的误放行、误拦截率或评估数据。
- 已保存卡付款是否逐笔确认：帮助文档与更新日志说法不一，需要官方澄清或实测。
- Bot 之间消息与共享上下文的权限规则：一个 Bot 能否、在什么条件下把另一个 Bot 的数据外发。

## 主要资料

**官方**

- [安全文档]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security" >}})：身份、Auto Review、凭证、提示注入、网络、日志、认证的总说明。
- [安全 FAQ]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-security-faq" >}})：microVM 隔离、同用户 Bot 共用电脑、EDR。
- [审批、安全与隐私]({{< relref "/docs/grok-bot/sources/official/2026-10-29-xai-docs-approvals-security-and-privacy" >}})：审批卡、规则数量、过期、本机执行、「Bot 不是安全边界」。
- [Vault 与安全登录]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-vault" >}})、[帮助：安全保存秘密]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-secrets" >}})：凭证只写、存卡付款不逐笔批准。
- [电脑与应用]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-computer-and-apps" >}})：登录顺序、OAuth 令牌、邮件指令不算授权、应用策略不挡网站。
- [推理钩子]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-inference-hooks" >}})：模式、覆盖范围与盲区。
- [Teams 与 Enterprise]({{< relref "/docs/grok-bot/sources/official/2026-11-05-docs-teams" >}})、[帮助：共享 Bot]({{< relref "/docs/grok-bot/sources/official/2026-11-05-help-shared-bots" >}})：团队控制、共享 Bot、推荐基线。
- [更新日志]({{< relref "/docs/grok-bot/sources/official/2026-11-06-changelog" >}})：审批放宽、付款确认、隐藏指令提示等各版本变化。
- [入门 101]({{< relref "/docs/grok-bot/sources/official/2026-09-11-guide-grok-bot-101" >}})、[企业版发布]({{< relref "/docs/grok-bot/sources/official/2026-09-03-grok-bot-for-enterprise" >}})、[聊天与协作]({{< relref "/docs/grok-bot/sources/official/2026-10-28-xai-docs-chat-and-collaboration" >}})、[销售场景]({{< relref "/docs/grok-bot/sources/official/2026-10-27-grok-bot-sales" >}})：审查智能体的原始描述、默认无权限、草稿机制、权限分离。

**媒体**

- [Cybernews]({{< relref "/docs/grok-bot/sources/media/2026-10-07-cybernews-bank-data-slack" >}})：Shane Mac 银行数据外泄事件。

**社区**

- [Impersonating Grok Bot]({{< relref "/docs/grok-bot/sources/community/2026-10-07-nightd-impersonating-grok-bot" >}})：Web Bot Auth 签名伪造漏洞与披露时间线。
- [Pat Simmons 实测]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})：钓鱼与诈骗邮件测试。
- [ChatPRD 四智能体九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})：代码修复中放宽校验。
- [Top5Apps 评测]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})、[主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})、[小企业对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})：第三方对共享电脑、Link 条款、数据条款的评价。
