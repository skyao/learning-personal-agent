---
title: "九款常驻型个人智能体横评：安全、记忆与成本"
linkTitle: "九款个人智能体横评"
date: 2026-11-03
originalTitle: "Best Personal AI Agents in 2026: 9 Always-On Assistants Compared on Security, Memory and Cost"
sourceUrl: "https://resources.rework.com/tools/ai-agents/best-personal-ai-agents-2026"
author: "Victor Hoang"
publisher: "Rework"
language: en
fidelity: 转载全文
translation: 已翻译
collectedAt: 2026-11-28
tags: [商业与规模, 安全, 开放与价格]
products: [dots, gemini-spark, poke]
dateNote: "2026-11-03 更新"
---

{{< source-info >}}

**收录说明**：Rework 对 9 款常驻型个人智能体的横评，按运行位置、交互渠道、记忆与安全四条轴比较，事实取自各厂商文档、发布文与公开安全研究。直接下载全文；删去页首语言切换、摘要按钮与作者简介，配图为装饰性插图未收入。补收（2026-11-03，11-28 轮次发现）。

**内容摘要**：文章把 9 款产品分成自托管与订阅制两类：OpenClaw 与 Hermes Agent 适合想自己掌控部署、只付模型费用的用户，OpenAI dots、Claude Cowork 与 Google Gemini Spark 适合愿意租用已有订阅内托管智能体的用户，Poke 与 Lindy 覆盖“直接发短信”一端，Perplexity Personal Computer 与 Manus 介于两者之间。涉及跟踪产品的内容称：dots 仅限 ChatGPT Pro（含 Pro 100、200、500 档位），首个 dot 不另收费，在 EEA、英国与瑞士不可用；Spark 含于 Google AI Pro 与 Ultra 订阅，在 Google 云端 24 小时运行，付款或发邮件前会征求确认；Poke 为短信助手。文末另有选购误区清单与按托管方式选产品的决策框架。

**保留理由**：这是跟踪产品（dots、Gemini Spark、Poke）与候选产品（Hermes、OpenClaw、Perplexity Personal Computer、Manus）同口径的横向对照，安全与记忆的比较轴此前已收横评较少涉及；各产品小节均注明事实来源。

---

OpenClaw 与 Hermes Agent 是最好的个人智能体——如果你想要自己掌控部署、把数据留在自己的机器上、只为模型付费；而 OpenAI 的 dots、Claude Cowork 与 Google 的 Gemini Spark 更适合你愿意租用一个已经包含在现有订阅里的托管智能体的情况。Poke 与 Lindy 覆盖「直接发条消息就行」那一端市场，Perplexity 的 Personal Computer 与 Manus 介于两者之间：桌面应用加云端大脑。我们按四项决定「个人智能体是不是个好主意」的属性比较了九款产品：它实际在哪里运行、你怎么和它说话、它记得什么，以及别人试图和它说话时会发生什么。

个人智能体与我们[最佳自主 AI 智能体](https://resources.rework.com/tools/ai-agents/best-autonomous-ai-agents-2026)或[最佳 AI 浏览器智能体](https://resources.rework.com/tools/ai-agents/best-ai-browser-agents-2026)汇总里的工具不是同一类东西。那些是为团队执行一项明确工作而造的。个人智能体为一个人工作：它读你的收件箱、动你的文件、待在你的消息应用里，在你睡觉时继续干活。这就是为什么选购问题大多关乎信任。智能体持有你的凭据和你的上下文，所以一次错误或被劫持的指令会落到你个人头上。基本定义见[什么是 AI 智能体](https://resources.rework.com/libraries/ai-agents/what-is-an-ai-agent)。这个品类变化也快，改名、所有权变更和停服都在几个月内发生，所以下面的产品说明都点明所有者，以及各厂商当前列出的套餐。

## 关键事实

- 提示注入（prompt injection），即智能体读到的文字悄悄改变它的行为，在 [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) 中排在 LLM01，是列在第一位的风险。一个读你邮件和消息的智能体，在设计上就暴露在它面前。
- OpenClaw 自己的安全指引假定[每个网关一个信任边界](https://docs.openclaw.ai/gateway/security)：单个操作者，或者一个彼此信任的团队。它明说这个产品不是按敌意的多租户边界来构建的。
- Hermes Agent 的网关是失败即关闭（fail-closed）的：按其[安全指南](https://hermes-agent.nousresearch.com/docs/user-guide/security)，如果没有配置白名单、也没打开全允许开关，所有消息用户都会被拒绝。
- OpenAI 的 [dots 文档](https://learn.chatgpt.com/docs/dots)说一个 dot 一次只能连接一台个人电脑，而且那台电脑必须在线并打开 ChatGPT 应用。
- Perplexity 的 [Personal Computer 帮助文章](https://www.perplexity.ai/help-center/en/articles/14659663-what-is-personal-computer)说，在 Mac 上云模型仍负责规划、搜索和推理，而本地模型处理私有文件和敏感步骤。

## 快速对照表

| 工具 | 最适合 | 起步价 | 关键优势 | 关键限制 |
| --- | --- | --- | --- | --- |
| **OpenClaw** | 想要完全掌控的折腾型用户与团队 | 免费，MIT 许可；模型费用付给模型提供商 | 跑在你自己的机器上，多个聊天渠道，持久记忆 | 安全加固由你自己负责 |
| **Hermes Agent** | 想要一个会学习的智能体的自托管用户 | 免费，MIT 许可；Nous Portal 可选 | 自动生成技能，沙箱后端，内置定时任务 | 终端优先的部署方式，由你自己运维 |
| **ChatGPT dots** | 想要托管型常驻智能体的 ChatGPT Pro 用户 | 含在 Pro 内（Pro 100、200、500 档） | 自有云电脑，可在 ChatGPT、Slack 和 Teams 中触达 | 仅限 Pro；在 EEA、英国与瑞士不提供 |
| **Claude Cowork** | 想要一个处理自己文件的知识工作者 | 含在 Claude Pro 内，按年付费 17 美元/月或按月 20 美元 | 定时任务，手机派发任务，按文件夹限定访问范围 | 访问本地文件需要桌面应用；有用量限制 |
| **Gemini Spark** | Google Workspace 用户 | 含在符合条件的 Google AI 套餐内；AI Pro 19.99 美元/月 | 在 Google 云端 24/7 运行，花钱或发送前会先询问 | 仅限部分国家，资格条件会变 |
| **Perplexity Personal Computer** | 想要本地/云端混合智能体的 Mac mini 或台式机用户 | Pro 按年付费 17 美元/月；Max 按年付费 167 美元/月 | 本地模型处理私有文件，在 Mac mini 上 24/7 运行 | 云端工作量按额度计费 |
| **Manus** | 研究与构建任务，外加一个桌面智能体 | 免费档；付费档为 8,000 或 40,000 额度 | 广域研究（Wide Research），My Computer 桌面桥接 | 按额度计费；2026 年所有权发生变更 |
| **Poke** | 想用短信使唤助手的人 | 免费；Pro 19 美元/月 | 存在于 Messages、WhatsApp 或 Telegram 里 | 自托管；先读隐私政策 |
| **Lindy** | 创始人与小团队 | 免费额度；团队版 29.99 美元/月起 | iMessage 接入，收件箱与日历工作流 | 定位更接近工作队友而非个人智能体 |

## 2026 年如何选择个人 AI 智能体

这个品类的大多数评测是在给演示排名。个人智能体值得按四项演示里看不出来的属性来评判。

### 1. 它实际在哪里运行？

有三种模式。像 OpenClaw 或 Hermes 这样的**本地**智能体跑在你自己的机器或服务器上，状态也存在那里。像 dots 或 Gemini Spark 这样的**托管云**智能体跑在厂商的计算机上，你的笔记本合上时仍在工作。像 Cowork、Perplexity 的 Personal Computer 或 Manus 这样的**混合**智能体，把云端大脑与能触及你文件的桌面应用配在一起。本地模式给你控制权，但配置错了爆炸半径也更大。云端模式给你在线时间，在你自己的设备上占用的空间更小。混合模式意味着你的手机可以发起任务，但碰本地文件的那部分需要桌面开机。

| 模式 | 例子 | 笔记本合上时能工作吗 | 谁打补丁 |
| --- | --- | --- | --- |
| 本地、自托管 | OpenClaw、Hermes Agent | 只有部署在常开机器上才行 | 你 |
| 托管云 | ChatGPT dots、Gemini Spark | 能 | 厂商 |
| 混合 | Claude Cowork、Perplexity Personal Computer、Manus | 云端任务可以；本地文件任务需要桌面开机 | 双方 |
| 文本优先助手 | Poke、Lindy | 能 | 厂商 |

### 2. 谁能和它说话？

一个在聊天应用里收听的个人智能体多出一个攻击面：任何能给它发消息的人。OpenClaw 的默认配置对此的回答是：给未知的私信发送者一个配对码，群组走白名单。Hermes 则除非你配置白名单，否则拒绝所有人。托管产品用另一种方式收窄范围。OpenAI 说一个 dot 只能给你发消息，而且只有你能给你的 dot 发消息。无论你选哪款，都要找到决定智能体接受谁指令的那个设置，并在连接任何一个账户之前设好。我们的 [AI 智能体安全](https://resources.rework.com/libraries/ai-agents/ai-agent-security)指南讲了威胁模型，[AI 智能体护栏](https://resources.rework.com/libraries/ai-agents/ai-agent-guardrails)讲了无论智能体被告知什么、都应当守住的硬性限制。

### 3. 它记得什么，存在哪里？

记忆是让个人智能体显得个人的功能，它同时也是一份关于你的数据存储。OpenClaw 保留关于你的偏好、项目和人物关系的持久记忆。Hermes 在会话之间保存对话、记忆和技能，并提示你换机器时备份它的数据目录。Dots 把对话、ChatGPT 记忆和它们自己保存的笔记合在一起。要问清记忆存在哪里、你能不能读取和删除、它会不会跟着你进入群聊。OpenAI 的文档说，dot 在把私密对话的信息分享给他人之前，会先确认你已允许。

### 4. 账单长什么样？

开源智能体下载免费，运行不免费。你要按 token 付给模型提供商，或者付托管账单，或者两者都付；常驻智能体重度使用可能比一份固定订阅更贵。订阅制智能体把 token 成本藏了起来，但用额度和用量限制来配给。在断定免费或固定费率更便宜之前，先按你真实的日常用量算一遍。

### 规模与人物画像表

| 工具 | 最合适的人 | 主要买家 |
| --- | --- | --- |
| OpenClaw | 熟悉终端、习惯自己动手的个人与小型可信团队 | 技术型创始人、开发者、IT 负责人 |
| Hermes Agent | 想要一个自己构建技能的自托管者 | 开发者、研究者 |
| ChatGPT dots | Pro 套餐上的重度 ChatGPT 用户 | 高管、顾问、重度用户 |
| Claude Cowork | 生活在文档、表格和研究里的人 | 分析师、幕僚长、运营经理 |
| Gemini Spark | Google Workspace 用户 | 使用 Google AI 套餐的管理者、创始人、学生 |
| Perplexity Personal Computer | 想要为私有文件做本地推理的 Mac 和 Windows 用户 | 研究者、顾问 |
| Manus | 研究密集、构建密集的个人工作 | 市场人员、创始人、分析师 |
| Poke | 想要短信界面的个人 | 忙碌的专业人士 |
| Lindy | 想要一个助手贯通邮件、日历和 Slack 的小团队 | 创始人、销售负责人 |

## 1. OpenClaw：想要自己拥有智能体的人的开源默认选择

今天人们说「个人 AI 智能体」时，多数人指的是 OpenClaw 这个项目。它是一个开源助手，你把它跑在自己的 Mac、Windows 或 Linux 机器上，它通过你已经在用的消息应用行动。它的网站列出 WhatsApp、Telegram、Discord、Slack、Signal 和 iMessage 等 29 个渠道，并描述整理收件箱、发邮件、管理日历这类工作。状态存在你的机器上而不是厂商云端，记忆跨对话持续保留。

所有权在这里很重要，因为这个项目已经改过形态。它由 OpenClaw Foundation 维护，这是一个独立的美国非营利组织。网站说 OpenAI 是捐赠者，而 OpenClaw 不是 OpenAI 的产品，并说整个产品保持 MIT 许可，没有企业版也没有付费版。你自己带模型——托管的、订阅附带的或本地的都行，网站举的例子是 Claude 和 GPT。

安全态势值得读得最仔细。OpenClaw 的[安全指南](https://docs.openclaw.ai/gateway/security)描述了保守的默认值：标准安装下网关绑定回环地址，未知的私信发送者会拿到配对码，群组访问走白名单。它也告诉你凭据、对话记录和日志都存在磁盘上，有消息工具权限的智能体默认可以跨会话发送消息，而 `openclaw security audit` 命令会检查你是否偏离了安全设置。这工具是给真的会读那份指南的人用的。

| 你得到什么 | 你得不到什么 |
| --- | --- |
| 免费、MIT 许可、状态在你自己的机器上 | 一条支持热线；你只有社区和文档 |
| 广泛的渠道覆盖与持久记忆 | 一个被托管、被打补丁的服务；加固是你自己的事 |
| 任意你选择的模型，包括本地模型 | 一份可预测的账单；模型花费取决于你的用量 |

**定价：** 免费。项目声明没有订阅、托管档或 token。模型访问由你接入的提供商计费，如果跑在服务器上还会有托管成本。来源：[openclaw.ai](https://openclaw.ai)。

**适合：** 想要一个完全由自己掌控的个人智能体的技术用户和小型可信团队。

**不适合：** 想要托管服务的人，或者没先读安全指南就把它连上工作账户的人。

---

## 2. Hermes Agent：自己写技能的自托管智能体

Hermes Agent 出自 Nous Research，与 OpenClaw 的基本交易相同：免费、MIT 许可、你放在哪里就在哪里运行、通过消息应用和你说话。它的网站列出 Telegram、Discord、Slack、WhatsApp、Signal、邮件和命令行，文档描述一个网关可达 20 个以上平台，包括 Microsoft Teams。你可以把它装在 macOS、Linux 或 Windows 本地，在 macOS 或 Windows 上用桌面应用，或者选择部署在 Nous Portal 上。

它的卖点是一个学习循环。Hermes 跨会话保留记忆，并从学到的东西里生成可复用的技能，文档把这称作与开放的 agentskills.io 标准兼容的程序性记忆。定时调度是内置的，可以把结果投递到任何已连接平台。

安全设计比多数产品更明确。有风险的命令会触发审批提示，如果你没及时回答，命令就被拒绝。即使在 YOLO 模式下，一条硬性黑名单也会拒绝灾难性命令。Docker、Modal、Daytona 和 Vercel Sandbox 后端以容器为边界。指南对局限也很诚实，指出其文件写入拒绝名单防的是意外，并不为敌意或已被攻陷的智能体做沙箱。对网关部署，它建议用容器或远程后端、明确的白名单和非 root 用户。

| 你得到什么 | 你得不到什么 |
| --- | --- |
| 免费且 MIT 许可，内置六种执行后端 | 一个托管产品，除非你选择 Nous Portal |
| 审批闸门、失败即关闭的白名单和容器隔离 | 本地后端上对已被攻陷智能体的防护 |
| 随时间累积的技能与记忆 | 打磨过的消费级入门流程 |

**定价：** 智能体免费。模型提供商和托管服务各有自己的定价。若使用 Nous Portal，其套餐为 Free（0 美元，仅免费模型）、Plus（20 美元/月）、Super（100 美元/月）和 Ultra（200 美元/月），付费档包含每月额度。来源：[hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com)。

**适合：** 想要一个自带真实审批模型和内置调度的自托管智能体的开发者与研究者。

**不适合：** 非技术用户，或者希望厂商承担运维负担的人。

---

## 3. ChatGPT Dots：OpenAI 的托管型常驻智能体

OpenAI 对常驻这一品类的回答是 dot。OpenAI 把它描述为一个让工作在你的各种工具和项目之间持续推进、需要你决策时会征求你意见的智能体。每个 dot 都有自己的云电脑和浏览器，所以你的设备关机时工作仍在继续。你可以在 ChatGPT、Slack、Teams 里，或者通过电话呼叫同一个 dot，切换渠道不会重置它的记忆。短信功能对美国 ChatGPT Pro 用户处于测试阶段。

有意思的是控制这部分。按 [dots 文档](https://learn.chatgpt.com/docs/dots)的说法，内置防护、你现有的 ChatGPT 应用权限和自动审批检查从一开始就生效，你自己的指令可以增加边界，但不能覆盖内置的安全要求。某个网站需要登录时，你在一个私密表单里输入凭据，凭据会送到浏览器而不是对话里，云浏览器还会把自己的会话与你电脑上的浏览器分开。连接一个消息渠道并不会授予它访问你的应用或电脑的权限。该页面还毫不含糊地说，dot 会犯错，而且停止一项任务并不会撤销它已经做过的操作。

可及性是问题所在。dots 只列在 ChatGPT Pro 上，不在 Plus 上：ChatGPT 定价页显示定时任务在 Go、Plus 和 Pro 上都有，而 dots 只在 Pro 上。OpenAI 的文档列出 Pro 100、Pro 200 和 Pro 500 为符合条件的套餐，面向 EEA、英国与瑞士以外 18 岁以上的用户；Business Premium 和 Enterprise 另行推出。

| 你得到什么 | 你得不到什么 |
| --- | --- |
| 自有云电脑和浏览器；设备关机也能工作 | Plus 或 Free 套餐上的可用性 |
| 可在 ChatGPT、Slack、Teams 里以及通过电话触达 | 美国测试版之外的短信功能 |
| 私密表单登录与审批检查 | 对已执行操作的撤销 |

**定价：** 含在符合条件的 ChatGPT Pro 套餐内，第一个 dot 不另收费。Pro 500 标价 500 美元/月，其他 Pro 档位的价格因国家而异。来源：[learn.chatgpt.com/docs/dots](https://learn.chatgpt.com/docs/dots)、[chatgpt.com/pricing](https://chatgpt.com/pricing/) 和 [DevDay 2026 笔记](https://learn.chatgpt.com/docs/whats-new/devday-2026)。

**适合：** Pro 上的重度 ChatGPT 用户，想要一个笔记本合上也能继续工作的托管智能体。

**不适合：** EEA、英国或瑞士的买家，或者想要检查和自托管这个智能体的人。

---

## 4. Claude Cowork：面向知识工作的文件夹限定型智能体

Cowork 是 Anthropic 为不涉及编程的知识工作做的智能体：研究、分析和文档撰写。你给它一个目标，它在你选定的文件和工具之间工作，然后把完成的工作交回来给你审阅。桌面应用是它的主要居所，也是触及你自己电脑上文件夹和应用的唯一方式。任务也可以从手机发起，在你笔记本合上时在云端继续。

让它进入个人智能体名单的是调度和派发。按 Anthropic 的 [Cowork 页面](https://claude.com/product/cowork)，你可以安排每天、每周或每月无人值守运行的重复任务，比如一份周报，还能从手机派发任务，随时随地去检查或改变任务方向。做网络工作时，Claude 会在侧边栏里打开一个单独的浏览器，这样你自己的浏览和登录不受影响。控制你屏幕的电脑使用功能还是研究预览版，Claude 会优先用连接器，其次用浏览器，只把屏幕当作最后手段。

权限模型围绕文件夹构建。你选择 Claude 能触及哪些文件夹和工具，删除任何东西都需要你批准；打开权限设置后，Claude 在做重要操作前会先显示计划并等你批准。Cowork 不太像是一个会在 WhatsApp 上给你发消息的智能体，更像是一位你能把活交给它的得力同事。

| 你得到什么 | 你得不到什么 |
| --- | --- |
| 按文件夹限定的访问，删除前需审批 | 聊天应用式的界面；你在 Claude 的应用里工作 |
| 定时的重复任务与手机派发 | 没有桌面应用就无法访问本地文件 |
| 含在一份你或许已经在付的套餐里 | 无限用量；它消耗套餐限额比聊天更快 |

**定价：** Anthropic 把 Cowork 列在 Pro、Max、Team 和 Enterprise 上。Pro 按年付费 17 美元/月（一次性付 200 美元）或按月 20 美元，Max 为 100 美元/月，Ultra 为 200 美元/月，Team 按年付费每标准席位 20 美元/月（按月 25 美元）。有用量限制。来源：[claude.com/product/cowork](https://claude.com/product/cowork) 和 [claude.com/pricing](https://claude.com/pricing)。

**适合：** 想要一个智能体从自己的文件里产出文档、报告和研究的分析师、幕僚长和运营人员。

**不适合：** 想靠聊天应用打理生活的人，或者需要自托管的团队。

---

## 5. Gemini Spark：Google 面向 Workspace 用户的 24/7 智能体

Spark 是 Google 的个人智能体，Google 自己的描述是一个在后台工作、你的笔记本合上或手机锁屏时仍在运行的 24/7 个人 AI 智能体。它跑在 Google 的云基础设施上，原生连接 Gmail、Docs 和 Sheets 等 Workspace 工具，并接受重复性指令，比如每周五早上检查某件事。

控制权在你手里。按 Google 的 [Spark 印度发布文](https://blog.google/intl/en-in/company-news/technology/introducing-gemini-spark-your-247-personal-ai-agent-in-country/)，由你决定是否开启 Spark、它可以连接哪些应用，而且它被设计成在花钱或发邮件这类高风险操作前先询问。它的草拟示例会把邮件存进草稿箱等你审阅，而不是直接发出，这对个人智能体是正确的默认做法。

诚实的局限是可用范围和清晰度。Google 说 Spark 面向部分国家的 Google AI Pro 与 Ultra 订阅者，推出情况因国家而异，所以要查你所在国家是否符合资格。它也与 Google 的生态绑在一起：如果你的工作活在 Microsoft 365 里，这就不是你的智能体。

| 你得到什么 | 你得不到什么 |
| --- | --- |
| 在 Google 云端运行，不需要笔记本 | 自托管或本地控制 |
| 由你自己开启的原生 Workspace 连接 | Google 应用之外同样的体验 |
| 花钱或发邮件前的审批 | 到处可用；它只限部分国家 |

**定价：** 含在符合条件的 Google AI 订阅内。在美国，Google AI Pro 为 19.99 美元/月（或按年 199.99 美元），Google AI Ultra 起价 99.99 美元/月，仅按月计费。请确认你所在国家哪个套餐带 Spark。来源：[Google AI 套餐](https://one.google.com/intl/en_us/about/google-ai-plans/)。

**适合：** 想要一个在 Gmail、Calendar 和 Drive 里撒手不管的智能体的 Google Workspace 用户。

**不适合：** 以 Microsoft 为中心的团队，或者需要智能体跑在自己掌控的硬件上的买家。

---

## 6. Perplexity Personal Computer：带本地模型的混合智能体

Perplexity 的 Personal Computer 是它面向 Mac 和 Windows 的桌面应用，围绕其基于网页的智能体 Computer 构建，可以访问你的本地文件和原生应用。它有特色的设计选择是感知隐私的路由。按[帮助中心文章](https://www.perplexity.ai/help-center/en/articles/14659663-what-is-personal-computer)，在 Mac 上一道隐私闸门可以遮蔽敏感细节、把某一步留在本地、拒绝该操作，或者在受保护的文件信息到达云端之前征求你的同意，同时由本地模型处理私有文件和敏感步骤。在 Windows 和 Linux 上，Portable Computer 版本在把任何东西从你的设备发往云端前会请求许可。

常驻的部分是硬件。Perplexity 推荐 Mac mini，因为它可以在你的笔记本合上时仍在后台 24/7 运行 Computer，任务从 iPhone 上发起、暂停或调整。Mac mini 不是必需的。操作在隔离沙箱里运行，设备端授权守护敏感步骤，Mac mini 会话还有双因素认证。由本地模型处理的工作不消耗 Computer 额度。

| 你得到什么 | 你得不到什么 |
| --- | --- |
| 为私有文件和敏感步骤服务的本地模型 | 一个完全本地的智能体；云端仍负责规划和推理 |
| 在你自己的 Mac mini 上 24/7 运行 | WhatsApp 或 Telegram 这类聊天应用渠道 |
| 隔离沙箱与同意提示 | 无限用量；云端工作会消耗额度 |

**定价：** Perplexity 列出 Pro 为按年付费 17 美元/月，Max 为按年付费 167 美元/月，Max 带有最高的 Computer 用量和更多每月额度。来源：[perplexity.ai/hub/pricing](https://www.perplexity.ai/hub/pricing)。

**适合：** 处理敏感文件、希望在链路中有本地模型的研究者和顾问。

**不适合：** 主要想从消息应用和自己的智能体对话的人。以研究为主的工具，见我们的[最佳 AI 研究智能体](https://resources.rework.com/tools/ai-agents/best-ai-research-agents-2026)汇总。

---

## 7. Manus：云智能体、桌面桥接与动荡的所有权之年

Manus 以面向研究、幻灯片和网站的云端智能体起家，2026 年转向个人使用。它的博客在 2026 年 2 月列出「Manus in Your Chat」，一个可从消息应用触达的个人智能体；3 月列出「My Computer」，一个桌面应用。My Computer 把云智能体与面向 macOS 和 Windows 的原生应用配在一起。设置时你授予它访问特定本地文件夹的权限，这就在云智能体与你的文件之间建立了桥接。任务可以从手机应用发起，但桌面机器必须开机、Manus Desktop 应用必须运行，Manus 建议用一台专用机器（比如 Mac mini）来实现 24/7 访问。

所有权这段故事就是它需要附带提醒的原因。Manus 于 2025 年 12 月 29 日发布「Manus Joins Meta」，随后于 2026 年 9 月 1 日发布题为「Manus Resumes Independent Operations」的文章，称创始团队继续领导公司。在那篇文章里，Manus 说部分用户不得不备份并恢复数据，部分用户一度失去访问。如果你在考虑把它作为个人上下文的居所，那是一个值得权衡的数据连续性信号。在连接任何敏感内容之前，先读那篇[文章](https://manus.im/blog/manus-resumes-independent-operations)。

| 你得到什么 | 你得不到什么 |
| --- | --- |
| 强大的研究与构建任务，外加一个桌面桥接 | 贯穿 2026 年稳定的所有权历史 |
| 从手机发起、在你的桌面上运行的任务 | 桌面关机或应用关闭时仍能运行的任务 |
| 一个可以试用的免费档 | 可预测的成本；计费按额度 |

**定价：** Manus 列出一个免费档和若干付费档；定价页显示每月 8,000 和 40,000 额度的档位，另有一个更低的档位，各自带 20 个并发任务和 20 个定时任务。美元金额和计费条款应在厂商页面上确认。来源：[manus.im/pricing](https://manus.im/pricing)。

**适合：** 想要一个智能体做网络工作、再加一个桌面桥接的个人研究者和市场人员。

**不适合：** 需要一家权属已定、有长期记录的公司作为买家的买家。

---

## 8. Poke：你用短信使唤的助手

Poke 是这里最简单的工具。它由 Interaction 制作，网站描述的是一个通过 Messages、WhatsApp 或 Telegram，以文字或语音消息使用的个人 AI 助手。它连接 Gmail、Google Calendar、Notion、GitHub、Asana、Linear 和 Todoist 等服务，创建提醒，还能运行它称为 Recipes 的自动化，并借助记忆主动帮忙。

Poke 还宣布 NewPoke 将并入 Cognition，所以要预期产品和政策会有变化。在连接敏感账户之前先读它的隐私政策。这对任何文本优先的助手都是正确的直觉：界面是一条聊天线程，背后的数据是你的邮件和日历。

| 你得到什么 | 你得不到什么 |
| --- | --- |
| 一条聊天线程式界面，无需安装 | 在读隐私政策之前对数据处理方式的确定性 |
| 广泛的应用连接与提醒 | 一个自托管选项 |
| 含 Gmail 和日历连接的免费档 | 在并入 Cognition 之后对产品方向的确定性 |

**定价：** 免费（0 美元，可连接应用、邮件和日历）；Pro 19 美元/月（前沿模型、后台自动化、更高的速率限制、优先支持）；Ultra 199 美元/月（最高速率限制，超出额度后按用量付费）。也提供按年计费。来源：[poke.com](https://poke.com)。

**适合：** 想要在消息线程里有个助手、不想配置任何东西的忙碌个人。

**不适合：** 对数据处理有严格要求的人。

---

## 9. Lindy：带文本界面的工作队友

Lindy 位于这个品类的边缘。它的定价页把「全天候与你的助手 iMessage 沟通」列在包含功能里，还有收件箱管理、日历排期、会议记录和每日简报，但它也把自己定位为面向业务工作的 Slack 原生队友。它更像创始人或小团队的队友，而不是 OpenClaw 意义上的个人智能体。如果你想把它和工作流工具比较，我们的 [Lindy 替代品](https://resources.rework.com/tools/ai-agents/best-lindy-alternatives)页面和 [Lindy vs Zapier Agents](https://resources.rework.com/tools/ai-agents/lindy-vs-zapier-agents) 对比讲得更深，我们的[最佳无代码 AI 智能体构建器](https://resources.rework.com/tools/ai-agents/best-no-code-ai-agent-builders-2026)汇总覆盖自己动手做的那一侧。

额度计量一切。日常请求用 2 到 250 额度，深度工作 250 到 1,000，大型构建 1,000 到 2,500；额度用完时，Lindy 会暂停使用额度的操作，而不是收取超额费用。

| 你得到什么 | 你得不到什么 |
| --- | --- |
| iMessage 接入，加上收件箱、日历和会议工作流 | 无限用量；每项任务都计额度 |
| 额度用尽时暂停而非超额计费 | 超出额度配额的超额账单 |
| 团队功能与企业级控制 | 消费优先的个人智能体设计 |

**定价：** 免费（0 美元，含 50 美元额度，有效期 7 天，无需信用卡）；团队版 29.99 美元/月起，含 3,000 额度，更大的档位最高到 1,750,000 额度、9,999.50 美元，额外额度每 1,000 收 10 美元；企业版定制。每月额度每周期重置，不结转。来源：[lindy.ai/pricing](https://www.lindy.ai/pricing)。

**适合：** 想在 iMessage 和 Slack 里有一个处理邮件和排期的助手的创始人与小团队。

**不适合：** 想要自托管或纯粹个人智能体的人。

---

## 选购个人 AI 智能体应避免的错误

| 错误 | 看起来是什么样 | 该怎么做 |
| --- | --- | --- |
| 第一天就连接所有东西 | 一个下午就把 Gmail、日历、文件、银行登录和 Slack 全连上 | 从一个低风险应用开始，随智能体赢得信任再扩大访问 |
| 把发送者策略留成开放 | 一个谁发消息都听的聊天应用智能体 | 在连接账户之前使用配对码或白名单 |
| 把「本地运行」当成「安全」 | 一个文件访问范围很广、没有沙箱的本地智能体 | 使用容器后端和限定范围的工作目录 |
| 忽视提示注入 | 一个总结了敌意邮件、然后照着做的智能体 | 对发送、付款和删除要求审批 |
| 凭演示购买 | 挑短任务里表现最好的那个智能体 | 用你自己真实的一周工作做试点 |
| 低估模型账单 | 以为免费软件就是免费智能体 | 先跟踪一周的 token 花费再决定 |
| 跳过所有权检查 | 在一个可能被收购、改名或关停的产品上养成习惯 | 读厂商最新的所有权与数据连续性说明 |

## 如何选择：决策框架

先挑智能体在哪里运行，再挑它为谁工作。

| 如果你需要…… | 就选…… | 为什么 |
| --- | --- | --- |
| 完全的控制，数据在你自己的机器上 | **OpenClaw** | MIT 许可，本地状态，任意模型 |
| 一个审批模型更严格的开源智能体 | **Hermes Agent** | 命令审批、失败即关闭的白名单、容器后端 |
| 一个笔记本合上也能工作的托管智能体 | **ChatGPT dots** 或 **Gemini Spark** | 自有云电脑或 Google Cloud，风险操作前审批 |
| 一个在你的文档和文件上工作的智能体 | **Claude Cowork** | 按文件夹限定的访问、定时任务、手机派发 |
| 为私有文件在链路中有本地模型 | **Perplexity Personal Computer** | 隐私闸门与本地推理 |
| 一个你直接发短信使唤的助手 | **Poke** 或 **Lindy** | 存在于你的消息线程里 |
| 繁重的研究与构建任务 | **Manus** | 广域研究、桌面桥接 |
| 团队运行的智能体而非个人智能体 | 见[最佳自主 AI 智能体](https://resources.rework.com/tools/ai-agents/best-autonomous-ai-agents-2026) | 为明确、共享的工作而造 |
| 一个零成本的起点 | 见[最佳免费 AI 智能体](https://resources.rework.com/tools/ai-agents/best-free-ai-agents-2026) | 免费与开源选项 |

如果你的智能体要处理购物，在给它支付方式之前，先读我们的[最佳 AI 智能体安全工具](https://resources.rework.com/tools/ai-agents/best-ai-agent-security-tools-2026)和[最佳智能体电商平台](https://resources.rework.com/tools/ai-agents/best-agentic-commerce-platforms-2026)汇总。

## 接下来做什么

从符合你托管偏好的那一节里挑一个智能体，在一项低风险工作流（比如晨间简报或收件箱分类）上做一周试点。只连接一个账户，先设好发送者策略，对任何发送、花钱或删除的操作都保持审批开启。一周结束时，读智能体的日志和你的账单，决定是扩大访问还是换工具。
