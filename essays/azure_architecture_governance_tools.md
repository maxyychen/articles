# Azure's Architecture Governance & Design Toolset

## 1. Guidance & decision frameworks (the "how should we design this")

- **Azure Well-Architected Framework** — five pillars (reliability, security, cost, ops excellence, performance) with per-service guides; recently expanded with AI-workload and HPC design patterns and a rewritten SQL MI guide.
- **Azure Architecture Center** — reference architectures, design patterns, and a changelog tracking new guidance as it ships.
- **Cloud Adoption Framework (CAF)** — the org-level playbook (strategy → ready → govern → manage) that Landing Zones and governance policy are built from.

## 2. Structural/foundational governance (the "what gets built and how it's controlled")

- **Azure Landing Zones** — CAF-aligned pre-built environment (management groups, subscriptions, policy, identity, networking) that new workloads land into; the standard starting point for enterprise governance.
- **Azure Policy** — the core enforcement mechanism (100+ built-in policies typically assigned across management groups), including `DeployIfNotExists`/`Modify` effects to auto-remediate non-compliant resources.
- **Deployment Stacks + Template Specs** — the replacement for **Azure Blueprints**, which is being retired (phased retirement started July 31, 2026, full retirement Jan 31, 2027). Template Specs version your IaC definitions; Deployment Stacks manage a resource set as a single locked, atomic unit and prevent drift.
- **Azure Resource Graph** — query engine for auditing resource state/compliance at scale across subscriptions.

## 3. API/agent governance (the newer layer)

- **Azure API Center** — centralized inventory for governance across REST, GraphQL, gRPC, SOAP, WebSocket/Webhook APIs, and now **MCP servers and A2A agents** — effectively extending API governance to agentic assets.
- **Azure API Management** — enforcement point (gateway, auth, versioning, oversight) for both traditional APIs and the new A2A/MCP traffic.

## 4. Security & data governance

- **Microsoft Defender for Cloud** — continuous posture management (CSPM) and workload protection; now includes **AI Security Posture Management** and multi-cloud (AWS/GCP) posture coverage.
- **Microsoft Purview** — data governance, discovery, compliance; now includes **Data Security Posture Management (DSPM) for AI** and **AI Data Security Investigations**, extending governance to what data agents can see/use.
- Defender + Purview + Sentinel together are Microsoft's recommended stack for governing an "AI Landing Zone."

## 5. Cost & recommendations

- **Azure Advisor** — ongoing recommendations across cost/security/reliability/performance mapped to Well-Architected pillars (not new, but the delivery mechanism for WAF guidance in-portal).

## Net picture

Azure's governance stack has a clear division of labor — CAF/Landing Zones set the org-level structure, Azure Policy + Deployment Stacks enforce and lock configuration, API Center/APIM govern the interface layer (now including agents), and Defender/Purview govern security and data. The most notable 2026 shift is that this same governance model is being extended to agentic workloads rather than treated as a separate concern — MCP servers and A2A agents show up in API Center right alongside REST APIs, and Purview/Defender now have AI-specific posture and data-risk modules.

## Sources

- [Azure governance design area — Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/governance)
- [Azure landing zone design principles — Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-principles)
- [What's New in Microsoft's Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/whats-new)
- [Azure Governance Visualizer Deployment Guidance — Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/azure-governance-visualizer-accelerator)
- [Chapter 14 — Deployment Stacks | Azure Governance](https://azgovernance.com/guide/part-4-iac-deployment/ch14-deployment-stacks.html)
- [Migrate blueprints to deployment stacks — Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/migrate-blueprint)
- [Azure Blueprints retirement — Azure Blueprints](https://learn.microsoft.com/en-us/azure/governance/blueprints/blueprint-retirement)
- [Azure Blueprints are dead: long live Specs and Stacks?](https://azurescholar.cloud/azure-blueprints-are-dead-long-live-specs-and-stacks)
- [Azure API Center — Key concepts](https://learn.microsoft.com/en-us/azure/api-center/key-concepts)
- [Azure API Management Landing Zone Architecture — Azure Architecture Center](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/app-platform/api-management/governance)
- [What's new in Azure API Management at Build 2026](https://techcommunity.microsoft.com/blog/integrationsonazureblog/whats-new-in-azure-api-management-at-microsoft-build-2026/4524683)
- [Securing AI Workloads with Defender for Cloud, Purview and Sentinel in Azure Landing Zones](https://techcommunity.microsoft.com/blog/azurearchitectureblog/securing-ai-workloads-with-microsoft-defender-for-cloud-purview-and-sentinel-in-/4457345)
- [Microsoft Defender Cloud Security Posture Management](https://www.microsoft.com/en-us/security/business/cloud-security/microsoft-defender-cloud-security-posture-management)
- [Microsoft Purview: Data Security and Governance](https://www.microsoft.com/en-us/security/business/microsoft-purview)
- [What's new in Microsoft Security: July 2026](https://www.microsoft.com/en-us/security/blog/2026/07/30/whats-new-in-microsoft-security-july-2026/)
