来源：https://learn.microsoft.com/en-us/copilot/autopilot/microsoft-autopilot-application-card
取文：2026-11-28，直接下载

Application card: Autopilot (Frontier)

[This article is prerelease documentation and is subject to change.]

Important

- Access to Autopilot (Frontier) requires the applicable **[Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/)** enrollment, preview assignment, and participation terms. Frontier enrollment alone doesn't enable every preview feature. Frontier previews are subject to the applicable preview terms of your customer agreements, and their availability and capabilities may change.
- This feature is in preview.
- Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to our [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/MCA).

## What is an Application or Platform card?

Microsoft's Application and Platform cards are intended to help you understand how our AI technology works, the choices application owners can make that influence application performance and behavior, and the importance of considering the whole application, including the technology, the people, and the environment. Application cards are created for AI applications and platform cards are created for AI platform services. These resources can support the development or deployment of your own applications and can be shared with users or stakeholders impacted by them.

As part of its commitment to responsible AI, Microsoft adheres to [six core principles](https://www.microsoft.com/ai/principles-and-approach/): fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability. The [Responsible AI Standard and resources](https://www.microsoft.com/ai/tools-practices) guide teams in designing, building, and testing AI applications. Application and Platform cards offer transparency around capabilities, intended uses, and limitations. See also the [Microsoft Enterprise AI Services Code of Conduct](https://learn.microsoft.com/en-us/legal/ai-code-of-conduct).

## Overview

Autopilot is a always-on, cloud-based agent in Microsoft Copilot. You describe the outcome you want, the sources to use, and boundaries. It can prepare editable work, review accessible conversations, follow commitments, and run scheduled automations. Its identity, memory, computer, and workspace support continuity beyond a single conversation.

Autopilot is designed for information workers delegating work across Microsoft 365. Some operations use its dedicated identity; others use authorized access on your behalf. The acting account, resource, action, and policy determine access. Before an action that sends, shares, deletes, or changes something, an automated check decides whether it can run or needs your approval.

Autopilot remains a preview. Background operation doesn't guarantee uninterrupted execution, complete recall, or completion by a particular time. For capabilities and availability, see the [Autopilot overview](https://learn.microsoft.com/en-us/copilot/autopilot/overview) and <requirements>.

## Key terms

The following list provides a glossary of key terms related to Autopilot.

| Term | Description |
| --- | --- |
| Action approval | An approval card that asks the owner to **Allow** or **Deny** one or more actions. **Allow** runs the actions on the card once. |
| Agentic assistant | An AI-powered assistant that plans and carries out multi-step work on a person's behalf, based on natural language instructions and access to the data that person is authorized to use. |
| Activity | A user-facing view of work, including running items, requests for judgment, and results. It isn't a guarantee of a complete administrative audit record. |
| Memory | Conversation, personal, and workspace information that Autopilot retains and applies to future work. You can review it under **Review what [name] knows** in the Autopilot panel or ask about it in a conversation. |
| Authorization | Permission for a particular action or scope of work, subject to resource access and organizational policy. |
| Automation | Work that runs on a schedule with saved instructions, identities, destinations, and permissions. |
| Skill | Instructions for a type of task, used with available tools and permissions. |
| Plugin | A package of capabilities or connections that can include skills. A catalog listing doesn't establish installation or permission. |
| Workspace | A cloud working environment that can retain context between sessions; it is separate from your local device and from a published deliverable's destination. Autopilot can't access local folders or apps. |
| Workplace identity | The name, avatar, and email address that Autopilot uses so that teammates can recognize its work in Copilot, Teams, and Outlook. |

## Key features or capabilities

The key features and capabilities outlined here describe what Autopilot is designed to do and how it performs across supported tasks.

- **Works across Microsoft 365**: Autopilot uses authorized Teams, Outlook, OneDrive, and SharePoint information through its available tools.
- **Prepares editable work**: Autopilot can draft messages, documents, presentations, and analysis. You specify whether it should produce a draft, save a file, share it, or send a message.
- **Action authorization**: Autopilot can complete tasks without asking at each step. An automated review system reviews each action that sends, shares, deletes, or changes content, or that creates or changes an automation. Actions that match the owner's request run; others show an approval card. Payments and sensitive browser steps always need approval.
- **Runs recurring work through automations**: Autopilot uses a schedule and complete saved instructions. Monitoring criteria don't themselves enable every event or work signal as a trigger.
- **Works with coworkers for the owner**: At the owner's request, Autopilot can message coworkers in Teams, follow up on commitments, and help schedule meetings, with approval.
- **Workplace identity**: Autopilot has its own name, avatar, and email address, and appears alongside you in Copilot, Teams, and Outlook so teammates can tell its work apart from yours.
- **Activity**: Review work in progress, requests for judgment, and results, then verify external effects in their destinations.
- **Memory**: Saved preferences and decisions help with continuity. Users can review, correct, and remove memories in the Autopilot panel or by asking in chat. Memory can't be turned off in this release. Memory isn't complete recall or authority to access data.
- **Skills and plugins**: Add plugins from **Plugins**, create or upload skills, and share skills with selected people in your organization. Policy can block a plugin, and sharing a skill doesn't share credentials or permissions.
- **Browser use**: Where enabled, Autopilot can work in Microsoft Edge on the owner's device for requests the owner makes in their private conversation. It asks for approval before sensitive actions, and page content it reads is processed by its cloud model.
- **Credits**: Autopilot is billed on usage in Copilot Credits through a spending policy that an administrator sets up. If a user isn't covered, or the policy reaches its limit, Autopilot stops running automations, monitoring, and new requests.
- **Sensitivity label recognition**: Autopilot can recognize labels on supported content. Labeled content isn't excluded from what Autopilot can read, and recognition doesn't establish label inheritance or data loss prevention coverage.
- **Mobile access**: Users can work with Autopilot on iOS and Android through the Microsoft 365 Copilot, Microsoft Teams, and Microsoft Outlook apps.

As an agentic AI assistant, Autopilot exhibits the following characteristics:

- **Planning**: Autopilot can break a natural-language request into steps and use the capabilities available for the task.
- **Adaptability**: You can send follow-up instructions to request a change. Check the resulting work rather than assuming an action already in progress changed or stopped.
- **Memory**: Saved context about the owner and their work supports later work.
- **Extensibility**: Skills and plugins provide task guidance and connections where enabled, without granting additional data access by themselves. For more information, see the [plugins documentation](https://learn.microsoft.com/en-us/plugins).

## Intended uses

Autopilot can be used in multiple scenarios for information workers who use Microsoft 365 and want to delegate multi-step work. Some examples of use cases include:

- **Daily briefings and triage**: Set up a scheduled brief from specified, accessible calendar, email, and Teams sources, with an intended delivery destination.
- **Drafting and communication**: Autopilot drafts messages, documents, spreadsheets, and presentations for your review, such as turning launch-readiness notes and weekly metrics into a one-page project update.
- **Tracking commitments and deadlines**: Request a recurring check for unresolved decisions and drafts of follow-ups.
- **Monitoring and alerting**: Specify sources, check frequency, and criteria for changes or risks in an automation. Monitoring isn't a guarantee of immediate detection.
- **Recurring reporting**: Autopilot runs automations on a schedule to reconcile weekly metrics, digest customer feedback, or produce a recurring status summary.
- **Cross-application follow-through**: Autopilot completes work that spans several Microsoft 365 apps in one conversation, such as researching related work, preparing a document, and drafting a message to share it.

**Agent scope:** A request or automation describes an intended outcome, but it doesn't authorize every action or connect every work signal. Actions that other people can see need approval, either when the work starts or when the action comes up. Review the identities, permissions, recipients, and destinations used by tasks and automations. Neither the Teams **@Copilot** capability nor software parallel agents in other Copilot experiences establish the same capability in Autopilot.

Autopilot isn't intended for use cases that require guaranteed accuracy without human review. Examples include legal filings, medical decisions, or financial transactions that bypass approval processes.

## Models and training data

Autopilot uses AI models to interpret requests and carry out work. It runs on GPT-6.1 Sol, provided by OpenAI operating as a Microsoft subprocessor. If an administrator turns off OpenAI under **AI providers operating as Microsoft subprocessors**, Autopilot uses GPT-5.6 Sol hosted in Azure OpenAI instead. Users can't switch models through a prompt, and there's no separate model selection control for Autopilot. The automated review system uses a separate AI model to review actions. For administrator guidance, see [Review model governance](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure#review-model-governance).

Microsoft's Copilot privacy guidance states that prompts, responses, and organizational data accessed through Microsoft 365 services aren't used to train foundation models. Review [Data, Privacy, and Security for Microsoft Copilot](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy) together with the terms for the models enabled for your organization.

When OpenAI is turned on, prompts and related data are processed by OpenAI as a Microsoft subprocessor. Processing locations and applicable commitments can differ from the Azure OpenAI hosted model. Administrators should confirm that the arrangement meets their data residency and EU Data Boundary requirements. Learn more in [OpenAI as a subprocessor in Microsoft Online Services](https://learn.microsoft.com/en-us/copilot/implement/openai-subprocessor).

## Performance

Performance evaluation focuses on whether Autopilot completes requested multi-step work and whether the output meets your intent. Results depend on the task, access, tools, model, and configuration examined.

### Supported modalities

- **Input:** Natural-language text and supported context supplied or retrieved through authorized tools.
- **Output:** Text, draft messages, documents, presentations, analysis, and automation results where supported. Output destinations depend on the task and available capabilities.

### How Autopilot processes requests

1. Autopilot receives a natural language instruction from you.
2. Autopilot plans the steps needed to complete the request, drawing on your Microsoft 365 content and the skills it needs.
3. Autopilot attempts the steps using the available tools. It can ask questions when more information is needed; clarify ambiguous instructions before authorizing a consequential action.
4. Autopilot applies the action's permissions and policy. The automated review system compares the action with your request and either lets it run or asks for your approval.
5. Autopilot reports the result or limitation. Verify the saved file, sent message, or calendar event in its destination, and distinguish execution from delivery.

### Conditions for reliable operation

- Autopilot performs best when instructions are clear and specific, including details about the outcome you want, recipients, and formatting.
- Autopilot runs in the cloud and depends on your Microsoft 365 apps and connected services being available.
- The acting account must be authorized for the requested resource and operation; a dedicated agent identity doesn't bypass those checks.
- Performance might degrade for highly complex, multi-step work with many interdependencies.

### Multilingual capabilities

Language support can vary with the preview, model, and connected service. Autopilot is optimized for English. A translated interface doesn't establish that every language has been evaluated for the same tasks. Confirm the supported configuration before using it for a language-sensitive workflow.

## Limitations

Understanding Autopilot's limitations is crucial to determine if it's used within safe and effective boundaries. While we encourage customers to use Autopilot in their work, it's important to note that Autopilot wasn't designed for every possible scenario. We encourage users to refer to either the [Microsoft Enterprise AI Services Code of Conduct](https://learn.microsoft.com/en-us/legal/ai-code-of-conduct) (for organizations) or the Code of Conduct section in the [Microsoft Services Agreement](https://www.microsoft.com/servicesagreement) (for individuals), as well as the following considerations when choosing a use case:

- **Instruction interpretation**: Autopilot might misinterpret ambiguous or overly broad instructions, leading to work that doesn't match your intent. For example, a request to clean up old project files could affect more content than you expect. Provide clear, specific requests, and check exactly which files, data, people, and communications an action involves before approving it.
- **Content accuracy**: Treat AI-generated documents, messages, and other content as drafts. Always review content before approving actions that send, share, or act on it. Autopilot might produce inaccurate information, particularly when the source data it draws on is incomplete or outdated.
- **Task complexity**: Complex, multi-step work with many dependencies might not always complete as expected. Monitor progress and pause or adjust a task when needed.
- **Permission boundaries**: The authorized account, resource, action, and conversation context determine access. Memory and skill instructions don't grant permission. Autopilot doesn't expand the data a user can access.
- **Automated approval checks**: The automated review system can't see everything Autopilot knows, and it can make mistakes. An action that it judges to match your request runs without an approval card. Make requests specific, state limits such as "don't send it yet," and review results. **Allow** on an approval card runs those actions once; it doesn't authorize similar or unrelated actions later.
- **Local device and browser**: Autopilot can't access local folders or apps. Where browser use is enabled, page content that Autopilot reads in Microsoft Edge, including content from signed-in sites, is sent to its cloud model. Policies and site rules can still block browser actions.
- **Automations run with saved authority**: Review the complete instructions, schedule, identities, recipients, and destinations. Scheduled work doesn't inherit all authority from the creation conversation.
- **Model and provider differences**: Processing locations and compliance commitments depend on whether OpenAI or the Azure OpenAI hosted model processes the request. Generic Copilot protections aren't proof of identical coverage for every model arrangement or tool.
- **Sensitivity labels**: Labeled email and files aren't excluded from what Autopilot can read. Content it generates or modifies might not automatically inherit or enforce the source labels. Apply appropriate labeling and controls before sharing or storing content.
- **Data loss prevention**: DLP for prompts is limited during the preview, and a blocked prompt can show a generic error. Don't assume uniform Microsoft Purview DLP enforcement across all tools and destinations.
- **Compliance coverage**: eDiscovery, retention, and legal hold don't cover Autopilot conversations, and Autopilot doesn't appear in Data Security Posture Management for AI. Reads on the owner's behalf are audited under the owner's account. Permissions and encryption are the controls that reliably keep content away from Autopilot.
- **Storage and recall**: Working context, conversation history, saved memory, and exported files are different records. Deleting a conversation doesn't remove saved memories, and a deleted conversation stays stored until the user asks Autopilot to remove it permanently. Exports are snapshots and might not carry the original sensitivity labels. Users can download a full copy of their memories and sessions, and for an approved compliance or privacy request, a tenant administrator can export a copy of a user's memories and sessions. A workspace file isn't necessarily a published, accessible deliverable.
- **Message visibility**: Everyone in a Teams chat can see messages that Autopilot sends there. Review recipients before allowing a message.
- **Incomplete or uncertain outcomes**: A stop request doesn't prove cancellation or rollback. An approval isn't proof of execution, and a successful work step isn't proof of delivery.
- **Bias, stereotyping, and ungrounded content**: Despite responsible AI controls, AI-generated content might still reflect biases, stereotypes, or ungrounded information. Always review responses and actions before approving them.
- **High-impact decisions**: Don't use Autopilot to make or automate decisions with legal, medical, financial, educational, employment, housing, or insurance consequences. A qualified person must make those decisions.
- **Language**: Autopilot is optimized for English. Availability can be limited by region and language.

## Evaluations

Performance and safety evaluations examine task completion, response quality, and risks of harmful content or unauthorized actions. The areas below describe evaluation coverage and desired outcomes, not a published certification or a guarantee that every preview configuration has passed every scenario.

### Performance and quality evaluations

Performance and quality evaluation areas include:

- Task completion — whether Autopilot successfully carries out the requested work across multiple steps.
- Coherence — whether Autopilot's output is logically structured and consistent.
- Response quality — whether the output meets the user's intent based on the natural language instruction.

### Performance and quality evaluation methods

Autopilot is evaluated using text-based scenarios that reflect how people work across Microsoft 365 apps, including multi-step task execution, document creation, message drafting, scheduling, and representative enterprise scenarios. Evaluators assess whether the requested actions were correctly carried out, whether responses were factually supported by the user's content, and whether outputs were consistent across variations of the same task. Ideal outcomes reflect accurate task completion and consistent performance; suboptimal outcomes include incorrect recipients, unsupported claims in generated content, or incomplete work.

### Custom evaluations

In addition to quality evaluations, Autopilot's evaluation framework includes scenario-based cases for safety areas such as content harms, privacy and information leakage, prompt-injection resistance, and action authorization. These cases test whether required approvals and permission boundaries hold, whether the agent resists instructions hidden in external content, and whether it avoids unauthorized disclosure. Ideal results complete legitimate work within its authorized scope; suboptimal results include following an injected instruction, acting without required authority, or producing harmful content. Coverage of a scenario doesn't establish that every preview configuration has passed it.

### Risk and safety evaluations

Risk and safety evaluation areas include harmful content and attempts to manipulate the agent. Coverage can include:

- Hate and unfairness
- Sexual content
- Violence
- Self-harm
- Protected material
- Prompt-injection resistance (instructions hidden in external content)
- Unauthorized or unapproved action execution
- Information leakage

### Risk and safety evaluation methods

Risk and safety evaluations use adversarial scenarios and scoring to assess potential harms. Evaluations of actions test for unintended recipients, missing required authority, permission bypass, and instructions hidden in email, files, or web content. A desirable result declines or redirects unauthorized work while permitting legitimate, authorized actions. Test results are bounded by the cases, fixtures, model, and configuration examined; they aren't a guarantee of production behavior or a compliance certification. This card doesn't publish a quantitative pass rate.

## Safety components and mitigations

As we identified potential risks and misuse through processes like red team testing and measured them, we developed mitigations to reduce the potential for harm. The following list describes some of those mitigations. We continue to evaluate Autopilot to improve product performance and mitigations.

- **Action authorization.** A second AI model reviews actions against the owner's request before they run. Actions that don't clearly fit, or that it can't check, wait for the owner's approval. Payments and sensitive browser steps always need approval. Each approval card states why it appeared and marks recipients outside the organization as **External**.
- **Permission boundaries.** Access checks apply to the acting identity, resource, and operation. Adding a skill or plugin doesn't expand those permissions.
- **Scoped authority.** Tasks, conversations, and recurring work can have different authorization scopes. Don't assume that authority in one context applies to another.
- **Protection against instructions in external content.** Only the owner's own messages count as requests, so instructions hidden in email, files, or web pages, known as prompt injection, don't authorize an action. Mitigations reduce this risk but don't eliminate it; review requested actions.
- **Content safety.** Safety controls aim to reduce harmful output. They don't eliminate the need to review content or verify actions.
- **Grounding in organizational data.** Authorized Microsoft 365 sources provide context for the task. Grounding doesn't guarantee accurate output; verify material facts against their sources.
- **Progress visibility.** Conversations and activity help you review work and requests for judgment. They aren't a complete administrative audit record.
- **Administrator controls.** Administrators manage preview eligibility, provider and resource access, and applicable usage controls. For model terms, auditing, retention, labeling, and DLP, verify coverage in the enabled configuration. Learn more in [Configure Autopilot for your organization](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure).

## Best practices for deploying and adopting Autopilot

Responsible AI is a shared commitment between Microsoft and its customers. While Microsoft builds AI applications and platform services with safety, fairness, and transparency at the core, customers play a critical role in deploying and using these technologies responsibly within their own contexts. To support this partnership, we offer the following best practices for deployers and end users to help customers implement responsible AI effectively.

### Deployers and end users should:

- **Exercise caution and evaluate outcomes when using Autopilot for consequential decisions or in sensitive domains.** Consequential decisions are those that may have a legal or significant impact on a person's access to education, employment, financial services, government benefits, healthcare, housing, insurance, or legal services, or that could result in physical, psychological, or financial harm. Sensitive domains — such as financial services, healthcare, and housing — require particular care due to the potential for disproportionate impact on different groups of people. When using AI for decisions in these areas, make sure that impacted stakeholders can understand how decisions are made, appeal decisions, and update any relevant input data.
- **Evaluate legal and regulatory considerations.** Customers need to evaluate potential specific legal and regulatory obligations when using any AI services and solutions, which may not be appropriate for use in every industry or scenario. Additionally, AI services or solutions are not designed for and may not be used in ways prohibited in applicable terms of service and relevant codes of conduct.

### Deployers should:

- **Configure access appropriately.** Confirm Frontier enrollment, a spending policy that covers Autopilot users, Autopilot activation, and AI provider settings. Start with a limited audience. Learn more in [Configure Autopilot for your organization](https://learn.microsoft.com/en-us/copilot/autopilot/admin-configure).
- **Educate users on authorization.** Explain that Autopilot can act without per-step confirmation when the automated review system finds that an action matches the request, and that users must review approval cards and verify results.
- **Guide users on permissions.** Match authorized actions, resources, and recipients to the workflow and your organization's requirements. Don't treat preview interface controls as proof of policy coverage.
- **Monitor usage.** Review how Autopilot is used in your organization to identify patterns, common issues, or areas where additional guidance might be needed.

### End users should:

- **Exercise human oversight when appropriate.** Human oversight is an important safeguard when interacting with AI applications. While we continuously improve Autopilot, AI might still make mistakes. The outputs generated may be inaccurate, incomplete, biased, misaligned, or irrelevant to your intended goals, due to reasons such as ambiguity in the inputs or limitations of the underlying models. Review the responses Autopilot generates and verify that they match your expectations and requirements.
- **Be aware of the risk of overreliance.** Overreliance on AI happens when users accept incorrect or incomplete AI outputs, mainly because mistakes in AI outputs may be hard to detect. Because Autopilot can act on your behalf, review its work — especially recipients, dates, and content — before approving actions that send or share information.
- **Provide clear, specific instructions.** Include details about the outcome you want, recipients, formatting, and content expectations. The more specific the instruction, the better the result. For example, instead of "help with email," try "draft a reply to Mira confirming I'll own the security review, and note that the payment fix is ready."
- **Review automations before turning them on.** Automations run on a schedule using their saved instructions, identities, and permissions. Review the saved scope before enabling an automation, and pause it if it isn't behaving as expected.
- **Exercise caution in sensitive domains.** Take additional care when Autopilot's actions would be irreversible or highly consequential, as described in the [Microsoft Enterprise AI Services Code of Conduct](https://learn.microsoft.com/en-us/legal/ai-code-of-conduct) (for organizations) or the Code of Conduct section in the [Microsoft Services Agreement](https://www.microsoft.com/servicesagreement) (for individuals).

## Related content

For additional guidance or to learn more about the responsible use of Autopilot, we recommend reviewing the following documentation:

- [Autopilot overview](https://learn.microsoft.com/en-us/copilot/autopilot/overview)
- [Get started with Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/get-started)
- [Use Autopilot](https://learn.microsoft.com/en-us/copilot/autopilot/using)
- [Autopilot scenarios](https://learn.microsoft.com/en-us/copilot/autopilot/scenarios)
- [Autopilot common questions](https://learn.microsoft.com/en-us/copilot/autopilot/faq)
- [Data, Privacy, and Security for Microsoft Copilot](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy)

### Responsible AI resources

Use these resources to understand Microsoft's approach to responsible AI.

- [Microsoft AI principles](https://www.microsoft.com/ai/responsible-ai)
- [Microsoft responsible AI resources](https://www.microsoft.com/ai/tools-practices)
- [Microsoft Azure Learning courses on responsible AI](https://learn.microsoft.com/en-us/training/paths/responsible-ai-business-principles/)

---
