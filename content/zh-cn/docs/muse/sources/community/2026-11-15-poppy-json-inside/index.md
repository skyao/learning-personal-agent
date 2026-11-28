---
title: "poppy.json 里到底写什么：对照 1.0 规范与验证器实测"
linkTitle: "poppy.json 内容核查"
date: 2026-11-15
originalTitle: "Inside poppy.json: What a Business Actually Publishes for Poppy 1.0, Checked on personalagentprotocol.org and the Validator Itself"
sourceUrl: "https://museexplained.com/guide/inside-poppy-json-what-a-business-publishes-poppy-1-0/"
author: "Marvin Jones"
publisher: "Muse Explained"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-16
tags: [连接器, 实测评测]
products: [muse]
dateNote: "JSON-LD 标注 datePublished 与 dateModified 均为 2026-11-16（UTC 日期），页面正文核查记录均为 11 月 15 日，按页面实际发布日记为 11-15。"
---

{{< source-info >}}

**收录说明**：直接下载；无图片。作者全文通读了 Poppy 1.0 规范第 3 节、指南、扩展页面与企业实施工具包，并对规范自带的示例文档离线运行了工具包里的验证器。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：本文是 Muse Explained 站的 Poppy 落地核查第二篇：作者于 2026 年 11 月 15 日全文通读了 Poppy 1.0 规范第 3 节、指南、扩展页面与企业实施工具包，并对规范自带的示例文档离线运行了工具包里的验证器。按规范第 3.1 节字段表，poppy.json 只有两个必填字段——protocol_version 与 organization——另须至少提供 agent、apis、web 三种渠道之一。离线验证结果为 Foundation 里程碑 7 项通过、0 项失败、7 项跳过，跳过的是需要联网的检查。同日核查发现，协议自家演示站点（含其 poppy.json 与协议检查器）均返回 Not Found，且截至 11 月 15 日仍无 Muse 内出现 Poppy 行为的实证，也无 Mercury、Synchrony、土耳其航空或 Shopify 以自家名义发布的公告。Mediated Sign-In 定于 2027 年 3 月 17 日退役，作者定于 11 月 23 日再次核查上述未决事项与首个真实企业 poppy.json。

**保留理由**：已收资料已有 Sierra 与 Muse 两份 11 月 13 日官方公告、allthingsmuse 的实施细节和本站 Part 1 的落地核查台账，但均未逐条核对规范原文或实际运行验证器。本篇逐项读了规范第 3 节与实施工具包并离线跑了验证器，给出了 poppy.json 字段规则与验证器实测结果，是已收资料中没有的一手核查。

---

## Poppy 承诺台账，第 2 部分

Poppy 承诺台账，第 2 部分

这是本站 Poppy 系列报道的第 2 部分。第 1 部分发表于 2026 年 11 月 15 日，报道了 Sierra 11 月 13 日帖子中的上线声明：Poppy 已向所有使用 Muse 的用户开放，Muse 访问每个网站时都会先查找 Poppy。那篇帖子点明了本篇要做的核查：直接读取协议自家网站上的实施文件，并用协议自带的验证器对它进行测试。

- 上线声明，2026 年 11 月 13 日：Sierra 的帖子，已全文阅读。Poppy 1.0 发布在 personalagentprotocol.org，Shopify 已为每个商家启用，Mercury、Synchrony 和 Turkish Airlines 被列为即将上线，设计合作伙伴总共超过 100 家。
- 实施工具包核查，即本篇，2026 年 11 月 15 日：1.0 规范、指南、扩展页面，以及 personalagentprotocol.org 上的企业实施工具包，均已全文阅读；另外还把工具包 GitHub 仓库里的验证器离线运行于规范自带的示例文档。结果见下文验证器一节。
- 仍未决，2026 年 11 月 15 日核查：在 Muse 内没有目睹 Poppy 行为的证据，Mercury、Synchrony、Turkish Airlines 或 Shopify 也都没有以自家名义发布公告。11 月 15 日的 DuckDuckGo 检索两者都没有找到。Synchrony 自家的 Poppy 条目都出自 2026 年 10 月，早于 1.0：10 月 15 日的一篇博客文章，以及 10 月 20 日一份关于作为设计合作伙伴加入的 8-K 文件。
- 下次核查：2026 年 11 月 23 日，针对上述两行未决事项，以及一份本站能用验证器的 survey 命令运行、并能具名打印出来的真实企业 poppy.json。

## 文件本身，以及它必须放在哪里

企业通过在一个固定地址发布一份 JSON 文档来加入 Poppy：`https://<domain>/.well-known/poppy.json`，以 application/json 通过 HTTPS 提供。规范第 3 节对另一种情形说得很直白：如果企业没有 poppy.json，它就不属于该协议。

这份文件告诉个人智能体四件事：企业是谁、如何与它启动一个会话（Session）、登录如何工作，以及它提供哪些渠道，即它的网站、它的 API，或它自己的企业智能体。智能体还会通过第二条途径获知登录的签发方（issuer），即标准 OAuth 元数据。企业在 /.well-known/oauth-protected-resource 发布受保护资源元数据（RFC 9728），其中的 authorization_servers 列表列出签发方，智能体随后跟进该签发方的 OAuth 服务器元数据（RFC 8414），以获取端点和登录方式。

第 3 节有两条规则统辖这份文件所说的一切。第一：只能依赖文档明确声明的内容。个人智能体不得假定文档未声明的服务、端点或方法。第二，来自第 3.1 节：标为可选的字段可以缺失，必填字段必须存在，存在的字段必须是正确的类型，并且个人智能体必须忽略未知字段。最后这条规则正是下一节那些确切形式值得逐字列出的原因。用错形式写的字段不是风格错误，而是智能体无法按原样使用的字段。

## 必填：两个字段，外加一个渠道

第 3.1 节的字段表恰好把两个字段标为必填，并把一组字段标为企业不能跳过的选择。

- protocol_version。必填。本文档遵循的协议版本，写作 major.minor。对本规范而言是「1.0」。个人智能体只有在版本与其所实现的版本兼容时才使用该文档，并且必须首先检查这个字段。
- organization。必填。企业的显示名称、域名，以及可选的 logo_uri。域名必须是在任何重定向之后提供该文档的主机。这项检查可防止一份被复制到其他域名的文档代表该企业发言。
- agent、apis 或 web 至少其一。企业必须至少提供一个渠道。agent 列出企业智能体的会话协议，每项含 type、HTTPS 端点和描述。apis 列出 API，每项含 type、url 和描述。web 是企业的网站，可带一个可选的 browser_session_endpoint，智能体的浏览器在那里加入会话。

这就是全部必填清单。只有网站的企业用 protocol_version、organization 和 web 就能满足。指南说得很明白：如果你的网站已支持登录，最省事的路径就是发布一份只列 web 的 poppy.json。个人智能体之后会使用网站，而不是 API。

## 第 3.1 节的可选字段：auth、tasks、extensions 与 supported_versions

- supported_versions。企业提供的其他协议版本，每个版本映射到该版本文档的 URL。它是对象，一个从版本到 URL 的映射，不是列表。若省略，则企业只支持 protocol_version。每个 URL 必须与提供 poppy.json 的主机在同一主机上，且每个版本的文档必须携带相同的 organization.domain 和相同的 issuer。
- auth。企业的登录细节。其组成部分是 issuer、disabled、scopes 和 scope_hints，下面逐一说明。
- auth.issuer。是有条件的，而不只是可选。如果该域的受保护资源元数据列出多个授权服务器，auth.issuer 选出个人智能体使用的那一个，且它必须在该列表中。只有一个服务器时，企业可以省略它。
- auth.disabled。默认为 false。设为 true 时，它告诉个人智能体：企业虽有签发方，但不提供登录，智能体不得与该企业启动登录。
- auth.scopes。作用域描述，以作用域名称为键。它是一个对象：每个作用域名称映射到一段书面描述，说明该作用域允许什么，形式与 OpenAPI 中 OAuth 2.0 安全方案的作用域相同。在规范的示例中，orders:read 被描述为「查看你的订单、退货和预订」，orders:write 涵盖换货、退货和预订变更。
- auth.scope_hints。关于每个作用域允许什么的提示，以作用域名称为键，有两个具名部分：changes 和 personal_data。在示例中，orders:read 的 changes 为「none」、personal_data 为 true，orders:write 的 changes 为「irreversible」、personal_data 为 true。撰写自家文件的企业必须以这种方式公开地给自己的作用域定级，而且是在任何智能体请求它们之前。
- web.disabled。默认为 false。为 true 表示企业要求个人智能体不要浏览其网站，而应改用其企业智能体和 API。
- web.unscoped。默认为 false。为 true 表示网站不施加企业的其他作用域，因此在网站上 poppy:browser-sign-in 作用域会给予该账户的完全访问权。
- tasks。一个端点，一个 HTTPS URL，个人智能体在那里获取企业选择不通过协议提供的任务、企业发布的技能，以及反馈的发送地址。
- extensions。企业支持的扩展，以名称为键，每个支持的版本一个条目。第 3.3 节补充了形式：每个名称映射到一个版本条目列表，纯名称保留给随协议定义的扩展，其他任何人都必须以自己控制的域名开头来命名扩展。

一个形式上的警告，因为这是文件里最容易犯的错：agent 协议条目和 apis 条目用的不是同一个词来表示地址。agent 协议条目携带 endpoint，apis 条目携带 url。验证器的 schema 检查会强制执行第 3.1 节的形式，如下面的运行结果所示。

## 规范自带的示例，简述

第 3 节给出了一份完整的示例文档，对象是 example.com 上一家虚构的 Example Company。它的结构如下（此处描述有缩短，全文见规范页面）：

- protocol_version 为「1.0」，没有 supported_versions，因此只提供 1.0 一个版本。
- organization：名称为「Example Company」，域名为「example.com」，以及一个 logo_uri。
- auth 未指定 issuer，scopes 是一个含四个条目的对象（orders:read、orders:write、addresses 和 poppy:browser-sign-in），scope_hints 为前三个定级。
- agent 含一个协议条目，type 为「poppy」，指向一个 HTTPS 会话端点。
- web 带一个 browser_session_endpoint，tasks 带一个端点，apis 有两个条目，一个 openapi、一个 mcp，各带一个 url。
- 完全没有 extensions 条目，字段表允许如此。

这就是下文验证器运行所用的文档，2026 年 11 月 15 日从规范页面复制。

## 验证器不是网页

两篇上线帖子都指向一个验证器，读者有理由期待网站上的一个表单：粘贴域名，得到一个评分。工具包提供的并不是这个。personalagentprotocol.org 上没有验证器页面或表单。验证器是公司实施工具包里的一个命令行程序，位于 GitHub 上工具包 skill 文件夹中的 validate/index.ts。其 README 称之为「Poppy 企业验证器（Poppy Company validator）」。它需要 Node 22.18 或更高版本，没有依赖，也没有安装步骤，作用相当于一个测试用个人智能体，对企业的线上部署进行测试。

按 README 的说法，它的命令有：survey <url> 是只读的，报告某个域已经发布的内容，只发送 GET 请求。check [url] 运行各项检查并把结果写入 .poppy/last-results.json。keygen 创建测试用个人智能体身份，包括一个 README 说绝不要托管或提交的私钥文件，以及由测试者托管在公开 HTTPS 地址的 agent.json 和 jwks.json 文件。report 根据最新结果起草一份实施报告。退出码：没有 MUST 检查失败时为 0，有一项失败时为 1，用法错误时为 2。未满足的 SHOULD 只是警告，不改变退出码。

它检查的内容按工具包的四个里程碑分组，每项检查都引用它所测试的要求：

- 里程碑 1，基础（Foundation）：discovery（poppy.json 本身）、metadata（签发方，来自受保护资源元数据及其 OAuth 服务器元数据）、session（资源处的 Session 头）和 assertion（令牌端点处的客户端断言）。
- 里程碑 2，接口（Interfaces）：OpenAPI 文档、MCP 服务器、会话端点、任务端点、反馈端点和浏览器会话端点。
- 里程碑 3，登录（Sign-in）：只检查不需要真实登录的部分，例如令牌端点处一个未知的 sign_in_id。README 说明登录的其余部分要对照工具包清单人工检查。
- 里程碑 4，扩展（Extensions）：只检查一次未声明任何扩展的运行所能看到的内容，即任何会话响应中都没有扩展内容（包括 operations）。

安全限制也印在同一份 README 里。验证器绝不调用除 probe 选项所指定 GET 之外的任何 API 操作，绝不获取令牌，绝不替任何人登录，也绝不让浏览器加入会话。每个 URL 都必须是 HTTPS，一次运行最多发出 400 个请求，会话测试只携带文本「Validator test message. Please ignore.」。README 指出它也能对生产环境运行，但它会启动真实会话并发送测试消息，因此更推荐测试环境。

## 本站实际做的那次运行

2026 年 11 月 15 日，本站从工具包的 GitHub 仓库克隆了它，并用验证器的离线模式 check --file，对上文复制的规范自带 Example Company 文档运行。离线模式按 schema 和字段规则检查本地 poppy.json，不发出网络请求。

结果，基础里程碑：7 项通过，0 项失败，0 项警告，7 项跳过。通过的检查包括：文档是 JSON 对象、其字段具有第 3.1 节描述的形式、协议版本与该验证器所检查的版本一致、agent、apis 或 web 至少存在其一，以及登录与浏览的一致性检查。跳过的 7 项是网络相关检查：在 well-known 路径上的 HTTPS 提供、重定向行为、supported_versions 文档，以及 organization.domain 是否与提供该文件的主机一致。离线时没有主机，验证器会如实说明，而不是猜测。

实地笔记

这次通过证明的东西比看上去要少，本文也不把它说得更大。它表明规范自带的示例是按工具包 schema 所强制要求的形式写的，而这并非理所当然：文件用 endpoint 表示 agent 协议、用 url 表示 API，scopes 用对象，scope_hints 也用对象。其中任何一项写成另一种形式都会通不过 schema 检查。

它并不表明任何真实企业的部署能够通过，因为这次运行没有检查任何真实企业的文件。完整的 check 模式需要线上部署和托管的测试智能体身份，而协议自家的演示地址没给本站任何可测的东西：2026 年 11 月 15 日，演示智能体站点、其 /.well-known/poppy.json 以及协议检查器站点都返回 Not Found。

注意

11 月 15 日的检索中出现了一些自称 Poppy 验证器的第三方网页。它们不是工具包的验证器，规范和工具包页面都没有链接到它们，本站也没有使用它们。企业在检查自家文件时，应运行工具包仓库中的程序，在测试环境中进行，并在执行 keygen 步骤之前（而不是之后）阅读 README 中关于密钥处理的说明。

## 分阶段采用：网站先行，登录最后

面向企业的指南页面用一句话排出工作顺序：每项能力都是单独的选择，所以先做网站，然后根据需要加上智能体、API 和登录。工具包把同样的顺序变成四个里程碑，并告诉实施者在每完成一个之后运行验证器，因为它会检查该里程碑的要求并列出缺失项。

1. 基础（Foundation）。发布一份 poppy.json，列出网站和企业已有的任何 API。发布 OAuth 服务器元数据。验证资源处的 Session 头。
2. 接口（Interfaces）。接上现有接口：OpenAPI、MCP、会话、任务、反馈和浏览器会话。测试它们。
3. 登录（Sign-in）。中介登录（Mediated Sign-In）、带 PKCE 的授权码、直接登录（Direct Sign-In）和设备登录（Device Sign-In）。测试登录。
4. 扩展（Extensions）。UCP 结账、operations、links、disclosures 和浏览器控制。测试扩展。

这个顺序对 Muse 用户有实际影响。企业能交付的第一个阶段，就是一份指向其普通网站的文件，没有登录也没有 API。这也是智能体除了浏览之外几乎无事可做的阶段。合作伙伴数量——包括 Sierra 帖子里的 100 多家——并不能说明任何具名公司达到了哪个里程碑，两篇上线帖子也都没有按阶段拆分这个数字。

## 登录与会话，按文件所声明的

登录是 OAuth 2.0。企业若有现成的 OAuth 服务器就用它，规范说没有的企业可以使用工具包 skill 中的服务器。个人智能体使用带 PKCE 的授权码流程，请求 auth.scopes 中列出的作用域，并在企业自己的页面上让用户登录。直接登录（Direct Sign-In）是用户在浏览器中批准访问。设备登录（Device Sign-In）是智能体展示给用户的一个链接和一个验证码，用于在任何设备上登录。中介登录（Mediated Sign-In）是一种第一方应用流程，已被标记为即将退役：扩展页面称它将于 2027 年 3 月 17 日停止工作，路线图也列了移除它。

与登录分开，每个请求都携带一个会话。会话是一个签名 JWT，放在 Poppy-Session 头中发送，包含会话名称和一个在各企业各不相同的用户 ID，用短期密钥签名。ES256 是基线签名算法，推荐 PS384，客户端断言必须在签发后最多五分钟内过期。规范第 11 节以一句话开启其安全部分，这句话企业应当在为这份文件庆贺之前先读一读：企业不得信任个人智能体。它应当转而验证会话并检查作用域。

## 文件可以声明的扩展

1.0 随附发布了六个扩展，每个都有自己的页面，企业在 poppy.json 的 extensions 下列出它支持的那些。

- ucp：通过通用商务协议（Universal Commerce Protocol）结账。企业声明一个结账端点，智能体发送结账请求，企业返回一个结账 URL。扩展页面用一句话说明边界：UCP 是用于结账的协议，不是支付方式，企业必须支持 UCP 结账才能使用它。
- operations：企业暴露具名操作，例如下单的方式，每项含名称、描述和参数。
- links：企业向智能体提供链接，每项含 url 和可选 title。
- disclosures：企业向智能体披露信息，例如其服务条款，作为含 url 和 title 的条目。
- browser-control：智能体可以请求浏览器做事，例如点击按钮或填写表单。
- mediated-sign-in：企业可以要求用户通过中介登录登录。按其自身页面，2027 年 3 月 17 日退役。

路线图补充了 1.0 没有的东西：签名批准、自托管的个人智能体、在退役日期之后移除中介登录，以及支付。支付在协议自家文档中仍是路线图话题，这一点可用于检验任何声称 Poppy 1.0 已解决智能体支付方式的说法。

## 11 月 13 日以来的跟进：没有以自家名义发布的新内容

本站于 2026 年 11 月 15 日用 DuckDuckGo 核查了上线时留下的三项跟进。除 Muse 博客文章之外的 Meta 一手资料：没有找到。针对 Meta 自家域名的搜索没有返回 Poppy 页面，更广的结果是 Sierra 的帖子和二手报道。在 Muse 应用内目睹 Poppy 行为：没有找到。没有出现截图、用户报告或应用界面证据。Gate.com 上有一条 11 月 15 日的结果重复了「Muse 默认查找 Poppy」的说法，但打开后落在一个合规页面上，因此这里只作为未经核实的片段记录，仅此而已。合作伙伴以自家名义发布的公告：自 11 月 13 日以来，Mercury、Synchrony、Turkish Airlines 和 Shopify 都没有找到。Poppy 的「已上线」一栏仍然只靠 Sierra 的帖子和 Muse 的帖子，两者日期都是 11 月 13 日，第 1 部分均已全文阅读。

有三项常设事项与本文并列保持原状。按 Skift 11 月 9 日的记录，Muse 中的 Expedia 仍只有酒店，机票未获证实。Spaces 分享仍未上线：Meta 在 11 月 6 日称正在探索分享方式。本站 11 月 14 日发布的「Muse 给商家打电话」是付费且仅限美国。企业网站上有一份 poppy.json，今天对 Muse 用户来说不会改变其中任何一行，因为核查过的资料都没有展示 Muse 找到一份 poppy.json 时用户会看到什么。

## 留给读者的问题

如果你使用的一家企业明天发布了一份 poppy.json，应该允许 Muse 用它做什么：浏览、预订，还是购买？又有哪些事它绝不该不问就做？这份文件本身就迫使企业回答这个问题的一个版本，就在 auth.scope_hints 中——在那里 orders:write 必须被定级为不可撤销的变更。针对某一类具名企业、说清动作与界限的答案，对 11 月 23 日复检的影响会比又一个合作伙伴数字更大。

## 快速回答

poppy.json 放在哪里？

在 `https://<domain>/.well-known/poppy.json`，以 application/json 通过 HTTPS 提供。规范第 3 节：如果企业没有 poppy.json，它就不属于该协议。

哪些 poppy.json 字段是必填的？

两个：按第 3.1 节字段表，是 protocol_version 和 organization。企业还必须至少列出 agent、apis 或 web 之一。表中其余字段都是可选的，但 auth.issuer 例外——当该域的受保护资源元数据列出多个授权服务器时它是必填的。

最小的可用 poppy.json 是什么？

只含 protocol_version、organization 和 web 的那一种。指南把只有 web 的文件称为网站已支持登录的企业最省事的路径，个人智能体将会使用网站，而不是 API。

Poppy 验证器是一个网站吗？

不是。它是 GitHub 上公司实施工具包里的一个命令行程序，需用 Node 22.18 或更高版本运行。它的命令是 survey、check、keygen 和 report，并按四个里程碑组检查部署：基础、接口、登录和扩展。

规范自带的示例通过验证器了吗？

通过了，在本站 2026 年 11 月 15 日做的离线运行中：基础检查 7 项通过、0 项失败、7 项跳过。跳过的检查需要真实主机。本文没有验证任何真实企业部署，协议演示站点在同一天返回 Not Found。

有 poppy.json 是否意味着 Muse 能在该企业购物？

不能。文件声明的是渠道和作用域。结账只通过 UCP 扩展存在，企业必须支持并声明该扩展，而协议自家的路线图仍把支付列为未决话题。

有任何 Poppy 合作伙伴以自家名义发布 1.0 吗？

在 2026 年 11 月 15 日的核查中没有。没有找到 Mercury、Synchrony、Turkish Airlines 或 Shopify 以自家名义发布的公告。Synchrony 自家的 Poppy 条目出自 2026 年 10 月，早于 1.0 发布。

## 常见问题

**Q：poppy.json 由谁发布，Sierra、Meta，还是企业自己？**

A：企业自己，在自己的域名上。Poppy 是 Sierra 的个人智能体协议（Personal Agent Protocol），与包括 Meta 在内的行业伙伴一同发布。Muse 的帖子（第 1 部分已全文阅读）从企业一侧描述了同一份文件：企业发布 poppy.json，告诉个人智能体它提供什么、如何到达它。实施工具包是给企业用的，工具包页面指出面向个人智能体的工具包尚未发布。

**Q：在没有 poppy.json 的网站上会发生什么？**

A：按规范的措辞，那家企业不属于该协议，个人智能体不得假定那里有任何服务、端点或方法。Sierra 的上线帖子说 Muse 访问每个网站时都会先查找 Poppy。Muse 在没有该文件的网站上接着做什么，两篇上线帖子都没有描述，截至 2026 年 11 月 15 日也没有找到任何应用内的目击证据。

**Q：为什么 auth.scopes 用描述而不是普通列表？**

A：因为第 3.1 节定义的就是这种形式：以作用域名称为键的作用域描述，与 OpenAPI OAuth 2.0 安全方案的形式相同。验证器的 schema 检查强制执行这一形式。企业还有第二种列出作用域的方式，即在其受保护资源元数据或签发方元数据的 scopes_supported 中，智能体使用这些列表的并集。

**Q：验证器不检查什么？**

A：它自己的 README 印有两条限制。登录只在不需要真实登录的地方检查，其余部分对照工具包清单人工检查。扩展只从外部检查，即一次声明无扩展的运行所能看到的范围。它按设计也绝不获取令牌、绝不替任何人登录、绝不让浏览器加入会话。

**Q：本站能替我对一家具名公司运行验证器吗？**

A：survey 命令是只读的，只发送 GET 请求，所以是对线上域名运行起来安全的那个。本文没有做线上检查，因为 11 月 23 日的复检是首次具名检查的既定日期。完整的 check 模式会启动真实会话并发送测试消息，README 更希望它在测试环境中使用，所以它不是那种可以指向一家没有要求测试的公司的工具。

**Q：poppy.json 与 Muse 连接器是一回事吗？**

A：不是，第 1 部分依据 Muse 自己的文字把两者区分开了。连接器把某个特定服务接入 Muse，需经 Meta 对已验证连接器的审核。poppy.json 是任何企业在自己网站上按开放协议发布的文件，规范和工具包都没有提到 Meta 审核。企业可以两者都做、只做其中之一，或都不做。

**Q：本站何时再核查 Poppy？**

A：2026 年 11 月 23 日，针对台账上两项未决事项：在 Muse 内目睹 Poppy 行为，以及合作伙伴以自家名义发布公告。同一次核查还会对本站能说出的首个真实企业 poppy.json 运行验证器的 survey 命令，并无论结果如何都按该日期发布。

## 资料来源

- 个人智能体协议规范 1.0 版，personalagentprotocol.org/docs/1.0/spec。2026 年 11 月 15 日全文阅读。第 3 节：poppy.json 位于 /.well-known/poppy.json，通过 HTTPS 提供，没有文件即不属于该协议，只能依赖文档所声明的内容，通过 RFC 9728 受保护资源元数据和 RFC 8414 签发方元数据发现。第 3.1 节字段表：protocol_version 与 organization 必填，agent、apis 或 web 至少其一，auth.issuer 有条件必填，以及本文列出的可选字段与形式，包括以作用域名称为键的描述式 scopes 和含 changes 与 personal_data 的 scope_hints。第 3.3 节：extensions 以名称为键，每个版本一个条目。第 3.4 节：supported_versions 是指向各版本文档的映射，位于同一主机、具有相同域名与签发方。第 3 节中完整的 Example Company 文档，用于验证器运行。第 4 至 6 节与第 11 节如文中引用：带 PKCE 的 OAuth 2.0、Poppy-Session JWT 头、ES256 基线且推荐 PS384，以及企业不得信任个人智能体的要求。
- 个人智能体协议指南 personalagentprotocol.org/docs/1.0/guides，以及公司实施工具包 personalagentprotocol.org/kit/company。2026 年 11 月 15 日阅读。指南：每项能力都是单独的选择，先做网站，再加入智能体、API 和登录；网站已支持登录时，只有 web 的 poppy.json 是最省事的路径。工具包：四个里程碑（基础、接口、登录、扩展），每完成一个里程碑运行一次验证器，面向个人智能体的工具包尚未发布。
- Poppy 企业验证器，README 与程序，github.com/personal-agent-protocol/personal-agent-protocol，skills/implement-personal-agent-protocol/validate。2026 年 11 月 15 日阅读并运行。README：命令 survey、check、keygen 和 report；检查按里程碑分组，如本文所列；退出码 0、1、2；Node 22.18 或更高，无依赖；安全限制包括不获取令牌、不登录、不加入浏览器、最多 400 个请求，以及偏好测试环境。本站运行，2026 年 11 月 15 日：以离线 --file 模式对规范的 Example Company 文档运行 check，基础结果 7 项通过、0 项失败、0 项警告、7 项跳过，跳过的是网络相关检查。
- 个人智能体协议扩展页面与路线图，personalagentprotocol.org/docs/1.0/extensions 与 /docs/roadmap。2026 年 11 月 15 日阅读。1.0 的六个扩展：ucp、operations、links、disclosures、browser-control 和 mediated-sign-in。UCP 页面：UCP 是用于结账的协议，不是支付方式。中介登录页面：即将退役，2027 年 3 月 17 日停止工作。路线图：签名批准、自托管个人智能体、移除中介登录，以及支付。
- Sierra，「发布 Personal Agent Protocol 1.0」（"Releasing Personal Agent Protocol 1.0"），2026 年 11 月 13 日，作者 Bret Taylor 与 Clay Bavor。2026 年 11 月 15 日再次全文阅读。仅为本文的起点：Poppy 现已向所有使用 Muse 的用户开放、Muse 优先查找 Poppy、Shopify 已为每个商家启用、Mercury、Synchrony 和 Turkish Airlines 即将上线、设计合作伙伴超过 100 家，以及一个带验证器的实施工具包位于 personalagentprotocol.org。
- Muse 博客，「Muse 与商家合作的更多方式」（"More Ways for Muse to Work With Businesses"），muse.ai/blog/poppy-personal-agent-protocol。2026 年 11 月 14 日为第 1 部分全文阅读，此处按同等权重沿用；2026 年 11 月 15 日重新抓取未返回该页面。Muse 是首个支持 Poppy 的个人智能体，poppy.json 被指为企业发布的那份文件，无需客户登录的纯网站设置，在企业自己的页面上进行 OAuth 授权与撤销，以及 Meta 已验证连接器作为单独的审核轨道。
- DuckDuckGo 核查，2026 年 11 月 15 日，为本文进行。查询了 Muse 博客文章之外的 Meta 一手资料、应用内目击 Poppy 行为，以及 Mercury、Synchrony、Turkish Airlines 和 Shopify 以自家名义发布的公告，另外还搜索了工具包和验证器的站点。三项跟进事项均未找到。协议演示地址（演示智能体站点、其 /.well-known/poppy.json 和协议检查器）在 2026 年 11 月 15 日返回 Not Found。Gate.com 上一条 11 月 15 日的结果打开后止于一个合规页面，仅作为未经核实的片段记录。
- 基线核查：本站 2026 年 9 月的研究文件不含 Poppy 材料，因为该协议于 2026 年 10 月才首次公布。本文没有任何内容依赖该基线文件。
- 编辑核查，2026 年 11 月 15 日：常设事实按本站 11 月记录保持不变。按 Skift 11 月 9 日，Muse 中的 Expedia 仅有酒店，机票未获证实。Meta 11 月 6 日称 Spaces 分享正在探索分享方式，尚未上线。按本站 11 月 14 日帖子，Muse 给商家打电话是付费且仅限美国。
