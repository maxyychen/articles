# DSOF-4 — Integrating DevSecOps Stakeholders

> **5 Questions**
> ← [Back to Index](DSOF-index.md)

---

## Primary Reference
- [DevSecOps Roles and Responsibilities — SupremeTech](https://www.supremetech.vn/devsecops-roles-and-responsibilities/)

---

## RACI Model

RACI is a responsibility assignment matrix. In DevSecOps it clarifies who owns each security activity across the delivery lifecycle.

| Letter | Role | Meaning |
|---|---|---|
| R | Responsible | Does the actual work for the activity |
| A | Accountable | Owns the outcome and signs off. **The golden rule: only ONE per activity** |
| C | Consulted | Provides expert input before decisions are made (two-way communication) |
| I | Informed | Kept up to date on progress and decisions (one-way communication) |

### Why RACI Matters in DevSecOps
When teams can see who is responsible at each pipeline stage, onboarding, exception handling, and escalation all become easier. Without RACI, security activities fall into ownership gaps — everyone assumes someone else is accountable.

---

## Typical Stakeholder Ownership

| Stakeholder | Primary Ownership |
|---|---|
| Developers | Security in the code and components they ship |
| AppSec / Security Team | Security standards, policy-as-code, threat modeling, escalation logic |
| Platform / DevOps Team | CI/CD hardening, artifact integrity, deployment controls |
| Operations / SRE | Runtime monitoring, incident response coordination, on-call |
| GRC / Compliance | Audit readiness, regulatory alignment, risk documentation |
| Business / Management | Risk appetite, security investment decisions, shared vision |

---

## Laloux's Advice Process (Exam Topic — Sample Q2)

The **Advice Process** is a Teal-organization decision-making model by Frederic Laloux. It is explicitly listed in the DSOF concept list and tested in the sample exam.

**Definition** (from DSOF v2.1 Glossary):
> "Any person making a decision must seek advice from **everyone meaningfully affected** by the decision **and people with expertise** in the matter. Advice received must be taken into consideration, though it does not have to be accepted or followed. The objective is not to form a consensus, but to inform the decision-maker so they can make the best decision possible."

**Key distinctions**:
- Gives everyone a **voice**, but not a **veto** — not even the CEO
- The bigger the decision, the wider the advice-seeking should be
- The decision-maker retains final authority but must genuinely consider all advice
- Applies in DevSecOps: security decisions are distributed to those with the most context (developers, ops), who must seek input from affected parties (security team, compliance, users)

**Sample Exam Q2**: *"According to Laloux's advice process, what must be done by any person making a decision?"*
→ **D. Both A and B** (Seek advice from an expert AND from people who will be impacted)

---

## Stakeholder Modeling

Stakeholder modeling in DevSecOps identifies all parties affected by or involved in security decisions:

- **Who** is involved: Dev, Sec, Ops, business owners, legal, end users, regulators
- **What** is at stake for each: delivery speed, compliance, user trust, legal liability
- **How** they interact: RACI assignments, shared metrics, joint retrospectives

Good stakeholder modeling prevents security from being seen as only the security team's responsibility — it establishes **shared ownership**.

---

## Key Terms

| Term | Definition |
|---|---|
| RACI | Responsible, Accountable, Consulted, Informed — responsibility assignment matrix |
| Stakeholder Modeling | Identifying all parties and their interests/risks in a DevSecOps initiative |
| Shared Vision and Objectives | Aligning security goals with business goals across all stakeholders |
| Cross-skilling | Developers learning security; security engineers learning DevOps tooling |
| GRC | Governance, Risk Management, and Compliance — org-wide framework for managing risk and regulatory obligations |
| Issue Management | Process for tracking, prioritizing, and resolving identified security issues |
| Ops Management | Operational processes for deploying, monitoring, and maintaining production systems |
| Privileged Access Management (PAM) | Extra controls and auditing for accounts with elevated system privileges |
| Identity and Access Management (IAM) | Centralized control of authentication and authorization across systems |

---

## Supporting References

- [Security Teams, Roles, and Functions — Microsoft Learn / Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/teams-roles)
- [RACI Matrix For Cybersecurity — Meegle](https://www.meegle.com/en_us/topics/raci-matrix/raci-matrix-for-cybersecurity)
- [7 Stages of the DevSecOps Model — Codefresh](https://codefresh.io/learn/devsecops/)
- [Security RACI Matrix: Who Really Owns What — CyberSierra](https://cybersierra.co/blog/security-raci-matrix-guide/)
- [Threat Modeling: RACI Model — VerSprite](https://versprite.com/blog/threat-model-raci-model/)

---

## Academic Research

### Myrbakken & Colomo-Palacios (2017) — DevSecOps Multivocal Literature Review
> **Title**: "DevSecOps: A Multivocal Literature Review"
> **Authors**: Hermanns Myrbakken, Ricardo Colomo-Palacios
> **Venue**: *SPICE Conference*, CCIS Springer (2017)
> **Free PDF**: [rcolomo.com](https://www.rcolomo.com/papers/314.pdf)

The foundational paper establishing DevSecOps as a discipline. Key stakeholder finding: *"Involving security in DevOps has been a challenge because traditional security methods have been unable to keep up with DevOps' agility and speed."* Proposed the Challenge–Practice–Tool–Metric model, which includes stakeholder integration as a core challenge category.

### Sinan et al. (2025) — Integrating Security Controls in DevSecOps
> **Title**: "Integrating Security Controls in DevSecOps: Challenges, Solutions, and Future Research Directions"
> **Journal**: *Journal of Software: Evolution and Process* (Wiley, 2025)
> **Link**: [Wiley](https://onlinelibrary.wiley.com/doi/full/10.1002/smr.70029)

A systematic literature review identifying **19 challenges** and **18 solutions** for integrating security controls across DevSecOps stakeholder groups. Covers organizational, technical, and cultural dimensions of stakeholder alignment.

### Rajapakse et al. (2022) — People Theme of DevSecOps Adoption
> **Title**: "Challenges and solutions when adopting DevSecOps: A systematic review"
> **Journal**: *Information and Software Technology*, Vol. 141 (2022)
> **Free preprint**: [arXiv:2103.08266](https://arxiv.org/abs/2103.08266)

The "People" theme (one of four major themes) specifically addresses stakeholder integration: skill gaps between Dev, Sec, and Ops roles; the need for cultural change; and organizational resistance to shared security ownership.

---

## Sample Exam Questions — Explained

### Q2 — Advice Process Requirements
> *"According to Laloux's advice process, what must be done by any person making a decision?"*
> **Answer: D — Both A and B (seek advice from an expert AND from people who will be impacted)**

The DSOF glossary definition requires both: "must seek advice from everyone meaningfully affected by the decision **and** people with expertise in the matter." Both conditions are explicitly stated — neither alone satisfies the Advice Process. **C** (consider the cost) is not part of the definition.

---

### Q8 — Reducing Dev-Sec-Ops Tensions
> *"Which approach can be used to reduce tensions between security, development and operations teams?"*
> **Answer: A — Introduce patterns over time so people become used to working in a certain way**

Gradual, incremental introduction of DevSecOps patterns allows teams to adapt and internalize new behaviors without feeling coerced. **Strict gates** (B) increase friction and reinforce silos. **Distributing conflicting tasks to non-security people** (C) sidesteps the cultural problem without solving it. A **GRC platform** (D) is a tool — it does not resolve human tension.

---

### Q24 — DevOps and Audit Concerns
> *"An organization's DevOps efforts have stalled due to audit concerns. Which DevSecOps practices can help?"*
> **Answer: D — All of the above**

Auditors need evidence that changes are authorized, executed by legitimate actors, and visible. All three practices contribute: **mapping changes to approved users** (A) provides audit trail; **M2M authentication** (B) ensures automated processes are authorized; **access logging and monitoring** (C) provides visibility. No single control is sufficient — the combination satisfies audit requirements.

---

### Q29 — Generative Culture: What Is NOT a Characteristic
> *"In the context of Westrum's research, which is NOT a characteristic of a generative culture?"*
> **Answer: B — Cooperation is difficult**

In Westrum's Generative culture, cross-functional cooperation is actively encouraged and rewarded — it is a defining characteristic. "Cooperation is difficult" describes a Bureaucratic or Pathological culture. **A** (failure = learning opportunity), **C** (new ideas welcomed), and **D** (shared responsibilities) are all confirmed Generative culture characteristics.

---

### Q35 — Alleviating Auditor Objections: What DOESN'T Help
> *"Which practice would most likely NOT alleviate auditors' objections and concerns?"*
> **Answer: B — Direct auditors to the issue management tool**

Simply pointing auditors at the engineering issue tracker does not help them understand or trust the DevOps process — it gives them a list of bugs without context, access, or training to interpret it. **Integrating auditors into the advice process** (A), **purpose-built dashboards** (C), and **real-time reporting** (D) all actively address auditors' need for transparency and visibility appropriate to their role.

---

### Q39 — DevSecOps and Business Transformation
> *"Which statement about DevSecOps and business transformation is CORRECT?"*
> **Answer: C — Security and DevOps practices help change how the business functions**

The DSOF glossary defines Business Transformation as "Changing how the business functions" — and DevSecOps does exactly that by integrating security into culture, processes, and technology across the organization. **A** (security minimizes constraints) is partially true but incomplete and frames security negatively. **B** (security plays no role) is plainly wrong. **D** (transformation = better security decisions) is too narrow.

---

## Exam Traps

> **TRAP — Advice Process gives voice, not veto**: Anyone can and must be consulted, but the decision-maker retains final authority. Even the CEO's advice is not binding on the decision-maker. An exam answer suggesting the advice process creates consensus or gives stakeholders veto power → incorrect.

> **TRAP — RACI "only one Accountable"**: The golden RACI rule is that each activity has exactly one Accountable — the person who owns the outcome and signs off. Multiple Responsible people are fine; multiple Accountable people is a governance failure. Exam questions testing RACI often probe this constraint.

> **TRAP — Auditor integration vs auditor redirection**: Auditors become allies when brought into the process (advice process, dashboards, real-time reporting). They remain adversaries when you try to redirect them to tools they don't understand. "Direct auditors to issue management" = wrong approach.

> **TRAP — Generative vs Bureaucratic culture confusion (Q29)**: "Cooperation is difficult" sounds like a barrier to DevSecOps — and it is — but it's a characteristic of Bureaucratic/Pathological culture, not Generative. Questions about what is NOT generative test whether you can identify the negative characteristics of the lower culture types.
