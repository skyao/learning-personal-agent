---
title: "Meta Muse：隐私"
linkTitle: "隐私"
weight: 90
analyzedAt: 2026-11-28
sourcesUntil: 2026-11-28
description: >
  Muse 默认用交互训练模型，承诺不把对话和虚拟机数据交给广告系统，但购物和浏览仍会间接影响广告；Meta 人员目前能在必要时访问数据，承诺的 Confidential VM 截至 11 月仍未上线。他人信息（人物页、Messages 同步、邮件、Signal 通知）是争议最集中的部分，11 月起已引来美国多州调查和英国监管的事前介入。
---

## 概要

- **训练默认开启。** 「帮助改进我们的 AI 模型」在首次使用时开启，可以在「设置 > 数据控制」中关闭，关闭也适用于此前的交互。Meta 称训练前会移除姓名、邮箱、电话等类别的个人身份信息，但没有独立审计；退出也无法从已训练的权重中撤回数据。2026-11-24 的英国稿首次写明不用含私人消息的交互训练，这与 11-16 邮箱帮助页的说法不一致。
- **不进广告系统，但会影响广告。** 官方承诺对话和虚拟机数据不与广告系统共享。同时官方也承认，Muse 代用户购物、订餐会「间接影响」广告。到 11 月下旬，Meta 已在美加测试让 Muse 跟进用户看到广告之后的行为；据 CNBC 报道，用户通过智能体买什么，是 Instagram 广告投放的「宝贵资产」。
- **Meta 能看到数据。** 现有架构只靠运营政策限制 Meta 人员访问，不阻止「必要时」访问；对话不是端到端加密。只有用户持有密钥的 Muse Confidential VM 从 9 月起就称「今年晚些时候」推出，截至资料所见的 11 月仍未上线。
- **他人信息是最大的隐私争议。** 争议有以下几类：
  - 为用户生活中每个人每小时更新的人物页；
  - Mac 应用同步约 18.7 万行 iMessage；
  - 转发进 @muse.ai 邮箱的第三方邮件；
  - 经通知权限读到的 Signal 消息；
  - 以用户身份发出、对方不知是 AI 的消息和电话。

  非用户没有查看或删除的入口。Meta 在 11 月补充说明：非用户的信息不与 Meta 账户关联。
- **监管从 11 月起介入。**
  - **美国：** 蒙大拿州 2026-11-23 牵头多州调查，起因是路透社 11-18 的报道。
  - **英国：** 上线前，CMA 促成了条款修改，ICO 与 Meta 达成自愿监测与报告安排；FCA 则称 Meta 拒绝了联合沙盒测试。

## 训练：默认开启，可退出，不可撤回

官方帮助页写明，这项设置「你首次使用 Muse 时，这项设置是开启的」，关闭路径是「设置 > 数据控制」。设置的更改也适用于此前的互动。保持开启时，Meta 会移除姓名、邮箱、电话号码、社会安全号码等类别的个人身份信息，并与账号脱钩（[帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）。

安全博文把对话、工具调用和子智能体交接统称为「轨迹」，称清洗后用于训练新检查点，并称这是「好的默认设置」（[我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。发布稿只写「可以选择不让自己的互动被用于训练」，没有提默认开启（[推出 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-introducing-muse" >}})）。默认开启这一点，有以下几方实测或核实过：

- 媒体：Engadget、WIRED、CNBC、ITmedia（[Engadget：Muse 上手指南]({{< relref "/docs/muse/sources/media/2026-09-12-engadget-getting-started-muse" >}})、[WIRED：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})、[CNBC：Muse 发布报道]({{< relref "/docs/muse/sources/media/2026-09-08-cnbc-meta-pushes-into-personal-agents" >}})、[ITmedia 入门解说]({{< relref "/docs/muse/sources/media/2026-11-22-itmedia-muse-explainer" >}})）；
- 社区用户（[社区用户]({{< relref "/docs/muse/sources/community/2026-10-09-ugoearn-five-task-types" >}})）；
- 马恩岛信息专员（[信息专员谈代理式 AI]({{< relref "/docs/muse/sources/community/2026-11-27-isle-of-man-commissioner-agentic-ai" >}})）。

批评集中在三点：

- **默认开启本身。** EPIC 的 Calli Schroeder 认为默认选择加入是重大危险信号（[WIRED：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})）。
- **去标识化的范围。** 政策点名的类别用「如」列举，清单是开放的，其余信息只与账户解除关联；作者推断，企业的毛利、供应商银行账号等不在去标识化之列（[账本训练模型与三层退出开关]({{< relref "/docs/muse/sources/community/2026-10-19-muse-small-business-data-trains-models" >}})）。
- **退出的效果。** 连接器带来的信息也是「互动」的一部分，受同一个开关控制（[帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})、[账本训练模型与三层退出开关]({{< relref "/docs/muse/sources/community/2026-10-19-muse-small-business-data-trains-models" >}})）；退出只停止今后的使用，已经训练进权重的数据无法抽出（[删除聊天记忆仍在]({{< relref "/docs/muse/sources/community/2026-10-28-muse-delete-chat-memory" >}})）。

私人消息与邮件的口径有变化：

| 日期 | 资料 | 说法 |
| --- | --- | --- |
| 2026-11-12 | ITmedia 转录的应用设置页 | 智能体收发的邮件属于对话的一部分，可能用于改进 Meta 的 AI（[Muse 邮箱日本可用]({{< relref "/docs/muse/sources/media/2026-11-12-muse-mail-japan-itmedia" >}})） |
| 2026-11-16 | 邮箱帮助页 | 发往 @muse.ai 的邮件「可能根据你的设置」用于开发和改进 AI 模型（[帮助：Muse 邮箱地址]({{< relref "/docs/muse/sources/official/2026-11-16-help-email-addresses" >}})） |
| 2026-11-24 | 英国上线控制权稿 | 「不会使用包含你私人消息（例如电子邮件或 Instagram 私信）的交互」训练模型（[英国上线与控制权]({{< relref "/docs/muse/sources/official/2026-11-24-muse-you-stay-in-control" >}})） |

资料没有说明英国稿的说法是全球政策变更还是英国专有条款。

## 广告：数据隔离，影响不隔离

官方的承诺是：对话和虚拟机内的数据不与广告系统共享，即使账户中心里有其他 Meta 产品（[帮助：隐私与安全]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}})、[Muse 登陆英国]({{< relref "/docs/muse/sources/official/2026-11-24-introducing-muse-in-the-uk" >}})）。同一篇安全博文也写明，Muse 浏览网络时表现为用户自己的活动，代订餐厅、在 Marketplace 找商品「也可能间接影响你看到的广告」（[我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。Chrome 扩展的说明更进一步：Muse 访问的网站可能把活动归到用户名下，并影响 Meta 产品内外的广告和推荐（[Muse Chrome 扩展]({{< relref "/docs/muse/sources/media/2026-11-13-muse-chrome-extension" >}})）。

11 月下旬的资料显示，广告与 Muse 的连接在加深：

- **MediaPost：** Meta 在美国和加拿大对已下载 Muse 的用户小范围测试，让 Muse 跟进用户看到广告之后的行为，包括「稍后保存、设置提醒、购买或填写表单」（[Muse 跟进广告后行动]({{< relref "/docs/muse/sources/media/2026-11-24-mediapost-muse-post-ad-actions" >}})）。
- **CNBC：** Meta 引导用户把 Instagram 收藏整理进 Muse；报道写道，用户用智能体买什么的信息「是让 Instagram 内的广告投放更精准的宝贵资产」，并称知情人士预计 Muse 最终会在信息流中出现广告（[Muse 助推 Instagram 广告]({{< relref "/docs/muse/sources/media/2026-11-24-cnbc-muse-instagram-ad-boost" >}})）。
- **撤下的广告：** 一则称 Muse 可每周显示谁取消关注你的 Instagram 广告，经 Business Insider 询问后被撤下（[撤下的取消关注广告]({{< relref "/docs/muse/sources/media/2026-11-05-meta-pulls-muse-unfollow-ad" >}})）。

推断：官方承诺的范围是「数据不进入广告系统」，不是「Muse 的使用不影响广告」。从以上测试和报道看，Muse 的商业逻辑与广告业务的联系在增强，承诺的边界会越来越受关注。商业层面的分析见 [商业与规模]({{< relref "/docs/muse/analysis/business" >}})。

## Meta 能否看到：运营政策与尚未上线的 Confidential VM

安全博文承认，现有架构「通过运营政策限制 Meta 人员对你数据的访问。它并不能阻止 Meta 在为支持、保护或运营服务而必要时访问数据」（[我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})）。虚拟机内的数据处理文档写明对话「not end-to-end encrypted」，交互可能被 Meta 记录和审查（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。社区拆解看到用户卷做了静态加密，也有遥测发往 Meta 日志（[Muse 沙箱剖析]({{< relref "/docs/muse/sources/community/2026-09-01-adwankar-whats-in-a-muse" >}})）。Future Society 的文件审查列出了离开虚拟机的集中记录，包括用户记忆嵌入、机群学习发件箱等；作者认为这与「只有有限数据离开虚拟机」的披露不一致（[Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})）。

Muse Confidential VM 计划用只有用户持有的密钥加密整台虚拟机，使 Meta 也无法访问。相关说法与时间如下：

| 时间 | 说法 | 资料 |
| --- | --- | --- |
| 2026-09-08 | 「今年晚些时候」推出；已在一小群受信任的测试者中使用，设计与源代码已提供给外部审计方 | [我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}}) |
| 2026-09-08 | 帮助页称仍「在设计中」 | [帮助：隐私与安全]({{< relref "/docs/muse/sources/official/2026-09-08-help-privacy-safety-security" >}}) |
| 2026-10-20 | 据社区作者转述，TestingCatalog 称网页端已有部分实现，并非正式发布 | [非用户消息隐私]({{< relref "/docs/muse/sources/community/2026-11-04-muse-non-user-messages" >}}) |
| 2026-11-03 | 社区核查称帮助页仍写「将来」，没有日期 | [非用户消息隐私]({{< relref "/docs/muse/sources/community/2026-11-04-muse-non-user-messages" >}})、[Muse 安全吗]({{< relref "/docs/muse/sources/community/2026-11-06-is-meta-muse-safe-privacy" >}})、[健康数据连接细则]({{< relref "/docs/muse/sources/community/2026-11-15-health-data-permission-chain" >}}) |
| 2026-11-27 | 马恩岛信息专员称更强的加密选项「尚在计划中」 | [信息专员谈代理式 AI]({{< relref "/docs/muse/sources/community/2026-11-27-isle-of-man-commissioner-agentic-ai" >}}) |

人工接触数据的问题，在电话功能上实际发生过。404 Media 披露，内部测试中电话由真人客服代打，有员工担忧隐私（[404 Media：电话任务背后的真人]({{< relref "/docs/muse/sources/media/2026-09-22-404media-muse-calls-made-by-humans" >}})）。据 All Things Muse 转述路透社，Meta 撤回了这一真人协助阶段，一位副总裁称之为「一次失误」（[电话代打 beta 首报]({{< relref "/docs/muse/sources/media/2026-10-05-muse-phone-call-beta" >}})）。

## 采集范围、保存与删除

- **采集范围广。** 互动记录包括文本、语音、照片以及「关于你或他人的信息」，连接器信息属于互动的一部分（[帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）。同一账户中心内的 Facebook、Instagram、Threads 会自动连接（[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})）。Mac 应用可读取 Messages、Mail、Notes（[帮助：Mac 文件与应用]({{< relref "/docs/muse/sources/official/2026-10-08-help-mac" >}})）。连接器各自的条款决定所收信息的用途，Meta 不审查自定义连接器（[帮助：连接器]({{< relref "/docs/muse/sources/official/2026-09-08-help-connectors" >}})）。
- **对连接器开发者的约束。** 开发者指南禁止二次使用连接器数据，包括出售、无关广告、推断敏感特征和模型训练（[连接器指南（开发者）]({{< relref "/docs/muse/sources/official/2026-11-04-connector-guidelines" >}})）。
- **删除有缺口。** 单条消息、对话、目标、文件、提醒可以分别删除，整体可以「Reset」（[帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）。但帮助页承认，删除内容后 Muse 可能仍记得从中学到的信息（[帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})）。断开连接器只停止新的数据交换，已用过的信息可能留在记忆和对话历史中（[56 个连接器普查]({{< relref "/docs/muse/sources/community/2026-10-17-muse-connector-census" >}})，转引 Meta 帮助文案）。社区作者按 Meta 文档整理了六层留存：主聊天不能单独删除，唯一完整的清除是 Reset；删除后的备份与保存期限没有公开文档（[2000 万条已删聊天]({{< relref "/docs/muse/sources/community/2026-10-24-muse-subpoena-agent-memory" >}})、[删除聊天记忆仍在]({{< relref "/docs/muse/sources/community/2026-10-28-muse-delete-chat-memory" >}})）。记忆机制见 [记忆与上下文]({{< relref "/docs/muse/analysis/memory" >}})。
- **语音没有单独的规则。** 眼镜上被判为误唤醒的语音在检测后 90 天内删除（[帮助：眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})）。眼镜在 Muse 与 Meta AI 之间切换时，分别适用两套隐私政策（[帮助：眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})）。社区作者并读各地区声明后指出：其他语音最长保留一年；美国版默认存储语音且无关闭选项，英国版可以选择（[眼镜端 Muse beta 解析]({{< relref "/docs/muse/sources/community/2026-11-09-muse-on-glasses-beta" >}})）。Muse 的数据页没有单独的语音转录设置或保存期限（[打开 Muse 语音模式]({{< relref "/docs/muse/sources/community/2026-11-06-how-to-turn-on-muse-voice-mode" >}})）。
- **分享链接泄露过。** Claroc 发现，Muse 分享页的主机名含对话标题，并会写入被动 DNS，一次查询即枚举出 6,800 多个分享主机名，部分含贷款申请、营收审查等内容（[Claroc：GhostShares]({{< relref "/docs/muse/sources/community/2026-10-18-claroc-ghostshares" >}})）。Ars Technica 询问后，Meta 于 2026-10-20 暂停了分享功能（[Ars Technica：分享链接泄露]({{< relref "/docs/muse/sources/media/2026-10-20-arstechnica-shared-conversations-exposed" >}})）。

## 他人的信息

这是资料中争议最多、监管最关注的部分。

| 场景 | 资料所述 | 来源 |
| --- | --- | --- |
| 人物页 | 研究者套出指令，要求为用户生活中的每个人保留一个页面并每小时更新；Meta 称这些文件对用户可见 | [WIRED：亲友人物档案]({{< relref "/docs/muse/sources/media/2026-10-03-wired-muse-profiles-friends-family" >}})、[Muse 评测核对]({{< relref "/docs/muse/sources/community/2026-11-02-muse-review-personalagentbench" >}})；TIME 的同类报道见 [Medianama：人物档案（二手）]({{< relref "/docs/muse/sources/media/2026-10-08-medianama-muse-dossiers" >}}) |
| Mac Messages 同步 | Inc. 的 Jason Aten 称拒绝授权后，Muse 仍同步了 Messages 数据库（约 18.7 万行），对来源的解释也有误；Meta 称该集成「完全自愿加入」，承认解释错误 | [“允许一次还是始终允许？”]({{< relref "/docs/muse/sources/community/2026-10-13-muse-approval-dialog-allow-always" >}})、[苹果重写 Mac 权限提示]({{< relref "/docs/muse/sources/community/2026-11-19-apple-rewrote-mac-permission-screen" >}})、[iMessage 事件详解]({{< relref "/docs/muse/sources/community/2026-10-01-did-muse-read-your-messages" >}}) |
| Signal 消息 | 路透社 2026-11-18 报道，与 Signal、AI Now 复现：Android 上经推送通知权限、macOS 上经辅助功能和截图读取 Signal 消息，绕过连接器；Signal 11-20 默认开启截图限制 | [路透：Muse 安全事故]({{< relref "/docs/muse/sources/media/2026-11-18-muse-early-safety-mishaps-surface" >}})、[Signal 限制截图防读取]({{< relref "/docs/muse/sources/media/2026-11-21-signal-screenshots-block-ai-agents" >}}) |
| 转发的邮件 | 他人转发或引用的邮件会把第三方信息带入 Muse，「即使你没有直接给 Muse 发过邮件」 | [帮助：Muse 邮箱地址]({{< relref "/docs/muse/sources/official/2026-11-16-help-email-addresses" >}}) |
| 以用户身份发出 | Marketplace 上 Muse 以 Robb 的身份议价并发出住址，买家以为对方是真人；群聊里以用户号码发消息，Meta 未公布是否标明为智能体发送 | [卫报：泄露家庭住址]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}})、[Muse 冒名发消息]({{< relref "/docs/muse/sources/community/2026-11-24-muse-messages-as-you-group-chat" >}}) |
| 电话对象 | 商家前台对 AI 通话未表示同意；Meta 员工分享的一通电话中，Muse 没有明确说明自己是 AI | [电话代打披露缺口]({{< relref "/docs/muse/sources/community/2026-11-08-phone-calls-disclosure-gap" >}})、[Muse 代打电话细节]({{< relref "/docs/muse/sources/media/2026-11-12-engadget-muse-phone-calls-paid" >}}) |
| 公开信息汇编 | Hunterbrook 演示按要求汇编名单；EFF 的 Mackey 等认为这是放大既有危害 | [Hunterbrook：按要求列名单]({{< relref "/docs/muse/sources/media/2026-09-28-hunterbrook-dox-for-me-muse" >}}) |

Meta 的回应分两步：

- **初期：** 每个用户的虚拟机彼此隔离，用户掌控自己的 Muse（[删除聊天记忆仍在]({{< relref "/docs/muse/sources/community/2026-10-28-muse-delete-chat-memory" >}})）。
- **2026-11-24 英国稿：** 处理关于不使用 Muse 的人的信息时，「不会将其与任何 Meta 账户关联，也不会以让 Meta 能够合理识别……的方式存储」（[英国上线与控制权]({{< relref "/docs/muse/sources/official/2026-11-24-muse-you-stay-in-control" >}})）。

Muse Explained 指出了这一承诺的矛盾：同一页面又称，Meta 只能为关联到账号或可识别的信息落实数据主体权利，非用户提出申诉时会被夹在两个承诺之间。作者截至 11-03 未见新的非用户控制途径（[非用户消息隐私]({{< relref "/docs/muse/sources/community/2026-11-04-muse-non-user-messages" >}})）。帮助页唯一面向接收方的建议，是请用户自己注明内容由 AI 生成（[帮助：开始使用]({{< relref "/docs/muse/sources/official/2026-09-08-help-get-started" >}})）。

推断：除邮件和 Signal 外，以上第三方问题出现在 Muse 上线后的头两个月。到 11 月，问题已从单个事件变成监管调查的内容（见下节）。Meta 的「不关联账户」承诺，回应的是「识别」问题，没有回应「同意」问题。

## 监管与地区差异

| 日期 | 事件 | 来源 |
| --- | --- | --- |
| 2026-10 下旬 | 英国 DRCF 下的 CMA、ICO 等称 AI 智能体可能「放大并加速风险」，ICO 公开征集证据 | [英国数周内上线]({{< relref "/docs/muse/sources/media/2026-11-09-times-muse-uk-launch" >}}) |
| 2026-11-23 | 蒙大拿州总检察长 Austin Knudsen 牵头多州调查，要求 Meta 在 30 天内提交用户数据用途、「为用户生活中的每个人」建档、未成年人使用与年龄验证等文件；起因是路透社 11-18 报道 | [蒙大拿州调查 Muse 隐私]({{< relref "/docs/muse/sources/official/2026-11-23-montana-ag-investigation-muse" >}}) |
| 2026-11-24 | 英国上线。CMA 称协商后 Meta 修改了条款，并发布使用建议，提醒检查信息是否用于训练 AI 或个性化广告；ICO 称已向 Meta 明确保护个人信息的责任 | [CMA 英国上线声明]({{< relref "/docs/muse/sources/media/2026-11-24-cma-statement-uk-launch-muse" >}})、[BBC 一周试用]({{< relref "/docs/muse/sources/media/2026-11-24-bbc-week-with-muse-uk-launch" >}}) |
| 2026-11-24 | 据转述，Meta 同意与 ICO 建立自愿监测与报告安排；马恩岛信息专员确认此事，并称正在监测 Muse | [英国第七个市场]({{< relref "/docs/muse/sources/media/2026-11-24-muse-launches-uk" >}})、[信息专员谈代理式 AI]({{< relref "/docs/muse/sources/community/2026-11-27-isle-of-man-commissioner-agentic-ai" >}}) |
| 2026-11-26 | WIRED：FCA 创新负责人 Colin Payne 称 Meta 拒绝了在 FCA 沙盒中联合测试 Muse，关注点是支付 | [Meta 拒绝 FCA 联合测试]({{< relref "/docs/muse/sources/media/2026-11-26-wired-meta-refused-fca-muse-test" >}}) |

其他与地区、年龄有关的资料：

- **欧盟与英国进度慢。** 据 DataDome 转述 Q3 财报电话会，Zuckerberg 称英国和欧盟预计耗时更长，因为 Muse 处理的个人数据比聊天机器人更多（[Muse 全球五国流量]({{< relref "/docs/muse/sources/community/2026-11-12-muse-goes-global-five-countries" >}})）。截至 2026-11-28，资料中没有 Muse 在欧盟上线的记录。
- **年龄限制。** Muse 限 18 岁及以上（[帮助：关于订阅]({{< relref "/docs/muse/sources/official/2026-09-08-help-about-subscriptions" >}})）。马恩岛信息专员提醒，其设计和推广方式可能吸引年轻人（[信息专员谈代理式 AI]({{< relref "/docs/muse/sources/community/2026-11-27-isle-of-man-commissioner-agentic-ai" >}})）；蒙大拿的调查也要求 Meta 提交年龄验证有效性的材料（[蒙大拿州调查 Muse 隐私]({{< relref "/docs/muse/sources/official/2026-11-23-montana-ag-investigation-muse" >}})）。
- **地区条款不同。** 眼镜语音存储美英两版条款不同（[眼镜端 Muse beta 解析]({{< relref "/docs/muse/sources/community/2026-11-09-muse-on-glasses-beta" >}})）。

## 资料缺口

- Muse 隐私政策原文（2026-09-17 生效）和各地区版本；各类数据的保存期限；删除后的备份处理。
- 英国稿「不用私人消息训练」是全球政策还是英国条款，与邮箱帮助页如何对应。
- Muse Confidential VM 的上线时间与审计结果；训练前去标识化流程的独立审查。
- 非用户删除人物页、提出数据主体请求的实际结果；电话对象的 AI 身份披露方式与商家退出机制。
- 蒙大拿多州调查的参与州名单与后续进展；Meta 对路透社 11-18 报道的正式回应；ICO 自愿监测安排的具体内容。
- 澳大利亚政策博文（[Muse 干活你做主]({{< relref "/docs/muse/sources/official/2026-11-17-medium-anz-muse-stay-in-control" >}})）只收了链接，原文待补抓。

## 主要资料

**官方**
- [帮助：数据管理]({{< relref "/docs/muse/sources/official/2026-09-10-help-manage-data" >}})：训练开关默认开启、删除入口。
- [我们如何将安全构建进 Muse]({{< relref "/docs/muse/sources/official/2026-09-08-how-we-built-safety-into-muse" >}})：轨迹训练、广告间接影响、Meta 人员访问、Confidential VM。
- [帮助：Muse 邮箱地址]({{< relref "/docs/muse/sources/official/2026-11-16-help-email-addresses" >}})：邮件内容与第三方信息。
- [英国上线与控制权]({{< relref "/docs/muse/sources/official/2026-11-24-muse-you-stay-in-control" >}})：英国稿，私人消息不用于训练，非用户信息不关联账户。
- [蒙大拿州调查 Muse 隐私]({{< relref "/docs/muse/sources/official/2026-11-23-montana-ag-investigation-muse" >}})：蒙大拿多州调查通稿。
- [帮助：眼镜 Beta]({{< relref "/docs/muse/sources/official/2026-10-27-help-glasses-beta" >}})：眼镜语音与位置数据。
- [连接器指南（开发者）]({{< relref "/docs/muse/sources/official/2026-11-04-connector-guidelines" >}})：连接器数据的二次使用禁令。

**媒体**
- [WIRED：更擅长监视]({{< relref "/docs/muse/sources/media/2026-09-20-wired-muse-better-at-surveilling" >}})：默认训练与专家批评。
- [路透：Muse 安全事故]({{< relref "/docs/muse/sources/media/2026-11-18-muse-early-safety-mishaps-surface" >}})：路透社安全事故调查，Signal 复现。
- [Muse 助推 Instagram 广告]({{< relref "/docs/muse/sources/media/2026-11-24-cnbc-muse-instagram-ad-boost" >}})、[Muse 跟进广告后行动]({{< relref "/docs/muse/sources/media/2026-11-24-mediapost-muse-post-ad-actions" >}})：Muse 与 Instagram 广告。
- [CMA 英国上线声明]({{< relref "/docs/muse/sources/media/2026-11-24-cma-statement-uk-launch-muse" >}})、[BBC 一周试用]({{< relref "/docs/muse/sources/media/2026-11-24-bbc-week-with-muse-uk-launch" >}})、[Meta 拒绝 FCA 联合测试]({{< relref "/docs/muse/sources/media/2026-11-26-wired-meta-refused-fca-muse-test" >}})：英国 CMA、ICO、FCA。
- [Ars Technica：分享链接泄露]({{< relref "/docs/muse/sources/media/2026-10-20-arstechnica-shared-conversations-exposed" >}})：分享链接泄露与暂停。
- [404 Media：电话任务背后的真人]({{< relref "/docs/muse/sources/media/2026-09-22-404media-muse-calls-made-by-humans" >}})：电话测试中的真人代打。
- [卫报：泄露家庭住址]({{< relref "/docs/muse/sources/media/2026-09-28-guardian-muse-home-address" >}})：Marketplace 住址事件。

**社区**
- [Future Society：Muse 文件审查]({{< relref "/docs/muse/sources/community/2026-09-26-future-society-muse-own-files" >}})：虚拟机内数据处理文档与集中记录。
- [Claroc：GhostShares]({{< relref "/docs/muse/sources/community/2026-10-18-claroc-ghostshares" >}})：GhostShares 研究。
- [账本训练模型与三层退出开关]({{< relref "/docs/muse/sources/community/2026-10-19-muse-small-business-data-trains-models" >}})：训练开关与去标识化范围。
- [2000 万条已删聊天]({{< relref "/docs/muse/sources/community/2026-10-24-muse-subpoena-agent-memory" >}})、[删除聊天记忆仍在]({{< relref "/docs/muse/sources/community/2026-10-28-muse-delete-chat-memory" >}})：留存层级与删除缺口。
- [非用户消息隐私]({{< relref "/docs/muse/sources/community/2026-11-04-muse-non-user-messages" >}})：非用户隐私承诺的矛盾。
- [苹果重写 Mac 权限提示]({{< relref "/docs/muse/sources/community/2026-11-19-apple-rewrote-mac-permission-screen" >}})：Mac Messages 同步与 Apple 权限变化。
- [眼镜端 Muse beta 解析]({{< relref "/docs/muse/sources/community/2026-11-09-muse-on-glasses-beta" >}})：眼镜语音的美英差异。
- [信息专员谈代理式 AI]({{< relref "/docs/muse/sources/community/2026-11-27-isle-of-man-commissioner-agentic-ai" >}})：马恩岛信息专员的监管视角。
