---
title: "你的智能体想要你的心率：先读清细则再点头"
linkTitle: "健康数据连接细则"
date: 2026-11-15
originalTitle: "Your Agent Wants Your Heart Rate. Read the Fine Print Before You Say Yes"
sourceUrl: "https://aihomebuilding.com/stories/muse-health-data-deal-2026.html"
author: "Catherine Chen"
publisher: "AI Home Building"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-16
tags: [隐私, 安全, 记忆与上下文]
products: [muse]
---

{{< source-info >}}

**收录说明**：直接下载；无图片（首图为装饰性照片，未收）。作者未做一手实测，文中已声明无 Muse 账号、未确认 HealthKit 实际请求的类别、是否请求写权限或连接界面披露了什么；“只读”等说法为作者据 Meta 未公布清单所作的推断，文中已标明。原文全文存于本目录的 original.md，网站上不显示，待翻译。

**内容摘要**：Muse 自 2026 年 9 月 8 日上线起提供健康数据连接，iPhone 上为 Apple Health、Android 上对应 Health Connect，可汇总睡眠、标出不足 6 小时的夜晚并起草就诊提问，但不能诊断、不能判断读数是否安全、不能替代临床医生；Meta 未公布 Muse 具体可读的数据类型清单，也未说明能否向 Health 应用回写数据。手机一侧的保护是按类型逐项授权：HealthKit 读写分开授权，数据不得用于广告、不得出售、未经明确许可不得向第三方披露；Health Connect 的权限参考列出 42 种以上记录类型，每类读写分开，另有授予全部历史与后台读取的两项元权限。数据离开手机后进入 Muse Secure VM：该 VM“并不阻止 Meta 在必要时访问数据”，员工访问限制靠运营政策而非密码学；对话、工具调用与子代理交接合称 trajectories，默认经脱敏后用于训练新模型检查点，除非用户在设置中关闭；以用户独持密钥加密的 Confidential VM 已宣布于 2026 年内推出，但截至 11 月 3 日的独立核查仍未上线；2026 年 9 月 17 日生效的隐私政策称，删除后 Muse“仍可能‘记得’从被删内容中学到的信息”。作者将两段对照为一次授权等于几十项许可：Muse 里连接只是一次点击，Meta 从未公布 Muse 请求哪些 HealthKit 类别；撤销权限只停止后续访问，不删除已复制的数据，删除也不保证遗忘；10 月 TIME 报道 Muse 每小时更新一份关于用户及每个被提及者的持续档案，Meta 未否认该报道。作者明确声明本文未做一手实测，未使用 Muse 账号，无法确认 Muse 实际请求的类别、是否请求写权限或连接界面披露了什么，“只读”的说法是据沉默作出的推断，不应视为已定事实。

**保留理由**：已收资料中没有对健康数据权限链的独立审计；本篇把手机端逐项授权与云端 Secure VM、训练默认开启、删除后仍“记得”的规则放在同一条链上对照，并给出一次点击对应几十项许可的计数。训练默认开启、删除后仍“记得”、以及被提及的第三方无退出途径，是此前收录未覆盖的角度。
