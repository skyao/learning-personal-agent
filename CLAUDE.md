# Personal Agent 学习笔记

Hugo（Docsy 主题）站点，收集并分析各家 Personal Agent 产品的资料。内容在 `content/zh-cn/`：`docs/<product>/sources/` 是资料页，`docs/<product>/analysis/` 是产品分析，`analysis/` 是跨产品的主题分析。

## 先读 skill

工作流程和约束都写在 `skills/` 下，开始任何工作前先读对应的 skill：

| 要做的事 | 读这个 |
| --- | --- |
| 任何工作（提交推送、路径写法、本机 shell 的坑） | `skills/repo-conventions/SKILL.md` |
| 收集资料（通用规则） | `skills/collect-sources/SKILL.md` |
| 收集某个产品 | `skills/collect-<product>/SKILL.md`（进度、渠道、逐篇判断） |
| 翻译外文资料 | `skills/collect-sources/references/translator.md` |
| 分析（产品维度、主题维度） | `skills/analyze/SKILL.md`，进度见 `skills/analyze/references/progress.md` |

## 几条最要紧的规则

- **一个产品（或一个主题）一个会话。** 当前会话已做过别的产品时，先提交推送，建议用户开新会话。
- **经验写进仓库，不写本地记忆。** 用户会换机器、换用户操作这个仓库；新发现的约定和教训写进对应的 skill（通用的写进 `repo-conventions`），随仓库提交。
- **不写死 home 路径**，用 `$HOME/...` 或相对路径。
- 资料页只由收集一侧写，分析页只由分析一侧写；分析时发现资料页的问题，记入 `progress.md`，不直接改。
- 改完内容运行 `npm run build` 校验，退出码须为 0（relref 写错会报 `REF_NOT_FOUND`）。
