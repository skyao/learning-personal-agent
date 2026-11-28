---
title: "dots 的安全与防护"
linkTitle: "文档：企业安全指南"
date: 2026-11-05
originalTitle: "Safety and security in dots"
sourceUrl: "https://learn.chatgpt.com/docs/enterprise/dots-security"
altUrls: ["https://learn.chatgpt.com/codex/enterprise/dots-security"]
publisher: "OpenAI（ChatGPT Learn）"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "文档不标日期；按规则取收集日期。文中评估数据引自 2026-10-26 的 GPT-6.1 Terra 系统卡附录；2026-11-28 发现原文更新：旧版「OpenAI 如何评估模型安全防护」整节（GPT-6 系列各模型的提示注入、越狱、欺骗评估图表）已删去；数据存储驻留加入阿联酋（推理驻留仍不含），并说明测试期创建的 dots 会在正式可用日（2026-11-04）后 30 天内迁移到工作区指定区域；Microsoft Teams 全部删去；新增 Wallet 付款须成员逐笔生物识别批准的说明"
tags: [安全, 隐私, 商业与规模]
products: [dots]
---

{{< source-info >}}

**收录说明**：OpenAI 在 ChatGPT Learn 上发布的 dots 文档，文档不标日期，页面日期取第一轮收集日期 2026-11-05。第一轮收集时直接翻译，原文未单独存档；2026-11-28 按新流程重新抓取（直接下载），原文存于本目录的 original.md（网站上不显示）：7 处结构示意图和设置界面示意（设置开关、权限地图、dots 架构、登录表单、主动研究、自动审查、云端计算机开关）整理为「（界面示意：……）」段落，并去掉抽取后重复出现的方框文字；删去头像图；页内相对链接改为绝对地址。新版有新增和改写，旧译文已删去（由 git 保留），已翻译。

**内容摘要**：这是面向管理员和安全团队的 dots 安全指南：个人 dot 只能由所有者指挥，只能使用所有者已授权的应用连接，数据默认不用于训练。云端计算机的浏览器、网络和计算机操作可以分别开关，另有自动审查、安全监控和活动视图；本地电脑访问要管理员另行开启，委派任务按 Agent Security 策略执行。文中列出数据驻留（存储驻留含阿联酋，推理驻留只有美国和欧洲）、EKM、HIPAA，并说明不提供零数据保留、不适用 FedRAMP。使用 Wallet 时，即使管理员开启且成员给过长期指示，每笔付款仍须成员用生物识别批准。另有保留与删除表、用 Compliance API 的 `client_id = DOTS` 追踪记录的方法，以及成员离职的处理流程。

**保留理由**：这是 dots 在企业侧的数据边界、控制层次与审计方法的官方说明；新旧版对照可以看出模型评估数据被撤下、Wallet 与阿联酋驻留加入。

---

dot 是个人智能体，可以在对话之间持续工作。管理员使用基于角色的访问控制（RBAC）来选择谁可以使用 dots。个人 dot 使用其所有者已授权的应用连接，并受工作区设定的应用与操作范围限制。dot 可以做什么由所有者指定。

dot 能做什么，取决于该名员工的权限、工作区允许的操作，以及 dot 执行任务的位置。

## 安全概览

个人 dot 可以代表其所有者在对话之间工作。例如，员工可以让它跟进一个项目，并在有新进展时准备一份简报。dot 在自己的云端计算机上工作，可以把任务委派给 Work 或 Codex。在已连接的应用中，它继承其所有者所授权账户的权限。工作区的应用与操作设置对所有者及其 dot 同时适用。

项目文档可以为简报提供事实，但 OpenAI 训练 dots 背后的模型去抵御项目文档或类似 [prompt injection](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs) 中的任何隐藏指令。自动审查会在有后果的操作执行前进行检查，安全监控在检测到可能有害的行为时可以暂停或停止工作。

- **云端计算机。** 管理员分别控制浏览器访问、代码的网络访问和桌面交互。浏览器开启时，dot 可以访问公开网站，或以在该网站登录的账户的权限使用该网站。所有者可以[查看云端计算机或接管](https://learn.chatgpt.com/codex/dots/computers-and-apps)。
- **操作审查。** 在分享简报之前，[自动审查](https://openai.com/index/how-we-build-safety-security-and-privacy-into-dots/)会检查将要分享的内容、接收者是谁，以及所有者的指示、Custom Rules 和安全要求是否允许。它可以阻止该操作或要求确认。dot 无法关闭必需的检查。
- **已连接的计算机与 Codex Cloud。** dot 在已连接计算机上运行的工作遵循适用的本地 [Agent Security 策略](https://learn.chatgpt.com/codex/enterprise/agent-security)。如果 dot 把任务委派给 Codex Cloud，该任务遵循 Codex Cloud 策略及其所选环境的权限。
- **所有者监督。** 在[活动视图](https://learn.chatgpt.com/codex/dots/controls)中，所有者可以检查进行中和已委派的任务、纠正指示，或让 dot 停止。
- 企业数据默认不用于训练模型。dot 上下文、文件、已委派任务和审计记录各有不同的保留与删除边界；请分别核实每份副本的要求。
- **审计记录。** 管理员可以使用[可用的合规记录](https://learn.chatgpt.com/codex/enterprise/compliance-api)调查 dot 活动，并检查所连接服务自身的记录以核实实际改动。

**熟悉的云环境**

Dots 建立在与 ChatGPT Work 相同的云端计算机基础设施之上，并遵循你的工作区适用的隐私与安全防护。Dots 可以跨会话保留云端计算机快照，因此工作可以继续，无需从头开始。如果你的组织已经审查过 Work Cloud，可以把那次审查作为评估 dots 的起点。关于云环境的细节，见 [ChatGPT Work 云安全](https://learn.chatgpt.com/codex/enterprise/chatgpt-work-cloud-security)。

**选择启用哪些云端能力**

即使你关闭对云浏览器、云端计算机桌面，以及代码与 shell 命令的互联网访问，dots 仍能提供价值。成员仍可以用他们的 dot 起草内容、整理信息，并使用工作区允许的连接应用。你可以启用符合组织需求的云端能力。这些设置同样适用于 Work Cloud，所以改动它们会同时影响 dots 和 Work 任务。

**理解主动研究**

主动研究是 dots 与典型的用户指令型 ChatGPT Work 任务的一个区别。dot 可以在获得许可的连接应用中查找有用信息，而不必等待用户发出新请求。例如，它可以检查已连接的信息中是否有与进行中的工作相关的更新。

在主动研究期间，dot 可以读取已获许可的信息并保存私人笔记。它的研究工具不能直接向他人发送消息、通过连接应用改动内容，也不能控制浏览器或计算机。个人 dots 不会在没有用户指示的情况下主动执行写操作。其他 dot 活动，例如用户明确安排的定时任务，遵循各自适用的权限与操作规则。

我们正在 Agent Security 中制定更多规则，让管理员可以选择 dot 的云浏览器可以访问哪些网站。

## dots 如何保护工作区数据

- **模型防护帮助 dot 遵循所有者的指示。** OpenAI 训练 GPT-6 系列的模型拒绝有害请求，并抵御藏在邮件、文件或网页中的恶意指令。例如，一封要求 dot 转发私人文件的邮件，并不构成 dot 发送该文件的授权。这项授权来自所有者或所有者授权的自动化。[GPT-6 模型防护](https://deploymentsafety.openai.com/gpt-6-october/prompt-injection)
- **自动审查在执行前检查某些操作。** 例如，在 dot 发送邮件之前，自动审查会对照所有者的指示、Custom Rules 和安全要求，检查收件人与消息内容。自动审查可以阻止发送，而 dot 无法关闭必需的检查。在一项模拟的 Codex 任务中，受测的 GPT-6 模型没有一个绕过自动审查的拒绝。[查看 OpenAI 如何测试对自动审查拒绝的反应](https://deploymentsafety.openai.com/gpt-6-1-terra/respecting-auto-review)。部分默认的操作与确认规则可以自定义，但所有者的批准不能覆盖内置的安全要求。[自动审查如何工作](https://openai.com/index/how-we-build-safety-security-and-privacy-into-dots/)
- **安全监控可以中断进行中的工作。** dot 在规划和行动时，监控会寻找可能有害的行为，例如试图绕过防护，或超出所有者的指示行事。一旦发现疑虑，它可以暂停或停止任务。暂停可能向所有者显示一条警告供其查看。[内置防护](https://openai.com/index/introducing-dots/)
- **管理员在工作区设置中管理插件访问。** 同一套设置控制用户及其 dot 可以使用哪些插件和操作。dot 的云浏览器访问由另一项设置控制。只读插件会限制 dot 通过该插件能做的事。如果启用了云浏览器，dot 仍可能通过在该网站登录的账户做出改动。[工作区控制](https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces)
- **所有者可以检查并调整工作方向。** 在活动视图中，所有者可以检查已委派的任务、补充上下文、改变方向，或让 dot 停止。当 dot 无法完成一项任务时，它应当告诉所有者是什么阻碍了它、还有什么没做完。在被选来诱发「阻塞报告」失败的编码任务中，GPT‑6.1 Terra 约有 8% 的情况未能准确报告阻塞，比 GPT‑5.6 Terra 的 29% 有所下降。[查看 OpenAI 如何评估阻塞报告](https://deploymentsafety.openai.com/gpt-6-1-terra/blocker-deception)。信息分享的时机很重要。如果 dot 已经在 Slack 发过帖，频道里的人可能已经读到了那条消息。[活动视图与已完成的操作](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs)

> **推出 dots 之前要审查什么**
>
> 决定哪些员工应当可以使用 dots。个人 dot 使用其所有者已有的应用连接。检查每个已连接账户允许所有者读取或改动什么，以及工作区通过该连接允许哪些操作。如果 dots 可以使用云浏览器，或把工作委派给已连接的计算机，还要检查在那里登录的账户或本地设备允许做什么。

## 确认资格与数据要求

| **类别** | **资格与数据要求** |
| --- | --- |
| **数据与推理驻留** | 个人 dots 支持在澳大利亚、加拿大、欧洲（欧洲经济区与瑞士）、印度、日本、新加坡、韩国、阿联酋（UAE）、英国和美国的数据存储驻留。在设有数据驻留的工作区中，测试期创建的 dots 会在正式可用日（2026-11-04）后 30 天内迁移到工作区指定的区域。dots 的推理驻留支持美国和欧洲，不支持阿联酋。dots 发起的推理调用遵循你工作区的推理驻留设置（如有）。 |
| **企业密钥管理（EKM）** | 符合条件的工作区支持企业密钥管理（EKM）。 |
| **HIPAA** | 符合条件的工作区支持 HIPAA。请确认你的商业伙伴协议（BAA）与配置覆盖预期的工作流程。 |
| **零数据保留** | dots 和带本地计算机访问的 Work 都不提供严格的零数据保留。 |
| **FedRAMP** | dots 在 FedRAMP 工作区中不可用。 |

### 数据驻留与 EKM

静态存储的客户数据按照工作区的[数据驻留](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)和[企业密钥管理（EKM）](https://help.openai.com/en/articles/20000943-openai-enterprise-key-management-ekm-overview)设置存放。

保护其他处理客户数据的 OpenAI 服务的同一套访问控制，也适用于运行中的云端计算机。

## 管理谁可以使用和指挥 dot

- **工作区访问：** 在管理员预览期间，dots 的访问默认关闭。要为某个群组开启，在该群组的自定义角色中授予 Use dots。

（界面示意：Dots 访问与规则；Dots 访问、消息渠道、本地计算机访问和自定义规则。；Use dots Beta；Add dots to Slack；Allow local computer access；Use custom rules for dots；示例设置；开关位置与可用渠道可能因工作区而异。）

- **dot 归属：** 只有所有者可以指挥其个人 dot。来自其他人的消息，包括 Slack 里的提及，都不会启动工作，也不会让他们获得对 dot 的控制权。
- **连接权限：** 个人 dot 使用其所有者已有的插件连接。通过每个插件，dot 只能访问已连接账户、插件权限和工作区设置所允许的数据，并只能执行这些条件允许的操作。见 [dots 隐私与安全常见问题](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs)。
- **自动化：** 所有者可以用自动化提前批准某个操作，具体说明 dot 可以做什么、在什么时候做。例如，所有者可以让 dot 每周五在团队的 Slack 频道发布项目进展。dot 被设计为在该授权范围内行事，并遵循通常的权限与安全检查。

## dot 在哪里工作、哪些控制生效

（界面示意：权限适用范围 简化权限地图；工作区权限 工作区所有者通过工作区默认设置或按群组分配的角色开启 Use dots。；工作区访问；Dot 所有者 只有所有者可以指挥这个 dot。；Only the owner can direct this dot；你的 dot；连接的应用 使用为该应用连接授权的账户。适用应用权限与操作审批。；云端计算机 浏览器、网络和 computer use 控制。独立的浏览器登录。；本地计算机 管理员选择开启、成员自行设置。Agent Security 与设备策略。；Work 与 Codex 委派的任务遵循各自的模型权限。）

主 dot 对话：企业模型控制与默认设置在这里不适用。委派出去的 Work 和 Codex 任务遵循各自的模型权限。启用 dots 并不会连接所有服务。请配置每条路径并完成所需设置。这里展示的是权限边界，不是网络或数据流。

自动审查对浏览器、桌面和委派操作的覆盖范围仍在审查中。

dot 在云端协调工作。例如，如果你让它总结保存在你已连接笔记本电脑上的一份报告，读取该文件的命令会在你的笔记本电脑上运行。Agent Security 的本地策略决定该命令可以读取哪些文件。

（界面示意：dots 架构；你 设定方向；请求；交回；你的 dot 在 OpenAI 云端运行并协调工作 执行身份：dot 所有者。保留的状态：对话、私人笔记和记忆。；选定的上下文 + 任务；结果；委派的任务 独立的 Work 或 Codex 线程 执行目标；云环境 云端计算机 本地机器；检查：产品与环境权限。任务历史与文件；执行身份：dot 所有者。；需要审查的操作；阻止 + 原因；审查考虑 你的指示、Custom Rules 和安全要求；自动审查 允许或阻止相关操作；允许；连接的应用 已连接账户身份；应用与来源权限；连接服务中的数据；应用/操作策略 + 来源权限；云工作区 云端计算机与工具；云端文件与浏览器会话；浏览 创建文件 运行代码与工具；受云端能力控制约束。；本地访问闸门 + 设备权限；你的个人电脑 通过 ChatGPT 应用可选 本地文件与应用账户；本地策略与设备权限。；云工作区 你的 dot）

虚线框：独立的任务边界，不构成隔离保证。自动审查对浏览器、桌面和委派操作的覆盖范围仍在审查中。

要让本地工作可用，管理员需为 dots 开启 Allow local computer access。然后每位员工自行决定是否在 ChatGPT 中连接自己的电脑。

dot 可以[并行委派任务](https://learn.chatgpt.com/codex/dots/tasks-and-memory#assigned-work)，同时所有者继续对话。它可以代表所有者启动一个 Work 或 Codex 线程。当本地访问已开启且所有者连接了某台电脑时，任务可以使用那台电脑上的文件或工具。对于代码仓库工作，dot 还可以在可用的云端编码环境中启动一个 Codex Cloud 线程，而不使用所有者的电脑。在活动视图中打开该任务，即可看到它在哪里运行。见[把你的电脑和应用连接到 dot](https://learn.chatgpt.com/codex/dots/computers-and-apps)。

### 按工作环境划分的控制

先从 dot 在哪里执行操作、使用哪个账户开始。例如，限制员工笔记本电脑上文件改动的规则就在那里生效。dot 自己的云端文件遵循另一套控制。如果某个操作必须在所有地方都被阻止，就要检查 dot 可能采取该操作的每一种已启用方式。有些操作还需要所有者批准。

| **环境** | **适用哪些控制** | **管理员设置与成员操作** |
| --- | --- | --- |
| **主 dot 对话** | 工作区角色决定谁可以使用 dots 并设定自定义规则。所有者在该对话中指挥 dot。企业模型控制与默认设置不适用于主 dot 对话。 | **管理员。** 在 [Admin Console → 权限](https://learn.chatgpt.com/codex/enterprise/dots-admin-guide#set-up-dots-for-work)中，在工作区默认设置或自定义角色里设置 Use dots 和 Use custom rules for dots。关于托管审批与网页搜索，使用 [Agent Security → Global](https://learn.chatgpt.com/codex/enterprise/agent-security)。在插件控制中检查应用权限。**成员。** 告诉 dot 你想让它做什么。如果你的工作区启用了自定义规则，你可以设置一条长期指示，例如「改动共享文件前先问我」。 |
| **插件（连接的应用）** | 个人 dot 使用其所有者已授权的应用连接。它能通过该连接读取或改动什么，取决于所有者在应用中的访问权限、授予该插件的权限，以及工作区允许的操作。 | **管理员。** 在[插件控制](https://learn.chatgpt.com/codex/enterprise/dots-admin-guide#2-configure-app-access)中设置可用的应用和允许的操作。在来源服务中检查已连接账户的权限与已授权范围。**成员。** 连接工作区管理员允许的插件。 |
| **dot 的云端计算机** | 云端计算机设置管理浏览、代码与 shell 命令的网络访问，以及 computer use。dot 可以创建、编辑或删除它自己的云端文件。网站使用登录到云浏览器的账户。员工笔记本电脑上的登录状态、VPN 和设备策略不会自动延续过来。 | **管理员。** 在 Admin Console → 权限中选择工作区默认设置或角色。在 Workspace capabilities → [Let agents use cloud computers](https://learn.chatgpt.com/codex/enterprise/dots-admin-guide#set-up-dots-for-work)下设置 Use a browser、Allow network access (code and shell) 和 Allow computer use。在 Workspace capabilities 下单独设置 Use password manager。Agent Security 的站点规则将会允许管理员在 dot 的云浏览器中允许或阻止域名，并选择哪些站点允许上传或下载。**成员。** 从 dot 的资料页打开云端计算机，查看它在做什么。选择 Take over 自己完成某一步，之后想让它继续时选择 Return control。如果网站要求你登录，使用[私密表单](https://learn.chatgpt.com/codex/dots/computers-and-apps#sign-in-to-a-website)或接管云浏览器登录。 |
| **委派的 Work 或 Codex 任务** | 当 dot 启动一个独立的 Work 或 Codex 线程时，该产品的模型控制决定任务可以使用哪些模型。任务遵循 Agent Security 要求，以及它运行所在的其它控制。 | **管理员。** 在 Admin Console → 权限中检查对 Work 或 Codex 的访问，并审查该产品的模型控制。对于已连接的计算机，检查 Agent Security → Global 以及任何 Local 覆盖设置。对于 Work Cloud，审查云端计算机能力。对于 Codex Cloud，检查 [Agent Security → Codex Cloud](https://learn.chatgpt.com/codex/enterprise/agent-security) 和 [Settings → Codex Cloud → Environments](https://learn.chatgpt.com/codex/environments/cloud-environments)。**成员。** 在活动视图中打开委派的线程。检查它在哪里运行，查看它的来源与结果，并在那里补充缺失的上下文。 |
| **已连接的员工计算机** | 工作区必须允许 dots 使用本地计算机访问，员工也必须连接该计算机。其上的命令遵循适用的 Agent Security 与设备策略。dot 可以使用获许的本地文件、工具和应用，同时云端继续协调任务并处理其上下文。 | **管理员。** 在 Admin Console → 权限 → Use dots 中开启 [Allow local computer access](https://learn.chatgpt.com/codex/enterprise/cloud-local-access#enable-local-computer-access)。已连接的计算机继承适用的 Agent Security → Global 设置。在同一策略内，当该计算机需要不同的文件系统或网络限制时，用 Local 覆盖受支持的设置。设备权限也适用于桌面应用和屏幕访问。**成员。** 在那台计算机上，于 ChatGPT 应用中打开 dot 的资料页。在 [Computers → Your computer](https://learn.chatgpt.com/codex/dots/computers-and-apps#connect-your-computer)下选择 Allow access 并确认。让计算机保持在线，并让 ChatGPT 保持打开。 |

（界面示意：✦Blossom Bank；登录以继续；输入你的登录信息以继续；用户名；密码；你的凭据会私密地发送到该网站。保存是可选的，使用已保存的凭据总是需要你确认。了解更多；改为在网页上登录；暂不；登录）

### 托管策略如何适用

- **全局策略：** 在 [Agent Security](https://learn.chatgpt.com/codex/enterprise/agent-security) → Global 中，检查托管的审批要求，以及该工作流程是否允许网页搜索。
- **执行覆盖：** 对于员工笔记本电脑上的命令，检查 Agent Security → Local 中的文件系统与网络限制。对于委派的 Codex Cloud 命令，检查 Agent Security → Codex Cloud 以及所选环境的网络设置。
- **分别设置的控制：** 对于 dot 的云端计算机和 Work Cloud，分别检查浏览器访问、代码与 shell 的网络访问，以及 computer use。对于委派的 Codex Cloud 任务，检查所选的 Codex 环境。

## 管理连接的应用与凭据

| **访问路径** | **要检查什么** | **该控制覆盖什么** |
| --- | --- | --- |
| **插件（连接的应用）** | 在插件控制中，审查成员可以使用哪些应用和操作。在来源服务中，检查是哪个账户授权了连接。对于发送邮件，确认该操作已启用，且该账户可以向预期收件人发送。 | dot 只能使用现有连接执行工作区允许、且已连接账户获许的操作。要结束通过该连接的访问，在来源服务中撤销应用授权。这会停止通过该连接发出的新请求。dot 可能仍然持有它早前获取的信息。应用访问与其他 ChatGPT 体验共享。见 [dots 隐私与安全常见问题](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs)和[在 ChatGPT 工作区中管理 dots](https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces)。 |
| **浏览器登录** | 确认登录到该网站的是哪个账户。在授予敏感数据访问权限之前，核实应用连接和网站账户在来源系统中的权限。 | 例如，某个插件可能允许 dot 读取一份文档，而该网站的账户同时还能编辑它。在允许该浏览器工作流程之前，先检查网站账户的角色。 |
| **网站凭据** | 网站登录时，使用私密登录表单或接管浏览器。对于受支持的登录，OpenAI 会从私密表单把密码直接发送到云浏览器，不向模型暴露。应用工具可以通过后端凭据处理完成认证，浏览器自动化可以使用已登录的会话。云浏览器单独保存自己的会话 cookie，与成员的设备分开。dot 计算机上的代码如果能看到某个应用令牌或浏览器 cookie 的值，就可以读取它；不要假定会话或令牌与在那里运行的代码相互隔离。插件凭据以及仅在浏览器会话中使用的值不会出现在日志中。 | 使用已保存的密码进行新的登录需要确认。登录之后，dot 可以以该账户的权限使用该网站。要结束访问，管理员可以在受支持的来源服务中撤销该网站会话。成员也可以在云浏览器中退出登录，或在 Settings → Cloud browser → Browser data 中清除该站点的 cookie。见[把你的电脑和应用连接到 dot](https://learn.chatgpt.com/codex/dots/computers-and-apps)。 |
| **Codex Cloud 密钥** | 对于委派的 Codex Cloud 任务，使用有文档说明的环境密钥控制。网络密钥会向程序传递占位符，并在允许的 HTTPS 目标处替换为真实凭据。直接设置的环境变量对程序可见。 | 这些控制适用于 Codex Cloud。关于密钥配置，见 [Codex Cloud 环境](https://learn.chatgpt.com/codex/environments/cloud-environments)。 |

## 设定审批与无人值守工作的规则

主动研究是 dot 在两次请求之间进行的后台工作，用来查找与其所有者工作相关的更新。这项研究是只读的。dot 可以读取其所有者通过连接应用有权访问的信息，并就发现的内容保存私人笔记。它的研究工具不能发送消息、编辑共享内容，也不能控制浏览器或计算机。要把一项发现发送到 Slack，dot 需要所有者对这次发送及其受众的授权。自动审查会检查拟议的发送。

（界面示意：你的 dot 的云环境；你；有用的建议；你的 dot 的云环境；你的 dot 决定如何帮忙；开始研究；私人笔记；主动研究 后台任务 · 只读工具；连接的应用 你的权限；读取请求；信息）

在授权一项重复任务时，要指明操作、收件人、触发条件和时间安排。获准起草一封客户邮件只覆盖草稿。发送它需要另行授权。关于操作审批，见 [dots 隐私与安全常见问题](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs)。

| **机制** | **它做什么** | **条件与限制** |
| --- | --- | --- |
| **操作审批** | 所有者可以授权「每周五把项目周报邮件发给项目负责人」。该指示覆盖指明的收件人和时间安排。 | 超出该范围的变化需要新的审批，包括受众、内容或时间的改变。 |
| [**自动审查**](https://learn.chatgpt.com/codex/sandboxing/auto-review) | [自动审查](https://learn.chatgpt.com/codex/sandboxing/auto-review)会在标记为「write」的工具调用执行前进行检查。例如，在发送邮件之前，它会对照所有者的指示、Custom Rules 和安全要求，检查收件人是谁、消息内容是什么。 | [自动审查](https://learn.chatgpt.com/codex/sandboxing/auto-review)可以阻止发送，或提示所有者澄清收件人或批准该操作。批准不能覆盖必需的安全检查。Computer Use 会单独请求使用桌面应用的权限。 |
| **Custom Rules** | 所有者可以设定一条规则，要求在发送邮件前询问。该规则可以增加这道审批步骤。它不能授予已连接账户不具备的发送权限，也不能覆盖必需的安全检查。 | 关闭自定义规则并不会强制每个操作都请求批准。请区分成员可编辑的规则、[Agent Security](https://learn.chatgpt.com/codex/enterprise/agent-security) 中的企业要求，以及连接服务强制执行的权限。关于自定义规则的设置，见[在 ChatGPT 工作区中管理 dots](https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces)。 |

（界面示意：对敏感操作的自动审查；你 设定方向；请求；交回；你的 dot 由 GPT-6 系列驱动；协调工作；需要审查的操作；阻止 + 原因；审查考虑 你的指示、Custom Rules 和安全要求；自动审查 允许或阻止相关操作；允许；云工作区 云端计算机与工具；云工作区 你的 dot）

对浏览器、桌面和委派操作的覆盖范围仍在审查中。

- **在本地计算机上委派的工作。** 委派的线程使用成员已连接的计算机。当 Computer Use 已启用且该应用已获批准时，选择「Always allow」即允许 ChatGPT 使用该应用而不再请求访问。
- **Wallet 付款。** 即使管理员启用了 Wallet，且成员已给其 dot 长期指示，成员仍须用生物识别审查并批准每一笔 Wallet 付款。

### 示例：同一封对外邮件经三条路径发送

- 假设所有者授权某个 dot 每周五把已批准的项目更新邮件发给客户方的 Lee，不带附件。把这次发送与新增一位收件人相比：新收件人需要新的授权。如果公司政策禁止该收件人，即使所有者批准也无法授权投递。

| **路径** | **技术上被阻止** | **新的审批** | **长期授权** |
| --- | --- | --- | --- |
| **邮件插件** | 发送操作被禁用，或已连接账户缺少发送权限。 | 新增收件人需要新的决定。要求写操作前询问的应用策略，也会对原本的发送要求批准。 | 如果该操作已启用、账户可以发送、且适用的检查允许，周五的发送可以继续进行。 |
| **网页版邮件中的云浏览器** | 工作区禁用了云浏览器访问，或邮件服务拒绝为已登录账户投递。 | 新收件人需要发送审批。确认已保存的登录只批准登录。在 Send 按钮处出现的提示未经核实。 | 可以复用活动会话。周五的指示覆盖原来那封邮件。需要核实网页版邮件能否无人值守地发出它。 |
| **已批准的桌面邮件应用** | 托管的 Computer Use 策略拒绝该应用，或邮件服务拒绝为该应用中的账户投递。 | 新收件人需要审批，即使应用已经打开。Computer Use 是否会在 Send 处提示，尚未核实。 | 「Always allow」让 dot 可以重新打开该应用。周五的发送仍需要自己的长期指示。需要在委派任务中核实无人值守投递。 |

- **适用于所有路径的企业要求**。如果你的组织禁止对外投递，就在邮件服务中为每个发送账户强制执行该限制，或禁用每一条能够发送的路径。如果必须有人批准每一封对外邮件，请核实每条已启用的路径都会在投递前暂停，包括在浏览器会话或桌面审批已经处于活动状态时。成员的一条自定义规则或一次成功的插件测试，本身并不能证明覆盖到位。
- **验证**。在每条路径上使用同一个测试邮箱和一次性消息。尝试一个被禁止的收件人、一个新的但被允许的收件人，以及获授权的周五发送。记录是哪项控制起了作用、是否有人批准了发送，以及邮件服务是接受还是拒绝。在批准该工作流程之前，核实每条已启用的浏览器和桌面路径的逐次发送行为。
- 见[应用权限](https://help.openai.com/en/articles/20001495-managing-app-permissions-in-chatgpt)、[云浏览器会话](https://learn.chatgpt.com/codex/dots/computers-and-apps)、[Computer Use 审批](https://learn.chatgpt.com/codex/computer-use)和 [Agent Security](https://learn.chatgpt.com/codex/enterprise/agent-security)。

## 检查浏览器、网络与设备访问

（界面示意：云端计算机工具；浏览器使用、网络访问和 computer use 各有独立开关。；Let agents use cloud computers；适用于 Work Cloud、dots 和团队自动化。；Use a browser；Allow network access；Allow computer use；示例云端计算机设置；开关位置仅说明一种工作区配置。）

### dot 的云端计算机

- **云端能力：** Use a browser 控制对 dot 云浏览器的访问。Allow network access (code and shell) 控制命令的互联网访问。Allow computer use 控制与桌面应用的交互。Agent Security 中的站点规则将会让管理员在 dot 的云浏览器中允许或阻止域名，并按站点设置上传和下载权限。在允许的站点内，dot 的访问还取决于在那里登录的账户。
- **密码管理器：** 单独审查密码管理器的访问。即使 ChatGPT Work 已禁用，云浏览器、网络和 computer use 控制也可以适用于 dots。关于能力设置，见[在 ChatGPT 工作区中管理 dots](https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces)。
- **本地防护：** dot 的云浏览器有自己的会话。在笔记本电脑上登录内部网站，或把笔记本连上 VPN，并不会把该会话或网络路径给云浏览器。
- **网络规则：** 例如，在笔记本电脑上为终端命令屏蔽某个主机名，限制的是那条命令路径。如果云浏览器、插件和网页搜索都可能到达同一目的地，要分别测试。见[把你的电脑和应用连接到 dot](https://learn.chatgpt.com/codex/dots/computers-and-apps)。禁用代码和 shell 的互联网访问本身，并不会禁用云浏览器或连接的应用。

### 云浏览器中的登录如何工作

云浏览器在 dots 中是可选功能。管理员可以通过关闭「Use a browser」来禁用它。

对于受企业 SSO 保护的网站，员工从 dot 的云浏览器登录。当 dot 提供私密登录表单时，检查网站地址，并在那里输入你的凭据和任何要求的验证码。该表单会把它们直接发送到云浏览器，不经过模型的视野。

如果该表单无法完成某个登录步骤，选择 **Open computer**，再选择 **Take over**。由你自己完成企业 SSO 和多因素认证（MFA）提示。应用打开后，选择 **Return control**，让 dot 用你已登录的账户继续。如果网站要求你再次验证，请在 dot 继续之前完成新的提示。

接管会让你控制云浏览器。如果企业 SSO 要求使用公司管理的设备，或通过公司 VPN 连接，云浏览器无法使用你笔记本电脑的设备状态或 VPN 连接来满足该要求。请让该策略继续生效。如果某个已批准的插件支持该任务，就用它，并使用获授权执行该操作的已连接账户。如果该任务只能在网站上完成，请在一台符合该策略的设备和网络上完成。

云浏览器保有自己的 cookie，与你设备上的浏览器分开。这包括用于在已保存会话中保持登录状态的授权令牌（如适用）。要退出某个网站并结束该已保存会话，在 Settings → Cloud browser → Browser data 中清除该站点的 cookie。

### 已连接的员工计算机

- **连接要求：** 管理员必须允许本地访问，成员必须连接该计算机。进行本地工作时，让它保持在线并让 ChatGPT 保持打开。让它离线会保留该连接。
- **消息渠道：** 成员可以通过消息渠道从另一台设备发送请求。如果成员已连接的计算机可用，dot 随后可以启动一个附带该计算机的新线程（原文在此处没有句号）
- **设备权限：** 摄像头、麦克风和屏幕访问还取决于已连接的计算机，以及设备设置中授予 ChatGPT 应用的权限。关于设备权限，见 [dots 隐私与安全常见问题](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs)。

## 审查记忆、保留与删除

- **保留的上下文：** dot 可以保存它通过已授权应用连接读到的信息，例如在 Slack 线程中分享的团队决定。断开该应用会停止通过该连接的未来读取。dot 已经保存的信息可能仍留在它的记忆中。
- **模型训练：** 企业数据默认不用于模型训练。即使在模型改进已关闭的情况下，也可能在有限情形下进行人工审查，包括与安全相关的情形。见 [dots 隐私与安全常见问题](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs)。
- **加密：** OpenAI 对你组织与 OpenAI 之间、以及 OpenAI 与其服务提供商之间的静态数据使用 AES-256 加密，传输中的数据使用 TLS 1.2 或更高版本加密。
- **保留：** 用下表查找每份副本的保留期限和删除步骤。关于记忆与删除，见 [dots 隐私与安全常见问题](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs)。
- **dot 上下文：** 移除工作区访问会保留 dot 的数据。删除 dot 也会在 30 天内删除它保留的上下文，包括私人研究笔记和后台研究线程历史。dot 拥有的备份也会在 30 天内删除。另行存储的 ChatGPT 对话和 Codex 线程、Space 中的文件、项目、已连接的存储或用户计算机上的文件，以及基于 dot 对话添加到 ChatGPT Memory 的信息，不会随 dot 一起删除。它们的所有者必须另行管理这些副本。
- **ChatGPT Memory：** dot 对话可能会贡献到 ChatGPT Memory。在 ChatGPT Memory 设置中管理共享的信息。移除信息时，要同时检查已保存的记忆和聊天历史。只删除一段对话可能让已保存的记忆留在原处。见 [ChatGPT 中的记忆](https://help.openai.com/en/articles/8590148-memory-in-chatgpt)。

### 按类别的数据保留

| **数据类别** | **保留策略** | **由谁、以什么方式启动删除** | **期限、剩余副本与例外** |
| --- | --- | --- | --- |
| dot 聊天、原生子智能体历史和定时任务 | 主 dot 在其存续期间保留自己的历史、配置和时间安排。 | 成员使用 Reset 删除自己的 dot，包括它的对话、已保存的记忆和时间安排。移除工作区访问会保留 dot 的数据。工作区管理员也可以删除 dot，包括在其所有者不可用时。 | dot 拥有的聊天、原生子智能体历史和定时任务在 dot 删除后 30 天内删除。 |
| dot 记忆、资料和私人研究笔记 | dot 在其存续期间保留自己的上下文，独立于 ChatGPT Memory 设置。后台研究可以从连接的来源保存私人笔记。 | 成员无法在保留 dot 的同时删除某条特定 dot 记忆或某个源自来源的研究笔记。要移除 dot 的上下文，成员可以删除 dot。 | 撤销来源访问会停止未来的访问，但可能让派生出的笔记继续留存。删除 dot 会在 30 天内移除它的私人研究笔记和 dot 拥有的备份。 |
| 后台研究线程 | 后台研究线程在 dot 存续期间保留与该 dot 相关的研究上下文。 | 删除 dot 也会删除它的后台研究线程及其保留的上下文。 | 后台研究线程历史及其 dot 拥有的副本在 dot 删除后 30 天内删除。 |
| ChatGPT Memory | ChatGPT 单独管理与 dot 对话所贡献的记忆，与 dot 自己的记忆分开。 | 成员在 ChatGPT 中移除已保存的记忆，并删除包含它的任何聊天。关闭共享会让 dot 已经收到的上下文留在原处。 | 删除 dot 会让另行保存的 ChatGPT 记忆留在原处。OpenAI 可能出于安全和调试目的，把[已删除保存记忆的日志](https://help.openai.com/en/articles/8590148-memory-in-chatgpt)保留最多 30 天。 |
| Space 文件 | 已保存的文件遵循企业工作区的保留策略。打开、下载或重新附加已有的 Space 文件[不会重启其保留期](https://help.openai.com/en/articles/20001052-using-library-to-manage-files-in-chatgpt)。 | 成员在 Space 中删除文件。合规管理员可以通过 Space API 删除它。文件也可以按工作区策略到期。 | Space 文件在 dot 删除后仍然存在。Space 删除后，永久移除会在 30 天内排期，例外是已经去标识化并解除关联的数据，或出于安全或法律义务而保留的数据。见下文「备份」。 |
| 缓存文件与 Outputs | dot 聊天可以保留 Space 文件的另一份副本。Space 的保留与删除控制适用于 Space 中的那份副本。 | 删除 Space 文件（即使从回收站删除）不会触发删除 dot 聊天缓存。没有确认可用的单独自助移除流程。 | Space 副本删除后，文件仍可能列在 Outputs 中。dot 拥有的缓存副本在 dot 删除后 30 天内删除。清除该列表的单独方式仍待确认。 |
| 云端计算机文件与浏览器状态 | dot 的云盘可以保留文件和浏览器状态。快照到期取决于工作区配置。 | 删除 dot 会删除它的云浏览器和计算机。 | dot 的云端计算机数据、磁盘、浏览器状态、快照和备份在 dot 删除后 30 天内删除。保存在别处的副本遵循其目的地策略。 |
| 云端计算机快照 | 在设有数据驻留或企业密钥管理（EKM）的符合条件工作区中，快照是短期的。在其他工作区中，快照可能在 dot 存在期间一直保留。 | OpenAI 会在符合条件的工作区中自动让快照到期。删除 dot 也会启动其云端计算机和快照的删除。 | 在没有自动到期的工作区中，客户无法请求提前清除。快照在 dot 删除后 30 天内删除。 |
| 备份 | Space 备份有单独的有文档说明的窗口。dot 拥有的备份在 dot 删除后 30 天内删除。 | 当 Space 文件被删除、到期或变为不活跃时，活动的 Compliance API 会停止返回它。平台管理备份到期。 | Space 备份可能再保留最多 30 天，出于安全或法律义务可更长。dot 拥有的备份在 dot 删除后 30 天内删除。 |
| 委派的 Work 与 Codex 线程 | 托管的 [Work](https://learn.chatgpt.com/codex/enterprise/chatgpt-work-cloud-security#data-handling-and-retention) 和 [Codex](https://learn.chatgpt.com/codex/auth#openai-authentication) 线程遵循工作区的保留策略。[仅设备上的记录](https://learn.chatgpt.com/codex/enterprise/chatgpt-work-local-security#data-handling-and-retention)遵循本地存储与备份策略。 | 工作区策略决定托管线程何时到期。关于 Codex Cloud，见[工作区保留指引](https://learn.chatgpt.com/codex/auth#openai-authentication)。删除 dot 会让它委派的 Codex 和 Work 线程保持原样。 | 在桌面应用中删除 Codex 聊天时，OpenAI 会安排在其系统内于 30 天内永久删除，遵循[已公布的例外](https://help.openai.com/en/articles/20001333-archiving-and-deleting-codex-chats-in-the-chatgpt-app)。Work Cloud 会安排把已删除的聊天在 30 天内永久删除，遵循[已公布的例外](https://learn.chatgpt.com/codex/enterprise/chatgpt-work-cloud-security#data-handling-and-retention)。 |
| Space 中的页面 | Space 页面会一直保留，直到有人删除；工作区聊天保留期不会让它们到期。 | 页面的[创建者或所有者](https://help.openai.com/en/articles/20001544-chatgpt-space-sharing-data-and-controls)可以把该页面及其子页面移到回收站。另行保存的附件要在其自己的位置删除。成员可以删除自己保存的 Space 文件。拥有[所需 API 权限](https://learn.chatgpt.com/codex/enterprise/chatgpt-space)的合规管理员可以删除符合条件的文件。 | Space 会在永久删除时、或在回收站中 30 天后清除页面。在 10 月 1 日推行之前被移入回收站的页面需要手动删除。删除页面会让另行存储的附件留在原处。 |
| 本地文件与连接应用的副本 | 设备或连接服务管理存放在那里的文件、消息和导出。 | 有删除权限的人在来源应用或设备上移除该项。组织管理任何另行保留的副本。 | 这些副本在 dot 删除后仍然存在。删除何时完成，由目的地的保留期、备份规则和任何保全措施决定。 |
| 合规日志与客户导出 | [合规日志平台](https://help.openai.com/en/articles/9261474-openai-compliance-platform-for-enterprise-and-edu-customers)把每个事件从创建起保留 30 天。下载的副本遵循接收系统的策略。 | 平台到期是自动的。你的组织在自己的系统中管理已下载副本的删除。 | 删除 dot 既不会抹去已发出的事件，也不会重启它们的计时。组织不能使用 Compliance API 抹去 OpenAI 的内部审计或安全日志。 |

### 访问变更与删除操作

| **操作或数据类别** | **会发生什么** | **管理员应当做什么** |
| --- | --- | --- |
| **断开一个应用** | 停止通过该连接的新访问。dot 保留其已有的上下文。 | 分别审查保留的上下文和其他副本。 |
| **关闭 ChatGPT Memory** | 停止与 dots 的共享记忆。dot 已经收到的任何上下文都会保留。 | 要移除 dot 已经收到的上下文，审查该 dot 的删除选项。 |
| **单条 dot 记忆** | 单条 dot 记忆无法删除。要删除 dot 的全部上下文，成员或管理员可以删除该 dot。ChatGPT 记忆在 ChatGPT 中另行管理。 | 对于 dot 拥有的上下文，成员或管理员可以删除整个 dot。另行保存的 ChatGPT 记忆在 ChatGPT 中管理。 |
| **重置/删除 dot** | 重置会移除该 dot、它的对话、dot 拥有的记忆和定时任务。 | 先阅读[删除说明](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)，并保存所需的证据。 |
| **文件与委派记录** | Spaces 文件、本地/外部文件、Codex 线程以及单独的 ChatGPT 对话，遵循其存放所在应用或工作区的保留策略。 | 在每个存储位置完成删除。 |
| **云状态、快照和备份** | 自动快照到期、云端计算机删除和 Space 备份保留各有独立的时间表。 | 对每份副本使用上文给出的期限。dot 拥有的备份在 dot 删除后 30 天内删除。 |

- **数据类别：** 对于涉及某条 Slack 消息的擦除请求，要定位原消息、任何引用或概括它的私人笔记，以及由它生成的任何报告。检查每份副本的删除路径。
- **已撤销的来源访问：** 改动来源系统的权限会限制未来通过该来源的访问；它不能证明已保留的上下文被删除。
- **隐私请求：** 在审查发现、更正和擦除需求时，要把客户和非用户的信息也包括在内。

## 审查消息传递与受众边界

- **Slack 身份：** 在离职处理期间，要同时检查 dot 的 Slack 身份和所有者的 Slack 插件连接。ChatGPT 和已启用的消息渠道到达的是同一个 dot。它们的对话相互独立，但[已保存的笔记与上下文](https://learn.chatgpt.com/codex/dots/tasks-and-memory#context-and-memory)可以为跨渠道的工作提供信息。
- **Slack 设置：** 检查工作区的通信权限以及任何所需的 Slack 应用审批。然后成员必须完成设置。关于 Slack 设置，见[管理 dots 权限与能力](https://learn.chatgpt.com/codex/enterprise/dots-admin-guide)。
- **受众可见性：** 任何有权访问该对话的人都能读到 dot 的帖子。dot 辅助的工作请使用内部 Slack 频道。我们建议只在组织内所有人都在的频道中使用 dot。这排除了与客户或合作伙伴共享的 Slack Connect 频道。**共享限制：** 举个例子，如果 dot 能读取一份私密的 HR 文档，在项目频道里贴出其中的薪资数字就会让所有能读该频道的人看到它们。在批准发帖之前，要指明 dot 可以分享什么，并确认频道里每个人都有权看到它。

## 收集审计证据并保护导出

### 为你的任务选择合适的报告

- **调查与报告：** 调查用[合规记录](https://learn.chatgpt.com/codex/enterprise/compliance-api)，采用情况的报告用 [Analytics API](https://learn.chatgpt.com/codex/enterprise/analytics-api) 数据。
- **用量指标：** 用量计数不会显示是谁授权了某个操作，也不会说明它是否成功。

### 追踪一项操作

1. **找到该操作。** 找到成员的提示和 dot 的回复，然后检查工具或插件事件。对于 Slack 发送，把插件结果与目标频道中的消息作对比。
2. **匹配记录。** 使用用户和工作区标识符定位记录。归因于 dots 的记录使用 `client_id = DOTS`，并在可用时包含 dot 元数据。用接收服务的日志检查结果。
3. **追踪委派的工作。** 对于委派的工作，查找父线程和任务 ID。记录任何缺失或被遮蔽的字段，因为它们会让你无法追踪该操作。
4. **检查目的地。** 工具记录可以指明请求执行的命令或浏览器操作。要核实目的地实际被访问到，请与那条路径的代理或网关日志作对比（如有）。本地 OpenTelemetry 收集器覆盖受支持的本地执行事件。云端编排不在该收集器覆盖范围内。关于受支持的记录，见[管理 dots 权限与能力](https://learn.chatgpt.com/codex/enterprise/dots-admin-guide)。

### 阅读当前的 Compliance API 记录

| **活动** | **要查找什么** | **该记录告诉你什么** |
| --- | --- | --- |
| 云浏览器或计算机 | TOOL\_CALL\_SUGGESTED | 指明 dot 尝试使用的工具。即使 status=completed，详细的输出也可能缺失。 |
| 连接的应用（插件） | APP\_MCP\_CALL 和 APP\_MCP\_RESULT | 该调用标明工具名称。结果报告成功或错误，并可能包含输出预览或错误详情。 |

Compliance API 导出包含用户提示、dot 回复、工具调用请求与响应，以及后台活动。要调查某个操作，请关联可用的记录，并检查连接的服务以核实外部效果。部分链接和结果可能不在导出中。

**更详细的云活动审计日志。** 我们正在为 dots 和其他在云端运行的智能体开发更详细的 Compliance API 记录。我们的目标是帮助安全团队跟进智能体在任务中走过的步骤，包括它调用了哪些工具和连接的应用，以及某个操作何时经过了自动审查。我们也在探索如何展示这些工具返回了什么，以及云浏览器访问了哪些网站。

### 保留并保护导出

- **保留期：** [合规日志平台](https://help.openai.com/en/articles/9261474-openai-compliance-platform-for-enterprise-and-edu-customers)把记录保留 30 天。如果你需要保留更久，就要持续导出所需的记录。
- **导出访问：** 限制谁可以读取导出及其密钥。导出中可能包含员工的消息或插件结果的预览。把你自己的保留、电子取证和法律保全规则应用到系统实际收到的记录上。另行确认保全是否覆盖原始聊天、文件或 dot 笔记。
- **日志权限：** 广泛的合规访问权限和对话消息权限需要工作区所有者授予。所有者或管理员可以授予受支持的较窄日志权限。

## 停止工作、撤销访问并处理离职

当拥有个人 dot 的员工（dot 所有者）已经离职或无法协助时，使用此流程。ChatGPT 工作区所有者或工作区管理员从自己的账户操作。如果活动仍在继续，或你无法确认敏感工作已经停止，请立即[提交 OpenAI 支持工单](https://help.openai.com/en/articles/6614161-how-can-i-contact-support)，同时继续执行下面的步骤。

- **如果员工已离职，移除工作区访问。** 工作区所有者或工作区管理员可以移除手动管理的成员。对于由目录管理的成员，请让你的身份管理员[移除工作区分配](https://help.openai.com/en/articles/10011769-scim-provisioning-and-management)，并在同步后核实该员工不再是活动成员。成员资格移除后，工作区访问即结束。dot 的遏制情况要另行核实：运行中的工作可能在 dot 撤销后完成，而移除成员对每个进行中和委派任务的影响需要确认。
- **如果员工需要保留工作区访问，撤销 dots 访问。** 工作区所有者可以在工作区设置 → 权限与角色中查看 [Use dots (Beta)](https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces)。检查工作区默认设置、直接分配的角色和群组角色。任何剩余的授予都可能让 dots 保持启用。改动共享授予之前，先检查还有谁依赖它。
- **在管理控制台中查找该员工的智能体。** 工作区管理员（包括所有者）可以查看用户的智能体，并暂停或删除某个 dot。
- **暂停该 dot。** 这会阻止它开始新工作，包括它自己的定时运行。如果该 dot 已经在独立的 Work 或 Codex 线程中启动了任务，该任务可以继续运行。要停止它，需单独取消那个任务。也要检查该 dot 创建的任何独立时间安排。
- **恢复该 dot。** 只有管理员才能恢复被管理员暂停的 dot。恢复后，之前的会话会再次响应消息；委派的工作不受影响。
- **撤销 dots 访问。** 当前运行中的工作可以完成，新消息不会触发模型操作，时间安排会暂停。移除工作区成员资格的影响要另行核实。
- **删除该 dot。** 删除不可恢复，因此请先保存所需证据。删除 dot 会删除它的云浏览器和计算机，但不会移除用户级插件。
- **撤销已连接的账户和会话。** 请相关服务的管理员撤销应用授权，并在受支持时终止 dot 的云浏览器所使用的网站会话。对于 Slack，要同时检查 dot 自己的身份和该员工的[已连接 Slack 账户](https://learn.chatgpt.com/codex/enterprise/dots-admin-guide)。请设备管理员限制对任何已连接计算机的访问，并检查是否已有本地工作在运行。在签发撤销的服务中逐项核实。
- **核实活动。** 运行中工作的状态可以在 Compliance API 中查询，报告的 p95 为 30 分钟。定时工作的状态可以在下一次计划运行后 30 分钟查询。这些是报告时延，不是立即停止的保证。已完成的操作要到接收服务中检查。
- **联系支持。** 从你自己的账户打开 help.openai.com 的聊天窗口。支持人员可以指导用户或管理员停止 dot；他们不能直接对客户工作区中的 dots 采取操作。请提供工作区 ID、员工邮箱、可用的 dot 或任务标识符、已采取的步骤、带时区的时间戳，以及最后观察到的活动。

## 相关资源

- 关于访问、审批、记忆和删除，查阅 [dots 隐私、安全与安全常见问题](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs)。
- 关于当前设置与权限，见[在 ChatGPT 工作区中管理 dots](https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces)。
- 关于配置、使用和合规指引，见[管理 dots 权限与能力](https://learn.chatgpt.com/codex/enterprise/dots-admin-guide)。
- 关于本地访问的资格与防护，见[Work Cloud 和 dots 的本地计算机访问](https://learn.chatgpt.com/codex/enterprise/cloud-local-access)。
- 关于委派 Work 任务的控制，见 [ChatGPT Work 云安全](https://learn.chatgpt.com/codex/enterprise/chatgpt-work-cloud-security)。
- 关于策略要求与执行设置，见 [Agent Security](https://learn.chatgpt.com/codex/enterprise/agent-security)。
- 关于合规记录与导出的访问，见 [Compliance API 与审计事件](https://learn.chatgpt.com/codex/enterprise/compliance-api)。
