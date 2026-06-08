# DSOF-1 — Realizing DevSecOps Outcomes

> **5 Questions**
> ← [Back to Index](DSOF-index.md)

---

## Primary Reference
- [CALMS Framework: Key to Successful DevOps Transformation — Sonatype](https://www.sonatype.com/blog/principle-based-devops-frameworks-calms)

---

## Official DevSecOps Definition (DSOF Exam)

From the DSOF v2.1 Glossary (DevOps Institute, 2021):
> **DevSecOps**: "A mindset that 'everyone is responsible for security' with the goal of safely distributing security decisions at speed and scale to those who hold the highest level of context without sacrificing the safety required."

This is the answer to Sample Exam Q1: *"Which BEST represents the goal of DevSecOps?"*
→ **B. Safely distribute security decisions at speed and scale**

---

## CALMS Framework

**Created by**: John Willis and Damon Edwards coined the original **CAMS** (Culture, Automation, Measurement, Sharing) at DevOpsDays Mountain View 2010. Jez Humble later added the **"L" for Lean**, producing **CALMS**. All three are credited as co-creators. (Confirmed in the DSOF v2.1 official glossary.)
**Purpose**: Assesses organizational readiness for DevOps/DevSecOps adoption and tracks transformation progress.

| Letter | Pillar | What It Means in Practice |
|---|---|---|
| C | Culture | Shared responsibility, breaking silos, management endorsement of DevOps values |
| A | Automation | Automate repetitive tasks — especially CI/CD, security scans, and testing |
| L | Lean | Eliminate waste; reduce WIP, increase visibility, reduce handoff delays |
| M | Measurement | Collect data on processes and deployments; use metrics to drive improvement |
| S | Sharing | Openness and transparency; shared tools, knowledge, and goals across teams |

---

## The Three Ways

**Origin**: Gene Kim — *The Phoenix Project* and *The DevOps Handbook*

| Way | Principle | Key Practices |
|---|---|---|
| First Way | **Flow** (Systems Thinking) | Visualize work (Kanban), limit WIP, small batch sizes, eliminate bottlenecks, no hand-off silos |
| Second Way | **Feedback** (Fast Feedback Loops) | Fail fast, shift-left QA/security, shared ownership between Dev and Ops |
| Third Way | **Continual Learning & Experimentation** | Psychological safety, daily improvement culture, share local discoveries org-wide, practice failure scenarios |

### First Way Detail
- View the entire development lifecycle as one interconnected system
- Make work visible — Kanban boards, dashboards
- Reduce work-in-progress (WIP) to reduce context-switching
- Deliver in small batches (shorter sprints) for faster feedback
- Identify and eliminate bottlenecks (environments, testing, architecture)

### Second Way Detail
- Address issues immediately when discovered — "stop the line" culture
- Integrate security and quality checks during development, not post-launch
- Reject "throw it over the wall" — Dev and Ops share responsibility for operability

### Third Way Detail
- Leadership establishes environments where mistakes and experimentation are acceptable
- Continuous refinement becomes embedded in regular workflows
- Local discoveries (e.g., incident learnings) are surfaced and shared organization-wide
- Teams practice failure scenarios (see Chaos Engineering in DSOF-8)

---

## DORA Four Key Metrics

**Source**: Nicole Forsgren, Jez Humble, Gene Kim — *Accelerate: The Science of Lean Software and DevOps* (IT Revolution Press, 2018). Based on six years of State of DevOps Report research (2013–2018) across thousands of organizations.

| Metric | Category | Measures | Elite Performance Target |
|---|---|---|---|
| Deployment Frequency | Velocity | How often code is deployed to production | On-demand (multiple times/day) |
| Lead Time for Changes | Velocity | Time from code commit to running in production | < 1 hour |
| Change Failure Rate | Stability | % of deployments causing production failures | 0–15% |
| Time to Restore Service (MTTR) | Stability | Time to recover from a production failure | < 1 hour |

### Critical DORA Findings
1. **Speed and stability are positively correlated** — high-performing teams deploy frequently AND have low failure rates. Small, frequent deployments carry less risk than large, infrequent ones.
2. **Generative culture (Westrum) predicts all four metrics** — culture is an enabler of technical performance, not separate from it.
3. **Elite performers are twice as likely to meet organizational goals** compared to low performers.

---

## Key Terms

| Term | Definition |
|---|---|
| Value Stream | End-to-end sequence of activities that delivers value from customer request to delivery |
| Business Transformation | Organization-wide shift to DevSecOps mindset, culture, and tooling |
| SRE (Site Reliability Engineering) | Google-originated practice applying software engineering to operations; uses error budgets and service-level objectives (SLOs) |
| Chaos Engineering | Deliberately injecting failures into systems to find weaknesses before real incidents occur |
| Continuous Integration (CI) | Automatically building and testing code on every commit |
| Continuous Delivery (CD) | Every passing build is deployable to production at any time |

---

## Supporting References

- [The Three Ways of DevOps — Sonatype](https://www.sonatype.com/blog/principle-based-devops-frameworks-three-ways)
- [CALMS Framework — Atlassian](https://www.atlassian.com/devops/frameworks/calms-framework)
- [DORA Four Keys Metrics — Google Cloud Blog](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance)
- [What is CALMS for DevOps? — TechTarget](https://www.techtarget.com/whatis/definition/CALMS)
- [Using CALMS to Assess an Organization's DevOps — DevOps.com](https://devops.com/using-calms-to-assess-organizations-devops/)

---

## Academic Research

### Forsgren, Humble, Kim (2018) — *Accelerate*
> **Title**: *Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations*
> **Authors**: Nicole Forsgren, Jez Humble, Gene Kim
> **Publisher**: IT Revolution Press (2018)
> **Academic foundation**: Six years of State of DevOps Report research (2013–2018)

The foundational research text for DevOps performance measurement. Establishes the four DORA metrics as scientifically validated predictors of organizational performance. Demonstrates that Westrum generative culture scores statistically predict all four DORA metrics.

### Myrbakken & Colomo-Palacios (2017) — DevSecOps Multivocal Literature Review
> **Title**: "DevSecOps: A Multivocal Literature Review"
> **Authors**: Hermanns Myrbakken, Ricardo Colomo-Palacios
> **Venue**: *Software Process Improvement and Capability Determination (SPICE) Conference*, CCIS Springer (2017)
> **Free PDF**: [rcolomo.com](https://www.rcolomo.com/papers/314.pdf)

The foundational academic paper that established the formal definition of DevSecOps and proposed the Challenge–Practice–Tool–Metric model for understanding how DevSecOps integrates security into DevOps.

---

## Sample Exam Questions — Explained

### Q1 — Goal of DevSecOps
> *"Which BEST represents the goal of DevSecOps?"*
> **Answer: B — Safely distribute security decisions at speed and scale**

The DSOF glossary definition is verbatim: the goal is "safely distributing security decisions at speed and scale to those who hold the highest level of context." The critical word is **distribute** — moving security decision-making to the teams closest to the work, not centralizing it. **A** (GRC/compliance) is a tool category. **C** (automate policies) is one tactic, not the goal. **D** (embed security practices) describes *how*, not *why*.

---

### Q7 — Resilience Definition
> *"Which term represents the capability of an environment or organization to tolerate change and disturbances?"*
> **Answer: A — Resilience**

The DSOF glossary defines Resilience as "Building an environment or organization that is tolerant to change and incidents" — the question uses nearly identical language. **Flexibility, Agility, and Adaptability** describe speed of response or capacity for change, not tolerance of disturbance. This is a recall question; match the glossary language.

---

### Q13 — How Resilient Organizations Overcome Failure
> *"Which characteristic of resilient organizations makes it possible for them to overcome failure? The ability to…"*
> **Answer: D — Both A and C (recover quickly AND learn fast)**

Resilience has two complementary dimensions: operational recovery (A) restores service; organizational learning (C) prevents recurrence and builds capability. **B (prevent impact)** is a pre-failure activity — resilience is specifically about overcoming failure after it occurs, not preventing it entirely.

---

### Q18 — Safety Culture
> *"The term Safety Culture most likely refers to which of the following statements?"*
> **Answer: A — I feel free to tell my boss bad news**

Safety Culture in Westrum's model means psychological safety — the belief that surfacing problems, admitting mistakes, and sharing bad news will not result in punishment. **B** (OSHA standards) is physical safety — an entirely different domain. **C and D** both describe blame cultures, which are the *opposite* of Safety Culture.

---

### Q37 — What to AVOID When Scaling
> *"An organization wants to scale DevSecOps across the enterprise. Which practice should they AVOID?"*
> **Answer: D — Create and dictate a clear set of security policies**

Dictating policies top-down contradicts the Advice Process, the Third Way (Continual Learning), and the DevSecOps shift-left mindset. Teams whose input is excluded treat policies as compliance checkboxes rather than shared principles — recreating the siloed culture DevSecOps replaces. **A** (pre-blessed libraries), **B** (learning time), and **C** (automated fast feedback) are all correct scaling practices.

---

## Exam Traps

> **TRAP — DevSecOps goal is "distribute," not "enforce"**: The exam tests that DevSecOps distributes security decision-making *outward* to those with context (developers, ops), not inward to a central security team. Any answer describing centralized control, mandatory top-down gates, or "the security team decides" contradicts the goal.

> **TRAP — Resilience ≠ Agility**: Both describe organizational capability, but Resilience = tolerate disturbances and recover; Agility = move and respond quickly. "Tolerate, withstand, recover" → Resilience. "Respond quickly, adapt fast" → Agility.

> **TRAP — AVOID questions invert logic**: Q37 asks what to *avoid*. The trap answer (D) sounds responsible — of course you want clear security policies. The flaw is "dictate." DevSecOps policies must be co-created through the Advice Process, not handed down.

> **TRAP — CALMS "L" was added later**: CAMS (Culture, Automation, Measurement, Sharing) was coined by Willis and Edwards in 2010. Jez Humble added "L" for Lean. The official DSOF glossary credits all three. If asked who created CALMS, the full trio is correct; if asked who added the L, the answer is Humble.
