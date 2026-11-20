来源：https://bugbounty.meta.com/blog/securing-muse/
取文：2026-11-19，页面文本抓取（直接下载返回 400 的外壳页）

Bug bounty researchers help us strengthen Muse's security alongside our own adversarial testing. Now, we're helping them dig deeper with new tools and dedicated test environments.

At our Tokyo live hacking event on November 16, we're introducing a new research environment for select Meta Bug Bounty researchers. Participants will receive dedicated test Muse accounts, controlled access to their own test virtual machines (VMs), and private tools to help them study and test Muse's security boundaries.

Testing is limited to these dedicated event accounts, each researcher's own test Muse, and the event's approved scope. No real user accounts or production data are involved, in accordance with the terms of the program.

## Testing Muse's isolation boundaries

Muse's tools run inside an isolated runtime cell, separate from the services that protect credentials and control approvals and network access. For more on this architecture, read How We Built Safety Into Muse.

The research environment is designed to reduce setup and give researchers a clearer view of the system, so they can focus on testing attack hypotheses, validating findings and demonstrating impact.

Controlled access to dedicated test VMs lets researchers:

- Inspect the interfaces and controls around the agent's runtime cell, rather than infer the underlying isolation model solely from black-box product behavior.
- Use synthetic files and data to test isolation boundaries between the runtime cell and security-sensitive services from approved sandbox contexts.
- Use agent assisted workflows to compare behavior, run experiments and organize evidence, while keeping researchers focused on interpreting results and validating findings.

Participants will also receive access to Muse Code to support their agentic research workflows. Researchers define the attack hypothesis, validate findings and demonstrate their impact.

Approved participants will receive private guidance on testing limits and use of the tools. The tools and detailed guide will remain private during early access, with time-bound access for participants.

## What's next

We'll use feedback from the Tokyo live hacking event to keep improving the research tools and expand access carefully to researchers as the controls, documentation, and tooling evolve. This early-access environment is invitation-only. Researchers can continue to report issues through Meta's Bug Bounty program.
