来源：https://aihomebuilding.com/stories/muse-wonder-active-memory-2026
取文：2026-11-22，直接下载

Hours before Meta announced Muse Wonder on October 12, Mark Zuckerberg posted a photo of a watermelon. It had been sent to him, he said, by his own Muse assistant, teasing the model's internal codename. Cute, and also revealing, because the thing being teased was not a faster model or a cheaper one but a model that remembers, and the first public artifact of that memory was a private joke between a man and his agent.

Memory is the most intimate thing a machine can offer you, because anyone can answer a question while remembering is what turns a tool into a relationship, and relationships are where the design questions get uncomfortable: what does it keep, how do you correct it, and what happens when it remembers wrong.

So let us look at what Meta actually shipped. Muse Wonder and its larger sibling Muse Wonder Full are the first models Meta calls frontier, built by its Superintelligence Labs for personal and professional agentic work: reading a lease, untangling an insurance claim, making sense of financial or health information, building software, and [two capabilities carry the whole pitch](https://siliconangle.com/2026/10/12/meta-releases-muse-wonder-ai-models-built-to-run-personal-and-professional-agents/): Active Memory carries context about you across conversations and retrieves the relevant details when a task needs them. Active Focus keeps working when a task gets hard, tries other approaches, recovers from errors, and checks in before doing anything important.

Meta research scientist Kavya Kopparapu put it plainly in the launch video: "a tremendous amount of effort into making sure your model can remember what's important to you over days, weeks, months, and beyond." [That is a lovely sentence.](https://pondero.ai/news/2026-10-13-meta-muse-wonder/) It is also a claim about engineering that deserves to be checked against arithmetic.

## The price list is a confession

Wonder is available through the Meta Model API at $4 per million input tokens and $20 per million output tokens. It accepts a context window of roughly one million tokens. Do the multiplication and a single read of a full million-token context costs $4.00. Now imagine the memory Meta is describing, a working recollection of your life carried into every request, and give it a modest size: 200,000 tokens of preferences, projects, ongoing constraints.

That memory costs $0.80 of input on every request. At fifty requests a day, a plausible number for someone who has actually handed their life to an agent, the memory alone costs $40 a day, which compounds to $1,200 a month.

~$1,200/month
What carrying a 200K-token memory into 50 daily requests would cost at Muse Wonder API prices ($4/M input), versus the $20 Power and $100 Maximum flat subscriptions.

Consumer Muse costs $20 a month for Power and $100 for Maximum. At API prices, Maximum would cover about 125 memory-carrying requests before Meta loses money on you, and that is input only, before a single word of output at $20 per million. Nobody is shipping a product where the memory costs twelve times the subscription, which means Meta is not stuffing your history into context wholesale, because it cannot be; Active Memory has to be selective retrieval, a system that finds the relevant sliver of your life and brings only that into the room.

Meta's own phrasing agrees with the math: Active Memory "retrieves the relevant details when needed," not when asked but when needed, which means some system decides what is relevant, out of months of your life, before the model ever sees the question. That retrieval layer is the entire product, because the model is the reader and the retrieval is the librarian, and librarians make judgment calls.

## Recall rots as the pile grows

This is where the independent evidence gets uncooperative. In July 2025, Chroma published a technical report called "Context Rot" that ran 18 models from Anthropic, OpenAI, Google, and Alibaba through tasks that should be trivial at any length: find one fact in a long text, copy a run of repeated words with one odd word in it. Chroma's summary line was blunt: across all experiments, model performance consistently degrades with increasing input length. [The sharpest result used LongMemEval, questions over a long chat history asked two ways.](https://www.matthewswong.com/en/blog/ai-agent-harness-engineering-research/) With about 300 tokens of focused context, Claude Opus 4 scored 0.92, yet with the full 113,000-token history containing the same answers it fell to 0.38: same information, and the pile was the difference.

Anthropic's own engineering guidance, published September 2025, names the mechanism without flinching: a finite attention budget, where every token spends a sliver of it, and where position encoding gets fuzzier the longer the sequence runs. The company calls context rot a performance gradient rather than a cliff, present in every model, and a bigger window does not fix it, because a bigger window is simply a bigger pile.

Meta knows this, and its MemoryBench evaluates recall across 64,000 to 100,000 tokens of multi-turn conversation laced with distractor turns and facts that change mid-stream. That is a serious test design, and it is also Meta's own test of Meta's own claim, run at a tenth of the advertised million-token window with no independent replication yet, which is to say that promising is not proven.

## What the benchmarks do and don't say

On Meta's scorecards, Wonder Full passes 13.1% of tasks on Harvey's Legal Agent Benchmark, a test where a deliverable counts only if it meets every criterion and passes hallucination checks, while Wonder scores 10.0% and GPT-6 Astra, the nearest rival, scores 8.6%. On DeepSWE 1.1, a long-horizon coding test, Wonder Full edges Wonder 79.0 to 78.8, which is noise wearing a lab coat. On AutomationBench-AA, end-to-end business workflows, Wonder Full leads Wonder 45.4 to 39.1. On the Artificial Analysis Intelligence Index, Wonder scores 52 and Wonder Full 56, both trailing Claude Opus 5.5 at 58.

Read the model card's fine print, because Meta included it: competitor runs were best-effort, and "prompts and tools may not have been optimally tuned for them." That is an honest caveat doing quiet work inside a confident announcement. It means the leaderboard is Meta grading Meta's homework with the rivals' papers marked by a tired TA.

Then there is the availability asterisk, and it is doing louder work. Wonder Full, the model that wins the benchmarks, is not on the API at any price; it lives inside Muse Code subscriptions, and Wonder itself reaches the consumer Muse agent "soon," rolling out to subscribers first. What is being celebrated does not yet exist in the product it was built for. You are reading a preview of a recollection.

## The strongest case for it

None of that is fatal, and the counterargument deserves its full weight. Selective retrieval is not a compromise; it is the correct architecture, and the price math that exposes it also vindicates it. A system that decides what is relevant before the model reads is exactly what a finite attention budget demands. Meta trained these models on diverse, long-running tasks specifically to sustain effort across cycles of testing and revision, evaluated focus through its own FocusBench and execution through SWE-Marathon, and built the whole thing at gigawatt scale at the Prometheus data center. The company is also shipping the open-weights sibling, Muse Spark Open, three days later: 816 billion parameters, a million-token window, downloadable, running on two Mac Studios in Meta's demo. Whatever you think of the closed flagship, the lab is showing its work in public.

And the design instinct is right, because an agent that asks for clarification and checks in before important actions is an agent built for the actual failure mode of personal agents, which is not stupidity but confident overreach; Active Focus reads like a response to every demo disaster where the machine did the wrong thing smoothly, and if the memory works half as well as the pitch, living with it will feel less like operating software and more like being known, which is the promise worth wanting.

## What I could not verify

Honesty requires the ledger. I have not tested Muse Wonder, since the consumer rollout had not reached it at publication, and all benchmark figures are Meta's, unreplicated independently. The memory-budget calculation uses illustrative inputs: a 200,000-token memory is my estimate, not Meta's disclosure, and fifty daily requests describes a heavy user. API prices are not Meta's internal inference cost, and cache discounts would soften the numbers without changing their order of magnitude. Chroma's context-rot measurements used mid-2025 models; I found no published study showing the effect has disappeared in current models, and Anthropic's guidance still treats it as the operative constraint. MemoryBench's distractor-turn design is genuinely adversarial, which cuts both ways: it is the right test, and it is their test.

## What to actually do

Do not upgrade to Maximum for the memory, not yet: the model that would justify it is not in the consumer product, and no independent test has measured its recall. When it arrives, treat the first month as an audition by asking it to recall something specific from weeks back, a constraint you stated once, a preference buried in an old thread, a fact you later corrected, and then watch whether it retrieves the correction or the original, because retrieval that cannot forget a superseded fact is not memory; it is a grudge.

Ask the rude questions early: what exactly is being stored, where, and for how long, how you see it, how you delete it, and how you correct it when it confidently remembers something that never happened. Meta calls Wonder its most aligned model to date, trained to protect private information and resist malicious instructions, which matters precisely because this agent will hold your messages, your calendar, your documents. Alignment claims deserve the same treatment as benchmark claims: interesting, unreplicated, pending.

The watermelon photo was charming, but notice what it demonstrated: the agent remembered something personal, surfaced it unprompted, and delighted its user, and every one of those three steps is a design decision someone made about your life. Delight is the easy part; the hard part is the month when it remembers the thing you needed it to forget, and you discover whether the librarian takes requests.
