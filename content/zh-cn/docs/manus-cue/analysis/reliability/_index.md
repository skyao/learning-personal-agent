---
title: "Manus Cue：实际效果与可靠性"
linkTitle: "实际效果与可靠性"
weight: 120
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  Cue 的实测资料很少：一份一天的详细实测（xiangxiang103）和一份上手体验（硅星人），都在发布次日。能用的是自带邮箱、云电脑和定时蹲守；问题是「说完成不等于完成」、群聊要用户当项目经理、身份在风控平台上站不住。其他反馈集中在价格、电话和 IP 等落地摩擦。
---

## 概要

- 截至 2026-11-10 的资料中只有两份 Cue 实测，都在 2026-09-29：xiangxiang103 用了一整天、记录详细；硅星人只做了上手体验，没有让智能体下单。没有任务完成率、出错率的数据，也没有发布一个月以上的复测。
- xiangxiang103 的总评：能用的是自带邮箱、云电脑、定时任务；差点意思的是拉群协作、邮件页脚、在风控严的平台注册。
- 他一天内遇到三次「说完成不等于完成」：说安排了跟踪却没建任务；说邮件已发送，其实只知道状态是 sent，信进了推广栏；Claude 账号注册成功 22 分钟后被封。
- 行业综述认为，Cue 目前能看到的反馈「几乎都指向落地摩擦，而不是任务成功率」：价格、电话收不到短信、IP 落在非主要西方国家。

## 两份实测

| 测试者 | 时间与条件 | 测了什么 | 结论 |
| --- | --- | --- | --- |
| xiangxiang103 | 2026-09-29，Mac 版，一整天；此前通读官网示例和 X 上几十条实测 | 注册流程、环境自检、代注册 Claude、发邮件、蹲机票、三智能体群聊 | 邮箱、云电脑、定时任务能用；群聊、邮件、风控平台注册差点意思 |
| 硅星人 | 2026-09-29，上手体验 | 新建助手、两个助手群聊规划家庭出游 | 能多轮协作，未接支付、未下单，没有给出效果判断 |

资料来源：[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})、[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})。这篇 xiangxiang103 是 X 长文的转载，其中对 Muse 的描述、部分价格和「前 1000 名」等说法没有注明出处。

## 「说完成不等于完成」

xiangxiang103 一天内遇到三次（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）：

- **任务没建**：说要盯机票，智能体回答「明白，我先安排跟踪」，任务列表里什么都没有。再次交代后它追问三轮，自己写的日期选项算错一天，「一个成人」是它自己默认的。任务建好后每天按时运行（见[持续执行](../continuous-execution/)）。
- **邮件没到**：智能体第一次只说「已发送」，追问后才承认只知道状态是 sent，不能证明已送达；信在收件方 Gmail 的推广栏里找到，带 Manus 页脚（见[交互渠道](../channels/)）。作者建议重要邮件隔一两天让智能体查回复。
- **账号被封**：智能体用 @bot.cue.im 邮箱和云电脑注册 Claude，在年龄确认和条款同意处停下来问作者，注册完成约 22 分钟后账号因「可疑信号」被暂停；官方邮件没说原因，作者推测与机器人邮箱域名、机房 IP、自动化操作有关。作者的提醒是「注册成功不等于能用」。

作者把这些归结为一句话：「别只看‘已完成’」；官方宣传「你只管拍板」，实际前几轮要用户当项目经理、把信息喂够（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。

## 群聊协作

xiangxiang103 让三个智能体规划东京亲子游：三个都回复了，但都在等信息，没人按合理假设往下做；研究员同一问题问了两遍；盯梢员在私聊里查过东京机票，到群里没人提，群聊和私聊记忆不互通；最后是「秘书」主动出来分工（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})）。硅星人的两个助手在群里进行了多轮对话，但没有走到执行一步（[硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})）。

## 反馈集中在落地摩擦

Datawhale 认为，目前能看到的关于 Cue 的具体反馈「几乎都指向落地摩擦，而不是任务成功率」：电话收费、部分国家收不到短信、号码绑定 IP、重启容器换到非主要西方国家的「住宅」IP（[Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})）。鸿煊同样认为这一轮产品的摩擦「大多不在‘模型聪不聪明’」，而在身份、IP、短信验证这些现实接入层（[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})）。这两篇都是转述公开反馈，没有逐条注明原帖。

xiangxiang103 注意到官网示例几乎都是美国本地生活服务，钱包、代付、电话都是美国优先（[xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})），对美国以外的用户，许多示例场景用不上。

Enterpret 的社交声量排名中，Cue 的声量份额只有 0.5%，好感度 0.481（[Enterpret 排名]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})），样本太小，不足以判断用户评价的倾向。

推断：两份实测都在发布次日，问题多出在「确认」环节（任务是否真建好、邮件是否送达、账号是否可用），智能体倾向于报告动作而非结果。这与 Cue 依赖独立身份办事有关：每一步都要经过外部平台的风控，结果不由智能体自己决定。由于没有后续复测，这些问题后来是否改善无从判断。

## 资料缺口

- 发布一个月以上的实测和复测；用户自己的实测（`exploration/` 为空）。
- 电话代接、扫码点单、付款、iMessage 等渠道的实测。
- 任务完成率、出错率的任何量化数据；官方对注册被封、邮件进推广栏的回应。
- 腾讯云开发者社区「Cue 的第一轮实测」等收集阶段未取得的中文实测（见 collect-manus-cue skill 的判断记录）。

## 主要资料

媒体
- [硅星人]({{< relref "/docs/manus-cue/sources/media/2026-09-29-guixingren-manus-2-cue" >}})：上手体验、群聊

社区
- [xiangxiang103 实测]({{< relref "/docs/manus-cue/sources/community/2026-09-29-xiangxiang103-manus-2-cue-hands-on" >}})：一天的详细实测，本页主要依据
- [Datawhale]({{< relref "/docs/industry/sources/community/2026-10-18-datawhale-personal-agent-overview" >}})、[鸿煊]({{< relref "/docs/industry/sources/community/2026-11-06-hongxuan-what-is-new" >}})：落地摩擦的反馈（转述）
- [Enterpret 排名]({{< relref "/docs/industry/sources/community/2026-11-03-personal-ai-agents-users-prefer" >}})：社交声量
