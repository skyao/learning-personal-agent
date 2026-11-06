来源：https://www.chatprd.ai/how-i-ai/grok-vs-dot-vs-muse-vs-claude-duet-nine-tasks-four-agents-no-universal-winner
取文：2026-11-06，直接下载

# Grok vs. Dot vs. Muse vs. Claude Duet: Nine Tasks, Four Agents, No Universal Winner

Claire Vo puts four personal agents through nine real tasks. Grok Bot wins the broad work test, Muse handles personal and creative jobs, and the coding favorites expose the limits of an overall score.

![Claire Vo's profile picture](images/img-01-c8e842.avif)

Claire Vo

October 29, 2026·10 min read

## Watch or listen to the full episode

[Watch on YouTube](https://youtu.be/hnCoQ5wB-GU)[Listen on Spotify](https://open.spotify.com/episode/60sosdBzFCkgB5jSQfcIO8)[Listen on Apple Podcasts](https://podcasts.apple.com/us/podcast/grok-vs-dot-vs-muse-vs-claude-duet-which-one-crushes/id1809663079?i=1000798510243)

## Episode chapters

6 chapters

1. [2:14Building the benchmark and checking agent accessClaire selects nine real tasks, uses computer-use operators, and explains the setup differences that limit the comparison.](https://youtu.be/hnCoQ5wB-GU?t=134s)
2. [10:11Slack replies, short clips, and bug fixesDot understands Claire’s preferences, Muse produces the strongest short clip, and coding review reveals a risky validation change.](https://youtu.be/hnCoQ5wB-GU?t=611s)
3. [17:31Figma thumbnails and actionable inbox triageGrok wins on new thumbnail ideas and a document interface that makes to-dos easier to use.](https://youtu.be/hnCoQ5wB-GU?t=1051s)
4. [20:49Family newspapers, homework, and shoe shoppingMuse excels at family-oriented artifacts and fast explanations; Grok handles product comparison best.](https://youtu.be/hnCoQ5wB-GU?t=1249s)
5. [26:25A launch video reverses Claude’s video-editing failureClaude Duet follows the product brief, branding, and voiceover workflow better than the other agents.](https://youtu.be/hnCoQ5wB-GU?t=1585s)
6. [30:14Final ranking and which agent to useGrok leads the overall ranking, Muse stands out for personal tasks, and Claire separates personal agents from her preferred coding tools.](https://youtu.be/hnCoQ5wB-GU?t=1814s)

## Workflows from this episode

3

1. [01Create a Personalized Family Newspaper with Meta's Muse](/how-i-ai/workflows/create-a-personalized-family-newspaper-with-meta-s-muse)
2. [02How to Create a Branded Product Launch Video with Claude Duet](/how-i-ai/workflows/how-to-create-a-branded-product-launch-video-with-claude-duet)
3. [03Generate Novel YouTube Thumbnail Ideas with Grok and Figma](/how-i-ai/workflows/generate-novel-youtube-thumbnail-ideas-with-grok-and-figma)

[All workflows](/how-i-ai/workflows)

Episode outline

Claude Duet wouldn’t download a video to cut a short clip. Later, it made the best product launch video in the entire test, complete with branding and an ElevenLabs voiceover.

That contradiction is more useful than a leaderboard. “Make a video” sounds like one capability until you ask an agent to find footage, download it, choose cuts, follow a design skill, or generate narration. Different jobs expose different strengths—and very different failure modes.

I ran Dot, Grok Bot, Muse, and Claude Duet through nine tasks I actually need done. Grok won the overall ranking. Muse was my favorite for several personal and creative tasks. Dot and Duet did the strongest coding work, but that didn’t make either my preferred general-purpose assistant.

I wanted to know which agent could finish a useful piece of work without making me manage every step.

## A benchmark built around my actual work—and imperfect access

I started by asking each agent for the top 10 tasks it does for me. Then I put those lists into Claude and asked it to build a benchmark around the most common tasks, while testing different capabilities.

The benchmark covered nine jobs I actually needed done:

- Draft a Slack reply.
- Cut a short-form video.
- Fix a Sentry bug.
- Make a How I AI thumbnail.
- Triage my inbox.
- Build a family newspaper.
- Explain a physics question to my fourth grader.
- Shop for shoes.
- Make a ChatPRD Product Intelligence launch video.

I wanted lightweight prompts, written the way I would actually ask for help. My instruction during preparation was: “Keep it in my voice. Do exactly what I would do.” The run sheet included each prompt, responses to likely follow-up questions, and ways to nudge a stalled agent. This wasn’t a competition in elaborate prompt engineering.

Then I used agents to operate the agents. Claude ComputerUse ran [Dot](https://chatgpt.com/features/dots/); [Codex](https://openai.com/codex) operated [Grok Bot](https://x.ai/bot), [Muse](https://ai.meta.com/muse/), and [Claude Duet](https://claude.com/product/claude-duet). Running tasks in parallel was genuinely useful. The operator layer was less reliable: computer use broke, I had to intervene, and I was particularly frustrated with Claude ComputerUse.

I also had Codex use BrowserUse to check connections and skills. That is worth copying even if you never run a benchmark. When several agents have different email accounts and connectors, apparent differences in intelligence can really be differences in access.

And I still missed things. Muse didn’t have Slack or GitHub connected. Claude only had my work calendar for the family newspaper. Existing memories differed, and using different operator agents introduced another variable.

So this was a practical comparison of my setups, not a controlled model evaluation. I judged the outputs openly, recorded my reactions, and gave that transcript to Claude for the final ranking. The reported 93% for Grok and 79% for Duet came from that scoring process; I did not establish a transparent scoring formula. Treat them as summaries of this run, not portable performance statistics.

## Grok’s work advantage was often the artifact, not the answer

The Slack reply was a useful example of why “sounds like me” and “acts in my interests” are different criteria.

A friend at Lovable had asked me to give a talk. The agents with access produced broadly acceptable replies. Grok sounded most like me. Dot, however, asked whether the event was remote and whether I would be paid. Those are material details for someone with a busy schedule who prefers not to leave the house.

Dot understood the decision better, even if the writing task itself wasn’t difficult. Muse couldn’t participate because I hadn’t connected Slack; that was a setup failure, not evidence that it couldn’t draft a reply.

Inbox triage exposed a different distinction. The agents generally found reasonable things to do. Grok delivered them in a Grok document: organized, readable, and equipped with check marks. Claude wanted to use its task follow-up list. Muse, working from Gmail, found parenting obligations ahead of Halloween week. Dot returned a message with roughly five priorities.

For me, Grok’s document was the best working surface. A list buried in a chat message creates more work than an artifact I can actually use. This is why Grok Bot functions as my chief of staff: the interface matters after the reasoning is finished.

Grok also won the thumbnail task. We already had good templates and a [Figma](https://www.figma.com/) MCP connection, so the agents weren’t starting from a blank canvas. Dot and Claude successfully put new content into existing templates. Grok produced new headline and thumbnail ideas that I liked. Muse made a composition with Blair peeking through what looked like creepy curtains. That one was a clear rejection.

![A detailed comparison of AI-generated thumbnail candidates for a podcast episode, showing design iterations and associated project notes.](images/img-02-a853df.avif)

The shopping test reinforced Grok’s advantage in navigation and comparison. I wanted red Adidas Tokyos at a good price. Grok found good options; Muse came close with some steering. Claude repeatedly encountered blocked shopping sites, searched for white shoes with red stripes rather than red shoes with white stripes, and found the most expensive options. Dot barely compared alternatives.

If you’re adapting these tasks, my recommendation is to define the usable output: an actionable checklist, a thumbnail candidate, or a comparison of the correct product and color. That makes it harder to mistake a plausible response for a completed job.

## Muse won the short clip—and the family newspaper

For the short-form video, the agents had access to a transcript and raw footage from our episode with Blair from Reddit. The job was to find the footage in [Dropbox](https://www.dropbox.com/), download it, and cut a clip. I didn’t manually edit the results.

Claude Duet wouldn’t download the video, so it failed before editing began. The other three produced clips, but their choices differed enough to make the winner obvious.

The three clips each had a different problem or strength:

- Grok handled zooming better, but its overlays were ugly; one landed on Blair’s forehead.
- Dot’s clip looked good but lacked punchy cuts.
- Muse used a simple How I AI tag, a familiar caption layout, and stronger pacing. It didn’t have the zoom effects, but I preferred its clip.

Muse won a task I hadn’t previously used it for. I had already been using it to post social content; this result gave me a reason to consider it for creating that content too. A better skill might improve these outputs further, but that was an opportunity to test later, not something this run proved.

The family newspaper made the same preference more pronounced. This is something I print for my kids: the week’s schedule, reminders, weather, and interesting news. I already run a version through my Grok bot, TradBot.

Grok made a useful paper with school information, a “don’t forget” list, Bay Area sports, Halloween content, and weather. Muse made the most appealing family artifact: an illustrated header, a schedule on one page, and day-by-day weather, ideas, and inspiration on a second. It took two pages, which I was happy to accept because the result was inviting.

![A look at 'The Cedar Ledger' family newspaper, showcasing its illustrated front page, weather forecast, and a detailed activity schedule.](images/img-03-c55569.avif)

Dot’s design was poor. Claude produced a Markdown outline after finding it lacked the relevant calendar access. That limitation was real, but instructions for making a newspaper were not the newspaper I had requested.

For readers copying this workflow, the adaptation is straightforward: connect the relevant family information and specify a printable artifact. Then inspect it before printing. A cute layout does not verify a schedule, and the episode’s review focused heavily on presentation rather than an item-by-item accuracy audit.

Muse also won the homework explanation on speed. All four agents correctly answered a velocity-over-time question—the answer was C—and explained it adequately. Muse responded in approximately half a second, by my observation; it was too fast to capture in the timing record. When correctness was effectively tied, responsiveness determined which tool I wanted to use again.

## Coding exposed the danger of a fast, plausible fix

The coding task started with a bug from [Sentry](https://sentry.io/). Muse couldn’t work on it because I hadn’t given it GitHub access. When I suggested assigning it to Devin in [Linear](https://linear.app/), it interpreted Devin as a person rather than an agent.

The other agents took about 10 minutes. I then had what I described in the review as Claude Opus 5.5 grade their fixes.

Dot, using Codex, came closest to the intended fix. Claude Duet found a second bug and also recognized that Dot had already fixed the original issue, concluding it didn’t need to ship more code for that part. That restraint mattered: generating another change is not inherently better than recognizing existing work.

Grok’s fix was the concerning one. It loosened validation, effectively avoiding the problem by accepting something that should have been rejected. It was fast, but speed didn’t make the change correct.

This was a win for Dot and Duet, with extra credit to Claude for the additional bug. It was also a reminder that the overall winner should not automatically get repository access and responsibility for shipping code.

My practical recommendation remains narrower than “use these personal agents to code.” I would use the underlying coding tools—Codex and Claude—directly. Review still needs to establish whether a patch preserves the requirement, rather than simply making an error disappear.

## Claude’s launch video redeemed a very uneven run

The last task was a launch video for Product Intelligence, a feature I was working on for [ChatPRD](https://www.chatprd.ai/). Unlike the short clip, this task had an existing skill intended to guide the output.

Dot produced something closer to a soothing PowerPoint than the launch video I wanted. Grok followed my skill and produced a recognizable version of our video style, but with layout problems and overflowing content.

Muse lacked access to my repository, so I had not set it up to succeed. It nevertheless produced an ambitious video with a British-accented overview—and made things up. The production effort did not compensate for missing product grounding.

Claude Duet delivered the most complete result. It captured the value proposition, used our branding, and avoided the layout problems. It also asked to use the [ElevenLabs](https://elevenlabs.io/) MCP and generated a voiceover. I would have preferred a female voice, or my own recorded voice in ElevenLabs, but the underlying artifact was clearly the best.

That is the distinction worth retaining: Claude failed at downloading and cutting an existing video, then succeeded at a branded product walkthrough. Those should not be collapsed into one “video” capability.

For a repeatable launch-video workflow, my suggested adaptation is to supply the product source material, the existing skill, brand references, and an explicit voice choice. The first three reflect what mattered in this test; specifying the voice addresses the remaining editorial mismatch.

## The verdict: delegate by job, then inspect the handoff

Here’s where I landed after the nine tasks:

- Grok won thumbnails, inbox to-dos, and shoe shopping. It was my best broad work agent in this run.
- Muse was my favorite for the family newspaper, quick explanations, and short-form content. Missing business connections limited what I could test.
- Dot stood out on the Slack reply and code fix.
- Claude Duet did strong bug work and made the best launch video.

Duet was also slow and asked for permission four times, compared with once for each of the others. I want appropriate control, but repeated approval requests can turn delegation into supervision. Muse’s sidebar for permission requests was a useful interface choice.

What is worth copying is the method: test agents on your own recurring jobs, check access before judging, and compare the finished artifacts. For broad work coordination, I would start with Grok Bot. For household tasks and lightweight creative work, I would start with Muse. For coding, I would still go directly to Codex or Claude.

Human judgment remains at the handoff: checking whether a fix preserves validation, whether a video invents product claims, whether a shopping result matches the requested color, and whether an artifact is something you can actually use. The best agent is the one that reduces that burden for the particular job—not the one that merely finishes first.

