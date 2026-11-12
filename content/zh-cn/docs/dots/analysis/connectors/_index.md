---
title: "OpenAI Dots：连接器"
linkTitle: "连接器"
weight: 40
analyzedAt: 2026-11-12
sourcesUntil: 2026-11-11
description: >
  dots 复用 ChatGPT 的插件生态（官方称 4,000 多个应用），另有云端浏览器和本地电脑两条操作路径；授权分插件、应用权限和源服务三层，断开连接后 dot 已获得的信息仍保留。
---

## 概要

- 连接应用的主要机制是 ChatGPT 的插件生态，官方称可连接 4,000 多个应用；插件权限在 dots、ChatGPT、ChatGPT Work、Codex 之间共享。
- 插件之外，dot 还可以用云端浏览器登录网站操作，或通过已连接的电脑使用本地文件、应用和浏览器。浏览器路径会绕过插件的只读限制，官方提醒两边的账户权限都要检查。
- 实测中常见 SaaS（Gmail、Slack、日历、Figma 等）基本可用；非 Gmail 邮箱和自定义 MCP 摩擦较大，本地 MCP 进程无法在云端运行。
- 平台拦截已经出现：据 36 氪转述 The Verge，Dots 也无法访问亚马逊；国内电商中淘宝被云端浏览器访问限制拦住。
- 资料中没有 dots 专属的第三方开发者接入方式或应用商店规则。

## 插件、浏览器、本地电脑三条路径

| 路径 | 说明 | 资料 |
| --- | --- | --- |
| 插件（应用连接） | 使用为用户账户安装并启用的受支持插件，如 Gmail 找邮件、Google Drive 读写文档、GitHub 调查问题并准备 PR；权限在 ChatGPT「插件」标签页统一管理 | [文档：连接计算机和应用]({{< relref "/docs/dots/sources/official/2026-11-05-docs-computers-and-apps" >}})、[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}}) |
| 云端浏览器 | 在 dot 的云端浏览器中登录网站操作，可使用已登录的会话 | [文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}}) |
| 已连接的电脑 | 本地文件、命令、桌面应用；云端浏览器被拦截时改用本地浏览器；本地技能需要已连接电脑 | [帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}}) |

消息渠道（Slack、Teams、短信）与应用连接相互独立，连接渠道不会授予收件箱或电脑访问，详见[交互渠道]({{< relref "/docs/dots/analysis/channels" >}})。已连接的服务支持时，可以让 dot 对特定事件作出响应（例如 Slack 频道里出现新的错误报告），但仅仅连接来源不会自动开始监控（[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})）。

「4,000 多个应用」出自发布稿（[推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}})），媒体普遍照引。Cyera 让 dot 自列可用工具，得到约 270 项，其中 GitHub 一组接近 90 个（含合并 PR、开启自动合并），还有 Slack 发消息、搜索公开与私有频道等工具（[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})）。两个数字的口径不同：前者是可连接的应用，后者是某个用户已连接应用暴露的工具。

## 实测：常见 SaaS 顺利，非标准接入费力

Slide Factory 的第一天实测（2026-10-03）最详细（[Slide Factory 第一天]({{< relref "/docs/dots/sources/community/2026-10-03-slidefactory-dots-first-day" >}})）：

- Slack 和日历可读，dot 从中发现了预算外的讨论和会议冲突；但给同事发 Slack 私信失败，改发到群组才成功，作者评价「宣布比证据来得更早」。
- 作者用 Zoho 邮箱加 Apple Mail 和 Outlook，dot 误以为对方用 Gmail，设置失败并给出三个格式错误的链接，邮件和改期未完成。
- 完成 Google 登录和设备批准后，dot 能通过浏览器访问客户的 GA4 与 Search Console，但浏览器登录没有把 Google API 连接到另一个 SEO 服务。
- 自定义 MCP：本地 Node 进程在云端跑不了，需改用托管端点；配置要在桌面端 MCP 设置和网页端插件设置之间来回切换；服务器新增工具后，要重装插件才能看到。接入后完成了 44 页与 111 页的抓取。
- 作者的结论是常见 SaaS 应用阻力较小，非 Gmail 邮箱和自定义 MCP 占去了大半个下午。

其他实测：Pat Simmons 报告 Dots 可以切换到 Codex Chrome 扩展、使用用户自己的 Chrome 进入 Amazon；在 FlightHub 的机器人检查上 Muse 和 Dots 都被拦，Grok Bot 通过（[Pat Simmons]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})）。Claire Vo 的九项任务中，Dot 借助 Slack 和 Figma 连接完成回复和缩略图任务（[ChatPRD 九项任务]({{< relref "/docs/industry/sources/community/2026-10-29-chatprd-four-agents-nine-tasks" >}})）。

## 平台拦截

据 36 氪转述 The Verge，亚马逊以「持续访问」违反网站政策为由抵制 Muse，xAI 的 Grok、Instinct 和 OpenAI 的 Dots 也无法访问亚马逊（[36 氪]({{< relref "/docs/industry/sources/media/2026-10-21-36kr-agents-blocked" >}})）。这与 Pat Simmons 通过本地 Chrome 进入 Amazon 的报告不矛盾：前者应指云端浏览器，后者走的是用户本地浏览器，但资料没有明确区分。

国内场景中，一位用户 11 天实测发现京东价格可以持续监控，淘宝在云端浏览器里被访问限制拦住，拼多多没有网页端；作者认为 Dots 在国内「水土不服」，因为最多的上下文在微信里（[靖轩：深度体验 11 天]({{< relref "/docs/industry/sources/community/2026-10-10-jingxuan-dots-11-days" >}})）。另一篇评论的说法是「Agent 能做什么，最终取决于平台愿不愿意开门」（[奈氏：到底能干什么]({{< relref "/docs/industry/sources/community/2026-10-15-naishi-what-can-it-do" >}})）。

资料中没有 OpenAI 对被拦截的回应，也没有 OpenAI 与电商、旅行等平台达成合作的报道。

## 生态：沿用 ChatGPT 插件，取向偏工作

官方资料对第三方的开放只写到「插件生态」和现有 ChatGPT 插件权限，企业通过「插件控制」管理可用的应用和操作（[管理员指南]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-admin-guide" >}})），没有 dots 专属的开发者接入或审核规则。第三方对比把 Dots 归为偏工作工具（Codex、Slack、发票和文档）的一类，与偏个人杂事和购物的 Muse 相对（[入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})）；也有综述指出 Dots 的文档没有提到 webhook 触发，新的 GitHub issue 不会立刻唤醒 dot，对事件驱动的开发者场景是缺口（[主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})）。

推断：OpenAI 没有为 dots 另建连接器体系，而是把 ChatGPT 已有的插件、Codex 的本地能力和 Work 的云端浏览器拼在一起。这让 dots 发布时就有较大的覆盖面，但连接器的质量和授权逻辑继承自各个产品，用户需要在多个设置页之间管理。

## 授权的三层与断开后的残留

官方把对 dot 的限制分为三层：插件控制（哪些应用和操作可用）、应用权限（何时需要批准）、各服务自身的授权（[帮助中心：工作区管理]({{< relref "/docs/dots/sources/official/2026-11-05-help-manage-dots-in-workspaces" >}})）。读取权限不等于发送权限，「仅仅启用这个应用，并不等于授权发送」（[管理员指南]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-admin-guide" >}})）。但只读插件只限制通过该插件做的事；开启云端浏览器后，dot 仍可能通过网站上登录的账户修改内容，官方提醒两个账户的权限都要检查（[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})）。自定义规则可以要求确认或阻止某些操作，但不能授予访问，也不能凌驾于内置安全要求（[文档：控制你的 dot]({{< relref "/docs/dots/sources/official/2026-11-05-docs-controls" >}})）。

连接过期时，dot 会请用户重新连接。断开插件只停止新的信息共享，dot 已了解的信息保留在它的上下文中，只有删除或重置 dot 才能清除（[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})）。Slack 的情况更复杂：关闭 dot 的 Slack 身份不会移除它通过所有者 Slack 插件获得的访问，离职交接时两处都要检查。Cyera 据此建议把 dot 当作「特权内部身份」管理：少连应用、用完撤销、限定频道范围、给仓库设分支保护（[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})）。

## 资料缺口

- 4,000 多个应用的清单，以及哪些支持写入操作。
- 第三方开发者为 dots 发布插件的方式、审核与分成规则。
- 自定义 MCP 的官方接入说明（目前只有 Slide Factory 一例实测）。
- OpenAI 对亚马逊等平台拦截的回应或合作进展。
- 连接器令牌的有效期、「连接过期」的触发条件，授权粒度是否细到文件夹或频道。

## 主要资料

- 官方：[文档：连接计算机和应用]({{< relref "/docs/dots/sources/official/2026-11-05-docs-computers-and-apps" >}})（三条路径）；[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})（浏览器与插件权限）；[帮助中心：工作区管理]({{< relref "/docs/dots/sources/official/2026-11-05-help-manage-dots-in-workspaces" >}})（三层授权）；[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})（断开后的残留）。
- 媒体：[36 氪]({{< relref "/docs/industry/sources/media/2026-10-21-36kr-agents-blocked" >}})（亚马逊拦截）。
- 社区：[Slide Factory 第一天]({{< relref "/docs/dots/sources/community/2026-10-03-slidefactory-dots-first-day" >}})（接入实测）；[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})（工具清单与授权风险）；[靖轩：深度体验 11 天]({{< relref "/docs/industry/sources/community/2026-10-10-jingxuan-dots-11-days" >}})（国内平台）；[Pat Simmons]({{< relref "/docs/industry/sources/community/2026-10-06-pat-simmons-grok-muse-dots" >}})（本地 Chrome 访问亚马逊）。
