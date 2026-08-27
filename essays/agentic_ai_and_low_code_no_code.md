# How Agentic AI Is Reshaping No-Code/Low-Code Development (2026)

**TL;DR**
- Agentic AI isn't a bolt-on feature for no-code/low-code (NCLC) platforms anymore — every major vendor has rebuilt around it.
- Analysts disagree on the outcome. Gartner and Forrester say AI **grows** the low-code market. Many practitioners say AI coding agents ("vibe coding") are quietly **replacing** it.
- Both are right — just in different segments. That split, not a single winner, is the real story (see §6).

**Contents**
1. [Definitions](#1-definitions-what-agentic-ai-adds-to-nclc)
2. [Vendor landscape](#2-vendor-landscape-how-the-incumbents-responded)
3. [The bull case](#3-the-bull-case-ai-grows-the-low-code-market)
4. [The bear case](#4-the-bear-case-ai-is-eating-low-codes-lunch)
5. [Governance and security risks](#5-governance-security-and-the-citizen-developer-risk-surface)
6. [Where the two cases resolve](#6-where-the-two-camps-actually-resolve-a-segmented-market-not-a-winner-take-all)
7. [The evolving developer role](#7-the-evolving-developerciting-developer-role)
8. [Key takeaways](#8-key-takeaways)
- [Sources](#sources)
- [Appendix: Governance framework for agentic AI-assisted ERP development](#appendix-governing-agentic-ai-in-enterprise-erp-development--an-applied-framework)

---

## 1. Definitions: what "agentic AI" adds to NCLC

**No-code/low-code (NCLC):** visual, declarative development — drag-and-drop builders, workflow canvases, DSLs, pre-built connectors. Built so people can create software with little or no hand-written code.

**Agentic AI:** AI that plans, calls tools/APIs, takes multi-step actions, observes results, and adapts — working toward a goal, not just responding to a single prompt. This is different from the older "AI features" already inside NCLC tools (autofill, smart suggestions), which were assistive, not autonomous. ([Taxonomy paper](https://arxiv.org/pdf/2505.10468))

Two distinct things are converging under the "agentic AI + low-code" banner. Conflating them is the main source of market confusion:

- **(a) AI as the builder** — natural-language tools where an LLM agent constructs the app or workflow for you.
  *Examples: Bubble AI Agent, Retool Assist, Zapier Canvas, Mendix Agent Builder.*
- **(b) AI as the artifact** — low-code platforms are no longer just for CRUD apps and workflows. They're now a preferred substrate for building, governing, and deploying **AI agents themselves** (orchestration, MCP wiring, guardrails, observability) — competing with code-first agent frameworks like LangChain/LangGraph.

They pull in different directions: **(a)** lowers the skill needed to *use* low-code. **(b)** expands what low-code is *used for*.

---

## 2. Vendor landscape: how the incumbents responded

| Platform | Agentic move | What it signals |
|---|---|---|
| **OutSystems** | "Agentic Systems Platform" + "Agent Workbench" on an Enterprise Context Graph; an "Agent Experience" layer exposing A2A/MCP so external tools (Claude Code, Codex, Cursor) can inspect/extend the platform | Betting the platform becomes the *governance and context layer* under any agent, not just a UI builder |
| **Mendix** | "Agents Kit" and "Agent Builder" in Mendix 11 | Same "governed agent factory" bet, aimed at large enterprise IT |
| **Microsoft Power Platform** | MCP server inside Power Apps (Apr 2026) letting business users wire agents into ~1,100 enterprise systems, no code; Copilot Studio for agent building | Pushes agent-building down to business users, on top of Microsoft's connector graph |
| **Retool** | "Assist" (text-to-app, public beta); AI Agents for reasoning over live data; natural-language dashboards | Repositioning from "internal tool builder" to "AI-powered operational tool" builder |
| **Bubble** | Bubble AI Agent (Oct 2025) generates pages/workflows and understands app architecture; AI App Generation builds full MVPs in 5–7 minutes from a prompt | Chasing the "vibe coding" experience without leaving Bubble's governed runtime |
| **Zapier** | Zapier Central: persistent AI agents across 7,000+ integrations; Zapier Canvas: draw a flowchart → AI configures the Zaps | Turning its integration graph into an agent-execution substrate |
| **n8n, Langflow, Workato** | MCP servers; visual agent-orchestration canvases; existing recipes exposed as MCP tools any LLM agent can call | Positioning as the *tool layer* agentic AI calls into, not just a user-facing builder |

**The common pattern:**
- Nearly every vendor converges on the same architecture: a governed, context-aware backend (connectors, data model, permissions, audit) exposed to agents via MCP/A2A, with a visual or conversational front end.
- The pitch to enterprises is explicit: *"use any AI agent you like — Claude Code, Cursor, whatever — but run it through us for governance, context, and control."*
- It's a defensive and offensive move at once: it keeps the platform relevant even to developers who'd rather use a coding agent directly.

---

## 3. The bull case: AI grows the low-code market

- **Analyst consensus.** Gartner and Forrester both argue AI will "enhance, not replace" low-code. Forrester's Bratincevic and Lo Giudice make a specific claim: natural language alone is *insufficient* as the sole way to author software — non-coders still need a visual, declarative surface to verify and adjust what got generated. NL-generation becomes a complement to visual tools, not a replacement.
- **Market sizing.** Forrester's growth scenario puts the combined low-code + digital process automation market on a path from ~$13.2B (2023) to $50B (2028) if AI adoption accelerates it (~33% CAGR). Broader 2026 estimates for the low-code/no-code market cluster around $58–65B, heading toward $150–190B by 2029–2030. Some no-code-AI-specific forecasts go as high as $72.9B by 2035. Gartner projects 80% of mission-critical apps will run on low-code by 2029.
- **Agent adoption inside enterprise apps.** Gartner predicts 40% of enterprise applications will embed task-specific AI agents by end of 2026, up from under 5% in 2025. Low-code vendors are positioning themselves as the fastest, most governed path to that number — versus a hand-rolled agent stack.
- **Productivity, still the core NCLC pitch.** NCLC projects reportedly complete in ~3.2 weeks vs. 14.8 weeks for traditional development (~74% faster time-to-market). Other cited figures: ~60% faster app delivery generally, new developers ~80% more productive, and average 3-year ROI of 342% in vendor-commissioned Forrester studies. Agentic features are marketed as compounding this by automating the remaining manual configuration.
- **Democratization.** Citizen developers already dominate the low-code user base — Gartner expects 80%+ of that base to be non-IT by 2026 (up from 60% in 2021), and 41% of enterprise employees report having built at least one app with NCLC tools. Advocates argue agentic AI expands this base further, since most citizen developers were never going to become full-code AI-agent engineers regardless of how good coding agents get.

---

## 4. The bear case: AI is eating low-code's lunch

- **The core argument.** Low-code's original pitch was "build software with less developer time and skill." AI coding agents now deliver that same outcome for *real* code — often faster and cheaper, without low-code's classic drawbacks: vendor lock-in, runtime ceilings, per-seat/per-workflow pricing, awkward escape hatches. Once an AI agent can generate, test, and maintain a working custom app, the ROI case for a proprietary low-code runtime weakens — especially for teams with some in-house technical capacity.
- **Case in point.** Cloud Capital reportedly migrated its internal tools entirely off Retool to AI-assisted, hand-written code within "a couple of sprints" — and reported better maintainability, safety, and UX than the low-code version.
- **"RIP Low-Code 2014–2025" framing.** Some commentators treat the AI-coding-agent wave as an extinction-level event for the *classic*, proprietary-runtime low-code category specifically. Their argument: platform vendors are bolting on AI defensively, but are structurally outpaced by foundation-model labs and code-first agent tools that iterate much faster.
- **Vibe coding is the faster-growing competitor.** "Vibe coding" — natural-language-to-real-code via Claude Code, Cursor, Replit Agent, Lovable, and similar — is estimated at ~$4.7B and growing ~85% year-over-year, far outpacing the broader NCLC market. It removes the lock-in and ceiling problems low-code always carried. **But** most analyses converge on one enterprise caveat: vibe coding currently lacks the governance, security, compliance, and audit trail that regulated or cross-departmental production apps require — exactly what governed NCLC platforms already provide. This caveat is the crux of the market split covered in §6.
- **A caution that cuts both ways.** Gartner also warns that over 40% of agentic AI *projects* will be cancelled by end of 2027 over cost, unclear value, or inadequate risk controls — a reminder that agentic capability doesn't automatically translate into either low-code's growth or its replacement.

---

## 5. Governance, security, and the "citizen developer" risk surface

Agentic AI sharply raises the stakes of a risk NCLC already had: non-technical people building things IT can't see.

- **Shadow IT → shadow agents.** ~61% of organizations cite shadow-IT risk from ungoverned citizen development as a leading concern; roughly 41% of employees now qualify as "citizen developers" building outside formal IT oversight. Self-serve agent-builder platforms turn "shadow apps" into "shadow agents" — software that can autonomously call tools, move data, and take actions. That's a much larger blast radius than a static shadow spreadsheet-app ever had.
- **The governance gap.** Surveys put ~73% of low-code *planners* and ~65% of *users* as lacking formal governance rules. Fewer than 30% of security leaders report having a formal governance framework in place — despite ~65% naming shadow IT a top-three security concern.
- **Regulatory pressure.** The EU AI Act's full enforcement for high-risk systems began August 2, 2026 — adding a compliance layer that citizen-built agentic apps can trigger inadvertently, often while sitting outside the organization's normal governance visibility.
- **MCP is a double-edged sword.** The same Model Context Protocol that lets low-code platforms cleanly expose enterprise systems to agents is also a fast-growing, under-governed attack surface: tool-schema sprawl, credential exposure, and unvetted third-party MCP servers are recurring findings in 2026 security research — echoing the broader API-sprawl risk seen in agentic API traffic generally.
- **The vendor response.** This is exactly why OutSystems, Mendix, and Power Platform emphasize "governed" agent building — context graphs, permissioning, audit, approved-connector catalogs — as their differentiator against both raw vibe-coding and ungoverned open-source agent frameworks. Governance, not ease-of-use, is becoming the incumbents' main pitch.

---

## 6. Where the two camps actually resolve: a segmented market, not a winner-take-all

Reading the bull and bear cases together, the emerging 2026 consensus isn't "AI kills low-code" or "AI merely accelerates it." It's that **agentic AI is splitting NCLC's traditional audience into two very different jobs-to-be-done**, and different tools win each one:

1. **Personal/small-team prototypes, internal scripts, one-off automations, technically-capable builders** → increasingly served directly by AI coding agents / vibe coding, bypassing low-code entirely. **This is the segment low-code is genuinely losing.**
2. **Governed, cross-departmental, regulated, or mission-critical enterprise systems** → increasingly served by NCLC platforms *because* they now embed agent-building. Enterprises want the agent capability, but need the governance, context graph, connector catalog, and audit trail a raw coding agent doesn't provide out of the box. **This is the segment where NCLC is actively growing.**

**Practical implication:** use a coding agent when speed and full customizability matter more than governance, and you have (or can borrow) the technical judgment to review the output. Use an agentic low-code platform when the app touches multiple systems, regulated data, or non-technical maintainers, and needs built-in guardrails from day one.

---

## 7. The evolving developer/citizen-developer role

A consistent trajectory shows up across both vendor material and academic work — this is about *how people work*, not just what tools they use:

- **The authoring pattern is shifting in stages:** visual drag-and-drop → conversational app generation → goal-driven agents that build and refine workflows on their own (Forrester's stated three-stage evolution).
- **Professional developers move up the stack** — from hand-placing components to defining the standards, guardrails, data models, and integration contracts that agents (AI-built or human-built) must operate within. It's a supervisory/architect role, not a component-assembly one.
- **Academic work tracks a parallel shift inside model-driven engineering (MDE):**
  - A 2026 systematic mapping study (86 primary studies, 2022–early 2026) surveys how LLMs are being folded into MDE pipelines.
  - A MODELS 2024 paper, *"Turning Low-Code Development Platforms into True No-Code with LLMs,"* proposes replacing textual/DSL modeling steps with LLM-generated models — so genuinely non-technical users can operate tools that were previously low-code, not no-code.
  - An ICLR 2026 paper on a *Bayesian Adversarial Multi-Agent* low-code platform for scientific computing shows the same "multi-agent-as-the-builder" pattern (task-manager, code-generator, and evaluator agents cooperating) appearing in domain-specific tools, not just general business-app platforms.
- **Net effect on skill requirements:** the floor for "who can produce something that works" keeps dropping — via both low-code and vibe coding. But the *ceiling skill* needed to make that output safe, correct, and maintainable at enterprise scale is rising, because agents now generate more complexity per unit of human review time than before.

---

## 8. Key takeaways

- Agentic AI is existential-stakes for the NCLC category, and the stakes cut both ways: it's simultaneously the biggest competitive threat (vibe coding eating the "build software without a big dev team" pitch) and the biggest growth vector (every major vendor now sells "governed agent building" as its core 2026 product).
- The decisive variable isn't raw capability — AI coding agents can demonstrably produce production-grade software. It's **governance, auditability, and organizational context**, which is exactly what enterprise low-code platforms are racing to bundle around agent-building before code-first tools catch up on that dimension.
- Expect continued consolidation around **MCP/A2A as the connective tissue** between whatever front end a builder uses (visual canvas, chat, or hand-written code) and a governed enterprise backend. The "low-code platform" of 2027 looks less like a UI builder and more like a context/governance layer any agent plugs into.
- **For organizations deciding today:** match the tool to the governance requirement, not the hype cycle. Vibe coding for disposable/prototype work by technically capable owners. Agentic low-code platforms for anything that will outlive its creator, touch regulated data, or need multi-department sign-off.

---

## Sources

**Market and industry analysis**
- [Top AI Agent No-Code Platforms in 2026 — Konverso](https://www.konverso.ai/en/blog/top-ai-agent-no-code-platforms-in-2026)
- [Top 14 Low-code AI Agent Platforms for Product Managers in 2026 — Vellum](https://www.vellum.ai/blog/top-low-code-ai-agent-platforms-for-product-managers)
- [Low-Code and No-Code in 2026 — Codewave](https://codewave.com/insights/understanding-low-code-no-code-development/)
- [Best No-Code AI Platforms for Building Apps — Kissflow](https://kissflow.com/no-code/what-are-the-best-no-code-ai-platforms-for-building-apps/)
- [6 Low-Code AI Agent Platforms for 2026 — Budibase](https://budibase.com/blog/ai-agents/low-code-ai-agent-platforms/)
- [Best Low-Code AI Agents Platforms for 2026 — Rasa](https://rasa.com/blog/best-low-code-ai-agents-platforms-for-2026)
- [2026 Low-Code/No-Code Predictions — DEVOPSdigest](https://www.devopsdigest.com/2026-low-code-no-code-predictions)
- [No-code vs low-code vs code — MindStudio](https://www.mindstudio.ai/blog/no-code-vs-low-code-vs-code)
- [Enterprise Low-Code Platforms Are a Launchpad for Implementing Agentic AI — Gartner](https://www.gartner.com/en/documents/7215730)
- [Low-Code Trends & Statistics Shaping Enterprise IT in 2026 — Kissflow](https://kissflow.com/low-code/low-code-trends-statistics/)
- [Gartner Insights: The Future is Low-Code AI Platforms — OutSystems](https://www.outsystems.com/1/low-code-ai-platforms-gartner/)
- [Forecast Analysis: Low-Code Development Technologies, Worldwide — Gartner](https://www.gartner.com/en/documents/7146430)
- [AI Agent Adoption 2026: What the Data Shows — Joget (Gartner/IDC)](https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/)
- [The State Of Agentic AI In 2026 — Forrester](https://www.forrester.com/blogs/the-state-of-agentic-ai-in-2026-companies-are-chasing-few-are-catching/)
- [Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025)
- [New Research: Will AI Kill The Low-Code Market? — Forrester](https://www.forrester.com/blogs/new-research-will-ai-kill-the-low-code-market/)
- [Low-Code Statistics 2026: 60+ Facts, Figures & Trends — ToolJet](https://blog.tooljet.com/low-code-statistics-market-ai-trends-2026/)
- [Low Code Statistics 2026: Market Size, Adoption, ROI, Enterprise Trends — CMARIX](https://www.cmarix.com/blog/low-code-statistics-and-trends/)
- [Top 50 No-Code and Low-Code Statistics for 2026 — Index.dev](https://www.index.dev/blog/no-code-low-code-statistics)
- [The State of No-Code in 2026 — Caspio](https://www.caspio.com/blog/state-of-no-code-2026/)

**Vendor / platform moves**
- [OutSystems Unveils Open Agentic Systems Platform for Enterprise AI](https://www.outsystems.com/news/outsystems-announces-agentic-systems-platform)
- [OutSystems Introduces Agentic Systems Engineering](https://www.outsystems.com/news/outsystems-agentic-systems-engineering-announcement)
- [Scale Agentic AI Systems with Agent Workbench — OutSystems](https://www.outsystems.com/low-code-platform/agentic-ai-workbench)
- [Mendix launches new release to meet surging demand for agentic AI](https://www.mendix.com/press/mendix-launches-new-release-to-meet-surging-demand-for-agentic-ai/)
- [Agentic AI in Action — Mendix](https://www.mendix.com/resources/agentic-ai-in-action/)
- [GenAI Agents — Mendix Documentation](https://docs.mendix.com/agents/agents/)
- [Mendix vs. OutSystems: 7 Powerful Agentic Low-Code Wins](https://www.progressiverobot.com/2026/04/29/mendix-vs-outsystems/)
- [Microsoft Power Apps MCP Server: Low-Code AI Agents — AI Magicx](https://www.aimagicx.com/blog/power-apps-mcp-server-low-code-agents-2026)
- [Retool Reviews 2026 — G2](https://www.g2.com/products/retool/reviews)
- [Retool Review: AI App Builder — AIIDEList](https://aiidelist.com/ide/retool)
- [20 Best AI App Builders in 2026 — Taskade](https://www.taskade.com/blog/best-ai-app-builders)
- [Enterprise AI agent development tools 2026 — n8n](https://n8n.io/reports/2026-ai-agent-development-tools/)
- [Best Enterprise AI Integration Platforms: MCP, Data Connectivity & Agent Orchestration — Medium](https://medium.com/@eliovasken/best-enterprise-ai-integration-platforms-mcp-data-connectivity-agent-orchestration-tools-52a86b8b8a65)
- [Building Enterprise AI Agents with a Managed MCP Platform — CData](https://www.cdata.com/blog/enterprise-ai-agents-managed-mcp-platform)
- [Oracle AI Database Private Agent Factory: MCP, Orchestration, Multi-Agent Workflows](https://blogs.oracle.com/ai-and-datascience/oracle-private-agent-factory-mcp-multi-agent)

**The "AI kills/doesn't kill low-code" debate**
- [Low Code No Code Agentic AI systems and tools — SAP Community](https://community.sap.com/t5/technology-blog-posts-by-sap/low-code-no-code-agentic-ai-systems-and-tools/ba-p/14291228)
- [No-Code AI Tools Empower Everyone to Build AI Agents — OneReach.ai](https://onereach.ai/blog/agent-platforms-democratizing-ai-agent-development/)
- [The Future of Low-Code/No-Code: When AI Agents Become the Platform — Medium (George Wen)](https://medium.com/@georgewen7/the-future-of-low-code-no-code-when-ai-agents-become-the-platform-756843d6775b)
- [Why Low-Code and No-Code Are Already Losing to Agentic AI — dev-end.com](https://dev-end.com/blog/why-lowcode-nocode-is-losing-to-agentic-ai)
- [RIP Low-Code 2014–2025 — Zack Liscio](https://www.zackliscio.com/posts/rip-low-code-2014-2025/)
- [Is Software Really Dead? Why Agentic AI Won't Kill It — MarketWise](https://marketwise.com/investing/death-of-software-exaggerated-why-agentic-ai-wont-kill-it/)
- [The Future of Low-Code: Trends Shaping 2026–2030 — Medium (Nigel Tape)](https://medium.com/@EnterpriseToolingInsights/the-future-of-low-code-trends-shaping-2026-2030-ddf4a475fd62)

**Governance, security, and citizen development**
- [The Vibe Coding Governance Gap — Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-research-note-vibe-coding-ai-governance-gap-20260602-csa/)
- [Citizen Developer: What It Is, Tools & Governance (2026) — WeWeb](https://www.weweb.io/blog/citizen-developer-tools-governance-guide)
- [Shadow IT Governance for AI Agents — Cosnet Global](https://cosnetglobal.com/blogs/shadow-it-governance-for-ai-agents/)
- [Citizen Development in 2026: Benefits, Risks, and Limits — Opsima](https://opsima.com/blog/operational-insights/citizen-development/)
- [Low-Code Governance: A Framework for Citizen Development — TxMinds](https://www.txminds.com/blog/low-code-governance-citizen-development/)
- [Democratizing Agentic AI: How Low-Code Builder Platforms Empower Citizen Developers — Cyber Gear](https://www.cyber-gear.ai/democratizing-agentic-ai-how-low-code-builder-platforms-empower-citizen-developers/)

**Vibe coding vs. no-code/low-code**
- [No-Code vs. Low-Code vs. Vibe Coding: Which Should You Use in 2026? — Medium (Gozade)](https://medium.com/@gozade/no-code-vs-low-code-vs-vibe-coding-which-should-you-use-in-2026-0f2a5e8c44ef)
- [Vibe Coding vs No-Code vs Low-Code: Enterprise Guide 2026 — Kissflow](https://kissflow.com/no-code/vibe-coding-vs-no-code-vs-low-code/)
- [Vibe Coding vs No-Code vs Low-Code Comparison — Taskade](https://www.taskade.com/blog/vibe-coding-vs-no-code-vs-low-code)
- [No-Code vs Vibe Coding: What Enterprise Teams Must Know — Kissflow](https://kissflow.com/no-code/no-code-vs-vibe-coding-enterprise-guide/)
- [Vibe Coding vs Low-Code: Key Differences Explained — Memberstack](https://www.memberstack.com/blog/how-does-vibe-coding-compare-to-low-code-platforms)
- [Vibe Coding vs Low-Code: Build Apps in 2026 — Yaabot](https://yaabot.com/41493/vibe-coding-vs-low-code-vs-no-code/)
- [Vibe Coding vs. Low-Code: A Guide for Enterprise Teams — Liferay](https://www.liferay.com/resource-hub/guides/vibe-coding-vs-low-code)

**Academic papers**
- [AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework (ICLR 2026) — arXiv:2603.03233](https://arxiv.org/abs/2603.03233)
- [Applying an Agentic Coding Tool for Improving Published Algorithm Implementations — arXiv:2604.13109](https://arxiv.org/abs/2604.13109)
- [AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges — arXiv:2505.10468](https://arxiv.org/pdf/2505.10468)
- [Low-code development and model-driven engineering: Two sides of the same coin? — SoSyM](https://dl.acm.org/doi/10.1007/s10270-021-00970-2)
- [On the use of large language models in model-driven engineering — SoSyM](https://dl.acm.org/doi/abs/10.1007/s10270-025-01263-8)
- [Turning Low-Code Development Platforms into True No-Code with LLMs — MODELS 2024, ACM/IEEE](https://dl.acm.org/doi/10.1145/3652620.3688334)
- [Large language models in model-driven engineering: a systematic mapping study — Empirical Software Engineering, Springer](https://link.springer.com/article/10.1007/s10664-026-10921-4)
- [A Survey on Large Language Models for Software Engineering (AwesomeLLM4SE) — GitHub](https://github.com/iSEngLab/AwesomeLLM4SE)

---

## Appendix: Governing Agentic AI in Enterprise ERP Development — an Applied Framework

*This appendix consolidates a follow-on design discussion applying the report's themes to a concrete case: using agentic AI (e.g., Claude Code) inside a traditional ERP environment. It's derived from applied architecture reasoning, not external sourcing, and is organized as a reusable governance checklist.*

### A.1 First, decide which of two things you're building

This is the single most important design decision — the two paths carry almost entirely different risk profiles:

- **(a) Agentic AI-assisted ERP development.** A coding agent (e.g., Claude Code) helps write or modify the ERP codebase. A human reviews the diff. A traditional SDLC (version control, CI/CD, tests) ships it. The agent never touches live production data or executes live business transactions.
- **(b) Agentic AI as a runtime actor inside the ERP.** An autonomous agent operates against live production data — initiating or approving real transactions (posting journal entries, releasing payments, creating master data) with limited human supervision.

Conflating the two is costly in both directions: it either under-governs a live financial-transaction agent, or over-builds runtime controls (kill switches, transaction dry-runs, live monitoring) for what is really just an AI-assisted coding workflow. Most organizations adopting agentic AI in 2026 start with (a). (b) is a materially higher-risk undertaking and deserves its own governance program.

### A.2 Checklist for (b) — agentic AI acting at runtime on live ERP data

Beyond a workflow engine, an API framework, and API/workflow governance, an agent that autonomously executes or approves real transactions needs:

1. **Semantic/context layer**
   A canonical business object model (Vendor, PO, GL Account, Cost Center) the agent reasons over — not raw tables.
2. **Identity and permission propagation**
   The agent acts *as* a specific identity, carrying that identity's real RBAC/segregation-of-duties (SoD) constraints — not just API-scope auth.
3. **A deterministic policy/business-rules engine, separate from the agent**
   Validates every proposed transaction (budget limits, tax rules, three-way match) before commit. The agent proposes; it never has the final word on material transactions.
4. **Human approval gates**
   On high-value or irreversible actions, flagged distinctly for agent-initiated vs. human-initiated transactions.
5. **Transaction safety**
   Idempotency keys and saga/compensating-transaction patterns — agents retry, and can fail mid-sequence.
6. **Sandbox/dry-run capability**
   The agent can simulate a specific transaction against a staging replica before executing it live.
7. **Audit trail with reasoning, not just action logs**
   Model/version used, tools and data consulted, and rationale — retrievable per transaction.
8. **Stricter master-data governance**
   Agent-created vendors or GL accounts get mandatory dual-control review, tighter than ordinary transactional governance.
9. **Runaway/cost circuit breakers**
   Step limits, timeouts, spend caps per agent session.
10. **Change management/versioning**
    For agent-authored workflows and configs, using the same promotion pipeline as any ERP customization.
11. **A kill switch and live monitoring dashboard**
    Real-time visibility and an immediate pause/revoke control — distinct from after-the-fact audit logs.
12. **A behavioral eval/regression harness**
    Run before every model or prompt update, including adversarial scenarios (SoD-bypass attempts, malformed data) — not just happy-path tests.
13. **Runtime PII/sensitive-data handling**
    Masking before data reaches the model's context — especially for HR/payroll modules.

### A.3 Checklist for (a) — agentic AI-assisted development, human-reviewed, traditionally shipped

This is the lower-risk, more common starting point. But standard SDLC tooling — version control, CI/CD, TDD/BDD — does **not** automatically cover it. The gaps specific to using an AI coding agent:

1. **Scoping and sandboxing the agent**
   Isolated dev environment/ephemeral worktrees, no production credentials or secrets in context, no direct push to protected branches or deploy triggers. An explicit autonomy policy defines which actions run unattended vs. require human approval mid-session.
2. **Provenance tagging and risk-calibrated review**
   AI-authored commits are distinctly flagged. Changes to financially material logic (GL posting, tax calc, approval routing) get mandatory senior/domain review, *enforced* — e.g., CODEOWNERS rules — not just logged.
3. **Business-rule specification as an authoritative, versioned artifact, with domain-expert sign-off**
   The agent must be grounded in finance/controller-authored rules, not engineer guesses. A domain expert — not just an engineer — signs off that AI-generated logic is *correct*, not merely tested. This is the gap most likely to persist even in a mature setup, because tests only prove correctness on the cases someone thought to write.
4. **IP and data protection, with an explicit model-hosting decision**
   The agent's context must never include real production data, secrets, or PII used as "sample data." Separately: resolve explicitly whether the model is reached via a private-network connection to a cloud-hosted service (with a no-training/data-handling agreement) or is genuinely self-hosted on-prem. "Everything is on the intranet" does not by itself answer this — the model call has to go *somewhere*, and that boundary crossing, if any, should be its own governed, documented decision.
5. **A session-level audit trail with defined content and tamper-evidence**
   Captures session/prompt content, files read, commands executed, and model version — linked to the resulting commit, and stored append-only/access-controlled so it holds up as audit evidence, not just a boolean "AI-assisted: yes/no" flag.
6. **Requirement traceability, ideally tool-native**
   Requirements, BDD scenarios, and commits chained together (e.g., GitLab Epics → Issues → MRs → commits), so "why does this code exist" is reconstructable.
7. **Named, versioned sign-off per requirement**
   Distinct from *coordination*: a stakeholder-coordination process (e.g., a PM looping in all stakeholder groups) proves participation, not approval. Each requirement/BDD scenario version should carry an explicit, named approval from the relevant stakeholder (finance, compliance, security), enforced via required reviewers/approval rules — not inferred from process involvement.
8. **Full stakeholder coverage, including compliance/audit — not business alone**
   Functional requirements from business/finance stakeholders describe desired behavior. SoD, security, and regulatory constraints often belong to a separate stakeholder class — compliance, internal audit, security — and won't appear in the requirements pipeline unless explicitly routed there.
9. **Adapting TDD/BDD for a non-deterministic agent**
   "Same input → same output" doesn't hold for an LLM-driven agent the way it does for hand-written code, so extend the practice with:
   - Property/invariant tests (e.g., debits always equal credits, no duplicate payment IDs), in addition to example-based Given/When/Then scenarios.
   - Statistical pass rates across repeated/varied runs, not a single pass/fail.
   - Adversarial/red-team scenarios as a distinct authored category, separate from expected-behavior BDD.
   - Prompts and tool descriptions versioned and regression-tested like code, since they can change behavior as much as a code diff.
   - Continuous production evals on a schedule, since a suite passing at merge time can silently drift after a model version update.
10. **Access control over who can invoke the agent on sensitive paths**
    With periodic entitlement review — separate from ordinary repository access control.
11. **Model/tool version pinning and change control**
    Treat a model update like a compiler/toolchain upgrade: tested before adoption, never rolled forward silently.
12. **A regulatory traceability matrix**
    Explicit mapping from each control (SoD enforcement, approval gate, three-way match) to the test(s) verifying it, with retained historical evidence — "green in CI today" isn't sufficient proof for a prior audit period.
13. **An incident response runbook specific to AI-assisted mistakes**
    Detection, rollback, and disclosure process for the specific failure mode of "plausible-looking but subtly wrong AI-generated business logic" — different in cause and downstream (financial-reporting) consequence from a typical software bug.
14. **Vendor/tool risk management**
    Standard third-party risk assessment — data residency, certifications, incident history — applied to the coding agent itself, given its broad codebase access.

### A.4 Worked example: mapping a real stack against the framework

Stack used in this discussion: self-hosted GitLab + DevSecOps + TDD/BDD + an audit-trail requirement + intranet-scoped infrastructure + GitLab-managed, PM-coordinated stakeholder requirements.

| A.3 item | Status | Note |
|---|---|---|
| 1. Scoping/sandboxing | Strengthened by intranet + DevSecOps | Still needs an explicit autonomy policy document |
| 2. Provenance & calibrated review | Partial | Needs enforcement (CODEOWNERS-style), not just audit logging |
| 3. Business-rule spec & domain sign-off | Strong | Stakeholder-authored requirements feed BDD directly |
| 4. IP/data protection & model hosting | Open | Intranet scoping doesn't resolve where the model itself runs |
| 5. Session audit trail, tamper-evident | Partial | "Audit trail requirement" needs a defined content spec + integrity protection |
| 6. Requirement traceability | Closed | Native GitLab Epic → Issue → MR → commit chain |
| 7. Named, versioned sign-off | Open | Coordination ≠ recorded per-version approval |
| 8. Full stakeholder coverage | Likely closed | Confirm compliance/audit are included, not just business/finance |
| 9. TDD/BDD adapted for non-determinism | Partial | Standard BDD in place; property-based/adversarial/statistical testing likely still to add |
| 10. Access control on agent invocation | Open | Not addressed by intranet or repo access alone |
| 11. Model/tool version pinning | Open | Not yet discussed |
| 12. Regulatory traceability matrix | Open | Not yet discussed |
| 13. Incident response runbook | Open | Not yet discussed |
| 14. Vendor/tool risk management | Open | Not yet discussed |

The two items that proved hardest to close through process or tooling alone: **#3/#7** — a domain expert must still read AI-generated logic on sensitive modules, and their approval must be recorded per-version, not just inferred from coordination — and **#4** — network scoping doesn't answer the model-hosting question; that requires an explicit architectural decision.

### A.5 Key takeaway for this appendix

For agentic AI-*assisted* (not autonomous-runtime) ERP development, a mature DevSecOps/GitLab/TDD-BDD foundation closes most of the mechanical governance surface: traceability, deployment control, code review workflow. What it does **not** close automatically are the two things that are inherently about **judgment, not process**:

1. Whether a domain expert has actually verified the business correctness of AI-generated logic — not just its test-passing behavior.
2. Whether that verification is captured as a named, versioned, auditable approval — rather than assumed from good coordination.

Both are worth deliberately engineering into the pipeline, rather than left as an emergent property of "stakeholders are involved."
