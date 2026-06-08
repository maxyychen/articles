# DSOF-5 — Establishing DevSecOps Practices

> **6 Questions**
> ← [Back to Index](DSOF-index.md)

---

## Primary Reference
- [SAST, SCA, DAST, IAST, RASP: What They Are and How to Automate — Eureka DevSecOps](https://www.eurekadevsecops.com/sast-sca-dast-iast-rasp-what-they-are-and-how-you-can-automate-application-security/)

---

## Security Testing Tools — Master Table

| Tool | When | Mechanism | Detect or Protect? | Notes |
|---|---|---|---|---|
| SAST | Build time | White-box; analyzes source code without running the app | Detect | 100% code coverage; high false-positive rate |
| SCA | Build time (continuous) | Checks open-source/third-party libraries against CVE databases | Detect | Generates SBOM; identifies license compliance issues |
| DAST | Runtime | Black-box; tests running application from outside (HTTP/API) | Detect | Language-independent; fewer false positives than SAST |
| IAST | Runtime | Agent instrumented inside the app; monitors during active testing | Detect | Combines SAST+DAST strengths; real-time; lower false positives; some tools include SCA capability |
| RASP | Runtime | Agent inside the app; monitors and actively blocks attacks | **Detect & Protect** | The only tool that actively blocks attacks; reduces perimeter dependency |

### Critical Distinctions
- **RASP is the only tool that both detects AND protects** (blocks). All others detect only.
- **IAST vs RASP**: Both use runtime agents inside the app. IAST detects during testing; RASP protects in production.
- **SAST vs DAST false positives**: Academic research confirms DAST produces fewer false positives than SAST because it operates with runtime context.
- **IAST = best of both**: Analyzes running app from inside with full code context — higher accuracy than SAST or DAST alone.

---

## Software Supply Chain Security (SCA + SBOM)

An SBOM (Software Bill of Materials) is a complete inventory of all components in a software artifact. SCA tools generate SBOMs automatically.

### Five Primary SBOM Application Areas
*(From O'Donoghue et al. 2024 — 40 peer-reviewed studies)*

| Application Area | Description |
|---|---|
| Vulnerability Management (45%) | Cross-reference components against CVE databases — the dominant use case |
| Transparency | Trace origins, integrity, and security of all software components |
| Component Assessment | Evaluate elements for quality, integrity, and policy compliance |
| Risk Assessment | Build dependency trees; calculate and prioritize risk scores |
| Supply Chain Integrity | Validate authenticity; detect unauthorized software infiltration |

### Key SBOM Adoption Barriers
- **Tooling inconsistency**: Trivy identified 7× more vulnerabilities than Grype in the same codebase
- **Format fragmentation**: Competing standards (SPDX, CycloneDX, SWID) create interoperability issues
- **Data privacy**: Exposed SBOMs can become "roadmaps for attackers"
- **Maintenance overhead**: Keeping SBOMs current across updates is significant operational burden
- **False positives**: High incorrect report rates undermine confidence in tooling

---

## Additional DevSecOps Practices (All Exam-Eligible)

### Identity & Access Management
| Term | Definition |
|---|---|
| IAM (Identity and Access Management) | Centralized control of who can access what resources and when |
| PAM (Privileged Access Management) | Extra controls, auditing, and time-boxing for high-privilege accounts |
| MFA (Multi-Factor Authentication) | Requiring multiple verification factors: something you know + have + are |
| RBAC (Role-Based Access Control) | Permissions assigned to roles, not individuals — simplifies management |
| SOD (Separation of Duties) | No single person can complete a sensitive task alone — reduces fraud risk |

### Monitoring & Runtime Security
| Term | Definition |
|---|---|
| SIEM | Security Information and Event Management — aggregates and correlates logs for threat detection |
| Log Management | Collecting, storing, indexing, and analyzing application and system logs |
| Telemetry | Real-time data streams from systems for monitoring and observability |
| Binary Instrumentation | Adding monitoring agents to compiled binaries at runtime — the technical basis for IAST and RASP |

### Vulnerability & Patch Lifecycle
| Term | Definition |
|---|---|
| Vulnerability Management | Full lifecycle: identify → classify → remediate → verify → report |
| Patch Management | Systematic process of applying security patches across all systems in a timely manner |
| Container Security | Image scanning, minimal base images, no hardcoded secrets, runtime protection |
| Secrets Management | Automated detection, storage, rotation of credentials, API keys, and tokens — never hardcode |

---

## Supporting References

- [DevSecOps: A Comprehensive Guide to DAST, IAST, SAST — Contrast Security](https://www.contrastsecurity.com/glossary/devsecops)
- [DevSecOps Toolchain Explained — Medium / Alfatah Jalalludin](https://al-fatah.medium.com/devsecops-toolchain-explained-sast-dast-sca-and-container-security-6e00d9bd7025)
- [SCA vs SAST vs DAST — Checkmarx](https://checkmarx.com/learn/sca/sca-sast-dast/)
- [Securing CI/CD Pipelines with SAST, DAST, SCA — Medium / Mahesh Gaikwad](https://medium.com/@maheshgaikwad128/securing-ci-cd-pipelines-with-sast-dast-and-sca-a-practical-guide-3d80f0dce380)
- [What Is SAST? — Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/what-is-sast-static-application-security-testing)

---

## Academic Research

### JSAER (2023) — Comparative Analysis of DAST, SAST, and IAST
> **Title**: "Comparative Analysis of DAST, SAST, and IAST"
> **Journal**: *Journal of Scientific and Engineering Research*, Vol. 10, Issue 8 (2023), pp. 158–165
> **PDF**: [JSAER](https://jsaer.com/download/vol-10-iss-8-2023/JSAER2023-10-8-158-165.pdf)

Key findings:
- IAST achieves best results when **combined with DAST**
- DAST is superior for runtime vulnerabilities (SQL injection, XSS, authentication issues)
- SAST is indispensable for high-severity code-level flaws (buffer overflows, hardcoded secrets)
- IAST = best of both: analyzes running apps from inside with full code context

### Benchmarking DAST Tools (2024)
> **Title**: "A Comparative Analysis and Benchmarking of Dynamic Application Security Testing (DAST) Tools"
> **Source**: [ResearchGate](https://www.researchgate.net/publication/385500967_A_Comparative_Analysis_and_Benchmarking_of_Dynamic_Application_Security_Testing_DAST_Tools)

Empirical testing of **75 real-world web applications** using 4 SAST and 5 DAST tools — the largest empirical comparison study for these tool types.

### O'Donoghue et al. (2024) — SBOM Systematic Literature Review
> **Title**: "Software Bill of Materials in Software Supply Chain Security: A Systematic Literature Review"
> **Authors**: Eric O'Donoghue, Yvette Hastings, Ernesto Ortiz, A. Redempta Manzi Muneza
> **Institution**: Montana State University
> **Year**: 2024 | arXiv:2506.03507
> **Open access**: [arXiv HTML](https://arxiv.org/html/2506.03507v1)

Synthesized 40 peer-reviewed studies. Conclusion: *"SBOMs are not yet turn-key solutions"* — effective integration requires tool tuning, manual validation, and VEX statements for exploitability context. Rising from 1 publication in 2020 to 21 in 2023 shows rapid growth of the field.

### Integrating Security into CI/CD: SAST, DAST, SCA (2025)
> **Title**: "Integrating Security into CI/CD Pipelines: A DevSecOps Approach with SAST, DAST, and SCA Tools"
> **Source**: [ResearchGate](https://www.researchgate.net/publication/390459514_Integrating_Security_into_CICD_Pipelines_A_DevSecOps_Approach_with_SAST_DAST_and_SCA_Tools)

Practical research on pipeline-stage placement of each tool type and combined effectiveness findings.

---

## Sample Exam Questions — Explained

### Q3 — Building Meaningful Metrics
> *"Which is needed to build meaningful metrics?"*
> **Answer: D — All of the above (data, a repeatable approach, context)**

Meaningful metrics require all three components: raw **data** to measure, a **repeatable approach** to produce consistent trend-able results, and **context** to interpret what the numbers mean. Any one or two alone is insufficient — data without context is noise, context without data is speculation, and a non-repeatable approach produces results you cannot compare over time.

---

### Q9 — Code-Driven Peer-Reviewed Processes
> *"Jacqueline establishes a pipeline and is determined to implement code-driven, peer-reviewed processes. Which is she attempting to implement?"*
> **Answer: B — Data Standards**

"Code-driven, peer-reviewed processes" in the pipeline context refers to establishing data/code standards enforced through the pipeline itself (linting rules, coding standards, security baselines in version control). This is the most conceptually opaque question in the sample exam — none of the other options (shift left, data validation, technical debt) describe embedding *standards* into the pipeline as executable, reviewed code.

---

### Q11 — Continuous Security Definition
> *"Which statement about continuous security practices is MOST correct?"*
> **Answer: A — Represents the addressing of security concerns and testing in the Continuous Delivery pipeline**

The DSOF glossary defines Continuous Security verbatim as "Addressing security concerns and testing in the Continuous Delivery pipeline on an ongoing basis." **B** is the Continuous Integration (CI) definition. **C** ("should be fully automated") is too absolute — human judgment remains necessary. **D** describes Continuous Deployment, not Continuous Security.

---

### Q20 — Dev-Sec Friction: What to Do First
> *"Security roadblocks are negatively impacting developers. Which DevSecOps principle should they consider FIRST?"*
> **Answer: C — Create a shared vision and objectives**

When Dev and Sec are in friction, the root cause is misaligned goals — each team optimizes for different outcomes. Creating a shared vision establishes what everyone is collectively trying to achieve *before* automating (B) or measuring (D). You cannot usefully automate practices that teams haven't agreed on. **A** (education) addresses symptoms; **C** addresses the cause.

---

### Q26 — "Just Enough" Security
> *"In the context of DevSecOps, how do you put in place 'just enough' security?"*
> **Answer: B — Strike a balance between real and perceived exposure**

"Just enough" means calibrating security investment to *actual* risk, not worst-case fears. **A** (invest as much as possible) ignores cost and delivery impact. **C** (let the business decide) partially delegates but doesn't address the calibration problem. **D** (countermeasures for all threats) is impractical — it would halt delivery.

---

### Q30 — Security Coverage at Scale
> *"Mr. Jones has two security experts covering 20–30 development teams. What may be a best practice to extend coverage at scale?"*
> **Answer: C — Security Champions**

Security Champions multiply expert reach across many teams by embedding security-aware developers within each team. They provide the human judgment, mentoring, and first-line triage that Policy as Code cannot replace. **Strict approval processes** (B) would further slow delivery and create bottlenecks. **Policy as Code** (D) automates enforcement but doesn't provide mentoring or team-level judgment.

---

### Q36 — Cloud Forensics: What Is INCORRECT
> *"Which statement about cloud forensics and incident response is INCORRECT?"*
> **Answer: B — Responsibility of the cloud provider**

Cloud forensics is governed by the **shared responsibility model** — customers are responsible for security incidents affecting their applications and data; cloud providers are responsible for the infrastructure. Assuming the cloud provider handles all forensics is a dangerous and incorrect position. **A** (live response emphasis), **C** (requires planning), and **D** (automation is possible) are all correct.

---

### Q38 — Separation of Duties: What Is INCORRECT
> *"Which statement about separation of duties and DevOps is INCORRECT?"*
> **Answer: A — Auditors must redefine controls**

DevSecOps *enhances* auditors' ability to verify controls — automated pipeline logs, continuous compliance evidence, and real-time dashboards make auditors' existing framework easier to apply, not harder. Auditors do not need to redefine their controls; the pipeline becomes the system of record that satisfies those controls. **B, C, D** are all correct statements about DevOps and SOD.

---

## Exam Traps

> **TRAP — IAST vs RASP: both runtime agents, opposite purposes**: IAST instruments the app during *testing* to detect vulnerabilities. RASP instruments the app in *production* to block attacks in real time. The distinguishing question: "Is it testing or protecting?" RASP is the only tool that actively blocks (Detect & Protect). IAST only detects.

> **TRAP — SAST has more false positives than DAST**: SAST analyzes code statically without runtime context, so it frequently flags code paths that are never actually reachable. DAST operates with real runtime data, so its findings are grounded in actual execution — fewer false positives. If asked which tool produces *fewer* false positives: DAST > SAST.

> **TRAP — SCA vs SAST for "limited budget" (Q21, DSOF-7)**: Counterintuitively, SCA is the better budget answer because free open-source SCA tools (Trivy, OWASP Dependency-Check) cover the single highest-value attack surface (known CVEs in dependencies) with minimal setup. SAST requires more tuning and generates more noise.

> **TRAP — Continuous Security ≠ Continuous Integration**: CI = developers merge code daily and automated tests run. Continuous Security = security concerns and testing are addressed *throughout* the CD pipeline. They overlap but are not the same. Q11 tests this distinction directly.

> **TRAP — Shared responsibility in cloud = customer owns their app security**: Any exam question implying the cloud provider is responsible for application-level incidents → INCORRECT. The cloud provider owns the infrastructure layer; the customer owns everything they deploy on top of it.
