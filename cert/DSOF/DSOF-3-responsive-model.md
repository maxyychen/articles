# DSOF-3 — Building a Responsive DevSecOps Model

> **3 Questions**
> ← [Back to Index](DSOF-index.md)

---

## Primary Reference
- [Westrum's Organizational Model in Technology Organizations — IT Revolution](https://itrevolution.com/articles/westrums-organizational-model-in-tech-orgs/)

---

## Westrum's Organizational Typology

**Source**: Ron Westrum, *"A Typology of Organisational Cultures"*, published in **Quality & Safety in Health Care** (the journal's name in 2004; now renamed *BMJ Quality & Safety*), Vol. 13, Suppl. 2, pp. ii22–ii27 (December 2, 2004). Originally developed from research into accident prevention in aviation and healthcare — then adopted by DevOps via *Accelerate* (2018).

| Culture Type | Orientation | Information Flow | Response to Failure | Response to New Ideas |
|---|---|---|---|---|
| Pathological | Power | Withheld for personal gain | Blame individuals | Suppressed |
| Bureaucratic | Rules | Compartmentalized by department | Seek justice by rules | Creates problems |
| **Generative** | Performance | Actively sought and shared | Inquire to improve | Implemented |

DevSecOps targets the **Generative** culture. The Pathological and Bureaucratic types are where security becomes either a blame mechanism or a compliance checkbox.

### DORA Measurement of Westrum Culture
The DORA research team measures organizational culture via six survey questions (1–7 scale):
1. Information is actively sought on teams
2. Messengers face no punishment for delivering bad news
3. Responsibilities are shared
4. Cross-functional collaboration is encouraged and rewarded
5. Failures become improvement opportunities
6. New ideas receive welcome

These six items are averaged into a single Westrum culture score used in regression models.

### Evidence from Research
- The **2019 DORA State of DevOps Report** confirmed: psychological safety predicts software delivery performance, organizational performance, and productivity
- *Accelerate* (Forsgren, Humble, Kim 2018) showed that Westrum culture scores **statistically predict all four DORA metrics**
- Generative teams have: lower turnover, more diverse ideas, higher revenue, and are rated effective **2× more often** by management

---

## Google Project Aristotle — Five Team Dynamics

**Source**: Google's two-year Project Aristotle research (2012), analyzing 180 teams.
[Google re:Work Guide](https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness)

| Dynamic | Definition | Importance |
|---|---|---|
| **Psychological Safety** | Shared belief the team is safe for interpersonal risk-taking | **Most critical — prerequisite for all others** |
| Dependability | Members reliably deliver quality work on time | 2nd |
| Structure & Clarity | Clear expectations, processes, and performance consequences | 3rd |
| Meaning | Finding personal purpose in the work or its output | 4th |
| Impact | Belief that work makes a measurable difference | 5th |

**Amy Edmondson's definition** (Administrative Science Quarterly, 1999): *"A shared belief held by members of a team that the team is safe for interpersonal risk taking."*

Key finding: Team composition (tenure, seniority, extroversion) mattered far less than team dynamics. Individual performance did not predict team performance — how members interact does.

---

## Laloux's Organizational Color Stages

**Source**: Frederic Laloux, *Reinventing Organizations* (2014).

| Color | Metaphor | Characteristics | DevSecOps Maturity |
|---|---|---|---|
| Red | Wolf pack | Power, fear-based control, short-term | Siloed, reactive security — firefighting |
| Amber | Army | Rules, hierarchy, stability, process | Security as a compliance checkbox only |
| Orange | Machine | Achievement, meritocracy, KPI-driven | Security team as a separate approval gate |
| Green | Family | Values, consensus, people-first | Shared responsibility begins to form |
| **Teal** | Living organism | Self-management, wholeness, evolutionary purpose | Full DevSecOps — security embedded everywhere |

### Three Core Teal Principles

| Principle | What It Means |
|---|---|
| Self-management | Distributed decision-making; no command-and-control hierarchy; teams own their security |
| Wholeness | Psychological safety; people bring their full selves to work; no blame culture |
| Evolutionary Purpose | The organization adapts and grows organically toward its mission |

---

## Erickson — Psychosocial Development in Teams

> The DSOF exam uses the term **"Erickson"** (the glossary entry name). The person is **Erik Erikson** (1902–1994), the developmental psychologist who published *Childhood and Society* (1950, 1963).

Erikson proposed a psychoanalytic theory of psychosocial development comprising **eight stages from infancy to adulthood** (confirmed in the DSOF v2.1 glossary). In the DevSecOps context, stages 5–8 (Identity, Intimacy, Generativity, Integrity) are used as a lens to understand how individuals and teams develop the trust, collaboration, and psychological maturity needed for a responsive DevSecOps model and safety culture.

---

## Key Terms

| Term | Definition |
|---|---|
| Safety Culture | Environment where people raise concerns, report failures, and experiment without fear of blame |
| Retrospective | Structured post-sprint or post-incident review — what went well, what didn't, what to improve next |
| Shared Vision | Alignment across all teams on goals, values, and direction — foundation for collaborative security |
| Psychological Safety | Shared belief that the team is safe for interpersonal risk-taking (Edmondson, 1999) |
| Generative Culture | Westrum's highest organizational type — high trust, shared risk, inquiry-based failure response |

---

## Supporting References

- [Westrum's Cultural Typology Assessment — Open Practice Library](https://openpracticelibrary.com/practice/westrums-cultural-typology-assessment/)
- [DORA Capabilities: Generative Organizational Culture](https://dora.dev/capabilities/generative-organizational-culture/)
- [Westrum's Organizational Cultures Are Vital but Misunderstood — The New Stack](https://thenewstack.io/westrums-organizational-cultures-are-vital-but-misunderstood/)
- [Teal Organizations Demystified — Echometer](https://echometerapp.com/en/reinventing-organizations-by-frederic-laloux-book-summary/)
- [DevSecOps Cultural Transformation — PagerDuty](https://www.pagerduty.com/blog/community/devsecops-ops-guide/)
- [5 Tips for Seeding a DevSecOps Culture — Red Hat](https://www.redhat.com/en/blog/devsecops-culture)

---

## Academic Research

### Westrum (2004) — A Typology of Organisational Cultures
> **Title**: "A Typology of Organisational Cultures"
> **Author**: Ron Westrum
> **Journal**: *Quality & Safety in Health Care* (journal's 2004 name; now *BMJ Quality & Safety*), Vol. 13, Suppl. 2, pp. ii22–ii27 (December 2004)

The original peer-reviewed paper defining the three culture types. Westrum initially researched accident prevention in aviation and medicine — DORA later validated its predictive power for software delivery performance.

### Forsgren, Humble, Kim (2018) — *Accelerate*
> **Title**: *Accelerate: The Science of Lean Software and DevOps*
> **Publisher**: IT Revolution Press (2018)

Demonstrated through multivariate regression analysis that Westrum generative culture scores predict all four DORA metrics. The book bridges Westrum's organizational research and DevOps practice.

### Edmondson (1999) — Psychological Safety and Learning in Work Teams
> **Title**: "Psychological Safety and Learning Behavior in Work Teams"
> **Author**: Amy C. Edmondson
> **Journal**: *Administrative Science Quarterly*, 44(2), 350–383 (1999)

Foundational academic paper defining psychological safety. Teams with higher psychological safety show significantly more learning behaviors and better performance outcomes — the empirical basis for the Westrum Generative culture type.

---

## Sample Exam Questions — Explained

### Q6 — KPIs for a Responsive Pipeline
> *"Which represents the BEST practices to building KPIs which reflect a responsive DevSecOps Pipeline?"*
> **Answer: B — KPIs are driven by pipeline/application with the ability to threshold and gate at every stage**

A responsive pipeline requires measurable KPIs *at every stage* — not just at the end — with configurable thresholds (what is acceptable) and gates (what blocks progression). This enables continuous feedback and rapid correction. **A** (whitelisting) is a security control, not a KPI methodology. **C** (let teams self-solve) is decentralized but uncoordinated. **D** (audit requirements) is compliance-oriented, not pipeline-performance-oriented.

---

### Q19 — Backlog Source for New Pipeline Work
> *"Which elements should best be used to create a backlog for new work in your responsive DevSecOps pipeline?"*
> **Answer: D — Integration and Output gaps**

A responsive pipeline is measured by its own performance. "Integration and output gaps" — delta between what the pipeline is designed to deliver and what it actually delivers — are the most actionable, data-driven source of improvement work. **Threat intelligence** (C) feeds the security team's queue, not the pipeline improvement backlog. **Customer suggestions** (A) and **C-Suite input** (B) are too distant from pipeline mechanics to drive operational improvements.

---

### Q23 — Testing That Complements CI
> *"Which testing type compliments an organization's continuous integration practices?"*
> **Answer: D — Static application security tests (SAST)**

SAST analyzes source code without needing a running environment, making it a natural fit for CI (which triggers on every commit/build). **Pen tests** (A) require a live environment and human expertise — incompatible with CI automation. **Vulnerability scans** (B) typically run against live systems. **Canary tests** (C) are a deployment strategy, not a CI-stage security test.

---

### Q28 — Practices That Support DevSecOps
> *"Which of the following practices support DevSecOps?"*
> **Answer: D — All of the above**

All three are core DevSecOps practices: **Security as Code** (A) embeds security configurations in version control alongside application code. **Automation** (B) enables continuous security at delivery speed. **Involving audit and compliance early** (C) prevents end-of-cycle surprises and is itself a form of shift-left. When all options are genuinely correct for the domain, the exam selects "all of the above."

---

### Q33 — Removing the Reporting Bottleneck
> *"Application security's tendency to hand one-off reports to Dev teams outside their normal cycles is a bottleneck. Which practice can BEST remove this constraint?"*
> **Answer: A — Automatically log findings into issue management**

The bottleneck is that security findings are *outside* developers' workflow. The solution is to push findings into the system developers already use (Jira, GitHub Issues) automatically — so security work appears in the same queue as feature work with the same priority mechanisms. **Real-time findings reports** (D) still require developers to context-switch to a separate system. **GRC-to-issue automation** (B) is a downstream step after findings are already logged.

---

## Exam Traps

> **TRAP — Westrum culture types are easy to mix up under pressure**: Pathological = power/blame; Bureaucratic = rules/compartmentalized; Generative = performance/shared. Q29 (in DSOF-4) tests Westrum typology recognition directly — it asks which characteristic is NOT generative. Know all three types cold: information flow (withheld / compartmentalized / actively shared), failure response (blame / seek justice / inquire to improve), and new ideas (suppressed / creates problems / implemented).

> **TRAP — SAST for CI, not pen tests**: CI triggers on every code commit. SAST is the only testing type that (a) requires no running environment, (b) runs in seconds to minutes, and (c) provides actionable code-level findings. Pen tests require hours, human expertise, and a live environment — fundamentally incompatible with CI automation.

> **TRAP — "All of the above" is correct when all options genuinely apply**: The exam uses "all of the above" when the question lists multiple practices that are independently valid. Q28 is an example — security as code, automation, and early compliance involvement are all confirmed DevSecOps practices. Don't overthink it.

> **TRAP — Pipeline KPIs need gates, not just measurements**: A "responsive" pipeline is distinguished by its ability to *gate* (stop/block) non-compliant changes at every stage, not just report on them afterward. Metrics that only report without blocking are monitoring, not pipeline quality gates.
