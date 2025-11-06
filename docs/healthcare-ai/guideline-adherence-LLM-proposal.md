# Multi-Agent LLM Framework for Automated AJCC Breast Cancer Staging and Treatment Guideline Conformance

## Executive Summary

Breast cancer staging using AJCC (American Joint Committee on Cancer) TNM criteria is foundational to treatment planning, yet manual staging is time-consuming, error-prone (31.8% clinical-pathological discordance rate [Weiss et al., 2019]), and struggles to incorporate evolving biomarker requirements. This research proposes a novel multi-agent LLM framework that automatically extracts AJCC breast cancer staging criteria and treatment guidelines from unstructured documents, structures them into FHIR-compliant computable representations, and performs real-time conformance checking to ensure accurate staging and guideline-concordant treatment recommendations.

**Key Innovation**: Integrating LLM-based AJCC guideline operationalization with process mining conformance checking to create a closed-loop system that automatically monitors staging accuracy and treatment adherence while providing explainable, auditable recommendations to oncology teams.

**Clinical Focus**: AJCC 8th Edition Breast Cancer Staging Manual and associated NCCN (National Comprehensive Cancer Network) treatment guidelines for breast cancer management.

---

## 1. Research Problem and Motivation

### 1.1 Breast Cancer Staging and Treatment: A Critical Challenge

Breast cancer is the most commonly diagnosed cancer in women worldwide. Accurate staging using AJCC TNM (Tumor, Node, Metastasis) criteria is fundamental to treatment planning, prognosis assessment, and clinical trial enrollment. However, significant challenges persist:

**The Staging Accuracy Problem**:
- **Clinical-pathological discordance**: 31.8% overall discordance between clinical and pathological staging (8.7% upstaging, 23.1% downstaging) among stage I-III breast cancer patients [Weiss et al., 2019]
- **Biomarker integration complexity**: AJCC 8th edition (2018) introduced prognostic staging incorporating biomarkers (ER, PR, HER2, Ki-67, Oncotype DX), creating substantial complexity
- **Manual staging burden**: Oncologists spend significant time extracting data from multiple sources (pathology reports, imaging, lab results) and applying complex staging algorithms
- **Staging errors**: Incorrect staging leads to inappropriate treatment (under-treatment or over-treatment), affecting patient outcomes and quality of life

**The Guideline Adherence Challenge**:
- **Treatment complexity**: NCCN guidelines for breast cancer exceed 250 pages with conditional treatment pathways based on stage, biomarkers, patient factors
- **Adherence variation**: Studies show 20-40% variation in guideline-concordant care across institutions
- **Knowledge burden**: Guidelines updated multiple times annually, clinicians struggle to stay current
- **Multidisciplinary coordination**: Breast cancer requires coordination across surgery, medical oncology, radiation oncology—each with guideline-specified recommendations

**Patient Impact**:
- **Survival**: Correct staging and guideline-concordant treatment significantly impact 5-year survival rates (98% for Stage I vs. 28% for Stage IV)
- **Quality of life**: Inappropriate treatment intensity (under or over-treatment) affects long-term morbidity
- **Healthcare costs**: Staging errors and non-guideline-concordant care increase costs through inappropriate procedures and delayed effective treatment

### 1.2 Limitations of Current Approaches

**Manual AJCC Staging**:
- **Time-consuming**: Extracting tumor characteristics from pathology reports, imaging, and lab results, then applying staging algorithms takes 15-30 minutes per patient
- **Error-prone**: Complex conditional logic (especially prognostic staging with biomarkers) leads to errors
- **Inconsistent**: Inter-rater variability in staging assessments
- **Difficult to update**: When AJCC updates staging criteria (every 7-8 years), re-training and process changes are required

**Existing Clinical Decision Support Systems (CDSS)**:
- **Manual encoding bottleneck**: Encoding AJCC staging algorithms and NCCN treatment guidelines requires months of knowledge engineering work
- **Vendor-specific**: Implementations tied to specific EHR platforms, limiting interoperability
- **Static**: Difficult to update as guidelines evolve
- **Limited adoption**: Due to encoding costs, many institutions lack comprehensive breast cancer CDSS

**Process Mining Conformance Checking**:
- **Retrospective only**: Identifies past deviations from pathways but no real-time intervention
- **Requires pre-defined models**: Manual creation of expected breast cancer care pathways
- **No automated guideline operationalization**: Cannot automatically extract AJCC/NCCN guidelines into checkable models

**Recent LLM Applications in Oncology**:
- Demonstrated capability for extracting tumor characteristics from pathology reports [Sharma et al., 2025; Kim et al., 2024]
- Some work on cancer staging assistance achieving 76-87% AJCC staging accuracy [Chen et al., 2025; Xu et al., 2024]
- Primarily single-agent, single-task approaches [Ibrahim et al., 2025]
- No systematic frameworks for complete staging pipeline (extraction → staging → treatment recommendation → conformance monitoring)
- Insufficient validation for clinical deployment

### 1.3 Why AJCC Breast Cancer Staging is Ideal for This Research

**1. Well-Structured Guidelines with Clear Validation**:
- AJCC provides comprehensive, detailed staging manual with explicit rules
- Gold-standard pathology reports available for validation
- Established metrics (staging accuracy, concordance with pathological staging)

**2. Significant Clinical Impact**:
- High-volume condition (2.3 million cases annually worldwide)
- Staging directly determines treatment decisions
- Measurable outcomes (survival, recurrence, treatment appropriateness)

**3. Appropriate Complexity**:
- Sufficiently complex to demonstrate framework capabilities (anatomic + prognostic staging, biomarker integration)
- Combines structured data (TNM values) with unstructured data (pathology narratives)

**4. Real Clinical Need**:
- Documented staging discordance and errors
- Treatment adherence variation across institutions
- Time burden on oncologists for manual staging
- Evolving guidelines requiring rapid operationalization

**5. Data Availability**:
- Pathology reports contain staging-relevant information
- EHR systems capture treatment decisions
- Cancer registries (SEER) provide population-level validation data
- Potential for collaboration with oncology departments

### 1.4 Research Gaps

**Gap 1: Automated AJCC Staging Extraction and Operationalization**
- No validated frameworks for automatically extracting AJCC staging criteria from unstructured text (AJCC manual, institutional protocols) and converting them into computable, testable representations

**Gap 2: LLM-Based Tumor Characteristic Extraction for Staging**
- Limited work on extracting structured tumor characteristics (T, N, M, biomarkers) from unstructured pathology reports and clinical notes for automated staging

**Gap 3: Real-Time Staging and Treatment Conformance Monitoring**
- No systems integrating automated staging with real-time conformance checking of treatment decisions against NCCN guidelines

**Gap 4: Explainable Multi-Agent Coordination for Oncology**
- When multiple agents collaborate (staging extraction, tumor characteristic extraction, treatment guideline monitoring, explanation), how do we ensure oncologists can understand, validate, and trust recommendations?

**Gap 5: Clinical Validation of Automated Staging**
- Limited clinical validation comparing automated LLM-based staging against gold-standard pathological staging and expert oncologist assessment

---

## 2. Research Questions and Objectives

### 2.1 Primary Research Question

**How can multi-agent LLM systems automatically extract AJCC breast cancer staging criteria and NCCN treatment guidelines, apply them to individual patients in real-time, and monitor conformance to improve staging accuracy and guideline-concordant care while maintaining oncologist trust?**

### 2.2 Secondary Research Questions

1. **AJCC Staging Extraction**: How accurately can LLM-based agents extract AJCC 8th edition breast cancer staging criteria (anatomic and prognostic staging) from the staging manual and convert them into FHIR-compliant, computable representations?

2. **Tumor Characteristic Extraction**: How accurately can LLMs extract structured tumor characteristics (T, N, M, ER, PR, HER2, Ki-67, grade, Oncotype DX) from unstructured pathology reports and clinical notes?

3. **Automated Staging**: Can the system accurately assign AJCC anatomic and prognostic stages based on extracted tumor characteristics, validated against gold-standard pathological staging?

4. **Treatment Guideline Operationalization**: How effectively can the system extract NCCN breast cancer treatment guidelines and monitor treatment decision conformance in real-time?

5. **Multi-Agent Coordination and Explainability**: What coordination protocols enable effective collaboration between specialized agents (staging extraction, tumor extraction, staging application, treatment monitoring, explanation) while maintaining transparency for oncologists?

6. **Clinical Integration and Trust**: What factors influence oncologist acceptance of automated staging and guideline recommendations? How does trust differ between automated vs. manually encoded systems?

7. **Clinical Impact**: Does the system improve staging accuracy, reduce staging time, increase guideline-concordant treatment, and (where measurable) improve patient outcomes?

### 2.3 Research Aims and Objectives

**Overall Aim**:
To develop and validate a multi-agent LLM framework that automates AJCC breast cancer staging and NCCN treatment guideline adherence monitoring, creating a closed-loop system that improves staging accuracy and evidence-based treatment while maintaining oncologist trust.

**Specific Objectives**:

1. **AJCC Staging Criteria Extraction Pipeline**
   - Develop multi-agent system for extracting AJCC 8th edition breast cancer staging criteria (T, N, M definitions, anatomic stage groups, prognostic stage groups)
   - Implement FHIR encoding using PlanDefinition and Clinical Quality Language (CQL)
   - Validate extraction accuracy against gold-standard manual encoding

2. **Tumor Characteristic Extraction from Clinical Documents**
   - Develop LLM-based extraction agents for pathology reports and clinical notes
   - Extract structured tumor characteristics: T (tumor size, extent), N (lymph node involvement), M (metastasis), ER/PR/HER2 status, Ki-67, histologic grade, Oncotype DX scores
   - Validate extraction accuracy against expert manual abstraction

3. **Automated Staging Application**
   - Implement staging logic applying AJCC criteria to extracted tumor characteristics
   - Generate both anatomic and prognostic stages
   - Validate staging accuracy against gold-standard pathological staging

4. **NCCN Treatment Guideline Extraction and Monitoring**
   - Extract NCCN breast cancer treatment guidelines for surgical, systemic, and radiation therapy
   - Develop real-time conformance monitoring checking treatment orders against stage-appropriate guidelines
   - Implement severity-tiered alerting for guideline deviations

5. **Explainability-as-Coordination Framework**
   - Design inter-agent coordination protocols requiring justification and peer review
   - Implement Explainability Agent synthesizing distributed reasoning into coherent oncology-focused narratives
   - Create oncologist-facing interfaces showing staging logic, extracted data, evidence sources, and treatment recommendations with traceable attribution

6. **Clinical Pilot and Evaluation**
   - Deploy system in breast oncology clinical environment with appropriate safeguards
   - Evaluate staging accuracy, tumor extraction accuracy, treatment conformance monitoring, oncologist trust, workflow integration, and clinical impact
   - Compare automated staging against manual staging and expert oncologist assessment

7. **Generalizable Framework and Toolkit**
   - Document validated methodology for cancer staging automation and guideline operationalization
   - Develop open-source toolkit adaptable to other cancer types and AJCC staging systems
   - Produce implementation resources for oncology departments

---

## 3. Novel Theoretical and Methodological Contributions

### 3.1 Explainability-as-Coordination for Oncology Decision Support

**The Oncology-Specific Trust Challenge**:

Oncologists making treatment decisions based on staging need to understand:
- "How was this stage determined?"
- "What data was extracted from the pathology report?"
- "Which AJCC criteria were applied?"
- "Why is this treatment recommended for this stage?"
- "What is the evidence strength?"

When multiple AI agents collaborate (staging extraction, tumor extraction, staging application, treatment recommendation), trust becomes complex: clinicians must trust the entire pipeline, not just individual components.

**The Novel Approach: Explainability-as-Coordination**

Rather than post-hoc explanations, we embed explainability into agent coordination protocols:

**Core Principles**:
1. **Staging Extraction Agent** must justify extracted AJCC criteria to **Staging Application Agent** (peer review before application)
2. **Tumor Extraction Agent** must cite specific locations in pathology reports where characteristics were found, with confidence scores
3. **Staging Application Agent** must explain which criteria matched patient data to determine stage
4. **Treatment Monitoring Agent** must reference specific NCCN guideline sections when recommending treatments
5. **Explainability Agent** coordinates and synthesizes into oncology-focused narratives


### 3.2 Automated AJCC Staging Pipeline

**The AJCC Staging Complexity**:

AJCC 8th edition breast cancer staging involves:
- **Anatomic staging**: T (5 categories), N (4 categories), M (2 categories) → 8 stage groups (0, IA, IB, IIA, IIB, IIIA, IIIB, IIIC, IV)
- **Prognostic staging**: Anatomic stage + ER/PR/HER2 + Grade + Oncotype DX (when available) → modified stage groups
- Complex conditional logic (e.g., "If T2, N1, M0, ER+, PR+, HER2-, Grade 1-2, Oncotype DX < 11, then prognostic Stage IA")

**Our Multi-Stage LLM Pipeline**:

**Stage 1: AJCC Criteria Extraction**
- **Extraction Agent** processes AJCC 8th edition breast cancer staging manual (PDF, ~100 pages)
- Extracts T, N, M definitions with conditional logic
- Extracts anatomic stage group tables
- Extracts prognostic stage group tables with biomarker integration rules
- Outputs structured JSON with confidence scores

**Stage 2: FHIR Encoding**
- **Encoding Agent** converts extracted criteria into FHIR PlanDefinition resources
- T, N, M definitions → CQL (Clinical Quality Language) expressions
- Stage group logic → CQL decision tables
- Biomarker integration → CQL conditional logic
- Validation: Automated testing with known cases

**Stage 3: Tumor Characteristic Extraction from Patient Data**
- **Tumor Extraction Agent** processes patient-specific documents:
  - Pathology reports (unstructured text)
  - Imaging reports (radiology, mammography)
  - Lab results (immunohistochemistry, genomic tests)
- Extracts structured T, N, M, ER, PR, HER2, Ki-67, grade, Oncotype DX
- Cites specific source locations (document, page, line)
- Confidence scoring for each extracted characteristic
- Quality assurance: Consistency checking across documents

**Stage 4: Staging Application**
- **Staging Application Agent** applies AJCC criteria to extracted tumor characteristics
- Executes CQL logic to determine anatomic and prognostic stages
- Handles missing data gracefully (e.g., Oncotype DX not always available)
- Explains which criteria matched to produce stage assignment

**Stage 5: Quality Assurance and Validation**
- **Validation Agent** performs multi-layer checks:
  - Consistency: Do extracted characteristics align across documents?
  - Completeness: Are all required data elements present?
  - Logic testing: Does staging output match expected results for test cases?
  - Confidence thresholds: Flag low-confidence extractions for expert review
- Expert review interface for validating uncertain cases

**Key Innovation**: End-to-end automation from AJCC manual to patient-specific staging with explainability and quality assurance at each stage.

### 3.3 Real-Time Treatment Conformance Monitoring

**NCCN Treatment Guideline Complexity**:
- 250+ pages of conditional treatment recommendations
- Pathways depend on: stage, biomarkers, patient age, menopausal status, comorbidities, patient preferences
- Multiple modalities: surgery, systemic therapy (chemotherapy, endocrine, targeted), radiation
- Evidence categories (1, 2A, 2B, 3) indicating recommendation strength

**Our Approach**:

**1. NCCN Guideline Extraction**
- Extract treatment recommendations for each stage and biomarker combination
- Map conditional logic (e.g., "For Stage IB, ER+, premenopausal → endocrine therapy + ovarian suppression")
- Encode using FHIR PlanDefinition and CQL
- Categorize by evidence strength

**2. Real-Time Conformance Monitoring**
- Integrate with EHR order entry via FHIR subscriptions or CDS Hooks
- Monitor treatment orders (surgery, chemotherapy, radiation, endocrine therapy)
- Check conformance against stage-appropriate NCCN guidelines
- Classify deviations by severity:
  - **Critical**: Category 1 recommendation not followed (e.g., no radiation after lumpectomy)
  - **Moderate**: Category 2A recommendation not followed
  - **Informational**: Category 2B/3 or acceptable alternative chosen

**3. Alert Generation and Delivery**
- Generate alerts at natural clinical decision points (order entry, treatment planning meetings)
- Provide context: stage, guideline recommendation, current orders, evidence strength
- Suggest actions: specific orders to consider, references to discuss with patient
- Track alert responses to reduce future alert fatigue

**4. Adaptive Learning**
- Monitor which alerts are acted upon vs. overridden
- Learn institution-specific practice patterns
- Adjust alert thresholds to balance sensitivity with reducing noise
- Identify systematic deviations for quality improvement initiatives

**Key Innovation**: Closed-loop system connecting automated staging with real-time treatment guideline monitoring and intervention.

---

## 4. Theoretical Foundation and Literature Review

### 4.1 Breast Cancer Staging and Treatment Guidelines

**AJCC TNM Staging System**:
- Gold standard for cancer staging worldwide
- 8th edition (2018) introduced prognostic staging for breast cancer incorporating biomarkers [Amin et al., 2017]
- Critical for treatment planning, clinical trial enrollment, prognosis assessment
- Challenge: Complex conditional logic, especially prognostic staging

**NCCN Treatment Guidelines**:
- Evidence-based, consensus-driven recommendations for cancer management
- Updated multiple times annually based on emerging evidence
- Category 1 recommendations: High-level evidence, uniform consensus
- Wide adoption but significant variation in adherence across institutions

**Clinical Need**:
- Staging discordance: 10-15% disagreement between clinical and pathological staging
- Treatment variation: 20-40% of breast cancer patients receive non-guideline-concordant care
- Time burden: Manual staging and guideline lookup time-consuming

**Research Gap**: Automated systems for accurate, rapid staging and real-time guideline adherence monitoring.

### 4.2 LLMs for Clinical Information Extraction

**Current State**:
- LLMs demonstrate strong performance extracting structured information from unstructured clinical text
- Applications in radiology report structuring, clinical note summarization, diagnosis extraction
- Some work on tumor characteristic extraction from pathology reports [Recent studies 2023-2024]

**Oncology-Specific Applications**:
- Early work on cancer staging assistance
- Extraction of TNM characteristics from pathology reports
- Limited validation for clinical deployment

**Limitations**:
- Hallucinations generating incorrect tumor characteristics (unacceptable in oncology)
- Most work single-agent, single-task
- Insufficient quality assurance for high-stakes staging decisions
- No systematic frameworks for complete staging pipelines

**Enabling Technology**:
- On-premises LLM deployment addressing patient data privacy concerns
- Fine-tuning on oncology-specific corpora improves domain performance

**Research Gap**: Multi-agent LLM frameworks with robust quality assurance for accurate, reliable tumor characteristic extraction and staging.

### 4.3 Process Mining and Conformance Checking in Oncology

**Current State**:
- Process mining successfully applied to cancer care pathways [Literature references]
- Identifies bottlenecks, delays, deviations from expected pathways
- Conformance checking measures adherence to evidence-based pathways

**Limitations**:
- Requires manually created process models (cancer care pathway engineering)
- Primarily retrospective analysis
- No real-time intervention capabilities
- No automated guideline operationalization

**Research Gap**: Integration of automated guideline extraction with real-time conformance monitoring for prospective intervention.

### 4.4 Multi-Agent Systems and Explainability

**Multi-Agent Coordination Theory** [Wooldridge, 2021; Durfee, 2019]:
- Established principles for agent communication, coordination protocols
- Multi-agent LLM systems emerging for complex tasks
- Healthcare applications limited

**Explainability in Clinical AI** [Kumpati et al., 2024]:
- Clinician trust depends on transparency, reliability, workflow alignment
- Explainability can increase or decrease trust depending on implementation
- In oncology: High-stakes decisions require clear evidence traceability

**Distributed Trust Challenge** [Glikson & Woolley, 2020]:
- Multi-agent systems require trusting coordination, not just individual agents
- Oncology-specific: Trust in automated staging requires understanding entire pipeline

**Research Gap**: Coordination protocols specifically designed for oncology decision support with explainability embedded in agent interactions (Explainability-as-Coordination).

### 4.5 Healthcare Interoperability Standards

**HL7 FHIR**:
- Standards-based interoperability for health data exchange
- FHIR PlanDefinition: Encoding clinical protocols and pathways
- Clinical Quality Language (CQL): Computable clinical logic
- CDS Hooks: Integration points for clinical decision support

**Oncology-Specific Standards**:
- mCODE (minimal Common Oncology Data Elements): FHIR profiles for cancer data
- Standardized cancer staging representation in FHIR
- Tumor characteristics, biomarkers, treatments

**Opportunity**: Standards maturity enables interoperable, cross-platform deployment of automated staging and guideline systems.

---

## 5. Feasibility and Risk Mitigation

### 5.1 Technical Feasibility

**Enabling Factors**:
- LLMs demonstrably capable of clinical text understanding and information extraction
- AJCC staging criteria well-structured and comprehensive (ideal for extraction)
- FHIR/mCODE standards provide mature interoperability framework for cancer data
- On-premises LLM deployment addresses patient data privacy concerns
- Pathology reports and cancer registry data available for validation

**Key Risks and Mitigation**:

**Risk 1: LLM Extraction Errors (Hallucinations)**
- *Challenge*: Incorrect tumor characteristics or staging criteria could harm patients
- *Mitigation*:
  - Multi-layer validation: Consistency checking, fact verification against knowledge bases
  - Confidence scoring: Low-confidence extractions flagged for expert review
  - Source citation: Cite specific locations in reports/guidelines for verification
  - Gold-standard validation: Compare against expert manual abstraction
  - Human-in-the-loop: Oncologist review required for all staging
  - Safety threshold: If confidence < X, require expert validation before clinical use

**Risk 2: AJCC Staging Logic Complexity**
- *Challenge*: Prognostic staging with biomarkers involves complex conditional logic that may be difficult to encode accurately
- *Mitigation*:
  - Start with anatomic staging (simpler), then add prognostic staging
  - Extensive automated testing with diverse staging scenarios
  - Expert oncologist validation of encoded logic
  - Iterative refinement based on validation errors

**Risk 3: EHR Integration Complexity**
- *Challenge*: Data access, API limitations
- *Mitigation*:
  - FHIR standards ensure baseline interoperability
  - Early engagement with EHR vendor and institutional IT


**Risk 4: System Performance and Latency**
- *Challenge*: LLM inference can be computationally intensive; oncologists need timely results
- *Mitigation*:
  - Optimize inference (model quantization, caching)
  - Asynchronous processing: Stage patients overnight or when reports arrive, results ready for next clinic visit
  - Load testing with realistic volumes
  - On-premises GPU servers for adequate performance

### 5.2 Clinical Feasibility

**Enabling Factors**:
- Clear clinical need: Staging errors, time burden, guideline adherence variation
- High-volume condition: Ample patient cases for validation
- Engaged oncology community interested in AI applications
- Established validation metrics (staging accuracy vs. gold standard)

**Key Risks and Mitigation**:

**Risk 5: Oncologist Trust in Automated Staging**
- *Challenge*: Resistance to AI-determined staging vs. expert oncologist judgment
- *Mitigation*:
  - Transparency: Complete explainability showing extracted data and staging logic
  - Validation: Publish staging accuracy vs. gold standard and expert oncologists
  - Human oversight: Oncologists review and approve all staging
  - Iterative refinement: Incorporate oncologist feedback
  - Education: Training on system capabilities and limitations
  - Clinical champions: Engage respected oncologists as advocates

**Risk 6: Alert Fatigue from Treatment Conformance Monitoring**
- *Challenge*: Too many alerts reduce compliance and cause frustration
- *Mitigation*:
  - Severity tiering: Critical vs. informational alerts
  - Evidence-based thresholds: Only alert for Category 1 (high evidence) guideline deviations initially
  - Adaptive learning: Track alert responses, adjust thresholds to reduce noise
  - Careful alert design: Actionable, concise, context-rich
  - Oncologist input: Co-design alert content and delivery with end users

**Risk 7: Workflow Disruption**
- *Challenge*: New system temporarily decreases efficiency, causes frustration
- *Mitigation*:
  - Staged rollout: Shadow mode → advisory mode (no disruption initially)
  - Extensive training: Role-specific education for oncologists, registrars, pathologists
  - Clinical champion engagement: Respected oncologists supporting implementation
  - Responsive support: Dedicated team for issue resolution
  - Iterative refinement: Continuous feedback loops and improvements

**Risk 8: Clinical Safety**
- *Challenge*: Staging errors could lead to inappropriate treatment
- *Mitigation*:
  - Human approval required: No automated staging used clinically without oncologist review
  - Extensive pre-deployment testing: Validate on diverse cases with expert review
  - Shadow mode: Validate accuracy before any clinician-facing deployment
  - Incident reporting: Systematic tracking and root cause analysis of any errors
  - Continuous monitoring: Ongoing staging accuracy assessment during pilot
  - Quick disable capability: Ability to turn off system immediately if safety concerns arise

**Risk 9: Pathological Staging Availability for Validation**
- *Challenge*: Gold-standard pathological staging may not be immediately available (requires surgery)
- *Mitigation*:
  - Retrospective validation: Use historical cases with completed pathological staging
  - Cancer registry data: Leverage existing validated staging data
  - Prospective validation: Shadow mode validation as new cases progress to surgery
  - Expert oncologist comparison: Inter-rater reliability with human experts alongside pathological gold standard

---

## References

### Cancer Staging and Guidelines

1. Amin, M. B., et al. (Eds.). (2017). *AJCC Cancer Staging Manual* (8th ed.). Springer. [Breast cancer staging chapter]

2. National Comprehensive Cancer Network (NCCN). (2025). *NCCN Clinical Practice Guidelines in Oncology: Breast Cancer* (Version 3.2025). https://www.nccn.org/guidelines/category_1

3. Giuliano, A. E., et al. (2017). "Breast Cancer-Major changes in the American Joint Committee on Cancer eighth edition cancer staging manual." *CA: A Cancer Journal for Clinicians*, 67(4), 290-303.

4. Weiss, A., et al. (2019). "Clinical and pathological stage discordance among 433,514 breast cancer patients." *American Journal of Surgery*, 217(5), 822-828. https://doi.org/10.1016/j.amjsurg.2019.01.018

### LLMs and Clinical Information Extraction

5. Zhao, J., et al. (2024). "Guideline-Incorporated Large Language Model-Driven Evaluation of Medical Records Using MedCheckLLM." *Healthcare Informatics Research*, 30(3), 220-229.

6. Wang, Y., et al. (2023). "MedDM: LLM-executable clinical guidance tree for clinical decision-making." *arXiv preprint* arXiv:2312.02441.

7. Chen, Y., et al. (2025). "Cancer Type, Stage and Prognosis Assessment from Pathology Reports using LLMs." *Scientific Reports*, 15, Article number. https://doi.org/10.1038/s41598-025-10709-4 / *arXiv preprint* arXiv:2503.01194.

8. Xu, X., et al. (2024). "Generalizable and automated classification of TNM stage from pathology reports with external validation." *Nature Communications*, 15, 8978. https://doi.org/10.1038/s41467-024-53190-9

9. Kim, S., et al. (2024). "Automated Pathologic TN Classification Prediction and Rationale Generation From Lung Cancer Surgical Pathology Reports Using a Large Language Model Fine-Tuned With Chain-of-Thought: Algorithm Development and Validation Study." *JMIR Medical Informatics*, 12, e67056.

10. Sharma, R., et al. (2025). "Using Large Language Models to Automate Data Extraction From Surgical Pathology Reports: Retrospective Cohort Study." *JMIR Formative Research*, 9, e64544.

11. Ibrahim, S., et al. (2025). "Large Language Model Applications for Health Information Extraction in Oncology: Scoping Review." *JMIR Cancer*, 11, e65984. https://cancer.jmir.org/2025/1/e65984

### Process Mining and Conformance Checking

12. Rojas, E., et al. (2016). "Process mining in healthcare: A literature review." *Journal of Biomedical Informatics*, 61, 224-236.

13. van der Aalst, W. M. P. (2016). *Process Mining: Data Science in Action* (2nd ed.). Springer-Verlag Berlin Heidelberg.

14. Guzzo, A., et al. (2025). "Checking Medical Process Conformance by Exploiting LLMs." *Applied Sciences*, 15(18), 10184. https://doi.org/10.3390/app152010184

### Multi-Agent Systems and LLM-based Agents in Medicine

15. Wooldridge, M. (2021). *An Introduction to MultiAgent Systems* (3rd ed.). Wiley.

16. Durfee, E. H. (2019). "Multiagent Coordination: Theory and Practice." *ACM Computing Surveys*, 52(5), Article 101.

17. Poon, A. I., et al. (2024). "Multiagent AI Systems in Health Care: Envisioning Next-Generation Intelligence." *JMIR Medical Informatics*, 12, e62864.

18. Zhang, Y., et al. (2025). "A Survey of LLM-based Agents in Medicine: How far are we from Baymax?" *arXiv preprint* arXiv:2502.11211. https://arxiv.org/html/2502.11211v1

19. Chen, Z., et al. (2025). "Enhancing diagnostic capability with multi-agents conversational large language models." *npj Digital Medicine*, 8, Article 74.

### Trust and Explainability in Healthcare AI

20. Kumpati, S., et al. (2024). "How Explainable Artificial Intelligence Can Increase or Decrease Clinicians' Trust in AI Applications in Health Care: Systematic Review." *JMIR AI*, 2024(1), e53207.

21. Glikson, E., & Woolley, A. W. (2020). "Human Trust in Artificial Intelligence: Review of Empirical Research." *Academy of Management Annals*, 14(2), 627-660.

22. Tiu, E., et al. (2024). "Autonomous medical evaluation for guideline adherence of large language models." *npj Digital Medicine*, 7, 356. https://doi.org/10.1038/s41746-024-01356-6

### Healthcare Interoperability Standards

23. HL7 International (2023). "FHIR R5 Specification: Fast Healthcare Interoperability Resources." http://hl7.org/fhir/R5/

24. mCODE (minimal Common Oncology Data Elements). "FHIR Implementation Guide for Cancer Data." https://hl7.org/fhir/us/mcode/

25. Mandel, J. C., et al. (2016). "SMART on FHIR: a standards-based, interoperable apps platform for electronic health records." *Journal of the American Medical Informatics Association*, 23(5), 899-908.

### Implementation Science

26. Damschroder, L. J., et al. (2009). "Fostering implementation of health services research findings into practice: a consolidated framework for advancing implementation science." *Implementation Science*, 4, 50.

27. Greenhalgh, T., et al. (2017). "Beyond Adoption: A New Framework for Theorizing and Evaluating Nonadoption, Abandonment, and Challenges to the Scale-Up, Spread, and Sustainability of Health and Care Technologies." *Journal of Medical Internet Research*, 19(11), e367.

### Clinical Decision Support Systems

28. Sutton, R. T., et al. (2020). "An overview of clinical decision support systems: benefits, risks, and strategies for success." *npj Digital Medicine*, 3, 17.

---

