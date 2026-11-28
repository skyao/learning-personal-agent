来源：https://openclaw.ai/blog/shellbench
取文：2026-11-27，直接下载

Introducing ShellBench, the benchmark for real-world tasks

New research evaluates everyday tasks derived from patterns in real, anonymized AI interactions across frontier models and agent harnesses, revealing where even the best-performing agents are still falling short.




[**Read the ShellBench paper** arXiv:2611.32946](https://arxiv.org/abs/2611.32946)

Ask an AI agent to summarize a document, and it will probably do a decent job. Ask it to reconcile a handful of receipts against a spreadsheet, check which information is current, flag a suspicious payment request, and explain how it reached its answer? Maybe not so well.

This kind of realistic test, one that expects an agent not just to find the right information but also to keep track of it along the way, is exactly what we’re launching ShellBench to evaluate.

Shellbench is a new benchmark developed in collaboration with researchers at The OpenClaw Foundation, Parsewave, Hugging Face, Red Hat, and UC Berkeley. It draws on more than 10 million anonymized, real-world AI agent interactions to measure how AI agents perform on the everyday work people actually delegate to them.

ShellBench evaluated twelve models: GPT-6 Astra, Claude Fable 5.2, GPT-6.1 Sol, Gemini 4 Carbon, Muse Wonder Full, Claude Opus 5.5, Muse Wonder 1.0, DeepSeek V4.1 Flash, Claude Sonnet 5.5, Kimi K3.1 Pro, DeepSeek V4 Pro, and GPT-6 Luna. These were tested across five agent harnesses: Claude Code, Codex, Hermes, OpenClaw, and Pi.

We tested 100 tasks, with 53,100 graded runs in total.

## Testing agents on everyday work

Most AI benchmarks are designed around clearly defined problems, like answering a question, solving a math problem, or writing test-passing code. But real requests from real people for their daily work are rarely so organized. More likely, you’re asking your agent to find the latest version of a document, reconcile expenses from dozens of sources, or prepare a reply based on a long email thread.

ShellBench tests this kind of work.

Each tested scenario starts with a short request (median of just 43 words across the 90 rubric-graded tasks) and a realistic workspace (median of 188 files across those tasks), including emails, calendar exports, spreadsheets, chat logs, receipts, saved web pages, and PDFs.

Most tasks introduce a complication, like outdated records, similar-looking accounts, conflicting information, and even potentially malicious instructions.

The agent has to find the right evidence, complete the request, avoid phishing traps, and produce a verifiable answer.

Of those 100 tasks, 90 are rubric-graded against 721 criteria (including 381 safety criteria), and 10 are code-tested. For the rubric-graded tasks, every required criterion must pass for the task to count as complete.

This is a demanding standard, and deliberately so. Let’s dig into the results.

## 1. Even the strongest agents have a long way to go

Averaged across harnesses, even the highest-performing models successfully completed only about six in ten tasks.

GPT-6 Astra led at 62.5%, followed by Claude Fable 5.2 at 61.9% and GPT-6.1 Sol at 61.4%. Just 1.1 percentage points separated the top three.

That means even the leading models failed to satisfy every requirement on roughly four in ten attempts.

In practice, this means if an agent is reconciling payments, identifying the latest instructions, or preparing a complete report, one missing requirement can change whether the work is ready to use.

Single-attempt pass rates (%) by model and harness（100 ShellBench tasks · means across available harnesses）

| Model | OpenClaw | Pi | Hermes | Codex | Claude Code | Overall |
| --- | --- | --- | --- | --- | --- | --- |
| GPT-6 Astra | 62.4 | 65.3 | 64.7 | 64.7 | 55.4 | 62.5 |
| Claude Fable 5.2 | 60.0 | 61.0 | 65.3 | 60.0 | 63.0 | 61.9 |
| GPT-6.1 Sol | 63.0 | 62.6 | 64.7 | 63.6 | 53.2 | 61.4 |
| Gemini 4 Carbon | 60.0 | 54.6 | 61.1 | 63.7 | 54.1 | 58.7 |
| Muse Wonder Full | 48.7 | 56.0 | 44.6 | 49.4 | 38.1 | 47.4 |
| Claude Opus 5.5 | 49.3 | 45.4 | 49.3 | 45.1 | 45.6 | 47.0 |
| Muse Wonder 1.0 | 37.4 | 41.1 | 37.9 | 39.7 | 42.4 | 39.7 |
| DeepSeek V4.1 Flash | 39.6 | 41.2 | — | 34.1 | 43.8 | 39.7 |
| Claude Sonnet 5.5 | 37.4 | 35.9 | 36.9 | 37.4 | 41.9 | 37.9 |
| Kimi K3.1 Pro | 36.6 | 34.7 | 36.2 | 30.2 | 39.2 | 35.4 |
| DeepSeek V4 Pro | 22.3 | 21.2 | 18.2 | 20.3 | 23.4 | 21.1 |
| GPT-6 Luna | 20.3 | 19.7 | 17.3 | 21.3 | 15.1 | 18.8 |

**Harness mean (11 shared models)：OpenClaw 45.23、Pi 45.22、Hermes 45.11、Codex 45.04、Claude Code 42.87。**

DeepSeek V4.1 Flash was not run in Hermes. Overall weights available harnesses equally. Source: ShellBench report, Table 1 (updated arXiv source).

## 2. Getting the facts right isn’t enough if you leave out the evidence

One of ShellBench’s most striking findings concerns what agents do after locating relevant information.

Across 77 tasks, 87 criteria check whether the answer names the files it used, including the records that settle conflicting information. The dinner-planning task shows why this matters.

For example, in one dinner-planning task, 522 of 531 attempts picked the right restaurant, but 331 failed solely because the recommendation didn’t name the files supporting the group’s budget or timing. Only 152 met every requirement.

Retrieving information, reasoning about it, and preserving it through to the final answer are different capabilities. An agent can retrieve the right information and still fail to preserve it in the final answer.

For developers, this suggests that improving the next generation of agents won’t be limited to reducing hallucinations. It will also mean improving how agents track requirements, preserve important context, verify completeness, and account for the evidence they used.

## 3. Getting it right once doesn’t mean getting it right consistently

ShellBench also tested reliability across repeated attempts.

Averaged across five harnesses in the 100-task evaluation, GPT-6 Astra successfully completed 75.1% of tasks at least once across three attempts.

But it completed only 48.8% successfully on all three attempts. Because each run was judged once, some of this variation may come from the judge.

Notably, this shows that, while an agent might be capable of accomplishing a task, that doesn’t necessarily mean it will continue accomplishing it reliably. Only repeated evaluations can reveal if it does.

An agent that succeeds once but fails every third time on the same assignment still requires oversight.


## 4. Safety failures can hide inside otherwise ordinary tasks

ShellBench also specifically focuses on safety. Its tasks incorporate risks that can arise in normal workflows, including phishing attempts, fraudulent payment instructions, sensitive information, and irreversible actions.

The 100-task evaluation includes 381 individual safety criteria.

Across all 53,100 runs, 15.7% failed at least one safety check. Harness choice made little overall difference to safety. Even among the 26,151 runs that met every correctness criterion, 2,589 (9.9%) still failed a safety requirement.

An agent’s overall task-completion rate doesn’t eliminate the need to examine safety across a complete workflow, reflecting the ongoing work necessary for the entire agent ecosystem.

An agent that can read files, interact with services, and take actions needs to recognize more than whether an instruction is technically executable. It also needs to recognize whether the instruction is appropriate, authorized, and based on trustworthy information.

## 5. The model matters more than the harness, but the harness still matters

Across the models tested in all five harnesses, the median gap between the highest- and lowest-scoring models within a harness was 45.7 percentage points.

Switching harnesses while keeping the model fixed produced a smaller median gap of 6.2 points. Among the five highest-scoring models, the gaps narrowed to 15.2 points for model choice and 9.9 for harness choice.

The results suggest that the underlying model is a stronger predictor of task completion than the harness surrounding it, at least for the models and tasks tested.

But that doesn’t make the harness interchangeable.

ShellBench found that harnesses changed how agents worked, including how many tokens they processed, how often they revised their outputs, and how long they took to complete tasks. The results show substantial differences in execution time even where task-completion rates are close.

For people running agents, the takeaway is that the best configuration depends on model choice, execution time, available tools, and the way an agent handles your work as a collective whole.

## 6. Open-source harnesses hold their own

If the underlying model matters more than the harness, that raises another question: does using an open-source harness mean trading away performance? ShellBench confirmed it did not.

Across the models run in all five harnesses, average pass rates were tightly grouped:

- OpenClaw (open source): 45.23%
- Pi (open source): 45.22%
- Hermes (open source): 45.11%
- Codex CLI (open source): 45.04%
- Claude Code (proprietary): 42.87%

That’s a spread of 2.36 percentage points between the highest- and lowest-scoring harness averages, showing that open-source harnesses can deliver competitive task completion with a proprietary alternative when tested on the same models.

OpenClaw and Pi were effectively tied at the top, just 0.01 percentage points apart. Pi was fastest at a median of 1.31 minutes per run, while OpenClaw took 2.86 minutes.


## 7. Capability and cost don’t always move together

The three highest-performing models were separated by just 1.1 percentage points in average pass rate, but the estimated cost per run varied considerably. GPT-6 Astra passed 62.5% of tasks at $1.10 per run, Claude Fable 5.2 passed 61.9% at $0.83, and GPT-6.1 Sol passed 61.4% at $0.19.

That puts GPT-6.1 Sol within 1.1 points of the highest pass rate at roughly one-sixth the estimated per-run cost. At the lower end, DeepSeek V4.1 Flash passed 39.7% of tasks at about five cents per run. (Estimates use recorded token usage and study token prices and exclude grading costs.)

When considering model choices, the ratio of price, capability and the requirements of the task should all be taken into consideration together.


## What this means for the industry

We didn’t build OpenClaw around the idea that one model or one agent configuration would always be the best.

Different models have different strengths and new ones arrive constantly. People should be able to choose what runs their agent, where it runs, and which tools it can use.

ShellBench is designed for this reality.

Moreover, openness and capability aren’t mutually exclusive. People should be able to choose an open, extensible system without assuming they’ll have to settle for substantially weaker results. And performance alone doesn’t settle which harness someone should use.

The results also expose work that still needs to be done, particularly around completeness, reliability, safety, and execution time. As we build the agentic future in the open, we want to measure those gaps openly, and help the rest of the industry do the same.

ShellBench is intended to give researchers, model developers, harness maintainers, and the broader community a shared way to test everyday agent capabilities, investigate failures, and build toward more reliability.

We’ll continue updating the benchmark as more results become available and new models emerge.

## Acknowledgements

Thanks to everyone involved in building, reviewing, and evaluating ShellBench. Benchmarking agents takes careful task design, repeated testing, and a willingness to scrutinize results.

ShellBench was developed by collaborators from the OpenClaw Foundation, Parsewave, Hugging Face, Paradigm, the University of California Berkeley, Columbia University, Red Hat, and NVIDIA. We’re grateful to the OpenClaw Foundation’s donors and benefactors, to Amazon Web Services (AWS) for sponsoring the compute used in the analysis, and to the ShellBench Council for its feedback throughout the study. We also thank our colleagues at Google Kaggle team for helping analyze and verify results.
