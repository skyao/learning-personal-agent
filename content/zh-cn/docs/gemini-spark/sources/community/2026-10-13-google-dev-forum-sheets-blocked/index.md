---
title: "Gemini Spark 无法写入任何 Google 表格：sheets_agent:call 被策略检查拦截"
linkTitle: "开发者论坛：表格写入故障"
date: 2026-10-13
originalTitle: "Gemini Spark cannot write to any Google Sheets — sheets_agent:call blocked by policy check"
sourceUrl: "https://discuss.google.dev/t/gemini-spark-cannot-write-to-any-google-sheets-sheets-agent-call-blocked-by-policy-check/404155"
author: "vailon 等"
publisher: "Google Developer forums"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-05
dateNote: "首帖 2026-10-13，楼主 2026-10-16 回报问题已修复"
tags: [实测评测, 安全]
products: [gemini-spark]
---

{{< source-info >}}

**收录说明**：Google 开发者论坛 Google Workspace Developers 版块的问答帖，收入楼主 vailon 的首帖与 4 条跟进，以及 Abel、DHolloway、Desmond_Lang、Edward_Chu、Jeremy_LaKosh 等用户的回复；论坛页尾的推荐话题未收入。旧笔记 learning-ai-agent 的 Gemini Spark 资料索引引用过这篇。原文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：楼主（个人账号，人在香港）报告 Spark 能读取所有表格，但对任何已有的 Google 表格的写入都会失败，包括设为「知道链接的任何人可编辑」的表格；重新连接 Workspace 也无效。Spark 显示失败的内部工具是 sheets_agent:call，错误为「Failed to verify file permissions: Blocking policy check failed … [PERMISSION_DENIED]」。楼主转述工程团队的答复：在表格中编辑应使用 Sheets 里的 Gemini 侧边栏，而不是独立的 Gemini 应用；其他用户回复遇到相同错误，有人认为「blocking policy check」位于 Gemini 的执行前检查层而不是 Sheets API，可能与账号资格或灰度有关。10 月 16 日楼主回报写入已恢复正常（测试于香港时间 10:14，环境为 Gemini Spark / Tasks 模式），并建议在智能体工具调用失败时自动上报遥测、在聊天中一键提交问题、修复后通知用户。

**保留理由**：用户一手记录的平台侧故障和恢复，并保留了内部工具名与错误信息，说明了 Spark 工具调用和权限检查的一角。

---

[vailon](https://discuss.google.dev/u/vailon)

2026 年 10 月 13 日 下午 4:49

1

你好，

我遇到一个持续存在的问题：Gemini Spark 对所有现有 Google 表格的写入操作都会失败。Spark 能读取表格内容，但无法追加行，也无法以任何方式修改我测试过的表格。

这似乎不限于某个特定表格或文件共享配置。

我测试过的情况：

- 问题影响我测试过的所有 Google 表格。
- 我已确认可以用个人 Google 账号手动编辑并保存这些表格。
- 我还测试了一个临时设为「知道链接的任何人可编辑」的表格。Spark 的写入操作仍然失败。
- 我在 Gemini 中关闭并重新打开了 Google Workspace 连接，问题依旧。
- Spark 能成功读取表格内容。失败只发生在 Spark 尝试写入操作时。
- 这是个人 Google 账号，不由 Google Workspace 组织管理。
- 我位于香港。

Gemini Spark 显示的失败内部工具是：

sheets\_agent:call

报告的错误是：

tool “sheets\_agent:call” failed: InvokeTool stream for “sheets\_agent:call” failed: generic::aborted: Failed to verify file permissions: Blocking policy check failed for event: “” [PERMISSION\_DENIED]

错误摘要：

失败工具：sheets\_agent:call

错误状态：generic::aborted

错误类别：PERMISSION\_DENIED

失败位置：InvokeTool stream for “sheets\_agent:call”

发生时间：2026-10-13, [insert exact time] HKT (UTC+8)

这个问题看起来不像标准的 Google Sheets API 授权错误。我没有收到 Google Sheets API 的 HTTP 403 响应，例如 “insufficientPermissions” 或 “The caller does not have permission.”。相反，请求似乎是在 Spark 执行前的文件权限验证和阻止策略检查期间就被中止了，发生在实际的 Sheets 写入操作执行之前。

我还发现一份被公开索引的 Gemini Community 报告，涉及 Gemini Spark 无法编辑 Google Slides，错误非常相似：

“Blocking policy check failed for event: ‘’ [PERMISSION\_DENIED]”

那份报告描述说，正常的 Drive 访问仍可继续，而用于文件编辑的某个高级 Spark 子智能体失败。我的情况涉及 Google Sheets，失败的工具是 sheets\_agent:call，所以我并不假定这些事件完全相同。不过，相同的错误模式可能表明这是更广泛的 Gemini Spark 子智能体、功能策略、账号资格或灰度推出问题，而不是特定于表格的共享权限问题。

有人能确认或帮助澄清以下问题吗？

1. Gemini Spark 目前是否支持个人 Google 账号通过 sheets\_agent:call 写入现有 Google 表格？
2. 此能力在香港是否可用，还是受地区、账号级别或分阶段推出的限制？
3. 对于个人、未受管理的 Google 账号，哪类策略会触发「Blocking policy check failed for event」错误？
4. 是否有用户侧补救办法，例如特定的重新授权流程、权限重置、账号设置或重新连接步骤？
5. 如果这是已知问题或服务事件，是否有问题跟踪条目、状态页或推荐的支持渠道？

如果 Google 代表要求，我可以私下提供完整的事件 ID、准确时间戳、截图，以及一个不含敏感信息的最小测试用例。我不会公开发布 OAuth 令牌、密码、私人表格链接或健康数据。

谢谢。

[Abel](https://discuss.google.dev/u/Abel)

2026 年 10 月 14 日 上午 5:19

2

我也遇到同样的错误。\
tool “sheets\_agent:call” failed: InvokeTool stream for “sheets\_agent:call” failed: generic::aborted: Failed to verify file permissions: Blocking policy check failed for event: ‘…’ [PERMISSION\_DENIED]

[DHolloway](https://discuss.google.dev/u/DHolloway)

2026 年 10 月 14 日 下午 12:44

3

这个措辞很说明问题，因为「blocking policy check」位于 Gemini 的执行前层，而不是 Sheets API 本身。这往往指向账号资格或灰度推出限制，而不是重新授权能解决的问题。地区可用性在香港也可能起作用。值得检查 Gemini 状态页是否有已知事件；如果没有，下一步就是附上事件 ID 提交报告。

[Desmond\_Lang](https://discuss.google.dev/u/Desmond_Lang)

2026 年 10 月 14 日 下午 8:55

4

我昨天也开始遇到同样的权限拒绝……就在他们推出 Argon 的时候……糟糕的发布，唉。我在美国。

[vailon](https://discuss.google.dev/u/vailon)

2026 年 10 月 15 日 上午 1:32

5

这一切都是从 Spark 被整合进 Chat 开始的。合并后侧边栏变得一团糟——普通聊天和 Spark 任务全混在一起，没有文件夹或标签可以区分。

[vailon](https://discuss.google.dev/u/vailon)

2026 年 10 月 15 日 上午 1:34

6

我已经向 Google 发了求助请求，但问题这么多，我怀疑他们不会回复我。

[vailon](https://discuss.google.dev/u/vailon)

2026 年 10 月 15 日 上午 1:36

7

「附上事件 ID 提交报告」，已经做了。

[Jeremy\_LaKosh](https://discuss.google.dev/u/Jeremy_LaKosh)

2026 年 10 月 15 日 下午 8:14

8

我也遇到了。我在美国。希望它能尽快修好。

[Edward\_Chu](https://discuss.google.dev/u/Edward_Chu)

2026 年 10 月 15 日 下午 11:13

9

我遇到了完全相同的问题，并发送了求助请求。这是回复（见下）。我是不是漏掉了什么？这完全破坏了智能体能力，不是吗？我用的是付费计划，而且这以前能用，现在不能了。

我有来自我们工程团队关于你案例的更新。

根据他们的调查，Google 表格内的编辑和协助应使用 Gemini 侧边栏，而不是独立的 Gemini 应用。直接在表格内使用侧边栏，将为你的工作流提供预期的功能。

[vailon](https://discuss.google.dev/u/vailon)

2026 年 10 月 16 日 上午 2:24

10

Blocking Policy Check 回归问题已解决 + 关于自动遥测派发的功能建议

大家好，

跟进近期关于 `sheets_agent:call` 因内部「Blocking Policy Check」失败而返回 `generic::aborted [PERMISSION_DENIED]` 的事件（大约从 2026 年 10 月初开始），我想报告后端回归问题似乎已**完全解决**。

### 验证更新

- **测试时间：** 2026-10-16 10:14 HKT
- **环境：** Gemini Spark / Tasks 模式直接向 Google 表格追加行，并更新 Google Docs 变更日志。
- **结果：** 直接写入操作现在可以无缝执行，不再触发策略拦截。临时变通方案（例如通过自定义技能强制输出 Markdown/CSV）现在可以安全停用。

### 功能建议：智能体失败的会话内自动遥测与上报

在这次故障期间，最大的痛点是报告 bug 的摩擦：当自主子智能体遇到平台级拦截时，它只是向最终用户返回一条冷冰冰的 trace/错误，完全依赖用户手动捕获日志、起草 bug 工单并提交到社区论坛。

随着 Gemini Agents 承担更深入、多步骤的生产工作流，我想提出一个内置的反馈闭环：

1. **自动事件遥测**：当子智能体的工具调用因意外的平台级门禁（例如带 Event ID 的策略中止）而终止时，智能体应能自动捕获经脱敏处理的系统 trace。
2. **一键上报提示**：UI 可以直接在聊天中提示用户：*「服务器端工具执行失败（Event: ID）。是否要将这份已脱敏的技术日志直接提交给 Google Cloud / Workspace 工程团队？」*
3. **解决通知**：一旦平台热修复部署，智能体或侧边栏可以通知受影响的工作流自动操作已恢复，而不是要求用户定期进行盲测写入。

这将大幅缩短智能体工具链回归问题的平均检测时间（MTTD），并增强开发者对自主智能体工作流的信心。

感谢工程团队推出热修复！
