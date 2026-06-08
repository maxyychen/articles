# DSOF-8 — Learning Using Outcomes

> **3 Questions**
> ← [Back to Index](DSOF-index.md)

---

## Primary Reference
- [DevSecOps Metrics & KPIs — Practical DevSecOps](https://www.practical-devsecops.com/devsecops-metrics/)

---

## Core DevSecOps Metrics (Official DSOF Terminology)

The DSOF exam uses the following three specific metrics. Note that **MTTC = Mean Time to Change** in the DevOps/DevSecOps context — not "Mean Time to Contain" (a general cybersecurity term not used in this exam).

| Metric | Full Name | Measures | Goal |
|---|---|---|---|
| MTTD | Mean Time to Detect | How long a vulnerability or software bug exists before it is identified | Minimize — faster detection limits damage and exposure window |
| MTTC | **Mean Time to Change** | Time from ideation/request through to final implementation in production | Minimize — measures pipeline efficiency and delivery speed |
| MTTR | Mean Time to Recover/Repair | Average time to repair or recover a failed component or service | Minimize — faster recovery restores normal operations |

> **MTTC disambiguation**: In the DSOF exam, MTTC = **Mean Time to Change** (a DevOps pipeline velocity metric — "time from concept to production"). This is NOT "Mean Time to Contain," which is a general cybersecurity incident metric outside DSOF scope. See official DSOF v2.1 glossary.

### Phase Relationship
```
Vulnerability introduced → [MTTD clock] → Detected → [MTTC clock] → Change implemented → [MTTR clock] → Recovered
```

---

## DORA Four Key Metrics (DevSecOps Context)

From *Accelerate* (Forsgren, Humble, Kim, 2018):

| Metric | Category | DevSecOps Learning Use |
|---|---|---|
| Deployment Frequency | Velocity | Tracks how often secure, tested code reaches production |
| Lead Time for Changes | Velocity | Measures pipeline efficiency including security gates |
| Change Failure Rate | Stability | Indicates whether security checks are catching issues pre-production |
| Time to Restore (MTTR) | Stability | The DORA version of incident recovery — maps directly to MTTR above |

---

## Additional DevSecOps Metrics

| Metric | What It Tracks |
|---|---|
| Number of Security Vulnerabilities | Trend of open vulnerabilities over time — improvement = fewer unresolved |
| Security Test Coverage | Breadth of security testing across the codebase |
| Code Review Findings | Security issues found during peer review — reflects developer security awareness |
| Deployment Frequency | How often software is released — indicator of security integration maturity |
| Patch Cadence | How quickly security patches are applied after release |

---

## Retrospective

A retrospective is a structured review session held after a sprint or incident. It is a core mechanism for implementing the Third Way (Continual Learning).

**Standard structure**:
1. What went well?
2. What didn't go well?
3. What will we improve next time?

In DevSecOps, retrospectives are used after both sprint cycles and security incidents to embed security learnings back into the team's practices.

---

## Chaos Engineering

Chaos Engineering is the practice of **deliberately injecting failures** into systems in a controlled way to find weaknesses before real incidents expose them.

**Workflow**:
1. Define system steady state via KPIs (e.g., error rate, latency, throughput)
2. Formulate a hypothesis: "If we kill one node, the system will continue to serve requests normally"
3. Inject the failure in a controlled environment
4. Observe the actual result vs. the hypothesis
5. Measure, learn, and improve — socialize findings across teams

**Key principle**: Chaos Engineering is a learning tool, not a destructive one. It answers the question: *"Does our system actually behave the way we think it does?"*

**Tools**: Chaos Monkey (Netflix), Chaos Mesh, LitmusChaos, Gremlin

---

## Key Terms

| Term | Definition |
|---|---|
| MTTD | Mean Time to **Detect** — how long before a vulnerability/incident is identified |
| MTTC | Mean Time to **Change** — time from concept/request to production implementation (pipeline velocity metric) |
| MTTR | Mean Time to **Recover** — how fast normal service is restored after failure |
| Retrospective | Structured post-sprint or post-incident learning review |
| Chaos Engineering | Deliberately injecting failures to validate system resilience proactively |
| Resilience | System's ability to withstand, recover from, and adapt to failures — improved by tracking MTTR trends |
| Incident Response | Defined process: detect → contain → remediate → recover → learn |
| Mean Time Between Failures (MTBF) | Average time a system operates before failing — a reliability metric |

---

## Supporting References

- [Incident Response Metrics: MTTD, MTTR, MTTC Complete Guide — Rootly](https://rootly.com/incident-response/metrics)
- [MTTD and MTTR: Security Metrics Explained — Cyberhaven](https://www.cyberhaven.com/infosec-essentials/what-is-mttd-mttr)
- [MTTR: The Magic Metric — DevOps.com](https://devops.com/mttr-magic-metric/)
- [SOC Metrics — MTTD, MTTR, and Security KPIs — nflo.tech](https://nflo.tech/knowledge-base/soc-metrics-mttd-mttr-kpi-security/)
- [DORA Four Keys Metrics — Google Cloud Blog](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance)
- [Essential Metrics for Security Operations — Fortinet](https://www.fortinet.com/resources/cyberglossary/secops-metrics)

---

## Academic Research

### Fossati et al. (2024) — Chaos Engineering in DevOps Pipelines
> **Title**: *"Let it be Chaos in the Plumbing!" Usage and Efficacy of Chaos Engineering in DevOps Pipelines*
> **Authors**: Stefano Fossati, Damian Andrew Tamburri, Massimiliano Di Penta, Marco Tonnarelli
> **Source**: arXiv:2509.14931 (2024)
> **Open access**: [arXiv HTML](https://arxiv.org/html/2509.14931)
> **Industrial validation**: NXP Semiconductors workshops

Gray literature review analyzing **50 sources (2019–2024)**. Developed a ten-concept classification framework in three categories:

**Hypothesis**: Define steady state via KPIs → formulate hypotheses → validate post-experiment

**Experiments**: Control real-world events → run in production (when feasible) → automate continuously → contain blast radius → increase complexity incrementally

**Learning & Collaboration**: Measure and improve → socialize findings continuously across teams

Key finding: Practitioners emphasize *"controlled experimentation, automation, and risk mitigation"* more than the original Netflix principles. **Observability and cross-team communication** are critical success factors that purely technical implementations overlook.

Tools studied: **Chaos Mesh**, **Gremlin**, **LitmusChaos**

### Forsgren, Humble, Kim (2018) — *Accelerate* (MTTR as DORA Metric)
> **Publisher**: IT Revolution Press (2018)

Established MTTR (Time to Restore Service) as one of the four scientifically validated metrics for software delivery performance. Elite-performing teams restore service in under one hour — this is the benchmark for DevSecOps incident response excellence.

---

## Sample Exam Questions — Explained

### Q40 — Value of Professional Certification
> *"The advantage of obtaining a professional certification to validate your learning practice is:"*
> **Answer: A — Recognized at multiple levels across the profession**

Professional certifications provide broad recognition: peers, hiring managers, and organizations all recognize the credential as a validated benchmark of knowledge. **B** (long lead time) describes a drawback, not an advantage. **C** (free drinks) is humorous misdirection. **D** (Git projects) describes practical experience, which is a different form of credential validation than certification.

---

## Exam Traps

> **TRAP — MTTC in DSOF means "Change," not "Contain"**: In general cybersecurity, MTTC often refers to "Mean Time to Contain" (how fast you contain a breach). In the DSOF exam, MTTC is explicitly **Mean Time to Change** — the pipeline velocity metric measuring how fast a concept or fix moves from idea to production. Always use the DSOF glossary definition on this exam.

> **TRAP — The three metrics flow in sequence, not in parallel**: MTTD → MTTC → MTTR describes a pipeline: vulnerability introduced → detected (MTTD ends) → fix deployed (MTTC ends) → service restored (MTTR ends). Confusing which clock starts and stops when is the most common error on metrics questions.

> **TRAP — MTTR appears in both DSOF metrics and DORA metrics**: In DSOF, MTTR = Mean Time to Recover (DevSecOps pipeline metric). In DORA, "Time to Restore Service" is the equivalent fourth metric. They measure the same thing from different research traditions — treat them as interchangeable for exam purposes.

> **TRAP — Chaos Engineering is a learning tool, not a destructive one**: The exam may present Chaos Engineering as reckless. The correct framing is controlled, hypothesis-driven experimentation to validate system resilience *before* real incidents expose weaknesses. The emphasis is on "controlled" and "learning," not chaos for its own sake.
