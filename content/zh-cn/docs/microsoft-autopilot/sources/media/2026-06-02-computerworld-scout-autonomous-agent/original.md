来源：https://www.computerworld.com/article/4180103/microsoft-unveils-scout-an-autonomous-ai-agent-built-on-openclaw.html
取文：2026-11-10，直接下载

## Scout is the first of a new breed of ‘autopilot’ agents in Microsoft 365 that can carry out tasks independently.
![Microsoft sign and logo on the facade of corporation campus in Silicon Valley. The company headquartered in Redmond, Washington - Mountain View, California, USA - 2019](images/img-01-18e2f9.webp)

Credit: Michael Vi / Shutterstock

Microsoft has developed a new AI agent that can run autonomously around the clock to complete tasks across Microsoft 365 applications.

Microsoft Scout, unveiled at the company’s [Build event](https://build.microsoft.com/en-US/home) Tuesday, is a new type of always-on agent based on the OpenClaw agent framework that Microsoft calls “autopilots.”

These act on a user’s behalf with their own governed Entra identity, [Omar Shahine](https://www.linkedin.com/in/omarshahine), corporate vice president at Microsoft, said in a blog post.

“Autopilots stay active in the background, understand how work gets done across your apps and systems, and take action without needing to be prompted each time,” said Shahine, a Microsoft veteran who recently announced he is leading a new team to bring OpenClaw-based personal assistants to Microsoft 365 apps.

Microsoft Scout connects to apps such as Teams, Outlook, OneDrive, and SharePoint, and accesses data from chat, email, calendar, and contacts. Accessed via Teams, it can also interact with a user’s browser and with external apps via model context protocol (MCP). The tool functions across cloud, desktop, and the web.

Shahine said Scout can reduce mundane tasks that office workers face, such as coordinating and scheduling meeting times with colleagues, or blocking times in a user’s calendar based on upcoming work commitments. “It can also spot risks, like stalled decisions, so you can address them before they become blockers,” he said.

It’s available as an “experimental release” to customers of the company’s Frontier program, Microsoft said, and will require Intune policy configuration and “opt-in attestation.”

Scout is the latest in a range of agentic tools available in Microsoft 365 apps, including [Agent Mode](https://www.computerworld.com/article/4163305/agent-mode-is-now-available-in-microsoft-word-excel-and-powerpoint.html), where users can interact with Microsoft 365 Copilot inside apps such as Word and Excel to create content, and [Copilot Cowork](https://www.computerworld.com/article/4142551/m365-copilot-gets-its-own-version-of-claude-cowork.html) — Microsoft’s version of Anthropic’s Claude Cowork agent that can complete tasks independently.

Despite the company’s big AI push, Microsoft has struggled to convince businesses that Microsoft 365 Copilot is worth the additional cost; it’s advertised at $30 per user each month for large businesses. Around [3% of Microsoft 365 customers pay](https://www.computerworld.com/article/4124591/microsoft-touts-m365-copilot-momentum-claims-15m-paid-users.html) for the add-on subscription, the company said in January, with 15 million paid users. (Microsoft [announced last month](https://www.computerworld.com/article/4166676/microsoft-now-has-over-20-million-paying-copilot-users.html) that that figure has now risen to 20 million.)

It’s not clear whether Scout will be included in Microsoft 365 Copilot subscriptions or charged separately. Microsoft did not immediately provide additional details about pricing.

The launch follows Google’s recent announcement of Spark, an autonomous agent that runs within the Google Workspace application suite. Spark can also be considered a response to the launch of OpenClaw last year, initially under the name “Clawdbot.”

OpenClaw has [drawn scrutiny](https://www.csoonline.com/article/4134540/six-flaws-found-hiding-in-openclaws-plumbing.html) due to [apparent security flaws](https://www.computerworld.com/article/4125939/by-whatever-name-moltbolt-clawd-openclaw-this-uber-ai-assistant-is-a-security-nightmare.html), but Microsoft promises Scout is built with “enterprise-grade security and controls, so it can be trusted in your organization from day one.”

For organizations that have already deployed Microsoft 365 Copilot, Scout doesn’t introduce entirely new data risks, said Jeff Pollard, vice president and principal analyst at Forrester. But it “amplifies whatever data governance problems already exist. The difference this time: instead of surfacing sensitive data to users, it can potentially act on it.

“That makes it an active risk in terms of day to day operations,” Pollard said.

Potential security concerns echo those for AI agents and are exacerbated with personal agents such as Scout: amplified data exposure (since agents can interact with data and use tools autonomously); agent manipulation or prompt injection; unexpected actions, such as using tools or acting in ways that aren’t supposed to be allowed; and observability gaps related to understanding user and agent intent and the explainability of actions.

“However, these tools exist because they make AI far more useful for individuals, so security leaders can’t draw a line in the sand and say “no.” They have to adapt and figure out how to secure them,” said Pollard.

As with most new workplace technologies, Pollard expects adoption to start with “power users” who design and develop the use cases for the agent that can then expand more widely across users.

He warned that the accuracy of tools such as Microsoft Scout can fall short of user expectations. “LLM agents still struggle with goal alignment, multi-step reasoning drifts, and tool misuse,” he said. “Users aren’t always great at explaining what they want and LLM agents aren’t always great at providing what was requested. That’s a continuing problem.”
