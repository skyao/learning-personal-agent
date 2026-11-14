---
name: repo-conventions
description: Personal Agent 学习笔记仓库的通用约定：git 提交与推送、路径写法、本机 shell 的坑。收集、翻译、分析各阶段都适用；开始任何一项工作前读一遍。由用户的本地记忆整理而来（2026-11-14），随仓库保存，换机器、换用户也能看到。
---

# 仓库通用约定

收集（`skills/collect-sources/`）、分析（`skills/analyze/`）等 skill 只写各自阶段的流程；几个阶段都会遇到的约定写在这里。新发现的通用经验也写在这里，不写进某台机器的本地记忆：用户会在不同机器上、用不同用户操作这个仓库，本地记忆换环境后就没有了（用户 2026-11-14 决定）。

## 提交与推送

- 直接在 `main` 上提交、推送（这个仓库的习惯）。提交信息用「阶段: 内容」格式，如 `collect: muse 5 篇`、`analysis: workbuddy 总览与 11 个主题`、`sources: …（某某分析中发现）`、`analyze: progress.md 记入…`。资料页的修改与分析页、进度文件分开提交。
- **推送被拒时先 fetch 再 rebase。** 常有多个会话同时往 `main` 推送（例如一个会话在分析，另一个在收集）。推送被拒（non-fast-forward）时：
  1. `git fetch`，用 `git log --oneline HEAD..@{u}` 和 `git diff --stat HEAD...@{u}` 看远端多了什么；
  2. 确认远端改动与本次改动的文件不重叠后，`git rebase @{u}` 再推送；不用 merge，不用 force；有重叠时停下来告诉用户；
  3. 分析阶段 rebase 之后，重新运行 `inventory.py product <product> --new`：远端新收的 industry 资料可能涉及正在分析的产品。
  4. 报告里告诉用户远端有并行提交。

  依据：2026-11-13 WorkBuddy 分析提交时推送被拒，原因是远端多了另一个会话的 Muse 收集提交；按上面的做法 rebase 后推送成功，`--new` 仍为 0 篇。

## 路径

- 不在 skill、任务说明、脚本里写死 home 路径（如 `/home/sky`、`/home/claude`）。写 `$HOME/...` 或相对仓库根目录的路径；Python 脚本里用 `os.path.expanduser("~")`，或者从脚本自身位置推出仓库根目录（用户 2026-11-14 决定，此前 home 路径变动导致子 agent 读错目录）。
- 临时文件放会话的临时目录（scratchpad），不放进仓库。并行的子 agent 共用同一个临时目录，文件名要带上区分用的前缀。

## 本机 shell 的坑

- **临时函数别用一两个字母的名字。** 用户的 zsh profile 把 `g` 等短名字定义成了别名，写 `g(){ ...; }` 会报 `defining function based on alias 'g'` 和 `parse error near '()'`，整条命令都不执行。用 `chk`、`vrf` 这类名字（2026-11-13 WorkBuddy 分析中遇到）。
- **`grep` 是 ugrep。** 带长上下文的中文正则会超出复杂度限制；核对用 `/usr/bin/grep` 或 Python（2026-11-12 Muse 分析中遇到）。
- **zsh 里单独的 `=` 开头的词会被展开。** `echo ===` 报 `=== not found`，整条命令中止（zsh 把 `=word` 当成命令路径展开）。分隔线写 `echo ---` 或加引号 `echo '==='`（2026-11-14 Poke 分析中遇到）。
- 这几条取决于机器配置，换机器后不一定成立；遇到新的差异就补在这里。
