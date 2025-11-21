---
marp: false
theme: default
paginate: true
---

# The LLM in KFSYSCC and the Future Plan

**Presentation Duration:** 40 minutes
**Presenter:** Max
**Audience:** IT Company Managers
**Date:** 2025/11/21

---

## Presentation Outline (40 minutes)

1. **Introduction** (3 min)
2. **Current LLM Infrastructure** (8 min)
3. **LLM Applications in Production** (12 min)
4. **Future Plans** (12 min)
5. **Lessons Learned & Recommendations** (3 min)
6. **Discussion with Q&A** 

---

## 1. Introduction (3 minutes)

### About This Presentation
- Focus: LLM implementation journey at Koo Foundation Sun Yat-Sen Cancer Center
- Goal: Share practical insights and lessons learned
- Audience benefit: Real-world implementation strategies for healthcare IT

### Why LLMs for Healthcare?
- Healthcare generates massive amounts of unstructured text data
- Clinical documentation is time-consuming for healthcare professionals
- Cancer care requires complex decision-making with multiple data sources
- Opportunity to improve efficiency and quality of care

---

## 2. Current LLM Infrastructure (8 minutes)

### Cloud LLM Services
**Azure OpenAI Service**
- Primary platform for GPT models
- Enterprise-grade security and compliance
- Integration with existing Azure infrastructure
- Used for: ChatGPT API services at chatgpt.kfsyscc.org

**Google Vertex AI**
- Secondary platform for model diversity
- Access to Gemini and other Google models
- Flexible deployment options

### Local LLM Infrastructure
**Self-hosted Llama 3.x Models**
- Deployed locally for sensitive data processing
- Benefits:
  - Data privacy and control
  - Reduced API costs for high-volume tasks
  - No internet dependency for critical operations
- Use case: Internal text processing at chatgpt.kfsyscc.org

### Hybrid Approach Strategy
**Why Both Cloud and Local?**
- Cloud: Advanced capabilities, latest models, scalability
- Local: Data sensitivity, cost control, offline capability
- Flexibility to choose based on use case requirements

**Architecture Overview**
```
┌─────────────────────────────────────────────────┐
│           KFSYSCC LLM Infrastructure            │
├─────────────────────────────────────────────────┤
│                                                 │
│  Cloud Services          Local Inference       │
│  ├─ Azure OpenAI        ├─ Llama 3.x Models   │
│  └─ Google Vertex AI    └─ GPU Servers        │
│                                                 │
│  Applications Layer                            │
│  ├─ GitHub Copilot                            │
│  ├─ chatgpt.kfsyscc.org                       │
│  └─ Medical Note System                       │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 3. LLM Applications in Production (12 minutes)

### Application 1: GitHub Copilot for Development (2024)
**Implementation**
- Deployed across IT department
- Integration with existing development workflow

**Use Cases**
- Code generation: Accelerate development of new features
- Code review: Automated code quality checks
- Documentation: Generate and maintain code documentation

**Impact**
- Improved developer productivity
- Faster code review cycles
- Better code quality and consistency

---

### Application 2: Internal ChatGPT Portal (chatgpt.kfsyscc.org)

**Platform Overview**
- Web-based interface for hospital staff
- Hybrid backend: Azure ChatGPT API + Local Llama 3.x
- Internal use for text processing tasks

**Key Features**
- Medical record summarization
- Text translation and processing
- Ad-hoc queries and information retrieval

**Prompt Management System**

*User-Defined Prompts*
- Users can create and save their own custom prompts
- Personalized workflows for specific tasks
- Examples:
  - Radiologist's imaging report template
  - Oncologist's treatment summary format

*Global Prompts*
- Hospital-wide standardized prompts available to all users
- Curated by IT and clinical departments
- Ensures consistency across departments
- Examples:
  - Standard EMR summary format
  - Lab result interpretation assistant

**Benefits of Prompt Management**
- Improved consistency in documentation
- Reduced time to create effective prompts
- Knowledge sharing across departments
- Quality control through standardized templates
- Easy onboarding for new users

**Technical Architecture**
- Frontend: Web interface
- Backend: API routing layer
- Model selection: Automatic based on task requirements
- Prompt library: Centralized storage with version control

**Security & Privacy**
- Internal network only
- User authentication and authorization
- Audit logging for compliance
- Prompt usage tracking and analytics

---

### Application 3: Medical Note System (Go Production in 2025)

**Background**
- Developed by Dr. Lin
- Addresses physician burnout from documentation burden
- Leverages LLMs for clinical documentation efficiency

**Development Story: AI-Assisted Development**
- Dr. Lin used natural language to communicate with Claude Code
- Generated React.js frontend through conversation
- IT engineer integrated frontend with backend API
- Example of how LLMs enable non-programmers to create solutions

**Core Capabilities**

1. **Lab Data Summarization**
   - Automatically summarize complex lab results
   - Highlight abnormal values and trends
   - Generate clinical interpretations

2. **Nursing Note Translation**
   - Translate Chinese nursing notes to English
   - Maintain medical accuracy and context
   - Support international collaboration and research

3. **Report Consolidation**
   - Merge multiple reports into single comprehensive note
   - Maintain temporal relationships
   - Extract key clinical findings

4. **Medical Record Summarization**
   - Condense lengthy patient histories
   - Highlight relevant oncology information
   - Generate admission/consultation notes

**User Experience**
- Intuitive web interface
- Real-time processing
- Review and edit capabilities
- Integration with existing workflows

**Clinical Impact**
- Reduced documentation time for physicians
- Improved note quality and completeness
- More time for patient care
- Better information synthesis

**Technical Implementation**
- React.js frontend (AI-generated)
- REST API backend
- LLM integration layer
- EMR system integration

---

## 4. Future Plans (12 minutes)

### Part A: Healthcare LLM Applications

#### 1. Nurse Handover Note Summarization (In Progress)
**Challenge**
- Nurses spend significant time on handover documentation
- Critical information may be missed during shift changes
- Inconsistent note quality

**Solution**
- Automated summarization of patient status
- Highlight critical changes and alerts
- Standardized handover format

**Expected Benefits**
- Reduced nursing documentation burden
- Improved continuity of care
- Fewer handover errors

**Timeline**
- Currently in development phase
- Pilot testing planned for Q1/Q2 2025

---

#### 2. Clinical Trial Screening (Planning Phase)
**Opportunity**
- Cancer patients often eligible for multiple trials
- Manual screening is time-consuming and complex
- May miss eligible patients

**Proposed Solution**
- LLM-based matching of patient profiles to trial criteria
- Automated eligibility screening
- Alert system for suitable trials

**Challenges to Address**
- Accuracy and reliability requirements
- Integration with trial databases
- Regulatory compliance

---

#### 3. Cancer Registry Data Extraction (Planning Phase)
**Current Situation**
- Cancer registry requires structured data from unstructured notes
- Manual abstraction is labor-intensive
- Data quality varies

**LLM Application**
- Extract structured cancer data from clinical notes
- Auto-populate registry fields
- Quality assurance checks

**Benefits**
- Reduced registry staff workload
- Improved data completeness
- Faster reporting to national registry

---

#### 4. EMR Quality Assurance (Planning Phase)
**Problem**
- Incomplete or inconsistent documentation
- Difficult to audit at scale
- Quality issues discovered late

**LLM Solution**
- Automated chart review for completeness
- Flag missing critical information
- Suggest improvements to documentation

**Implementation Considerations**
- Define quality metrics
- User acceptance and workflow integration
- Handling false positives

---

#### 5. Guideline Compliance Checking (Planning Phase)
**Cancer Care Challenge**
- Multiple clinical guidelines (NCCN, ASCO, local protocols)
- Guidelines frequently updated
- Difficult to ensure consistent adherence

**Proposed System**
- Real-time guideline checking during treatment planning
- Alert for deviations with explanations
- Support clinical decision-making

**Technical Approach**
- Encode guidelines in structured format
- LLM-based interpretation of clinical context
- Integration with order entry system

**Value Proposition**
- Improved adherence to evidence-based care
- Reduced variations in treatment
- Educational tool for trainees

---

### Part B: IT Department Innovation

#### Infrastructure Development

**1. MCP (Model Context Protocol) Services**
**What is MCP?**
- Standardized protocol for LLM-application integration
- Developed by Anthropic
- Enables modular, reusable LLM capabilities

**Our MCP Implementation Strategy**
- Build reusable building blocks for LLM applications
- Standardize integration patterns
- Enable rapid application development

**Current MCP Servers in Production**

We have already implemented **4 foundational MCP servers**:

1. **Search MCP** - Search capabilities across various data sources
2. **Fetch MCP** - HTTP requests to retrieve data from APIs
3. **SendMail MCP** - Email notification and communication
4. **SQLite MCP** - Database query and data access

**Real-World Example: Pathology Report Data Extraction**
```
┌──────────────────────────────────────────────┐
│   AI Agent for Pathology Data Extraction    │
├──────────────────────────────────────────────┤
│                                              │
│  User Request: Extract tumor staging data   │
│         ↓                                    │
│  AI Agent (with LLM)                        │
│         ↓                                    │
│  Fetch MCP Server                           │
│         ↓                                    │
│  Pathology Report API                       │
│         ↓                                    │
│  Free-text pathology report                 │
│         ↓                                    │
│  LLM extracts structured data:              │
│  - Tumor size: 2.5 cm                       │
│  - Stage: T2N1M0                            │
│  - Grade: Moderately differentiated         │
│  - Margins: Negative                        │
│                                              │
└──────────────────────────────────────────────┘
```

**Why This Matters**
- Easy integration: Combine Fetch MCP + Pathology API = Instant AI agent
- No custom code for API integration
- Reusable across different report types
- Standardized approach for all future agents

**Planned Additional MCP Services**
```
┌────────────────────────────────────────┐
│    Future MCP Services Layer           │
├────────────────────────────────────────┤
│ ├─ EMR Data Access MCP                │
│ ├─ Medical Knowledge Base MCP         │
│ ├─ Clinical Guideline MCP             │
│ ├─ Medical Terminology MCP            │
│ ├─ Document Processing MCP            │
│ └─ Audit & Logging MCP                │
└────────────────────────────────────────┘
```

**Key Benefits of MCP**

1. **Standardized AI Integration**
   - Universal standard for AI-data connections
   - Works with any AI model without structural changes
   - Reduces development overhead significantly

2. **Extended AI Capabilities**
   - Enables AI to perform real-world tasks (file operations, database queries, web scraping)
   - Transforms AI from chatbot to interactive agent
   - Real-time access to tools and data sources

3. **Reduced Complexity & Cost**
   - No custom code needed for each data source or model
   - AWS reports up to 30% reduction in development and maintenance costs
   - Significantly lower computational overhead

4. **Better Context & Accuracy**
   - External state management maintains session context and user history
   - Direct access to factual data reduces hallucinations
   - Real-time data queries ensure up-to-date responses

5. **Enhanced Security**
   - Central point for data access management
   - Minimizes data leak risks
   - Consistent security and governance policies across all AI interactions

**Our Implementation Benefits**
- Accelerated development of new applications
- Consistent security and compliance implementation
- Easier maintenance and updates
- Reusable across multiple projects
- Transform AI assistants into powerful agents that interact with hospital systems securely

---

#### 2. Local LLM Model Expansion

**Current State**
- Llama 3.x models in production
- Limited GPU resources

**Expansion Plans**
- Deploy additional open-source models
  - Specialized medical models
  - Multilingual models (Chinese-English)
  - Smaller models for specific tasks
- Model evaluation and benchmarking framework
- Model fine-tuning capabilities for hospital-specific use cases

**Model Selection Criteria**
- Performance on medical tasks
- Chinese language support
- Resource requirements
- Licensing and commercial use

---

#### 3. High-Performance GPU Infrastructure

**Hardware Survey and Acquisition**
**Current Challenge**
- Growing demand for local inference
- Performance requirements for real-time applications
- Cost constraints

**Infrastructure Plans**
- Survey latest GPU options (H100, A100, alternatives)
- Cost-benefit analysis: cloud vs. local
- Scalable architecture for future growth

**Planned Capabilities**
- Increased inference throughput
- Support for larger models
- Fine-tuning infrastructure
- Development/testing environment

**Architecture Considerations**
```
┌──────────────────────────────────────────┐
│     GPU Infrastructure Architecture      │
├──────────────────────────────────────────┤
│                                          │
│  Production Tier                         │
│  ├─ High-availability inference servers  │
│  └─ Load balancing                       │
│                                          │
│  Development Tier                        │
│  ├─ Model training/fine-tuning          │
│  └─ Testing and validation              │
│                                          │
│  Management Layer                        │
│  ├─ Model versioning                    │
│  ├─ Monitoring and logging              │
│  └─ Resource allocation                 │
│                                          │
└──────────────────────────────────────────┘
```

---

#### 4. Building LLM Capabilities Framework

**Objective**
- Create reusable components for rapid application development
- Standardize LLM integration patterns
- Enable clinical teams to request and deploy solutions faster

**Framework Components**

1. **Prompt Engineering Library**
   - Tested prompts for common medical tasks
   - Version control and A/B testing
   - Multilingual prompt templates

2. **Evaluation & Testing Suite**
   - Automated testing for medical accuracy
   - Bias and safety checks
   - Performance benchmarking

3. **Deployment Pipeline**
   - Containerized deployment
   - CI/CD for LLM applications
   - Rollback capabilities

4. **Monitoring & Observability**
   - Usage metrics and analytics
   - Quality monitoring
   - Cost tracking

---

#### 5. Vibe Coding Workflow (Pilot Program)

**Vision: AI-Driven Development Pipeline**
Transform software development from manual coding to specification-driven automation

**Workflow Overview**
```
┌─────────────────────────────────────────────────────────┐
│          Vibe Coding Development Workflow               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Step 1: Requirements Gathering                        │
│  └─ User requirements + Usage scenarios                │
│                                                         │
│  Step 2: AI-Generated Specifications                   │
│  ├─ API specifications (endpoints, data models)        │
│  └─ UI specifications (components, workflows)          │
│           ↓                                             │
│  Step 3: Automated Implementation                      │
│  ├─ Generate code within provided framework            │
│  ├─ Follow architectural patterns                      │
│  └─ Integrate with existing systems                    │
│           ↓                                             │
│  Step 4: Automated Testing                             │
│  ├─ Generate test cases                                │
│  ├─ Generate test code                                 │
│  └─ Execute automated tests                            │
│           ↓                                             │
│  Step 5: Developer Review                              │
│  ├─ Review specifications                              │
│  ├─ Analyze test results                               │
│  └─ Approve or request modifications                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Developer Role Transformation**
*From:* Manual coding and implementation
*To:* Specification review and quality assurance

**Traditional vs. Vibe Coding**
| Aspect | Traditional | Vibe Coding |
|--------|------------|-------------|
| Developer Focus | Writing code | Reviewing specs & tests |
| Time Allocation | 70% coding, 30% testing | 30% review, 70% value-add |
| Iteration Speed | Days to weeks | Hours to days |
| Code Consistency | Variable | Framework-enforced |
| Testing Coverage | Manual effort | Auto-generated |

**Expected Benefits**

1. **Reduced IT Resource Requirements**
   - Automate repetitive coding tasks
   - Enable faster development with smaller teams
   - Free developers for complex problem-solving

2. **Accelerated Software Delivery**
   - Rapid prototyping from requirements to working code
   - Faster iteration cycles
   - Quicker time-to-production

3. **Improved Code Quality**
   - Consistent adherence to framework patterns
   - Comprehensive automated testing
   - Reduced human error in implementation

4. **Better Documentation**
   - AI-generated specifications serve as documentation
   - Clear traceability from requirements to code
   - Easier maintenance and knowledge transfer

**Implementation Strategy**

*Phase 1: Pilot (Q2-Q3 2025)*
- Select small, well-defined projects
- Establish development framework and patterns
- Train team on specification review processes
- Measure productivity metrics

*Phase 2: Refinement (Q4 2025)*
- Iterate based on pilot learnings
- Expand framework capabilities
- Develop best practices guide
- Build internal case studies

*Phase 3: Scale (2026)*
- Roll out to additional projects
- Train broader development team
- Integrate with existing CI/CD pipeline
- Measure ROI and efficiency gains

**Key Success Factors**
- Well-defined architectural framework
- Clear coding standards and patterns
- Robust testing infrastructure
- Developer buy-in and training
- Iterative improvement process

**Challenges to Address**
- Ensuring AI-generated code meets security standards
- Handling complex edge cases
- Maintaining human oversight and accountability
- Balancing automation with developer expertise
- Integration with existing systems and workflows

---

### Implementation Roadmap

**Q1 2025**
- Complete nurse handover note system
- Deploy additional MCP services
- Begin GPU infrastructure upgrade

**Q2 2025**
- Pilot clinical trial screening
- Launch cancer registry extraction pilot
- Expand local model capabilities

**Q3-Q4 2025**
- Scale successful pilots
- Deploy EMR quality assurance
- Begin guideline compliance system development

---

## 5. Lessons Learned & Recommendations (3 minutes)

### Key Lessons from Our Journey

#### 1. Start with Clear, Measurable Use Cases
**Our Experience**
- Medical note system succeeded because it solved specific pain point
- Clear value proposition: save physician time
- Measurable: time saved per note

**Recommendation**
- Don't try to "boil the ocean"
- Identify high-impact, well-defined problems
- Ensure user buy-in before development

---

#### 2. Hybrid Cloud-Local Strategy is Essential
**Why It Works**
- Flexibility for different security requirements
- Cost optimization for high-volume tasks
- Risk mitigation if one platform has issues

**Recommendation**
- Evaluate each use case for cloud vs. local deployment
- Build infrastructure for both
- Consider data sensitivity and compliance requirements

---

#### 3. Involve Clinical Users Early and Often
**Dr. Lin's Note System Success**
- Designed by a physician who understands workflow
- AI tools (Claude Code) enabled rapid prototyping
- Resulted in high user adoption

**Recommendation**
- Co-design with end users
- Rapid iteration based on feedback
- Consider low-code/no-code tools for user-led development

---

#### 4. AI Can Democratize Software Development
**Our Discovery**
- Non-programmers can create functional applications
- Dr. Lin generated React.js frontend using Claude Code
- Reduces dependency on IT backlog

**Recommendation**
- Provide AI coding tools to clinical staff
- Create templates and frameworks for common patterns
- IT focuses on integration, security, and production deployment

---

#### 5. Quality and Safety Must Be Built In
**Critical for Healthcare**
- LLM outputs must be reviewed by humans
- Need clear escalation for uncertain cases
- Audit trails for compliance

**Recommendation**
- Design human-in-the-loop workflows
- Implement monitoring and alerting
- Regular accuracy assessments
- Clear policies on LLM use in clinical care

---

#### 6. Infrastructure Investment Pays Off
**Building Blocks Approach**
- MCP services enable rapid development
- Reusable components reduce duplication
- Standardization improves security and compliance

**Recommendation**
- Invest in foundational infrastructure early
- Think in terms of platforms, not just applications
- Balance quick wins with long-term architecture

---

#### 7. Manage Expectations and Communicate Limitations
**Reality Check**
- LLMs are not perfect
- Hallucinations can occur
- Some tasks are not suitable for current LLMs

**Recommendation**
- Be transparent about capabilities and limitations
- Set realistic expectations with stakeholders
- Start with augmentation, not replacement of human expertise

---

### Recommendations for IT Managers

**If You're Just Starting**
1. Begin with non-clinical use cases (like GitHub Copilot)
2. Build team expertise gradually
3. Establish governance and ethical guidelines early
4. Start with cloud services for faster time-to-value

**If You're Scaling**
1. Invest in local infrastructure for cost and control
2. Build reusable platforms and frameworks
3. Create centers of excellence for LLM development
4. Develop comprehensive evaluation frameworks

**Critical Success Factors**
- Executive sponsorship and vision
- Clinical-IT partnership
- Iterative, agile approach
- Focus on user adoption and change management
- Continuous learning and adaptation

---

## 6. Conclusion & Key Takeaways (2 minutes)

### Our Journey So Far
- Started with developer tools (GitHub Copilot)
- Expanded to clinical applications (note system)
- Built hybrid infrastructure (cloud + local)
- Learned valuable lessons about implementation

### Where We're Going
- Broader healthcare applications in development
- Infrastructure scaling for future growth
- Building reusable LLM capabilities
- Positioning for AI-enabled cancer care

### Key Messages for IT Managers

1. **LLMs are transforming healthcare IT** - Real impact today, not just future potential

2. **Hybrid approach provides flexibility** - Balance cloud innovation with local control

3. **User-centric design is critical** - Clinical staff involvement ensures adoption

4. **Infrastructure investment enables scale** - Building blocks accelerate future applications

5. **Start now, but start smart** - Clear use cases, measurable outcomes, iterative approach

### The Opportunity
- Healthcare has massive potential for LLM applications
- First movers can establish significant advantages
- Technology is ready; focus on implementation and adoption
- Learn from each other's experiences

---

## Q&A (2 minutes)

**Contact Information**
[Your Name]
[Your Title]
Koo Foundation Sun Yat-Sen Cancer Center
Email: [your-email]

**Thank you for your attention!**

---

