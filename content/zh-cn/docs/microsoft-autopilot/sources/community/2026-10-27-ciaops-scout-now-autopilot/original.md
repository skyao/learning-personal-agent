来源：https://blog.ciaops.com/2026/10/27/scout-now-autopilot-how-microsofts-always-on-agent-really-works/
取文：2026-11-10，直接下载

Scout, Now Autopilot: How Microsoft’s Always-On Agent Really Works
![Cartoon of a woman standing on a stack of documents looking through binoculars and guiding her colleagues forward](images/img-01-b17da2.png)

Most workplace AI I use still sits there politely, waiting for me to type something. Microsoft Scout is different, and that’s exactly why I think MSPs and SMBs need to understand how it works before someone in the business goes looking for the download link.

Quick housekeeping first. Microsoft introduced Scout at Build in June 2026 as its first “Autopilot” agent. On 25 September it renamed the product itself to Autopilot, describing it as “previously called Scout”. Yes, same name as Windows Autopilot, the device provisioning service, which is entirely unrelated. The docs still say Scout, so I will too.

## So what is it, really?

Scout is an agent that works on your behalf without being prompted every time. The current Frontier release is a desktop app for Windows 11 and macOS. You describe a task in a chat, Scout picks the tools it needs, works through the steps visibly, pauses for your approval on sensitive actions, then hands back the result or saves files to your workspace.

The tools are the interesting bit. Scout can read and write files in an approved workspace folder, run shell commands, drive a browser to fill in forms, and connect to Microsoft 365. That covers Outlook mail and calendar, Teams chats, meetings and transcripts, SharePoint Lists, and files in OneDrive, SharePoint and Teams. It creates Word, Excel and PowerPoint files, remembers your preferences and can spin up parallel sub-agents.

What makes it “always-on” are two background modes. Heartbeat runs check-in prompts every 15 to 120 minutes while you’re away, and Automations run on schedules or triggers you define. The September announcement goes further: Autopilot becomes cloud-hosted, with its own identity, memory and workspace inside your tenant, and you @mention it in Teams, Outlook and documents like a colleague.

Under the hood it’s built on open-source OpenClaw, with Microsoft adding Entra identity and access controls on top.

## The permissions story is where you need to pay attention

Scout operates with the user’s existing Microsoft 365 permissions. It can’t see anything the user can’t. That sounds reassuring until you remember how many SMB tenants I see with broad sharing links scattered across SharePoint. An agent that tirelessly works through everything a user can reach will find your oversharing faster than any auditor.

There’s a finer detail buried in Microsoft’s own Responsible AI FAQ. In the Frontier desktop app, model interactions are processed through GitHub Copilot, under separate terms. When that happens, some Microsoft 365 protections, such as data residency, retention, sensitivity label enforcement and eDiscovery, don’t apply to that processing. That’s why admins must complete an attestation before anyone can use it. Read that page before you tick the box.

Getting access is deliberately fiddly. You need Frontier turned on in the Microsoft 365 admin centre, an Intune policy on devices, the attestation form, and a GitHub Copilot Business or Enterprise seat for each user. Miss any one of those and sign-in fails without a clear message, which will make for entertaining helpdesk tickets.

## How I’d approach it

Treat this as a pilot for a handful of technically capable people, not a rollout. Clean up permissions and sharing first. Keep the approval prompts on and resist the temptation to click “Always allow”. Lock down heartbeat and automation permissions tightly, because those run when nobody is watching. And budget carefully: Microsoft says Autopilot runs on usage-based billing, not the fixed Copilot licence.

I genuinely think agents that follow through are where this is heading. But an assistant that acts is a very different beast from one that answers. The organisations that do well here will be the ones that realised their governance needed to be ready before the agent arrived, not after.

Sources: [Microsoft Scout overview (Microsoft Learn)](https://learn.microsoft.com/en-us/microsoft-scout/overview), [Responsible AI FAQ](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq), [Admin access overview](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview), [Introducing the new Copilot with Home, Code and Autopilot](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)
