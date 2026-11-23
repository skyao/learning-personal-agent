---
title: "你联系不上，你的智能体却没闲着"
linkTitle: "联系不上时智能体在做什么"
date: 2026-10-27
originalTitle: "You Are Unreachable. Your Agent Is Not Idle."
sourceUrl: "https://aihomebuilding.com/stories/muse-unreachable-decision-rules-2026"
author: "Frank DeLuca"
publisher: "AIHomeBuilding"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-22
tags: [安全, 持续执行]
products: [muse]
---

{{< source-info >}}

## 收录说明

本页收录的文章于 2026-10-27 发布在 AIHomeBuilding。直接下载后以 article.article-body 抽取全文，未做删改。头图为装饰图，未收。原文全文存于本目录的 original.md，网站上不显示，待翻译。

作者限定：四级分类为作者提出的协议而非实测结论；作者自承无法修复原始指令错误、经检索文档的操纵、半睡半醒间误点批准卡等问题；1000 万用户数字引自扎克伯格的公开说法。

## 内容摘要

文章以六小时航班设问：智能体在途中完成研究、找到更优价格，到达需批准的一步时，批准卡片躺在开飞行模式的手机里，六小时无人响应。Meta 的文档化承诺是：发送邮件、完成购买等敏感步骤暂停等待用户批准；每位用户有专属云电脑 Muse Secure VM；Sentinel 审批每项出站动作；完整审计轨迹展示已做与计划做的事。作者核查后指出未找到任何已公布的 Meta 规则说明批准请求的有效期、时效性批准过期后智能体怎么做、向谁求助的后备顺序、无人应答时怎么办。文章提出原创的四级分类：ACT（可逆、低成本、已完整指定）；PREPARE（做到不可逆步骤之前，留一个待决决定）；HOLD（事实可能变化时冻结任务并记录冻结与复查时间）；EXPIRE（让窗口关闭并记录为决定而非事故），并要求把批准的有效期写入任务，如“本批准有效期至周四中午 12 点（太平洋时间），仅当价格低于 400 美元且出发时间在早上 8 点之后”。

## 保留理由

这是唯一一篇讨论“用户不可达时智能体该怎么办”的文章；四级分类（ACT/PREPARE/HOLD/EXPIRE）与“批准有效期”写法是本篇独创的操作框架，且其出发点——Meta 未公布批准有效期与后备顺序——是作者实际核查过的文档空白。
