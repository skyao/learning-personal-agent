来源：https://dev.to/tng_thnhnhn_c933ee88b/meta-brings-muse-wonders-memory-and-focus-to-everyone-what-active-memory-and-active-focus-386p
取文：2026-11-09，直接下载

On November 6, Meta started rolling out new models to everyone who uses Muse and Meta AI — not the frontier Muse Wonder model itself, but specialized versions of Meta's existing models, trained using Muse Wonder. The upgrade brings two capabilities from Wonder down to the assistants most people actually use: Active Memory and Active Focus.

If you build with AI agents, this is worth paying attention to, not because of the headline numbers, but because of the pattern: a frontier model acting as a teacher, and the distilled result shipping to the whole fleet.

## What actually shipped

A few weeks earlier, on October 12, Meta introduced the Muse Wonder series — Muse Wonder and the larger Muse Wonder Full — as its most capable models for personal and professional agentic tasks. Wonder is available through the Meta Model API and Muse Code, with Wonder Full for Muse Code subscribers. It was never going to be the model inside the free Muse and Meta AI apps.

What shipped on November 6 is different: specialized versions of the existing models behind Muse and Meta AI, trained using Muse Wonder. Meta says the rollout is underway, and it did not name the specialized models, their sizes, or which regions and account tiers get them first. The charts in the announcement refer only to "Current Muse Model" versus "Previous Muse Model."

## Active Memory: forgetting less of what matters

Active Memory is Meta's name for an assistant that remembers what matters and recognizes when earlier information becomes relevant again, so it can build on your past conversations instead of starting from zero each time.

Concretely, Meta says the models were trained to tell temporary information apart from permanent information, to reason across time, and to distinguish what is still relevant from what has gone stale. In Muse, the improved models show a 2.4x reduction in forgetting critical information needed to help you reach your goals. On Meta's Active Memory evaluation, which measures tasks that correctly use critical context, the current Muse model scores 90%, up from 76% for the previous model.

That framing matters. Memory in agents is usually talked about as storage — how much context you can cram in. Active Memory is a retrieval and judgment problem instead: what to keep, when to surface it, and when to let it go. A model that remembers everything but surfaces the wrong thing at the wrong time is arguably worse than one that forgets cleanly.

## Active Focus: staying on the goal when things go wrong

Active Focus is the other half. It describes a model that keeps working toward a goal when unexpected challenges appear — trying harder, recovering from setbacks, or finding alternatives, rather than stalling or declaring the task done.

Meta says the models were trained on a variety of real-world-style bottlenecks. In Muse, they show a 67% improvement in completing everyday tasks where unexpected issues arise. The specialized models also learned to be better multi-taskers: knowing when to push on your goals independently and when to collaborate live with you, and adapting to steers and clarifications in the middle of a running task without getting confused.

In Meta AI, the same improvements are pitched differently: a better thinking partner that breaks complex problems into clear steps, asks sharper follow-up questions, and keeps up when you change direction mid-conversation.

Meta's own summary score tells the same story in one number. On its Personal Superintelligence Index, the current Muse model scores 47%, up from 38% for the previous model.

## The pattern worth copying: teacher models, fleet models

Strip away the product names and the announcement describes a deployment pattern that is becoming standard across the industry:

1. **Train one frontier model** with the expensive capabilities — in this case, memory judgment and persistent focus.
2. **Use it to teach specialized models** that are cheap enough to serve to everyone.
3. **Ship the capability, not the model.** Users get the behavior; the frontier model stays behind the API and the subscription tier.

For anyone building agents, the lesson is that memory and focus are the two capabilities that decide whether an agent is useful over days rather than minutes. A model that forgets the constraint you stated yesterday, or gives up at the first unexpected error, is a demo, not a coworker. Meta is betting that both problems are trainable — and that the training transfers from a frontier teacher to a smaller student.

## The honest caveats

Every number in this announcement is Meta's own, measured on tests Meta designed, with no independent verification:

- **No baselines for two of the four figures.** The 2.4x forgetting reduction and the 67% improvement have no published starting point, so it is impossible to judge how large the absolute change is.
- **No methodology published.** Meta has not explained what the Personal Superintelligence Index measures task by task, or which test sets sit behind the Active Memory evaluation.
- **No separate figures for Meta AI.** All four numbers describe Muse. The Meta AI side of the rollout has no published scores.
- **No model identity.** The specialized models are unnamed, with no parameter counts, no model card, and no pricing.

The 47% versus 38% index score is best read as a direction of travel, not a benchmark you can compare against any rival. The interesting claim is not the number — it is that memory judgment and task persistence can be distilled from a frontier model into the models that serve everyone. That claim will be tested in daily use, where the only evaluation that matters is whether the assistant still remembers what you told it last week.

*Source: Meta AI Research, [Bringing Specialized Models to Muse and Meta AI](https://research.meta.ai/blog/specialized-models-for-muse-and-metaai), published November 6, 2026. See also Meta AI Research, [Muse Wonder: A Frontier Model For Personal & Professional AI Agents](https://research.meta.ai/blog/muse-wonder), published October 12, 2026.*
