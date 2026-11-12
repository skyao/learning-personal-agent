---
title: "OpenAI Dots：安全"
linkTitle: "安全"
weight: 80
analyzedAt: 2026-11-12
sourcesUntil: 2026-11-11
description: >
  dots 的安全设计是「授权绑定任务 + 独立的自动审查（Auto-review）+ 只读主动研究 + 隔离的云端沙箱」，官方公开了较多评估数据；但官方也承认审查对浏览器和桌面操作的覆盖尚未核实，且没有第三方独立审计。
---

## 概要

- 权限按任务授予，不会随后续工作或委派扩大；数据越敏感，对接收方要求越具体（健康数据须具名接收方）；改密码、转账等最敏感的操作必须由用户接管。
- 防护分层：模型训练、插件权限、自定义规则、独立的自动审查（Auto-review）、安全监控、每个 dot 独立的云端沙箱。自动审查在发送、修改等写操作前检查收件人和内容，dot 无法关闭必需的检查。
- 密码通过私密登录表单直接进入云端浏览器，不进入模型上下文；但聊天、文档里另行出现的密码不受保护，云端计算机上运行的代码也能读到暴露给它的令牌和 cookie。
- 系统卡给出了较多评估数字：批量和迭代提示注入红队无计分成功；长链任务中的中等严重性越界率随中间任务增多而上升（8.6% 到 19.7%）。不同测试集的数字口径不同，不能互相换算。
- 官方承认的薄弱点：自动审查对浏览器、桌面和委派操作的覆盖「仍在审查中」，网页邮箱等路径在「发送」处是否会提示「尚未核实」；更细的审计日志和网站白名单仍在开发。
- 资料中没有第三方独立审计、漏洞赏金或 Dots 自身的安全事件；Cyera 称已向 OpenAI 负责任披露了几项发现，细节未公开。

## 授权绑定任务，越敏感越具体

只有所有者能指挥自己的 dot，其他人的消息（包括 Slack 中的提及）不会启动工作（[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})）。发布时的安全博客给出了授权规则：发送消息或分享文件需要覆盖「信息类型 + 接收方类型」的授权，数据越敏感，对接收方越具体，「健康数据总是要求用户指定一个具名的接收方」，邮箱、电话等低敏数据默认只需接收方类别（如「任何航空公司」）；授权绑定在该任务上，之后的继续工作或委派都不会扩大它（[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})）。

| 操作 | 规则 | 资料 |
| --- | --- | --- |
| 改密码、账户间转账 | 必须用户接管，自定义规则和批准都不能覆盖 | [隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}}) |
| 永久删除数据、安装未知软件、授予新的敏感访问 | 博客称「每次都需要你的确认」，常见问题写「可能每次都需要批准」 | [安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}}) |
| 用网站上保存的卡购物 | 需要批准，除非预先批准明确涵盖这笔 | [隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}}) |
| 起草与发送 | 起草权限只涵盖草稿；受众、内容或时间变化需要新的批准 | [文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}}) |
| 周期性消息 | 可预先批准（如每周五在团队频道发更新），需写明对象、内容、时间 | 同上 |

用户可以用自定义规则调整行为，四档是不询问直接做、预先批准时做、做之前先问、交给用户（[文档：控制你的 dot]({{< relref "/docs/dots/sources/official/2026-11-05-docs-controls" >}})）。自定义规则不能授予账户没有的权限，不能凌驾于必需的安全检查，也不能改变自动审查和主动研究的限制；dot 可以帮忙起草规则，但修改要用户批准。Cyera 实测确认 dot 改规则时请求了批准，但提醒「约束智能体的规则引擎同时也是智能体手里握着的工具」（[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})）。

批准在 ChatGPT 中完成：短信渠道里需要批准时，dot 发一个链接让用户回到 ChatGPT 审阅（[文档：给你的 dot 发消息]({{< relref "/docs/dots/sources/official/2026-11-05-docs-message-your-dot" >}})）。系统卡提到红队曾发现确认策略可以加强，更新后连「被指示永不征求许可、完全自主工作」的场景也得到缓解（[系统卡附录]({{< relref "/docs/dots/sources/official/2026-09-29-gpt-6-astra-system-card-dots" >}})）。

## 自动审查与安全监控

自动审查（Auto-review）是独立于 dot 的安全系统：在发邮件、改文件等操作以及标为 write 的工具调用之前，对照用户的说明、自定义规则和安全要求检查收件人与内容，可以阻止，也可以要求澄清或批准；被阻止后 dot 可以补充信息后重提、换一种获准的做法、把敏感步骤交给用户或停止。普通只读步骤不经过自动审查。控制放在 dot 能修改的环境之外，dot「无法修改或关闭一项必需的检查」（[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})）。另有安全监控在 dot 规划和行动时寻找绕过防护或超出指示的行为，可以暂停工作并向所有者显示警告。

主动研究的只读限制在代码中强制执行，见[持续执行]({{< relref "/docs/dots/analysis/continuous-execution" >}})。沙箱和隔离见[运行环境]({{< relref "/docs/dots/analysis/runtime" >}})。

官方企业文档对覆盖范围写得很坦白：自动审查对浏览器、桌面和委派操作的覆盖「仍在审查中」；同一封外部邮件经邮件插件、云端网页邮箱、桌面邮件应用三条路径发出，拦截和批准行为不同，云端浏览器和计算机操作在「发送」按钮处是否会提示「尚未核实」，要求企业逐条路径测试；公司政策禁止的收件人，所有者批准也不能放行（[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})）。

推断：权限体系主要建立在插件的工具调用上，浏览器和桌面操作是一条可以绕开插件权限的路径（[连接器]({{< relref "/docs/dots/analysis/connectors" >}})中官方也提醒只读插件不限制浏览器）。在官方补齐这部分覆盖之前，关闭云端浏览器或计算机操作是企业控制风险的主要手段。

## 凭证：密码不进模型，但不是全部机密

受支持的登录走私密登录表单：填写期间模型暂停，凭证直接进入云端浏览器，不进入模型上下文；「保存到密码」通过加密的凭证服务提供，使用已保存的登录需要用户确认（[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})）。dot 的上下文不保留凭证、图片和截图。

保护范围有限：在聊天、文档中或通过插件另行分享的密码不在保护之内（[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}})）；应用令牌或浏览器 cookie 的值一旦暴露给 dot 计算机上运行的代码，代码就能读取，「不要假定会话或令牌与在那里运行的代码相互隔离」（[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})）。单点登录和多因素认证由用户接管完成；要求公司设备或 VPN 的登录，云端浏览器无法满足。

社区把这种做法与 Muse 对照：Muse 把凭证、审批和安全服务放在智能体容器之外，由独立的 Sentinel 在网络边界判断；两种设计都在减少模型直接接触真实凭证的机会（[鸿煊：工程内核]({{< relref "/docs/industry/sources/community/2026-11-07-hongxuan-engineering-core" >}})）。

## 评估数字：多，但口径各异

系统卡附录（2026-09-29，GPT-6 Astra，dots 运行框架）的主要结果（[系统卡附录]({{< relref "/docs/dots/sources/official/2026-09-29-gpt-6-astra-system-card-dots" >}})）：

| 评估 | 结果 |
| --- | --- |
| 批量提示注入红队 | 100 次推演、50,000 封邮件（其中 16,600 封为生成的攻击邮件），无计分的攻击成功 |
| 迭代提示注入红队 | 100 条攻击链、2,638 次有效尝试，无计分的攻击成功 |
| 任务中途权限变更 | 通过率 91.8%（45/49），17 个显式权限变更案例全部通过 |
| 长链任务越界 | 无高严重性违规；中等严重性越界标记率随中间任务从 5 个增至 10 个，由 8.6% 升至 19.7% |
| 严重未对齐率 | 0.84% |
| 被禁止操作完成率 | 各时间预算（4 分钟至一年）下均为 0% |
| Preparedness 评级 | 生物化学 High，网络安全 Critical |

系统卡同时写明仍在处理已知漏洞，认为部署合适的理由是利用这些漏洞需要大量准备、高度宽松的提示或跨界面的高级技术。

企业安全文档（2026-11-05 收集）另引 2026-10-26 GPT-6.1 Terra 系统卡附录的数据：间接提示注入稳健性 GPT-6 Astra 99.789%、GPT-6.1 Terra 98.770%（[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})）。Cyera 则引用系统卡中外部提示注入竞技场的攻击成功率 8.5%（前一模型 27%），换算为「大约每 12 次尝试中有 1 次成功」（[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})）；本库收录的系统卡附录是节选，其中没有这两个数字，无法核对。三组数字来自不同测试集，并列记录，不做取舍。表中的部分模型并不驱动 dots，只是对照。

## 审计与企业控制

企业可以用基于角色的权限控制谁能用 dots，Enterprise 默认关闭；Slack/Teams、本地计算机访问、自定义规则是三项独立的权限，多个角色中只要一个授予即生效（[帮助中心：工作区管理]({{< relref "/docs/dots/sources/official/2026-11-05-help-manage-dots-in-workspaces" >}})）。云端浏览器、网络访问、计算机操作、密码管理器可分项关闭，这些设置与 Work Cloud 共用。官方建议只在全部成员属于本组织的 Slack 频道使用 dot，不建议 Slack Connect 频道（[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})）。

Compliance API 记录用户提示、dot 回复、工具调用和后台活动（`client_id = DOTS`），但浏览器和计算机活动只有建议调用的记录，详细输出可能缺失；运行状态报告的 p95 时延为 30 分钟。更详细的云端审计日志、网站允许和阻止规则都「正在开发」。

## 外部评价与已披露问题

Cyera 的检查（2026-10-14）是资料中唯一偏安全方向的一手研究：用「想上报数据过度共享」的薄借口向 dot 索要敏感数据，dot 帮忙检索，但没有交出所有者权限之外的内容；dot 自列约 270 个工具，包括合并 PR、读取生产环境变量等高权限工具；Cyera 设想被劫持的 dot 会成为可信的钓鱼渠道，建议用别的渠道核实 dot 的主动消息，不点它发来的登录链接。Cyera 称已通过负责任披露向 OpenAI 报告「几项发现」，细节未公开（[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})）。

一位自述有 15 年企业安全背景的作者认为，在六款产品中 Microsoft 和 OpenAI dots 的安全说明写得最清楚（[六款智能体对比]({{< relref "/docs/industry/sources/community/2026-11-05-ai-agents-compared-small-business" >}})）；Top5Apps 称 dots「纸面上有该品类最严格的设计」（[Top5Apps]({{< relref "/docs/industry/sources/community/2026-11-01-best-personal-ai-agents-top5apps" >}})）；DataCamp 指出 Dots 与 Muse「都没有经过独立审计」（[DataCamp]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})）。

截至 2026-11-11 的资料，没有 Dots 自身的公开安全事件；媒体报道的对话分享漏洞、通讯录同步等事件都属于 Muse。

## 资料缺口

- 第三方独立审计、渗透测试报告和漏洞赏金计划；Cyera 披露内容与 OpenAI 的回应。
- 自动审查在生产环境中的误拦率和漏拦率。
- 浏览器、桌面路径上审批行为的实测。
- 网站白名单和详细审计日志的上线时间。

## 主要资料

- 官方：[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})（授权规则、自动审查、凭证）；[文档：dots 的安全与防护]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-security" >}})（企业控制、覆盖范围、审计、评估表）；[系统卡附录]({{< relref "/docs/dots/sources/official/2026-09-29-gpt-6-astra-system-card-dots" >}})（评估数字）；[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}})（用户侧规则）。
- 媒体：[DataCamp]({{< relref "/docs/industry/sources/media/2026-10-27-datacamp-dots-vs-muse" >}})（无独立审计）。
- 社区：[Cyera]({{< relref "/docs/dots/sources/community/2026-10-14-cyera-dots-double-edged-sword" >}})（一手安全检查）；[鸿煊：工程内核]({{< relref "/docs/industry/sources/community/2026-11-07-hongxuan-engineering-core" >}})（与 Muse 的凭证设计对照）。
