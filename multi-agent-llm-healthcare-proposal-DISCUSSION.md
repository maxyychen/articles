# Process Mining-Driven Multi-Agent LLM Implementation for Healthcare Workflow Optimization

## Executive Summary

This research addresses a critical gap in healthcare AI implementation: while Large Language Models (LLMs) show promise for clinical tasks, current single-agent approaches fail to address systemic workflow challenges. This proposal presents a novel framework integrating Object-Centric Process Mining (OCPM) with multi-agent LLM systems to enable data-driven, trustworthy AI deployment in healthcare workflows.

**Key Innovation**: **Explainability-as-Coordination** — a paradigm shift treating explainability as an inter-agent coordination protocol rather than post-hoc output, addressing fundamental trust challenges in distributed AI decision-making.

---

## 1. Research Problem and Motivation

### 1.1 The Healthcare Workflow Challenge

Healthcare delivery involves complex interdisciplinary coordination across multiple specialties, departments, and information systems. Despite substantial health information technology investments, clinical workflows remain plagued by:

- **Operational inefficiencies**: Bottlenecks, communication gaps, and resource misallocation
- **Clinical quality issues**: Suboptimal adherence to evidence-based guidelines (30-70% adherence rates)
- **Human costs**: Clinician burnout from documentation burden and administrative overhead
- **Patient safety**: Delayed care and preventable adverse outcomes

These challenges are fundamentally **workflow-level problems** requiring systemic solutions, not isolated point interventions.

### 1.2 The AI Implementation Gap

Recent Large Language Models (ChatGPT, Claude, Gemini) demonstrate remarkable capabilities in medical question answering, clinical note generation, and diagnostic reasoning. However, current healthcare AI applications face critical limitations:

**Technical Limitations**:
- Single-task focus without workflow integration
- Hallucinations and lack of explainability
- Insufficient validation for high-stakes clinical decisions
- Privacy concerns with cloud-based models

**Deployment Limitations**:
- No systematic methodology for identifying where to deploy AI
- Lack of validated integration approaches for existing workflows
- Unclear mechanisms for ensuring reliability and trust
- Limited understanding of coordination requirements for multi-agent systems

**Adoption Barriers**:
- Workflow disruption and perceived loss of clinical autonomy
- Insufficient transparency and explainability
- Concerns about liability and accountability

### 1.3 Multi-Agent Systems as a Solution

Multi-agent systems, where specialized AI agents collaborate to accomplish complex tasks, offer a promising paradigm for healthcare process optimization. However, **four critical gaps** remain:

1. **Implementation Gap**: Lack of validated methodologies for integrating multi-agent systems into established clinical workflows without disruption

2. **Optimization Gap**: Absence of systematic, data-driven approaches to identify where and how to deploy agents for maximum impact

3. **Quality Gap**: Limited understanding of how multi-agent systems can enforce evidence-based guideline adherence while respecting clinical judgment

4. **Trust Gap**: Unresolved challenges in ensuring reliability, transparency, and explainability when multiple AI agents contribute to recommendations in high-stakes healthcare environments

### 1.4 Research Questions

**Primary Research Question**:
How can multi-agent LLM systems be practically implemented in existing healthcare workflows to improve process efficiency and clinical decision quality while maintaining minimal workflow disruption and ensuring clinician trust?

**Secondary Research Questions**:
1. How can Object-Centric Process Mining inform systematic agent design and placement within complex clinical workflows?
2. What coordination protocols enable effective multi-agent collaboration while maintaining explainability in safety-critical contexts?
3. What mechanisms build distributed trust when multiple agents contribute to clinical recommendations?
4. What organizational and individual factors influence clinician acceptance of multi-agent clinical decision support systems?
5. How can concrete use cases (e.g., guideline adherence monitoring) validate the framework's effectiveness?

### 1.5 Research Aims and Objectives

**Overall Aim**:
To develop and validate a comprehensive, data-driven framework for implementing trustworthy multi-agent LLM systems in healthcare workflows that optimizes operational efficiency and clinical decision quality.

**Specific Objectives**:
1. **OCPM-Driven Agent Design**: Develop a process mining methodology for analyzing workflows and systematically identifying optimal agent types, roles, and placement strategies
2. **Multi-Agent Architecture**: Design and implement a multi-agent system with specialized agents addressing workflow pain points
3. **Trust and Safety Mechanisms**: Implement and evaluate explainability-as-coordination, hallucination prevention, and distributed responsibility attribution
4. **Clinical Use Case Validation**: Demonstrate framework through automated guideline extraction and adherence monitoring
5. **Generalizable Framework**: Produce validated frameworks and best practices for multi-agent healthcare system implementation

---

## 2. Novel Theoretical Contributions

### 2.1 Explainability-as-Coordination Framework

**The Distributed Trust Challenge**:

When multiple AI agents contribute to a clinical recommendation, how do clinicians:
- Understand the collective reasoning process?
- Attribute responsibility and assess reliability?
- Maintain appropriate skepticism and clinical judgment?

**Current Limitations**:
- Traditional explainability treats transparency as post-hoc output for humans
- Multi-agent systems struggle with distributed accountability
- Clinicians cannot practically trace reasoning through each individual agent

**Our Paradigm Shift**:

Rather than treating explainability solely as output for human users, we conceptualize it as an **inter-agent coordination protocol**:

**Core Principles**:
1. **Peer Justification**: Agents communicate decision rationales to each other as part of coordination (not just to humans)
2. **Explainability Agent**: A specialized coordinator synthesizes distributed reasoning into coherent, clinically interpretable narratives
3. **Coordination-Embedded Transparency**: Explanation generation becomes part of the coordination mechanism itself—agents must justify recommendations to peers before presenting to clinicians
4. **Unified Accountability**: The Explainability Agent provides unified responsibility attribution while maintaining traceable links to source agents

**Benefits**:
- Transparency emerges naturally from agent interaction patterns rather than being retrofitted
- Clinicians receive coherent explanations without tracing individual agent reasoning
- Trust calibration becomes manageable through unified interface
- Distributed accountability maintains traceable attribution

**Impact**: This addresses a fundamental challenge in multi-agent AI systems applicable beyond healthcare to any safety-critical domain requiring distributed decision-making.

### 2.2 OCPM-to-Agent Design Pipeline

**The Agent Design Problem**:

Current multi-agent systems lack systematic methodologies for:
- Determining what agent types are needed
- Defining agent roles and responsibilities
- Justifying agent placement within workflows
- Ensuring agents address actual workflow pain points

**Our Solution**:

A data-driven pipeline translating Object-Centric Process Mining insights into multi-agent architectures:

**Pipeline Stages**:
1. **OCPM Discovery**: Extract object types, interactions, and process patterns from healthcare event logs
2. **Bottleneck Analysis**: Identify workflow inefficiencies, delays, and quality gaps using OCPM analytics
3. **Agent Type Mapping**: Systematically map object classes to specialized agent types (e.g., patient objects → patient communication agents; task objects → coordination agents)
4. **Role Definition**: Define agent responsibilities based on identified pain points and improvement opportunities
5. **Placement Strategy**: Position agents at optimal intervention points identified through process mining
6. **Coordination Protocol Design**: Structure inter-agent communication based on discovered object interactions

**Impact**:
- Bridges descriptive analytics (process mining) with prescriptive interventions (multi-agent AI)
- Provides empirical justification for agent design decisions
- Enables reproducible, systematic agent architecture development
- Grounds AI deployment in actual workflow patterns rather than assumptions

---

## 3. Theoretical Foundation and Literature Review

### 3.1 Integrated Theoretical Framework

This research synthesizes multiple theoretical perspectives:

**1. Object-Centric Process Mining (OCPM)** [van der Aalst, 2023]
- Enables natural mapping from object types (patients, tasks, departments, clinicians) to specialized agent types
- Serves as foundation for systematic, justified agent design and placement
- **Research Gap**: Limited integration with AI-driven interventions for real-time workflow optimization

**2. Multi-Agent Coordination Theory** [Wooldridge, 2021; Durfee, 2019]
- Establishes principles for agent communication protocols and collaborative problem-solving
- Frames systems as distributed cognitive architectures where intelligence emerges from interactions
- **Research Gap**: Validated frameworks for safety-critical healthcare with explainability requirements

**3. Distributed Trust Framework** [Glikson & Woolley, 2020]
- Extends human-AI trust theory to multi-agent contexts
- Distinguishes performance trust (capability) from purpose trust (intention)
- **Research Gap**: Mechanisms for building distributed trust through transparency and oversight

**4. Implementation Science (CFIR)** [Damschroder et al., 2009]
- Provides systematic framework for evaluating adoption barriers across five domains
- Guides implementation strategy addressing organizational, individual, and intervention factors
- **Research Gap**: Application to multi-agent AI system deployment

**5. Supporting Theories**:
- **Sociotechnical Systems Theory**: Holistic consideration of people, processes, and technology
- **Evidence-Based Medicine**: Grounding interventions in systematic evidence synthesis
- **Human-AI Collaboration**: Emphasizing complementary strengths rather than full automation

### 3.2 Process Mining in Healthcare

**Current State**:
Process mining successfully analyzes patient pathways, identifies bottlenecks, and optimizes resource allocation in healthcare [Davari et al., 2024; Fernández-Llatas et al., 2020].

**Object-Centric Process Mining (OCPM)** [van der Aalst, 2023]:
- Models multiple interacting object types addressing many-to-many relationships
- Provides natural representation of complex clinical workflows
- Offers foundation for multi-agent system design

**Research Gap**: Existing research focuses on descriptive analytics rather than prescriptive interventions. Limited integration with AI-driven real-time optimization.

### 3.3 Large Language Models in Healthcare

**Current State**:
Recent LLMs demonstrate capabilities in medical question answering, clinical note generation, and diagnostic reasoning [Chen et al., 2025; Zhang et al., 2025]. Applications remain single-task focused without workflow integration.

**Critical Concerns**: Hallucinations, lack of explainability, insufficient validation, privacy concerns.

**Enabling Technology**:
Hospitals can now deploy affordable LLM inference systems through hybrid architectures combining:
- **On-premises servers**: Centralized control over sensitive data within hospital infrastructure
- **Edge-AI devices**: Real-time processing at point of care on medical devices and bedside systems

This hybrid approach enables sophisticated multi-agent AI while maintaining strict data governance and regulatory compliance (HIPAA, GDPR).

**Research Gap**: Systematic approaches to deploying LLMs within clinical workflows with safety guardrails and human oversight remain underdeveloped.

### 3.4 Multi-Agent Systems

**Theoretical Foundation**: Established principles for agent coordination, communication protocols, and collaborative problem-solving [Wooldridge, 2021; Durfee, 2019].

**Healthcare Applications**: Remain limited, with most research focusing on simulation rather than real-world deployment [Poon et al., 2024; Kim et al., 2024].

**Key Challenges**: Ensuring reliable coordination in safety-critical contexts, managing complexity, maintaining explainability, adapting coordination protocols for LLM-based agents requiring auditability.

**Research Gap**: Validated frameworks for deploying multi-agent LLM systems in safety-critical healthcare environments with trust and transparency mechanisms.

### 3.5 Clinical Practice Guidelines and Conformance Checking

**The Guideline Implementation Problem**:
- Adherence rates: 30-70% depending on guideline and context [Holder et al., 2024]
- Existing CDSS require extensive manual guideline encoding
- Systems struggle with complex, evolving recommendations

**Process Mining Conformance Checking** [Rojas et al., 2016]:
- Measures actual vs. intended process execution
- Quantifies guideline adherence in clinical pathways

**Current Limitations**: Requires pre-defined models, no real-time intervention, no automated guideline operationalization.

**Research Gap**: Automated methods for extracting, structuring, and monitoring clinical protocols in real-time workflows with closed-loop conformance checking.

### 3.6 Trust and Adoption in Clinical AI

**Trust Requirements**: Clinician trust depends on reliability, transparency, and workflow alignment [Kumpati et al., 2024].

**Adoption Barriers**: Workflow disruption, perceived loss of autonomy, liability concerns.

**Distributed Trust Challenge** [Glikson & Woolley, 2020]: In multi-agent systems, clinicians must trust not only individual agents but also inter-agent coordination, making responsibility attribution complex.

**Implementation Science**: CFIR [Damschroder et al., 2009] offers systematic approach across five domains but has not been applied to multi-agent AI deployment.

**Research Gap**: Mechanisms for building distributed trust with systematic evaluation frameworks addressing organizational adoption factors.

---

## 4. Expected Contributions and Impact

### 4.1 Theoretical Contributions

**To Multi-Agent Systems Research**:

1. **Explainability-as-Coordination Framework**
   - Novel paradigm with empirical validation in safety-critical contexts
   - Addresses distributed trust and accountability challenges
   - Generalizable to other multi-agent domains requiring transparency

2. **OCPM-to-Agent Design Pipeline**
   - Systematic methodology bridging descriptive analytics with prescriptive interventions
   - Data-driven justification for agent placement and role definition
   - Reproducible framework for agent system development

3. **Distributed Trust Mechanisms**
   - Extension of trust framework to multi-agent contexts
   - Empirical evidence on trust calibration with multiple AI agents

4. **Safety-Critical Coordination Protocols**
   - Validated protocols balancing efficiency with explainability
   - Adaptation for LLM-based agents requiring auditability

**To Healthcare Informatics**:

1. **OCPM Integration with Prescriptive AI**
   - First framework connecting object-centric process mining with real-time multi-agent interventions
   - Closed-loop quality assurance integrating conformance checking with agent monitoring

2. **CFIR-Based Adoption Framework for Multi-Agent AI**
   - Systematic application of implementation science to multi-agent systems
   - Evidence-based change management strategies for clinical AI

3. **Clinical Protocol Operationalization Theory**
   - Framework for automated guideline extraction and structuring using LLMs
   - Integration with FHIR standards for cross-platform deployment

### 4.2 Practical Contributions

**Immediate Healthcare Impact**:

1. **Improved Clinical Quality**
   - Enhanced guideline adherence with measurable patient outcome benefits
   - Real-time conformance monitoring with severity-tiered alerting
   - Evidence-based decision support integrated into workflows

2. **Operational Efficiency**
   - Reduced clinician documentation burden
   - Automated care coordination and communication
   - Optimized resource allocation based on process mining insights

3. **Technical Infrastructure**
   - **FHIR-compliant multi-agent framework** enabling rapid deployment across diverse EHR platforms
   - Standards-based interoperability reducing vendor lock-in
   - Hybrid on-premises/edge-AI architecture addressing privacy concerns
   - LLM-based pipeline for converting unstructured protocols to structured representations

4. **Trust and Safety Mechanisms**
   - Comprehensive hallucination detection and consistency checking
   - Audit trails with distributed responsibility attribution
   - Explainability interfaces designed for clinical comprehension

**Impact on Healthcare Organizations**:
- Validated roadmap from isolated AI pilots to systematic, workflow-integrated implementations
- Framework for data-driven AI investment decisions
- Reduced implementation costs through standards-based architecture

**Generalizable Insights**:
- Evidence-based understanding of clinician adoption factors
- Validated change management strategies for clinical AI
- Mixed-methods evaluation toolkit spanning operational, clinical, trust, and adoption dimensions

**Impact Beyond Healthcare**:
- Practical solutions to multi-agent challenges (trust, coordination, explainability) generalizable to other safety-critical domains
- Framework for responsible AI deployment balancing innovation with safety

**Policy and Regulatory Impact**:
- Evidence informing AI governance frameworks and safety standards
- Case study for responsible AI deployment in regulated industries

---

## 5. Research Approach (High-Level)

### 5.1 Overall Strategy

**Design**: Mixed-methods research combining quantitative workflow analysis and clinical outcomes with qualitative evaluation of clinician experiences and adoption factors.

**Phased Approach**:

**Phase 1: OCPM-Driven Workflow Analysis and Agent Design**
- Analyze clinical workflows using Object-Centric Process Mining
- Identify bottlenecks, inefficiencies, and quality gaps
- Systematically design multi-agent architecture based on insights
- Engage stakeholders to validate findings and gather requirements

**Phase 2: Multi-Agent System Development**
- Implement multi-agent architecture with specialized LLM-based agents
- Develop Explainability-as-Coordination framework
- Build trust and safety mechanisms (hallucination detection, audit trails)
- Create guideline extraction pipeline as validation use case
- Ensure FHIR-based interoperability with EHR systems

**Phase 3: Pilot Deployment and Evaluation**
- Staged rollout (shadow → advisory → integrated modes)
- Quantitative evaluation: operational efficiency, clinical quality, system performance
- Qualitative evaluation: trust, explainability, adoption factors (CFIR-guided)
- Mixed-methods analysis with iterative refinement

**Phase 4: Framework Generalization**
- Document comprehensive methodology and best practices
- Develop open-source toolkit and implementation resources
- Assess scalability and generalizability to other clinical contexts
- Disseminate findings to academic and practitioner communities

### 5.2 Key Validation Approach

**Use Case**: Automated guideline extraction and adherence monitoring
- Demonstrates practical application of multi-agent framework
- Provides concrete metrics for evaluation (adherence rates, clinical outcomes)
- Addresses real clinical need with clear value proposition

**Evaluation Dimensions**:
1. **Operational**: Process efficiency, documentation time, coordination overhead
2. **Clinical**: Guideline adherence, recommendation appropriateness, patient outcomes
3. **Trust**: Clinician trust in recommendations, perceived explainability, trust calibration
4. **Adoption**: CFIR-based assessment of organizational and individual factors

---

## 6. Key Feasibility Considerations

### 6.1 Technical Feasibility

**Enabling Factors**:
- Open-source LLMs (Llama, Mistral) available for on-premises deployment
- FHIR standards mature and widely adopted in healthcare
- Process mining tools (PM4Py, Celonis) capable of OCPM analysis
- Multi-agent frameworks (LangChain, AutoGen) provide development foundations

**Key Challenges and Mitigation**:
- **EHR integration complexity**: Adopt FHIR standards for vendor-agnostic interoperability; engage EHR vendor early
- **LLM hallucinations**: Multi-layer fact verification, confidence scoring, mandatory human review for low-confidence outputs
- **System performance**: Load testing, hybrid on-premises/edge architecture, auto-scaling capabilities

### 6.2 Organizational Feasibility

**Enabling Factors**:
- Growing healthcare interest in AI-driven workflow optimization
- Process mining increasingly adopted in healthcare organizations
- Strong potential for industry partnerships given practical focus

**Key Challenges and Mitigation**:
- **Clinician resistance**: Apply CFIR-guided implementation strategy addressing barriers across all five domains; early stakeholder engagement; clinical champions
- **Workflow disruption**: Staged rollout (shadow mode first); extensive training; parallel operations initially
- **Clinical safety**: Human verification at all decision points; extensive pre-deployment testing; clear escalation procedures; incident reporting

### 6.3 Research Limitations

**Single-site initial deployment**: Findings may not generalize, but CFIR framework enables systematic assessment of transferability; framework designed for adaptability.

**Limited temporal scope**: Focus on proximal outcomes measurable within PhD timeframe; design for longitudinal follow-up.

**Use case specificity**: Framework designed for generalizability beyond guideline adherence; toolkit enables adaptation to other contexts.

---

## 7. Timeline (High-Level)

**Year 1**: Literature review completion, partnership establishment, OCPM workflow analysis, agent design pipeline development

**Year 2**: Multi-agent system implementation, Explainability-as-Coordination framework development, safety mechanisms, integration testing

**Year 3**: Pilot deployment (shadow → advisory modes), evaluation, data analysis, findings synthesis

**Year 4** (if applicable): Framework generalization, toolkit development, dissertation writing, dissemination

---

## 8. Conclusion and Discussion Points

This research addresses a critical gap at the intersection of healthcare delivery, artificial intelligence, and implementation science. By integrating Object-Centric Process Mining with multi-agent LLM systems, we provide a systematic, data-driven approach to deploying trustworthy AI in complex clinical workflows.

**Key Innovations**:

1. **Explainability-as-Coordination**: Paradigm shift addressing distributed trust challenges unique to multi-agent systems

2. **OCPM-to-Agent Pipeline**: Systematic methodology bridging descriptive process analytics with prescriptive multi-agent interventions

3. **CFIR-Based Multi-Agent Adoption Framework**: Application of implementation science to multi-agent AI deployment

**Expected Impact**:

This research will produce validated frameworks, open-source tools, and evidence-based best practices enabling healthcare organizations to move beyond isolated AI pilots toward systematic, workflow-integrated implementations. By addressing fundamental challenges in trust, coordination, and explainability, the work contributes to multi-agent systems research broadly, with implications for any safety-critical domain requiring collaborative AI decision-making.

---

## Discussion Questions for Supervisor

1. **Research Direction**: Does this align with the research group's focus and strategic priorities?

2. **Scope**: This is ambitious for a PhD. Which aspects would you prioritize if narrowing is needed?
   - Focus on theoretical contributions (Explainability-as-Coordination) with simpler validation?
   - Focus on practical implementation (OCPM-to-Agent pipeline) with less novel theory?
   - Alternative scoping suggestions?

3. **Partnerships**: Do you have existing healthcare collaborations or suggestions for partnership development? This research requires EHR access and clinical site engagement.

4. **Methodological Priorities**: What evaluation approaches are most important for demonstrating impact?
   - Technical validation (system performance, safety mechanisms)?
   - Clinical validation (outcomes, guideline adherence)?
   - Trust and adoption (CFIR-based assessment)?

5. **Collaboration**: Should I involve co-supervisors with clinical informatics or implementation science expertise?

6. **Funding**: Are there grant opportunities to pursue for infrastructure costs (LLM servers, EHR integration)?

7. **Publication Strategy**: What venues should I target? Healthcare informatics (JAMIA, NPJ Digital Medicine), multi-agent systems (AAMAS), implementation science, or a mix?

8. **Timeline Realism**: Does the 3-4 year timeline seem achievable given infrastructure and partnership needs?

---

## References

### Process Mining in Healthcare

1. Davari, H., et al. (2024). "Optimizing emergency department efficiency: a comparative analysis of process mining and simulation models to mitigate overcrowding and waiting times." *BMC Medical Informatics and Decision Making*, 24, Article 702.

2. Fernández-Llatas, C., et al. (2020). "Process Mining-Supported Emergency Room Process Performance Indicators." *International Journal of Environmental Research and Public Health*, 17(18), 6574.

3. van der Aalst, W. M. P. (2023). "Object-Centric Process Mining: Unraveling the Fabric of Real Processes." *Mathematics*, 11(12), 2691.

4. van der Aalst, W. M. P. (2016). *Process Mining: Data Science in Action* (2nd ed.). Springer-Verlag Berlin Heidelberg.

### Multi-Agent LLM Systems in Healthcare

5. Chen, Z., et al. (2025). "Enhancing diagnostic capability with multi-agents conversational large language models." *npj Digital Medicine*, 8, Article 74.

6. Kim, H., Park, S., et al. (2024). "MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making." OpenReview.

7. Zhang, Y., et al. (2025). "A Survey of LLM-based Agents in Medicine: How far are we from Baymax?" *arXiv preprint* arXiv:2502.11211.

8. Poon, A. I., et al. (2024). "Multiagent AI Systems in Health Care: Envisioning Next-Generation Intelligence." *JMIR Medical Informatics*, 12, e62864.

### Multi-Agent Coordination Theory

9. Durfee, E. H. (2019). "Multiagent Coordination: Theory and Practice." *ACM Computing Surveys*, 52(5), Article 101.

10. Wooldridge, M. (2021). *An Introduction to MultiAgent Systems* (3rd ed.). Wiley.

### Trust in AI and Implementation Science

11. Glikson, E., & Woolley, A. W. (2020). "Human Trust in Artificial Intelligence: Review of Empirical Research." *Academy of Management Annals*, 14(2), 627-660.

12. Damschroder, L. J., et al. (2009). "Fostering implementation of health services research findings into practice: a consolidated framework for advancing implementation science." *Implementation Science*, 4, 50.

13. Greenhalgh, T., et al. (2017). "Beyond Adoption: A New Framework for Theorizing and Evaluating Nonadoption, Abandonment, and Challenges to the Scale-Up, Spread, and Sustainability of Health and Care Technologies." *Journal of Medical Internet Research*, 19(11), e367.

### Explainable AI and Trust in Healthcare

14. Kumpati, S., et al. (2024). "How Explainable Artificial Intelligence Can Increase or Decrease Clinicians' Trust in AI Applications in Health Care: Systematic Review." *JMIR AI*, 2024(1), e53207.

### Clinical Practice Guidelines

15. Holder, A. L., et al. (2024). "Sepsis Alert Systems, Mortality, and Adherence in Emergency Departments: A Systematic Review and Meta-Analysis." *Journal of Emergency Medicine*, 67(1), e78-e91.

16. Rojas, E., et al. (2016). "Process mining in healthcare: A literature review." *Journal of Biomedical Informatics*, 61, 224-236.

### Healthcare Interoperability Standards

17. HL7 International (2023). "FHIR R5 Specification: Fast Healthcare Interoperability Resources." http://hl7.org/fhir/R5/

18. Mandel, J. C., et al. (2016). "SMART on FHIR: a standards-based, interoperable apps platform for electronic health records." *Journal of the American Medical Informatics Association*, 23(5), 899-908.

---

*This proposal outline is intended as a discussion starter. Methodology details, evaluation frameworks, and implementation specifics can be refined based on supervisor feedback and partnership opportunities.*
