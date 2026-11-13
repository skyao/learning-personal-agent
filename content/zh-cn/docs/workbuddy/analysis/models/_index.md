---
title: "WorkBuddy：模型"
linkTitle: "模型"
weight: 70
analyzedAt: 2026-11-13
sourcesUntil: 2026-11-10
description: >
  WorkBuddy 不绑定单一模型：内置混元、GLM、MiniMax、Kimi、DeepSeek 多家模型，按快速、均衡、极致三档供用户选择，也可以接自定义 API 或本地 Ollama。资料中没有为智能体专门训练模型的说法。
---

## 概要

- 多模型并列：截至 2026-11-10 的模型页列出 14 个内置模型，包括腾讯混元 Hy4 preview、Hy3，以及 GLM、MiniMax、Kimi、DeepSeek 系列；没有资料说明有为 WorkBuddy 专门训练或优化的模型。
- 用户自选：三档模式（快速、均衡、极致）加思考强度、上下文窗口档位，档位越高单轮积分越多；体验版为 Auto 调度，付费版全模型可选。
- 可以接自定义模型：腾讯云 Token Plan、腾讯云/智谱/Kimi 的 Coding Plan、本地 Ollama、自定义 URL；配置和 API Key 只存在本地。
- 算力紧张时有排队：选择器显示模型繁忙度（空闲到不可用四级），但不阻止选择；实测中标「空闲」的模型也排不上。
- 模型下线时自动切换到同系列新模型，本地自定义模型不受影响。

## 内置模型与三档模式

模型配置页（2026-11-10 版）列出的内置模型：Hy4 preview、Hy3、GLM-5.3、GLM-5.3-Flash、GLM-5.2、GLM-5.1、GLM-5v-Turbo、MiniMax-M3、MiniMax-m2.7、Kimi-K3、Kimi-K2.7-Code、Kimi-K2.6、Deepseek-V4-Flash、Deepseek-V4-Pro，其中 GLM-5.3 与 DeepSeek-V4 标注支持 1M 上下文（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）。4.5.0 正式版发布时就支持多模型切换（GLM、DeepSeek 等）（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

用户选择的维度（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）：

- **三档模式**：快速（简单任务，响应最快、消耗最低）、均衡（绝大多数任务，不确定时选它）、极致（复杂任务，消耗更高但结果更稳定）。
- **思考强度与上下文窗口**：窗口分默认、适中、超长；页面提醒「更大的窗口不会让模型变聪明」，档位越高单轮积分越大，只对当前任务生效。
- **经济模式**：原「Max 模式」开关移到「设置 → 智能体」，个人版默认开启，自动压缩上下文以降低消耗。

套餐与模型的关系：体验版是「Auto 模型调度（限免全模型可选）」，标准版及以上「全模型可选」（[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})）。积分消耗取决于模型的 Token 定价和任务复杂度，高级模型单价更高（[帮助：积分]({{< relref "/docs/workbuddy/sources/official/2026-10-09-help-credits" >}})）。日志中还有夜间折扣展示（5.2.3、5.3.3）（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

## 自定义模型与本地模型

接入方式有三种（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）：提供商接入（腾讯云 Token Plan 的四类套餐，以及腾讯云、智谱、Kimi 的 Coding Plan）、本地 Ollama（默认端口 11434）、自定义 URL。Token Plan 是腾讯云「专为 AI 编程和 WorkBuddy 场景打造」的订阅（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）。

自定义模型的配置（含 API Key）只保存在本地 `workbuddy/models.json`，不上传云端；WorkBuddy 只做通信转发，费用由用户向第三方支付（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）。同页的提示框又写作 `~/.codebuddy/models.json`，路径口径不一致。本地模型的适用场景是数据不出本机、零成本试用、离线可用（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）。5.8.0 起，使用非官方中转域名时会提示数据安全风险（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。

企业版中，管理员在后台禁用的模型在客户端隐藏或置灰（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）。据数智奔流转述官方直播，企业微信的企业控制台可以统一配置混元、DeepSeek 等模型（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。

## 繁忙度、排队与下线切换

5.8.0（10-09）起模型选择器显示繁忙度：空闲、轻微拥堵、极度拥堵、不可用；「繁忙程度仅供参考，不阻止你选择该模型」（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。数智奔流的定时任务因「当前模型队列已满」失败，作者切换到标「轻微拥堵」「空闲」的模型也没有改善，称算力排队是早期体验的门槛，原因用户并不清楚（[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})）。

模型下线时（2026-11-10 新增说明）：优先切到同系列新模型（如 Kimi-K3 下线后切 Kimi 系列），没有则用系统默认；思考强度与上下文窗口不沿用；本地自定义模型不会被自动替换（[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})）。定时任务的切换规则见[持续执行]({{< relref "/docs/workbuddy/analysis/continuous-execution" >}})。

## 多模态生成

日志显示 WorkBuddy 也承担图片、视频、3D 生成：4.21.0 起生成的视频和图片自动加水印；5.4.0 加入 3D 模型生成；5.5.5 的「创意设计」覆盖图片、视频生成和品牌设计；5.5.3 起 Kling V3 视频支持 720P、1080P（[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})）。资料没有说明这些生成能力分别用哪家模型，除 Kling 外均未写明。

## 资料缺口

- Auto 调度的路由规则；三档模式各对应哪些模型。
- 混元 Hy3、Hy4 是否针对智能体任务做过专门训练（数智奔流转述财新称混元 Hy3 「重点强化 Agent 能力」，但没有说明与 WorkBuddy 的关系）。
- 各模型的积分单价。
- 排队的原因与各档套餐的排队优先级。

## 主要资料

- 官方：[帮助：模型配置]({{< relref "/docs/workbuddy/sources/official/2026-11-02-help-model" >}})（模型列表、三档、自定义与本地模型、繁忙度、下线切换）、[帮助：价格]({{< relref "/docs/workbuddy/sources/official/2026-09-24-help-pricing" >}})（套餐与模型调度）、[帮助：积分]({{< relref "/docs/workbuddy/sources/official/2026-10-09-help-credits" >}})（积分与模型单价的关系）、[更新日志]({{< relref "/docs/workbuddy/sources/official/2026-11-03-changelog" >}})（模型相关的功能演变）
- 社区：[数智奔流企业微信实测]({{< relref "/docs/workbuddy/sources/community/2026-10-19-shuzhibenliu-wecom-hands-on" >}})（排队实测、企业控制台的模型配置）
