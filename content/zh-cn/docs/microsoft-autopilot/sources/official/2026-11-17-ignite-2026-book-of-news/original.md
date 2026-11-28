来源：https://news.microsoft.com/events/ignite/2026/book-of-news/
取文：2026-11-28，直接下载

## Introduction

### What is the Book of News?

Instant Summary:

The Microsoft Ignite 2026 Book of News is a guide to key announcements at the event. You can explore topics with the interactive Table of Contents and click the Translate button in the lower-right corner to read in different languages. If you have questions or feedback about the content, please email [[email protected]](https://www.microsoft.com/cdn-cgi/l/email-protection#bfdac9dad1cbdcd0d2ffd2d6dccdd0ccd0d9cb91dcd0d2). If you’re interested in speaking with an industry analyst about the announcements or Microsoft’s broader strategy and product offerings, please contact [[email protected]](https://www.microsoft.com/cdn-cgi/l/email-protection#384f5d554b59565954414b4c4a5d54594c5157564b784f5d154f574a545c4f515c5d165b5755).

The Microsoft Ignite 2026 Book of News brings together the event’s key announcements in one interactive guide. Readers can browse topics through the Table of Contents, translate the content into other languages and contact the event team or analyst relations for more information.

## Azure

Instant Summary:

AI has moved into production, and agents need the whole stack. Azure brings silicon, infrastructure, data and operations into one system. **Azure Cobalt 200** virtual machines, **Azure HorizonDB**, **Rayfin** and **Fabric apps** are now generally available. New previews bring **Microsoft Foundry** models and agents to **Azure Kubernetes Service**, with **Azure SRE Agent** and expanded **confidential computing** to operate and protect them.

These updates and the ones listed below mark the next chapter of Azure: built from chip to agent, with the security and control organizations need to run AI at scale.

Azure is unifying silicon, infrastructure, data and operations to help organizations run production AI and agents at scale. Azure Cobalt 200 virtual machines, Azure HorizonDB, Rayfin and Fabric apps are now generally available, while new previews extend Microsoft Foundry to Azure Kubernetes Service (AKS) and add Azure SRE Agent capabilities and confidential computing protections.

### Brand, infra & silicon

#### Azure Chaos Studio Workspaces, AKS extension now generally available

Instant Summary:

Azure Chaos Studio Workspaces and the Azure Chaos Studio extension for Azure Kubernetes Service (AKS) are now generally available, expanding the ways organizations can test how applications respond to and recover from disruptions. These updates expand Azure Chaos Studio, a managed service that allows organizations to introduce controlled failures into applications to test how they respond and recover.

Azure Chaos Studio Workspaces provide a simpler way to organize and run resilience tests. Organizations can define the resources they want to test and apply reusable scenarios that represent disruptions, such as the loss of an availability zone or database failover. This makes it easier to test how an application responds to realistic disruptions and repeat those tests over time.

The Azure Chaos Studio extension for AKS brings resilience testing to applications running on AKS. The extension requires fewer permissions to run experiments, providing a more secure way for organizations to introduce controlled disruptions to Kubernetes pods and observe how applications respond and recover.

These updates help organizations validate whether applications can recover from disruptions as expected. By introducing failures in a controlled environment, organizations can identify weaknesses and make improvements before similar failures occur unexpectedly.

[**Learn more about this news**](https://aka.ms/chaosstudio/workspaces-ga)**.**

Azure Chaos Studio Workspaces and the Azure Chaos Studio extension for Azure Kubernetes Service are now generally available, giving organizations safer, simpler ways to test application resilience. Teams can organize reusable disruption scenarios, simulate events such as availability-zone loss or database failover, and introduce controlled disruptions to Kubernetes pods with fewer permissions — helping uncover weaknesses before real incidents occur.

#### Azure expands confidential computing for protecting highly sensitive data

Instant Summary:

Microsoft Azure is expanding its confidential computing offerings to help organizations unlock more value from data, scale AI innovation and collaborate with greater confidence and control — protecting not only where data is stored and how it moves, but also how it is processed. Three offerings are now in preview:

- VR72 multi-GPU confidential computing that will advance Azure’s confidential computing AI roadmap and open a path to protect large models that extend beyond a single GPU.
- Azure Confidential Enclaves and AKS Kata CoCo confidential containers, whichwillcreate a smaller trusted execution environment within a broader virtual machine. This will help businesses narrow what must be trusted and verified instead of placing that trust in the entire surrounding system.
- Azure Confidential Clean Room, which will enable organizations to bring data together for multiparty analytics while helping protect each participant’s sensitive raw data from other collaborators and cloud operators. This will open new opportunities to generate shared insights without giving up control of protected information.

[**Learn more about this news.**](https://aka.ms/acc-ignite2026)

Azure is expanding confidential computing with three previews designed to protect sensitive data while it is processed. VR72 multi-GPU confidential computing opens a path to securing models that span multiple GPUs; Azure Confidential Enclaves and AKS Kata CoCo confidential containers reduce the trusted environment; and Azure Confidential Clean Room enables multiparty analytics without exposing participants’ raw data.

#### Built for the agentic AI era, Azure Cobalt 200 virtual machines are now generally available

Instant Summary:

Azure Cobalt 200 virtual machines (VMs), built on Microsoft’s own Arm-based processor, are now generally available. They will be deployed in 24 Azure regions by the end of the year, adding to existing datacenter deployments in Australia East, Central US, East US, Indonesia Central, Italy North, South Central US, Spain Central, Sweden Central, UK South, West US 2 and West US 3.

Cobalt 200 was built for AI agents, which do much of their work outside the AI model on general-purpose central processing units (CPUs). Because agents constantly spin up temporary workspaces, CPU speed shapes how fast tasks get done. Cobalt 200 VMs deliver up to 50% better CPU performance than Cobalt 100, so organizations can also do more with the same number of machines.

Cobalt 200 VM customers can now set each VM to a consistent-speed mode or a boost mode for peak speed. Two new VM types serve large in-memory databases (Mpsv4) and storage-heavy jobs such as search, with up to 23 TB of built-in storage (Lpsv5).

[**Learn more about this news**](https://aka.ms/Cobalt200VMs-GA)**.**

Azure Cobalt 200 virtual machines, powered by Microsoft’s Arm-based processor, are now generally available and planned for 24 Azure regions by year-end. Built for the CPU-intensive work surrounding AI agents, they deliver up to 50% better CPU performance than Cobalt 100, add consistent-speed and boost modes, and introduce VM options for large in-memory databases and storage-heavy workloads with up to 23 TB of built-in storage.

### Core

### Azure expands agentic operations with new monitoring, AI capabilities

Instant Summary:

Agentic operations bring AI agents directly into Azure, helping teams investigate issues faster, optimize resources continuously and act with greater confidence. **Expanded** **agentic capabilities** **across Azure Monitor, Azure Copilot and Azure SRE Agent** will deliver richer operational context, stronger governance and a common foundation for operational agents, while keeping humans in control.

**New natural language capabilities**, now generally available in Azure Monitor, help users plan and deploy cloud workloads. Azure Copilot spaces and custom skills, in preview, will allow teams to tailor agents for faster, more efficient and accurate operations while carrying persistent context. Users will also be able to extend agentic operations to Oracle and SAP through Azure Workload Center, in preview, for workload health monitoring and configuration validation.

New Azure SRE Agent capabilities, in preview, will enable **secure agentic operations at enterprise scale**. Customer-managed keys will give teams full control of agent data, while Entra Agent ID and Agent 365 integration will provide users with a consistent way to discover, govern, audit and manage agents throughout their lifecycle. Cross-agent communications will enable context and task-sharing across agents for faster incident resolution. Azure SRE Agent will also integrate with Microsoft Teams and extend investigations across multicloud environments. These updates will help organizations move from agent experimentation to deployment across complex production environments.

Azure Monitor health models, now generally available, **turn telemetry into actionable health context**. Users can translate telemetry into a real-time health graph that connects application architecture, dependencies and business priorities. This helps teams understand what is affected, distinguish platform issues from application failures and prioritize incidents by business impact. The same context enables AI agents to investigate issues, identify root causes, recommend remediation and automate workflows.

[**Learn more about this news**](https://aka.ms/ignite2026/agenticops).

Azure is broadening agentic operations across Azure Monitor, Azure Copilot and Azure SRE Agent so teams can investigate incidents faster, optimize resources and govern operational agents at enterprise scale. New and preview capabilities add natural-language operations, persistent custom context, SAP and Oracle monitoring, customer-managed keys, cross-agent communication, Teams and multicloud integration, plus generally available health models that turn telemetry into business-aware, actionable context.

### Azure infrastructure foundation for production AI applications and agents

Instant Summary:

New capabilities built for the unique needs of production AI applications—from agent networking and security to isolation, confidentiality, context and state—will span an AI foundation across compute, storage and networking.

**A continuous experience from Microsoft Foundry to Azure:** Microsoft Foundry lets customers deploy in a fully managed environment and easily extend to Kubernetes for greater control over infrastructure performance, security and economics. Customers will now be able to deploy open-weight models and agents from Foundry to their own Azure Kubernetes Service (AKS) clusters using infrastructure, security policies and governance they already have. Teams will be able to choose GPUs and regions based on cost, latency and data residency. Foundry will handle setup, enabling the same developer workflow from experimentation through production. This will combine Foundry’s simplicity with Kubernetes’ flexibility and control.

**Azure AI infrastructure**: For production AI, infrastructure directly determines agent performance, security and operating cost. Azure’s latest capabilities will optimize the underlying infrastructure for inferencing and agents, linking infrastructure decisions and business outcomes:

- **Agent Grid** will secure interactions among agents, models, tools and Azure services with centralized policy enforcement.
- **Agent Sandbox extension for AKS** will run agent-written code in sandboxes isolated at the virtual-machine level.
- **Flex nodes for AKS** will extend the same AKS clusters to customer servers outside Azure.
- **Azure Cobalt 200** virtual machines add CPU performance for services around AI models.

**Openness and choice**: Azure’s AI foundation is built to stay open. Open-source projects, including vLLM, Ray and Kubernetes, keep workloads portable, and Microsoft is the largest public cloud contributor to Cloud Native Computing Foundation projects over the past three years.

All capabilities are in preview except Azure Cobalt 200, which is generally available.  
  
[**Learn more about this news**](https://aka.ms/ai-infra-ignite26).

Azure is extending Microsoft Foundry into Azure Kubernetes Service so organizations can move open-weight models and agents from experimentation to production using their existing infrastructure, security and governance. Preview capabilities — including Agent Grid, Agent Sandbox extension for AKS and Flex nodes for AKS — strengthen networking and isolation, while generally available Azure Cobalt 200 VMs boost the CPU services surrounding AI models. Support for vLLM, Ray and Kubernetes keeps the foundation open and portable.

### Introducing Azure Catalyst

Instant Summary:

**Azure Catalyst** is a new, unified experience for agentic modernization across Azure and GitHub that helps organizations modernize infrastructure, applications and data, and accelerate AI transformation. It is generally available.

Azure Catalyst brings together AI-powered discovery, planning, migration and modernization to help IT teams and developers work across the modernization lifecycle. By connecting estate-wide insights with agent-assisted execution in Azure Copilot and GitHub Copilot, organizations can reduce manual effort, modernize complex systems and unlock the business logic within existing applications to build new AI-powered experiences and agentic business processes.

Azure Catalyst brings together new and expanded capabilities, including:

- **Azure Catalyst agent** (formerly Azure Copilot migration agent), now generally available, with new capabilities in preview that extend the agent from migration planning into deeper modernization and execution. Enhancements include richer estate insights, AI-powered application discovery, modernization strategy and cost comparisons, and expanded planning and execution across applications, databases, storage and networking.
- **GitHub Copilot modernization updates**, including agent governance rulebooks, bring-your-own-model support in command-line interfaces and integrated development environments, now generally available. New capabilities, in preview, expand modernization scenarios like integrated application and database modernization, and migration from BizTalk to Azure Logic Apps.

[**Learn more about this news**](https://aka.ms/modernization-ignite26).

Azure Catalyst, now generally available, unifies AI-powered discovery, planning, migration and modernization across Azure and GitHub. The experience connects estate-wide insights with Azure Copilot and GitHub Copilot execution, while an enhanced Azure Catalyst agent, governance rulebooks, bring-your-own-model support and new preview scenarios help teams modernize applications, databases, storage, networking and BizTalk environments with less manual effort.

### Introducing Windows Server 2028

Instant Summary:

For enterprises that depend on Windows-based applications and infrastructure, Windows Server provides a trusted foundation that extends existing skills, tools and investments while supporting critical workloads from the datacenter to the edge. **Windows Server 2028** is now in preview. It will strengthen the infrastructure organizations already depend on while extending Windows Server to enterprise AI inference and hybrid intelligence. Features include:

**Stronger security**: Windows Server 2028 will strengthen security by default with a hardened Server Core configuration, a new security baseline, Trusted Launch for virtual machines, post-quantum cryptography and automated certificate management. These capabilities will help protect identities, workloads and encrypted communications while helping organizations prepare for emerging threats and evolving regulatory requirements.

**Accelerated enterprise infrastructure:** Organizations will be able to improve the performance and efficiency of storage- and data-intensive workloads with NVMe over Fabrics, native NVMe storage and the ability to boot from the Resilient File System—helping them get more from modern infrastructure and accelerated hardware.

**Simplified administration and management at scale:** Organizations will be able to manage Windows Server more consistently across datacenters, the cloud and remote locations using Microsoft Intune, Azure Arc, Windows Admin Center and vMode.  
  
**Enterprise hybrid intelligence:** Windows Server 2028 will expand the infrastructure organizations already trust to support enterprise AI inference close to business-critical applications and data. Investments include:

- **Software**: Supported runtimes and inference platforms, including Windows ML, Foundry Local, vLLM and Llama.cpp.
- **Security**: Microsoft Execution Containers and multilayer protection spanning hardware, the operating system, hypervisor and runtimes.
- **Governance and control**: Integration with Agent 365 to help organizations govern AI across their environments.
- **Hardware**: Support for accelerated AI silicon, including the AMD MI350P accelerator and the NVIDIA GB300 Grace Blackwell Ultra Desktop Superchip.

Together, these capabilities help organizations run AI on infrastructure they control while connecting to Azure as part of a hybrid AI architecture. The security, performance and management features are in preview through the Windows Server Insider Program. Hybrid intelligence features are available to a limited number of customers through an early access program. Hardware requirements apply.

[**Learn more about this news**](https://aka.ms/WindowsServer2028Announcement).

Windows Server 2028 is now in preview, strengthening the familiar enterprise platform with hardened default security, post-quantum cryptography, faster NVMe-based storage and more consistent management across datacenters, cloud and edge. It also extends Windows Server to hybrid AI inference through supported runtimes, Execution Containers, Agent 365 governance and accelerated silicon from AMD and NVIDIA, allowing organizations to run AI close to critical applications and data while connecting to Azure.

### Data

#### Azure Cosmos DB improves development, retrieval and data protection

Instant Summary:

Azure Cosmos DB is introducing seven updates that improve search and retrieval quality, help developers design and evolve applications and strengthen protection for production data. They include:

##### **Developer tools and application design**

- **Azure Cosmos DB Shell:** Now generally available in Visual Studio Code and the Azure portal, the shell gives developers interactive access to explore resources, query and manage data, and enable AI-assisted workflows through MCP integration.
- **AI-assisted data modeler and other updates in Azure Cosmos DB extension for VS Code:** Now in preview, these updates will bring account insights, AI-powered recommendations and guided data modeling for partition keys and container configurations directly into VS Code.
- **Rust SDK for Azure Cosmos DB:** Now generally available, the SDK provides a native Rust client with built-in performance and resilience capabilities to help teams build reliable distributed production applications.

##### **Search and retrieval quality**

- **Semantic reranker:** Now generally available, this capability uses an AI model to evaluate candidate search results and reorder them according to the meaning and context of the query and content.
- **FuzzyBM25 score projection updates in full-text search:** Now generally available, these updates expand full-text search by making relevance scores available to applications.

##### **Data movement and production protection**

- **Azure Backup for Azure Cosmos DB:** Now generally available, Azure Backup adds an independent, vault-based protection layer for centralized backup policies, monitoring, retention and recovery.

Together, these updates support the Azure Cosmos DB application lifecycle: improving retrieval relevance, helping teams design and evolve applications and protecting production data.

[**Learn more about this news**](https://aka.ms/ignite26/cosmosdb).

Azure Cosmos DB is adding seven updates spanning development, retrieval and data protection. Generally available releases include Azure Cosmos DB Shell, a native Rust SDK, semantic reranking, full-text relevance scores and vault-based Azure Backup, while preview enhancements in the VS Code extension bring account insights, AI-powered ecommendations and guided data modeling into VS Code.

#### Azure DocumentDB expands developer tools, sovereignty and security

Instant Summary:

Azure DocumentDB is introducing five feature updates to help developers build applications, apply more-granular access controls and run MongoDB-compatible workloads across hybrid environments.

##### **Faster development and provisioning**

- **Azure DocumentDB extension for Visual Studio Code:** Now generally available, the extension lets developers connect to clusters, browse databases and collections, inspect documents and run queries—all within Visual Studio Code.
- **Near-instant Azure DocumentDB cluster provisioning:** Now generally available for M10 through M30 clusters, this capability reduces the wait for new environments. Developers and AI agents can begin testing, experimentation and production onboarding faster.

##### **Hybrid deployment and data sovereignty**

- **DocumentDB enabled by Azure Arc:** Now in preview, this offering will extend Azure DocumentDB to hybrid and multicloud environments. Organizations will have more flexibility to run MongoDB-compatible workloads where their applications and data need to reside, including scenarios with data sovereignty, residency and infrastructure-control requirements.
- **DocumentDB on Azure Local:** Now in preview, this offering will run MongoDB-compatible document workloads on Azure Local infrastructure. Organizations will be able to keep applications and data within their own environments to support sovereignty, residency and regulatory requirements.

##### **More-granular access controls**

- **Fine-grained role-based access control for databases and collections:** Now in preview, Azure DocumentDB will let organizations scope custom roles and permissions to individual databases and collections. This will support least-privilege access without granting users and applications broader cluster-level permissions than they need.

[**Learn more about this news**](https://aka.ms/ignite26/documentdb).

Azure DocumentDB is expanding tools, deployment choices and access controls for MongoDB-compatible workloads across hybrid environments. Its Visual Studio Code extension and near-instant provisioning for M10 through M30 clusters are generally available; meanwhile, previews for Azure Arc and Azure Local extend workloads to hybrid and controlled environments, and fine-grained role-based access control brings least-privilege permissions to individual databases and collections.

#### Azure HorizonDB generally available for mission-critical applications

Instant Summary:

**Azure** **HorizonDB,** now generally available, is a fully managed, PostgreSQL-compatible database service that combines enterprise security, resilience and scale with built-in vector search and AI capabilities. It helps developers build intelligent, mission-critical applications using the transactional data they already rely on.  
  
**Security and business continuity**

Enterprises running critical applications need to protect sensitive data and maintain business continuity. Azure HorizonDB supports Microsoft Entra ID for authentication and access, private endpoints for network isolation and user-assigned managed identities for service identities. Service- and customer-managed keys encrypt data at rest, while encrypted client connections protect data in transit. Multi-zone replication and distributed storage support fast recovery and help organizations keep applications resilient.

##### **AI development and platform connections**

Bringing models, data and familiar tools together reduces integration work for developers building AI-powered applications. **Built-in AI model management**, in preview, will manage generative and ranking models alongside data, while **AI Functions** and **AI Pipelines**, in preview, will enable developers to invoke models directly from SQL queries without impacting application performance.

Microsoft platform connections support both development and analytics. The **PostgreSQL extension for Visual Studio Code (VS Code)**, now generally available, brings AI-enabled database management, query plans and monitoring into developers’ tools. Mirroring Azure HorizonDB into Microsoft Fabric, in preview, will make operational data available for analytics alongside other business data.

[**Learn more about this news**](https://aka.ms/ignite26/horizondb)**.**

Azure HorizonDB is now generally available as a fully managed, PostgreSQL-compatible service for intelligent, mission-critical applications. Enterprise security, multi-zone replication and distributed storage protect transactional data, while AI model management, SQL-invoked AI Functions and Pipelines, and the ability to mirror Azure HorizonDB in Microsoft Fabric mirroring, all in preview, connect operational data with models and analytics. A generally available PostgreSQL extension for Visual Studio Code adds AI-enabled management and monitoring.

### Azure Managed Redis previews Redis 8 and an agent kit

Instant Summary:

Azure Managed Redis is introducing two preview updates to help developers build responsive modern and AI applications:

- **Redis 8 in Azure Managed Redis:** This update to the existing service will combine support for JSON, search, time-series data, vector search and other data types in one Redis version, simplifying capability management. Applications will be able to find related information, provide recommendations, reuse relevant responses to similar AI requests and give AI agents access to context and memory. The update will expand how applications can store, search and work with data while retaining Azure Managed Redis as a managed Azure service.
- **Azure Managed Redis agent kit:** This preview will bring Redis and Azure guidance into AI-assisted development by reviewing how applications connect to and use Azure Managed Redis. The agent kit will identify configuration settings that could affect reliability, network connections and performance, then suggest changes for developers to evaluate. This will help teams identify common configuration concerns and apply more consistent development practices.

[**Learn more about this news**](https://aka.ms/ignite26/AMR).

Azure Managed Redis is previewing Redis 8 and a new agent kit to support responsive modern and AI applications. Redis 8 unifies JSON, search, time-series,vector search and other data types so apps and agents can retrieve context, provide recommendations and reuse relevant responses to similar AI requests, while the agent kit reviews configurations and suggests improvements to reliability, connectivity and performance.

#### Azure SQL expands modernization, resiliency and local development options

Instant Summary:

Azure SQL updates will help organizations modernize SQL Server workloads and build cloud and AI applications. They expand resiliency and resource flexibility, simplify migration and disaster recovery, and bring Azure SQL Database development to local environments.

##### **Resiliency and flexible resources**

The Azure SQL Managed Instance Next-gen General Purpose tier now offers two generally available updates:

- **Zone redundancy:** Service components are distributed across Azure availability zones in supported regions, helping protect applications against datacenter outages without changing application logic.
- **Flexible memory for zone-redundant instances:** Customers using Premium-series hardware can adjust memory independently of processing capacity to meet workload needs without adding processor cores.

Azure SQL Managed Instance is a fully managed cloud database service based on SQL Server. It handles routine backups, patching and database engine updates. The new capabilities help organizations improve resiliency and tailor resources to their workloads.

##### **Migration and disaster recovery**

Now generally available, Azure SQL Managed Instance link supports **SQL Server Always On availability groups** containing multiple databases. It replicates database changes from SQL Server to Azure SQL Managed Instance in near real time, enabling migrations with minimal downtime and disaster recovery in Azure.

Customers can extend supported existing availability groups or create new groups from standalone databases. A single link can replicate every database in a group, reducing the need to configure a separate link for each one.

##### **Local development with Azure SQL Database**

Azure SQL Database container, now in preview, will allow developers to **run the Azure SQL Database engine locally** without an Azure subscription, shared cloud instance or credit card. Developers will be able to build and test with the same database engine, T-SQL dialect, system views, connection protocol and driver behavior used in Azure SQL Database.

The container will support ledger, vector search and embedding workflows. Developers will be able to use familiar drivers, frameworks and Visual Studio Code tooling, and run integration tests in continuous integration environments before moving applications to Azure SQL Database. Local development will be free; cloud database and model usage will remain subject to their respective charges.

[**Learn more about this news**](https://aka.ms/ignite26/mssql).

Azure SQL is expanding resilience, simplifying migration and bringing Azure SQL Database development to local environments. Generally available updates add zone redundancy, flexible memory and multi-database replication through Azure SQL Managed Instance link, helping customers tune resources, migrate with minimal downtime and strengthen disaster recovery. A preview Azure SQL Database container allows local engine usage and capabilities such as secure enclaves, ledger and vector search.

#### Database Hub in Fabric generally available; SQL and PostgreSQL database agents in preview

Instant Summary:

**Database Hub in Fabric**, now generally available, gives organizations a single place to discover, monitor and manage databases across Azure, Microsoft Fabric, on-premises environments and other clouds. Its broader view helps admins identify emerging bottlenecks, prioritize operational work and apply governance practices more consistently, so database teams can spend less time navigating management complexity and more time improving business-critical systems.

##### **AI-assisted operations with database agents**

Within Database Hub in Fabric, **database agents,** in preview, will bring AI-assisted SQL and PostgreSQL operations to familiar tools. They will help teams move from reactive monitoring toward automated, intelligent database operations. Using Microsoft-authored skills for common performance and health scenarios, the agents will continuously observe operational signals across an organization’s database estate, detect engine-specific issues and explain why they matter. They recommend fixes or carry out approved actions with AI assistance.

Database agents will support rather than replace human judgment. They will work within existing identity permissions, approval boundaries and auditable actions. They will be available across supported Microsoft database services in two familiar places:

- **Database agent in Database Hub in Fabric:** Database professionals and developers will be able to use AI-assisted guidance to investigate SQL and PostgreSQL performance, health and operational issues across their database estate.
- **Database agent in the Microsoft PostgreSQL extension for Visual Studio Code:** Developers and database professionals will be able to investigate PostgreSQL performance and operational issues without leaving their development environment.

[**Learn more about this news**](https://aka.ms/ignite26/databases)**.**

Database Hub in Fabric is now generally available as a unified place to discover, monitor and manage databases across Azure, Fabric, on-premises environments and other clouds. Preview SQL and PostgreSQL database agents will continuously analyze operational signals, explain performance and health issues and recommend or execute approved fixes within existing permissions and audit controls — both in Database Hub and the Microsoft PostgreSQL extension for Visual Studio Code.

#### Microsoft Fabric HorizonDB brings PostgreSQL to Fabric in preview

Instant Summary:

**Microsoft Fabric HorizonDB**, a new database offering in preview, will bring PostgreSQL, one of developers’ most popular databases, directly into Microsoft Fabric. It will connect applications, data analysis and AI in one place.

**Serverless databases for changing workloads**

Agents are building applications faster than developers ever have. They create databases for prototypes, experiments and short-lived tasks, then drop them when the work is done. These workloads run in bursts or sit idle, so demand is hard to predict. Fabric HorizonDB is serverless PostgreSQL built for these patterns.

- Databases will provision in seconds and scale automatically with demand.
- Idle databases will pause, then resume when the next query arrives.

##### **A managed backend for Fabric apps**

Fabric HorizonDB will also be enabled for Fabric apps. It will provide a managed backend with data APIs, authentication, storage and hosting, so developers can go from idea to a running app with PostgreSQL built in.

Query across operational and analytical data  
Fabric HorizonDB will bring live operational data and analytics in OneLake together, so applications can act on both.

**Translytical queries**

A single PostgreSQL query will combine live data in Fabric HorizonDB with analytical data in OneLake, running on Fabric Data Warehouse’s scale-out compute.  
  
**Mirroring**

Fabric HorizonDB tables will copy into Fabric for analytics, with no separate pipelines.

##### **Reverse ETL**

Enriched data from Fabric Data Warehouse will flow back into Fabric HorizonDB, where apps and agents can read it quickly.

**[Learn more about this news.](https://aka.ms/AAncdv4)**

Microsoft Fabric HorizonDB is previewing serverless PostgreSQL inside Fabric, connecting applications, analytics and AI in one environment. Databases provision in seconds, scale with demand and pause when idle, while a managed backend supports Fabric apps with built-in APIs, authentication, storage and hosting. Translytical queries, mirroring and reverse ETL then link live operational data with OneLake and Fabric Data Warehouse insights without separate pipelines.

### PostgreSQL on Azure simplifies migration and expands modernization options

Instant Summary:

Microsoft is investing across the PostgreSQL lifecycle to simplify adoption and modernization. The updates help enterprises move workloads to Azure, keep them current and run demanding applications with built-in performance, security and resilience.

- **Simpler migration and modernization.** Azure Database Migration Service (DMS) support for Oracle-to-PostgreSQL data migration is now in preview. Combined with assessment, schema conversion and application conversion in the Microsoft PostgreSQL extension for VS Code, it will provide a first-party path from preparation and code conversion to data movement. Additionally, customers will be able to use Azure DMS, in preview, to move existing Azure Database for PostgreSQL workloads to Azure HorizonDB through a seamless, managed experience. DMS will handle connectivity validation, data copy, continuous synchronization for online migrations, monitoring and planned cutover, simplifying modernization on a high-performance, scalable PostgreSQL platform.
- **More choice for performance and scale.** Burstable v2 compute, in preview, will add flexibility for development and workloads with changing demands. Cobalt 200, now generally available for Azure Database for PostgreSQL, adds Microsoft-designed Arm64-based compute alongside Intel and AMD x64-based options. Customers can choose the architecture that best fits their workloads as they modernize and scale on Azure.
- **Stronger protection for sensitive workloads.** AMD v6 confidential compute, now generally available, helps protect data in use. Point-in-time restore immutability, also generally available, helps protect backups against changes or deletion.
- **Expanded backup and resilience.** Azure Backup for Azure Database for PostgreSQL flexible server and elastic clusters version 2, in preview, will support larger databases with snapshot-based backups and direct restore. Same-zone to zone-redundant high availability conversion, now generally available, helps protect against availability zone failures without recreating servers.

These enhancements strengthen PostgreSQL on Azure for critical and regulated applications. Organizations can expand their use of PostgreSQL as their needs grow while maintaining performance, protection and resilience.

[**Learn more about this news**](https://aka.ms/Ignite26/Postgres_on_Azure).

Microsoft is simplifying PostgreSQL migration and modernization on Azure with preview services for Oracle-to-PostgreSQL moves and managed transitions from Azure Database for PostgreSQL to Azure HorizonDB. Customers also gain preview burstable compute and snapshot-based backup options, while generally available Cobalt 200 compute, AMD v6 confidential computing, immutable point-in-time restore and in-place conversion to zone-redundant high availability improve performance, protection and resilience for critical workloads.

#### Power BI introduces custom data app creation in preview

Instant Summary:

Power BI Pro customers will have a new way, now in preview, to create purpose-built data apps directly in Power BI Desktop.

##### **From viewing reports to taking action**

A data app combines trusted business data, analysis and actions in an interactive experience. Users can do more than view a report: they can enter information, update records and write changes back to the underlying data source. Teams can turn insights into action without switching tools.

##### **Build with trusted models and natural language**

Customers will be able to start with a trusted Power BI semantic model—the organized, governed layer that defines business data and metrics—and describe the app they want in natural language, reducing the technical effort needed to get started. Power BI Pro customers will also have access to Fabric Database capabilities, enabling them to build applications that support both analytical and transactional scenarios. This brings AI-assisted app creation to Power BI users through their existing licensing options.

Extending preview access to Power BI Pro customers will let more organizations explore secure, tailored apps for planning, approvals, tracking and data collection in the familiar Power BI environment.

[**Learn more about this news**](https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/microsoft-fabric-is-fueling-frontier-transformation/5422989).

Power BI Pro customers can now preview purpose-built data apps they create directly in Power BI Desktop. Starting from a governed semantic model, users describe an app in natural language, which then combines trusted analytics with data. Customers can also update records and make. Access to Fabric Database capabilities further supports analytical and transactional scenarios such as planning, approvals, tracking and data collection without leaving Power BI.

#### Rayfin and Fabric apps reach general availability

Instant Summary:

**Rayfin and Fabric apps** are now generally available, simplifying how developers and AI agents build and deploy complete business applications with enterprise data, security and governance built in. Builders have created more than 100,000 apps with Rayfin since its preview launch.

##### **A connected application backend**

AI is making it possible to build applications in minutes, but production deployment still requires databases, authentication, backend services and access to trusted business data. Rayfin brings these capabilities together in Microsoft Fabric. Developers can choose Microsoft SQL database or Fabric HorizonDB, connect to existing Fabric semantic models, warehouses and lakehouses, and reuse trusted business definitions and access controls without building a separate backend stack.

##### **Governance and integration at scale**

Now generally available, these new capabilities can help organizations manage applications at scale through centralized app governance in the OneLake Governance hub, enhanced security controls and built-in observability. Fabric apps are also expanding into familiar e-tools:

- **Microsoft Copilot:** People can create applications using natural language. Through Fabric apps integration with Copilot Managed Runtime, business users will have access to database and backend services for apps that require extensive app capabilities.
- **Power BI Pro and Power BI Desktop:** Integration enables users to turn trusted semantic models into interactive business applications, extending analytics from insights to action.

[**Learn more about this news**](https://aka.ms/FabricApps-Ignite26).

Rayfin and Fabric apps are now generally available, giving developers and AI agents a governed path to complete business applications with databases, authentication, backend services and trusted enterprise data already connected. More than 100,000 apps have been created with Rayfin since preview; new centralized governance, security and observability features, plus integrations with Microsoft Copilot and Power BI, now help organizations move from natural-language creation and analytics to production deployment at scale.

## Microsoft Foundry

Instant Summary:

Updates to Foundry provide new capabilities to enable continuous improvement for AI agents and models, leveraging live signals to suggest and promote changes to every layer of AI systems.

Led by agent optimizer, Foundry updates each step of the agent loop leveraging the customer’s unique definition of good and respective evaluations.

This is combined with new training capabilities that enable models to be post-trained automatically, with programable options for advanced users. To support this, Foundry is bringing new Microsoft AI (MAI) models and partner offerings.

Foundry IQ, part of Microsoft IQ, now provides an enterprise knowledge graph out of the box over customers full estate of unstructured and application data, enabling rich experiences for custom applications and use cases.

Microsoft Foundry is introducing a continuous-improvement loop that uses live signals, evaluations and agent optimizer to recommend and promote changes across AI systems. New automated and programmable training options help adapt models, supported by Microsoft AI and partner offerings. Foundry IQ, part of Microsoft IQ, also creates an enterprise knowledge graph across unstructured and application data to ground richer custom apps and experiences.

### Continuous improvement in Foundry

#### Turning production experience into better agents

Instant Summary:

**Continuous improvement** in Microsoft Foundry builds on existing observability and evaluation capabilities to help customers create a learning loop. Evaluations establish a baseline for quality, safety, latency and cost, and production traces show how agents behave. New capabilities help teams identify opportunities, test changes and measure whether each iteration improves results.

**Multi-turn evaluation**, now generally available, assesses entire conversations against quality standards. Teams can also generate task-specific rubric evaluators from curated, verified “golden” datasets, with new safety support in preview alongside quality evaluation.

Foundry automatically analyzes production signals with a **new insights capability**, now generally available. It groups recurring failures, such as hallucinations and token spikes, and ranks the most frequent issues and fixes for teams to investigate.

**Human annotation features**, in preview, will enable customers to add expert ratings, comments and expected answers to agent traces, and to curate golden datasets so that evaluations reflect the business’s judgment. This feeds back into the improvement loop.

**Agent optimizer** proposes and tests candidate changes against the team’s evaluations, allowing developers to compare results and choose what to deploy. It is generally available and driving significantlift for customer evaluation results.

**Training in Microsoft Foundry** has new capabilities in preview that will adapt supported models with organizational data when agent changes are not enough. Managed Training will run the process end to end, and teams will test the resulting model against the same baseline.

**Programmed Training**, in preview, will let AI engineers write their own training loops, including supervised fine-tuning and reinforcement learning, on supported open-weight models while Foundry runs the compute.

Each deployed improvement becomes the next baseline. Teams can continue measuring production results and testing changes, improving quality or reducing cost while checking for regressions.

[**Learn more about this update**](https://aka.ms/miq-ignitelaunchblog)**.**

Microsoft Foundry is turning production traces, evaluations and expert feedback into a repeatable learning loop for agents. Generally available multi-turn evaluation, production insights and agent optimizer reveal recurring failures, test proposed changes and measure improvements, while preview human annotation, Managed Training and Programmed Training let teams incorporate business judgment and adapt supported models when agent-level changes are not enough. Each deployment becomes the next baseline for quality, safety, latency and cost.

### New models

### Microsoft-Decision-1.1 now generally available

Instant Summary:

**Microsoft-Decision-1.1,** now generally available, is a fast, cost-effective model designed to make reliable decisions in software at scale. It enables applications to make intelligent decisions dynamically, rather than relying on hard-coded rules, while addressing three key challenges to embedding AI more broadly in software: cost, latency and control. The model is ready for enterprise production deployment and available in Microsoft Foundry and through OpenRouter and Vercel.

Unlike general-purpose LLMs, Microsoft-Decision-1.1 is purpose-built for structured decisions such as routing, classification, prioritization, verification and workflow control. It chooses among permitted actions within developer-defined constraints and provides calibrated confidence scores, allowing applications to defer when uncertainty is high. It handles decisions quickly at a fraction of the cost of larger models, which can then be reserved for more complex reasoning tasks.

Building on Microsoft-Decision-1, released in October, the new model delivers significant improvements in intelligence and speed, at the same competitive price. It’s built on a new base, Gemma 4 26B A4B, and adds multimodal support to analyze images in question instructions.

On the Artificial Analysis Decision Index v2.1, Microsoft-Decision-1.1 scores 68, up six points from the first model and ahead of Jev 1.14, Google’s Gemini-Decision-1 and OpenAI’s GPT-6 Luna (Decisions). Microsoft-Decision-1.1 is also more than twice as fast as the first model.

The model is being integrated across Microsoft products to make faster, more token-efficient decisions, including:

- In Copilot, Microsoft-Decision-1.1 routes user requests to the right experience, determining whether they’re best handled by Copilot or Cowork.
- In Cowork, it powers Auto, dynamically adjusting how much reasoning effort Cowork applies to each task.

[**Learn more about this news**](https://aka.ms/decision-model-ga).

Microsoft-Decision-1.1 is now generally available in Microsoft Foundry, OpenRouter and Vercel for fast, economical routing, classification, prioritization, verification and workflow control. The model handles frequent, small agent decisions in real time,milliseconds so frontier models can focus on deeper reasoning, and its general-availability release adds stronger performance, a Gemma 4 26B A4B base and image inputs. Microsoft is already integrating it into Copilot routing and Cowork’s adaptive Auto mode.

### Microsoft Foundry adds new AI models for coding, images, security

Instant Summary:

**New models in Microsoft Foundry** give organizations more choice in matching the right model to each task, along with the control to keep improving models with their own context. Foundry now includes a growing first-party family from Microsoft AI (MAI) and others, built for enterprise trust and efficiency at scale. Benefits of the new models include:

- **Code:** MAI-Code-2 handles demanding agentic coding work, while MAI-Code-2-Flash supports high-volume, everyday coding, so developers can pick the balance of performance and cost that fits the task. Both are generally available in GitHub, and Code-2-Flash is in private preview in Foundry.

- **Create:** MAI-Image-2.7 and MAI-Image-2.7-Flash are in preview and will offer sharper editing and more consistent image generation, helping brands keep one look across a campaign.

- **Secure:** MAI-Cyber-2-Flash is purpose-built for cybersecurity and available in preview only in Codename MDASH. With new capabilities spanning code vulnerability discovery, validation and remediation, it helps security teams find, confirm and fix vulnerabilities faster and more cost-effectively.

- **Decisions:** Microsoft-Decision-1.1 is now generally available. Built on Gemma, it supports fast, cost-effective routing, classification, prioritization and verification, now including image inputs. Alongside Laya and the Decisions API, it gives developers more ways to choose the decision model that fits each workload and bring decision capabilities into agents and workflows with less integration complexity.

- **Route:** Model router in Foundry Models makes model selection easier. With an expanded model pool featuring the top 50 models in Foundry, support for the model router in AI Gateway and expanded support for messages and responses APIs, customers can bring intelligent model selection into their existing workflows. They can also access a broader range of models and optimize for quality, cost and performance without the complexity of manually selecting and managing models.

- **Choice:** Microsoft Foundry offers more than 11,000 models from OpenAI, Claude, Muse, Mistral, the open-source community and others. Video generation models from fal, including Kling, LTX and MiniMax, are now in preview in Foundry. Baseten on Foundry, also in preview, will bring Baseten’s inference platform into Foundry so organizations can run open models optimized for speed, throughput and cost, with serverless pay-as-you-go deployments globally or in the US Data Zone.

Supported models can be evaluated and deployed in Foundry as part of the same continuous improvement workflow used for agents.

[**Learn more about this news.**](https://aka.ms/foundrymodelsignite2026)

Microsoft Foundry is expanding model choice across coding, image creation, cybersecurity and workflow decisions. New Microsoft AI models include MAI-Code-2, MAI-Code-2-Flash, MAI-Image-2.7, MAI-Image-2.7-Flash and MAI-Cyber-2-Flash, while generally available Microsoft-Decision-1.1 adds efficient multimodal routing and verification. An expanded router, more than 11,000 available models, preview video-generation options and Baseten integration help customers optimize quality, speed and cost within the same evaluation and deployment workflow.

## GitHub

Instant Summary:

New Copilot capabilities are helping developers build agents, work across tools and ship higher-quality code. Microsoft Copilot SDK 2.0 brings a production-proven harness to secure, scalable agent deployments. Powered by a native Rust runtime, the harness is available in six languages. The GitHub Copilot app takes Azure DevOps repos from clone to merge, and brings testing to a real, logged-in browser. Copilot code review helps catch issues earlier with local reviews in the CLI and app, secret detection, adaptive review effort, cross-repository context and repository insights.

New GitHub Copilot capabilities help developers build and deploy agents, work across tools and catch code issues sooner. Microsoft Copilot SDK 2.0 adds a production-proven, Rust-powered agent harness across six languages; the GitHub Copilot app moves Azure DevOps repositories from clone to merge and tests in a real signed-in browser; and enhanced code review adds local CLI and app reviews, secret detection, adaptive effort, cross-repository context and repository insights.

### GitHub

#### Microsoft Copilot SDK 2.0 improves security and scale for AI apps

Instant Summary:

**Microsoft Copilot SDK** is now **2.0**, a major improvement for enterprises seeking to build agents, especially for large-scale deployments. This update includes the improved Copilot harness built on a native Rust runtime, enabling developers to integrate agents directly inside applications, as well as multi-tenant, high-scale applications that require robust enterprise security.

The SDK uses the same harness technology deployed in production across Microsoft and GitHub and is supported across six programming languages. This is now generally available.

[**Learn more about this news**](https://aka.ms/copilot-sdk/blog-2.0).

Microsoft Copilot SDK 2.0 is now generally available, giving enterprises a more secure and scalable foundation for embedding agents in applications. Its enhanced Copilot harness runs on a native Rust runtime, supports multi-tenant, high-scale deployments and works across six programming languages using the same production-proven technology deployed by Microsoft and GitHub.

## Microsoft Copilot

Instant Summary:

As the way we work with AI has evolved, so has Microsoft Copilot. The new Copilot includes **Home**, the single starting point for Chat and Cowork; **Auto**, the smart router for Copilot that dynamically picks the right models and effort for your task, optimizing for quality, speed and cost; and **Word**, **Excel** and **PowerPoint** in Copilot to create and collaborate on files alongside your conversation. It also includes **Code**, which lets anyone build secure apps using natural language and **Autopilot**, a persistent, proactive agent for personal productivity. **Copilot Managed Runtime**securely hosts what you build in Cowork, Code and Copilot Studio.

These updates, detailed below, signal the next chapter of Copilot built for work: a connected platform where people and AI collaborate, with the context, choice and control organizations need to get more done. [Learn more](https://aka.ms/MicrosoftIgnite26Blog).

Microsoft Copilot is evolving into a connected work platform where Home unifies Chat and Cowork, Auto selects the right model and reasoning effort, and Word, Excel and PowerPoint sit alongside the conversation. Copilot Code enables natural-language app creation, Autopilot provides persistent personal productivity, and Copilot Managed Runtime securely hosts solutions built in Cowork, Code and Copilot Studio — giving organizations context, choice and control across human-AI collaboration.

### Microsoft Copilot

#### Agent 365 turns AI spend into business value with FinOps for AI

Instant Summary:

Agent 365 is Microsoft’s observability platform for AI, bringing together management, governance, security and business value for the agents and AI services in organizations. AI spending is growing fast and moving beyond IT, and leaders need to see what it costs and delivers.

With Agent 365, FinOps for AI goes beyond control to maximize business value, giving IT and business leaders visibility to plan, control and optimize AI investments. Features include:

**Agent 365 Cost Management** in the [Microsoft admin center](https://aka.ms/microsoftadmincenter) is a centralized place to see and control a growing list of usage-based AI services, including Copilot Cowork, Copilot Code, GitHub Copilot CLI, Microsoft Copilot Studio, Copilot Managed Runtime, Autopilot and Work IQ APIs.

- Admins will be able to see what is driving spend; set spending policies, limits and alerts; and extend analysis through Microsoft Fabric for custom chargeback and reporting. In preview.
- Admins will be able to forecast spend, ask questions in plain language and act on optimization recommendations. Available in the Frontier program this month.
- In December, these capabilities will expand to include value insights across Microsoft and non-Microsoft agents as well as delegation to business leaders.

**Agent 365 Business Analytics,** now available in the Frontier program, is a new experience for business leaders with the data necessary to understand AI spend, measure its value and decide where to invest next. They will be able to:

- Understand spend: Insight into what’s driving cost across agents, services, models and users.
- Drive business value: Measure the value of AI assistance for specific jobs and tasks through measures such as success rate, user satisfaction and assisted hours.
- Optimize ROI: Forecast cost scenarios, act on recommendations and ask questions in plain language, then work with IT to adjust guardrails for chargebacks.

Users can get started with Agent 365 Business Analytics [application](https://aka.ms/a365analytics) today. Insights for Microsoft services require at least one Microsoft 365 Copilot license in the tenant, while insights for non-Microsoft services require an Agent 365 license.

[**Learn more about this news**](https://techcommunity.microsoft.com/blog/ai-finops-blog/introducing-microsoft-agent-365-business-analytics-turn-ai-investment-into-busin/4574149).

Agent 365 is bringing FinOps discipline to AI with centralized cost management, forecasting, policies, alerts and business-value measurement across agents and AI services. Preview and Frontier capabilities reveal spending drivers, support custom chargeback through Fabric, and measure outcomes such as task success, satisfaction and assisted hours; in December, value insights will expand across Microsoft and non-Microsoft agents and allow business-leader delegation.

#### Autopilot is rolling out to Frontier customers

Instant Summary:

**Autopilot** is Microsoft’s first enterprise-grade, long-running agent for personal productivity. It will live in an organization’s tenant with its own identity, memory and access to tools, and can follow up on threads, run recurring work and continue a project without waiting for another prompt. Designed for collaboration, colleagues will be able to @mention a person’s Autopilot in a Teams channel or group chat to ask for information or request supported actions. Autopilot is designed for security: Actions it takes (even on a user’s behalf) aretied to its own agent ID and safety-checked, and it is visible and manageable by admins. Customers will be able to find Autopilot in the left navigation of the Copilot app. Autopilot is rolling out through the Frontier program.

**[Learn more about this news](https://aka.ms/MicrosoftIgnite26Blog)****.**

Autopilot, Microsoft’s first enterprise-grade long-running personal productivity agent, is rolling out through the Frontier program. With its own identity, memory and tool access inside the organization’s tenant, it can continue projects, follow up on threads and run recurring work without prompts. Colleagues can @mention a user’s Autopilot in Teams, while administrators retain visibility and control over safety-checked actions tied to the agent’s identity.

#### Copilot Managed Runtime is now generally available, with new capabilities

Instant Summary:

Copilot Managed Runtime provides Microsoft-managed hosting and execution for applications, separate from where those applications are created. Builders can start with experiences, including Copilot Code, Copilot Cowork and Microsoft Copilot Studio, or use compatible third-party development tools. When an app is published to Copilot Managed Runtime, organizations gain a common way to host, run and govern it.

With the **general availability of Copilot Managed Runtime**, Microsoft is expanding this product, giving apps built across Microsoft Copilot and compatible third-party development tools an optional data backend with services from Microsoft Fabric.

With the new integration, applications that optionally need persistent data or additional backend capabilities can use Fabric as their underlying data foundation out of the box. Fabric can provide backend capabilities including database, storage and data APIs, while Copilot Managed Runtime continues to provide the application hosting and enterprise management layer.

The integration brings together flexible app creation, Microsoft-managed hosting and governance and an **optional Fabric data backend**, allowing organizations to choose the development experience that fits their needs while providing a consistent path for running applications in their Microsoft environment.

Microsoft is also announcing **Agents and Workflows in Copilot Managed Runtime**. The first iteration will allow users to build custom Copilot Studio agents and workflows locally, make modifications with their dev tool of choice and then publish to Copilot Studio using the CLI. This also gives developers a collaborative approach to agent development on Copilot Studio, alongside version control through platforms like GitHub.

[**Learn more about this news**](https://aka.ms/CopilotManagedRuntime-Ignite-Blog)**.**

Copilot Managed Runtime is now generally available, providing a consistent Microsoft-managed environment to host, execute and govern apps created in Copilot Code, Copilot Cowork, Copilot Studio and compatible third-party tools. Optional Microsoft Fabric integration adds databases, storage and data APIs, while new Agents and Workflows support local development, CLI publishing to Copilot Studio and collaborative version control through platforms such as GitHub.

#### Copilot Workspaces helps teams work together with Copilot

Instant Summary:

Copilot Workspaces brings teams, their work and Copilot together in a shared space in the Microsoft Copilot app. As the evolution of Copilot Notebooks, Workspaces helps teams turn shared context into shared progress on an ongoing workstream.

Work IQ can suggest relevant workspaces based on current workstreams to help people get started quickly. Once in a workspace, team members can work together on shared documents while Copilot connects the dots across the work, surfacing what changed, what remains unresolved and which actions need attention so everyone can quickly catch up and keep the work moving. And coming soon, teams will be able to bring their personal Autopilot into Workspaces, so humans and agents can collaborate in one space and team members can shift from doing the work to directing it.

Copilot Workspaces is available in the Copilot app through the Frontier program.

[**Learn more about this news**](https://aka.ms/MicrosoftIgnite26Blog).

Copilot Workspaces brings teams, shared content and Copilot into an ongoing collaborative space within the Microsoft Copilot app. Work IQ can recommend relevant workspaces, while Copilot tracks changes, unresolved questions and actions across shared documents so members can catch up quickly. Available through the Frontier program, Workspaces will soon let teams bring personal Autopilot agents into the same space and shift from completing work to directing it.

#### Dynamics 365 CRM and ERP plugins now available in Copilot

Instant Summary:

Two new Dynamics 365 plugins let users complete sales, finance and operations tasks in Microsoft Copilot without switching apps. They are:

- **Dynamics 365 Sales plugin**, now generally available, brings sales capabilities into Copilot. Sellers can build account plans, prepare for customer meetings, catch up on deals and prioritize pipelines. New deal insights track progress against the quarterly forecast, map decision makers and engagement gaps, and flag deals and risks that need attention. Within this plugin, sellers can also create presentations in PowerPoint, adapt existing decks for new customers and refresh slide data, and confirm approval and sharing requirements.
- **Dynamics 365 ERP apps plugin**, now generally available, brings enterprise resource planning (ERP) context and actions into Copilot Cowork and Excel. Purpose-built business skills give Copilot and agents knowledge of common finance and operations tasks. In the Source-to-Pay process, for example, a sourcing lead can streamline purchase requisitions, requests for quotes and purchase orders.

[**Learn more about this news**](https://aka.ms/A365AnalyticsLearn)**.**

Two generally available Dynamics 365 in Copilot plugins let users complete CRM and ERP work directly in Microsoft Copilot. The Sales plugin supports account planning, meeting preparation, pipeline prioritization, deal-risk analysis and PowerPoint creation, while the ERP apps plugin brings finance and operations context into Copilot Cowork and Excel, using purpose-built skills to streamline processes such as purchase requisitions, requests for quotes and purchase orders.

#### Easily build secure apps with Copilot Code

Instant Summary:

**Copilot Code** will empower everyone to build dashboards, trackers and apps with natural language, using the same agentic technology as GitHub Copilot. Cloud projects will run in a secure sandbox, stay within your tenant and are easy to share internally and take on the go with iOS and Android. A new local sandbox will extend those protections to people’s devices, limiting what Code and everything it runs can read, write and access on the network.

IT will be able to stay in control. Supported apps will be able to be published through Copilot Managed Runtime, extending existing Microsoft 365 identity, security and governance controls, with apps visible and managed in the Microsoft 365 admin center.

Copilot Code is available in the Frontier program on Windows, web, iOS and Android, with local sandbox available on Windows and coming soon to macOS. Copilot Code will be generally available in December.

[**Learn more about this news**](https://aka.ms/MicrosoftIgnite26Blog).

Copilot Code lets people create dashboards, trackers and apps with natural language using the agentic technology behind GitHub Copilot. Cloud and local sandboxes restrict network access, while Copilot Managed Runtime extends Microsoft 365 identity, security, governance and admin visibility to published apps. It is available through the Frontier program on Windows, web, iOS and Android, with general availability planned for December and macOS local sandbox support coming soon.

#### Home in the Microsoft Copilot app

Instant Summary:

**Home**, [announced in September](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/) and now rolling out worldwide, is the new starting point in Copilot, bringing Chat and Cowork together so people can easily move between asking quick questions and delegating complex workflows. Updates include two new capabilities when using **Auto**, Copilot’s smart router, which dynamically picks the right model and effort for your task:

- Auto now recommends moving from Chat to Cowork for complex tasks to help users select the mode that offers the best response. If users choose to continue in Cowork, their context goes with them, keeping them in the flow of work. This is generally available.
- Auto in Cowork will use Microsoft-Decision-1.1, a fast, cost-effective decision model, to dynamically pick effort levels according to a user’s task. It will break the task into parts, match each part to a model and ultimately use the decision model to quickly determine the right effort level for each. This is available to Frontier customers.

Other new capabilities are:

- **Copilot Cowork** will recommend tasks to start based on recent Work IQ signals and invoke the declarative agents a company has already built to help users get more of their complex work done. Declarative agents are available in private preview through the Frontier program.
- **Office in Copilot** is now generally available, bringing the full power of Word, Excel and PowerPoint into the Microsoft Copilot app so people can move directly from a conversation to creating and collaborating on documents, workbooks and presentations.  
    
  People can shape their work with Copilot or edit directly with the familiar formatting, commenting and real-time coauthoring capabilities of Office, then seamlessly transition into the full Office apps when needed. Files are saved to OneDrive and inherit Microsoft 365 permissions, sensitivity labels and compliance controls, helping people collaborate securely without rebuilding context or starting over.

[**Learn more about this news**](https://aka.ms/MicrosoftIgnite26Blog)**.**

Home is rolling out worldwide as the Copilot app’s unified starting point for Chat and Cowork. Generally available Auto recommendations can move complex work into Cowork without losing context, while Frontier customers can use Microsoft-Decision-1.1 to vary effort, suggest tasks from Work IQ and invoke company agents. Office in Copilot is also generally available, embedding the power of Word, Excel and PowerPoint into creating and collaborating with Microsoft 365 protections directly in the conversation.

#### Microsoft expands Dynamics 365 Activate to support agentic ERP migration

Instant Summary:

New capabilities will extend Microsoft Dynamics 365 Activate from CRM to ERP, helping organizations and their implementation partners assess existing SAP ECC environments and move to Dynamics 365. For CRM, the Salesforce migration experience is now generally available.

As SAP ECC approaches the end of mainstream maintenance, organizations evaluating their ERP options must decide which customizations, integrations and business processes to move, simplify or redesign. Dynamics 365 Activate is an implementation and migration platform that uses agentic capabilities to support this work with project teams that review and validate every recommendation.

The new and upcoming capabilities include the following, which start rolling out today and continue over the coming weeks:

- **SAP ECC discovery** will analyze an existing SAP ECC environment, including business processes, configurations, customizations and dependencies. It will identify migration complexity, potential gaps and areas that need further evaluation to help teams define project scope before implementation begins.
- **Requirements analysis** will help teams translate business needs into Dynamics 365 requirements.
- **Configuration** will help teams set up the new Dynamics 365 environment. **Data migration** will help move data from existing systems into Dynamics 365. Project context will carry forward from assessment through implementation, so teams do not have to repeat work at each stage.

Dynamics 365 Activate is built on Success by Design, Microsoft’s implementation methodology.

[**Learn more about this news**](https://aka.ms/D365Ignite2026)**.**

Microsoft Dynamics 365 Activate is expanding from CRM to ERP, using agentic capabilities and human validation to help organizations assess SAP ECC environments and migrate to Dynamics 365. Rolling out over the coming weeks, the platform will analyze processes, configurations, customizations and dependencies, translate needs into requirements, configure the new environment, move data and retain project context from assessment through implementation. The Salesforce CRM migration experience is now generally available.

#### Microsoft, Salesforce announce Salesforce in Copilot, Teams and Fabric

Instant Summary:

Microsoft and Salesforce continue their collaboration with new integrations of Salesforce across Microsoft Copilot, Microsoft Teams and Microsoft Fabric. This brings Salesforce customer context, business processes and actions into the Microsoft tools people use every day.

**Salesforce in Copilot**, now available in preview with more than 38+ prebuilt sales skills, will connect customer context with the work happening across the business. From within Copilot, sellers will be able to securely retrieve customer information and take supported business actions within their existing Salesforce permissions through authenticated Salesforce MCP access. Sellers will then be able to put that context to work across Microsoft 365 with Work IQ adding relevant context from Teams meetings, Outlook emails and documents.

For many organizations, work first starts in Teams, where people share files, make decisions and hand work to each other. Sales Cloud in Teams, now available in pilot, will bring Salesforce customer context directly into that collaboration, allowing sellers to get a real-time view of pipeline and quota progress, deal notifications and briefing materials.

Additionally, Microsoft and Salesforce are bringing a two-way, Zero Copy connection between Salesforce Data 360 and Microsoft Fabric. With Data Federation, now generally available, joint customers can now directly query and analyze supported Microsoft Fabric OneLake data within Salesforce Data 360. This native, Zero Copy connection allows organizations to ground customer workflows and CRM experiences in enterprise-wide operational and financial data while leaving the source data in Fabric.

[**Learn more about these updates**](https://aka.ms/AA1457n5).

Microsoft and Salesforce are expanding their collaboration with new integrations across Copilot, Teams and Fabric. The Salesforce in Copilot plugin brings customer context and 38+ prebuilt sales skills into Microsoft Copilot365, while Sales Cloud in Teams provides real-time pipeline insights and deal updates. A two-way, Zero Copy connection between Salesforce Data 360 and Microsoft Fabric also lets organizations analyze enterprise data across platforms without moving the source data.

#### Today helps people prioritize and act on what matters

Instant Summary:

**Today** is a new experience in the Microsoft Copilot app and Outlook that will help people stay on top of their work by surfacing key priorities and proactively preparing next steps.

Today will bring together information from across emails, calendars, chats and meetings to create a personalized view of what needs attention. It will also proactively prepare work, including email drafts, chat messages and scheduling changes, for users to review and approve.

The experience includes two capabilities:

- **Today Brief** will provide a personalized morning briefing that highlights priorities and prepares next steps, helping users start their day caught up and ready to act. This daily refresh is included with a Microsoft 365 Copilot license.
- **Today Feed** will build on the morning briefing by automatically refreshing throughout the day as new emails, messages and meetings come in, helping users stay on top of shifting priorities as the day unfolds. Recurring updates throughout the day require Copilot credits.

Today will begin rolling out in private preview through the Frontier program.

[**Learn more about this news**](https://aka.ms/MicrosoftIgnite26Blog).

**Today** is a new feature in Copilot and Outlook that combines information from email, calendars, chats and meetings to help identify priorities and prepare next steps for approval. Today Brief, included with a Microsoft 365 Copilot license, provides a personalized morning overview and prepares actions for users to review. Today Feed, which requires Copilot credits, updates priorities throughout the day as new information comes in. The experience will begin rolling out in private preview through the Frontier program.

## Microsoft Edge

Instant Summary:

Industry research indicates that approximately 85% of work happens in the browser, making it a critical endpoint to manage and secure. Microsoft Edge for Business is an industry-leading secure enterprise browser — and now the most-used enterprise browser in the world[1](#Footnote1). As AI moves from chat to taking action, browser governance matters more than ever. Edge for Business offers security with native integration, maximizing protection from Microsoft 365. New updates bring agentic browsing built for enterprise governance and foundational security for today’s cybersecurity landscape.

Microsoft Edge for Business is adding new AI and security features to help organizations protect and manage browser-based activity by people and AI agents. With about 85% of work happening in browsers, the updates pair agentic browsing with built-in Microsoft 365 security protections, helping organizations maintain control as AI moves from conversation to action.

### Edge for Business

#### Edge for Business adds governed AI workflows, stronger security

Instant Summary:

Microsoft Edge for Business, now the most-used enterprise browser in the world[1](#Footnote1), is announcing new AI and security capabilities designed to help organizations increase productivity while keeping human and agent activity governed and protected. They include:

**AI updates:**

- Skills recorder will let employees record a workflow in Edge for Business and turn it into a reusable, shareable skill for Copilot Cowork. IT will be able to control when the capability is enabled, and the resulting skills will operate within the bounds of the employee’s existing permissions and organizational policies. Recorded skills will follow the same steps every time, for predictable and efficient execution. Skills recorder is in preview with Cowork.
- A new managed agent browsing experience will enable IT to enforce the use of Edge for Business by Microsoft and third-party agents whenever an agentic task needs a browser. Each agent will work in a dedicated window with its own Microsoft Entra agent identity and operate within the bounds of the user’s existing permissions and organizational policies. Visual cues will make it clear when a window belongs to an agent. This experience is now in preview.

**Security updates:**

- Extension safety, now generally available, provides an organization-wide inventory with Akamai and Spin.AI risk scores at the extension and version level to help admins assess risk and make allow and block decisions. Extension leak control, in preview, will take this one step further by preventing selected organization-installed extensions from reading content on protected pages.
- A native Microsoft Sentinel connector for Edge for Business will bring browser security events and audit logs into Microsoft Sentinel, helping teams investigate and hunt threats in one place. The connector is in preview.
- Microsoft Entra Global Secure Access in Edge for Business will simplify secure access, enabling employees on Windows PCs to reach private web applications through their signed-in work profile, without a separate VPN client, network agent or browser extension. The integration is in preview.

*1Based on worldwide browser share of minutes on Windows devices at organizations with more than 1,000 employees.*

[**Learn more about this news**](https://aka.ms/EdgeIgnite26).  
**[Download visual assets related to this news.](https://msftglobalcomms-my.sharepoint.com/:f:/g/personal/global_msftglobalcomms_onmicrosoft_com/IgCu2rsoKP-1QIRcGw-FZ_uTAS8sy4r_vXCOOD-74p3FEYU?e=z38MOs)**

Microsoft Edge for Business is adding new AI workflows and stronger security protections. Preview features let employees record reusable, shareable skills for Copilot Cowork and give Microsoft and third-party AI agents their own browser windows with separate identities. Security updates include generally available tools to assess browser extension risks plus preview controls for extension data access, Microsoft Sentinel integration and access to private web apps without a separate VPN through Microsoft Entra Global Secure Access.

## Microsoft IQ

Instant Summary:

Microsoft believes that AI should amplify customers’ business advantage. Today, **Microsoft IQ** is expanding to be a complete enterprise context management platform.

Microsoft IQ brings together the data, knowledge, expertise and proven ways of working that make every organization distinctive and is putting that intelligence to work across apps and agents. New features provide a governed home to reuse skills, tools and agents across teams with business plugins. Enhanced context management capabilities connect agents to work, business data, unstructured content and real-world knowledge through Work IQ, Fabric IQ, Foundry IQ and Web IQ, with continuous improvement provided by Microsoft Foundry.

Together, these updates help organizations retain, apply and grow their own IQ, so what they build today becomes the foundation for what they build next.

**Microsoft IQ** is expanding into an enterprise context management platform that brings an organization’s data, knowledge, expertise and proven ways of working into apps and agents. Reusable business plugins, skills, tools and agents help teams securely share and build on what works, connecting AI to people’s work, business data, unstructured content and real-world knowledge. Continuous improvement through Microsoft Foundry helps that organizational intelligence grow over time.

### Microsoft IQ

#### Introducing Microsoft IQ, the platform for enterprise AI

Instant Summary:

**Microsoft IQ**, now generally available, puts customers’ intelligence to work in the apps and agents that they build, so teams can reuse what works and preserve what they learn as models, tools and business needs change. Each improvement adds to the customer’s IQ, giving future work a stronger starting point. Microsoft IQ brings together two capabilities:

- **Enterprise context management** connects agents to how people work, business data, unstructured content and real-world information through Work IQ, Fabric IQ, Foundry IQ and Web IQ, along with reusable business plugins, skills, tools and agents. Business plugins organize that context and expertise for each scenario.
- **Continuous improvement** in Microsoft Foundry connects evaluations and production insights to agent optimization and model training, enabling significantly improved customer outcomes.

The new Microsoft IQ is built on products customers already use, with no new SKU or subscription. Together with **Microsoft Agent 365 for governance**, it helps customers retain, apply and grow their IQ as they extend applications, adopt new models and improve agents.

[**Learn more about this news**](https://aka.ms/miq-ignitelaunchblog).

**Microsoft IQ** is now generally available, combining enterprise context management with continuous improvement so organizations can preserve and reuse what their apps and agents learn. It connects AI to people’s work, business data, unstructured content and real-world information, while Microsoft Foundry uses evaluations and production insights to improve agents and train models. Microsoft IQ is built on products customers already use, without requiring a new subscription, and works alongside Microsoft Agent 365 to help organizations govern their agents.

### Microsoft IQ: Enterprise context management

#### Microsoft IQ connects agents to the expertise of your business

Instant Summary:

**New enterprise context management capabilities** connect agents to the information, meaning and expertise they need to understand the work at hand. Work IQ brings work data and the context behind decisions, Fabric IQ connects business data with metrics and operational meaning, Foundry IQ activates unstructured content and Web IQ supplies real-world information. Together these sources help agents draw on more of what the organization knows. Context capabilities are generally available across Microsoft Copilot, GitHub Copilot, Microsoft Foundry and any agent harness via MCP.

Organizations can also discover and reuse the building blocks of enterprise AI, available in Microsoft Copilot and through Microsoft IQ APIs. Business plugins package capabilities for installation and reuse; skills capture reusable instructions, expertise and supporting resources for a particular task; tools give agents callable capabilities, such as retrieving information from a business system or taking an action; and agents can be published for reuse across the organization. These capabilities are generally available.

**Business plugins in Microsoft IQ**, available in the Frontier program, take that reuse further. Where plugins package individual capabilities, business plugins will build on reusable skills with a managed hierarchy of scenario-specific guidance. They will tell agents which context, tools, skills and authoritative sources to use, helping organizations apply their expertise consistently across teams.

Business plugins in Microsoft IQ are:

- Curated by domain experts. Authorized teams organize guidance for an organization, business unit or project around the work agents need to do.
- Capable of hierarchical inheritance. Agents can inherit relevant guidance from the organizational structure, so teams can reuse a common foundation of expertise and add scenario-specific context.
- Governed throughout. Sensitivity labels, change auditing and governance insights support management of that guidance over time.

Business plugins are designed to help agents use relevant instructions and sources with less unnecessary context. The goal is higher-quality results and lower token costs as organizations scale the reuse of skills and expertise.

[**Learn more about this news**](https://aka.ms/miq-ignitelaunchblog).

Microsoft IQ now connects AI agents to an organization’s knowledge and expertise through generally available capabilities across Microsoft Copilot, GitHub Copilot, Microsoft Foundry and other compatible agent platforms. Organizations can reuse business plugins, skills, tools and agents, while new business plugins, available in the Frontier program, let experts provide guidance that agents can use across teams. Sensitivity labels, audits and other controls help organizations manage that guidance, with the goal of improving results and reducing costs.

### Foundry IQ

#### Foundry IQ brings unstructured data to applications and agents

Instant Summary:

Foundry IQ helps developers put unstructured data to work in both traditional application search and agentic workloads. It combines keyword, vector and hybrid search with semantic ranking for search-driven applications and agentic retrieval that plans and iterates across knowledge sources for more complex questions. New capabilities deepen how applications and agents find and connect information:

- **Knowledge graphs** (in preview) will connect entities and relationships across documents and organize content into topics. Agents will be able to trace connections from a regulation through suppliers to affected products, citing supporting sources. Topic-based retrieval will help answer broader questions across a collection, such as themes running through a set of contracts.
- **Microsoft-Retriever-1** (in preview), a new retrieval model, will run iterative search and query planning for faster, more efficient grounding.
- **A Foundry IQ resource in every new Foundry project** (in preview) will provide grounding from day 1 on a usage-based, serverless plan.
- **The SharePoint indexed knowledge source** is now generally available, bringing SharePoint content into Foundry IQ retrieval so applications and agents can find relevant information while respecting source permissions.

These updates help developers build search experiences and agents that can retrieve relevant content, follow relationships across documents and ground responses in organizational data.

[**Learn more about this news**](https://aka.ms/miq-ignitelaunchblog).

Foundry IQ is expanding how applications and AI agents retrieve and connect information across documents and other content. New features in preview include knowledge graphs that help identify relationships and topics across documents, Microsoft-Retriever-1 to help agents find relevant information faster and more efficiently and built-in access to information that helps ground AI responses in new Foundry projects. A SharePoint integration, now generally available, lets applications and agents find relevant organizational content while respecting existing permissions.

### Fabric IQ

#### Bring trusted business context to more experiences with Fabric IQ

Instant Summary:

New Fabric IQ integrations across Microsoft Copilot and Fabric apps are now generally available, as well as integrations across Excel, GitHub Copilot, ChatGPT and Claude, making it easier to bring trusted enterprise data and business context into the experiences people and AI use every day.

Fabric IQ provides a shared intelligence layer that connects enterprise data with the business meaning and operational context needed by people, applications and AI agents. It combines unified data from Microsoft OneLake, trusted metrics from Power BI semantic models and operational context from ontologies to give people and agents a consistent understanding of the business, including the rules that govern the best actions. Specialized data agents build on this context to reason over enterprise data and deliver relevant answers to natural-language questions.

**In Microsoft Copilot**, users can bring Fabric IQ directly into their work to get answers grounded in trusted business context. They can also access Power BI semantic models in Copilot, a capability that is generally available.

**In Excel**, users can turn on Fabric IQ in Edit with Copilot, in preview, to ask questions of governed semantic models and create live, Fabric-connected PivotTables.

**With Fabric apps**, developers can embed conversational experiences powered by Power BI semantic models and Fabric data agents into their custom applications, enabling users to explore and interact with enterprise data directly within the app. And Fabric IQ ontologies in GitHub Copilot, in preview, will bring trusted business context into application development.

**New** **Fabric IQ connectors for ChatGPT and Claude**, in preview, will bring insights from Power BI semantic models directly into both assistants. Users will be able to ask questions of their enterprise data without opening a report, and answers will draw on the measures an organization’s analysts already maintain, so a revenue figure in ChatGPT or Claude will match the one in the company’s quarterly business review.

[**Learn more about this news**](https://aka.ms/miq-ignitelaunchblog).

Fabric IQ is bringing trusted business data and information into Microsoft Copilot, Fabric apps and other tools people use every day. New integrations, some generally available and others in preview, extend these capabilities to Excel, GitHub Copilot, ChatGPT and Claude. Users can ask questions about their organization’s data and create PivotTables connected to live data. Answers in ChatGPT and Claude will be based on the same information their organization already uses, so a revenue figure can match the one in a company’s quarterly business review, for example.

### Web IQ

#### Web IQ now generally available to Azure customers

Instant Summary:

Web IQ is now generally available to all Azure customers, making it easier for developers to bring fresh, relevant knowledge from across the web into AI agents and applications at a new, lower price. Web IQ connects real-world knowledge — from web pages, news, images, videos and more — with specialized data to expand what agents know beyond their underlying models and business data, so they can deliver better answers and actions. Other updates include:

- **Auto mode in Web IQ** makes it simpler to bring the right real-world knowledge into agents.Instead of requiring developers to select and orchestrate individual APIs, Auto mode brings Web, Images, Videos, News and the new Places and Weather categories together in a single, fast and cost-effective experience. This reduces the work required to build web grounding into an application while helping agents retrieve relevant external context for their responses. Now generally available.
- **Web IQ Auto Advanced** improves retrieval for more complex questions.When an initial result is not sufficient, Auto Advanced can evaluate the response, refine the query and retrieve additional information. This gives developers a way to improve results for demanding scenarios without building that iterative retrieval logic themselves. Now generally available.
- **Web IQ Scopes** gives organizations greater control over the web content their AI agents can access. This lets developers and enterprise administrators include or exclude specific URLs, domains, sites and paths when grounding AI responses. Now generally available.
- **Specialized knowledge domains** feature three new data categories. **Web IQ Places** provides intelligence on 207.5 million real-world entities tohelp customers build location-aware experiences faster, improve local discovery and recommendations, and reduce the effort to maintain place data. **Web IQ Weather** brings Microsoft’s weather intelligence directly into AI agents to help customers build weather-aware experiences faster, improve planning and recommendations, and respond to changing conditions. Web IQ Places and Web IQ Weather are generally available. **Web IQ Commerce** will give AI shopping agents structured product data across more than 40 billion listings. Product IDs, images, descriptions, pricing, availability and multi-merchant offers will help agents compare products and deliver faster, higher-quality recommendations at scale. Web IQ Commerce is in private preview.
- **Healthcare enhancements to Web IQ** help organizations build better health agents and other AI experiences with credible, cited health evidence. A new health-aware ranking uses source credibility signals, informed by principles established independently by the National Academy of Medicine in the US, to surface credible health sources ahead of forums and blogs. It runs on the Web IQ API with no new integration or separate SKU needed. Generally available.

[**Learn more about these updates**](https://aka.ms/webiqnews)**.**

Web IQ is now generally available to all Azure customers, helping developers give AI agents and applications current information from websites, news, images, videos and other sources more easily and at a lower price, so they can deliver better answers and actions. Auto mode and Auto Advanced simplify retrieval, even for complex questions, while Scopes gives organizations more control over which web sources agents can access. New Places and Weather capabilities help agents provide location-specific information and weather forecasts, while Commerce, in private preview, will provide shopping agents with information from more than 40 billion product listings. And new health-related search improvements help agents find credible sources of medical information.

### Work IQ

#### Work IQ expands context, actions and controls for Copilot and agents

Instant Summary:

Work IQ is expanding with new capabilities that give Copilot and agents richer organizational context, more ways to act and additional controls for businesses to govern how agents operate.

These new capabilities include:

- **Richer context:** Work IQ is expanding the information agents can access across Microsoft 365 and business applications. New retrieval capabilities help agents find relevant, permission-aware information, while memory can make useful user and organizational context available across experiences. Now generally available.
- **More ways to act:** New agent capabilities go beyond answering questions to creating and editing work content, handling longer-running tasks and executing more-complex workflows. Now generally available.
- **More proactive agents:** A new listen capability will allow agents to respond when relevant events happen, such as a new message or business event, instead of requiring a person to initiate every interaction. In preview.
- **Expanded enterprise controls:** New governance capabilities will provide more-granular policies and human approval options to help organizations control what agents can access and what actions they can take. In preview.
- **Expanded partner platforms:** Work IQ is expanding to third-party AI platforms, with integrations planned for OpenAI and Anthropic (coming soon), giving customers more ways to bring organizational context into the AI experiences and agents they use. Now generally available.

Together, these updates advance Work IQ from providing context for AI experiences to enabling agents that can understand an organization’s work, act on its behalf and operate within enterprise controls.

[**Learn more about this news**](https://aka.ms/miq-ignitelaunchblog).

Work IQ is expanding with new capabilities that help AI agents better understand an organization’s work, take action and operate within its rules. Generally available updates help agents find relevant information while respecting existing permissions, remember useful context, create and edit content and handle more complex tasks. New capabilities in preview will let agents listen for relevant events, such as new messages, without being prompted and give administrators more control over what agents can access and do. Work IQ is also expanding to third-party AI platforms, with integrations planned for OpenAI and Anthropic (coming soon).

### Continuous improvement

#### Continuous improvement helps agents and models learn in production

Instant Summary:

Continuous improvement in Microsoft IQ brings new capabilities from Microsoft Foundry to life so apps and agents keep getting better once they reach production. It turns live production signals into improvements at every level, from an agent’s configuration to the model itself. Teams define success and measure quality, latency and cost per successful outcome, then approve changes before deployment.

Agent Optimizer in Foundry evaluates an agent against those success criteria, generates improved configurations and ranks them so teams can deploy the best one. When configuration changes stop producing gains, teams can apply the same criteria and production signals to the model itself through post training.

- Managed Training is a simple, automated way to improve model quality that covers most customization needs.
- Programmed Training, in preview, gives AI engineers greater control to write custom training loops, including supervised fine-tuning and reinforcement learning, for supported open-weight models while Foundry manages the compute.

Together, these tools give teams one path from simple, automated optimization through fully customized training. This work builds on Foundry capabilities that are generally available:

- Start where your team works. Makers can begin in Copilot and professional developers can build in GitHub or Foundry.
- Choose and adapt models. Foundry enables teams to compare models against quality and cost requirements, choose the model that fits the task and adapt supported models with their own data.
- Build and run agents. Foundry Agent Service connects models to enterprise knowledge and tools so agents can take action across business systems. A managed runtime for supported agents, with identity and authorization, helps teams operate them in production.
- Operate and improve in production. Integrated tracing, evaluations and safety controls help teams understand behavior and assess changes, while connections to enterprise governance support oversight.

What works carries forward. The context, skills and evaluations that prove their value become reusable across agents and workflows through enterprise context management, so each improvement builds on the last.

[**Learn more about this news**](https://aka.ms/miq-ignitelaunchblog).

Microsoft IQ and Foundry are adding capabilities to help organizations continuously improve apps and AI agents after they’re put to work. Teams can set goals for quality, speed and cost, then evaluate and approve improvements before deploying them. Agent Optimizer generates and ranks potential changes so teams can deploy the best ones. When those changes stop producing gains, Managed Training and Programmed Training, which is in preview, help teams improve the underlying AI models. Organizations can also reuse and build on what they’ve learned across agents and workflows.

## Security

Instant Summary:

As AI agents move from answering questions to taking action, security becomes the foundation for trust. **Microsoft Perception is now generally available**, bringing specialized security agents and playbooks together to investigate threats and strengthen defenses. New agent governance and security capabilities across **Agent 365, Microsoft Entra, Intune, Defender** and **Purview** give organizations greater visibility and control over agents, their identities, tools, access and data.

Together, these updates and the ones below help organizations establish trust at every layer of the agentic enterprise, giving people and agents the freedom to act with the security, control and accountability organizations need.

Microsoft is strengthening security for agents as they move from answering questions to taking action. Microsoft Perception, now generally available, combines specialized security agents and playbooks to investigate threats and strengthen defenses. New capabilities across Microsoft Agent 365, Microsoft Entra, Intune, Defender and Purview help organizations monitor and control agents, including their identities, tools, access and data.

### Agent 365

#### Dynamic Agent Risk within Agent 365 in preview

Instant Summary:

**Dynamic Agent Risk**, in preview, will leverage Microsoft’s security context engine to fuse runtime signals (identity, access, data, endpoints, cloud and network), posture and blast radius into a comprehensive agent risk assessment — removing the need for security teams to stitch together siloed security tools to gain a complete agent risk understanding.

Dynamic Agent Risk will follow the agent as it takes new actions, becomes the target of malicious activity or receives code or model updates — always updating as risk changes — and serve as a core primitive, along with Agent Registry, that is visible across Microsoft 365 Admin Center and Defender, Entra, Intune and Purview.

Additionally, a partnership with risk management platforms Check Point, Cyera, Darktrace and Zenity brings partner agent-security signals into Microsoft Sentinel and uses them as evidence in Microsoft-calculated agent risk for Agent 365. The planned flow uses dedicated agent-risk connectors and an agreed data schema. Sentinel analytics rules turn incoming partner signals into alerts. Microsoft Security then correlates supported alerts to agents and incorporates them into its risk assessment. Microsoft computes the unified low, medium or high level of risk, while contributing providers remain visible as data sources. The overall risk design considers runtime risk, exposure and blast radius, with partner signals contributing runtime evidence.

This authoritative understanding of agent risk will form the foundation for comprehensive runtime risk mitigation and containment at speed and scale, working 24/7 via Microsoft Perception.

[**Learn more about this news**](https://aka.ms/secureAIannounce).

Dynamic Agent Risk, now in preview in Microsoft Agent 365, helps organizations continuously assess security risks posed by AI agents. It combines information about agents’ identities, access, data and activity to assess risk as agents take new actions, face attacks and receive updates. The assessments will be available across Microsoft administration and security products and incorporate information from risk-management platform partners Check Point, Cyera, Darktrace and Zenity through Microsoft Sentinel. The information will help organizations respond to threats more quickly with Microsoft Perception.

#### Management insights now default for Microsoft agents

Instant Summary:

Access to Agent 365 usage and activity insights is expanding in the Microsoft Admin Center for Microsoft pre-built agents and agents built on Microsoft platforms. This change, generally available, expands access to the agent overview, active users and advanced usage metrics for activity, sessions, exception rate and run time, regardless of Agent 365 licensing status. This gives administrators foundational visibility into agent usage and activity and helps them understand where additional management, governance and security capabilities may be needed.

Viva Insights will remove its Agent 365 license requirement for agent insights while retaining the requirement for at least 50 assigned Copilot licenses. Eligible organizations can review agent, user and session metrics, export data and explore it through flexible queries.

These changes will give more organizations access to information about agent usage and operations. To capture the full value of Agent 365’s management metrics, governance and security capabilities, customers will still require an Agent 365 or ME7 license. An Agent 365 license is still required for customers to get enterprise-grade management, security and governance. That includes risk and security insights from Microsoft Defender, the Agent Map within Defender’s Advanced Hunting features, Microsoft Purview and full insights for third-party agents.

[**Learn more about this update.**](https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753)

Microsoft is expanding access to Agent 365 usage and activity insights in the Microsoft Admin Center, making them generally available for Microsoft pre-built agents and agents built on Microsoft platforms, without requiring an Agent 365 license. Administrators can see how many people use agents, how often they run and how well they perform. Eligible Viva Insights customers also no longer need an Agent 365 license for agent insights. Advanced insights for third-party agents and additional management, governance and security capabilities still require Agent 365 or ME7 licensing.

#### Microsoft Agent 365 expands governance for agents and their tools

Instant Summary:

Microsoft Agent 365 is adding capabilities to help IT administrators identify agents requiring attention, understand agent and model use and govern the tools, policies and models across the agent estate:

- A **new action center** will bring governance tasks into a focused experience, initially surfacing inactive agents and ownerless agents for review and cleanup. Administrators can start with agents requiring attention rather than searching the full inventory. The action center is expected to enter private preview in December.
- **Business use-case and task classification** in Agent Map will help administrators understand what agents do and identify agents performing similar work. These insights will support decisions about which agents to retain or consolidate. The capability is in preview.
- **Plugins and skills governance for Copilot and Cowork** lets administrators centrally manage plugin and skill availability and assign access to specific users and groups from the Microsoft 365 admin center. Plugins and skills governance is generally available.
- **Expanded governance for MCP servers and tools** will let administrators bring MCP servers from Azure AI Gateway and third-party gateways such as LiteLLM into a centralized governance experience, with visibility into tool use and dependencies and controls to manage availability, including understanding which plugins may be affected when an MCP server is blocked. Azure AI Gateway and LiteLLM gateway support is in preview.
- **Local and shadow agent governance** will add more granular controls beyond blocking. Administrators will also be able to observe local and shadow MCP servers and related activity to identify tools for investigation. This capability is in preview.

These updates build on Agent 365’s existing inventory and administrative controls to support ongoing governance as organizations deploy more agents.

[**Learn more about this update.**](https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753)

Microsoft Agent 365 is adding capabilities to help IT administrators monitor and manage AI agents and the tools they use. A new action center, expected in private preview in December, will help administrators identify inactive agents and those without owners. New Agent Map capabilities, in preview, will help identify agents performing similar work. New controls, now generally available, let administrators manage which users and groups can access plugins and skills. And additional features in preview provide more ways to monitor and control AI agents and the tools they connect to, including MCP servers.

#### New Microsoft Agent 365 capabilities help maximize value of AI investments

Instant Summary:

Microsoft Agent 365 is expanding its business value capabilities that help IT, business and security leaders optimize AI spend and turn investments into business impact. Now available in Frontier preview, **Agent 365 Business Analytics** helps leaders see where AI investments are delivering value. Additional enhancements expand reporting across Microsoft and third-party agent costs and outcomes, with recommendations to help improve efficiency and maximize the value of AI investments.

[**Learn more about this update.**](https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753)

Microsoft Agent 365 is adding business analytics capabilities, now available in Frontier preview, to help IT, business and security leaders understand the value of their AI investments. Expanded reporting covers costs and outcomes across Microsoft and third-party agents, with recommendations to help organizations improve efficiency and maximize business impact.

### Codename MDASH

#### Codename MDASH, a new agentic code security system, available in preview

Instant Summary:

**Codename MDASH, Microsoft’s agentic code security system**, is in preview for eligible organizations. It adds new capabilities that will help security and engineering teams work from validated findings. Advances in AI models are changing how vulnerabilities are discovered and exploited.

Codename MDASH uses more than 100 specialized AI agents in a four-stage pipeline. It will map the attack surface, scan code, validate findings through agent debate, remove duplicates and, where possible, reproduce findings with a triggering input.

New capabilities for Codename MDASH include:

- **Quality improvements:** Reduces low-quality results and false positives, so teams can spend less time triaging and more time on actionable vulnerabilities.
- **Repository sharding:** Analyzes large repositories by partitioning codebases into logical units, using fewer tokens per scan.
- **Progress visibility:** Makes scan stages, completed work, elapsed time and result availability more visible to better understand scan progress.
- **Broader MAI Cyber model support:** Codename MDASH now supports more of the MAI Cyber model family, including MAI Cyber 1.1 Flash, and will use MAI-Cyber-2 once evaluation testing is complete, improving efficiency while maintaining the quality of security findings.

[**Learn more about this news**](https://aka.ms/perceptionignite).

Codename MDASH, Microsoft’s agentic code security system, is in preview for eligible organizations. More than 100 specialized agents map attack surfaces, scan code, debate and validate findings, remove duplicates and reproduce vulnerabilities when possible. New quality controls, repository sharding and clearer progress reporting reduce false positives and token use, while broader MAI Cyber model support improves scanning efficiency maintaining validated results.

### Defender

#### Integrated Security Operations Center now generally available, vulnerability shielding in preview

Instant Summary:

Core capabilities in the **Integrated Security Operations Center** (ISOC) are generally available. The full breadth of Security Information and Event Management (SIEM) capabilities and 90 days of included Defender data retention are now in preview.

ISOC will bring SIEM and threat protection together to provide the foundation for the agentic SOC by giving people and agents a shared foundation to see, understand and act across the environment, with the cyber stack working as one system.  
  
Additionally, **vulnerability shielding** will expand attack disruption in Defender beyond containment of compromised assets to anticipating and shielding vulnerabilities. This will be an actuator in the new cyber stack and available in preview. The new shielding capability will help protect organizations during an active attack on their environment by autonomously deploying targeted, temporary controls to known vulnerable systems. This will prevent attackers from exploiting active vulnerabilities when a system isn’t patched yet and buy defenders more time to apply a permanent fix.

[**Learn more about this news.**](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/ignite-2026-whats-new-in-microsoft-defender--sentinel/4569975)

Core capabilities in Microsoft’s Integrated Security Operations Center (ISOC) are now generally available, giving people and agents a shared foundation that unifies threat protection and Security Information and Event Management (SIEM) workflows. Full SIEM breadth and 90 days of included Defender data retention are in preview, alongside vulnerability shielding — a new attack-disruption capability that autonomously applies targeted temporary controls to known vulnerable systems during active attacks, buying defenders time to deploy permanent patches.

#### Microsoft Defender extends runtime protection for local AI agents

Instant Summary:

By **extending runtime protection for local AI agents** on Windows, Microsoft Defender is helping organizations detect and stop malicious instructions while AI agents are operating across endpoints.

- **Agent-native runtime protection on Windows** is generally available for Claude Code, GitHub Copilot CLI, GitHub Copilot app, Claude Desktop (Code), VS Code GitHub Copilot extension and VS Code Claude Code extension.
- **Network-based runtime protection on Windows** is generally available for Open Claw, Ollama Desktop, ChatGPT Classic and ChatGPT Desktop (Chat).

Local AI agents can read files, interact with tools and take actions using users’ access, creating risk when malicious instructions hidden in the content an agent processes could influence unintended actions. Defender scans local AI agent calls for these threats, and with Network DLP, Microsoft Entra and Microsoft Purview can extend protection across data and access, helping prevent sensitive data from being exposed or exfiltrated over the network. Runtime protection can be configured in the Defender or Microsoft Intune portal with either Audit or Block mode selected.

Together, these updates help security teams protect local AI agents, sensitive data and access as agents become part of everyday work. Runtime protection for local AI agents will be available to Defender for Endpoint P2 customers.

[**Learn more about this news.**](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/ignite-2026-whats-new-in-microsoft-defender--sentinel/4569975)

Microsoft Defender now provides generally available runtime protection for a range of local AI agents on Windows, including GitHub Copilot, Claude, ChatGPT, Open Claw and Ollama experiences. It scans agent calls for malicious hidden instructions and works with Network DLP, Microsoft Entra and Purview to protect data and access. Defender for Endpoint P2 customers can configure controls in Audit or Block mode through Defender or Intune.

#### Microsoft threat intelligence adds zero-day and emerging threat insights

Instant Summary:

Threat intelligence in Microsoft Defender will add a new zero-day and emerging threats experience, available in preview, designed to help security teams spot the most urgent threats sooner and understand them faster.

Zero-day attacks exploit software flaws before a fix is available, giving organizations little or no warning. Emerging threats are new or rapidly developing threats where intelligence is still evolving.Information about these threats is often scattered across separate articles, reports, telemetry and incidents, making it hard for security teams to quickly see one clear, time-sensitive picture of what is happening. As AI increases the speed and reach of attacks, defenders need a faster way to know which threatsmatter most to them. The new capabilities, built into the revamped threat intelligence experience in Microsoft Defender, will bring zero-day and emerging threats to the forefront:

- **Zero-day and emerging threat tags:** Threat intelligence content about zero-day and emerging threats will be clearly labeled so it stands out from other threat intelligence articles.
- **Updated threat intelligence overview and threat analytics articles:** A new zero-day widget and a latest-threats view will highlight new zero-day and emerging threat research from Microsoft Security Research soon after discovery. Security teams will be able to filter by industry and region to focus on the threats most relevant to them.
- **Email notifications:** Security teams will be able to sign up to receive zero-day and emerging threat updates by email.
- **Protection validation:** From a threat analytics article, security teams will now be able to run the “Protect against a threat” playbook in Perception, which checks existing coverage and creates custom detections tailored to their environment, supplementing built-in protections.

[**Learn more about this update.**](https://www.microsoft.com/en-us/security/blog/2026/11/17/security-for-the-agentic-era-powered-by-microsoft-perception/)

Microsoft Defender is previewing a zero-day and emerging-threat experience that brings urgent, fast-changing intelligence into one prioritized view. New tags, widgets, industry and regional filters, refreshed analytics articles and email alerts help teams identify relevant threats sooner, while a Microsoft Perception playbook validates existing protections and creates environment-specific detections to supplement built-in defenses.

#### New investments to reduce on-premises security risk

Instant Summary:

A new **on-premises security initiative,** with guidance that will soon appear in Secure Now, is starting with supported Exchange Server, SharePoint Server and Skype for Business Server workloads. This initiative is designed to help organizations understand their most important risks, move eligible workloads to Microsoft 365 and better protect critical systems that need to remain on-premises.

The initiative brings together security guidance, migration support and product investments so organizations can reduce their on-premises footprint while strengthening the systems they retain. A key part of this initiative is **On-Premises Baseline Security Mode**, intended to build more of Microsoft’s recommended security settings into supported server products and reduce manual setup and ongoing maintenance.

The work will improve three areas: delivering security updates faster and helping them reach connected servers; making safer configurations easier to establish and maintain; and applying temporary protections against emerging threats until a permanent update is available.

Some protections and guidance are available today, including security updates, hardening guidance, health tools and emergency mitigation capabilities where supported. Additional capabilities will roll out over time, with availability varying by product and workload.

Microsoft continues to recommend moving eligible workloads to Microsoft 365 for cloud security and resilience. For systems that must remain on-premises, organizations can act now by using supported releases, applying updates promptly, enabling available protections and confirming that recovery plans are ready.

[**Learn more about this news**](https://aka.ms/OnpremSecInitiativeBlog).

Microsoft is launching an on-premises security initiative for supported Exchange Server, SharePoint Server and Skype for Business Server workloads. Guidance, migration support and future On-Premises Baseline Security Mode can help organizations reduce their server footprint, establish safer defaults, accelerate updates and apply temporary protections against emerging threats. Microsoft continues to recommend moving eligible workloads to Microsoft 365 and promptly updating and hardening systems that must remain on-premises.

### Entra

#### Microsoft Entra expands secure identity and access for agentic AI era

Instant Summary:

Microsoft Entra is introducing new capabilities to help organizations maintain visibility, control and protection across every AI interaction, while discovering, prioritizing and reducing identity security risks across their entire estate.

##### **Entra Agent ID**

- **Agent ID for discovered local agents**, in preview, will automatically assign an Agent ID to discovered local agents, starting with GitHub Copilot CLI and Claude Code, to separate agent from human activity and help secure their access.
- **Agent ID for Microsoft cloud agents**, in preview, will extend Agent ID to Microsoft Autopilot agents, so admins can secure their identity and access to resources.

##### **Entra ID**

- **Microsoft MCP Server for Enterprise** (generally available): Agents and applications access Microsoft Entra data through a controlled, permissions-based interface with natural language.
- **Conditional Access policy plans**, in preview, will simplify policy management at scale by expressing access intent once and enforcing granular controls consistently across identities.
- **High assurance credentials**, in preview, will strengthen identity assurance through verification across the account lifecycle, including onboarding, high-risk credential registration, privileged access and account recovery, with credential provenance.
- **Microsoft Entra Backup and Recovery Premium**, in preview, will improve resilience with 30-day backup retention and integration with Microsoft 365 Backup.

##### **Entra Tenant Governance**

- **Cross-tenant configuration management**, in preview, will maintain consistent identity and security configuration with a single-pane-of-glass experience to deploy, monitor and enforce resource configuration across all tenants.

##### **Entra ID Governance**

- **Privileged Identity Management**, in preview, will reduce the risk of privilege misuse and unauthorized access with just-in-time role and group activation, while enabling least-privilege access through MyAccess, secure Azure VM connectivity and greater control over standing access and privileged sessions.
- **Dynamic membership groups,** in preview, will reduce manual group maintenance with MemberOf Next and Transitive Reports To capabilities.

##### **Entra Global Secure Access**

Microsoft Entra Global Secure Access unifies Internet Access and Private Access, extending identity-aware Zero Trust controls across private apps, internet, SaaS, AI and agents.

- **Agentic traffic acquisition** (generally available): Improves visibility and enforcement by selectively acquiring agentic traffic.
- **Local agents**, in preview, will gain network visibility and control over local agents, destinations, MCP servers and resources.
- **MCP Firewall**, in preview, will control access to MCP servers, tools, resources, prompts, protocols and transports.
- **Unsanctioned agents**, in preview, will coordinate Intune, Defender and Global Secure Access policies through Agent 365.
- **Adaptive access**, in preview, will apply network policies and take into account evolving risk.

##### **Entra External ID**

- **Improved customer identity experiences** (preview): Flexible sign-in experiences with application-native authentication, hosted sign-in options, AI-assisted development and enhanced security controls.

[**Learn more about this news**](https://aka.ms/ignite/entra).

Microsoft Entra is expanding identity, access and network capabilities for people, agents and cross-tenant environments. Agent IDs in preview will distinguish local and Autopilot activity. New governance, backup, privileged-access, group and credential features will strengthen resilience and identity assurance. Agentic traffic acquisition, generally available in Global Secure Access, improves visibility and enforcement. And Microsoft MCP Server for Enterprise, generally available, provides permissions-based, natural-language access to Entra data.

#### AI Readiness Initiatives to strengthen security foundations

Instant Summary:

New AI Readiness Initiatives in Perception, in preview in January, will help organizations track progress against critical security work overtime. These initiatives are aligned to the priorities laid out in Secure Now, helping to strengthen security foundations and continuously reduce exposure across identities, devices, data, endpoints, AI agents, code, networks and more.

Each of the new initiatives will give agents and security teams a shared, structured plan for closing gaps in one area of their security foundation. Progress will be measured using live tenant data, giving teams evidence that gaps have been closed and exposure has gone down.

- **Patching and vulnerability management:** Will assess, shield and coordinate patching for priority vulnerabilities.
- **Modernize authentication:** Will strengthen administrator identity security by guiding the rollout of phishing-resistant passkeys.
- **Agent discovery and governance:** Will help organizations strengthen their security foundations for AI agents.

The patching and vulnerability management initiative is one example of how this approach works in practice, bringing agents and security teams together to continuously manage vulnerabilities discovered in the Monthly Windows Update. When new vulnerabilities are disclosed, agents can assess exposure, identify which vulnerabilities matter most in an organization’s environment, apply shielding where appropriate and coordinate permanent remediation through Microsoft Intune. Endpoint administrators maintain control over deployment, while agents help verify that risk has been reduced.

[**Learn more about this update**](https://aka.ms/exposurenewsignite).

New AI Readiness Initiatives in Microsoft Perception will enter preview in January, giving agents and security teams shared, measurable plans to strengthen foundations across identities, devices, data, endpoints, agents, code and networks. Initial initiatives cover vulnerability management, phishing-resistant authentication and agent governance, using live tenant data to measure progress. For monthly Windows vulnerabilities, agents can assess exposure, apply shielding and coordinate Intune remediation while administrators retain deployment control.

### Intune

#### Microsoft Intune helps secure AI adoption and reduce endpoint risk

Instant Summary:

Microsoft Intune is introducing new controls for **local AI agents governance**, in preview. IT will be able to discover which agents are running on managed devices with Microsoft Agent 365, mark devices with unapproved agents as noncompliant with Intune software compliance policies and apply Microsoft Entra Conditional Access to block those devices from company data.

For approved agents, Intune policies will define boundaries on what they can access and do with Microsoft Execution Containers. Microsoft Entra Global Secure Access will extend these protections to the network, with granular control over how local agents reach internet, SaaS and private resources.

Together, these capabilities will give IT visibility into the agents on their endpoints and the ability to act upon risk detection, so organizations can adopt AI agents without choosing between innovation and control.

**[Learn more about this news.](https://techcommunity.microsoft.com/blog/microsoftintuneblog/what%E2%80%99s-new-in-microsoft-intune-at-ignite/4570003)**

New Microsoft Intune controls for local AI agents governance are in preview. IT will be able to discover which agents are running on managed devices with Microsoft Agent 365, mark devices with unapproved agents as noncompliant with Intune policies and block those devices from company data with Microsoft Entra. Policies for approved agents define boundaries through Microsoft Execution Containers. Microsoft Entra Global Secure Access adds granular network controls over internet, SaaS and private-resource connections.

### Perception

#### New capabilities now available for Microsoft Perception

Instant Summary:

**Microsoft Perception**, previously known as Project Perception, is now generally available, including the agents and playbooks announced in July.

Microsoft Perception uses specialized agents and multi-agent workflows to carry out common security tasks. The agents have three roles: Red team agents look for weaknesses from an attacker’s perspective. Blue team agents triage alerts, investigate attacks, detect threats and create threat intelligence. Green team agents help prioritize security weaknesses, so teams know where to focus. Each agent performs a specialized task, while playbooks orchestrate their capabilities to address broader security challenges.

New capabilities include:

- **Broader triage and investigation:** The Triage Agent now covers about 80% of alerts in a typical Microsoft Defender queue. The Investigation Agent can follow attacks across endpoints, identities, email, Active Directory and cloud resources and recommend prioritized response actions.
- **Expanded third-party support:** The Triage Agent now handles AWS and Salesforce alerts and incidents. The Investigation Agent can reason over AWS and Okta data. The Detection Authoring Agent can reason over AWS, Salesforce and Okta data. Similarly, the Threat Intelligence Agent can turn external research into structured threat profiles and recommended actions.
- **New detection playbook:** The detect emerging threats playbook uses structured threat intelligence to create tenant-aware Kusto query language (KQL) detection recommendations, test them against historical data and suggest tuning.
- **Authorized web application testing:** The Web App Pen Test Agent, in preview, will validate exploitable weaknesses and provide evidence and remediation guidance through the Run web pen test and Protect web app playbooks.
- **Repository-scale vulnerability discovery:** Codename MDASH identifies and validates code vulnerabilities and supports developer and security workflows across Microsoft Defender, GitHub, Azure DevOps, CI/CD and Microsoft Security Exposure Management.
- **Agentic risk prioritization:** The Posture Prioritization Agent and playbooks for planning posture remediation and protecting against threats will help teams focus on critical exposures and plan coordinated protection.
- In preview, the **Reduce exposure risk** playbook will call on the Risk Reduction Agent to assess the available paths for reducing risk and recommend the right response. When a permanent fix is ready, the agent can coordinate patching through Microsoft Intune, with IT maintaining control of deployment. When patching is not immediately possible or could disrupt the business, the agent can help shield vulnerabilities by providing targeted protection while teams work toward the permanent fix.
- **Secure AI agents and playbooks:** An extension of agentic security will help teams investigate and reduce AI agent risk. Together, Microsoft Perception and Microsoft 365 bring signals, context and registry data into a consistent view of the agent landscape. Playbooks turn that understanding into prioritized remediation and coordinated response, helping teams contain risk and respond as agent behavior and access evolve. In private preview.
- **Playbooks within SOC workflows:** Teams can trigger playbooks automatically or launch them directly from Microsoft Defender.
- **API-first extensibility:** APIs and Model Context Protocol support enable organizations to start playbooks from ITSM, SIEM and SOAR tools and return agent sessions and artifacts to existing workflows.
- **Governance and cost transparency:** Least-privilege access, approval controls, audit logging, usage views and a cost calculator help organizations govern agent activity and plan spending.

[**Learn more about this news**](https://aka.ms/perceptionignite)**.**

Microsoft Perception is now generally available, orchestrating specialized red, blue and green security agents through playbooks for testing, investigation, detection, triaging and prioritizing weaknesses. Expanded agents cover about 80% of typical Defender alerts, follow attacks across Microsoft and third-party environments, create tenant-aware detection recommendations and validate exploitable weaknesses and code vulnerabilities. New previews add web-app testing, repository-scale vulnerability discovery, agentic risk prioritization, API-first extensibility, new playbooks and more.

### Purview

#### Microsoft Purview helps accelerate Copilot deployment and secure agent interactions

Instant Summary:

As businesses increasingly use AI to work with company information, they need to know which data is sensitive, who can access it and how to prevent it from being shared inappropriately. New Microsoft Purview capabilities in preview will address these challenges by:

- **Advancing faster time to protection** through high precision, scalable and up-to-date classification and labeling of sensitive data. Microsoft Purview will advance how it automatically classifies and labels sensitive information, such as financial records, personal information and confidential business documents, keeping the protections up to date while reducing the need for manual adjustments.
- **Accelerating Copilot adoption:** Data loss prevention capabilities for Copilot will be strengthened by grounding protection to block Copilot from referencing files with sensitive information even when those files are not labeled. It will also expand protection for prompts to include attachments, linked files and text.
- **Extending security capabilities for AI agents:** Microsoft Purview will extend data security capabilities for endpoint agents running on Windows, helping organizations control what data AI agents can access and share. Security teams will be able to apply protections to individual agents or groups of agents and help prevent sensitive information from being exposed through their conversations and connections to other tools.

[**Learn more about this news**](https://aka.ms/SecureData/Blog).

Microsoft Purview is previewing faster protections for sensitive data, stronger data loss prevention capabilities for Copilot and extended security capabilities for AI agents. The capabilities include more precise, scalable and up-to-date classification and labeling of sensitive data. Data loss prevention will be strengthened to block Copilot from referencing files with sensitive information even when those files are not labeled. Extended security capabilities for endpoint AI agents on Windows will help security teams prevent exposure of sensitive information through agent conversations and connections to other tools.

## Windows

Instant Summary:

As agents move from pilots to production, organizations are asking for clear governance over what agents can do, as well as more choice in where AI runs. New **process container controls** will provide IT more granular control to isolate and govern agents on Windows devices. Hybrid intelligence empowers organizations to run AI where it delivers the most value, with updates across **Windows** client, **Windows 365 Cloud PCs** and **Windows Server**, as well as new capabilities leveraging local context in **Copilot on Windows**. Built on a secure foundation, new **Windows** and **Intune** securityimprovements keep devices, apps and agents secure, current and under IT control.

New process container controls will help IT isolate and manage agents on Windows devices. Updates in Windows client, Windows 365 Cloud PCs and Windows Server and new capabilities leveraging local context in Copilot on Windows will help organizations govern and manage AI. New Windows and Intune security improvements will help keep devices, apps and agents secure, current and under IT control.

### Windows

#### Copilot on Windows improvements across file operations, PC diagnostics and in search

Instant Summary:

New capabilities in Copilot on Windows will leverage on-device context for troubleshooting and file management, as well as integrate easier access to Copilot from the taskbar. Updates, all in preview, include:

##### **Local file management in Copilot**

Copilot will support AI-assisted file management for files on Windows PCs. Users will be able to describe tasks like finding, organizing, moving, copying or renaming files in plain language, and Copilot will help carry out those actions.

##### **Local PC diagnostics in Copilot**

Copilot will be able to help diagnose issues on Windows PCs using Windows diagnostic information to better understand what may be causing a problem and provide clear explanations and recommended next steps.

##### **Easier access to Copilot in the new Windows Search experience**

As part of the new Search experience on Windows, users will be able to access Copilot directly from the taskbar to ask questions, get help with supported actions and find information from across their organization. Users can opt in to Copilot in Windows Search through Windows Settings, and IT administrators can manage the experience across their organization through policy.

[**Learn more about this news**](https://aka.ms/WindowsAtIgnite2026).

New capabilities in Copilot on Windows will leverage on-device context for troubleshooting and file management, as well as integrate easier access to Copilot from the taskbar. Users will be able to manage local files with natural language requests to Copilot and access the AI assistant directly from the taskbar in a new Windows Search experience.

#### New capabilities in Windows 365 across Direct Stream, Windows 365 admin assistant and more

Instant Summary:

Tens of thousands of organizations now use Windows 365 Cloud PCsto provide secure-by-design and simple-to-manage workspaces, and these new enhancements further streamline the experience:

- **Direct Stream**: The cloud streaming technology behind Windows 365 and Azure Virtual Desktop has enhancements now generally available for Cloud PC users that enable all-day productivity with more resilient connectivity and high-fidelity multimedia experiences across variable networks. Additionally, with Direct Stream enhancements made in collaboration with NVIDIA, GPU-enabled Cloud PC users will be able to work in graphically intensive applications with up to two 4K streams at 60 frames per second and low latency even in subpar network conditions (in preview early next year in select regions).
- **Windows 365 admin assistant:** An AI-powered experience in Microsoft Intune, now in preview, will enable IT admins to more easily monitor Cloud PC health, investigate issues, identify likely causes and accelerate troubleshooting.
- **Windows Mobile Application Management (MAM)**: Enables applying security and data-protection policies to the Windows App while allowing Windows devices accessing Cloud PCs to remain unmanaged. Now in preview.
- **Context-based redirections**: Enable dynamic allowing or restricting clipboard, drive, printer and USB redirections based on the trust level of each connection using Microsoft Entra authentication context. Now generally available.

[**Learn more about this news**](https://aka.ms/W365Ignite26Blog).

**[Download visual assets related to this news.](https://msftglobalcomms-my.sharepoint.com/:f:/g/personal/global_msftglobalcomms_onmicrosoft_com/IgAJqdt1iULvTqss9Pp2X7OsAZLyWlsaG6Et2trELnog9gM?e=AqG3uO)**

Windows 365 is improving Cloud PC performance, administration and data protection. Direct Stream enhancements, generally available, strengthen connectivity and multimedia quality. Starting early next year in select regions, users can run graphically intensive apps on GPU Cloud PCs more smoothly due to a collaboration with NVIDIA. Other updates include an Intune AI assistant for monitoring Cloud PC health, new security and data protection capabilities for the Windows App and context-based redirections based on Microsoft Entra authentication context.

#### New Windows and Microsoft Intune capabilities

Instant Summary:

Microsoft is introducing new Windows and Microsoft Intune capabilities designed to help organizations move AI from pilots into everyday work while keeping devices, applications and AI agents secure, current and under IT control.

**Windows baseline protection** (in private preview) will apply and maintain critical security settings to keep devices protected from the time the device boots up, reducing attack surface and enforcing hardware-rooted security and integrity features. The new **Windows Endpoint Security Platform,** now generally available, gives approved security products a safer way to protect devices while improving reliability.

Microsoft is also extending Windows management beyond PCs to include servers, applications and new Windows experiences. Microsoft Intune and Windows Autopatch will support **Windows Server 2028 for client-like scenarios** (in private preview) alongside PCs, while Enterprise App Management will **expand automatic updates** **to all Windows applications, not just those IT deployed** (in private preview). **Declarative device management** (in preview) will make sure that when IT defines the desired outcome, Windows works to apply and maintain it.

New **experience controls** (in private preview) will give IT teams time to evaluate and introduce upcoming Windows experiences and features on their own schedule with recommended controls.

Additional **OS reliability reporting** (in private preview) in Windows Autopatch will surface reliability insights so IT can patch faster and more confidently, stay compliant, understand Windows stop error trends, spot recurring failure patterns and see exactly which devices are affected. Together, these capabilities will bring security, management and intelligent assistance into a more unified experience.

[**Learn more about this news**](https://aka.ms/WindowsAtIgnite2026).

New Windows and Microsoft Intune capabilities include updated baseline protections and a new endpoint security platform. Intune and Windows Autopatch will support Windows Server 2028, and automatic updates will expand to all Windows applications, not just those deployed by IT. Other updates include declarative device management, new controls for IT and OS reliability reporting in Windows Autopatch for reliability insights.

#### Windows 365 for Agents scales to Microsoft Foundry, introduces persistent Cloud PCs

Instant Summary:

With the rising adoption of computer-using agents, IT increasingly needs to deliver secure, managed and reliable workspaces at scale, not only for people but also for agents doing work in organizations. **Windows 365 for Agents** is introducing new capabilities to enable running enterprise-ready AI agents securely at scale. This is particularly useful for organizations with legacy business applications without APIs.

- Windows 365 for Agents is now **eligible for Copilot Credits**—a common currency for eligible Microsoft services with usage-based billing—enabling a unified AI billing, governance, reporting and cost-management experience.
- Agent makers can bring Windows 365 for Agents into their agent experiences through Microsoft Copilot Studio as well as Microsoft Foundry. In Copilot Studio, Windows 365 for Agents is available as a computer-use tool in the Standard harness and will be in preview in the Microsoft Copilot harness in December. In preview early next year, Foundry builders will be able to use the Windows 365 for Agents Model Context Protocol (MCP) to enable agents to execute computer-use tasks on governed Cloud PCs.
- Agents using Windows 365 for Agents Cloud PCs will be able to **access on-premises** **applications using agent identities** (in preview) to extend automation across legacy business applications without APIs.
- Windows 365 for Agents will **support persistent Cloud PCs** in Frontier (in preview), helping IT admins deploy, manage and secure always-on personal agents. This will enable long-running business process automation while maintaining enterprise security and compliance.

[**Learn more about this news**](https://aka.ms/W365Ignite26Blog).

**[Download visual assets related to this news.](https://msftglobalcomms-my.sharepoint.com/:f:/g/personal/global_msftglobalcomms_onmicrosoft_com/IgD9mkHr64w1T6W7Yvv_-FgLAc8umkBrTpBIDl_IQ6SCtAI?e=DINHs0)**

Windows 365 for Agentsis now eligible for Copilot Credits for a unified AI billing, governance, reporting and cost-management experience. The platform is available in the Standard harness in Copilot Studio and will be in preview in the Microsoft Copilot harness by December. Early next year, Foundry builders will be able to use the Windows 365 for Agents Model Context Protocol in preview. Agents on Windows 365 for Agents Cloud PCs will be able to access on-premises applications using agent identities, extending automation to legacy apps without APIs. Windows 365 for Agents will also support persistent Cloud PCs, helping IT admins deploy, manage and secure always-on personal agents.

#### Windows expands local and hybrid capabilities

Instant Summary:

Windows now supports a wider range of AI workload placement by adding local model execution, hybrid orchestration and expanded Cloud PC and server‑based options.

Together, these updates provide additional execution paths for AI workloads across local PCs, Cloud PCs and server‑based environments. Updates include:

- **Windows 365 Cloud PCs support running the latest local AI models**, including up to 32 vCPU and GPU-enabled Cloud PCs for development and AI workloads. This is generally available. With Foundry Local, developers can run compatible AI models directly on appropriately sized Cloud PCs, with predictable subscription costs for workloads that require more compute capacity or performance.
- **Windows Server 2025 with AVD Hybrid** (in private preview) will support multi-user AI development environments managed through Windows Server and Azure Virtual Desktop infrastructure. Organizations will be able to run supported models within environments they manage directly rather than relying exclusively on cloud-hosted inference.

[**Learn more about this news**](https://aka.ms/WindowsAtIgnite2026).

Windows now supports a wider range of AI workload placement by adding local model execution, hybrid orchestration and expanded Cloud PC and server‑based options. Updates include Windows 365 Cloud PCs support for running the latest local AI models, including up to 32 vCPU and GPU-enabled Cloud PCs. With Foundry Local, developers can run compatible AI models directly on appropriately sized Cloud PCs. Additionally, Windows Server 2025 with AVD Hybrid will support multi-user AI development environments managed through Windows Server and Azure Virtual Desktop infrastructure.

#### Windows introduces controls that help isolate and govern AI agents

Instant Summary:

Windows is introducing new process container controls that provide Component Object Model (COM) and Inter-Process Communication (IPC) governance, granular network policies and identity‑proofing protections, giving organizations clearer boundaries around how agents operate and how their activity is isolated, observed and governed.

These updates, all in preview, include:

- **Process container capabilities** will give each running agent or app a protected workspace with clear limits on what it can talk to, which networks it can reach and how it proves its identity. This will reduce the risk of an agent accessing the wrong data, impersonating something else or affecting the rest of the device.
- **Learning and permissive mode**, now generally available, will allow teams to observe how an agent normally communicates with system services before fully enforcing restrictions. This will help admins create policies safely without breaking legitimate workflows during rollout.

[**Learn more about this news**](https://aka.ms/WindowsAtIgnite2026).

Windows is introducing new process container controls that provide COM and IPC governance, granular network policies and identity‑proofing protections, giving organizations clearer boundaries around how agents operate and how their activity is isolated, observed and governed. The process-container controls will give each running agent or app a protected workspace with clear limits on what it can talk to. A new learning and permissive mode will allow teams to observe how an agent normally communicates with system services before fully enforcing restrictions.
