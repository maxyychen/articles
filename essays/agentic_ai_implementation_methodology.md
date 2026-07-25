# Implementing Agentic AI into Business Workflows: A Methodology Report

*A synthesis of academic research, consulting frameworks, vendor reference architectures, and real-world case studies, with a recommended systematic approach for enterprise implementation.*

---

## Executive Summary

There is no single, universally-adopted "standard" methodology for implementing agentic AI in business workflows — the field is too new (the core enabling papers are from 2022–2024, and most enterprise frameworks were published in 2025–2026). But there **is** convergence. Independently, academic researchers, the "big four/five" consultancies, analyst firms (Gartner, Forrester, IDC), and every major platform vendor (Microsoft, Google, AWS, Salesforce, IBM, SAP, ServiceNow) have arrived at strikingly similar structures:

1. **Assess readiness before building** — process-level, technical, and organizational.
2. **Pick workflows, not jobs** — target end-to-end, cross-system, judgment-heavy processes, not isolated tasks.
3. **Build governance in before scaling, not after** — identity, autonomy tiers, and kill-switches are day-one requirements, not retrofits.
4. **Stage the rollout by autonomy level** — sandbox → shadow → limited production → scaled autonomy, expanding oversight as stakes rise.
5. **Treat evaluation as continuous, not a pre-launch gate** — because agent behavior is non-deterministic and drifts.
6. **Measure outcomes, not usage** — task success rate, escalation rate, cost-per-action, not adoption counts.

The evidence for why this discipline matters is stark: MIT's 2025 *State of AI in Business* report found **~95% of generative AI pilots fail to deliver measurable business impact**, and S&P Global found **42% of companies abandoned most AI initiatives in 2025** (up from 17% in 2024). The organizations that succeed — JPMorgan Chase, Wilson Sonsini, Unilever — share a common trait: they treated implementation as a *process redesign discipline* with staged autonomy and governance, not a software rollout.

This report synthesizes ~50 sources across academic literature, consulting/analyst frameworks, technical architecture documentation, and case studies into one recommended methodology, with the full evidence base underneath it.

---

## 1. What "Agentic AI" Actually Means

Before a methodology can be designed, the target needs a precise definition — "agentic AI" is used loosely enough in industry writing that it blurs into RPA and chatbots.

The clearest academic distinction comes from Sapkota, Roumeliotis & Karkee (2025), *"AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges"* ([arXiv:2505.10468](https://arxiv.org/abs/2505.10468)):

- **AI Agents**: modular, LLM-driven, task-specific systems that use tools and prompting to automate a bounded task.
- **Agentic AI**: multi-agent collaboration, dynamic task decomposition, persistent memory, and *coordinated* autonomy across a workflow — not a single task.

Laakmann, Ciftci & Janiesch (BPM Forum 2024, [arXiv:2509.15730](https://arxiv.org/abs/2509.15730)) provide a complementary taxonomy for where ML-enhanced RPA ends and true agentic behavior begins, across eight dimensions (architecture, capabilities, data basis, intelligence level, integration depth, deployment environment, lifecycle phase, user-robot relation) — useful for scoring how "agentic" a candidate workflow solution actually is before you claim the label.

**Practical takeaway for a methodology:** the old automation model scripted every step in advance and escalated only scripted exceptions. Agentic AI inverts this — agents sense, reason, and act on their own, escalating to a human only when stakes are high, confidence is low, the case is novel, or a regulation requires sign-off. A methodology has to be designed around *that* inversion, not around deploying "a slightly smarter bot."

---

## 2. Why Discipline Matters: The Failure-Rate Evidence

- MIT's 2025 *State of AI in Business* report: ~95% of generative AI pilots fail to deliver measurable business impact.
- S&P Global Market Intelligence (2025 survey): 42% of companies abandoned most AI initiatives in 2025 (up from 17% in 2024); the average organization scrapped 46% of AI proofs-of-concept before production.
- McKinsey's own diagnosis (the "Gen AI paradox," [Seizing the Agentic AI Advantage](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage), 2025): most deployments failed to move earnings because they were horizontal tools (chatbots, copilots) bolted onto existing workflows, rather than agents with the workflow redesigned around them.
- Google Cloud's blueprint names three recurring failure modes: building agents on unresolved technical debt, uncontrolled "agent sprawl" from siloed deployments, and "automating the past" — using agents for incremental efficiency instead of redesigning the workflow.

This is the empirical case for *why* a systematic methodology — not ad hoc pilots — is the right unit of investment.

---

## 3. Survey of Existing Systematic Approaches

No org "owns" the definitive methodology, but four convergent traditions exist. Understanding all four lets you borrow the strongest part of each.

### 3.1 Academic / Research Frameworks

| Framework | Source | Core Idea |
|---|---|---|
| **Agentic AI Readiness (process-oriented)** | Schmidt, Alt & Zimmermann, HICSS 2026 ([link](https://scholarspace.manoa.hawaii.edu/items/174fe069-9545-4445-96ef-9cf693bd87ea)) | Dual assessment: (a) potential readiness across five BPM-native perspectives — activities, decisions, data operations, control flow, resource management; (b) "process debt" — the gap between documented and actual practice. Validated on 40+ stakeholders across 9 processes. |
| **Governance Maturity Model (AAGMM)** | Acharya, 2026 ([arXiv:2604.16338](https://arxiv.org/abs/2604.16338)) | Five-level, 12-domain governance maturity model anchored to NIST AI RMF and ISO/IEC 42001, validated via 750 simulation runs across five enterprise scenarios. Names five concrete "agent sprawl" failure patterns: shadow agents, orphaned agents, permission creep, functional duplication, unmonitored delegation chains. |
| **EDDOps (Evaluation-Driven Development & Operations)** | Xia et al., CSIRO Data61 ([arXiv:2411.13768](https://arxiv.org/abs/2411.13768)) | Embeds evaluation as a *continuous* governing function across the whole agent lifecycle, not a pre-deployment checkpoint — offline dev-time and online runtime evaluation in one feedback loop. |
| **Evidence-synthesis / ODTA framework** | Koch & Wellbrock, 2026 ([arXiv:2604.19818](https://arxiv.org/abs/2604.19818)) | Names the "governance-to-action closure gap" — evaluation says what's *good*, governance says what's *permissible*, but neither shows how obligations become verifiable actions. Proposes an ODTA test (Observability, Decidability, Timeliness, Attestability) for state-changing agent actions. |
| **Agentic BPM (A-BPMS)** | Dumas, Milani & Chapela-Campa, 2026 ([arXiv:2601.18833](https://arxiv.org/abs/2601.18833)) | Reframes BPM platforms so agents *sense* process state via process mining, *reason* about improvement opportunities, and *act* autonomously — a continuum from human-driven to fully autonomous processes. |
| **Agentic BPM Manifesto** | Calvanese, Casciani, De Giacomo, Dumas, Fournier, Kampik, et al. (18 authors across multiple European universities and IBM Research), 2026 ([arXiv:2603.18916](https://arxiv.org/abs/2603.18916)) | Four required capabilities for agentic BPM: framed autonomy, explainability, conversational actionability, self-modification. |
| **Practitioner governance study** | Vu, Klievtsova, Leopold, Rinderle-Ma, Kampik, 2025 ([arXiv:2504.03693](https://arxiv.org/abs/2504.03693)) | 22 BPM-practitioner interviews. Benefits: efficiency, data quality, compliance, scalability. Concerns: bias, over-reliance, security, job displacement, ambiguous decision authority. Six governance recommendations: clear objectives, legal/ethical safeguards, human-agent collaboration design, customization, risk management, fallback mechanisms. |
| **Agent autonomy measurement via code inspection** | Cihon, Stein, Bansal, Manning, Xu, 2025 ([arXiv:2502.15212](https://arxiv.org/abs/2502.15212)) | Scores agent autonomy via static inspection of orchestration code (demonstrated on Microsoft AutoGen) along "impact" and "oversight" dimensions — a cheaper, auditable alternative to runtime-only testing. |

**Foundational orchestration-pattern papers** (the technical DNA underneath every framework above): ReAct (Yao et al., ICLR 2023, [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)) — reason/act/observe loop; Reflexion (Shinn et al., NeurIPS 2023, [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)) — verbal self-critique via episodic memory; Generative Agents (Park et al., UIST 2023, [arXiv:2304.03442](https://arxiv.org/abs/2304.03442)) — memory-stream + reflection + planning; Toolformer (Schick et al., NeurIPS 2023, [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)) — self-supervised tool use; HuggingGPT (Shen et al., NeurIPS 2023, [arXiv:2303.17580](https://arxiv.org/abs/2303.17580)) — controller/planner-executor with specialist workers; MegaAgent (Wang et al., ACL 2025 Findings, [arXiv:2408.09955](https://arxiv.org/abs/2408.09955)) — hierarchical multi-agent systems at scale without hand-written SOPs.

**Evaluation and failure-mode research:** AgentBench (Liu et al., ICLR 2024, [arXiv:2308.03688](https://arxiv.org/abs/2308.03688)) found that poor long-horizon reasoning and instruction-following — not raw model capability — are the dominant bottleneck in agent performance, a finding directly relevant to setting realistic enterprise expectations. AgentErrorTaxonomy (Zhu et al., 2025, [arXiv:2509.25370](https://arxiv.org/abs/2509.25370)) categorizes agent failures across memory, reflection, planning, action, and system operations — a ready-made checklist for a post-incident review process.

### 3.2 Consulting & Analyst Frameworks

| Firm | Framework | Structure |
|---|---|---|
| **McKinsey** | "Seizing the Agentic AI Advantage" ([source](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage), 2025) | Diagnoses a "Gen AI paradox" (~80% of companies use gen AI; ~80%+ report no material earnings impact) and proposes: three CEO-level actions (conclude experimentation & realign priorities; redesign AI governance & the operating model; launch a "lighthouse" transformation project), organized around four transformation dimensions (Strategy, Unit of transformation, Delivery model, Implementation process) and four critical enablers (People, Governance, Technology architecture, Data). |
| **BCG** | "Machines That Manage Themselves" ([source](https://www.bcg.com/publications/2025/machines-that-manage-themselves), 2025) | Frames adoption around four strategic tensions leaders must resolve — scalability vs. adaptability, investment vs. employment, supervision vs. autonomy, and process retrofitting vs. reimagining — followed by five practical implementation steps. *(Note: some secondary sources attribute a distinct "Agentic Operating Model" — Delegation Charters, AgentOps Pods, Outcome Metrics — to BCG; that terminology in fact comes from an unrelated Forbes Technology Council contributor piece, not this BCG report, and is not reproduced here.)* |
| **Deloitte** | Tech Trends 2026: "Agentic AI Strategy" ([source](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html), 2025) | Argues for targeting end-to-end, multi-system, high-volume processes rather than single pain points — captured in a quote from Deloitte's Brent Collins: "don't pave the cow path." A separate Deloitte survey-based piece ("AI Maturity and Digital Value," 2025 Tech Value Survey) segments organizations into "Automators" (single-agent workflows, foundational stage) and "Transformers" (multi-agent, organization-wide reimagination). |
| **Bain** | Two distinct reports: ["Building the Foundation for Agentic AI"](https://www.bain.com/insights/building-the-foundation-for-agentic-ai-technology-report-2025/) (2025) and ["From Roadmap to Reality"](https://www.bain.com/insights/from-roadmap-to-reality-phasing-agentic-ai-into-production/) (2026) | The Foundation report proposes "four motions": focus on a few business domains; assess architectural readiness for agentic AI; define observability/governance/controls; use agentic AI itself to reduce the cost of the transformation. The separate Roadmap-to-Reality report proposes a three-phase scaling sequence: Phase 1 (Build the Foundation — governance, security, single-agent pilots) → Phase 2 (Deploy Orchestration — multi-step workflows, agent-to-agent protocols) → Phase 3 (Scale Across the Enterprise — federated discovery/routing). Both target complex, nondeterministic, cross-system processes that have historically required human judgment. |
| **PwC** | Agent Powered Performance / Sense-Think-Act ([source](https://www.pwc.com/us/en/services/consulting/business-transformation/agent-powered-performance.html), 2025) | Works backward from target KPIs, then aligns tech/process/operating model. Agents run a continuous Sense (monitor) → Think (reason against benchmarks) → Act (execute corrective action) loop. |
| **Gartner** | Hype Cycle positioning ([source](https://www.gartner.com/en/newsroom/press-releases/2025-08-05-gartner-hype-cycle-identifies-top-ai-innovations-in-2025), 2025) | Agents at "Peak of Inflated Expectations"; mainstream adoption 5–10 years out. Implicit guidance: favor narrowly-scoped, well-bounded use cases over broad autonomy while pre-Trough. |
| **Forrester** | AEGIS Framework ([source](https://www.forrester.com/technology/aegis-framework/)) | Security/governance-first sequencing: 0–3mo governance foundation → 3–6mo IAM + data security → 6–12mo agent-lifecycle traceability → 12mo+ Zero Trust maturity. |
| **IDC** | AI-Fueled Organization Maturity Model + CoE guidance ([source](https://my.idc.com/getdoc.jsp?containerId=US53564125)) | No single CoE model fits all maturity stages — governance structure should evolve as an org moves from pilot to scaled deployment. |

### 3.3 Vendor / Platform Reference Architectures

| Vendor | Framework | Notable Structure |
|---|---|---|
| **Microsoft** | Agentic AI Adoption Maturity Model ([source](https://learn.microsoft.com/en-us/agents/adoption-maturity-model/)) | Explicit CMM adaptation: 5 levels (100-Initial → 500-Efficient) × 5 pillars (AI strategy, business strategy, governance & security, tech & data, org & culture) = a 5×5 grid. Prioritization rule: fix your *lowest-scoring pillar*, not just the highest-ROI workflow. |
| **Google Cloud** | Enterprise-wide agentic transformation blueprint ([source](https://hbr.org/sponsored/2026/02/a-blueprint-for-enterprise-wide-agentic-ai-transformation), 2026) | Anchor deployments in P&L-measurable outcomes; design for human-agent collaboration, not pure automation; treat early use cases as reusable components of a broader agent ecosystem. |
| **Bain / AWS** | Well-Architected Agentic AI Lens ([source](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html)) | Maturity path: first agent (scope, least-privilege identity) → production (tracing, LLM-as-judge eval, cost controls) → multi-agent scale (arbiter/fallback patterns) → hardening (guardrails, HITL, rogue-agent detection). |
| **Salesforce** | Enterprise Agentic Architecture ([source](https://architect.salesforce.com/fundamentals/enterprise-agentic-architecture)) | Start with monolithic (single) agents; move to multi-agent only as complexity/scale genuinely demands it — an explicit "don't over-engineer early" principle. |
| **IBM** | Agent Development Lifecycle (ADLC) ([source](https://www.ibm.com/think/tutorials/build-production-ready-ai-agent-with-watsonx-orchestrate)) | Treats agents as continuously evolving, probabilistic systems managed through design → develop → deploy → continuously improve, not one-time releases. |

**A pattern worth naming explicitly:** every serious framework above — academic, consulting, and vendor — independently converges on *staged autonomy expansion* (narrow pilot → shadow/limited production → scaled autonomy) and *governance-before-scale*. That convergence is the strongest evidence for the methodology recommended in Section 4.

---

## 4. Recommended Methodology

Synthesizing the strongest, most concrete elements of the frameworks above into one sequence. This is not any single firm's framework — it's the common spine underneath all of them, adapted to be tool-agnostic.

### Phase 0 — Readiness Assessment
Run a dual assessment before touching any workflow (per Schmidt/Alt/Zimmermann and Microsoft's maturity grid):
- **Process readiness**: For each candidate workflow, score across activities, decisions, data operations, control flow, and resource management. Identify "process debt" — where documented process diverges from actual practice (agents inherit whatever the *actual* process is, warts included).
- **Technical readiness**: Data quality/accessibility, integration architecture (do candidate systems expose APIs or only UIs?), existing identity/access infrastructure.
- **Organizational readiness**: Is there executive sponsorship, a governance owner, and a change-management plan, or is this a shadow-IT pilot waiting to be shut down?

### Phase 1 — Workflow Discovery & Prioritization
Reject the "which jobs get automated" framing. A job is a bundle of workflows; agentic AI goes after the workflow, not the job title.

- Use process mining (e.g., Celonis-style event-log analysis, or manual process discovery workshops) to build a ranked, ROI-scored list of candidate workflows — not a workshop guess.
- Prioritize workflows that are: end-to-end and cross-system (not single-task), high-volume, judgment-heavy/nondeterministic, and currently reliant on unstructured data or tribal knowledge. Avoid "pave the cow path" — automating a single narrow step of an otherwise unchanged process rarely moves the P&L (Deloitte, Google Cloud both name this failure mode independently).
- Favor a small number of high-value, vertical, function-specific use cases over a horizontal capability rollout (chatbots/copilots layered onto every team) — McKinsey's research ties the "Gen AI paradox" (widespread adoption, little earnings impact) directly to horizontal-first deployment. Favor narrowly-scoped, well-bounded use cases while the technology is still immature (Gartner).

### Phase 2 — Governance & Architecture Foundation (before scaling)
This is the phase organizations most often skip, and the one every framework says not to skip.

- **Autonomy tiers**: Classify each agent/workflow by autonomy level (a four-tier model — supervised → conditionally autonomous → highly autonomous → full autonomy — is emerging as a common pattern across NIST-adjacent proposals). Higher tiers require more frequent re-certification.
- **Identity & least privilege**: Treat each agent as a managed identity with scoped, short-lived credentials — not a shared service account. Separate "read" agents from "write" agents (see [[ai_agent_governance]] in this same folder for the personnel-security analogy this report's companion essay develops).
- **Accountability**: Name a human business owner who accepts risk for each agent *before* deployment — not the AI team, who only builds it.
- **Observability**: Instrument tracing (every LLM call, tool invocation, reasoning step) from day one, not after an incident. This is what lets Phase 3's evaluation loop function at all.
- **Kill-switch**: Can you cut an agent's access in minutes? If not, don't deploy it.

### Phase 3 — Staged Rollout by Autonomy
The single most consistent pattern across every source in this report — academic, consulting, vendor, and case study alike:

**Sandbox → Shadow mode → Limited production → Scaled autonomy**

- *Sandbox*: agent runs against test/synthetic data only.
- *Shadow*: agent runs in parallel with the existing human/process, its outputs logged but not acted on — used to measure accuracy against ground truth before it touches anything real.
- *Limited production*: agent acts, but only within a narrow segment (one client tier, one geography, one case type) with human sign-off on consequential actions. Citigroup's "Citi Sky" (Citigold clients first, US only) and the BigLaw pattern (Wilson Sonsini, A&O Shearman, Troutman Pepper: low-risk non-client-facing work first) are concrete examples.
- *Scaled autonomy*: expand scope only after the prior stage's evaluation metrics clear a defined bar, and only as far as the governance tier for that workflow permits.

Klarna's reversal (full-scale rollout in Feb 2024 that later had to reintroduce human agents for complex cases due to CSAT drops) is the cautionary counter-example: it skipped the shadow/limited-production validation step for its highest-complexity case tier.

### Phase 4 — Multi-Agent Orchestration at Scale
Once single-agent workflows are proven, move to orchestration across agents — but only when complexity genuinely demands it (Salesforce's "don't over-engineer early" principle). At this stage:
- Standardize on interoperability protocols: **MCP** (Model Context Protocol — agent-to-tool/data) and **A2A** (Agent2Agent — agent-to-agent, now Linux Foundation-governed) are the emerging cross-vendor standard pair; nearly every 2025–2026 enterprise reference architecture (AWS, Google, Salesforce) assumes both.
- Choose an orchestration topology deliberately: supervisor/planner-executor (a router delegating to specialist workers) vs. handoff-based (ownership transfers cleanly between specialists, good for conversational/triage use cases) vs. event-driven step graphs (good for RAG-heavy knowledge work). See Section 5 for the pattern-to-framework mapping.
- Federated discovery/routing (the language Bain uses for its "Scale Across the Enterprise" phase in *From Roadmap to Reality*) becomes necessary once agents need to find and delegate to other agents across domain boundaries.

### Phase 5 — Continuous Evaluation & Governance (ongoing, not a gate)
Per the EDDOps model (Xia et al.): evaluation is a continuous function across the whole lifecycle, combining offline dev-time testing with online runtime monitoring — not a one-time pre-launch checkpoint. This phase runs in parallel with all prior phases once any agent is live, and never actually ends.

---

## 5. Technical Architecture Patterns

For the solutions-architect audience, mapping orchestration patterns to concrete frameworks:

| Pattern | Best suited for | Representative frameworks |
|---|---|---|
| Simple tool-use loop (ReAct-style) | Bounded, single-agent tasks with verifiable progress | OpenAI Agents SDK, Anthropic's five composable workflow patterns |
| Planner-executor | Heterogeneous specialist sub-tasks under one controller | HuggingGPT-style controllers, Semantic Kernel planners |
| Supervisor / router-to-workers | Complex workflows needing durable, resumable state and fine-grained branching | LangGraph (graph-based state machine, Pregel-inspired) |
| Handoff-based | Conversational, routing-heavy tasks (e.g., support triage) where task ownership should transfer cleanly | OpenAI Agents SDK handoffs |
| Conversation-centric multi-agent | Research/prototyping, natural-language agent-to-agent negotiation | AutoGen (now merging into Microsoft Agent Framework) |
| Event-driven step graph | Knowledge-work automation wrapped around retrieval (contract review, claims processing) | LlamaIndex Agent Workflows |
| Hierarchical multi-agent at scale | Large agent fleets, dynamic task splitting without hand-written SOPs | MegaAgent (research), Google ADK's 8 documented multi-agent patterns |

**Anthropic's own framing** (["Building Effective Agents"](https://www.anthropic.com/engineering/building-effective-agents), Dec 2024) is worth internalizing directly: distinguish *workflows* (LLMs + tools composed through predefined, deterministic code paths) from *agents* (LLMs that dynamically direct their own tool use and control flow). Start with the simplest pattern that passes evals; invest in the "agent-computer interface" (tool docs/schemas) as heavily as human-facing UX; add autonomy only when justified by the task, not by ambition.

**Interoperability & guardrails stack:**
- **MCP** (Anthropic, Nov 2024) — standardizes agent-to-tool/data access via host-client-server architecture; explicit trust-boundary rules (user consent before tool invocation; untrusted-server tool descriptions treated as untrusted input — a documented prompt-injection surface).
- **A2A** (Google, Apr 2025; now Linux Foundation-governed) — standardizes agent-to-agent task delegation across vendor/org boundaries via Agent Cards and OAuth 2.0.
- **Observability**: LangSmith or Langfuse (the latter open-source/self-hostable, relevant for data-residency-constrained enterprises) — both support trajectory evaluation (did the agent take the *right sequence* of actions, not just produce the right final answer), which matters more for agents than for single-shot LLM calls.
- **Guardrails**: a three-layer model — input validation, output filtering, and *architectural containment* (scoped credentials limiting what an agent can physically do, not just what it's prompted not to do). The third layer is the one most enterprises under-invest in.
- **Integration with legacy/RPA**: UiPath's own positioning is instructive — agents handle ambiguous, judgment-based steps; RPA robots remain the reliable executor for high-volume, structured steps. This is a hybrid model, not "agents replace RPA."

---

## 6. Governance & Risk Management

- **NIST AI RMF 1.0** (Govern / Map / Measure / Manage, applied iteratively) remains the base standard; NIST has not yet published an official agentic-specific profile (one is reportedly planned for Q4 2026). In the interim, the Cloud Security Alliance's *"Agentic Profile"* white paper (March 2026, industry-authored, not an official NIST document) is the most concrete gap-filler: a four-tier autonomy classification, an agent accountability register, tool-risk inventories, and behavioral telemetry (permission-escalation rate, delegation depth).
- **ISO/IEC 42001:2023** (AI Management System standard) functions as the governance "chassis" — plan-do-check-act continual improvement — onto which agent-specific controls attach.
- **EU AI Act**: Article 12 (record-keeping — harder for agents since decisions may not trace to discrete human-reviewable inputs), Article 13 (transparency for consequential autonomous decisions), Article 14 (human oversight — with a documented tension: oversight effectiveness degrades as agent autonomy/complexity increases), Article 15 (robustness). High-risk obligations for regulated-sector agentic systems phase in from August 2, 2026.
- **RACI for agents**: name exactly one Accountable human per agent/governance function; Responsible roles checked against operational reality, not just documentation. Multiple sources (Cyberhaven) candidly note most current vendor governance content stops short of a real RACI matrix in practice — this remains an implementation gap, not a solved problem.
- **Companion essay in this repo**: [[ai_agent_governance]] develops the "treat your agent like a new hire" framing (segregation of duties, least privilege, need-to-know, lifecycle management, pre-deployment evaluation, prompt-injection defense) that operationalizes several of the points above.

---

## 7. Organizational Change Management

Classic frameworks apply, but need adaptation:

- **ADKAR** (Awareness, Desire, Knowledge, Ability, Reinforcement) maps well to individual-level adoption: Awareness = the business case for agent delegation; Desire = directly countering job-security fear; Reinforcement = metrics/recognition tied to *outcomes*, not usage counts.
- **Kotter's 8-step model** works for org-level, big-bang change but several practitioner sources argue its sequential urgency-building approach can conflict with iterative agentic rollouts and feel like it undermines developer/employee autonomy — better suited to Moderna-style enterprise-wide launches than to phased pilots.
- **Labor considerations are real and uneven**: 47 U.S. collective bargaining agreements signed 2023–March 2026 contain explicit AI provisions (mandatory pre-implementation bargaining, use prohibitions, no-layoff clauses) — but U.S. union density is only ~10%, so most of the workforce has no equivalent bargained protection. A responsible methodology should treat workforce communication and reskilling as a governed deliverable, not an afterthought, regardless of union status.

---

## 8. Metrics & Evaluation

Move away from usage/adoption counts toward outcome metrics:

| Category | Representative metrics |
|---|---|
| Task performance | Task success/completion rate (85%+ is cited as a production-grade bar for well-defined workflows), human escalation rate (10–15% or below at that bar) |
| Efficiency/cost | Cost per action (CPA) = total agent operating cost ÷ successful actions completed; cost per deployed agent |
| Speed | End-to-end cycle time, time-to-resolution |
| Quality/risk | Quality score, incidents per 1,000 agent runs |
| Business impact | Revenue influenced, CSAT impact — the metrics that actually justify continued investment |

A five-stage measurement discipline recurs across sources: define objectives → select metrics per category → benchmark against historical/industry baselines → continuous dashboard monitoring → iterate. Track both real-time operational dashboards (anomaly/incident detection) and weekly trend analysis (catching performance degradation before it becomes business impact) — mirroring NIST RMF's "Measure" function, which treats risk as something that changes over time, not a one-time score.

---

## 9. Case Studies: What Actually Happened

| Organization | Approach | Outcome / Lesson |
|---|---|---|
| **Klarna** | Full-scale customer-service AI rollout (Feb 2024) | 2.3M chats in 30 days at launch (workload equivalent of 700 agents, later revised to 853 by Q3 2025); $60M in savings and cost-per-transaction down from $0.32 to $0.19 reported by Q3 2025 — but partially reversed in May 2025, with CEO Sebastian Siemiatkowski citing quality/satisfaction concerns and rehiring human agents. Lesson: skipping shadow/limited-production validation for high-complexity tiers is costly. |
| **JPMorgan Chase** | Internal-first (employee productivity before customer-facing autonomy); 450+ use cases | LLM Suite to 230,000+ staff before expanding into agentic payments/treasury workflows, gated by internal governance. |
| **Citigroup ("Citi Sky")** | Segment-limited rollout: Citigold clients, US only, before broader expansion | Explicit example of staged production rollout by client tier/geography. |
| **Moderna** | Enterprise-wide deployment (not narrow pilot), parallel individual/community/structural change workstreams | Rare successful non-staged rollout — contrasted with the more common staged-pilot pattern; every department built domain-specific GPTs. |
| **Walmart** | Vertically integrated "Super Agent" layer over proprietary infrastructure, not point-solution agents per workflow | Distinct from vendor-agent-per-workflow approaches; autonomous inventory/demand-forecast adjustment. |
| **Unilever ("Sky")** | Human-defined planning cycle augmented by agent-generated forecasts, not autonomous decision authority | 98% fill rate, 12% sales growth — a contrast case where the agent augments rather than replaces judgment. |
| **BigLaw (Wilson Sonsini, A&O Shearman, Troutman Pepper)** | Staged-risk: low-risk, non-client-facing work first, then high-value/high-expertise domains | Consistent "start narrow/high-value, expand after validation" pattern across the sector. |
| **Healthcare insurer (Accelirate case)** | Claims pipeline with fraud detection and audit-ready compliance logging built in from the start | 85% improvement in claims turnaround; governance designed in at rollout, not retrofitted. |

---

## 10. Common Anti-Patterns (What to Avoid)

Drawn from convergent warnings across McKinsey, Google Cloud, Bain, and the case studies above:

1. **Automating the past** — using agents to speed up an unchanged, badly-designed process, instead of redesigning the workflow around agent capability.
2. **"Paving the cow path"** — automating one narrow step instead of an end-to-end, cross-system workflow.
3. **Skipping the shadow/limited-production stage** — going straight from pilot to full autonomy (Klarna).
4. **Building on unresolved technical debt** — agents amplify whatever mess already exists in the underlying systems and data.
5. **Agent sprawl** — deploying agents siloed by team with no central registry, leading to shadow agents, orphaned agents, permission creep, and unmonitored delegation chains.
6. **Governance as an afterthought** — bolting on identity/audit/kill-switch controls after an incident rather than designing them in during Phase 2.
7. **Measuring usage instead of outcomes** — adoption counts look good and mean nothing; task success rate, escalation rate, and cost-per-action are the metrics that matter.

---

## 11. Full Reference List

**Academic / Research**
- Sapkota, Roumeliotis & Karkee (2025). *AI Agents vs. Agentic AI: A Conceptual Taxonomy.* [arXiv:2505.10468](https://arxiv.org/abs/2505.10468)
- Laakmann, Ciftci & Janiesch (BPM Forum 2024). *A Nascent Taxonomy of ML in Intelligent RPA.* [arXiv:2509.15730](https://arxiv.org/abs/2509.15730)
- Han, Zhang, Jin & Xu (2024). *LLM Multi-Agent Systems: Challenges and Open Problems.* [arXiv:2402.03578](https://arxiv.org/abs/2402.03578)
- Schmidt, Alt & Zimmermann (HICSS 2026). *Agentic AI Readiness: A Process-Oriented Assessment Framework.* [Link](https://scholarspace.manoa.hawaii.edu/items/174fe069-9545-4445-96ef-9cf693bd87ea)
- Acharya (2026). *Governing the Agentic Enterprise: A Governance Maturity Model.* [arXiv:2604.16338](https://arxiv.org/abs/2604.16338)
- Xia, Lu, Zhu, Xing, Zhao & Zhang (CSIRO Data61, 2024/25). *Evaluation-Driven Development and Operations of LLM Agents.* [arXiv:2411.13768](https://arxiv.org/abs/2411.13768)
- Koch & Wellbrock (2026). *Beyond Task Success: An Evidence-Synthesis Framework.* [arXiv:2604.19818](https://arxiv.org/abs/2604.19818)
- Yao et al. (ICLR 2023). *ReAct: Synergizing Reasoning and Acting in Language Models.* [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- Shinn et al. (NeurIPS 2023). *Reflexion: Language Agents with Verbal Reinforcement Learning.* [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)
- Park et al. (UIST 2023). *Generative Agents: Interactive Simulacra of Human Behavior.* [arXiv:2304.03442](https://arxiv.org/abs/2304.03442)
- Schick et al. (NeurIPS 2023). *Toolformer.* [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)
- Shen et al. (NeurIPS 2023). *HuggingGPT.* [arXiv:2303.17580](https://arxiv.org/abs/2303.17580)
- Wang et al. (ACL 2025 Findings). *MegaAgent.* [arXiv:2408.09955](https://arxiv.org/abs/2408.09955)
- Huang et al. (2024). *Understanding the Planning of LLM Agents: A Survey.* [arXiv:2402.02716](https://arxiv.org/abs/2402.02716)
- Liu et al. (Tsinghua, ICLR 2024). *AgentBench: Evaluating LLMs as Agents.* [arXiv:2308.03688](https://arxiv.org/abs/2308.03688)
- Mohammadi, Li, Lo & Yip (2025). *Evaluation and Benchmarking of LLM Agents: A Survey.* [arXiv:2507.21504](https://arxiv.org/abs/2507.21504)
- Zhu et al. (2025). *Where LLM Agents Fail and How They Can Learn From Failures.* [arXiv:2509.25370](https://arxiv.org/abs/2509.25370)
- Cihon, Stein, Bansal, Manning & Xu (2025). *Measuring AI Agent Autonomy via Code Inspection.* [arXiv:2502.15212](https://arxiv.org/abs/2502.15212)
- Dumas, Milani & Chapela-Campa (2026). *Agentic Business Process Management Systems.* [arXiv:2601.18833](https://arxiv.org/abs/2601.18833)
- Calvanese et al. (2026). *Agentic Business Process Management: A Research Manifesto.* [arXiv:2603.18916](https://arxiv.org/abs/2603.18916)
- Vu, Klievtsova, Leopold, Rinderle-Ma & Kampik (2025). *Practitioner Perspectives on Agent Governance in Business Processes.* [arXiv:2504.03693](https://arxiv.org/abs/2504.03693)
- Berti, Maatallah, Jessen, Sroka & Ghannouchi (2024). *Re-Thinking Process Mining in the AI-Based Agents Era.* [arXiv:2408.07720](https://arxiv.org/abs/2408.07720)
- Huang, Lambros, Huang, Mehmood, Atta, Beck, Narajala, Baig, Ul Haq, Shahzad & Gupta (2025). *AAGATE: A NIST AI RMF-Aligned Governance Platform for Agentic AI.* [arXiv:2510.25863](https://arxiv.org/pdf/2510.25863)

**Consulting / Analyst**
- McKinsey (2025). [Seizing the Agentic AI Advantage](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage); [Reimagining Tech Infrastructure for Agentic AI](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/reimagining-tech-infrastructure-for-and-with-agentic-ai)
- BCG (2025–26). [Machines That Manage Themselves](https://www.bcg.com/publications/2025/machines-that-manage-themselves)
- Deloitte (2025–26). [Agentic AI Insights](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/articles/agentic-ai-insights.html); [Tech Trends 2026: Agentic AI Strategy](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html)
- Bain (2025–26). [Building the Foundation for Agentic AI](https://www.bain.com/insights/building-the-foundation-for-agentic-ai-technology-report-2025/); [From Roadmap to Reality](https://www.bain.com/insights/from-roadmap-to-reality-phasing-agentic-ai-into-production/)
- PwC (2025). [Agent Powered Performance](https://www.pwc.com/us/en/services/consulting/business-transformation/agent-powered-performance.html)
- Accenture (2025). [AI Refinery for Industry](https://newsroom.accenture.com/news/2025/accenture-launches-ai-refinery-for-industry-to-reinvent-processes-and-accelerate-agentic-ai-journeys)
- Gartner (2025). [Hype Cycle for AI](https://www.gartner.com/en/newsroom/press-releases/2025-08-05-gartner-hype-cycle-identifies-top-ai-innovations-in-2025)
- Forrester. [AEGIS Framework](https://www.forrester.com/technology/aegis-framework/)
- IDC (2025). [AI-Fueled Organization Maturity Model](https://my.idc.com/getdoc.jsp?containerId=US53564125); [COEs for the Era of Agentic AI](https://info.idc.com/scaling-ai-maturity-with-agentic-ai.html)

**Vendor / Technical**
- Anthropic (2024). [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents); [Model Context Protocol announcement](https://www.anthropic.com/news/model-context-protocol); [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25)
- Microsoft. [Agentic AI Adoption Maturity Model](https://learn.microsoft.com/en-us/agents/adoption-maturity-model/); [AutoGen](https://www.microsoft.com/en-us/research/publication/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation-framework/); [Semantic Kernel Agent Architecture](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-architecture); [Baseline Foundry Chat Reference Architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat)
- Google. [Agent Development Kit docs](https://google.github.io/adk-docs/); [Multi-agent patterns in ADK](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/); [Agent2Agent Protocol announcement](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/); [Multi-agent reference architecture](https://docs.cloud.google.com/architecture/multiagent-ai-system); [Enterprise transformation blueprint](https://hbr.org/sponsored/2026/02/a-blueprint-for-enterprise-wide-agentic-ai-transformation)
- AWS. [Well-Architected Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html); [Agentic AI Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/enterprise-architecture.html)
- Salesforce. [Enterprise Agentic Architecture](https://architect.salesforce.com/fundamentals/enterprise-agentic-architecture)
- ServiceNow. [AI Agent Orchestrator](https://www.servicenow.com/products/ai-agents.html)
- SAP. [Joule Studio](https://www.sap.com/products/artificial-intelligence/joule-studio.html)
- IBM. [watsonx Orchestrate / Agent Development Lifecycle](https://www.ibm.com/think/tutorials/build-production-ready-ai-agent-with-watsonx-orchestrate)
- LangChain. [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview); [LangSmith Observability](https://docs.langchain.com/langsmith/observability)
- LlamaIndex. [Workflows 1.0](https://www.llamaindex.ai/blog/announcing-workflows-1-0-a-lightweight-framework-for-agentic-systems)
- OpenAI. [Agents SDK Multi-Agent Guide](https://openai.github.io/openai-agents-python/multi_agent/)
- Langfuse. [Observability Overview](https://langfuse.com/docs/observability/overview)
- Guardrails AI. [GitHub](https://github.com/guardrails-ai/guardrails)
- UiPath. [Agentic Automation Platform](https://www.uipath.com/automation/agentic-automation)
- Celonis. [AI Process Discovery](https://www.celonis.com/blog/ai-process-discovery)

**Governance / Standards**
- NIST. [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- Cloud Security Alliance (2026). [NIST AI RMF: Agentic Profile v1](https://labs.cloudsecurityalliance.org/agentic/agentic-nist-ai-rmf-profile-v1/)
- ISO. [ISO/IEC 42001:2023](https://www.iso.org/standard/42001)
- CMS Law (2026). [Agentic AI, Risk and Compliance Under the EU AI Act](https://cms.law/en/aut/legal-updates/agentic-ai-and-the-eu-ai-act2)

**Case Studies & Context**
- Harvard Business School. *JPMorganChase: Leadership in the Age of GenAI* (faculty case)
- Murphy-Hill, Butler & Savelieva (2026). *Adoption and Impact of Command-Line AI Coding Agents: A Study of Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI.* [arXiv:2607.01418](https://arxiv.org/abs/2607.01418)
- MIT (2025). *State of AI in Business* report (95% pilot-failure figure, widely cited secondary source).
- S&P Global Market Intelligence (2025 survey). AI initiative abandonment rates.

---

## Related Essays in This Collection

- [[agentic_ai_workflow]] — the short-form thesis: agentic AI redesigns workflows, not jobs; the exception boundary is the real design question.
- [[ai_agent_governance]] — "treat your AI agent like a new hire": segregation of duties, least privilege, need-to-know, lifecycle management, and prompt-injection defense, mapped from classic personnel security.

*Compiled 2026-07-25. Sources current as of research date; given the pace of this field, revalidate vendor-specific framework names (several, e.g., AutoGen/Semantic Kernel, are actively consolidating) before citing in time-sensitive contexts.*
