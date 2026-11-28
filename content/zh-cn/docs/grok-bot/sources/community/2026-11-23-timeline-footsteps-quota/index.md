---
title: "用脚步取代 cron：我如何把 Grok Bot 的额度消耗降了一半"
linkTitle: "Timeline：脚步省额度"
date: 2026-11-23
originalTitle: "How footsteps cut my Grok Bot quota burn by 50%"
sourceUrl: "https://timeline.place/guides/footsteps-instead-of-cron"
author: "Marcel Marais"
publisher: "Timeline"
language: en
fidelity: 全文
translation: 已翻译
collectedAt: 2026-11-28
dateNote: "日期取页面元数据的发布日期"
tags: [持续执行, 实测评测]
products: [grok-bot]
---

{{< source-info >}}

**收录说明**：直接下载；去掉了作者头像和文首、文末的 Timeline 下载推广框，以及文末的「More guides」列表。作者与「Grok Bot symbiosis」相同，文中的事件来源是自家产品，也提到 Home Assistant、OwnTracks 等替代方案。标题写 50%，正文数据为 568 次降到 274 次（52%）。原文全文存于本目录的 original.md，网站上不显示，已翻译。

**内容摘要**：作者的例行任务每周唤醒 VM 近 600 次，周四 15:20 周额度耗尽。改为按所在位置而非时钟驱动后，每周后台运行从 568 次降到 274 次，减少 52%，周日晚间仍剩 40% 以上额度。做法是手机的到达与离开事件只更新 VM 上的 `/state/presence.json`（不消耗 token），各轮询任务由一个 shell 包装脚本在模型之外先检查位置与租约，不符则直接退出；办公室的 Slack 与 GitHub 检查为 45 分钟租约，在家的浏览器检查为 2 小时租约。作者也承认几项不足：手机没电收不到离开事件、在家办公要手动切换、访问检测太慢不能开门、一次性监视任务容易忘记设过期。

**保留理由**：给出 Grok Bot 后台运行消耗周额度的量化数据和把门控放在模型之外的具体做法，是少见的用量实测。

---

到周四下午，我的 Grok Bot 已经阵亡了。

我甚至不用它写代码（那方面有更好的工具，致敬 [Amp](https://ampcode.com)）。我用它处理背景生活和工作的杂事，而且已经把工作检查限制在工作日 09:00 到 18:00，个人检查在夜间静音，我的例程仍然每周唤醒 VM 近 600 次。而我只是做了自认为最基础的事：每 15 分钟检查一次 Slack 和邮件里的紧急线程，每 20 分钟看一次 GitHub 的 CI 失败和过期分支，每 30 分钟用浏览器查一次包裹和周五餐厅的候补，再加每小时一次的检查来让其余事情保持就绪。

每次运行都会加载记忆和工具 schema，检查一个 API 或打开浏览器标签页，发现无事可做，却仍然用掉每周额度的一部分。到周四 15:20，当我想用它做真正的工作时，额度已经没了。

那些白天运行大多发生在我根本不在正确地点的时候。我出去吃午饭或看牙医时，工作 Slack 和打开的 PR 仍在被轮询；我在办公室时，家里送货的浏览器检查仍整天运行。

## 用脚步取代 cron

我已经让手机把签名的到达和离开事件发送给 Grok Bot（我开发了 [Timeline](https://timeline.place/)，一个带 webhook 和 MCP 服务器的 iPhone 位置历史应用；不过 Home Assistant、OwnTracks 或 Apple Shortcuts 的 POST 也能写入同一个文件）。在那之前，我只用这些停留事件触发通知。周四触顶让我尝试用它们来控制 Bot 究竟何时才被允许运行。

当我用自己所在的位置而不是时钟来驱动时间表后，每周后台运行从 568 次降到 274 次，减少 52%，其中浏览器检查减少得最多。每周额度不再在周中耗尽，到周日晚上仍有超过 40% 留给浏览器调研和我让它做的事。

- **工作日 cron**
  - 568 次/周
  - 工作 09:00 到 18:00，个人 09:00 到 21:00
- **脚步 + 租约**
  - 274 次/周
  - 唤醒次数减少 52%

**每周额度使用情况**

- 纵轴：100%、50%、0%
- 工作日 cron：周四 15:20 触顶
- 脚步 + 租约：使用 58%
- 横轴：周一、周二、周三、周四、周五、周六、周日

一周的后台唤醒与每周额度的对照。工作日 cron 在周四 15:20 耗尽。脚步方案到周日晚上仍剩 42%，可用于真正的工作。

## 到达事件取代一半循环

我把 Slack 和邮件设为 15 分钟一轮，是因为我想在不整个上午开着两个应用的情况下，抓住改期的会议、评审前发来的文档链接，或紧急消息。但大多数日子里，重要消息会在一夜之间堆积，午休出去时又会堆一批。在工作地点的 `stop.arrived` 触发时运行一次摘要，午休回来时再做一次补查，就能处理大部分情况，而不必每刻钟唤醒 Bot。

在 GitHub 上，你忙的时候队友会往 `main` 合并，不稳定的测试会一直红着直到有人发现，所以 20 分钟一次的轮询看起来很诱人。把变基和 CI 清扫移到中午的 `stop.left`，就能在我走去吃午饭时处理这些漂移，等我坐回来时分支又变绿了。

同样的替换对个人检查也有效。购物清单从晚间定时器改为在任意超市的 `stop.arrived` 触发；健身或机场准备只在我到达相应地点时才唤醒。这也顺带取消了每小时一次的编排检查：到达某个地点的停留事件会唤醒那个地点对应的单个例程，而不是每小时轮询每个子智能体。

## 只在合理的地方轮询

有些任务仍然需要定时器：Resy、本地网球场网站和包裹追踪器不发 webhook，所以完全关掉 cron 会让它们失效。

我没有把 Timeline 的 webhook 直接指向 Grok Bot 的每个例程，而是指向 VM 上的一个小端点，它只更新一个纯文本文件 `/state/presence.json`，写入我当前的地点、模式和过期时间。写这个文件不消耗任何 token。

之后每个轮询器只在对应的租约打开时运行。在工作地点，Slack 紧急检查和 GitHub 监视器以 45 分钟为周期解锁，并在 `stop.left` 触发时关闭。在家里，08:00 到 22:30 之间，针对送货、餐厅候补和 Mac 工具（Messages、Notes、Reminders）的浏览器轮询器每两小时运行一次；我一出门旅行就休眠。在健身房或吃晚饭时，什么都不轮询。落地机场或切换时区后，家庭轮询器暂停，由航班和铁路监视器接管。

| 地点 | 轮询情况 |
| --- | --- |
| 在工作地点 | 离开时关闭：Slack 紧急检查 45 分钟；GitHub CI 45 分钟 + gh 门控 |
| 在家里 | 08:00 到 22:30：送货与预订 2 小时；Mac Messages 与 Notes 2 小时 |
| 健身房 / 外出 | 仅 webhook：什么都不轮询，0 token |
| 旅行 | 机场或新时区：航班与铁路监视器 2 小时 |

只有手机报告我位于某个地点时，对应的轮询器才运行。其他一切都以零 token 休眠。

这也有助于 Grok Bot 的 macOS 位置集成。MacBook 要么放在桌上，要么在背包里睡觉，所以它永远不知道你出去吃午饭或离开了城市。让手机持续更新 `/state/presence.json`，就能把 Messages 和 Notes 这类 Mac 工具与你是否在家绑定起来。

## 绝不要为了查你在哪而唤醒 LLM

我最初的尝试保留了直接指向 Grok Bot 的 15 分钟 cron，只在提示词里加了一行：*"First call Timeline's `get_current_location` tool; if I'm not at Work, stop."*（译注：意为「先调用 Timeline 的 `get_current_location` 工具；如果我不在工作地点，就停止。」）这几乎省不下什么。启动一轮智能体对话、加载系统提示词和 MCP schema、调用一个工具、读取回复，仍然每 15 分钟烧掉完整的一轮。

门控必须放在模型之外。在 Grok Bot 的 VM 上，一个简短的 shell 包装脚本会在调用智能体之前读取 `/state/presence.json`。如果地点不匹配或租约已过期，它就以零 token 退出。

`/state/presence.json`

```
{
  "place": "Work",
  "placeKind": "saved",
  "mode": "office",
  "updatedAt": "2026-11-23T08:58:12Z",
  "expiresAt": "2026-11-23T12:58:12Z",
  "timeZone": "Europe/Berlin"
}
```

`run-if-at.sh`

```
#!/usr/bin/env bash
set -euo pipefail

STATE="/state/presence.json"
REQUIRED="${1:?usage: run-if-at.sh <PlaceOrMode> <command...>}"
shift

jq -e --arg req "$REQUIRED" \
  '(.place == $req or .mode == $req) and (.expiresAt | fromdateiso8601) > now' \
  "$STATE" >/dev/null 2>&1 || exit 0

exec "$@"
```

当工具提供快速 CLI 时，在模型前面再叠一道预检查。在工作租约期间唤醒 GitHub 工作进程之前，包装脚本会运行 `gh pr list --author @me --json statusCheckRollup`，检查是否有检查失败或分支落后于 `main`。一切正常时，脚本退出，模型永远不会醒来。

## 仍然糟糕的地方

手机没电时，VM 仍然只能猜。如果我的 iPhone 在 17:30 在办公室没电，`stop.left` 就不会到达，所以我只能依靠一个粗糙的四小时过期时间和 20:00 的工作租约硬停止，来阻止它整夜轮询。

在家或咖啡馆办公仍然要手动切换。仅凭位置无法区分周三在厨房餐桌和周六，所以我必须在聊天中输入 `"working from home until 17:00"`，把 `/state/presence.json` 里的 `"mode": "office"` 翻转过来，解锁工作轮询器。

访问检测对任何即时用途来说都太慢。因为 iOS（`CLVisit`）会等几分钟，确认你是停下了而不是在等红灯，所以这对 45 分钟的 CI 租约没问题，但你仍然不能用它来在走到门口时开前门或开灯。

一次性监视任务仍然很容易忘记。每当我在聊天中随口让 Bot 监视某个航班价格或餐厅桌位，它都会乐于永远轮询下去，除非我记得加上三小时或午夜过期。

## 仍然需要真正 webhook 的地方

生产故障和支付失败 webhook 不应等待脚步事件，也不应放在 15 分钟的轮询里。把 Sentry 或你的可用性监控直接指向推送 webhook，然后让 Bot 检查 `/state/presence.json`，决定是现在打断你，还是留到早上。

这段提示词会在 Grok Bot 上设置 presence 文件、租约过期和 shell 包装脚本：

Grok Bot 设置提示词

```
Set up a Standard Webhooks endpoint for my Timeline stop.arrived and stop.left events and give me the webhook URL and whsec_ signing secret.

1. On every incoming event, update /state/presence.json with: place, placeKind, timeZone, updatedAt, mode ("office" at Work, "home" at Home, "travel" at any airport or foreign timezone, else "away"), and expiresAt (now + 4 hours). Do not wake an LLM turn just to update this file.
2. Wrap all recurring cron jobs in a zero-token shell gate that reads /state/presence.json and exits immediately if the required place/mode does not match or expiresAt has passed.
3. Move Work pollers (Slack urgency, GitHub PR/CI) to a 45-minute Work lease and add a zero-token CLI pre-check before waking the model.
4. Move Home browser pollers (deliveries, bookings, Mac-local checks) to a 2-hour Home lease between 08:00 and 22:30, dormant whenever Home is left.
5. Run one-shot transition routines directly on stop.arrived / stop.left (Work morning brief, midday lunch PR sweep, supermarket list, gym plan) and stay silent on every non-matching stop.
```

（译注：这段提示词要求为 Timeline 的 `stop.arrived` 和 `stop.left` 事件搭建 Standard Webhooks 端点，然后做五件事：每次事件到达时更新 `/state/presence.json` 中的地点、模式与过期时间，且不为更新文件唤醒模型；给所有循环 cron 任务套上读取该文件、不匹配就立即退出的零 token 门控；把工作轮询改为 45 分钟的工作租约，并在唤醒模型前加零 token 的 CLI 预检查；把家庭浏览器轮询改为 08:00 到 22:30 的 2 小时家庭租约，离开家即休眠；在到达和离开事件上直接运行一次性过渡例程，不匹配的停留事件保持沉默。）

有了这些规则，Grok Bot 仍在运行同样的工作和杂事例程，而我不再在周四用完额度。
