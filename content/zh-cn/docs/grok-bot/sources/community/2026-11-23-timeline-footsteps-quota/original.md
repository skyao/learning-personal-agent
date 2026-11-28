来源：https://timeline.place/guides/footsteps-instead-of-cron
取文：2026-11-28，直接下载

By Thursday afternoon my Grok Bot was deceased.

I don't even use it for writing code (there are much better tools for that, shoutout [Amp](https://ampcode.com)). I use it for background life and work admin, and even with work checks limited to weekdays 09:00 to 18:00 and personal ones muted overnight, my routines still woke the VM nearly 600 times a week. And I was only doing what I consider the basics: a 15-minute Slack and email check for urgent threads, a 20-minute GitHub watcher for broken CI and stale branches, a 30-minute browser check for a parcel and a Friday restaurant waitlist, and an hourly check-in to keep the rest lined up.

Each run loads memory and tool schemas, checks an API or opens a browser tab, finds nothing to do, and still uses part of the weekly pool. By Thursday at 15:20, when I wanted to use it for a real task, the quota was gone.

Most of those daytime runs fired while I wasn't even in the right place. Work Slack and open PRs kept getting polled while I was out at lunch or at the dentist, and browser checks for home deliveries kept running all day while I was at the office.

## Replacing cron with footsteps

I already had my phone sending signed arrival and departure events into Grok Bot (I build [Timeline](https://timeline.place/), an iPhone location history app with webhooks and an MCP server, though Home Assistant, OwnTracks, or an Apple Shortcuts POST can write the same file). Until then I had only used those stops to trigger notifications. Hitting the Thursday cap made me try using them to control when the bot is allowed to run at all.

Once I drove the schedules from where I was instead of the clock, weekly background runs dropped from 568 to 274, a 52% cut, with the heaviest browser checks cut the most. The weekly pool stopped running dry mid-week, leaving over 40% of it free by Sunday night for browser research and things I ask it to do.

- Weekday cron

  568 runs/wk

  Work 09:00 to 18:00, personal 09:00 to 21:00
- Footsteps + leases

  274 runs/wk

  52% fewer wake-ups

Weekly quota used

100%50%0%Weekday cronCap hit Thu 15:20Footsteps + leases58% used

MonTueWedThuFriSatSun

One week of background wake-ups against the weekly quota. Weekday cron ran dry on Thursday at 15:20. Footsteps reached Sunday night with 42% left for real work.

## Arrivals replace half the loops

I had Slack and email on a 15-minute loop because I wanted to catch a moved meeting, a doc link dropped before a review, or an urgent message without keeping both apps open all morning. Most days, though, the important messages pile up overnight and again while I step out for lunch. Running one summary when `stop.arrived` fires at Work, and a catch-up when I get back from lunch, handles most of it without waking the bot every quarter-hour.

On GitHub, teammates merge to `main` while you are busy and flaky tests sit red until someone notices, which is why a 20-minute poller feels tempting. Moving the rebase and CI sweep to `stop.left` at midday handles that drift while I walk to get lunch, so branches are green again when I sit back down.

The same swap worked for personal checks. Grocery lists moved from an evening timer to `stop.arrived` at any supermarket, and gym or airport prep only wakes up when I arrive at one. That also killed the hourly orchestrator check-in: a stop event wakes the single routine for that place instead of polling every sub-agent on the hour.

## Polling only where it makes sense

Some jobs still need a timer: Resy, a local tennis court site, and parcel trackers don't send webhooks, so turning cron off completely breaks them.

Instead of pointing Timeline's webhook straight at Grok Bot for every routine, I pointed it at a small endpoint on the VM that updates one plain file, `/state/presence.json`, with my current place, mode, and an expiry time. Writing that file uses zero tokens.

Each poller then runs only while its matching lease is open. At Work, Slack urgency checks and the GitHub watcher unlock on a 45-minute cadence and shut off when `stop.left` fires. At Home between 08:00 and 22:30, browser pollers for deliveries, restaurant waitlists, and Mac tools (Messages, Notes, Reminders) run every two hours, then go dormant whenever I leave for a trip. At the gym or dinner, nothing polls at all. Land at an airport or switch timezones, and home pollers pause while a flight and rail watcher takes over.

WhereWhat polls

- At Work

  Closes on departure

  - Slack urgency45 min
  - GitHub CI45 min + gh gate
- At Home

  08:00 to 22:30

  - Deliveries & bookings2 h
  - Mac Messages & Notes2 h
- Gym / Out

  Webhook only

  Nothing polls0 tokens
- Travel

  Airport or new timezone

  - Flight & rail watcher2 h

A poller only runs while my phone says I am in its place. Everything else stays dormant at zero tokens.

It also helps with Grok Bot's macOS Location integration. A MacBook sits on a desk or sleeps in a backpack, so it never knows you went out for lunch or left town. Keeping `/state/presence.json` updated from the phone ties Mac tools like Messages and Notes to whether you are home.

## Never wake an LLM to check where you are

My first attempt left the 15-minute cron pointed straight at Grok Bot and added one line to the prompt: *"First call Timeline's `get_current_location` tool; if I'm not at Work, stop."* That saves almost nothing. Booting an agent turn, loading its system prompt and MCP schemas, calling a tool, and reading the reply still burns a full turn every 15 minutes.

The gate has to sit outside the model. On Grok Bot's VM, a short shell wrapper reads `/state/presence.json` before invoking the agent. If the place does not match or the lease has expired, it exits with zero tokens spent.

/state/presence.json

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

run-if-at.sh

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

Where a tool has a fast CLI, stack one more pre-check in front of the model. Before waking the GitHub worker during a Work lease, the wrapper runs `gh pr list --author @me --json statusCheckRollup` and checks whether any check failed or a branch is behind `main`. When everything is green, the script exits and the model never wakes up.

## Things that still suck

A dead phone battery still leaves the VM guessing. If my iPhone dies at the office at 17:30, `stop.left` never arrives, so I have to rely on a crude four-hour expiry and a 20:00 hard-stop on Work leases to stop it polling all night.

Working from home or a café is still manual. Location alone cannot tell a Wednesday at the kitchen table from a Saturday, so I have to type `"working from home until 17:00"` in chat to flip `"mode": "office"` in `/state/presence.json` and unlock the work pollers.

Visit detection is too slow for anything instant. Because iOS (`CLVisit`) waits a few minutes to make sure you stopped instead of sitting at a red light, this works fine for a 45-minute CI lease, but you still cannot use it to unlock a front door or turn on lights as you walk in.

One-off watchers are still easy to forget. Whenever I casually ask the bot in chat to watch a flight price or a restaurant table, it will happily keep polling forever unless I remember to tack on a three-hour or midnight expiry.

## What still needs a real webhook

Production outages and failed payment webhooks should not wait for footsteps, and they should not sit on a 15-minute poll either. Point Sentry or your uptime monitor straight at a push webhook, then let the bot check `/state/presence.json` to decide whether to interrupt you now or hold it until morning.

This prompt sets up the presence file, lease expiries, and shell wrappers on Grok Bot:

Grok Bot setup prompt

```
Set up a Standard Webhooks endpoint for my Timeline stop.arrived and stop.left events and give me the webhook URL and whsec_ signing secret.

1. On every incoming event, update /state/presence.json with: place, placeKind, timeZone, updatedAt, mode ("office" at Work, "home" at Home, "travel" at any airport or foreign timezone, else "away"), and expiresAt (now + 4 hours). Do not wake an LLM turn just to update this file.
2. Wrap all recurring cron jobs in a zero-token shell gate that reads /state/presence.json and exits immediately if the required place/mode does not match or expiresAt has passed.
3. Move Work pollers (Slack urgency, GitHub PR/CI) to a 45-minute Work lease and add a zero-token CLI pre-check before waking the model.
4. Move Home browser pollers (deliveries, bookings, Mac-local checks) to a 2-hour Home lease between 08:00 and 22:30, dormant whenever Home is left.
5. Run one-shot transition routines directly on stop.arrived / stop.left (Work morning brief, midday lunch PR sweep, supermarket list, gym plan) and stay silent on every non-matching stop.
```

With those rules in place, Grok Bot still runs the same work and errand routines, and I stopped running out of quota on Thursdays.
