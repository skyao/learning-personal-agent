---
title: "模型是引擎，78 行技能文件是驾驶手册"
linkTitle: "78 行技能文件"
date: 2026-10-18
originalTitle: "The Model Is the Engine. The 78-Line Skill File Is the Driver's Manual."
sourceUrl: "https://aihomebuilding.com/stories/muse-skill-files-beat-prompts-2026"
author: "Frank DeLuca"
publisher: "AIHomeBuilding"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-22
tags: [运行环境, 实测评测]
products: [muse]
---

{{< source-info >}}

## 收录说明

本页收录的文章于 2026-10-18 发布在 AIHomeBuilding。直接下载后以 article.article-body 抽取全文，未做删改。头图为装饰图，未收。原文全文存于本目录的 original.md，网站上不显示，待翻译。

作者限定：盘点的技能库在“一台在用的智能体”上，采用内部格式（元数据在独立卡片文件而非 Markdown 头部），不是 Meta 发货的 Muse 目录；2384 的社区计数为自报，作者未能独立核实其安全审查说法；未做有无加载技能的任务成功率对照试验。

## 内容摘要

作者盘点了一台在用智能体上的技能库：64 个技能文件，平均 78 行，共 4276 行，其中 55 个随系统提供，9 个是智能体在反复出现的真实工作后自己写的；最长的购物技能 285 行，最短的风格工具 21 行。文章引用 flight-booking 技能的决策树：先定路线、日期、舱位与灵活度，只问真正会改变路线或价格的缺失细节，按核实后的总价与总行程时间排序，绝不拿单程价与往返总价比较，绝不以另一航班替代用户点名的航班。Gmail 技能写明发一封邮件 100 个预算单位、读一封 20 个单位，因此智能体批量处理而非循环调用。社区目录已列出 2384 个 Muse 技能，但截至成文时没有官方安装方式，需把文件粘贴进聊天并告知用途，无版本管理、无更新、无撤销。

## 保留理由

这是唯一一篇对技能文件做一手数量盘点的文章（64 个、4276 行、平均 78 行、购物 285 行），且首次讲清“连接器是到达工具的路，技能是使用工具的程序”这一分工，以及读技能文件可在 OAuth 之前先看到读写权限范围。
