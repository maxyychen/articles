# Generative AI and Human Cognition: What the Research Actually Shows

> A synthesis of recent academic papers (MIT Media Lab, MIT Economics/NBER, arXiv, Nature Human Behaviour, Frontiers in Psychology, Science Advances) and practitioner/blog commentary on generative AI's relationship to human thinking — both how AI itself reasons, and how using it changes the way we reason.
>
> Generated: 2026-07-28

---

## Executive Summary

Two distinct research conversations are happening under the same banner of "AI and cognition," and conflating them causes most of the public confusion:

1. **How does AI reason, compared to humans?** Cognitive-science research increasingly shows that large language models arrive at correct answers through mechanisms fundamentally unlike human reasoning — impressive on benchmarks, fragile on trivial variants, and missing the meta-cognitive monitoring humans use to know when they're wrong.
2. **What does using AI do to human reasoning?** Behavioral and neuroscience research shows the effect is not fixed — it swings from measurable skill erosion to genuine cognitive augmentation depending almost entirely on *how* the tool is used, not *whether* it is used.

The strongest emerging finding across both literatures is that **passive, transactional use of generative AI correlates with cognitive decline (offloading, weaker neural engagement, reduced critical thinking), while active, metacognitively engaged use correlates with cognitive enhancement (better problem-solving, creativity gains, deeper learning).** The technology is not neutral, but it is not deterministic either — the outcome is a design and behavior choice, not a law of nature. A newer and more unsettling strand of research pushes this from the individual to the societal level, modeling conditions under which AI could cause a collapse of *collective* human knowledge even while each individual gets better answers.

---

## 1. How Large Language Models Reason (and How That Differs From Humans)

### The Cognitive Foundations Gap

A 2025 arXiv paper, ["Cognitive Foundations for Reasoning and Their Manifestation in LLMs"](https://arxiv.org/abs/2511.16660), built a taxonomy of 28 cognitive elements drawn from human reasoning research and used it to audit both LLM outputs and a meta-analysis of roughly 1,600 LLM research papers. The central finding: **models frequently produce correct answers through mechanisms fundamentally different from the humans they're being compared to.** They solve complex problems yet fail on simpler variants of the same problem — a signature of pattern-matching rather than principled reasoning.

Specifically, the models:
- Default to **"surface-level enumeration"** — mechanically listing possibilities — rather than the deeper abstraction human think-aloud traces show.
- **Possess** the behavioral capability for good reasoning strategies but **fail to deploy them spontaneously**, especially on ill-structured problems that require diverse representations and self-monitoring.
- Are weakest exactly where meta-cognitive control matters most: the research community's own papers overwhelmingly measure easy-to-quantify elements like sequential organization (55% of papers) and decomposition (60%), while self-awareness/meta-cognitive monitoring is covered in only 16% — despite being one of the strongest predictors of success.

When the authors built test-time scaffolding that explicitly forced models to use the neglected cognitive elements, performance on complex problems improved by up to **66.7%** — suggesting the capability exists latently but isn't triggered by default prompting.

### Theory of Mind: Convincing Behavior, Uncertain Mechanism

A widely cited 2024 Nature Human Behaviour study, ["Testing theory of mind in large language models and humans"](https://collaborate.princeton.edu/en/publications/testing-theory-of-mind-in-large-language-models-and-humans/) (Strachan et al.), ran a comprehensive battery of false-belief and mentalizing tasks across humans and LLMs. LLMs produced outputs "consistent with the outputs of mentalistic inference in humans" — but the authors' own framing is a caution, not an endorsement: passing a behavioral test is not proof of the underlying cognitive machinery, and follow-up 2025–2026 work (e.g., ["Language Statistics and False Belief Reasoning: Evidence from 41 Open-Weight LMs"](https://arxiv.org/pdf/2602.16085)) has been actively re-examining whether apparent theory-of-mind performance is a statistical artifact of training-corpus language patterns rather than genuine belief-tracking.

### The Practical Upshot

This body of work matters beyond academic interest: it explains *why* AI reasoning failures are often surprising to users. A model that aces a bar exam question can fail a much simpler logic puzzle, because it never built the general-purpose reasoning scaffold a human uses — it pattern-matched its way to the hard answer. This asymmetry is a recurring theme in the ["Large Language Model Reasoning Failures"](https://arxiv.org/pdf/2602.06176) literature and is one reason expert oversight of AI output remains necessary even as benchmark scores climb.

---

## 2. What Using AI Does to Human Cognition: The Neuroscience

### MIT Media Lab: "Your Brain on ChatGPT"

The single most-discussed empirical study in this space is MIT Media Lab's [**"Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task"**](https://www.media.mit.edu/publications/your-brain-on-chatgpt/) ([arXiv:2506.08872](https://arxiv.org/abs/2506.08872)).

**Methodology:** 54 participants were split into three groups — LLM-assisted writing, Search Engine use, and Brain-only (no tools) — each completing three essay-writing sessions. An 18-person subset did a fourth session in which conditions were swapped (LLM users went tool-free; Brain-only users got LLM access). EEG measured neural engagement throughout; essays were scored by NLP tools, human graders, and AI evaluators; participants were interviewed and asked to quote their own essays from memory.

**Key findings:**
- **Neural connectivity scaled inversely with tool reliance.** Brain-only participants showed the strongest, most distributed neural networks; Search Engine users showed moderate engagement; LLM users showed the weakest connectivity of the three groups.
- **Ownership and memory degraded with LLM use.** Self-reported ownership of the essay was lowest in the LLM group and highest in the Brain-only group. LLM users also struggled to accurately quote sentences from essays they had just "written."
- **The effect showed some but incomplete recovery.** In the swapped fourth session, participants moving from LLM to Brain-only still showed reduced alpha/beta connectivity (a lingering under-engagement), while participants moving from Brain-only to LLM showed higher memory recall and prefrontal activation similar to Search Engine users — suggesting habits of independent thinking built up over prior sessions partially transferred.
- Over the four-month span, the researchers coined the term **"cognitive debt"**: reliance on the LLM correlated with underperformance across neural, linguistic, and behavioral measures simultaneously, raising concern about compounding costs to learning if this pattern is sustained at scale (e.g., in classrooms).

**Caveats worth stating plainly:** the sample is small (54, with only 18 in the critical swap condition), the task is narrow (persuasive essay writing), and the study is not yet peer-reviewed in a journal — as [The Conversation's critical response](https://theconversation.com/mit-researchers-say-using-chatgpt-can-rot-your-brain-the-truth-is-a-little-more-complicated-259450) points out, "brain rot" headlines overstate what n=54 EEG data can support. It is a strong first signal, not a settled fact.

### Real-World Skill Decay: The Physician Example

Beyond the lab, the [APA Monitor's July/August 2026 feature "How AI is reshaping human skills and thinking"](https://www.apa.org/monitor/2026/07-08/ai-job-skills-thinking) cites a concrete field example: **physicians' polyp-detection rates dropped 6 percentage points** after AI-assisted colonoscopy tools were introduced into their workflow — a real-world instance of the "GPS effect," where reliance on an automated aid measurably degrades the underlying human skill it assists, even among trained experts. The Monitor's broader synthesis frames three moderating factors that determine whether AI use helps or hurts a given worker: (1) whether the offloaded task was routine or a core learning experience, (2) whether the user is expert enough to critically evaluate AI output or a novice who can't catch its errors, and (3) whether organizational incentives reward speed (encouraging passive use) or quality (encouraging active verification).

---

## 3. Critical Thinking: Convergent Evidence of a Confidence-Mediated Effect

Two large, independent studies converge on a strikingly similar mechanism.

### Microsoft Research / CHI 2025: Lee et al.

["The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects from a Survey of Knowledge Workers"](https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/), presented at CHI 2025, surveyed knowledge workers on their GenAI use and found:
- **Higher confidence in GenAI correlates with less critical thinking**; higher confidence in *oneself* correlates with more.
- GenAI use doesn't eliminate critical thinking so much as **relocate it** — away from generative analysis and toward verification, integration of AI output, and "stewardship" of the task rather than execution of it.

### Gerlich (2025), *Societies* / MDPI

[**"AI Tools in Society: Impacts on Cognitive Offloading and the Future of Critical Thinking"**](https://www.mdpi.com/2075-4698/15/1/6) surveyed **666 participants** (plus 50 follow-up semi-structured interviews) across age groups and education levels and found a **significant negative correlation between frequent AI tool use and critical thinking scores, mediated by cognitive offloading.** Younger participants showed both higher AI dependence and lower critical thinking scores than older participants; higher educational attainment moderated (softened) the negative AI effect, predicting better critical thinking scores even among frequent AI users. *(Note: the journal issued a [correction](https://www.mdpi.com/2075-4698/15/9/252) in September 2025 fixing a duplicated table; the author states the correction does not change the sample size, statistics, or conclusions above.)*

### The Common Thread

Across both studies (and echoed in the [Frontiers "cognitive paradox" review](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1550621/full)), the mechanism is not "AI makes you dumber" in a direct sense — it's that **uncritical, high-trust, low-effort AI use habituates a pattern of accepting output rather than interrogating it**, and that pattern generalizes into a broader posture of reduced scrutiny. This is now often described in the literature as a pipeline: repeated uncritical acceptance → cognitive offloading → metacognitive laziness → AI overreliance → AI overdependence → skill deskilling — with each stage more entrenched and harder to reverse than the last.

---

## 4. Not All Findings Are Negative: Augmentation, Creativity, and "Tools for Thought"

It would be a distortion to summarize the literature as uniformly alarmist. A 2026 Frontiers in Psychology systematic review, **["Amplifier or substitute? A systematic review of generative AI's impact on higher-order cognitive skills among university students,"](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1863931/full)** found:
- **Positive effects in 36 of 89 studies reviewed (40.4%)**, mixed/conditional effects in 21 (23.6%), and negative effects in only 15 (16.9%).
- **Problem-solving showed the most consistently positive empirical signal** of any cognitive domain studied.
- Creative-thinking gains were substantial in controlled studies — Urban et al. (2024, cited in the review) found significant improvements in solution quality (d = 0.69), elaboration (d = 0.61), and originality (d = 0.55) when GenAI was used as a creativity aid.

Microsoft Research's CHI 2025 workshop synthesis, **["Understanding, Protecting, and Augmenting Human Cognition with Generative AI"](https://arxiv.org/pdf/2508.21036)**, reframes the entire design question: rather than asking whether AI helps or hurts cognition, the field is shifting toward designing **"tools for thought"** — systems deliberately built to provoke critical thinking, provide Socratic-style tutoring, or scaffold sensemaking, instead of systems optimized purely for task completion speed. This reframing treats the cognitive effect as a *design choice embedded in the product*, not an inevitable side effect of the underlying model.

### The Individual vs. Collective Paradox

One of the more counter-intuitive findings comes from *Science Advances*: **["Generative AI enhances individual creativity but reduces the collective diversity of novel content."](https://www.science.org/doi/10.1126/sciadv.adn5290)** Each person who uses GenAI to brainstorm produces better individual output than they would unaided — but because many people are drawing from the same underlying model, the *population* of ideas becomes more homogeneous. Individually rational adoption can still produce a collectively worse outcome: more good ideas per person, fewer distinct ideas overall. This finding foreshadows the societal-scale argument in Section 5.

---

## 5. The Societal Question: Could AI Cause "Knowledge Collapse"?

The most theoretically ambitious paper in this space is by Daron Acemoglu, Dingwen Kong, and Asuman Ozdaglar (MIT): **["AI, Human Cognition and Knowledge Collapse"](https://economics.mit.edu/sites/default/files/2026-02/AI,%20Human%20Cognition%20and%20Knowledge%20Collapse%2002-20-26.pdf)** ([NBER Working Paper 34910](https://www.nber.org/papers/w34910)).

**The model:** Good decisions require combining two complementary inputs — society's shared, general knowledge stock, and an individual's private, context-specific knowledge. Historically, human effort in solving problems has produced *both* a private signal (helping the individual) and a "thin" public signal that, aggregated across many people, replenishes the general knowledge commons (think: published research, shared professional norms, public discourse).

**The mechanism of concern:** As agentic AI recommendations become accurate enough, individuals rationally stop exerting the effort that used to generate that public signal — they just take the AI's answer. Because that public signal was the *only* thing replenishing the general-knowledge commons, the commons stops being replenished. The model shows that once human effort is sufficiently elastic and AI accuracy crosses a threshold, **the system can tip into a "knowledge-collapse" steady state where general knowledge eventually vanishes — even though every individual, in every single interaction, is getting excellent personalized advice.** This is the theoretical companion to the Science Advances homogenization finding above: both describe a wedge between individual-level benefit and population-level knowledge health.

**A genuinely counter-intuitive policy result:** welfare is *non-monotone* in AI accuracy — meaning there is an interior, welfare-maximizing level of AI precision, and pushing accuracy higher without bound can eventually reduce total welfare by accelerating knowledge collapse. The paper's proposed lever isn't banning AI but investing in **aggregation capacity** — better mechanisms for pooling and sharing the general knowledge that's still being generated, which unambiguously raises welfare and resilience regardless of AI accuracy.

**A live academic pushback:** Not everyone accepts the model's framing. In a detailed critique, [**"Acemoglu et al (2026) are wrong about AI & Human Cognition,"**](https://carlolc.substack.com/p/acemoglu-et-al-2026-are-wrong-about) Carlo Ludovico Cordasco argues the model's core flaw is treating the *forms* of knowledge and competence as fixed — it doesn't allow for new competencies or new knowledge-production functions to emerge in response to the technology itself. Cordasco points to historical precedent: cockpit automation didn't just erode pilots' manual skills, it also produced **Crew Resource Management**, an entirely new discipline now used across healthcare and emergency services; the printing press didn't just disrupt scribal knowledge transmission, it created the scientific journal as a wholly new knowledge form nobody in 1440 could have modeled in advance. His conclusion: deliberately limiting AI's precision to preserve old knowledge-production pathways (what the original paper calls "garbling") may suppress exactly the experimentation that produces the next unforeseeable leap, and "designing for flexibility" with capable AI is preferable to deliberately degrading it.

This is a live, unresolved debate between a formal economic model predicting collapse under specific elasticity conditions, and a historically grounded critique arguing that technological disruption reliably produces new, unmodelable forms of knowledge that a static model can't see coming.

---

## 6. Emotional and Social Cognition: A Related but Distinct Risk

Adjacent to reasoning and knowledge, a separate 2025–2026 research thread examines AI's effect on *emotional* cognition and social skills:

- **Scale of the phenomenon:** These come from two separate, sequential efforts, not one study. First, a **March 2025 joint OpenAI/MIT Media Lab research collaboration** ([arXiv:2504.03888](https://arxiv.org/abs/2504.03888)) analyzed nearly **40 million ChatGPT interactions** alongside a ~1,000-person randomized trial to study affective use patterns. Separately, an **October 2025 OpenAI-only analysis** (applied across OpenAI's full user base, without MIT involvement) found approximately **0.15% of active weekly users** show patterns consistent with heightened emotional reliance on the chatbot — which, at OpenAI's ~800 million weekly-active-user scale at the time, works out to roughly **1.2 million people**, not the smaller figures sometimes circulated in secondary coverage (as reported via [APA Monitor](https://www.apa.org/monitor/2026/01-02/trends-digital-ai-relationships-emotional-connection) and [TechPolicy.Press](https://www.techpolicy.press/new-research-sheds-light-on-ai-companions/)).
- **Longitudinal signal:** A two-year Finnish study of nearly 2,000 chatbot users found that while AI companionship can reduce short-term loneliness, **long-term use is associated with increased anxiety and depression** in a subset of users.
- **Mechanism:** Researchers (e.g., in [ScienceDirect's "Healthy bonds or pathological ties?"](https://www.sciencedirect.com/science/article/abs/pii/S0736585326000407)) frame the risk through rumination and metacognitive awareness — AI's unconditional availability and compliance can make navigating the friction of real human relationships feel comparatively harder, particularly for children and older adults who form attachments more readily.
- **Regulatory response:** China's Cyberspace Administration, jointly with several other ministries, issued the "Interim Measures for the Management of AI Human-Like Interaction Services" around **April 2026**; the rules — targeting emotional dependency on AI companion products specifically, via mandated detection of dependency signs, crisis-intervention triggers, and anti-addiction measures — **took effect July 15, 2026**, prompting major Chinese platforms to suspend some companion features. It's one of the first concrete government interventions aimed at this cognitive/emotional risk category rather than at misinformation or safety failures.

This strand is mechanistically distinct from the reasoning/critical-thinking research above but shares its core structural finding: the risk concentrates in passive, high-frequency, low-friction use, and is smaller (though not absent) among people who engage more deliberately and with greater self-awareness.

---

## 7. Synthesis: What the Evidence Actually Supports

Pulling the threads together, five claims are reasonably well supported by current evidence, and one is a serious open question:

1. **LLM reasoning is not human reasoning wearing a mask.** It frequently reaches the same answers via different, more brittle mechanisms, and it underuses the meta-cognitive monitoring that makes human reasoning robust to novel problems. (Section 1)
2. **Passive AI use measurably weakens neural engagement, memory, and sense of ownership over one's own work**, at least in the short-term lab evidence available so far (MIT Media Lab), and can degrade real, high-stakes professional skills over time (physician polyp detection). (Section 2)
3. **The critical thinking effect is confidence-mediated, not deterministic**: trusting the tool more than yourself predicts decline; trusting yourself more than the tool predicts resilience or even improvement, and the type of thinking shifts (toward verification) rather than simply disappearing. (Section 3)
4. **Active, structured, metacognitively engaged use produces real cognitive augmentation** — better problem-solving, measurable creativity gains — and the design of the AI tool itself (whether it's built to provoke thinking or to just finish the task) is a major causal factor, not a side detail. (Section 4)
5. **Individual-level gains can coexist with population-level harm** — both empirically (creativity homogenization) and theoretically (the knowledge-collapse model) — meaning that "is this good for me" and "is this good for us" can have opposite answers at the same time. (Sections 4–5)
6. **Open question:** whether the long-run trajectory bends toward Acemoglu et al.'s knowledge-collapse steady state or toward Cordasco's history-informed prediction of unforeseeable new knowledge forms emerging from the disruption — is not resolvable from current data and is likely to be one of the defining empirical questions of the next decade of this research.

The practical implication for anyone building or deploying generative AI tools — not just studying them — is that the cognitive outcome is substantially a *design and usage-pattern* variable, not an inherent property of the technology: friction that provokes verification, interfaces that surface uncertainty, and defaults that reward deliberate engagement over one-click completion appear, across this literature, to be the difference between augmentation and debt.

---

## Sources

- [MIT Media Lab — "Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task"](https://www.media.mit.edu/publications/your-brain-on-chatgpt/) / [arXiv:2506.08872](https://arxiv.org/abs/2506.08872)
- [The Conversation — "MIT researchers say using ChatGPT can rot your brain. The truth is a little more complicated"](https://theconversation.com/mit-researchers-say-using-chatgpt-can-rot-your-brain-the-truth-is-a-little-more-complicated-259450)
- [arXiv 2511.16660 — "Cognitive Foundations for Reasoning and Their Manifestation in LLMs"](https://arxiv.org/abs/2511.16660)
- [arXiv 2602.06176 — "Large Language Model Reasoning Failures"](https://arxiv.org/pdf/2602.06176)
- [arXiv 2602.16085 — "Language Statistics and False Belief Reasoning: Evidence from 41 Open-Weight LMs"](https://arxiv.org/pdf/2602.16085)
- [Princeton / Nature Human Behaviour — "Testing theory of mind in large language models and humans"](https://collaborate.princeton.edu/en/publications/testing-theory-of-mind-in-large-language-models-and-humans/)
- [Microsoft Research / CHI 2025 — "The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers"](https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/)
- [MDPI Societies 2025 — Gerlich, "AI Tools in Society: Impacts on Cognitive Offloading and the Future of Critical Thinking"](https://www.mdpi.com/2075-4698/15/1/6) (see also [correction notice](https://www.mdpi.com/2075-4698/15/9/252))
- [arXiv:2504.03888 — OpenAI/MIT Media Lab, "How AI and Human Behaviors Shape Psychosocial Effects of Chatbot Use"](https://arxiv.org/abs/2504.03888) (the 40-million-interaction study)
- [Frontiers in Psychology — "The cognitive paradox of AI in education: between enhancement and erosion"](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1550621/full)
- [Frontiers in Psychology 2026 — "Amplifier or substitute? A systematic review of generative AI's impact on higher-order cognitive skills among university students"](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1863931/full)
- [arXiv 2508.21036 — "Understanding, Protecting, and Augmenting Human Cognition with Generative AI: A Synthesis of the CHI 2025 Tools for Thought Workshop"](https://arxiv.org/pdf/2508.21036)
- [Science Advances — "Generative AI enhances individual creativity but reduces the collective diversity of novel content"](https://www.science.org/doi/10.1126/sciadv.adn5290)
- [APA Monitor, July/Aug 2026 — "How AI is reshaping human skills and thinking"](https://www.apa.org/monitor/2026/07-08/ai-job-skills-thinking)
- [MIT Economics / NBER — Acemoglu, Kong, Ozdaglar, "AI, Human Cognition and Knowledge Collapse"](https://economics.mit.edu/sites/default/files/2026-02/AI,%20Human%20Cognition%20and%20Knowledge%20Collapse%2002-20-26.pdf) / [NBER w34910](https://www.nber.org/papers/w34910)
- [Carlo Ludovico Cordasco (Substack) — "Acemoglu et al (2026) are wrong about AI & Human Cognition"](https://carlolc.substack.com/p/acemoglu-et-al-2026-are-wrong-about)
- [APA Monitor, Jan/Feb 2026 — "AI chatbots and digital companions are reshaping emotional connection"](https://www.apa.org/monitor/2026/01-02/trends-digital-ai-relationships-emotional-connection)
- [Tech Policy Press — "New Research Sheds Light on AI 'Companions'"](https://www.techpolicy.press/new-research-sheds-light-on-ai-companions/)
- [ScienceDirect — "Healthy bonds or pathological ties? Unpacking emotional dependence on AI through rumination and metacognitive awareness"](https://www.sciencedirect.com/science/article/abs/pii/S0736585326000407)
- [China.org.cn — "New rules to reduce emotional dependency on AI"](http://www.china.org.cn/2026-07/27/content_118619732.shtml)

> **Caveat on recency:** Several sources dated 2026 (including the Acemoglu/Kong/Ozdaglar paper, the APA Monitor features, and the Frontiers 2026 review) reflect very recent preprints/publications relative to this document's generation date and have not had extended time to accumulate independent replication or peer critique. The MIT Media Lab EEG study in particular is a high-profile but small (n=54) first study, confirmed here directly against the authors' own preprint text (still marked "under review," not yet peer-reviewed/journal-published as of this writing); treat its findings as a strong initial signal rather than a settled result. The 0.15%/emotional-reliance figure in Section 6 comes from an OpenAI company blog post, not a peer-reviewed study.
