# DSOF-6 — Best Practices to Get Started

> **7 Questions** — Highest weight topic on the exam
> ← [Back to Index](DSOF-index.md)

---

## Primary Reference
- [Top 15 DevSecOps Best Practices — Practical DevSecOps](https://www.practical-devsecops.com/devsecops-best-practices/)

---

## The 15 Practices (all exam-eligible)

| # | Practice | Core Idea |
|---|---|---|
| 1 | Shift Left | Move security to the earliest SDLC stages — design and code, not QA |
| 2 | Adopt Automation | Automate security testing and policy enforcement in CI/CD |
| 3 | Implement Continuous Testing | Ongoing testing throughout development, not just at release |
| 4 | Prioritize Risk Management | Identify threats, implement controls, reduce incident impact |
| 5 | Integrate Security Tools | SAST, DAST, SCA scans embedded in pipelines |
| 6 | Collaborate Across Teams | Break silos between Dev, Sec, and Ops |
| 7 | Implement Secure Coding Standards | Developer-facing security guidelines |
| 8 | Enforce Access Controls | RBAC and least-privilege throughout development |
| 9 | Monitor for Threats | Real-time threat detection via logs and network traffic |
| 10 | Provide Security Training | Educate teams on risks and secure practices |
| 11 | Embrace Policy as Code | Define security policies in versioned, executable code (OPA, Sentinel) |
| 12 | Utilize Threat Modeling | Proactively identify threats before system impact (STRIDE, OCTAVE) |
| 13 | Expand Incident Response | Integrated response plans; improve MTTD, MTTC, MTTR |
| 14 | Leverage Immutable Infrastructure | Prevent configuration drift with unchangeable components |
| 15 | Enhance Security Observability | Advanced monitoring for anomaly detection |

---

## Security Champions (Exam Topic — Sample Q30)

**Security Champions** are a key best-practice mechanism for scaling security coverage across large organizations — explicitly tested in the sample exam.

**Definition**: Developers or team members who take on an additional security advocacy role within their team. They bridge the gap between centralized security teams and distributed development teams.

**Why they matter** (Sample Exam Q30 context): When a security team has only a few experts but must cover 20–30 development teams, Security Champions extend security reach at scale without requiring a large security headcount. They:
- Act as the first point of security contact within their team
- Promote secure coding practices
- Triage security issues before escalating to the central security team
- Participate in threat modeling and security reviews

**Sample Exam Q30**: *"What may be a best practice to extend his security coverage at scale?"*
→ **C. Security champions** (not Policy as Code alone, not strict approval processes)

> Note: The official answer key maps Q30 to DSOF-5 (Establishing DevSecOps Practices), though Security Champions are also a core DSOF-6 best practice.

---

## Key Terms

| Term | Definition |
|---|---|
| Shift Left | Moving security earlier in the SDLC — catch issues at design/code, not QA/deploy |
| Policy as Code | Security policies expressed as versioned, executable code enforced automatically (OPA, Sentinel) |
| Security as Code | Security configurations (firewalls, access rules) managed in version control like application code |
| Immutable Infrastructure | Infrastructure that is replaced rather than modified — prevents configuration drift |
| Supply Chain Security | SBOM generation, signed artifacts, dependency integrity verification |
| Secure Coding Standards | Developer-facing rules and guidelines for writing code without common vulnerabilities |

---

## Supporting References

- [8 Essential DevSecOps Best Practices — Wiz Academy](https://www.wiz.io/academy/application-security/devsecops-best-practices)
- [Shift Left with Security — Medium / SquareOps](https://medium.com/@nitinyadav745/shift-left-with-security-devsecops-best-practices-for-developers-fcd3cd1bfc11)
- [DevSecOps Best Practices: SDLC Integration — Veracode](https://www.veracode.com/blog/devsecops-best-practices-sdlc/)
- [DevSecOps Pipeline Best Practices — Wiz](https://www.wiz.io/academy/application-security/devsecops-pipeline-best-practices)
- [Shift-Left Security: 5 Ways to Embed Security — Cloud4C](https://www.cloud4c.com/blogs/shift-left-security-devsecops-explained)

---

## Academic Research

### Rajapakse et al. (2022) — Systematic Review of DevSecOps Adoption
> **Title**: "Challenges and solutions when adopting DevSecOps: A systematic review"
> **Authors**: Roshan N. Rajapakse, Mansooreh Zahedi, M. Ali Babar, Haifeng Shen
> **Journal**: *Information and Software Technology*, Vol. 141 (2022)
> **Free preprint**: [arXiv:2103.08266](https://arxiv.org/abs/2103.08266)

Key findings from 54 peer-reviewed studies:
- Identified **21 distinct DevSecOps adoption challenges** and **31 specific solutions**
- Classified across four themes:
  - **People**: skill gaps, culture resistance
  - **Practices**: shift-left and continuous security assessment are the two most recommended
  - **Tools**: most-discussed theme — automation tooling is the primary enabler
  - **Infrastructure**: secure, rapid deployment environments
- Critical finding: *"Achieving a suitable balance between the speed of delivery and security is a significant issue practitioners face"*
- Recommends developer-focused security tooling that is compatible with continuous delivery pipelines

### Feio et al. (2024) — Empirical Study on Continuous Security Testing
> **Title**: "An Empirical Study of DevSecOps Focused on Continuous Security Testing"
> **Conference**: *EuroS&PW 2024* (IEEE European Symposium on Security and Privacy Workshops)
> **Free PDF**: [INESC-ID](https://syssec.dpss.inesc-id.pt/papers/feio_eurospw24.pdf)

Key findings:
- Main confirmed **benefits**: shifting security left and automating security checks
- Main **challenges**: creating a security culture, lack of appropriate tooling, and shortage of security specialists
- Shift-left alone is insufficient without both tool integration and cultural change

### MDPI (2025) — Evolution of DevSecOps: Systematic Literature Review
> **Title**: "Evolution of DevSecOps and Its Influence on Application Security: A Systematic Literature Review"
> **Journal**: *Technologies*, MDPI (2025)
> **Open access**: [MDPI](https://www.mdpi.com/2227-7080/13/12/548)

Key challenges identified: operational friction adopting automation tools, skills gaps, security vs. performance tradeoffs, privacy compliance difficulties in multi-cloud environments.

### Vakhula et al. (2024) — Policy-as-Code for Role-Based Access Control
> **Title**: "Policy-as-Code for Role-Based Access Control"
> **Authors**: Vakhula, Opirskyi, Vorobets, Bobko, Kulinich
> **Venue**: *CEUR Workshop Proceedings*, Vol. 3991
> **Paper**: [CEUR PDF](https://ceur-ws.org/Vol-3991/paper11.pdf)

Key finding: Treating access control policies as executable, versioned code enables programmatic definition, testing, and enforcement — making policies auditable and maintainable like regular software artifacts.

---

## Sample Exam Questions — Explained

### Q4 — PAM for Automation Access
> *"Which type of tool can be used to limit access to production by automation, orchestration and configuration management tools?"*
> **Answer: C — Privileged access management tools**

PAM controls, audits, and time-boxes access by privileged accounts — including service accounts used by automation and orchestration tools. **Password management tools** (A) store credentials but don't gate what those credentials can access. **Configuration management tools** (B) deploy configs; they don't control access scope. **GRC** (D) is a governance/reporting platform, not an access enforcement tool.

---

### Q12 — Shift Left Example
> *"In the context of DevSecOps, which is an example of the 'shift left' principle?"*
> **Answer: A — Involve security during application design**

Design is the earliest SDLC stage — before a single line of code is written. Catching security issues at design costs a fraction of fixing them post-build. **Automate pen tests** (B) is good practice but pen tests are typically late-stage. **Threat modeling** (C) is itself a shift-left practice (it happens at design time), but it names one specific technique — option A states the overarching principle that encompasses threat modeling and all other design-phase security activity. **TDD** (D) is a quality practice, not a security shift-left example.

---

### Q16 — Incident Response Triggers
> *"Which is a trigger for the incident response process?"*
> **Answer: D — Both A and B (log data AND threat intelligence)**

Both log data (showing anomalies, failed logins, unusual patterns) and threat intelligence (external knowledge of active threats/IOCs) are valid triggers for starting incident response. **Attack response data** (C) is produced *during* incident response, not before it — it cannot trigger what hasn't started yet.

---

### Q17 — IAM Best Practice: What NOT to Do
> *"Which is NOT an IAM best practice?"*
> **Answer: B — Assign permissions directly to users**

IAM best practice is to assign permissions to **roles**, then assign users to roles (RBAC). Assigning permissions directly to individual users creates unmanageable sprawl as the org scales, makes auditing inconsistent, and violates the principle of least privilege. **A** (vault for root keys), **C** (rotate secrets), and **D** (MFA for privileged users) are all positive IAM controls.

---

### Q22 — Production Data in Testing
> *"A development team wants to replicate full original production data for tests. What conditions must be met?"*
> **Answer: C — Store the data in a fully production-secure environment**

If real production data must be used, it must be handled with the same security controls as production — same access restrictions, encryption, and audit logging. **D** (mask data *after* replication) is wrong in sequence: once the data is replicated unmasked, the exposure has already occurred. **A** (never use production data) is too absolute. **B** (backup before testing) addresses data integrity, not security.

---

### Q27 — IAM Risk Increase
> *"Which practice increases an organization's risk profile relative to IAM?"*
> **Answer: B — Storing secrets outside of vault**

Secrets stored outside a vault (hardcoded in source, plain text in config files, unencrypted environment variables) are a leading cause of credential compromise. All other options — **enabling MFA** (A), **identifying high-risk users** (C), **auditing policies** (D) — reduce IAM risk.

---

### Q32 — Emergency Response: What Is INCORRECT
> *"Which statement about Emergency Response is INCORRECT?"*
> **Answer: B — Prefers agile responses over documented plans**

Good incident response is the opposite: it relies on pre-documented plans (runbooks), assigned RACI roles, and rehearsed procedures precisely because people make worse decisions under stress. "Agile improvisation" during a live incident increases response time and error rate. **A** (selects key stakeholders), **C** (RACI matrix), and **D** (high availability) are all correct principles.

---

## Exam Traps

> **TRAP — PAM vs IAM vs Password Managers**: IAM = who can access what resources broadly. PAM = extra controls specifically for *privileged* accounts (including machine accounts used by automation). Password managers = store/retrieve credentials. When the question mentions "automation tools accessing production" → PAM.

> **TRAP — Shift Left is not just SAST**: Shift left is a *principle* (move security earlier in SDLC), not a specific tool. The earliest possible stage is *design* — before coding begins. If an exam option says "involve security at design," that is the purest example of shift left, beating out "run SAST at build time."

> **TRAP — Security Champions vs Policy as Code (Q30)**: Both scale security coverage, but differently. Policy as Code automates enforcement of rules. Security Champions scale *human judgment* — mentoring, triage, team-level security conversations. When the scenario is "one security team, 20–30 dev teams," the answer is Security Champions (the human scaling mechanism), not Policy as Code alone.

> **TRAP — "INCORRECT" questions need inverted logic**: Q32 asks which statement is INCORRECT. The trap is that "prefers agile responses over documented plans" sounds like good DevOps thinking, but it describes the wrong approach to incident response. Read "INCORRECT" questions carefully — the correct-sounding answer is often the trap.

> **TRAP — Production data masking timing**: The exam tests that masking must happen *at* or *before* replication, not after. Once sensitive data is copied to a test environment unmasked, the exposure window exists regardless of later masking.
