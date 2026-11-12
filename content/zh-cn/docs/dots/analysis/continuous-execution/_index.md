---
title: "OpenAI Dots：持续执行"
linkTitle: "持续执行"
weight: 30
analyzedAt: 2026-11-12
sourcesUntil: 2026-11-11
description: >
  dot 自己决定何时暂停和醒来，支持定时任务、受支持的事件监控和只读的主动研究，能把工作分给并行的后台智能体；实测显示长任务可持续数天，但定时任务漏跑、状态显示不准的情况已有报告。
---

## 概要

- dot 定位为「始终在线」：在对话之间持续工作，可以自己决定何时暂停、何时醒来，不需要为每次跟进设固定时间表；也支持指定时间的定时任务和受支持服务的事件监控。
- 主动研究是 dots 的特色机制：后台智能体只读地查看已连接来源、记私人笔记，有发现时由 dot 带来建议或问题；只读限制「在代码中强制执行」。
- 任务可以分给并行的后台智能体、云端会话线程或本地 Work/Codex 任务；暂停 dot 只停止当前主要任务，不停止委派任务，也不取消未来的计划运行。
- 主动联系的渠道是 ChatGPT、Slack、Teams 和短信（测试版）；发布时 dot 不能主动打电话。打扰频率由用户的指示控制，官方没有频率上限或免打扰机制。
- 实测中长任务可以持续数天、在被打断后回到原任务；但也有定时任务没有运行、暂停期间到期的任务未送达却标为「已完成」的报告。没有 webhook 和基于实时位置的触发。

## 自己决定何时醒来，也可以定时或按事件

官方文档写明，dot 可以同时跟踪多项职责，「可以自己决定何时暂停、何时醒来继续工作，所以你不需要把每一次跟进都放进固定的时间表」（[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})）。需要固定时间的任务，官方建议在请求中写明查什么、何时（含时区和结束日期）、哪些变化值得通知、结果送到哪里，并让 dot 确认保存了什么。事件触发只在已连接服务支持事件监控时可用（例如 Slack 频道出现新的错误报告），仅连接 Slack 或把 dot 加入频道不会建立监控。2026-10-09 那一周起，dot 还可以读取和编辑 ChatGPT Work 的自动化（[移动端创建 dot]({{< relref "/docs/dots/sources/official/2026-10-09-docs-whats-new-dots-mobile" >}})）。

任务的执行位置分四类：新的本地 Work/Codex 任务（电脑要在线并打开 ChatGPT 应用）、已有的本地 Codex 任务、新的云端编程任务（电脑可以离线）、dot 自己创建的任务。dot 可以把工作分给并行运行、向它汇报的后台智能体，用户同时继续对话（[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})）。执行环境见[运行环境]({{< relref "/docs/dots/analysis/runtime" >}})。

一篇第三方对比（作者 2026-10-31 核实）指出，OpenAI 的文档没有提到 webhook 触发，新的 GitHub issue 不会立即唤醒 dot，要等下次检查（[主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})）。《纽约时报》实测中，dot 无法根据实时位置触发动作，拒绝了「到健身房时推送训练计划」，Muse 可以（[NYT 五个杀手级任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}})）。

## 主动研究：只读，发现后再问

安全博客描述了主动研究：dot 不等新请求，读取被允许的已连接来源，为自己保存私人笔记；这些工具只读，不能发消息、修改应用内容或控制浏览器和计算机，「我们在代码中强制执行这些限制」。官方举的例子是发现旅行计划有变，或某个发布决定与上周的草稿冲突（[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})）。发现由后台智能体汇报给 dot，再由 dot「带给你一条建议或一个问题」，后续操作遵守相应的权限和批准。

发布稿的场景包括：Slack 里出现错误时立即调查；测试者的 dot 发现他忘了开发票，备好发票并在他批准后发出（[推出 dots]({{< relref "/docs/dots/sources/official/2026-09-29-introducing-dots" >}})）。CNBC 转引 OpenAI CFO Sarah Friar 的说法，dots 是「可以拍拍你肩膀」的智能体（[CNBC DevDay]({{< relref "/docs/dots/sources/media/2026-09-29-cnbc-devday-dots" >}})）。

推断：主动研究把「主动」拆成两段，读和记可以自动进行，写和发必须回到用户。这让 dots 可以默认开启后台查看，而把风险集中在批准环节（见[安全]({{< relref "/docs/dots/analysis/security" >}})）。代价是记忆在用户不知情时形成（见[记忆与上下文]({{< relref "/docs/dots/analysis/memory" >}})）。

## 暂停、停止、取消是三件事

| 操作 | 效果 | 资料 |
| --- | --- | --- |
| 暂停 dot | 停止当前主要任务；不停止每个委派任务，也不取消将来的计划运行；「继续」恢复 | [文档：控制你的 dot]({{< relref "/docs/dots/sources/official/2026-11-05-docs-controls" >}}) |
| 停止委派任务 | 在「活动」中逐个停止；停止不撤销已完成的操作 | 同上 |
| 取消周期任务 | 在「已安排」中禁用或删除 | 同上 |
| 结束对话或通话 | 不一定停止已分配的工作 | [文档：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-docs-getting-started" >}}) |
| 安全监控介入 | 可暂停或停止进行中的工作并显示警告 | [安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}}) |
| 管理员暂停 | 成员不能自行恢复，暂停期间停止计费 | [管理员指南]({{< relref "/docs/dots/sources/official/2026-11-05-docs-dots-admin-guide" >}}) |

官方提醒「一次运行完成，本身并不能确认所请求的结果已经实现或交付」，要检查输出和报告的错误（[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})）。帮助中心对暂停的描述更宽，写成让 dot 停下直到恢复（[帮助中心：开始使用]({{< relref "/docs/dots/sources/official/2026-11-05-help-getting-started-with-your-dot" >}})）。

官方没有给出定时任务的数量上限、最短间隔、单任务最长时间和重试策略。系统卡的评估使用了 4 分钟、30 分钟、4 小时和一年的模拟「时间预算」，并说明 dots 用时间预算设置引导工作时长；这是评估设定，不是产品限制（[系统卡附录]({{< relref "/docs/dots/sources/official/2026-09-29-gpt-6-astra-system-card-dots" >}})）。

## 实测：能跑数天，也会漏跑

**能持续推进的例子。** Reddit 用户让 dot 审阅数百份 PDF，工作持续数天，dot 记得进度，中途插问后能回到原任务；遇到需要许可的步骤时，它继续做已授权的部分。没有原生队列，dot 会记住被阻塞的任务、定期重试（[Reddit：拿棍子戳 Dots]({{< relref "/docs/dots/sources/community/2026-10-01-reddit-poking-dots-with-sticks" >}})）。国内用户让 dot 持续监控京东上的 Mac 价格和敦煌到北京的机票，每次降价都收到消息（[靖轩：深度体验 11 天]({{< relref "/docs/industry/sources/community/2026-10-10-jingxuan-dots-11-days" >}})）。Wired 2026-10-27 的横评中，要求研究 30 分钟时，只有 Muse 和 Dots 在大部分规定时间里持续研究；只有 Dots 和 Claude Duet 发现了邮件提醒与日历的冲突（[Wired 全面实测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})）。

**出问题的例子。** FSR 在 Pro 200 美元档上做了几组定时任务测试（日本时间 2026-10-04 至 10-07，单次、无对照）：间隔 20 分钟的检查都按时收到；但 dot 改写了保存的指令，编辑页摘要显示「每 20 分钟、永不结束」，打开重复规则才看到两次的上限；暂停某个计划任务后，那次检查没有按时运行，dot 事后补做；dot 整体暂停期间 19:02 到期的一次性「ping」始终没有送达，「已计划」列表却把它标为「已完成」，dot 也没有补发。FSR 建议把「已完成」当标签而不是结果，并指出官方两处文档都没有说明暂停期间到期的任务会怎样（[FSR 实测]({{< relref "/docs/dots/sources/community/2026-10-09-fsr-dots-tested" >}})）。Slide Factory 设置的每天上午 8 点 SEO 日报，在作者结束会话时仍未运行（[Slide Factory 第一天]({{< relref "/docs/dots/sources/community/2026-10-03-slidefactory-dots-first-day" >}})）。

社区评价两极：一方面有人认为 dots「擅长主动调研」（[中国新闻周刊]({{< relref "/docs/industry/sources/media/2026-11-08-china-newsweek-personal-agents" >}})）；另一方面有人批评其主动性「近乎定时任务、缺常识、空转烧 token」（[鸿煊：到底新在哪]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。

## 打扰的边界由用户的指示决定

官方建议用户告诉 dot 把更新发到哪里、什么时候打断自己，例如例行进展留在 ChatGPT，需要决定的事带到 Slack 或短信，「只有在截止日期面临风险或你需要我做决定时才发消息」（[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})）。2026-10-28 起，短信测试版中的 dot「也会主动给你发短信」，回复 STOP 可停止（[发布说明：给你的 dot 发短信]({{< relref "/docs/dots/sources/official/2026-10-28-relnotes-texting-your-dot" >}})）。由 dot 发起的通话计划在发布之后推出（[文档：给你的 dot 发消息]({{< relref "/docs/dots/sources/official/2026-11-05-docs-message-your-dot" >}})）。

对外联系要单独批准：批准一条消息「并不意味着你的 dot 获得了代表你联系他人的持续许可」；可以预先批准「每周五在团队频道发更新」这类定期消息，但要写明对象、内容和时间（[隐私常见问题]({{< relref "/docs/dots/sources/official/2026-11-05-help-dots-privacy-security-faqs" >}})）。官方没有给出主动联系的频率上限或免打扰时段设置。

## 资料缺口

- 定时任务的数量上限、最短间隔、单任务时长、失败重试与失败通知。
- 主动研究多久运行一次，什么程度的发现会推送给用户。
- 哪些服务支持事件监控，延迟多少。
- 电脑关机时本地任务和定时任务的行为；FSR 测试时电脑一直开着。
- 后台智能体和主动研究是否计入用量。

## 主要资料

- 官方：[文档：任务与记忆]({{< relref "/docs/dots/sources/official/2026-11-05-docs-tasks-and-memory" >}})（任务类型、定时与事件、打扰控制）；[文档：控制你的 dot]({{< relref "/docs/dots/sources/official/2026-11-05-docs-controls" >}})（暂停、停止、取消）；[安全博客]({{< relref "/docs/dots/sources/official/2026-09-29-how-we-build-safety-into-dots" >}})（主动研究只读）；[系统卡附录]({{< relref "/docs/dots/sources/official/2026-09-29-gpt-6-astra-system-card-dots" >}})（时间预算）。
- 媒体：[Wired 全面实测]({{< relref "/docs/industry/sources/media/2026-10-27-wired-every-major-ai-agent" >}})（持续研究对比）；[NYT 五个杀手级任务]({{< relref "/docs/industry/sources/media/2026-10-25-nyt-five-killer-tasks" >}})（无位置触发）。
- 社区：[FSR 实测]({{< relref "/docs/dots/sources/community/2026-10-09-fsr-dots-tested" >}})（定时与暂停测试）；[Reddit：拿棍子戳 Dots]({{< relref "/docs/dots/sources/community/2026-10-01-reddit-poking-dots-with-sticks" >}})（多日长任务）；[主动型智能体对比]({{< relref "/docs/industry/sources/community/2026-11-03-proactive-ai-agents-compared" >}})（无 webhook）。
