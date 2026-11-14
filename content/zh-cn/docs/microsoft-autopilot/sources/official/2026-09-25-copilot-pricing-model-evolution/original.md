来源：https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/evolution-of-the-copilot-pricing-model/4559416
取文：2026-11-14，直接下载

You need to know what AI is going to cost so you can plan for it and manage it. That’s a fair ask. As AI becomes more agentic, we’re committed to delivering predictable value for everyday AI, while enabling state-of-the-art AI experiences that deliver more value and cost more to run. That’s why Copilot pricing is evolving to combine predictable per-user pricing with usage-based pricing

## Everyday AI

Everyday AI is what you give your whole workforce. It's covered by the Copilot user subscription license (USL), priced per user per month (the way you've bought software for years), and there are no changes to the value you already have.

We price it this way on purpose. Some vendors put everyday AI work on a meter. We think that's the wrong deal, because when every task has a meter, companies may ration access and only some people get to use AI. We think everyone should.

*Microsoft internal analysis, September 2026. Cost comparison modeled two user profiles across 40 prompts, with each prompt tested 10 times: everyday AI users (15 prompts: 9 Chat, 6 across Word, Excel, and PowerPoint) and advanced AI users (25 prompts: 5 Cowork plus 20 everyday work prompts: 11 Chat, 9 across Word, Excel, and PowerPoint, with a higher proportion of app-based tasks to reflect the advanced user’s broader use of AI across Microsoft 365 apps). Copilot used Auto for Chat and Microsoft 365 apps; Copilot Cowork used Opus 5 and GPT-5.6 Sol with high effort. Claude used Opus 5 with medium effort for Chat, extended thinking for Microsoft 365 add-ins, and Opus 5 with high effort for Claude Cowork. ChatGPT used GPT-5.6 Sol with medium effort for Chat and Microsoft 365 add-ins, and GPT-5.6 Sol with high effort for ChatGPT Work. Copilot costs reflect subscription list pricing, with Copilot Cowork costs calculated using variable rates based on model, context, tools, and runtime. Claude and ChatGPT costs were modeled using publicly available list pricing and API rates at the time of analysis. Costs exclude discounts, promotions, negotiated rates, and other special pricing. Actual results may vary based on customer usage, configuration, pricing, and other factors.*

A fixed price fits everyday AI because of what we call saturation: the point where a more capable model stops changing the result, because the task never needed it. Tasks like turning a meeting transcript into bullet points or summarizing a document from a teammate are saturated.

Auto in the Copilot model picker is built around that idea. When you use Auto, it weighs accuracy, speed, and cost on each request to route to the model and level of reasoning effort best suited to the job. You get the **best quality for a fixed price** without thinking about which model to pick. If you'd rather choose, you can, because model selection is part of the USL. GPT-5.6 and Sonnet 5 are included—and new models like Opus 5 will be included with limits.

The USL has always come with fair use, and that won’t change. We're setting usage limits so that the vast majority of people never reach a limit. For the heaviest users, hitting a limit is not hitting a wall. You get a clear warning first, then a choice: switch your model selection to Auto at no additional cost or move to credits.

The USL is the foundation of Copilot, and we remain committed to adding more everyday value to it.

## Advanced AI

Advanced AI is work you hand off: agents that run for hours, workflows without supervision, business processes rebuilt with agents doing much of the work. A multi-step financial model running all afternoon. Cowork, Code, Autopilot, new advanced experiences in apps like SharePoint, and frontier models like Fable and Astra. When you need the best possible quality or the best model for a task, that work runs on usage-based billing (UBB) with Copilot Credits. UBB builds on the USL, which is required to access these capabilities.

Both the USL and UBB run on models from multiple labs. Today that means OpenAI and Anthropic, with more labs and open-weight models coming soon. The benefit goes beyond choice. Models from different labs have different strengths, so they complement each other.

Think of our commercial model as a plug-in hybrid. The USL is the battery: it covers most of your driving at a fixed monthly cost. UBB is the gas tank, there when a task needs more range than the battery can give. The choice is yours, task by task.

## FinOps

You stay in control. UBB capabilities are visible in the product, because we want everyone to see what Copilot can do. For enterprise customers, UBB services stay off until an admin creates a spending policy in the Microsoft 365 admin center, and nothing is billed before that.

The spending policy is where the decisions get made. Admins set budgets at the tenant and group level, including user-level caps inside group policies, and set alerts when spend hits a threshold. You decide what happens when someone approaches a limit: a warning, a way to request more, or no prompt at all if you'd rather users never see it.

Spend maps to your org the way the rest of your budget does. If you manage departmental costs through Azure subscriptions or resource groups, you can assign usage to the right one, so AI shows up in the same place as everything else that team spends money on. Reporting follows the same logic, broken out by user, group, workload, policy, and payment method.

We’re listening to customers and moving quickly to improve FinOps. Today, we’re rolling out additional capabilities to make AI spend easier to understand, manage, and optimize:

- **More workloads under cost management:** Cost management now covers Code and Managed Runtime alongside Cowork and the Work IQ APIs, with Copilot Studio agents coming in October. More AI workloads will follow.
- **Manage model choice:** Tailor model family access for different groups, giving admins the ability to match the right models to the right user or scenario to maximize value generated. Rolling out in Cowork with plans to expand to additional workloads.
- **Consumption insights for Cowork:** See which scenarios are driving credit consumption and what they produced, so you can decide where to sustain, expand, or optimize.
- **Programmatically manage policies with APIs:** Use Microsoft Graph API to manage spending policies at scale in your own business intelligence and FinOps tools of choice. This helps organizations automate with the systems and processes they already work in.
- **Spend visibility for end users:** Your people can view credit usage, remaining credits, and usage history directly within Microsoft Copilot to manage their own use.

For more information, [see here.](https://aka.ms/finopsforai/optimization)

## What's next

Models keep getting better and more efficient, so some capabilities will start on UBB and move into the USL as the economics allow. Sometimes they'll arrive with a usage limit at first, which lets people use them sooner than they otherwise could.

Most customers already use Copilot for everyday work. As you hand off more complex work, compare the total cost with the alternatives, the way you would for any other investment in getting work done.  
  
To learn more about the new Copilot, [see here](https://aka.ms/AA13g7uq).
