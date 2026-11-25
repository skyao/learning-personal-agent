---
title: "你把陌生人的技能文件粘贴进了 Muse，它能读到你的智能体能读的一切"
linkTitle: "粘贴技能文件的风险"
date: 2026-11-12
originalTitle: "You Pasted a Stranger's Skill File Into Muse. It Can Read Everything Your Agent Can."
sourceUrl: "https://aihomebuilding.com/stories/muse-pasted-skill-trust-gap-2026"
author: "Catherine Chen"
publisher: "aihomebuilding"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-25
tags: [安全]
products: [muse]
dateNote: "回填：发表于 2026-11-12，此前漏收"
---

{{< source-info >}}

**收录说明**：直接下载（article.article-body 容器；回填）。

**内容摘要**：文章起因是今年秋天 X 上的一篇帖子，号召 Muse 用户收藏十个营销类技能文件，每个文件复制粘贴进对话即可使用，而帖子没有说明这些文件粘贴后能做什么。Muse 于 2026 年 9 月 8 日上线，Meta 于 9 月 29 日首次在发布标题中提到技能，宣布在 Muse for Small Business 中新增一批技能与连接器；按 Meta 的界定，技能是完成某类任务的指令，连接器是经用户授权的、与外部应用的带权限链接，两者是不同层面。消费版 Muse 应用中没有安装自有技能的按钮，2026 年 10 月的独立测试确认了这一缺口，实际通行的做法是把整个 SKILL.md 文件粘贴进对话、仅在该对话中生效，唯一有记录的例外是开发者智能体 Muse Code 可原生读取标准 SKILL.md 文件。2026 年 1 月 27 日至 2 月初，攻击者向 OpenClaw 的公开市场 ClawHub 上传了大量投毒技能：VirusTotal 分析了 3,016 多个技能，发现数百个有恶意特征，其中 314 个与同一 ClawHub 用户有关；Koi Security 审计 2,857 个技能，发现 341 个恶意，其中 335 个属于其命名为 ClawHavoc 的同一协同行动；到 2 月 16 日，Koi 的计数升至 824 个，同期注册技能总数超过 10,700 个；VirusTotal 2 月 5 日的第二份报告记录了五种不同手法，包括 Better-polymarket 内嵌的 bash 反向 shell、Wake-up 语义蠕虫、Evilweather 注入 SSH 密钥、Rankaj 窃取智能体环境文件内容，以及被称为“认知 rootkit”的 Devinism。2026 年 5 月，Palo Alto Networks Unit 42 报告的两个技能把智能体引向托管窃密命令的粘贴站点，ClawHub 的自动审计却给出了 Pass 或无结论，说明只读技能文件的扫描存在盲区；安全研究员 Simon Willison 提出的模式指出，同时具备私有数据访问、不可信内容接触与外泄渠道的智能体即暴露，而 Muse 按设计三者俱全。作者同时写明，公开记录中没有已证实的粘贴 SKILL.md 文件导致 Muse 用户受损的案例，审批缺口的论述是对 Meta 已公布政策与已有外泄手法的分析，并非针对真实 Muse 智能体的实测漏洞；文末给出五条做法，包括粘贴前通读文件、拒绝会取 URL、跑脚本或读文件的技能、粘贴进无多余连接的新对话、事后查活动日志、优先使用内置技能与 Goals。

**保留理由**：把 Muse 技能粘贴做法与 ClawHub 2026 年 2 月的投毒事件、5 月的漏网案例并置，说明了“审批只守发送、发布与花钱三道门、而外泄可借已批准的能力走出去”这一缺口，是已收资料中对 Muse 技能安全边界最系统的社区分析；作者同时明确区分了机制可迁移与事件本身发生在其他智能体上。
