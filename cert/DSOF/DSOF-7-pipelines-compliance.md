# DSOF-7 — DevOps Pipelines and Continuous Compliance

> **5 Questions**
> ← [Back to Index](DSOF-index.md)

---

## Primary Reference
- [DevSecOps Pipeline: Continuous Compliance Guide — Drata](https://drata.com/grc-central/compliance-as-code/devsecops-pipeline)

---

## What Continuous Compliance Means

| Model | How It Works |
|---|---|
| Traditional Compliance | Periodic audits (quarterly, annual) — a snapshot at a point in time |
| Continuous Compliance | Automated policy checks built into **every pipeline stage** — every commit, build, test, and deploy triggers validation |

The shift from periodic to continuous compliance mirrors the shift-left philosophy: catch issues early, automatically, rather than discovering them during an audit.

---

## Security and Compliance Checks by Pipeline Stage

| Stage | Activity |
|---|---|
| Pre-Commit | Secrets scanning, IaC linting, local policy validation (Conftest, OPA hooks) |
| Build | SAST, SCA, license compliance checking, dependency vulnerability scanning |
| Test | DAST, IAST, integration security tests, regression checks |
| Artifact | Image signing, provenance verification, SBOM generation and attachment |
| Deploy | GitOps policy gates, cluster configuration validation, IaC security checks |
| Runtime | SIEM correlation, anomaly detection, observability, automated compliance report generation |

---

## Key Concepts

### Policy as Code / Compliance as Code
Security and compliance rules are written as executable, versioned code — not static documents.
- Tools: Open Policy Agent (OPA), Conftest, HashiCorp Sentinel
- Policies can be tested, peer-reviewed, and audited in version control
- Violations fail pipeline stages automatically, blocking non-compliant deployments

### GitOps and Supply Chain Integrity
- Signed manifests ensure only verified artifacts are deployed
- Image provenance tracked from build to runtime
- SBOM attached to each artifact for downstream compliance verification

### Three-Plane Compliance Framework (MDPI, 2026)
| Plane | Role |
|---|---|
| Control Plane | Policy definitions and governance rules |
| Data Plane | Compliance data collection and storage (Compliance Data Lakehouse) |
| Management Plane | Multi-dimensional lineage tracking and automated audit report generation |

---

## Key Terms

| Term | Definition |
|---|---|
| Continuous Compliance | Automated, always-on policy checks embedded at every CI/CD stage |
| Policy as Code | Compliance rules written as executable, versioned code (OPA, Sentinel, Conftest) |
| Artifact Management | Storing, versioning, signing, and attesting build outputs in a secure repository |
| CI/CD Pipeline | Continuous Integration / Continuous Delivery — automated flow from code commit to production |
| GRC | Governance, Risk, Compliance — the management framework above the technical pipeline |
| System of Record | The authoritative source of truth for a given data domain (e.g., the pipeline as the compliance record) |
| SBOM | Software Bill of Materials — complete inventory of all components in a software artifact |
| IaC (Infrastructure as Code) | Defining infrastructure (servers, networks, policies) as version-controlled code |

---

## Supporting References

- [Integrating Security into CI/CD Pipelines — Free eBook PDF, Practical DevSecOps](https://www.practical-devsecops.com/wp-content/uploads/2024/06/eBook-Integrating-Security-into-CI_CD-Pipelines-through-DevSecOps-Approach-1.pdf)
- [Automating DevSecOps in CI/CD Pipelines — Medium / Sandeep Komal](https://medium.com/@sandeepkomalp/automating-devsecops-in-ci-cd-pipelines-integrating-security-without-slowing-delivery-264227cd29d9)
- [What Is CI/CD Security? — Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/what-is-ci-cd-security)
- [How DevSecOps CI/CD Secures the Software Supply Chain — OpsMx](https://www.opsmx.com/blog/how-devsecops-ci-cd-pipeline-secures-the-software-supply-chain/)
- [Top DevSecOps Tools for a Secure CI/CD Pipeline — CloudBees](https://www.cloudbees.com/blog/top-devsecops-tools)

---

## Academic Research

### MDPI (2026) — Three-Plane Continuous Compliance Framework
> **Title**: "Integrating Continuous Compliance into DevSecOps Pipelines: A Data Engineering Perspective"
> **Journal**: *Data*, MDPI (2026)
> **Open access**: [MDPI](https://www.mdpi.com/2674-113X/5/1/6)

Proposes a Three-Plane Continuous Compliance Framework and a Compliance Data Lakehouse architecture. Introduces an End-to-End DevSecOps Integration Pattern where embedded Policy-as-Code validation gates run at every CI/CD stage, transforming compliance from a periodic audit into a continuous, automated process.

### SSRN / Singh (2025) — Automated Security Testing in CI/CD
> **Title**: "Automating Security Testing in CI/CD Pipelines using DevSecOps Tools: A Comprehensive Study"
> **Source**: [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5267959)

Surveys SAST, DAST, and SCA tool integration patterns within CI/CD pipelines, with focus on automation depth and security gate placement at each pipeline stage.

### ResearchGate (2025) — DevSecOps Security Framework for CI/CD Risk Mitigation
> **Title**: "DevSecOps-Driven Security Framework for CI/CD Pipeline Risk Mitigation"
> **Source**: [ResearchGate](https://www.researchgate.net/publication/394141708_DevSecOps-Driven_Security_Framework_for_CICD_Pipeline_Risk_Mitigation)

Presents a risk mitigation framework targeting the most common CI/CD pipeline vulnerability classes.

### Sinan et al. (2025) — Integrating Security Controls in DevSecOps
> **Title**: "Integrating Security Controls in DevSecOps: Challenges, Solutions, and Future Research Directions"
> **Journal**: *Journal of Software: Evolution and Process* (Wiley, 2025)
> **Link**: [Wiley](https://onlinelibrary.wiley.com/doi/full/10.1002/smr.70029)

Systematic review identifying 19 challenges and 18 solutions specifically for pipeline-level security control integration.

### Vakhula et al. (2024) — Policy-as-Code for RBAC
> **Title**: "Policy-as-Code for Role-Based Access Control"
> **Venue**: *CEUR Workshop Proceedings*, Vol. 3991
> **Paper**: [CEUR PDF](https://ceur-ws.org/Vol-3991/paper11.pdf)

Demonstrates treating pipeline access control policies as executable, versioned, testable code — enabling continuous compliance for authorization decisions.

---

## Sample Exam Questions — Explained

### Q5 — Pipeline Goal
> *"Bob Berker establishes a pipeline to deploy software in a fast and continuous manner. Which DevSecOps goal could he be trying to achieve?"*
> **Answer: D — Rapid time to market**

Deploying "fast and continuously" is the operational definition of reducing Time to Market — getting value to customers sooner. **Bake security in** (A) describes security integration philosophy, not deployment speed. **Third Way** (B) is Continual Learning, not continuous deployment. **Quality checks** (C) are a component of a pipeline, not its primary business goal.

---

### Q14 — Architecture Asset Categories
> *"Planning for a DevSecOps pipeline requires tools for notification, health and architectures. What asset categories are typically associated with architecture?"*
> **Answer: A — Virtual Machines, Containers, Platform as a Service**

Architecture in the pipeline context refers to the compute/hosting infrastructure layer: VMs, containers, and PaaS are the canonical infrastructure components. **B** mixes IaC (a practice) with a specific web server (Apache). **C** lists specific tools (Kafka, Kubernetes, Docker) rather than categories. **D** mixes an access control method, a metrics type, and a methodology — not architecture.

---

### Q15 — DAST Purpose
> *"Which describes the purpose of dynamic application security testing (DAST) tools?"*
> **Answer: B — Performs vulnerability and weakness analysis on compiled (built) code**

DAST operates on the running (built) application — it does not require source code. "Compiled/built" distinguishes DAST from SAST (which needs source code). **A** (source code analysis) = SAST. **C** (libraries with known vulnerabilities) = SCA. **D** (gaining access to a system's data) = Penetration Testing. Note: DAST tests from outside via HTTP/API; "compiled (built)" is the official exam language for this distinction.

---

### Q21 — Limited Budget Testing Choice
> *"An organization with a very limited budget is investigating ways to improve application security testing. Which testing technique will BEST meet their current needs?"*
> **Answer: C — Software composition analysis**

SCA offers the best cost-to-coverage ratio because mature open-source tools (OWASP Dependency-Check, Trivy, Grype) are free, and known CVEs in third-party dependencies represent the single largest attack surface in most applications. **Pen testing** (D) is the most expensive option and requires specialized expertise. **SAST** (A) and **DAST** (B) require more configuration and produce more noise to tune through.

---

## Exam Traps

> **TRAP — DAST is not the same as Penetration Testing**: DAST is automated black-box scanning of a running application (typically via HTTP/API crawling). Pen testing involves a human tester with creative attack chains, social engineering, and chained exploitation. Q15 option D describes pen testing, not DAST.

> **TRAP — SAST ≠ "compiled code" analysis**: SAST analyzes *source code* statically, before compilation. DAST analyzes the compiled, running application. This is the exact distinction Q15 tests — "source code" → SAST; "compiled/built" → DAST.

> **TRAP — SCA runs at build time, not runtime**: SCA checks libraries and dependencies against CVE databases during the build phase (before the app runs). It is the only major security testing tool that operates on dependency *metadata* rather than application code or behavior.

> **TRAP — Rapid time to market vs Third Way**: "Deploying fast and continuously" = Time to Market (a business goal). The Third Way (Continual Learning) is about organizational learning from experiments and incidents — not about deployment speed. Don't conflate CD/CI practices with the philosophical framework.
