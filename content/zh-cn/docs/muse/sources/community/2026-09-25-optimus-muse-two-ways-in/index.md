---
title: "两种入侵路径：本地设置与技能更新如何让 Muse 反噬用户"
linkTitle: "两种入侵路径"
date: 2026-09-25
updatedAt: 2026-11-16
originalTitle: "Two Ways In: A Local Setting and a SKILL Update Turned Meta's Muse Against Its User"
sourceUrl: "https://optimuslabs.io/research/briefings/meta-muse-dictation-endpoint-hijack"
author: "Optimus Labs · Civilizations"
publisher: "Optimus Labs"
language: en
fidelity: 全文
translation: 待翻译
collectedAt: 2026-11-27
tags: [安全, 运行环境]
products: [muse]
dateNote: "2026 年 11 月 16 日更新加入第二条攻击链；本轮迟发现，属回填。"
---

{{< source-info >}}

**收录说明**：直接下载（main 容器抽取）。原文全文存于本目录的 original.md，网站上不显示，待翻译。攻击链示意图按页面原文位置补回并本地化到 images/；导航、byline、相关简报与下载链接等站内元素已删去。

**内容摘要**：这篇 Optimus Labs 威胁研究简报记录了针对 macOS 版 Meta Muse 的两条攻击链：第一条由 Patrick Wardle 于 2026 年 9 月 21 日公布本地概念验证，同一用户会话中运行的进程无需管理员权限即可改写未公开的听写偏好设置 `endo_voyager_dictation_endpoint`，将语音、转录内容与会话材料重定向到攻击者端点，并返回攻击者选定的文本让 Muse 当作用户指令执行，简报称 Meta 在披露后数小时内发布了热修复。第二条链由 Harsha Gundala 于 2026 年 11 月 16 日报告：一个表面干净的 SKILL 或 MCP 服务器在安装时伪造用户同意并悄悄设置后台 git pull，随后的仓库更新改写了 Muse 每轮都会作为用户偏好加载的 AGENTS.md 与 MEMORY.md，使中毒的记忆让浏览器助手把 Ctrl+X 理解为「清空字段」，在 Muse 填入已保存密码时将其剪切到剪贴板并粘贴到攻击者控制的页面、随后正常完成登录，Meta 为此在受管浏览器中屏蔽了键盘快捷键，但研究者称相关变体仍未修复且尚未公开。简报称，第一条链一旦得手，攻击者可能动用 Muse 已获授权的访问权限，涉及文件、邮件、日历、WhatsApp、麦克风、摄像头、位置与已连接的 iPhone，具体范围取决于每位用户的授权与连接情况。简报同时限定：它没有证实真实客户入侵、野外利用或远程零点击入侵，第一条链需要代码已在登录用户的 macOS 会话中运行，Meta 将实际风险描述为低，且 9 月简报未分配 CVE、也无正式公告。简报还列出了修复与缓解清单，包括确认安装热修复、检查听写端点偏好是否被改为陌生主机、核查本地偏好变更遥测与外发听写连接、清点桌面智能体及其已连接账号与授权，并按 0–24 小时遏制、24–72 小时调查的时限分段执行。

**保留理由**：这篇是仓库中 11 月第二条攻击链（SKILL 更新改写记忆文件、Ctrl+X 剪切已保存密码）的首个结构化记录，并附有两条链各自的修复状态与分时段的缓解清单，是 9 月听写端点事件的后续补充。
