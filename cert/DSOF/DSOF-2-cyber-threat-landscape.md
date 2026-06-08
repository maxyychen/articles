# DSOF-2 — Defining the Cyber Threat Landscape

> **6 Questions**
> ← [Back to Index](DSOF-index.md)

---

## Primary Reference
- [Threat Modeling with STRIDE and DREAD: A Comprehensive Guide — Medium](https://medium.com/@nandeesh-kumar/threat-modeling-with-stride-and-dread-a-comprehensive-guide-64992a04f0ac)

---

## STRIDE — Threat Classification Framework

**Origin**: Created by **Loren Kohnfelder and Praerit Garg** at Microsoft in 1999, published in Microsoft's internal "Interface" journal as *"The Threats to our Products"* (April 1, 1999). Formally adopted in Microsoft's Security Development Lifecycle (SDL) by 2002. Popularized externally by Adam Shostack's 2014 book *Threat Modeling: Designing for Security*. Used to systematically enumerate what can go wrong in a system.

| Letter | Threat | Description |
|---|---|---|
| S | Spoofing | Gaining unauthorized access by impersonating another user or device |
| T | Tampering | Maliciously modifying data or configurations, causing integrity issues |
| R | Repudiation | Denying actions or transactions, complicating accountability |
| I | Information Disclosure | Unauthorized exposure of sensitive information |
| D | Denial of Service | Disrupting service availability to legitimate users |
| E | Elevation of Privilege | Gaining unauthorized access to higher privilege levels |

Each letter maps to a violation of a CIA Triad property:
- Spoofing → Confidentiality | Tampering → Integrity | Repudiation → Non-repudiation | Information Disclosure → Confidentiality | Denial of Service → Availability | Elevation of Privilege → Authorization

---

## DREAD — Threat Risk Scoring Model

**Usage**: After STRIDE identifies threats, DREAD ranks them by risk score (0–10 per criterion, then averaged).

| Letter | Criterion | What It Measures |
|---|---|---|
| D | Damage | Severity of impact if the threat is exploited |
| R | Reproducibility | How easily the attack can be repeated |
| E | Exploitability | Ease of executing the attack |
| A | Affected Users | How many users are impacted |
| D | Discoverability | How easily the vulnerability can be found |

**Workflow**:
1. List assets
2. Apply STRIDE per asset to enumerate threats
3. Score each threat with DREAD (average the five scores)
4. Rank by total score → prioritize mitigation from highest down

---

## OCTAVE — Organizational Risk Methodology

**Origin**: Carnegie Mellon University Software Engineering Institute (SEI), 1999.
Unlike STRIDE/DREAD (developer-facing, technical), OCTAVE is **organizational and strategic** — it involves all business levels and focuses on what matters most to the mission.

### Official Publications
> **OCTAVE Framework v1.0**
> Authors: Christopher J. Alberts, Sandra Behrens, Richard D. Pethia, William R. Wilson
> Report: CMU/SEI-99-TR-017 (1999)
> [SEI Library](https://www.sei.cmu.edu/library/operationally-critical-threat-asset-and-vulnerability-evaluation-octave-framework-version-10/)

> **OCTAVE Allegro (2007 update)**
> Authors: Caralli, Stevens, Young, Wilson — Report: CMU/SEI-2007-TR-012
> [SEI Library](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=8419)

### Three OCTAVE Phases
1. **Build asset-based threat profiles** — using knowledge from all organizational levels
2. **Identify infrastructure vulnerabilities** — technical component assessment
3. **Develop and implement a security strategy** — risk-based protection plans

### OCTAVE Variants

| Variant | Designed For | Key Difference |
|---|---|---|
| OCTAVE | Large enterprises | Full 3-phase, multi-team workshop-based process |
| OCTAVE Allegro | Small/medium organizations | Streamlined; fewer resources required; no large workshop |
| OCTAVE-S | Small orgs with flat structure | Fully self-directed; no external facilitation needed |

---

## Threat Modeling Methodology Comparison

| Method | Best Used When | Strength | Limitation |
|---|---|---|---|
| STRIDE | Developer-level threat enumeration | Systematic, well-documented, Microsoft-backed | Does not prioritize threats by itself |
| DREAD | Scoring/ranking STRIDE-identified threats | Quantitative risk ranking | Scoring criteria can be subjective |
| OCTAVE | Org-wide, mission-critical risk assessment | Holistic — involves all business levels | Resource-intensive, requires workshops |
| PASTA | Business-driven risk modeling | Aligns security with business objectives | Complex to implement |
| LINDDUN | Privacy threat modeling | Dedicated privacy focus | Narrow scope (privacy only) |
| VAST | Large-scale Agile/DevOps environments | Scalable, process-integrated | Less prescriptive guidance |

---

## Key Terms

| Term | Definition |
|---|---|
| CIA Triad | Confidentiality, Integrity, Availability — the classic security baseline |
| DIE Triad | Distributed, Immutable, Ephemeral — cloud-native alternative to CIA |
| Threat Intelligence | Actionable knowledge about existing and emerging threats to inform defenses |
| Vulnerability | A weakness that can be exploited by a threat actor |
| Threat | A potential cause of an unwanted incident that may result in harm |
| Penetration Testing | Authorized simulated attack to identify exploitable vulnerabilities |
| Fuzzing | Sending unexpected/random input to an application to discover crashes and flaws |
| Threat Modeling | Structured process for identifying, classifying, and prioritizing threats |

---

## Supporting References

- [What Is the STRIDE Threat Model? — Practical DevSecOps](https://www.practical-devsecops.com/what-is-stride-threat-model/)
- [OCTAVE Method and Its Variants — Medium / C0rs0](https://c0rs0.medium.com/the-octave-method-and-its-variants-octave-allegro-and-octave-s-dc49ce51a05e)
- [5 Threat Modeling Methodologies Compared — IriusRisk](https://www.iriusrisk.com/threat-modeling-methodologies)
- [Shostack's Ultimate Beginner's Guide to Threat Modeling](https://shostack.org/resources/threat-modeling.html)
- [Threat Modeling Methodologies: STRIDE, PASTA, DREAD — DestCert](https://destcert.com/resources/threat-modeling-methodologies/)
- [Threat Modeling Process — OWASP Foundation](https://owasp.org/www-community/Threat_Modeling_Process)

---

## Academic Research

### Naik et al. (2024) — Comparative Analysis of Threat Modeling Methods
> **Title**: "A Comparative Analysis of Threat Modelling Methods: STRIDE, DREAD, VAST, PASTA, OCTAVE, and LINDDUN"
> **Authors**: Nitin Naik, Paul Jenkins, Nick Grace et al.
> **Institution**: Cardiff Metropolitan University
> **Venue**: TechRxiv (2024)
> **Paper**: [TechRxiv PDF](https://www.techrxiv.org/users/845749/articles/1234181/master/file/data/A%20Comparative%20Analysis%20of%20Threat%20Modelling%20Methods-DrNitinNaik/A%20Comparative%20Analysis%20of%20Threat%20Modelling%20Methods-DrNitinNaik.pdf)

The most comprehensive academic comparison of the six threat modeling methodologies tested in the DSOF exam. Provides structured strengths/weaknesses analysis and guidance on when to use each.

### STRIDE-Based Modeling for Industrial Control Systems (2023)
> **Title**: "STRIDE-based threat modeling and DREAD evaluation for the distributed control system in the oil refinery"
> **Year**: 2023
> **Source**: [ResearchGate](https://www.researchgate.net/publication/365184422_STRIDE-based_threat_modeling_and_DREAD_evaluation_for_the_distributed_control_system_in_the_oil_refinery)

Confirmed STRIDE+DREAD as practical and accessible to non-security experts through "STRIDE per element" analysis on data flow diagrams (DFDs). Real-world industrial validation.

---

## Sample Exam Questions — Explained

### Q10 — What Is GRC?
> *"What is Governance, Risk Management and Compliance (GRC)?"*
> **Answer: D — Either A or B**

The DSOF glossary defines GRC as "A team or software platform intended for concentrating governance, compliance, and risk management data." Because the official definition covers both a tooling category (A) and an organizational function (B), "either A or B" is the most complete answer. **C** (executive committee) is not in the definition.

---

### Q25 — Threat Impact Factors
> *"Which factors are recommended to consider the potential impact of a threat?"*
> **Answer: A — Probability, Intent, Capability**

These three factors assess whether a threat will materialize and how severe it would be: Probability (how likely), Intent (does the actor want to harm you?), Capability (can the actor execute?). **B and C** are military SALUTE/SAMDOC identification frameworks — not security assessment models. **D** (CIA Triad) describes *what you protect*, not how you assess threats against it.

---

### Q31 — Measuring Vulnerability Dwell Time
> *"Which can be used to measure how long a vulnerability or software bug exists before it is identified?"*
> **Answer: B — Mean Time to Detect (MTTD)**

MTTD measures the window from vulnerability introduction to discovery — the "dwell time." **MTTC** (Mean Time to Change) measures pipeline velocity from detection to fix deployed. **MTTR** measures recovery time after the fix is deployed until service is fully restored. **Deployment Frequency** measures release cadence. The phrase "before it is identified" is the specific signal for MTTD.

---

### Q34 — First Step for Protection Metrics
> *"What is the first step to understanding the protection metrics associated with DevSecOps?"*
> **Answer: B — Find the organization's crown jewels**

You cannot define meaningful protection metrics without first knowing which assets matter most. "Crown jewels" (highest-value data, most critical systems) determine what thresholds and KPIs are worth tracking. This mirrors OCTAVE Phase 1: "Build asset-based threat profiles." **A** (decompose the application), **C** (source code review), and **D** (develop telemetry) all presuppose that priorities are already known.

---

## Exam Traps

> **TRAP — STRIDE identifies; DREAD scores**: These are sequential steps, not alternatives. STRIDE enumerates *what* could go wrong (per asset). DREAD scores *how bad* each threat is. "Which tool ranks/prioritizes threats?" → DREAD. "Which tool classifies/enumerates threats?" → STRIDE.

> **TRAP — MTTD vs MTTC vs MTTR: know the clock start points**: The three metrics run sequentially. MTTD: vulnerability *introduced* → *detected*. MTTC: *detected* → *fix deployed to production*. MTTR: *fix deployed* → *service fully restored*. In short: `Introduced → [MTTD] → Detected → [MTTC] → Fix deployed → [MTTR] → Recovered`. Q31 says "before it is identified" → MTTD only.

> **TRAP — CIA Triad is what you protect, not how you assess threats**: Q25 is a common confusion point. CIA (Confidentiality, Integrity, Availability) defines the security properties of assets. Probability/Intent/Capability defines how you evaluate the threat itself. These are different analytical layers.

> **TRAP — OCTAVE is org-level, not developer-level**: STRIDE/DREAD = developer analyzing one application's attack surface. OCTAVE = organization-wide risk assessment involving multiple business units, senior management, and IT. If a scenario describes company-wide asset prioritization workshops → OCTAVE.

> **TRAP — GRC "either/or" answer pattern**: When an official definition covers two distinct forms (tool OR team), the exam answer is "either A or B" = D. Recognizing this "both are valid per the glossary" pattern saves time on definition-recall questions.
