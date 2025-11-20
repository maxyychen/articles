# LLM-Based Medical Record Structured Data Extraction

## 1. Overview

Structured data extraction transforms unstructured medical text into machine-readable, schema-compliant data. This framework focuses exclusively on leveraging Large Language Models (LLMs) for precise, consistent extraction of medical entities from clinical documentation.

### Research Foundation

Recent research demonstrates significant advances in LLM-based medical information extraction:

**Clinical Context**: Approximately 80% of clinical data exists in unstructured format, making automated extraction critical for healthcare analytics, research, and decision support.

**Performance Benchmarks** (2024-2025 studies):
- **ChatGPT-3.5**: 89% accuracy for pathological classifications in lung cancer datasets, outperforming traditional NLP methods (npj Digital Medicine, 2024)
- **GPT-4 with prompt engineering**: Up to 20% performance improvement on clinical NER tasks, approaching fine-tuned model performance (JAMIA, 2024)
- **GPT-4o with prompt ensemble**: F1-score of 0.95, recall of 0.98 for medical entity recognition from EHRs (arXiv, 2025)
- **Llama 2 (local deployment)**:
  - Liver cirrhosis detection: 100% sensitivity, 96% specificity
  - Ascites detection: 95% sensitivity, 95% specificity
  - Confusion detection: 76% sensitivity, 94% specificity
  - Abdominal pain detection: 84% sensitivity, 97% specificity
  - Shortness of breath: 87% sensitivity, 97% specificity
  - (Nature Digital Medicine, 2024 - Privacy-preserving medical information retrieval study)

**Key Findings from Literature**:
1. Open-source LLMs can match traditional pattern-matching methods for social determinants of health (SDoH) extraction without fine-tuning
2. Strategic few-shot prompting yields 15-20% F1 score improvement across clinical NER benchmarks
3. RAG-augmented approaches (e.g., DiRAG with UMLS) achieve state-of-the-art zero-shot NER performance
4. LLMs excel at extraction but still underperform for complex medical coding (GPT-4: <50% exact match for ICD-10 codes)

**References**:
- Multiple model performance evaluation (BMC Medical Research Methodology, 2025)
- Entity extraction pipeline study (JMIR, 2024)
- Privacy-preserving extraction (Nature Digital Medicine, 2024)
- Clinical NER prompt engineering (Oxford Academic JAMIA, 2024)

### Task Definition

**Primary Goal**: Convert unstructured clinical notes into structured JSON/XML that can be ingested by downstream systems (EHRs, analytics platforms, billing systems).

**Key Characteristics**:
- **Output Format**: Structured data (JSON, XML, FHIR resources)
- **Audience**: Systems, databases, analytics engines
- **Quality Focus**: Precision, completeness, consistency
- **Error Tolerance**: Very low (critical for billing, clinical decision support)
- **Temperature Setting**: 0-0.2 (maximum determinism)
- **Validation**: Schema compliance, field accuracy, medical code correctness

### Use Cases

- **EHR Integration**: Extract data from clinical notes for structured EHR fields
- **Medical Coding**: Identify diagnoses and procedures for ICD-10/CPT coding
- **Clinical Research**: Build structured datasets from medical records
- **Quality Metrics**: Extract data for healthcare quality measure calculation
- **Billing**: Capture billable procedures and diagnoses
- **Clinical Decision Support**: Provide structured input for alert systems
- **Population Health**: Aggregate patient data for cohort analysis

## 2. Extraction Principles

### Determinism Over Creativity

Structured extraction requires consistent, repeatable outputs:
- Same input should produce identical (or near-identical) structured data across runs
- Use lowest possible temperature (0-0.2) to minimize stochastic variation
- Prefer explicit rules over interpretive flexibility
- Test same record multiple times to verify consistency

### Schema-Driven Processing

Every extraction is guided by a predefined schema:
- Define explicit data schemas before any extraction
- Every field has defined type, format, and constraints
- Specify how to handle missing information systematically
- Use industry standards (FHIR, HL7) where applicable
- Custom schemas must be rigorously documented

### Completeness Matters

Extract ALL mentioned information:
- Don't selectively extract based on perceived importance
- Include uncertain or ambiguous information with confidence scores
- Flag missing critical information explicitly
- Capture negative findings ("no history of diabetes")
- Preserve all dates, even if approximate

### Machine-First Design

Optimize for machine consumption:
- Output must be parseable by standard JSON/XML parsers
- Consistent field naming (snake_case or camelCase, not mixed)
- Standardized date formats (ISO 8601)
- Numeric values as numbers, not strings
- Enums from predefined value sets
- Human readability is secondary

### Precision Over Recall (When Necessary)

For critical applications:
- Better to flag uncertainty than to guess
- Use null for truly missing data, not default values
- Include confidence scores for ambiguous extractions
- Allow human review for low-confidence items

## 3. Standard Schema Components

### Patient Information
```
{
  "patient_id": string (MRN or unique identifier),
  "age": integer,
  "gender": enum["male", "female", "other", "unknown"],
  "date_of_birth": "YYYY-MM-DD",
  "ethnicity": string,
  "primary_language": string
}
```

### Diagnoses
```
{
  "diagnoses": [
    {
      "condition": string (full diagnosis name),
      "icd10_code": string (e.g., "E11.9"),
      "status": enum["primary", "secondary", "ruled_out", "history_of"],
      "onset_date": "YYYY-MM-DD",
      "resolved_date": "YYYY-MM-DD" | null,
      "severity": enum["mild", "moderate", "severe"],
      "clinical_status": enum["active", "resolved", "inactive"],
      "confidence_score": 0-100
    }
  ]
}
```

### Medications
```
{
  "medications": [
    {
      "name": string (generic name preferred),
      "brand_name": string | null,
      "dosage": string (e.g., "500mg"),
      "frequency": string (e.g., "twice daily", "BID"),
      "route": enum["oral", "IV", "IM", "topical", "inhaled"],
      "start_date": "YYYY-MM-DD",
      "end_date": "YYYY-MM-DD" | null,
      "status": enum["active", "discontinued", "completed"],
      "indication": string (why prescribed),
      "prescriber": string | null,
      "confidence_score": 0-100
    }
  ]
}
```

### Lab Results
```
{
  "lab_results": [
    {
      "test_name": string (standardized name),
      "loinc_code": string | null,
      "value": number,
      "value_string": string (for non-numeric results),
      "unit": string (e.g., "mg/dL"),
      "reference_range": string (e.g., "70-100"),
      "abnormal_flag": enum["normal", "high", "low", "critical"],
      "collection_date": "YYYY-MM-DD",
      "result_date": "YYYY-MM-DD",
      "confidence_score": 0-100
    }
  ]
}
```

### Vital Signs
```
{
  "vital_signs": {
    "blood_pressure_systolic": integer,
    "blood_pressure_diastolic": integer,
    "heart_rate": integer,
    "temperature": number,
    "temperature_unit": enum["C", "F"],
    "respiratory_rate": integer,
    "oxygen_saturation": number (0-100),
    "weight": number,
    "weight_unit": enum["kg", "lbs"],
    "height": number,
    "height_unit": enum["cm", "inches"],
    "bmi": number,
    "measurement_date": "YYYY-MM-DD"
  }
}
```

### Procedures
```
{
  "procedures": [
    {
      "name": string,
      "cpt_code": string | null,
      "date": "YYYY-MM-DD",
      "location": string (anatomical site),
      "provider": string | null,
      "indication": string,
      "outcome": string,
      "complications": string | null,
      "confidence_score": 0-100
    }
  ]
}
```

### Allergies
```
{
  "allergies": [
    {
      "allergen": string,
      "allergen_type": enum["medication", "food", "environmental", "other"],
      "reaction": string,
      "severity": enum["mild", "moderate", "severe"],
      "onset_date": "YYYY-MM-DD" | null,
      "status": enum["active", "resolved", "suspected"],
      "confidence_score": 0-100
    }
  ]
}
```

## 4. Benchmark Datasets and Evaluation

### Standard Clinical NLP Benchmarks

**i2b2/n2c2 Challenges** (Informatics for Integrating Biology & the Bedside)
- **2010 i2b2 Challenge**: Concepts, assertions, and relations in clinical text
  - Entity types: Problems, Treatments, Tests
  - Gold standard annotations from Beth Israel Deaconess Medical Center
  - Benchmark for NER, assertion classification, relation extraction
- **2012 i2b2 Challenge**: Temporal relations in clinical narratives
- **2014 i2b2 Challenge**: De-identification and heart disease risk factors
- **n2c2 2018**: Adverse drug events and medication extraction
- **n2c2 2019**: Multi-track including n2c2/UMass Track 3 (physical activity extraction)

**Performance Context**:
- Traditional fine-tuned models (BioClinicalBERT): F1 ~85-90% on i2b2 test sets
- GPT-4 zero-shot: F1 ~70-75% on i2b2 benchmarks
- GPT-4 with prompt engineering (few-shot): F1 ~80-85%, approaching supervised models
- Strategic in-context example selection: 15-20% F1 improvement

**NCBI Disease Corpus**
- 793 PubMed abstracts with disease entity annotations
- 6,892 disease mentions, 790 unique disease concepts
- GPT-4 zero-shot performance: F1 58.4
- DiRAG (RAG + UMLS) with GPT-4: State-of-the-art zero-shot results

**BC5CDR (BioCreative V Chemical Disease Relation)**
- Chemical and disease entity recognition
- 1,500 PubMed articles
- GPT-4 zero-shot: F1 71.3

**BC2GM (BioCreative II Gene Mention)**
- Gene/protein entity recognition from biomedical text
- 20,000 sentences from PubMed abstracts

**MTSamples Corpus**
- Over 5,000 medical transcription samples
- Multiple specialties and note types
- Used for evaluating extraction across diverse clinical contexts

### FHIR Extraction Benchmarks

**Infherno Framework** (2025)
- End-to-end agentic FHIR resource synthesis from free-form clinical notes
- Evaluates extraction and conversion to FHIR/JSON format
- Includes Patient, Medication, Condition, Observation resources

**LLM-FHIR-Eval**
- Specialized benchmark for FHIR-compliant data extraction
- Tests extraction of specific healthcare data elements
- Evaluates adherence to FHIR schema specifications

### Evaluation Metrics

**Entity-Level Metrics**:
- **Precision**: TP / (TP + FP) - percentage of extracted entities that are correct
- **Recall**: TP / (TP + FN) - percentage of actual entities that were extracted
- **F1 Score**: 2 × (Precision × Recall) / (Precision + Recall) - harmonic mean

**Token-Level Metrics**:
- Exact match: Extracted entity boundaries match gold standard exactly
- Partial match: Overlap between extracted and gold standard spans
- Relaxed matching: Allow minor boundary variations (±1-2 tokens)

**Field-Level Accuracy**:
- Percentage of individual structured fields correctly extracted
- Critical for schema-compliant extraction (JSON validation)

**Code Assignment Metrics**:
- **Exact Match Rate**: ICD-10/CPT code exactly matches ground truth
- **Top-K Accuracy**: Correct code in top K predictions
- **Hierarchical Accuracy**: Code at correct level in taxonomy (e.g., E11 vs E11.9)

**Confidence Calibration**:
- Expected Calibration Error (ECE): How well confidence scores match actual accuracy
- Well-calibrated: Items with 80% confidence should be 80% accurate

### Zero-Shot vs Few-Shot Performance

**Research Findings** (2024-2025 studies):

**Zero-Shot Capabilities**:
- GPT-4: 70-75% F1 on clinical NER without examples
- Sufficient for screening and initial extraction
- Best with clear entity definitions in prompt
- DiRAG (RAG-augmented): Achieves near-SOTA zero-shot performance

**Few-Shot Benefits**:
- 2-4 examples: 10-15% F1 improvement
- 5-10 examples: 15-20% F1 improvement
- Strategic example selection (diverse, edge cases) > random selection
- Prompt framework with entity definitions + annotation guidelines + examples: Up to 20% improvement

**Comparison to Fine-Tuned Models**:
| Approach | F1 Score (i2b2) | Training Required | Cost per Record |
|----------|----------------|-------------------|-----------------|
| BioClinicalBERT (fine-tuned) | 85-90% | Yes (thousands of examples) | Low (self-hosted) |
| GPT-4 Zero-shot | 70-75% | No | Medium (API) |
| GPT-4 Few-shot (5 examples) | 80-85% | No (just examples) | Medium (API) |
| GPT-4o Prompt Ensemble | 95% | No | High (multiple calls) |

**Trade-offs**:
- Fine-tuned models: Highest accuracy, requires training data and infrastructure
- Zero-shot LLMs: Quick deployment, lower accuracy, API costs
- Few-shot LLMs: Best balance for most use cases
- Ensemble methods: Highest accuracy, highest cost

## 5. Extraction Processing Patterns

### Pattern A: Single-Pass Extraction

**When to Use**:
- Standard clinical notes (2-5 pages)
- Well-structured documents
- When latency is critical
- Budget-constrained scenarios

**Approach**:
1. Define complete schema in system prompt
2. Include 2-4 few-shot examples
3. Single LLM call with JSON mode enabled
4. Extract all entities in one pass
5. Post-process for validation

**Prompt Structure**:
```
System: You are a medical data extraction specialist. Extract structured
information following the exact schema provided.

User: Extract all medical information from this record into the following
JSON schema:

[Complete schema definition with field types, constraints, examples]

Medical Record:
<record>
{medical_record_text}
</record>

Instructions:
- Return ONLY valid JSON, no explanatory text
- Use null for missing values, never omit required fields
- All dates in YYYY-MM-DD format
- Include confidence_score (0-100) for each entity
- Extract exactly what is stated, do not infer
```

**Advantages**:
- Fast (single API call)
- Simple to implement
- Cost-effective
- Good for standard cases

**Limitations**:
- May miss nuanced relationships
- Less accurate for complex multi-condition patients
- Struggles with very long documents
- Lower consistency on edge cases

### Pattern B: Multi-Stage Pipeline

**When to Use**:
- Complex patients with multiple conditions
- When accuracy is paramount
- Research applications
- High-value extractions (e.g., oncology records)

**Stage 1: Entity Identification**

Focus: Identify what entities exist, grouped by category

Prompt: "List all entities in this record by category: DIAGNOSES, MEDICATIONS,
LAB_RESULTS, PROCEDURES, VITAL_SIGNS, ALLERGIES. Format as simple lists."

Output: Category-grouped entity lists

**Stage 2: Detailed Extraction per Category**

For each category, dedicated extraction pass:

Prompt: "For each {category} entity, extract complete details including all
fields in the schema. Context: {original_record_relevant_sections}"

Output: Fully detailed entities for that category

**Stage 3: Relationship Linking**

Focus: Establish connections between entities

Prompt: "Given these extracted entities, identify relationships: which medications
treat which conditions, which labs monitor which diagnoses, temporal sequences."

Output: Relationship graph (entity pairs with relationship types)

**Stage 4: Timeline Construction**

Focus: Chronological ordering

Prompt: "Create timeline of all dated events. Order chronologically, calculate
durations, identify status changes."

Output: Ordered timeline with all events

**Stage 5: Cross-Validation**

Focus: Verify consistency

Prompt: "Review all extracted data for: conflicting information, impossible
values, missing critical data, temporal inconsistencies."

Output: Validated data with error flags

**Advantages**:
- Highest accuracy
- Better relationship extraction
- Handles complexity well
- Each stage can be optimized independently

**Limitations**:
- 5x latency vs single-pass
- Higher API costs
- More complex orchestration
- Requires careful prompt engineering per stage

### Pattern C: Multi-Document Aggregation

**When to Use**:
- Multiple records for same patient
- Longitudinal analysis
- Care transition summaries
- Historical medical record compilation

**Approach**:

**Step 1: Document Tagging**
Label each record with metadata:
```
{
  "record_id": "...",
  "date": "YYYY-MM-DD",
  "type": "emergency_visit" | "follow_up" | "lab_results" | "imaging",
  "facility": "...",
  "provider": "..."
}
```

**Step 2: Individual Extraction**
Extract from each document independently using Pattern A or B

**Step 3: Aggregation Prompt**
```
You have extracted data from {n} medical records spanning {date_range} for the
same patient.

Record 1 (date: YYYY-MM-DD, type: emergency_visit):
{extracted_data_1}

Record 2 (date: YYYY-MM-DD, type: follow_up):
{extracted_data_2}

...

Tasks:
1. Merge diagnoses: Deduplicate, track status changes (new → active → resolved)
2. Build medication timeline: Started, changed, discontinued dates
3. Aggregate labs chronologically, identify trends
4. Identify contradictions or conflicting information
5. Maintain source attribution (which record each data point came from)

Output consolidated JSON with:
- Deduplicated entities
- Chronological timelines per category
- Status change tracking
- Source references
```

**Output Structure**:
```
{
  "diagnoses": [
    {
      "condition": "Type 2 Diabetes Mellitus",
      "icd10_code": "E11.9",
      "timeline": [
        {"date": "2023-01-15", "status": "diagnosed", "source": "record_1"},
        {"date": "2023-06-20", "status": "controlled", "source": "record_3"}
      ],
      "current_status": "active"
    }
  ],
  "medications": [
    {
      "name": "metformin",
      "timeline": [
        {"date": "2023-01-15", "action": "started", "dosage": "500mg BID", "source": "record_1"},
        {"date": "2023-03-10", "action": "increased", "dosage": "1000mg BID", "source": "record_2"},
        {"date": "2023-08-05", "action": "discontinued", "reason": "GI intolerance", "source": "record_4"}
      ]
    }
  ]
}
```

**Advantages**:
- Complete patient view
- Tracks changes over time
- Identifies trends and patterns
- Maintains provenance

**Limitations**:
- Requires substantial context window
- Complex deduplication logic
- May need multiple aggregation passes
- Challenging contradiction resolution

## 5. Extraction-Specific Prompt Engineering

### Explicit Schema Definition

Always include in prompt:

**Data Types**:
- "field_name: string" (for text)
- "field_name: integer" (for whole numbers)
- "field_name: number" (for decimals)
- "field_name: boolean" (for true/false)
- "field_name: enum[value1, value2, ...]" (for constrained choices)

**Format Constraints**:
- "All dates must be YYYY-MM-DD format"
- "All ICD-10 codes must be uppercase with period (e.g., E11.9)"
- "All numeric values without units as numbers, not strings"

**Null Handling**:
- "Use null for truly missing information"
- "Never omit required fields - use null if not found"
- "Use empty array [] for missing lists, not null"

**Validation Rules**:
- "Heart rate must be 20-300 bpm"
- "Temperature must be 90-110°F or 32-43°C"
- "Blood pressure systolic must be 50-250"
- "Dates cannot be in the future"

### Few-Shot Examples for Extraction

Include 2-4 examples covering:

**Example 1: Standard Case (Complete Information)**
```
Input: "62-year-old male with chest pain. ECG shows ST elevation. Troponin
elevated at 2.5 ng/mL. Started on aspirin 325mg daily and atorvastatin 80mg
nightly. Diagnosis: STEMI."

Output:
{
  "patient_info": {"age": 62, "gender": "male"},
  "diagnoses": [
    {"condition": "ST elevation myocardial infarction", "icd10_code": "I21.9",
     "status": "primary", "confidence_score": 95}
  ],
  "medications": [
    {"name": "aspirin", "dosage": "325mg", "frequency": "daily", "route": "oral",
     "status": "active", "confidence_score": 100},
    {"name": "atorvastatin", "dosage": "80mg", "frequency": "nightly", "route": "oral",
     "status": "active", "confidence_score": 100}
  ],
  "lab_results": [
    {"test_name": "Troponin", "value": 2.5, "unit": "ng/mL", "abnormal_flag": "high",
     "confidence_score": 100}
  ]
}
```

**Example 2: Missing Data**
```
Input: "Patient has diabetes. Continue current medications."

Output:
{
  "diagnoses": [
    {"condition": "diabetes mellitus", "icd10_code": null, "status": "primary",
     "onset_date": null, "confidence_score": 80}
  ],
  "medications": [],
  "note": "Medications mentioned but not specified"
}
```

**Example 3: Complex Multi-Condition**
```
Input: "Patient with poorly controlled DM2 (HbA1c 9.2%), hypertension, and stage 3
CKD. Current meds: metformin 1000mg BID, lisinopril 20mg daily, atorvastatin 40mg
nightly. Add glipizide 5mg daily. Nephrology referral placed."

Output:
{
  "diagnoses": [
    {"condition": "Type 2 diabetes mellitus", "icd10_code": "E11.9", "status": "primary",
     "clinical_status": "active", "confidence_score": 100},
    {"condition": "hypertension", "icd10_code": "I10", "status": "secondary",
     "confidence_score": 100},
    {"condition": "chronic kidney disease stage 3", "icd10_code": "N18.3",
     "status": "secondary", "confidence_score": 100}
  ],
  "medications": [
    {"name": "metformin", "dosage": "1000mg", "frequency": "BID", "status": "active",
     "indication": "diabetes", "confidence_score": 100},
    {"name": "lisinopril", "dosage": "20mg", "frequency": "daily", "status": "active",
     "indication": "hypertension", "confidence_score": 100},
    {"name": "atorvastatin", "dosage": "40mg", "frequency": "nightly", "status": "active",
     "confidence_score": 100},
    {"name": "glipizide", "dosage": "5mg", "frequency": "daily", "status": "active",
     "indication": "diabetes", "confidence_score": 100}
  ],
  "lab_results": [
    {"test_name": "HbA1c", "value": 9.2, "unit": "%", "abnormal_flag": "high",
     "reference_range": "4.0-5.6", "confidence_score": 100}
  ]
}
```

**Example 4: Ambiguous Information**
```
Input: "Patient may have had MI in past, unclear. On some cardiac medications per patient,
can't remember names."

Output:
{
  "diagnoses": [
    {"condition": "myocardial infarction", "icd10_code": "I21.9", "status": "history_of",
     "onset_date": null, "confidence_score": 40}
  ],
  "medications": [],
  "note": "Patient reports cardiac medications but unable to specify"
}
```

### Role Assignment for Extraction

System prompt should establish clear role:

```
You are a medical data extraction specialist with expertise in clinical documentation.
Your task is to convert unstructured clinical notes into structured JSON data.

Key directives:
- Prioritize accuracy and completeness over interpretation
- Extract exactly what is stated in the text
- Do not infer information not explicitly mentioned
- When information is ambiguous, extract with lower confidence score
- Never invent or hallucinate data
- Use medical terminology precisely
- Apply standard medical coding (ICD-10, CPT, LOINC) accurately
```

### Strict Output Instructions

Include explicit formatting requirements:

```
Output requirements:
- Return ONLY valid JSON, no explanatory text before or after
- Use null for missing values, never omit required fields
- All dates must be YYYY-MM-DD format (ISO 8601)
- All times must be HH:MM:SS format (24-hour)
- Include confidence_score (0-100) for each extracted entity
- Use lowercase for enum values unless schema specifies otherwise
- Arrays must be present even if empty: []
- No trailing commas in JSON
- Ensure all quotes are properly escaped
```

### Chain-of-Thought for Complex Extraction

For difficult cases, request reasoning:

```
Before providing the structured output, think step-by-step:

<reasoning>
1. Identify the clinical context (emergency, routine visit, follow-up, etc.)
2. List all conditions mentioned, in order of clinical significance
3. For each medication:
   - Is it newly prescribed or continued from before?
   - What is the indication (which condition is it treating)?
   - Are there any dosage changes mentioned?
4. For lab results:
   - Which are abnormal and clinically significant?
   - How do they relate to the documented diagnoses?
   - Are there trends from prior values mentioned?
5. Establish temporal relationships:
   - What is the sequence of events?
   - Which findings led to which decisions?
</reasoning>

<structured_output>
[JSON output based on reasoning above]
</structured_output>
```

## 6. Context Window Management for Extraction

### Intelligent Chunking Strategy

When documents exceed context window:

**Section-Aware Splitting**:
- Split by logical sections (History, Physical Exam, Labs, Assessment, Plan)
- Keep section headers with their content
- Don't split mid-entity (e.g., keep medication with its dosage)

**Overlap Strategy**:
- Maintain 10-15% overlap between chunks
- Prevents information loss at boundaries
- Especially important for entities spanning multiple lines

**Chunk Processing**:
```
Chunk 1:
- Extract entities
- Note: "This is chunk 1 of 4"
- Pass forward summary: "Found 2 diagnoses, 3 medications"

Chunk 2:
- Context: "Previous chunk found: 2 diagnoses, 3 medications"
- Extract entities from this chunk
- Continue pattern...

Final Merge:
- Combine all chunk extractions
- Deduplicate entities appearing in overlaps
- Validate complete timeline
```

### Multi-Record Context Management

For multiple documents:

**Priority-Based Inclusion**:
1. Most recent records (full detail)
2. Key historical records (full detail)
3. Older records (compressed summaries)

**Hierarchical Context**:
```
RECENT RECORDS (full extraction):
Record 1 (2024-11-15, Emergency Visit): [full text]
Record 2 (2024-11-10, Follow-up): [full text]

HISTORICAL CONTEXT (summarized):
2024-01-15: Diagnosed with Type 2 Diabetes, started metformin
2023-08-20: Diagnosed with hypertension, started lisinopril
2022-03-10: Baseline labs normal

Now extract structured data considering full patient history.
```

## 7. Multi-Agent Architecture for Extraction

### Agent Pipeline

**Agent 1: Entity Extraction Specialist**
- **Role**: Identify and extract all medical entities
- **Temperature**: 0-0.1 (maximum consistency)
- **Input**: Original medical record text
- **Output**: Raw structured data (JSON with all entities)
- **Optimization**: Completeness, accurate value capture
- **Prompt Focus**: "Extract ALL entities mentioned. Use null for missing data. Do not skip any information."

**Agent 2: Relationship Mapper**
- **Role**: Identify connections between entities
- **Temperature**: 0.2-0.3 (slight reasoning flexibility needed)
- **Input**: Entities from Agent 1 + original text for context
- **Tasks**:
  - Link medications to conditions they treat
  - Associate lab results with relevant diagnoses
  - Establish cause-effect relationships
  - Identify treatment responses
- **Output**: Relationship graph (entity pairs with relationship types)
```
{
  "relationships": [
    {"medication": "metformin", "treats": "type_2_diabetes", "confidence": 95},
    {"lab": "HbA1c", "monitors": "type_2_diabetes", "confidence": 100},
    {"procedure": "angioplasty", "for": "coronary_artery_disease", "confidence": 100}
  ]
}
```

**Agent 3: Timeline Constructor**
- **Role**: Chronological ordering and temporal reasoning
- **Temperature**: 0-0.1 (precise date handling critical)
- **Input**: All entities with dates from Agent 1
- **Tasks**:
  - Order all events chronologically
  - Calculate durations between events
  - Identify progressions (new → active → resolved)
  - Flag temporal inconsistencies
- **Output**: Chronologically ordered event timeline
```
{
  "timeline": [
    {"date": "2023-01-15", "event": "diagnosis", "entity": "type_2_diabetes"},
    {"date": "2023-01-15", "event": "medication_started", "entity": "metformin_500mg"},
    {"date": "2023-03-20", "event": "lab_result", "entity": "HbA1c_8.2"},
    {"date": "2023-03-20", "event": "medication_increased", "entity": "metformin_1000mg"}
  ]
}
```

**Agent 4: Medical Code Mapper**
- **Role**: Assign accurate medical codes
- **Temperature**: 0 (deterministic code assignment)
- **Input**: Entities with condition/procedure names
- **Tasks**:
  - Assign ICD-10 codes to diagnoses
  - Assign CPT codes to procedures
  - Map lab tests to LOINC codes
  - Verify code appropriateness
- **Output**: Entities with standardized codes
- **Note**: May integrate with external code databases for accuracy

**Agent 5: Validation and QA**
- **Role**: Review and correct all extracted data
- **Temperature**: 0 (strict evaluation)
- **Input**: All extracted data + original text
- **Tasks**:
  - Verify extracted values match source text exactly
  - Check for hallucinated information
  - Identify inconsistencies
  - Flag missing critical data
  - Assess medical plausibility
- **Output**: Validated data + confidence scores + error flags

### Orchestration Flow

```
Original Record
    ↓
Agent 1: Entity Extraction
    ↓
    ├→ Agent 2: Relationship Mapper
    ├→ Agent 3: Timeline Constructor
    └→ Agent 4: Medical Code Mapper
    ↓
Agent 5: Validation & QA
    ↓
Final Structured Output
```

**Sequential Dependencies**:
- Agent 2, 3, 4 can run in parallel (all depend only on Agent 1)
- Agent 5 must run after all others complete
- If Agent 5 flags critical errors, can retry Agent 1 with refined prompt

**Failure Handling**:
- If Agent 1 fails: Retry with more explicit instructions
- If Agent 2-4 fail: Can still deliver partial results (entities without relationships/timeline/codes)
- If Agent 5 flags high-risk errors: Route to human review

## 8. RAG-Augmented Extraction with Medical Knowledge Bases

### Motivation

Research demonstrates that integrating external medical knowledge bases significantly improves extraction accuracy, particularly for:
- Zero-shot performance (DiRAG achieves state-of-the-art results)
- Rare conditions and specialized terminology
- Medical code assignment (ICD-10, CPT, SNOMED CT)
- Entity disambiguation (e.g., "MS" = multiple sclerosis vs mitral stenosis)

### Knowledge Base Integration

**UMLS (Unified Medical Language System)**
- Comprehensive metathesaurus integrating 200+ biomedical vocabularies
- Contains >4 million concepts, >14 million names
- Semantic relationships between medical concepts
- Access via UMLS API or local deployment

**SNOMED CT (Systematized Nomenclature of Medicine - Clinical Terms)**
- Comprehensive clinical terminology with 350,000+ active concepts
- Hierarchical structure for clinical findings, procedures, body structures
- Used for semantic interoperability in healthcare systems
- Integrated within UMLS

**LOINC (Logical Observation Identifiers Names and Codes)**
- Standard for lab tests and clinical observations
- 90,000+ observation terms
- Essential for lab result extraction and coding

### RAG Architectures for Extraction

**Architecture 1: Entity Augmentation (CLEAR Method)**

Research: Clinical Entity Augmented Retrieval (Nature Digital Medicine, 2024)
- Achieves >70% reduction in token usage and inference time
- Outperforms embedding-based retrieval methods

**Process**:
1. Initial NER identifies candidate entities in clinical text
2. Query UMLS API with each entity
3. Retrieve concept names from NLM Metathesaurus or SNOMED CT
4. Augment entity list with official terminology and synonyms
5. LLM uses augmented list for final extraction

**Example**:
```
Clinical text: "Patient has DM2 with poor glycemic control"

Step 1 - Initial NER: Identifies "DM2"
Step 2 - UMLS Query: "DM2" → Search UMLS
Step 3 - Retrieved Concepts:
  - Diabetes Mellitus, Type 2
  - Type 2 Diabetes Mellitus
  - NIDDM (Non-insulin dependent diabetes mellitus)
  - ICD-10: E11.9
  - SNOMED CT: 44054006

Step 4 - Augmented Extraction:
{
  "condition": "Type 2 Diabetes Mellitus",
  "icd10_code": "E11.9",
  "snomed_code": "44054006",
  "synonyms": ["DM2", "NIDDM", "Type 2 DM"],
  "umls_cui": "C0011860"
}
```

**Advantages**:
- Standardizes medical terminology
- Provides correct medical codes automatically
- Disambiguates abbreviations using medical ontology
- 70% faster than full-text retrieval methods

**Architecture 2: DiRAG (Disambiguation RAG)**

Research: Achieved state-of-the-art zero-shot NER on i2b2 and NCBI datasets

**Process**:
1. Extract entities using LLM zero-shot
2. For ambiguous entities, query UMLS for context
3. Use retrieved definitions and relationships to disambiguate
4. Final extraction with disambiguated entities

**Example**:
```
Clinical text: "Patient has MS and experiences MS episodes"

Challenge: "MS" has multiple meanings
- Multiple Sclerosis
- Mitral Stenosis
- Mental Status
- Morphine Sulfate

DiRAG Process:
1. Context Analysis: "experiences MS episodes" suggests disease, not medication
2. UMLS Query: Retrieve definitions for all "MS" possibilities
3. Context Matching: "episodes" commonly associated with Multiple Sclerosis
4. Disambiguation: Select "Multiple Sclerosis" as correct interpretation
5. Code Assignment: ICD-10 G35, SNOMED CT 24700007
```

**Architecture 3: Medical Graph RAG**

Research: MedGraphRAG framework (2024) - creates three-tier hierarchical graph

**Structure**:
1. **Entity Layer**: Extracted medical entities from clinical text
2. **Relationship Layer**: Connections between entities (medication treats condition)
3. **Knowledge Layer**: Links to UMLS, SNOMED CT, medical literature

**Process**:
1. Extract entities using LLM
2. Build local knowledge graph from extraction
3. Link entities to UMLS/SNOMED CT nodes
4. Traverse graph for relationship extraction
5. Query external medical knowledge when needed

**Benefits**:
- Maintains semantic interoperability
- Supports complex relationship extraction
- Enables reasoning over medical knowledge
- Validates extractions against established medical knowledge

### Implementation Approaches

**Approach 1: Pre-Retrieval Augmentation**

```
System: You are a medical data extraction specialist with access to UMLS
medical terminology.

User: Extract entities from this clinical note. For each entity, I will
provide standardized medical terminology and codes.

Clinical Note: [text]

Medical Knowledge Base (UMLS):
- "DM2" → Type 2 Diabetes Mellitus (ICD-10: E11.9, SNOMED: 44054006)
- "HTN" → Hypertension (ICD-10: I10, SNOMED: 38341003)
[...additional terminology provided...]

Now extract structured data using the standardized terminology provided.
```

**Approach 2: Iterative Retrieval During Extraction**

```
1. LLM performs initial extraction
2. System identifies entities needing disambiguation or coding
3. Query UMLS/SNOMED CT for each entity
4. Re-prompt LLM with retrieved knowledge
5. LLM produces refined extraction with codes
```

**Approach 3: Post-Extraction Enrichment**

```
1. LLM extracts entities without external knowledge
2. Post-processing pipeline queries UMLS for each entity
3. Automated code assignment using UMLS mappings
4. Validation agent checks code appropriateness
5. Final output enriched with standardized codes
```

### Performance Impact

**Research-Backed Results**:
- **Zero-shot NER**: DiRAG + GPT-4 achieves SOTA on i2b2/NCBI benchmarks
- **Code Assignment**: UMLS integration improves ICD-10 accuracy from 45% to 65% exact match
- **Disambiguation**: >80% accuracy on ambiguous abbreviations (vs ~50% without RAG)
- **Inference Efficiency**: CLEAR method reduces tokens by 70%, faster processing
- **Rare Conditions**: Significant improvement on long-tail medical entities

### Practical Considerations

**UMLS API Access**:
- Free UMLS license required from NIH
- API rate limits: Consider local deployment for high-volume
- Caching: Store frequent concept lookups to reduce API calls

**SNOMED CT Licensing**:
- Free in most countries for clinical use
- SNOMED International membership for commercial use
- Consider integration via UMLS (includes SNOMED CT)

**Implementation Complexity**:
- Pre-retrieval: Simplest, but requires pre-processing all possible terms
- Iterative: Most accurate, but highest latency (multiple LLM calls)
- Post-enrichment: Good balance, separates extraction from coding

## 9. Confidence Scoring and Uncertainty Quantification

### Research Foundation

**Key Finding**: Detecting LLM hallucinations is critical for medical applications, where fabricated information can have serious consequences.

**State-of-the-Art Methods** (2024-2025):
- **Semantic Entropy**: Measures consistency across multiple model responses
- **UQLM Toolkit**: Production-ready uncertainty quantification for LLMs
- **Token Probability Analysis**: White-box methods using model logits
- **LLM-as-Judge**: Using second LLM to evaluate outputs

### Confidence Scoring Approaches

**1. Black-Box Uncertainty Quantification**

No access to model internals, rely on stochastic sampling.

**Self-Consistency Method**:
```
Process:
1. Run same extraction prompt 3-5 times (temperature 0.1-0.3)
2. Compare outputs for each entity
3. Calculate agreement rate per entity
4. Confidence = Agreement rate × 100

Example:
Run 1: Extracts "Type 2 Diabetes" with ICD-10 E11.9
Run 2: Extracts "Type 2 Diabetes" with ICD-10 E11.9
Run 3: Extracts "Diabetes Type 2" with ICD-10 E11.9
Run 4: Extracts "Type 2 Diabetes" with ICD-10 E11.9
Run 5: Extracts "Type II Diabetes" with ICD-10 E11.9

Agreement: 5/5 for condition (semantic match), 5/5 for code
Confidence: 100
```

**Cost**: 3-5x API calls, but significantly improves reliability

**Semantic Entropy Method** (Nature, 2024):
- Generate multiple responses
- Measure semantic consistency (not just string matching)
- High entropy = high uncertainty = potential hallucination
- Particularly effective for detecting confabulations

**2. White-Box Uncertainty Quantification**

Access to token probabilities (logits) from model.

**Token Probability Scoring**:
```
Process:
1. Extract with model that returns token probabilities (GPT-4, Claude with API support)
2. Calculate per-token confidence based on probability
3. Aggregate to entity-level confidence

Example:
Entity: "metformin"
Token probabilities: ["met"=0.92, "form"=0.89, "in"=0.94]
Average probability: 0.917
Confidence: 92

Entity: "glipizide" (less common medication)
Token probabilities: ["gli"=0.78, "pi"=0.65, "zide"=0.71]
Average probability: 0.713
Confidence: 71 (flag for review)
```

**Threshold Calibration**:
- >90: High confidence, likely correct
- 75-90: Medium confidence, spot check
- <75: Low confidence, human review required

**3. LLM-as-a-Judge**

Use second LLM to evaluate extraction quality.

**Validation Prompt**:
```
You are a medical quality assurance specialist. Evaluate this extraction:

Original Text: [clinical note]

Extracted Data: [JSON output]

For each extracted entity, assess:
1. Is it explicitly stated in the source text? (Quote supporting text)
2. Is the extracted value accurate? (exact match to source)
3. Is the medical code appropriate for the entity?
4. Confidence (0-100): How certain are you this extraction is correct?

Return: {
  "entity_id": "...",
  "supported": true/false,
  "accurate": true/false,
  "code_appropriate": true/false,
  "confidence": 0-100,
  "reasoning": "..."
}
```

**Research Performance**: LLM-as-judge achieves high correlation with human expert judgments

**4. Ensemble Scoring (UQLM Approach)**

Combine multiple uncertainty quantification methods.

**UQLM Framework** (CVS Health, 2024):
```
Scorers:
1. Semantic Consistency (black-box): Multiple responses, measure agreement
2. Token Probability (white-box): Logit-based confidence
3. LLM-Judge (LLM-based): Second model evaluation
4. Lexical Similarity: Compare to known medical terminology

Ensemble Score: Weighted average of all scorers
  Final_Confidence =
    0.4 × Semantic_Consistency +
    0.3 × Token_Probability +
    0.2 × LLM_Judge +
    0.1 × Lexical_Similarity
```

**Advantages**: More robust than single method, well-calibrated confidence scores

### Hallucination Detection

**Definition**: LLM invents medical information not present in source text.

**Detection Methods**:

**1. Source Attribution Verification**
```
For each extracted entity, require LLM to quote supporting text:

{
  "condition": "Type 2 Diabetes Mellitus",
  "icd10_code": "E11.9",
  "source_quote": "Patient has Type 2 DM",
  "confidence": 95
}

Validation: Verify "source_quote" exists in original text
If quote not found → Hallucination detected
```

**2. Factual Consistency Checking**
```
Prompt: Compare extracted data to source text. Flag any extractions that:
- Mention entities not in source
- Contain values different from source (dates, numbers)
- Make inferences beyond what is stated

Return: {"hallucinated_entities": [...], "factual_inconsistencies": [...]}
```

**3. Medical Plausibility Checks**
```
Automated checks for impossible values:
- Birth date in future
- Age negative or >150
- Heart rate >300 or <20
- Lab values outside physiologically possible ranges
- Contradictory diagnoses (e.g., Type 1 and Type 2 diabetes simultaneously)

If implausible → Likely hallucination or extraction error
```

**4. Uncertainty Head Pre-training** (Research: 2025)

Fine-tuned "uncertainty heads" added to LLM architecture:
- Trained on labeled correct vs incorrect extractions
- Outputs calibrated confidence scores
- Available for popular 7B-9B parameter models
- Can be integrated into extraction pipeline

### Confidence Calibration

**Expected Calibration Error (ECE)**:

Measures how well confidence scores match actual accuracy.

```
Example:
- Items with confidence 80-90: Should be 80-90% accurate
- Items with confidence 60-70: Should be 60-70% accurate

Well-calibrated system: ECE < 0.05
Poorly calibrated: ECE > 0.15

Calibration improves with:
- Temperature tuning
- Confidence score normalization
- Calibration dataset (map raw scores to actual accuracy)
```

### Implementation Recommendations

**Tier 1: Minimum Viable Confidence Scoring**
- Self-consistency check (3 runs, measure agreement)
- Source attribution requirement (quote supporting text)
- Automated plausibility checks
- Cost: 3x inference, robust baseline

**Tier 2: Production-Grade**
- Ensemble scoring (semantic consistency + token probability + LLM-judge)
- Calibrated confidence thresholds
- Automated hallucination detection
- Human review routing based on confidence
- Cost: 4-5x inference, high reliability

**Tier 3: Research/Critical Applications**
- All Tier 2 methods
- Uncertainty quantification heads (if using open models)
- RAG integration for medical knowledge verification
- Multiple LLM cross-validation
- Cost: 5-10x inference, maximum accuracy

### Confidence-Based Routing

```
Confidence Score → Action:

>90: Automatic approval, no review needed
80-90: Spot check random sample (10%)
70-80: Review all extractions, focus on critical fields
60-70: Full human review, flag issues
<60: Reject extraction, manual extraction required

Critical Fields (always review if confidence <90):
- Diagnoses with serious implications (cancer, MI)
- Medication dosages and routes
- Allergies
- Critical lab values
- Surgical procedures
```

## 10. Medical Coding: ICD-10 and CPT Extraction

### Current State of Automated Medical Coding

**Research Findings** (2024-2025):

**Performance Limitations**:
- GPT-4 Exact Match Rates: 45.9% (ICD-9-CM), 33.9% (ICD-10-CM), 49.8% (CPT)
- Current SOTA automated systems fall short of human coder performance
- Complex hierarchical coding remains challenging for LLMs

**Key Challenges**:
1. ICD-10-CM has >70,000 codes (vs ICD-9's ~14,000)
2. Coding requires clinical reasoning, not just entity extraction
3. Specificity requirements (e.g., left vs right, initial vs subsequent encounter)
4. Combination codes (diabetes with complications)
5. Excludes notes and coding guidelines

**Recent Advances**:
- **MedCodER Framework** (2024): Micro-F1 score of 0.60, significantly outperforms prior methods
- **RoBERTa + GPT-4 Assistant**: F1-score of 0.80 for ICD lead term extraction
- Computer-assisted coding shows promise for augmenting human coders

### MedCodER Framework Architecture

**Research**: Generative AI framework for automatic medical coding (arXiv, 2024)

**Pipeline**:

**Step 1: Disease Diagnosis Extraction**
```
Prompt: Extract all disease diagnoses mentioned in this record:

Input: [Clinical note]

Output: {
  "diagnoses": [
    {"disease": "Type 2 Diabetes Mellitus", "supporting_evidence": "HbA1c 9.2%, on metformin"},
    {"disease": "Hypertension", "supporting_evidence": "BP 165/95, on lisinopril"},
    ...
  ]
}
```

**Step 2: Initial Code Retrieval**
```
For each diagnosis:
1. Generate initial ICD-10 codes using LLM medical knowledge
2. Retrieve candidate codes from ICD-10 database via semantic search
3. Create candidate pool (LLM suggestions + database retrievals)
```

**Step 3: Candidate Re-Ranking**
```
LLM re-ranks candidate codes based on:
- Match between diagnosis description and code definition
- Supporting evidence from clinical note
- Specificity requirements
- Excludes notes and coding guidelines

Output: Top-K codes with confidence scores
```

**Results**: Achieves 0.60 micro-F1, significantly better than previous approaches

### ICD-10 Extraction Best Practices

**Approach 1: Lead Term Extraction + Code Lookup**

Research: RoBERTa fine-tuned model achieves F1 0.80 for lead term extraction

**Process**:
```
Step 1: Extract ICD Lead Terms
  Clinical text: "Patient admitted with acute MI, anterior wall, initial encounter"
  Lead term: "myocardial infarction"
  Modifiers: "acute", "anterior wall", "initial"

Step 2: Code Search
  Query ICD-10 database: "acute myocardial infarction anterior"
  Candidates: I21.01, I21.09, I21.4

Step 3: Specificity Selection
  Apply modifiers:
  - Anterior wall: I21.0x
  - Initial encounter: I21.01 (not I21.02 subsequent)

Final: I21.01 - ST elevation myocardial infarction involving anterior wall, initial encounter
```

**Approach 2: Hierarchical Code Assignment**

```
Level 1: Category (e.g., E11 - Type 2 Diabetes)
Level 2: Subcategory (e.g., E11.6 - with other specified complication)
Level 3: Full code (e.g., E11.65 - with hyperglycemia)

LLM Process:
1. Identify disease category from diagnosis
2. Determine if complications/manifestations present
3. Select appropriate subcategory
4. Add specificity (laterality, encounter type, etc.)
```

**Approach 3: RAG with Coding Guidelines**

```
Process:
1. Extract diagnosis from clinical note
2. Retrieve relevant ICD-10 coding guidelines
3. Retrieve "Excludes" notes for candidate codes
4. Retrieve "Code also" notes for combination coding
5. LLM applies guidelines to select appropriate code

Example:
Diagnosis: "Diabetic retinopathy"
Retrieved guideline: "Use additional code to identify type of diabetes (E10-E13)"
Retrieved note: "Code also any associated conditions"
LLM decision:
  Primary: E11.311 (Type 2 diabetes with mild nonproliferative retinopathy)
  Secondary: H36.011 (Diabetic retinopathy, right eye)
```

### CPT Code Extraction

**Procedure Extraction Pipeline**:

**Step 1: Procedure Identification**
```
Extract from clinical notes:
- Procedure name
- Approach/technique
- Body site/laterality
- Extent/complexity
- Duration

Example: "Laparoscopic cholecystectomy performed without complications"
  Procedure: Cholecystectomy
  Approach: Laparoscopic
  Site: Gallbladder
  Complexity: Standard (no complications)
```

**Step 2: CPT Code Mapping**
```
Query CPT database with extracted elements:
  "Laparoscopic cholecystectomy" → 47562

Verify:
- Code description matches procedure
- No additional codes needed (add-ons)
- Modifiers required? (e.g., -LT left side, -RT right side)
```

**Step 3: Bundle and Modifier Logic**
```
Check for:
- Multiple procedures → Modifier -51 (multiple procedures)
- Bilateral → Modifier -50 (bilateral)
- Repeat procedure → Modifier -76 (repeat by same physician)
- CPT bundling rules (some codes include others)
```

**Research Performance**: GPT-4 achieves 49.8% exact match for CPT codes

### Computer-Assisted Coding (CAC) Approach

**Human-in-the-Loop Framework**:

```
AI Role:
- Extract diagnoses and procedures
- Suggest ICD-10/CPT codes with confidence scores
- Highlight supporting evidence from notes
- Flag ambiguous cases

Human Coder Role:
- Review AI suggestions
- Resolve ambiguities
- Apply complex coding guidelines
- Make final code decisions

Performance:
- AI provides 80-90% of codes correctly
- Human focuses on 10-20% requiring expert judgment
- Overall coding time reduced by 40-60%
- Accuracy maintained or improved vs manual coding
```

### Practical Implementation

**Stage 1: Lead Term Extraction**
- High accuracy (F1 ~0.80) with fine-tuned models
- Can use zero-shot LLMs with structured prompts
- Extract all codeable diagnoses and procedures

**Stage 2: Candidate Code Generation**
- LLM generates initial codes
- Semantic search over ICD-10/CPT databases
- Create top-K candidate list (K=5-10)

**Stage 3: Evidence-Based Ranking**
- Re-rank candidates using clinical evidence
- Apply coding guidelines
- Output top-1 or top-3 codes with confidence

**Stage 4: Human Review**
- Confidence >85%: Minimal review
- Confidence 70-85%: Targeted review
- Confidence <70%: Full manual coding

## 11. Validation for Structured Extraction

### Schema Compliance Validation

**Automated Checks**:
- JSON/XML parseable
- All required fields present
- Data types match schema (string vs number vs boolean)
- Enum values from allowed sets
- Date formats consistent (YYYY-MM-DD)
- Numeric values within valid ranges
- No unexpected fields (strict schema enforcement)

**Validation Prompt**:
```
Review this extracted data for schema compliance:

Schema: [schema definition]
Extracted Data: [JSON output]

Check:
1. Are all required fields present?
2. Do all fields match expected data types?
3. Are enum values valid?
4. Are dates in YYYY-MM-DD format?
5. Are numeric values within plausible ranges?
6. Are there any fields not in the schema?

Return: {"compliant": true/false, "errors": [list of specific issues]}
```

### Medical Accuracy Validation

**Code Correctness**:
- ICD-10 codes match condition descriptions
- Code format valid (e.g., E11.9, not e119 or E11-9)
- CPT codes appropriate for documented procedures
- LOINC codes match lab test names

**Medical Plausibility**:
- Vital signs within physiologically possible ranges:
  - Heart rate: 20-300 bpm (flag <40 or >200)
  - Blood pressure: 50-300 systolic, 30-200 diastolic
  - Temperature: 90-110°F (32-43°C)
  - Oxygen saturation: 70-100%
- Lab values within possible ranges (even if abnormal)
- Medication dosages appropriate for route and indication
- Age-appropriate diagnoses and treatments

**Logical Consistency**:
- Medication dosages appropriate for route (oral vs IV)
- Status transitions valid (can't go from resolved → new)
- Treatment after diagnosis, not before
- Lab results correlate with diagnoses
- Medication indications align with diagnosis list

### Cross-Reference Validation

**Source Text Verification**:

Validation prompt:
```
Compare extracted data to source text:

Source: {original_medical_record}
Extracted: {structured_output}

For each extracted entity:
1. Quote the exact source text that supports this extraction
2. Flag any data not found in source text (hallucination)
3. Flag any data that contradicts source text
4. Note any relevant source data that was missed

Return validation report with:
- Verified entities (with source quotes)
- Hallucinated entities (not in source)
- Contradictions (extracted vs source)
- Omissions (in source but not extracted)
```

### Completeness Validation

**Critical Field Check**:
- Diagnoses: Must have condition name and ICD-10 code
- Medications: Must have name, dosage, frequency, route
- Lab results: Must have test name, value, unit
- Procedures: Must have name and date
- Vital signs: Must have value and unit

**Missing Information Handling**:
```
{
  "completeness_score": 85,
  "missing_critical_fields": [
    {"entity": "diagnosis_1", "field": "icd10_code", "severity": "high"},
    {"entity": "medication_2", "field": "frequency", "severity": "high"}
  ],
  "missing_optional_fields": [
    {"entity": "lab_result_1", "field": "reference_range", "severity": "low"}
  ]
}
```

### Confidence Scoring

**Per-Entity Confidence**:
- 90-100: Explicitly stated, unambiguous
- 70-89: Stated but some ambiguity (abbreviations, unclear wording)
- 50-69: Inferred from context, not explicitly stated
- 0-49: Highly uncertain, flag for review

**Overall Extraction Confidence**:
```
Overall Confidence = (
  Σ(entity_confidence × entity_importance_weight) /
  Σ(entity_importance_weight)
)

Importance weights:
- Diagnoses: 10
- Medications: 10
- Allergies: 10
- Lab results: 7
- Procedures: 8
- Vital signs: 5
```

### Validation Output Structure

```
{
  "validation_status": "pass" | "warning" | "fail",
  "overall_confidence": 0-100,
  "schema_compliance": {
    "status": "pass" | "fail",
    "errors": [
      {"field": "diagnoses[0].icd10_code", "issue": "invalid format", "severity": "critical"}
    ]
  },
  "medical_accuracy": {
    "code_accuracy": 0-100,
    "plausibility_score": 0-100,
    "issues": [
      {"entity": "vital_signs.heart_rate", "value": 300, "issue": "implausible", "severity": "critical"}
    ]
  },
  "source_verification": {
    "verified_entities": 42,
    "hallucinated_entities": 0,
    "contradictions": 0,
    "omissions": 3,
    "details": [...]
  },
  "completeness": {
    "score": 85,
    "missing_critical": 2,
    "missing_optional": 5
  },
  "recommendations": [
    "Human review required for: diagnosis code assignment",
    "Verify heart rate measurement from original chart"
  ]
}
```

## 9. Model Selection for Extraction

### Primary Model Criteria

| Criterion | Importance | Why |
|-----------|-----------|-----|
| Structured Output Support | Critical | JSON mode essential for consistent formatting |
| Medical Knowledge | Critical | Accurate entity recognition, code assignment |
| Consistency | Critical | Same input → same output across runs |
| Context Window | High | Handle long medical records (10-50 pages) |
| Reasoning Ability | High | Complex multi-condition cases, relationships |
| Speed | Medium | Affects throughput for batch processing |
| Cost | Medium | Processing thousands of records |

### Recommended Models

**Tier 1: Highest Accuracy** (Critical applications, complex cases)
- **GPT-4**: Excellent structured output, strong medical knowledge, highly consistent
- **Claude 3.5 Sonnet**: Superior long context (200K tokens), excellent medical reasoning
- **Temperature**: 0-0.1
- **Use for**: Oncology records, multi-condition patients, billing/coding, clinical trials

**Tier 2: Balanced** (Standard clinical notes)
- **GPT-4 Turbo**: Good balance of accuracy, speed, and cost
- **Claude 3 Sonnet**: Good accuracy with reasonable cost
- **Temperature**: 0-0.2
- **Use for**: Routine progress notes, standard lab reports, general documentation

**Tier 3: High Volume** (Batch processing, less critical)
- **GPT-4o-mini**: Fast and cost-effective for simple extractions
- **Claude 3 Haiku**: Fastest response times, lowest cost
- **Temperature**: 0-0.2
- **Use for**: Vital signs extraction, simple medication lists, screening

**Tier 4: On-Premise** (Privacy-sensitive, no cloud)
- **Llama-3-70B-Instruct**: Best open-source general model
- **Med-PaLM, BioGPT**: Medical domain-specific models
- **Temperature**: 0-0.1
- **Use for**: HIPAA-sensitive environments, air-gapped systems
- **Trade-off**: Lower accuracy, requires more prompt engineering

### Agent-Specific Model Selection

Different agents can use different models:

```
Agent 1 (Entity Extraction): GPT-4 Turbo (needs balance of accuracy and speed)
Agent 2 (Relationships): Claude 3.5 Sonnet (needs strong reasoning)
Agent 3 (Timeline): GPT-4o-mini (deterministic date ordering, simpler task)
Agent 4 (Code Mapping): GPT-4 (needs strong medical knowledge)
Agent 5 (Validation): Claude 3.5 Sonnet (excellent at critique)
```

### Temperature Settings by Task

- **Entity Extraction**: 0-0.1 (maximum consistency)
- **Relationship Mapping**: 0.2-0.3 (allow slight reasoning flexibility)
- **Timeline Construction**: 0 (deterministic ordering)
- **Code Assignment**: 0 (deterministic mapping)
- **Validation**: 0 (consistent evaluation)

## 10. Implementation Workflow

### Step-by-Step Extraction Process

**Step 1: Document Preprocessing**
- Detect document format (PDF, DOCX, HL7, plain text)
- Extract text (use OCR if scanned)
- Identify document type (progress note, discharge summary, lab report)
- Detect sections (using headers, formatting)
- De-identify PHI if required (remove names, MRNs before LLM)

**Step 2: Schema Selection**
- Choose appropriate schema based on:
  - Document type
  - Intended use (billing, research, EHR integration)
  - Downstream system requirements
- Load schema definition, field constraints, validation rules
- Prepare few-shot examples relevant to document type

**Step 3: Context Analysis**
- Measure document length (character/token count)
- Compare to model context window
- Decision:
  - If fits in window: Single-pass extraction (Pattern A)
  - If moderately long: Chunking strategy
  - If very complex: Multi-stage extraction (Pattern B)
  - If multiple records: Aggregation strategy (Pattern C)

**Step 4: LLM Extraction**
- Select model based on complexity and criticality
- Construct prompt with:
  - Role assignment
  - Complete schema definition
  - Few-shot examples
  - Explicit output formatting requirements
  - Medical record text
- Set temperature: 0-0.2
- Enable JSON mode if available
- Execute extraction (single or multi-agent)
- Capture raw output and metadata (model, timestamp, token usage)

**Step 5: Schema Validation**
- Parse JSON output
- Validate against schema (all required fields, correct types)
- Check date formats, numeric ranges
- Verify enum values
- Flag any schema violations

**Step 6: Medical Validation**
- Verify medical codes (ICD-10, CPT format and appropriateness)
- Check medical plausibility (vital signs, lab values)
- Validate logical consistency (medication-diagnosis alignment)
- Calculate per-entity confidence scores

**Step 7: Source Verification**
- Cross-reference extracted data against original text
- Identify hallucinations
- Find omissions
- Quote supporting text for each entity
- Calculate verification score

**Step 8: Post-Processing**
- Deduplication (if from multiple chunks/records)
- Standardize formatting (uppercase codes, ISO dates)
- Enrichment:
  - Add missing ICD-10 codes via lookup database
  - Standardize medication names (brand → generic)
  - Convert units if needed
- Build relationships (medication → diagnosis links)
- Construct timeline

**Step 9: Quality Review Routing**
- Calculate overall confidence and validation scores
- Route based on scores:
  - **High confidence (>90)**: Automatic approval
  - **Medium confidence (70-90)**: Spot check critical fields
  - **Low confidence (<70)**: Full human review
  - **Validation failures**: Mandatory human review

**Step 10: Output Delivery**
- Format final JSON/XML
- Include metadata:
  - Source document identifier
  - Extraction timestamp
  - Model and version used
  - Confidence scores
  - Validation results
- Provide human review interface if needed
- Log for audit trail

## 11. Quality Assurance

### Metrics to Track

**Accuracy Metrics**:
- **Precision**: % of extracted entities that are correct
- **Recall**: % of actual entities that were extracted
- **F1 Score**: Harmonic mean of precision and recall
- **Field-Level Accuracy**: % of individual fields correct
- **Code Assignment Accuracy**: % of ICD-10/CPT codes correct

**Consistency Metrics**:
- **Same-Input Variance**: Run identical input 5 times, measure differences
- **Schema Compliance Rate**: % of outputs that pass schema validation
- **Format Consistency**: % of dates, codes in correct format

**Completeness Metrics**:
- **Required Field Population**: % of required fields with non-null values
- **Critical Information Capture**: % of must-have entities extracted
- **Omission Rate**: % of entities in source but missed in extraction

**Error Metrics**:
- **Hallucination Rate**: % of extracted entities not in source
- **False Positive Rate**: Incorrect entities extracted
- **False Negative Rate**: True entities missed
- **Critical Error Rate**: Errors affecting clinical decisions or billing

**Performance Metrics**:
- **Processing Time**: Seconds per record
- **Token Usage**: Tokens per record
- **Cost**: Dollars per record
- **Throughput**: Records per hour

### Ground Truth Evaluation

**Creating Gold Standard Dataset**:
1. Select representative sample (50-100 records)
2. Human expert manual extraction
3. Dual-annotation with adjudication
4. Create ground truth structured data
5. Version and maintain gold standard

**Evaluation Process**:
1. Run extraction on gold standard records
2. Compare LLM output to ground truth
3. Calculate all metrics
4. Analyze error patterns
5. Identify improvement opportunities

### Continuous Improvement

**Error Pattern Analysis**:
- Collect all validation failures and human corrections
- Categorize errors:
  - Code assignment errors
  - Missing information
  - Hallucinations
  - Formatting issues
  - Logic errors
- Identify root causes

**Prompt Refinement**:
- Update prompts to address common errors
- Add few-shot examples for problematic cases
- Clarify ambiguous instructions
- Strengthen validation criteria

**Model Updates**:
- Evaluate new model releases on benchmark set
- A/B test prompt variations
- Compare models for specific document types
- Fine-tune if sufficient training data available

**Feedback Loop**:
```
Extraction → Validation → Human Review → Corrections Logged →
Error Analysis → Prompt Updates → Improved Extraction
```

## 12. Common Challenges and Solutions

### Challenge 1: Hallucinated Entities

**Problem**: LLM invents medical information not in source text

**Solutions**:
- Use temperature 0-0.1
- Implement strict source verification agent
- Add to prompt: "Quote the exact text that supports each extraction"
- Few-shot examples showing: "If information is not stated, use null"
- Post-validation cross-reference check

### Challenge 2: Inconsistent Formatting

**Problem**: Dates, codes, values formatted differently across runs

**Solutions**:
- Explicit format specification in prompt
- Provide format examples in few-shot learning
- Enable JSON schema validation in API call
- Post-processing normalization (regex-based)
- Use temperature 0 for maximum determinism

### Challenge 3: Missing Context in Chunks

**Problem**: Entities split across chunk boundaries

**Solutions**:
- 10-15% overlap between chunks
- Section-aware chunking (don't split mid-section)
- Pass forward context: "Previous chunk contained: ..."
- Final consolidation pass to merge split entities
- Maintain entity IDs across chunks for deduplication

### Challenge 4: Ambiguous Abbreviations

**Problem**: Medical abbreviations have multiple meanings (MS = multiple sclerosis or mitral stenosis)

**Solutions**:
- Include abbreviation dictionary in prompt
- Chain-of-thought: "Consider context to disambiguate"
- Use confidence scores: ambiguous → lower confidence
- Flag for human review if confidence <70
- Learn common abbreviations in specific departments

### Challenge 5: Code Assignment Errors

**Problem**: Incorrect ICD-10/CPT codes or invalid code formats

**Solutions**:
- Dedicated code mapping agent
- Integrate with code database/API for validation
- Few-shot examples with correct codes
- Post-processing code format validation
- Human review for uncommon/complex codes

### Challenge 6: Temporal Reasoning Errors

**Problem**: Events ordered incorrectly or duration calculations wrong

**Solutions**:
- Dedicated timeline agent
- Extract all dates first, then order separately
- Validate timeline logic (treatment must follow diagnosis)
- Use structured timeline format
- Cross-check against source for date accuracy

### Challenge 7: Multi-Condition Complexity

**Problem**: Difficult to extract all entities in complex patients with many conditions

**Solutions**:
- Use multi-stage extraction (Pattern B)
- Chain-of-thought reasoning
- Relationship mapping agent
- Break by condition (extract for diabetes, then for HTN, etc.)
- Higher-tier model (GPT-4, Claude Opus) for complex cases

### Challenge 8: Cost at Scale

**Problem**: Extracting thousands of records becomes expensive

**Solutions**:
- Tiered processing:
  - Fast/cheap model first
  - Route low-confidence to better model
- Batch processing where API supports it
- Cache common extractions (same form, different values)
- Consider fine-tuning smaller model for specific use case
- Use cheaper models for simple extractions (vitals only)

## 13. HIPAA Compliance

### LLM Provider Requirements

**Business Associate Agreement (BAA)**:
- Required for any vendor processing PHI
- Azure OpenAI: Offers BAA
- AWS Bedrock: Offers BAA with approved models
- Google Cloud Vertex AI: Offers BAA
- OpenAI API (standard): No BAA available
- Anthropic API (standard): Limited BAA availability

**Data Handling**:
- Data encrypted in transit (TLS 1.2+)
- Data encrypted at rest
- No retention of PHI in vendor logs
- Data residency requirements met (US, EU, etc.)
- Audit logging of all API calls

### De-identification Options

**Pre-Processing De-identification**:
- Remove: Patient names, MRNs, addresses, phone numbers, SSNs
- Redact: Dates (shift by random offset)
- Generalize: Specific ages >89 → "over 89"
- Use before LLM processing for extra safety

**Retain Clinical Relevance**:
- Keep: Medical terminology, diagnoses, medications, lab values
- Preserve: Relative dates ("3 months ago")
- Maintain: Clinical relationships and context

**Re-identification Post-Processing**:
- Map extracted data back to patient identifiers
- Secure ID mapping database
- Access controls and audit trails

### On-Premise Alternatives

For maximum security:
- Self-host open-source models (Llama-3-70B, Medical domain models)
- Deploy within healthcare institution's network
- No data leaves organizational control
- Full audit trail and access control
- Trade-off: Lower accuracy, higher infrastructure costs

## 14. Advanced Techniques

### Self-Consistency Voting

For critical extractions:
1. Run same extraction 3-5 times
2. Vary temperature slightly (0, 0.05, 0.1)
3. Compare outputs
4. Use majority voting for each field
5. Flag fields with disagreement for review

**Benefit**: Catches stochastic errors, improves reliability
**Cost**: 3-5x API calls

### Retrieval-Augmented Extraction

Augment LLM with external medical knowledge:
- ICD-10 code database lookup
- Drug formulary integration
- LOINC code reference
- Clinical guidelines

**Process**:
1. LLM extracts entity (e.g., "diabetes type 2")
2. Query code database for matching ICD-10
3. Return most appropriate code to LLM
4. LLM validates and includes in output

**Benefit**: Improved code accuracy, handles rare conditions

### Confidence-Based Routing

Optimize cost and quality:
1. Use fast/cheap model (GPT-4o-mini) for initial extraction
2. Calculate confidence scores
3. Route low-confidence items (<80) to premium model (GPT-4, Claude Opus)
4. Merge high-confidence and re-processed items

**Benefit**: 60-70% cost reduction with minimal accuracy impact

### Iterative Refinement

Two-pass extraction:
1. Initial extraction with standard prompt
2. Second LLM call: "Review this extraction for errors, omissions, inconsistencies. Provide corrected version."
3. Compare versions, use refined output

**Benefit**: Catches errors missed in first pass
**Cost**: 2x API calls

---

## Conclusion: Research-Backed Best Practices

This framework synthesizes cutting-edge research (2024-2025) on LLM-based medical information extraction. Key findings demonstrate that modern LLMs can achieve near-human performance on clinical NER tasks when properly engineered, while still facing challenges in complex medical coding.

### Research-Validated Performance Expectations

**Entity Extraction**:
- GPT-4 zero-shot: F1 ~70-75% on i2b2 benchmarks
- GPT-4 few-shot (5 examples): F1 ~80-85%, approaching supervised models
- GPT-4o with prompt ensemble: F1 ~95%, recall 98% (highest reported)
- Open-source Llama-3-70B: Competitive performance, viable for on-premise deployment

**Medical Coding**:
- ICD-10 exact match: 34-46% for current LLMs (still below human performance)
- Lead term extraction: F1 ~80% (strong first step)
- MedCodER framework: 60% micro-F1 (state-of-the-art automated coding)
- Recommendation: Computer-assisted coding (AI suggests, human validates) most practical

**RAG Integration Impact**:
- Zero-shot performance boost: DiRAG + GPT-4 achieves SOTA on benchmarks
- Code accuracy improvement: 45% → 65% with UMLS integration
- Inference efficiency: 70% token reduction with CLEAR method
- Disambiguation: >80% accuracy on ambiguous medical abbreviations

### Framework Requirements

**1. Schema-Driven Architecture**
- Define explicit JSON/XML schemas with field-level constraints
- Use industry standards (FHIR, HL7) where applicable
- Validate all outputs against schema rigorously
- Benchmark against i2b2/n2c2 datasets for evaluation

**2. Temperature Optimization**
- Entity extraction: 0-0.1 (maximum determinism)
- Relationship mapping: 0.2-0.3 (slight reasoning flexibility)
- Always <0.2 for schema-compliant structured output

**3. Prompt Engineering Excellence**
- Few-shot examples: 2-4 examples yield 10-15% F1 improvement
- Strategic example selection: Diverse cases > random selection
- Prompt framework: Entity definitions + annotation guidelines + examples
- Research shows: Prompt engineering can yield 20% performance gains

**4. Confidence Scoring & Hallucination Detection**
- Implement black-box (self-consistency) or white-box (token probability) methods
- LLM-as-judge for validation (high correlation with human experts)
- Ensemble approaches (UQLM framework) for production robustness
- Source attribution requirement to detect hallucinations
- Confidence-based routing: >90% auto-approve, <70% human review

**5. RAG-Augmented Extraction**
- UMLS/SNOMED CT integration significantly improves accuracy
- Three architectures: Pre-retrieval, iterative, post-enrichment
- Best for: Zero-shot performance, rare conditions, code assignment, disambiguation
- Practical: Post-enrichment offers best balance of accuracy and complexity

**6. Multi-Agent Specialization**
- Agent 1: Entity Extraction (completeness focus)
- Agent 2: Relationship Mapping (reasoning focus)
- Agent 3: Timeline Construction (temporal logic focus)
- Agent 4: Medical Code Mapping (knowledge base integration)
- Agent 5: Validation & QA (error detection focus)
- Research shows: Specialized agents outperform monolithic approaches

**7. Comprehensive Validation Pipeline**
- Schema compliance: Automated JSON validation
- Medical accuracy: Code correctness, plausibility checks
- Source verification: Cross-reference all extractions against original text
- Confidence calibration: ECE < 0.05 for well-calibrated systems
- Hallucination detection: Semantic entropy, factual consistency checking

**8. Benchmark-Driven Evaluation**
- Test on standard datasets: i2b2, n2c2, NCBI Disease, BC5CDR
- Track precision, recall, F1 at entity and field levels
- Monitor exact match rates for medical codes
- Measure confidence calibration (predicted vs actual accuracy)
- Compare zero-shot vs few-shot vs fine-tuned performance

### Implementation Tiers

**Tier 1: Minimum Viable Product**
- Single-pass extraction with GPT-4
- 2-4 few-shot examples in prompt
- Basic schema validation
- Self-consistency scoring (3 runs)
- Cost: 3x inference, F1 ~75-80%

**Tier 2: Production Grade**
- Multi-stage extraction pipeline
- RAG integration with UMLS (post-enrichment)
- Ensemble confidence scoring
- Automated hallucination detection
- Human-in-the-loop for confidence <80%
- Cost: 4-5x inference, F1 ~85-90%

**Tier 3: Research/Critical Applications**
- Multi-agent architecture (5 specialized agents)
- Iterative RAG with UMLS + SNOMED CT
- Multiple LLM cross-validation
- Uncertainty quantification heads (if open models)
- Strict human review protocols
- Cost: 5-10x inference, F1 >90%

### Key Success Factors

**Based on 2024-2025 Research Literature**:

1. **Prompt Engineering > Model Size**: Well-engineered prompts with GPT-4 outperform naive prompts with larger models
2. **Few-Shot Learning Essential**: 15-20% improvement with just 5 well-chosen examples
3. **RAG Integration Critical**: Especially for rare entities, medical coding, disambiguation
4. **Validation Non-Negotiable**: Hallucinations occur; strict validation prevents errors from propagating
5. **Domain Knowledge Matters**: UMLS/SNOMED CT integration consistently improves accuracy
6. **Human-in-the-Loop Optimal**: Computer-assisted approach (AI suggests, human validates) most practical for high-stakes applications
7. **Confidence Calibration Key**: Knowing when LLM is uncertain enables intelligent routing
8. **Benchmark Against Standards**: Use i2b2/n2c2 datasets to measure real performance

### Current Limitations and Future Directions

**Present Challenges**:
- Medical coding accuracy (ICD-10: 34-46%) still below human coders
- Complex hierarchical reasoning (combination codes, excludes notes)
- Long-tail rare conditions require extensive medical knowledge
- Hallucination risk in zero-shot scenarios
- Cost at scale for high-volume applications

**Emerging Solutions**:
- Fine-tuned uncertainty heads for better calibration
- Medical graph RAG for complex relationship extraction
- Multi-modal processing (text + imaging integration)
- Specialized domain models (Med-PaLM, BioGPT evolution)
- Agentic frameworks (Infherno for FHIR synthesis)

### Target Performance Metrics

For a production-grade system processing clinical notes:

**Entity Extraction**:
- Precision: >90% (few false positives)
- Recall: >85% (captures most entities)
- F1 Score: >87% (balanced performance)

**Medical Coding**:
- ICD-10 top-1 accuracy: >60% (state-of-the-art)
- ICD-10 top-3 accuracy: >80% (human can select from candidates)
- Lead term extraction: >80% F1

**System Quality**:
- Hallucination rate: <5% of extractions
- Confidence calibration ECE: <0.05
- Schema compliance: >98%
- Processing throughput: 50-100 records/hour (depending on complexity)

### Final Recommendation

Structured medical data extraction with LLMs is **viable for production** with proper engineering:

- Use **few-shot GPT-4** or **Claude 3.5 Sonnet** for core extraction
- Integrate **UMLS via RAG** for code assignment and disambiguation
- Implement **confidence scoring** and route low-confidence items to human review
- Validate **everything** against source text and medical plausibility
- Benchmark against **i2b2/n2c2 datasets** to measure real-world performance
- For medical coding, adopt **computer-assisted** approach (not fully automated)

The goal is machine-readable, accurate, complete structured data that downstream systems can confidently use for clinical decision support, billing, research, and population health analytics. With research-validated techniques, modern LLMs can achieve this goal for 80-90% of extractions automatically, with human review ensuring quality for the remaining 10-20%.

### Key References

1. BMC Medical Research Methodology (2025): Multiple LLM performance evaluation for EHR data extraction
2. Nature Digital Medicine (2024): Privacy-preserving LLMs, CLEAR method for entity augmented retrieval
3. JMIR (2024): Entity extraction pipeline study
4. Oxford Academic JAMIA (2024): Clinical NER prompt engineering framework
5. arXiv (2024): MedCodER framework, DiRAG for zero-shot NER
6. arXiv (2025): Infherno framework for FHIR synthesis, LLM-based prompt ensemble
7. Nature (2024): Semantic entropy for hallucination detection
8. CVS Health: UQLM toolkit for uncertainty quantification
