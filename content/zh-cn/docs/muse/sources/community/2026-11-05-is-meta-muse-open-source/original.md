来源：https://personalagentbench.com/is-meta-muse-open-source/
取文：2026-11-07，直接下载

## Is Meta Muse open source? What is open, and what is not

Is Meta Muse open source? Not the product. The Muse agent, the apps you reach it through and the Linux machine it runs on in Meta's cloud are all closed. The models are mixed. On 15 October Meta released Muse Spark Open, which it calls the open-weight version of Muse Spark, under a licence of its own with commercial conditions. Muse Wonder, announced on 12 October and due to power more of Muse, has no public weights. Meta has not said that Spark Open is the model the Muse agent runs on.

"Meta Muse open source" is not an empty search, then, because Meta has opened three things with the Muse name on them: a kit for building small devices that talk to Muse, released on 2 October 2026; a 30-billion-parameter model called Muse Glimmer, released with open weights in August; and Muse Spark Open in October. None of them lets you run Muse yourself. This page goes through each layer, says where each answer comes from, and points to the two open-source projects that were built to be what Muse is not.

- The Muse agent, its apps and its per-user cloud VM are closed. Meta has described the design in public, and [our teardown](https://personalagentbench.com/agents/muse/) examined it from outside, but no code is published.
- Muse Spark, the model Muse launched on, is offered through APIs. On 15 October Meta also published Muse Spark Open, an open-weight model of 816 billion parameters, under its Muse Model License, which is not an open-source licence. Meta does not say it is the model inside the Muse agent.
- Muse Wonder, announced on 12 October and due to power more of Muse, is API-only. Meta's model card says nothing about releasing its weights, and as of 5 November Meta had published none.
- Muse Glimmer 30B is open-weight under Apache 2.0, distilled from Muse Spark and built to run on your own hardware. It is a separate model, not the one Meta says Muse runs on.
- Muse Gadgets is open source under Apache 2.0, but every gadget needs a token from Meta to pair, so it extends Muse rather than replacing it.


## Is Meta Muse open source? The answer, layer by layer

The Muse name covers several layers, each with its own answer.

- **The app.** iOS, Android, the web, WhatsApp, and since 17 September a Mac app. Closed.
- **The agent and its machine.** Each user gets a Linux virtual machine in Meta's cloud, with the agent, its tools and a gatekeeper Meta calls Sentinel running on it. Closed. Meta has published a detailed account of the design but not the code.
- **The model.** Meta's [launch post](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) says Muse is "powered by Muse Spark," and Meta's [security write-up](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) names Muse Spark 1.3. On 12 October Meta said Muse Wonder will soon power more of Muse, subscribers first. Wonder has no public weights. Spark now has an open-weight version, Muse Spark Open, but Meta has not said that is the one the product uses.
- **Muse Code.** Meta’s separate terminal coding agent is installed from [dev.meta.ai](https://dev.meta.ai/docs/muse-code). Meta announced it [out of beta on 31 August 2026](https://dev.meta.ai/resources/blog/muse-code-new-plans-and-features). Its [public SDK](https://github.com/meta-models/muse-code-sdk) is MIT-licensed, but that repository explicitly excludes the host binary; it does not establish that the full agent runtime is open source.

- **The devices around it.** The [Muse Gadgets SDK](https://github.com/facebookincubator/muse-gadget-sdk) is open source under Apache 2.0.

And separately, there are two open-weight models in the same family, Muse Glimmer 30B and Muse Spark Open. Meta names neither as the model behind the Muse product.

So the short version is: what you would need to run Muse is closed, and what is open sits around the edges of it.

## Meta Muse's agent and VM: closed, but described in public

The part that makes Muse Muse is the agent: one long conversation, memory kept as files, tools it can call, and a gate in front of anything that leaves the machine. All of it runs on a virtual machine Meta provisions for each user, which Meta calls Muse Secure VM. None of that runtime is published as source.

What Meta has published is an unusually detailed description. The security write-up explains that a second agent, Sentinel, is the only thing that can approve a connector action or let network traffic out; that the agent works with stand-in credentials that are swapped for real ones at the network edge after approval; and that approval requests go straight to your app rather than through the conversation. It also says that, for now, staff access to your data is restricted by policy rather than made impossible, and that an encrypted Muse Confidential VM is planned for later.

A published design is not open source. You cannot read the code that enforces it, run it yourself, or check that the build you are talking to matches the description. Our [Muse teardown](https://personalagentbench.com/agents/muse/) got as far as the structure of the requests and the permission sheet of 246 methods, and lists what it could not reach, starting with every request the runtime actually sent to the model.

## Muse Spark and Muse Spark Open: hosted, plus an open-weight version since October

Muse Spark is what Meta's launch post calls its "most capable model to date," and it is the model Meta named for Muse in both its launch post and its security write-up. You can call Spark models through APIs. [OpenRouter's Meta page](https://openrouter.ai/meta) listed Muse Spark 1.1, 1.2 and 1.3, plus the open-weight Spark Open as a hosted model, on 5 November 2026, priced per token like any hosted model.

On 15 October Meta [introduced Muse Spark Open](https://research.meta.ai/blog/muse-spark-open), which it calls the open-weight version of Muse Spark, and put the weights on [Hugging Face](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B). The model card describes a mixture-of-experts model with 816 billion parameters in total and 42 billion active, a 1-million-token context, and text, image, video and audio in with text out. It says this version had extra safety post-training, to make it harder to misuse once it runs without Meta's own guardrails. Meta's post also lists Amazon SageMaker AI, Google Cloud Model Garden and Microsoft Foundry as places to get the weights, and seven hosted API providers, OpenRouter and Together AI among them.

The weights come with conditions. The licence is Meta's own Muse Model License, not an open-source licence. Anything built on the model has to display "Built with Muse Spark Open". A company that offers the model to others as a service, and whose gross revenue together with its affiliates passes $20 million in any 12-month period, has to notify Meta and sign a separate agreement first. Use has to follow Meta's usage policy, and the download sits behind a form asking for your legal name, date of birth and organisation. It is not a home project either: the card puts the compressed weights at about 700 GB of video memory and the full-precision ones at about 2 TB, and Meta's post says it runs on two Mac Studios with M5 Ultra chips.

The release reversed an earlier line before it was signalled. In May, [Implicator reported](https://www.implicator.ai/alex-wang-says-muse-spark-is-not-ready-for-open-source/) Alexandr Wang, who leads Meta's AI work, saying Muse Spark had triggered safety checks that made it unsuitable for open sourcing. In August, [Constellation Research reported](https://www.constellationr.com/insights/news/meta-releases-open-weight-muse-glimmer-model-open-muse-spark-12-tap) that Wang had said Muse Spark 1.2 would get an open-weight version. Neither Meta's post nor the model card says which Spark version Spark Open was built from, and neither says it is what the Muse agent runs on; for the product, Meta has named Spark, and Spark 1.3 in its security write-up.

That matters for anyone hoping to reproduce Muse. Spark Open gives you a large Meta model you can host, not the agent, its tools, its gatekeeper or its VM, and not necessarily the exact model the product calls.

## Muse Wonder: the newer model, and closed

On 12 October Meta [announced Muse Wonder](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/) in two versions, Muse Wonder and Muse Wonder Full, and called them its most capable models to date. According to Meta's [research post](https://research.meta.ai/blog/muse-wonder), Muse Wonder can be called today through the Meta Model API and used in Muse Code, Muse Wonder Full is open only to Muse Code subscribers, and Wonder "will soon power experiences in Muse," reaching subscribers first. Meta gave no date for free accounts.

None of that involves weights. The [model card](https://research.meta.ai/static/muse-wonder-model-card) lists a 1-million-token context, text, image, video and audio in, and text out. On weights it says only that Meta protected them during development and deployment under its weight security programme. Neither the announcement nor the card says anything about releasing them. On 5 November [OpenRouter](https://openrouter.ai/meta) listed Muse Wonder as a hosted model at $4 per million input tokens and $20 per million output, the same hosted arrangement as the Spark API models at a higher price.

One thing to watch for. Hours after the announcement, a Hugging Face account calling itself meta-01 created a repository named muse-wonder. On 5 November it still held no model files, and the account is not Meta Superintelligence Labs, which publishes as meta-models. The meta-models account lists Glimmer and Spark Open, and no Wonder. A download link for "Muse Wonder weights" is not a sign that Meta opened anything.

Meta also says it will use Muse Wonder to build specialised models for everyone who uses Muse. That is about bringing the same level of ability to all Muse users, not a promise of open weights. Glimmer came from Spark through distillation, and Spark now has an open-weight version, but Meta has not said whether anything open will come from Wonder.

## Muse Glimmer: the small open-weight model in the Meta Muse family

[Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) is the smaller of Meta's two open-weight Muse models. Meta Superintelligence Labs published it on Hugging Face on 9 August 2026 under the Apache 2.0 licence, with no gate on downloading it.

The model card describes a dense model of about 29.6 billion parameters with a built-in image encoder, distilled from Muse Spark and "purpose-built for autonomous agentic tasks on consumer hardware." Quantised to around 4 bits, the language model fits in under 20 GB, and the card lists target setups from 24 GB to 64 GB of video memory. It names tool use, failure recovery and multi-step planning as what it was trained for, and says it works with open agent frameworks such as [OpenClaw](https://personalagentbench.com/openclaw-security/) and [Hermes Agent](https://personalagentbench.com/hermes-agent/).

Two cautions. First, Glimmer is not what Meta says Muse runs on; the launch post and security write-up both name Spark. Running Glimmer at home gives you a capable open model from the same lab, not a copy of Muse. Second, "open weights" is not the same as open training. The card says the training data includes publicly available data, licensed data and information from Meta's products and services, and none of that data is released.

Glimmer is still the most useful answer to the question for many people, because Spark Open needs hundreds of gigabytes of video memory or two top-end Mac Studios. If what you want is a Meta-trained model for agent work on hardware you already own, this is it. Our [where it runs](https://personalagentbench.com/where-it-runs/) page sets the hosted agents beside the ones you run yourself, which is where a model like this would go.

## Muse Gadgets: the open-source part of Meta Muse itself

The release that triggered most of the early "Meta Muse open source" headlines is [Muse Gadgets](https://github.com/facebookincubator/muse-gadget-sdk), published on GitHub under Meta's facebookincubator organisation on 2 October 2026.

It contains two device SDKs. One is firmware for off-the-shelf ESP32 boards, so a small board with a screen, a speaker or some sensors can show images, play audio or report readings to Muse. The other is a service for a Raspberry Pi or any spare Linux box, so you can add your own commands and let Muse run chores on it. Gadgets pair with the Muse app on iOS and Android once you switch on a developer mode in its device settings. Meta's README is cheerful about the risks and lists bricked boards and voided warranties among the side effects.

For setup, follow the official [ESP32 quickstart](https://github.com/facebookincubator/muse-gadget-sdk/blob/main/esp32/README.md) or [Linux instructions](https://github.com/facebookincubator/muse-gadget-sdk/tree/main/linux). Obtain the SDK token and review the terms before pairing.

The code is under Apache 2.0, with a few third-party files under their own licences and one exception: the animated avatar is not covered. The bigger limit is in the pairing step. Every gadget needs an SDK token from Meta and is subject to Meta's separate Gadget SDK terms. So Muse Gadgets is open source in the sense that you can read and change the device side. It does not make Muse portable: a gadget with no Muse account behind it has nothing to talk to.

## Open-source alternatives to Meta Muse

If the question behind the search is "can I have something like Muse that I run myself," there are two projects built specifically as an answer, and they made opposite choices.

[OpenMuse](https://personalagentbench.com/openmuse/), from CopilotKit, was published on 15 September under the MIT licence. It runs on a server you control, with a persistent browser and an optional Linux workspace, and the apps are windows onto that server. We read its source rather than probing it. The catch we found is that conversation persistence depends on a hosted CopilotKit service the MIT licence does not cover.

[nanoMuse](https://personalagentbench.com/nanomuse/), from a small team at Zhejiang University, went up on GitHub in late September under GPL-3.0-or-later. It puts a whole agent on each of your devices instead of one agent on a server, and on Android and a computer it can operate other apps through their screens; Meta Muse also has a Mac app that acts in some Mac apps. Its paper is frank that it lacks Muse's per-user VM and the hard security boundary that comes with it.

Neither is affiliated with Meta, neither has been through our exam, and both are young. Each has a page here that sets out what is public and what is still unknown.

## What an open Meta Muse would change

The case for openness here is not abstract. A personal agent holds your inbox, your calendar and a written profile of you, and acts on them while you are away. The questions people most want answered about such a thing, what exactly it sends, what it keeps, and whether the gate in front of a payment really holds, are the ones that are hardest to settle from outside.

Our own work shows the gap. On Muse we could describe the shape of the request and the permission sheet, but we never saw a request leave the machine. [OpenMuse](https://personalagentbench.com/open-source-personal-agents/#openmuse)'s public repository can be inspected; we did not inspect hosted persistence internals or establish every data destination. Neither is a verdict on which is safer, but only one of them can be checked by anyone who cares to look.

Our [Muse teardown](https://personalagentbench.com/agents/muse/) describes a per-user Linux VM where the model request is assembled, and Meta's security write-up is more detailed than most vendors publish. Opening the device kit and two models are real steps. The agent you actually talk to, and the machine it runs on, remain Meta's.

## FAQ

**Is Meta Muse open source?** No. The Muse agent, its apps and the cloud VM it runs on are closed, and Muse Wonder has no public weights. Meta has open-sourced the Muse Gadgets SDK and released two models with open weights: Muse Glimmer 30B in August and Muse Spark Open on 15 October 2026, the second under a licence with commercial conditions.

**Is Muse Spark open source?** Partly, and not under an open-source licence. The Spark models are offered through hosted APIs, and on 15 October 2026 Meta published Muse Spark Open, an open-weight version with 816 billion parameters, under its Muse Model License, which requires attribution and a separate agreement for large model-as-a-service businesses. Meta does not say it is the model the Muse agent uses. Muse Glimmer 30B, distilled from Spark, is the smaller open-weight option.

**Is Muse Wonder open source?** No. Meta announced Muse Wonder and Muse Wonder Full on 12 October 2026 as hosted models, reachable through the Meta Model API and Muse Code. The model card does not mention releasing weights, and the muse-wonder repository on Hugging Face was still empty on 5 November and belongs to an account that is not Meta's.

**What is Muse Glimmer?** A roughly 30-billion-parameter open-weight model from Meta Superintelligence Labs, released in August 2026 under Apache 2.0, built for agent tasks and designed to run on consumer hardware. It is not the model Meta says powers the Muse app.

**What are Muse Gadgets?** An open-source SDK, released on 2 October 2026, for building small devices on ESP32 boards or Linux computers that pair with your Muse. Each gadget needs a token from Meta to pair.

**Can I self-host Meta Muse?** No. The agent only runs on Meta's infrastructure. If you want something in the same shape that you run yourself, [OpenMuse](https://personalagentbench.com/openmuse/) and [nanoMuse](https://personalagentbench.com/nanomuse/) are two independent open-source projects in that shape; the [source comparison](https://personalagentbench.com/open-source-personal-agents/) covers their implementation limits alongside other options.

**Is OpenMuse made by Meta?** No. [OpenMuse](https://personalagentbench.com/openmuse/) is from CopilotKit and [nanoMuse](https://personalagentbench.com/nanomuse/) is from an independent university team. Their names do not establish an affiliation with Meta or the maintainers' reasons for choosing them.
