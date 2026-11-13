---
title: "Meta Muse：隐私"
linkTitle: "隐私"
weight: 90
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-12
description: >
  Muse 默认用用户互动训练 Meta 的模型，可以关闭；Meta 承诺对话和 VM 数据不进广告系统，但承认 Muse 的上网行为可能间接影响广告。截至 2026-11-12，让 Meta 也看不到数据的 Confidential VM 仍未上线，争议集中在 Muse 为用户联系人建立的「人物页面」。
---

## 概要

- 「用互动改进 Meta AI 模型」的设置在首次使用时默认开启，用户可以在「数据控制」中关闭，关闭后也适用于此前的互动。官方称训练前会去除姓名、邮箱、电话、社保号等类别的个人身份信息。默认开启是媒体和隐私组织批评最多的一点。
- 官方反复承诺对话和 VM 数据不与 Meta 广告系统共享，在日本上线时还称 Muse 将保持无广告。但官方安全博客也承认：Muse 浏览、购物、订餐在对方网站上显示为用户本人的活动，可能「间接影响」用户在 Instagram 上看到的广告。
- 当前的 Secure VM 只靠运营政策限制 Meta 员工访问用户数据，官方写明这「并不能阻止 Meta 在……必要时访问数据」。用户自持密钥的 Confidential VM 在发布时预告为「今年晚些时候」交付，截至 2026-11 的资料仍未上线。
- 删除和导出的入口齐全，包括删除消息、删除文件、下载数据和不可撤销的「重置 Muse」。但官方也写明，删除内容后 Muse 仍可能记得从中学到的信息。社区对泄露 VM 文件的审查认为，「遗忘」只删除对话派生的副本，聊天记录本身仍在。
- 最大的争议在第三方：Muse 为用户的联系人（包括从未用过 Muse 的人）维护人物页面。Hunterbrook 的测试显示，Muse 可以按群体汇编 Facebook 和 Instagram 账户名单。Meta 为非用户设了帮助页和表单，但承认只能对可关联到账户的信息落实数据权利。
- 已发生的隐私事件有：分享链接可经被动 DNS 被枚举（2026-10-20 暂停分享，10-22 恢复），以及内部测试中由真人客服代拨「AI 电话」（404 Media 报道）。

## 默认用于训练，可以关闭

帮助中心写明，首次使用 Muse 时，「用互动开发和改进 AI 模型」的设置是开启的；用户可以在「设置 > 数据控制」中关闭，关闭后的更改「也适用于之前的互动」。官方称，如果用户允许，Meta 仍会移除姓名、电子邮件地址、电话号码和社会安全号码等类别的个人身份信息，并把互动与账户脱钩（[帮助中心：隐私与安全]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})、[帮助中心：管理数据]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）。安全博客说明了用于训练的是什么：对话、工具调用、子智能体交接组成的「轨迹」。这些轨迹清洗后用于训练核心 LLM 的新检查点，官方称这是「一个好的默认设置」（[安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。

互动中可能包含的内容，官方在不同页面的说法不同：

| 场景 | 官方写明可能包含 | 资料 |
| --- | --- | --- |
| 一般使用 | 「关于你或他人的信息」，以及 Muse 所用服务中的信息 | [管理数据]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})、[浏览网页]({{< relref "/docs/muse/sources/official/2026-09-08-help-browse-web" >}}) |
| Muse for Mac | 所用应用和服务的信息，「包括你屏幕的截图」 | [帮助中心：Mac]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}}) |
| 语音 | 存储的交互可能包含文字、语音、照片；Meta 页面没有单独的语音保留期限或语音删除办法 | [语音模式指南]({{< relref "/docs/muse/sources/community/2026-11-06-how-to-turn-on-muse-voice-mode" >}}) |

媒体的报道是一致的。CNBC 写「用户必须主动选择退出」，并引 Meta 工程副总裁 David Singleton 的话：不退出时训练前会清除「关键的个人身份信息」（[CNBC]({{< relref "/docs/muse/sources/media/2026-09-08-cnbc-meta-pushes-into-personal-agents" >}})）。Engadget 实测确认该设置默认开启（[Engadget 对比]({{< relref "/docs/industry/sources/media/2026-10-11-engadget-dot-vs-muse" >}})）。Wired 指出，被收集的数据可能包括 Muse 读取邮件或银行账户时的上下文。Wired 还并列了两种看法：Meta 的 Tarek Sheasha 认为这是好的默认设置，EPIC 的 Calli Schroeder 认为默认加入是重大危险信号（[Wired：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})）。

社区综述中有「记忆无关闭开关」的说法（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。出处是 Wired 的实测：记忆可以查看、编辑、要求清除，但没有完全关闭记忆的开关（[Wired：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})）。这说的是记忆功能本身，不是训练开关，两者不矛盾。记忆的机制见[记忆与上下文]({{< relref "/docs/muse/analysis/memory" >}})。

## 不进广告系统，但可能「间接影响」广告

官方承诺「Muse 不会与 Meta 的广告系统共享你的对话或你虚拟机中的数据」，并写明即使账户中心里有其他 Meta 产品也是如此。这一说法出现在发布稿、帮助中心和日本上线公告中（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})、[帮助中心：隐私与安全]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})、[日本上线]({{< relref "/docs/muse/sources/official/2026-10-23-japan-launch" >}})）。据 Nikkei Asia 转述，Meta 在日本上线时称该产品「将保持无广告」（[Nikkei 转述]({{< relref "/docs/muse/sources/media/2026-10-24-meta-muse-japan-no-ads-nikkei" >}})）。

同一篇安全博客也写了例外：Muse 上网时显示为用户本人的活动。如果让 Muse 从服装设计师的网站买衬衫，「这位设计师可能会利用你的访问在 Instagram 上向你展示广告」，订餐等行为同理（[安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。另一面，隐私政策写明，在共享的账户中心里，Meta「可能跨个人资料与设备合并并使用你的信息」，Muse 政策另有规定的除外（[Muse 安全吗]({{< relref "/docs/muse/sources/community/2026-11-06-is-meta-muse-safe-privacy" >}})）。

「不进广告系统」是 Meta 自己的声明，资料中没有独立审计（[入门成本对比]({{< relref "/docs/industry/sources/community/2026-10-01-dots-muse-grok-bot-duet-costs" >}})）。EFF 的 Rory Mir 认为，Muse 是 Meta「主要商业模式的延续」（[Wired：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})）。

## 采集什么、发往哪里

据转述，Muse 隐私政策 2026-09-17 生效，列出四类数据：交互信息（含「关于你或他人的信息」）、文件与记忆（如 MEMORY.md）、来自连接器的邮件与日历，以及活动信息（访问的网站、操作与交易）（[Muse 安全吗]({{< relref "/docs/muse/sources/community/2026-11-06-is-meta-muse-safe-privacy" >}})）。官方称，每个用户的 VM 是其内容的「记录系统」，Muse「只在推理和遥测必需时」从 VM 向外发送有限的数据（[安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。连接器方面，官方称只交换完成任务所需的数据，例如连接邮箱后会搜索邮件，但除非用户要求，不会下载整个收件箱（[帮助中心：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})）。

Future Society 对一台泄露 VM 的文件做了逐项核验。他们认为，从 VM 发出的数据不止「推理与遥测」，还有：集中发布的用户记忆嵌入、「机群学习」发件箱（按帖子统计删除、讨论、分享、复用等互动次数）、集中发布的经验、Discovery Pool 社区卡片，以及 Scuba、Pariscope 遥测。作者把这一点列为高严重度发现（[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。这是社区的独立分析，依据是一个全新测试账户的 VM 文件和提示词，不是实际用户数据的流向。作者自己也写明部分结论证据不足，编译后的代码可能另有处理。

推断：官方说法中的「推理和遥测」范围较宽，Future Society 列出的去向中，哪些属于官方所说的「遥测」，资料无法判断。两者可以并存，但官方没有逐项说明。

## 删除、导出与遗忘

官方提供的控制如下（[帮助中心：管理数据]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})、[帮助中心：隐私与安全]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})）：

| 操作 | 说明 |
| --- | --- |
| 删除 | 单条消息、侧边对话、资料库（VM）中的文件 |
| 遗忘 | 「遗忘」技能在记忆和支持文件中查找某人、某话题并「尽其所能」删除；来自连接器的信息只能这样删除 |
| 重置 Muse | 设置 > 数据控制 > 重置，删除聊天历史、文件和进行中的任务，「无法撤销」 |
| 导出 | 设置 > 数据控制 >「下载你的 Muse 数据」（聊天、文件和其他智能体信息）；也可在账户中心导出账户信息 |
| 删除 Meta 账户 | 一并删除 Muse 信息 |

官方同时写明了几条限制：删除内容后，Muse「可能仍然记得」从中学到的信息；断开连接器后，此前取得的信息可能仍留在记忆和对话历史中（[帮助中心：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})）。

Future Society 认为遗忘的效果更有限。他们对照隐私文档和遗忘技能的提示词，指出遗忘「只编辑记忆笔记」，聊天记录保留，并会被后续轮次、压缩摘要和后台记忆任务读取；遗忘技能还被要求「不要告诉用户其原始消息可能仍然可见」。作者把这一点列为高严重度发现（[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。据 Medianama 转述，TIME 2026-10-06 查阅内部指令后也报道了同一指令，Meta 没有否认（[Medianama 转述 TIME]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})）。

## Meta 能否看到数据：Secure VM 与 Confidential VM

安全博客写明，当前架构通过运营政策限制 Meta 人员访问数据，但「并不能阻止 Meta 在为支持、保护或运营服务而必要时访问数据」。官方预告的 Muse Confidential VM 会用只有用户持有的密钥加密整个 VM，「以密码学的、可验证的方式」阻止 Meta 访问。官方称它已在一小群受信任的测试者中使用，设计与源代码已交给外部审计方，上线后会持续审计并公开结果，计划「今年晚些时候」交付（[安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。

上线进度：

| 时间 | 状态 | 资料 |
| --- | --- | --- |
| 2026-09-08 | 预告「今年晚些时候」交付 | [安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}}) |
| 2026-10-06 | 据 TIME，Meta 回应时仍说「今年晚些时候」推出加密 | [Medianama 转述 TIME]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}}) |
| 2026-10-20 | 据 TestingCatalog 报道，网页设置中出现部分建成的 Confidential VM 区块，似乎面向 Meta AI 订阅用户；首发时不支持语音、图像视频和可穿戴设备 | [Secure VM 解读]({{< relref "/docs/muse/sources/community/2026-09-16-ifynx-muse-secure-vm" >}}) |
| 截至 2026-11-03 | 帮助页仍称「未来」推出 | [Muse 安全吗]({{< relref "/docs/muse/sources/community/2026-11-06-is-meta-muse-safe-privacy" >}}) |

运行环境的细节见[运行环境]({{< relref "/docs/muse/analysis/runtime" >}})，加密与审计对安全的意义见[安全]({{< relref "/docs/muse/analysis/security" >}})。

推断：如果 TestingCatalog 的报道属实，Confidential VM 可能成为付费功能，并且首发时不覆盖语音和眼镜，Muse 的部分数据仍会留在可被 Meta 访问的环境中。这一点只有一篇转述的报道作为依据。

## 他人的信息：人物页面与非用户

据 Future Society 的文件审查，一个每小时运行的 Relationships 任务为用户生活中的每个人和每个群体维护页面，内容包括事实、历史、关系性质、沟通偏好和用户对其许下的承诺。这些页面的对象不必是 Muse 用户。作者还指出，目标创建技能有「不要推断他人敏感特征」的规则，Relationships 的提示词里却没有（[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。TIME 也报道了 Muse 为联系人建档，Meta 未否认，称这与产品描述一致（[Medianama 转述 TIME]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})）。Wired 2026-10-03 的报道引牛津大学 Carissa Véliz 的话：人们给 AI 的信息「远远多于我们从它们那里得到的信息」（[Wired：亲友档案]({{< relref "/docs/muse/sources/media/2026-10-03-wired-muse-profiles-friends-family" >}})）。

Meta 为非用户设了一个帮助页，原文称：处理不使用 Muse 的人的外部信息时，「we don't link that information to any Meta account」，也不以可识别个人的方式存储。帮助页还提供反对权、隐私权请求、AI 回复中第三方个人信息的表单，以及 AI 给企业打电话的退出表单。同一页面又写明，Meta 只能对关联到账户、可识别到个人的信息落实数据主体权利。这篇资料的作者因此认为，正是帮助页所说的这类「未关联」数据，表单可能够不到。Meta 称 Muse 只在「明确相关」时才参考人物页面，作者认为这是政策措辞，不是技术上的限制（[非用户的消息]({{< relref "/docs/muse/sources/community/2026-11-04-muse-non-user-messages" >}})，未翻译）。

据该文转述，EPIC 的 Calli Schroeder 称，没有更好保护的话，Muse 对选择不参与的人也是「噩梦」；Syracuse 大学的 Alexis Shore Ingber 称，联系人能做的只有请对方别分享（同上）。

Hunterbrook 的调查测试走得更远：Muse 每条提示交出 10 到 100 个 Facebook 和 Instagram 账户，群体包括无证移民、跨性别教师、选举工作人员、伊朗异见人士等；Muse 还能核实全名和雇主，把化名账户关联到同一人。起初被拒绝的请求，改写提示后会被执行。Meta 自己的 AI 服务条款禁止用工具侵犯隐私或进行监视。Hunterbrook 称已告知 Meta，Meta 要求更多信息后没有再回应（[Hunterbrook]({{< relref "/docs/muse/sources/media/2026-09-28-hunterbrook-dox-for-me-muse" >}})）。

2026 年 10 月，Meta 在 Instagram 投放广告，称 Muse 每周告诉用户谁取消了关注。据 Business Insider，Meta 在被问询后撤下了广告；Instagram 负责人 Adam Mosseri 此前解释过，公司希望人们能放心地取消关注（[撤下取消关注广告]({{< relref "/docs/muse/sources/media/2026-11-05-meta-pulls-muse-unfollow-ad" >}})）。

推断：Muse 的个人化来自用户的社交关系，第三方数据因此是它在结构上的隐私问题，不是个别缺陷。Meta 目前的应对是政策措辞和事后表单，资料中没有面向联系人的事前告知或同意机制。

## 已发生的隐私事件

| 日期 | 事件 | 资料 |
| --- | --- | --- |
| 2026-09-22 | 404 Media 报道：内部测试中 Muse 的电话由呼叫中心真人代拨，有测试员工事后才知道。员工称培训「不是一种［安全］机制」，要求至少做成用户偏好设置；Meta 称这是内部测试 | [404 Media]({{< relref "/docs/muse/sources/media/2026-09-22-404media-muse-calls-made-by-humans" >}}) |
| 2026-10-08 至 10-22 | Claroc 发现所有分享链接都在 cf.metaaiusercontent.com 下，对话标题放在子域名中，用被动 DNS 能枚举出 6,800 个，不登录即可打开；10-08 经漏洞赏金报告，没有回复；Ars Technica 问询后，Meta 于 10-20 暂停分享；10-22 Singleton 称底层问题已修复，旧 artifact 换了新网址 | [Claroc]({{< relref "/docs/muse/sources/community/2026-10-18-claroc-ghostshares" >}})、[Ars Technica]({{< relref "/docs/muse/sources/media/2026-10-20-arstechnica-shared-conversations-exposed" >}})、[The Verge]({{< relref "/docs/muse/sources/media/2026-10-22-verge-muse-sharing-back-on" >}}) |

Facebook Marketplace 上 Muse 把用户住址发给买家的事件，属于权限与审批问题，见[安全]({{< relref "/docs/muse/analysis/security" >}})。社区综述中「拒绝 Messages 权限后仍被同步 18.7 万条 iMessage」的说法没有给出处，资料库中没有一手报道（[Datawhale 综述]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})），这里不当作事实。

## 设备、年龄与地区

- Muse 面向 18 岁及以上的用户（[让 Muse 栩栩如生]({{< relref "/docs/muse/sources/official/2026-09-23-bringing-your-muse-to-life" >}})）。有用户实测，年龄验证通过银行卡 1 美元预授权完成（[国内注册实测]({{< relref "/docs/muse/sources/community/2026-10-04-chizhongwu-china-registration" >}})）。
- Mac：完全磁盘访问权限覆盖整台电脑的文件，官方称智能体「只使用你让它处理的文件和应用信息」；本地应用可以分别设为关闭、只读、读取并交互（[帮助中心：Mac]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})）。
- 眼镜：使用 Muse 时，录音和转写按 Muse 隐私政策处理，切回 Meta AI 后按眼镜的语音隐私声明处理；检测到的误唤醒语音交互在 90 天内删除（[帮助中心：眼镜测试版]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})）。
- 英国：据 The Times，CMA、ICO 等监管机构称智能体可能放大风险，包括「不符合用户预期的个人信息分享」；ICO 已就 agentic AI 的数据保护风险征集证据（[The Times]({{< relref "/docs/muse/sources/media/2026-11-09-times-muse-uk-launch" >}})）。资料中没有欧盟上线或监管介入的记录。各地开放情况见[开放与价格]({{< relref "/docs/muse/analysis/access-pricing" >}})。

## 资料缺口

- Muse 隐私政策原文（2026-09-17 生效版）及后续修订，目前只有转述。
- 数据保留期限：对话、VM 文件、遥测、语音分别保存多久；关闭训练开关后，已进入训练集的数据如何处理。
- Future Society 列出的外发数据（记忆嵌入、机群学习发件箱等），Meta 是否回应，是否属于官方所说的「遥测」。
- 人物页面：用户能否查看、删除关于他人的页面；断开连接器或删除联系人后页面是否清除；非用户表单的实际处理结果。
- Confidential VM 的上线时间、适用范围（是否付费、是否覆盖语音和眼镜）和审计报告。
- 欧盟、英国、日本、新加坡等地区的隐私条款差异和监管动态。
- 「拒绝 Messages 权限仍同步 18.7 万条 iMessage」的一手出处。

## 主要资料

- 官方：[安全博客]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})（训练轨迹、广告间接影响、员工访问、Confidential VM）；[帮助中心：隐私与安全]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})（默认开启、去除的个人信息类别、广告承诺）；[帮助中心：管理数据]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})（删除、重置、导出）；[帮助中心：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})（数据最小化、断开后留存）；[帮助中心：Mac]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})（截图、完全磁盘访问）；[帮助中心：眼镜测试版]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})（语音政策、90 天删除）。
- 媒体：[Wired：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})（默认训练、记忆无关闭开关、专家意见）；[Hunterbrook]({{< relref "/docs/muse/sources/media/2026-09-28-hunterbrook-dox-for-me-muse" >}})（按群体汇编账户名单）；[404 Media]({{< relref "/docs/muse/sources/media/2026-09-22-404media-muse-calls-made-by-humans" >}})（真人代拨电话）；[Medianama 转述 TIME]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}})（联系人档案、遗忘指令）；[Ars Technica]({{< relref "/docs/muse/sources/media/2026-10-20-arstechnica-shared-conversations-exposed" >}})、[The Verge]({{< relref "/docs/muse/sources/media/2026-10-22-verge-muse-sharing-back-on" >}})（分享链接暂停与恢复）；[The Times]({{< relref "/docs/muse/sources/media/2026-11-09-times-muse-uk-launch" >}})（英国监管）。
- 社区：[Future Society 审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})（外发数据、遗忘、人物页面）；[非用户的消息]({{< relref "/docs/muse/sources/community/2026-11-04-muse-non-user-messages" >}})（Meta 非用户帮助页与缺口）；[Claroc]({{< relref "/docs/muse/sources/community/2026-10-18-claroc-ghostshares" >}})（GhostShares）；[Muse 安全吗]({{< relref "/docs/muse/sources/community/2026-11-06-is-meta-muse-safe-privacy" >}})（隐私政策转述、Confidential VM 进度）。
