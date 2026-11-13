---
title: "WorkBuddy：记忆与上下文"
linkTitle: "记忆与上下文"
weight: 20
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  WorkBuddy 的上下文分两层：每晚从会话中提取的个人记忆，加上工作空间和项目里的记忆文件与资料库。用户能查看、编辑、清空、关闭记忆，但本地记忆与云端记忆的关系没有官方说明。
---

## 概要

- 个人记忆从会话历史中提取事实、偏好、人物关系和近期跟进事项，每晚整理当天的会话，默认开启，仅本人可见；使用时注入系统提示词，也支持检索会话历史。
- 用户可以在设置中查看、清空、一键关闭，也可以在对话里让它记住或忘记什么；还能从其他 AI 产品导入记忆。官方承认自动抽取的记忆「可能存在概括偏差或时效性问题」。
- 工作层面的上下文来自工作空间的 `MEMORY.md`、项目级 `CODEBUDDY.md` 和项目资料库（每个项目默认 5 GB，以 RAG 方式注入）。
- 本地长期记忆（07-21 起可展示编辑）与云端记忆（10-22 起「可记住项目相关内容」）并存，二者如何分工资料没有说明。
- 个人数据主要经本地文件和连接器接入，没有像平台型产品那样直接调用账号里的邮件、相册、购物记录。

## 个人记忆：每晚提取，注入提示词

帮助中心的记忆页（最后更新 2026-07-08）写明（[帮助：记忆]({{< relref "/docs/workbuddy/sources/official/2026-07-08-help-memory" >}})）：

- **提取内容**：事实信息、偏好习惯、人物关系、近期跟进事项等「具有参考价值的个人信息」。
- **频率**：「每晚整理当天会话，仅您本人可见」；默认开启。提取由 WorkBuddy「自费完成」，不消耗用户积分。
- **使用方式**：一是注入系统提示词作为上下文，二是检索会话历史（如「上周做过什么」）。
- **用户控制**：在「设置 - 记忆」查看；在对话中告诉它记住或忘记什么；清空或一键关闭。记忆摘要每晚重新生成。关闭或删除后数据停止用于后续对话，但已生成的输出不追溯撤回。
- **导入**：把示例提示词复制到其他 AI 对话里，再把结果粘贴回来「添加到记忆」。
- **局限**：官方提醒记忆由模型自动抽取，依赖它做重要判断前应核验。

更新日志显示记忆功能的演变（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）：4.6.2（03-20）Working Memory 改为按工作空间独立存储；4.7.0 初始化工作空间时自动创建 `MEMORY.md`；5.3.3（07-21）个性化页新增「本地长期记忆展示与编辑」；5.4.5（08-30）个人面板新增「记忆与进化」入口；5.9.1（10-22）「优化云端记忆，可记住项目相关内容」。5.2.6（07-12）写有「专享版禁用 Memory 个性化功能」。记忆开关也出过问题：4.22.12 修复「关闭再打开记忆开关导致记忆丢失」，5.8.1 修复记忆删除后重新导入不显示。

推断：记忆页只描述一套「每晚提取」的机制，而日志同时出现「本地长期记忆」和「云端记忆」。可能本地与云端各存一份，或云端记忆专指项目内容，资料不足以判断。

## 工作空间与项目的上下文

项目中发起任务时，上下文由三部分拼成：项目指令拼入模型上下文，项目资料库以 reference 形式进入，个人记忆也拼入上下文（[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})）。具体做法（[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})）：

- **资料库**：内容以 RAG 形式注入，Agent 也可用 read-file 读取；每个项目默认 5 GB，依托腾讯网盘。
- **项目记忆文件**：`.codebuddy/CODEBUDDY.md` 存放项目架构、约定、常用命令等团队知识，兼容 `AGENTS.md`。
- **共享**：项目的指令、Skill、专家、连接器配置存在云端，成员共享。
- **任务转交**：原任务的完整上下文（对话记录、调用记录、中间产物）复制到新会话，附自动生成的进度摘要。

长对话的上下文靠压缩控制成本。「经济模式」在个人版默认开启，会在合适时机自动压缩上下文；关闭后保留完整上下文，但积分消耗明显增加（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）。日志中多个版本修复过压缩后消息错序、`/clear` 后压缩仍带旧内容等问题（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

## 个人数据怎么进来

WorkBuddy 没有直接读取某个账号体系里全部个人数据的设计，个人数据主要有三条来路：

- **本地文件**：授权后读写工作空间里的文件（[帮助：简介]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-overview" >}})）。
- **连接器**：如 QQ 邮箱连接器可读取收件箱近一个月的邮件（[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})），详见[连接器]({{< relref "/docs/workbuddy/analysis/connectors" >}})。
- **转发**：5.5.0 起可通过系统分享入口把微信聊天记录发给 WorkBuddy；5.5.5 起从企业微信转发聊天记录后，自动读取其中的文档、微盘文件、日程、待办、会议和智能纪要（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

## 跨渠道共用一个会话

助理（远程任务）只有一个会话，保留完整历史，不可清空（[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})）。数智奔流的企业微信实测发现，企业微信和 WorkBuddy 客户端「两边共享同一个会话记忆，回复却只发回消息的来路」：企业微信发来的消息同步到客户端，客户端里的对话不同步到企业微信。问「看看我最近在忙啥」时，它翻了自己的会话记录，又列出桌面和素材文件夹的目录来回答（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。

## 第三方的说法

程序员鱼皮把 WorkBuddy 这类桌面端 Agent 描述为「下次找它还得重新交代」，以此与有长期记忆的 Personal Agent 对比（[程序员鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})）。这与官方记忆页的说明不一致；该文没有实测 WorkBuddy，本页以官方说明为准。黑咖啡全景解读的对比表把 WorkBuddy 的上下文概括为「工作任务、项目记忆、文件与用户偏好」，Personal Agent 则是「长期个人记忆、目标与现状」（[黑咖啡全景解读]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})）。

## 资料缺口

- 本地长期记忆与云端记忆的关系、存放位置、同步方式。
- 记忆数据的保存期限；关闭记忆后已提取的数据是否删除。
- 7-08 之后记忆页是否更新（资料页只存档了这一版）。
- 记忆实际效果的实测：提取是否准确，跨会话能否用上。

## 主要资料

- 官方：[帮助：记忆]({{< relref "/docs/workbuddy/sources/official/2026-07-08-help-memory" >}})（个人记忆机制）、[帮助：项目]({{< relref "/docs/workbuddy/sources/official/2026-10-13-help-project" >}})（项目上下文、资料库、转交）、[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})（经济模式与上下文压缩）、[帮助：助理接入指南]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-assistant-guide" >}})（助理单一会话）、[帮助：连接器]({{< relref "/docs/workbuddy/sources/official/2026-10-23-help-connector" >}})（QQ 邮箱读取范围）、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})（记忆功能演变、聊天记录转发）
- 社区：[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})（跨渠道共享会话记忆的实测）、[程序员鱼皮]({{< relref "/docs/industry/sources/community/2026-10-12-yupi-why-big-tech-personal-agent" >}})、[黑咖啡全景解读]({{< relref "/docs/industry/sources/community/2026-11-01-heikafei-personal-agent-panorama" >}})（第三方对比）
