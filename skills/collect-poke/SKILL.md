---
name: collect-poke
description: 收集 Poke（The Interaction Company of California，2026-07 起加入 Cognition）的资料时使用：Poke 的官方渠道、抓取方法、收录范围与已知问题。与 collect-sources 配合使用，通用流程与页面规则见 collect-sources。
---

# 收集 Poke 资料

通用流程、页面模板与翻译规则见 `skills/collect-sources/SKILL.md`。本文件只记录 Poke 特有的内容；与通用规则冲突时，以本文件为准。

## 状态

| 项目 | 值 |
| --- | --- |
| 产品目录 | `content/zh-cn/docs/poke/`（尚未建立，第一轮收集时按 section-templates.md 建） |
| 时间线 | 2026-03 前后上线（据二手报道，待核实）；2026-06-04 TechCrunch 报道成为首个获准上 Apple Messages for Business 的 AI 智能体；2026-07-23 Cognition 宣布「welcoming」The Interaction Company，产品照常运营 |
| 最后收集日期 | —（2026-11-06 用户同意纳入，尚未收集） |

## 背景

- 帕洛阿尔托初创公司 The Interaction Company of California，创始人 Marvin von Hagen、Felix Schlegel。Cognition（Devin 的开发商）公告没有明说是收购；poke.com 写的是「Poke is joining Cognition」。
- 没有独立 App：通过 iMessage、SMS、WhatsApp（部分市场）、Telegram 交互。
- 接入 Gmail、Google Calendar、Outlook、Notion、Asana、Linear、Todoist、Granola、GitHub、Strava 等；能起草和发送邮件、整理收件箱、建提醒；有记忆，会主动发消息。开发者可在 Poke Kitchen 自建 recipe 与集成。
- 价格（2026-11-06 官网）：Free $0；Pro $19/月（前沿模型、后台实时自动化）；Ultra $199/月（每次操作用前沿模型，超出额度按量付费）。
- 官网首页没有说明权限、审批与对外通信的控制设计，第一轮收集时到帮助文档或 FAQ 中找。

## 收录范围

- 收：poke.com 的官方页面与公告、帮助文档、Cognition 关于 Poke 的公告、专门写 Poke 的报道和实测、创始人访谈（有文字稿或节目页文字时）。
- 法律文档按 tracking.md 不收。
- 首页的用户推荐语是宣传材料，不作为实测证据。
- Cognition 把 Poke 的风格带到 Devin 的资料：只讲 Devin 编程能力的不收；明确说明 Poke 产品变化的收。

## 官方渠道

| 渠道 | 地址 | 内容 | 抓取方法 |
| --- | --- | --- | --- |
| 官网 | `poke.com`（含 `/pricing`） | 产品介绍、集成、价格 | 2026-11-06 用 WebFetch 可读，下载方法待第一轮确认 |
| Cognition 博客 | `cognition.com/blog/interaction` | 2026-07-23 加入 Cognition 的公告 | 同上 |
| Poke Kitchen | 地址待查 | 开发者 recipe 与集成 | 待确认 |

## 媒体与社区检索

- 英文检索词：`Poke AI assistant`、`Poke iMessage agent`、`poke.com Interaction Company`、`Poke Cognition`
- 中文检索词：`Poke AI 助理`、`Poke 短信 智能体`
- 「Poke」是常见词（还有 poke 菜品、Facebook 的 poke 功能），检索时要带 AI、iMessage 或 Interaction。
- 重点媒体：TechCrunch（2026-06-04 Apple Messages for Business；2026-10-10 短信类智能体合集）。
- 检索结果中有大量 SEO 与聚合站（dealroom、aidirectory、poster.ly、theaiagentindex、neuronfeed、runtimewire、justthink 等），不收。

## 已知问题

（第一轮收集时补充。）

## 命名约定

- 目录名用 `poke`。
