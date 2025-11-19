# Self-Hosted LLM Selection Guide: A Practical Engineering Guide

## Table of Contents
1. [Introduction: Why Self-Host?](#1-introduction-why-self-host)
2. [Quick Decision Framework](#2-quick-decision-framework)
3. [Selection Criteria](#3-selection-criteria)
4. [Model Comparison by Use Case](#4-model-comparison-by-use-case)
5. [Hardware Requirements Guide](#5-hardware-requirements-guide)
6. [Recommended Models by Category](#6-recommended-models-by-category)
7. [Deployment Architecture](#7-deployment-architecture)
8. [Cost Analysis](#8-cost-analysis)
9. [Step-by-Step Selection Process](#9-step-by-step-selection-process)
10. [Production Deployment Checklist](#10-production-deployment-checklist)
11. [Troubleshooting and Optimization](#11-troubleshooting-and-optimization)
12. [References and Tools](#12-references-and-tools)

## 1. Introduction: Why Self-Host?

### When Self-Hosting Makes Sense

Self-hosting open-source LLMs is the right choice when you face one or more of these scenarios:

**✅ You Should Self-Host If:**
- Processing **>10M tokens daily** (cost crossover point vs APIs)
- Handling **sensitive data** (healthcare, finance, legal, government)
- Need **predictable costs** and budget control
- Required to meet **data localization** regulations (GDPR, HIPAA)
- Want to **fine-tune** on proprietary data without sharing
- Need **guaranteed availability** and no rate limits
- Operating in **air-gapped environments**
- Building **latency-sensitive applications** (local inference < 50ms)

**❌ Stick with APIs If:**
- Processing **<1M tokens daily** (APIs are cheaper)
- **Rapid prototyping** phase without production requirements
- **Limited ML expertise** in your team
- **No hardware infrastructure** and unwilling to invest
- Need **cutting-edge performance** at any cost (GPT-4/Claude still lead)
- **Experimentation** without commitment

### The Self-Hosting Value Proposition

**Cost Savings:** Running Llama-3-70B costs ~$0.60/M tokens vs $10-30/M for GPT-4 (10-50x savings at scale)

**Performance Gap Closing:** Open-source models now trail proprietary by only ~1.7% on benchmarks (down from 8% a year ago)

**Total Control:** Customize, modify, and deploy exactly where and how you need

## 2. Quick Decision Framework

### Decision Tree

```
START: What's your primary use case?
│
├─ Code Generation/Review
│  ├─ Simple autocomplete → DeepSeek-Coder 7B, CodeGemma 7B
│  ├─ Complex refactoring → DeepSeek-Coder 33B, Code Llama 70B
│  └─ Multi-language + explanation → Qwen 2.5 Coder 32B
│
├─ General Chat/Assistant
│  ├─ Customer support → Llama 3.3 70B, Qwen 2.5 72B
│  ├─ Internal tools → Mistral 7B, Gemma 2 9B
│  └─ Enterprise-grade → Command R+ 104B, Llama 3.1 405B
│
├─ RAG/Document Q&A
│  ├─ Short docs (<10K tokens) → Mistral 7B, Gemma 2 9B
│  ├─ Long context (>32K) → Command R 35B, Qwen 2.5 72B
│  └─ Multilingual docs → Command R+ 104B, Qwen 2.5 72B
│
├─ Specialized Domain
│  ├─ SQL generation → Snowflake Arctic, DBRX
│  ├─ Math/reasoning → DeepSeek V3, Qwen 2.5
│  ├─ Multilingual → BLOOM 176B, Qwen 2.5, Yi-34B
│  └─ Vision + text → PaliGemma 2, Yi-VL-34B
│
└─ What's your hardware budget?
   ├─ Laptop/Single GPU (16-24GB) → 7B models quantized
   ├─ Workstation (40-80GB) → 13-34B models, 70B quantized
   ├─ Single server (1-2x A100) → 70B full precision, 405B quantized
   └─ Multi-GPU cluster → 70B+ full precision, 405B, MoE models
```

### Quick Reference Table

| Use Case | Recommended Size | Top 3 Models | Min Hardware |
|----------|------------------|--------------|--------------|
| **Code completion** | 7-13B | DeepSeek-Coder 7B, CodeGemma 7B, StarCoder2 15B | 16GB GPU |
| **General chat** | 7-70B | Llama 3.3 70B, Qwen 2.5 72B, Mistral 7B | 24GB-140GB GPU |
| **RAG/document Q&A** | 7-35B | Command R 35B, Mistral 7B, Qwen 2.5 32B | 16GB-70GB GPU |
| **SQL generation** | 30-480B MoE | Snowflake Arctic, DBRX, DeepSeek V3 | 80GB+ GPU |
| **Math/reasoning** | 34-671B | DeepSeek V3, Qwen 2.5, DeepSeek-R1 | 80GB+ GPU |
| **Multilingual** | 34-176B | BLOOM 176B, Qwen 2.5 72B, Yi-34B | 80GB+ GPU |

## 3. Selection Criteria

### 3.1 Use Case Requirements

**Task Complexity Assessment:**
- **Simple tasks** (classification, basic QA): 7B-13B models sufficient
- **Medium complexity** (summarization, code completion): 13B-34B recommended
- **Complex tasks** (reasoning, multi-step problems): 34B-70B+ required
- **Specialized domains** (legal, medical, finance): Fine-tuned 13B-70B models

**Context Length Needs:**
- **Short context** (<4K tokens): Most 7B-13B models work well
- **Medium context** (8K-32K): Llama 3.x, Mixtral, Qwen, Yi models
- **Long context** (64K-128K): Llama 3.1 405B, Gemma 3, Command R+, Qwen 2.5
- **Very long** (200K+): Yi-34B-200K, specialized long-context variants

**Language Support:**
- **English only**: Most models perform well
- **Chinese + English**: Qwen, Yi, DeepSeek, InternLM, GLM
- **10+ languages**: Command R/R+, Qwen 2.5, Gemma 3
- **46+ languages**: BLOOM 176B

### 3.2 Performance Requirements

**Latency Targets:**
- **Real-time** (<100ms first token): 7B models on GPU, quantized
- **Interactive** (<500ms): 7B-13B models on mid-range GPU
- **Batch processing** (seconds OK): 70B+ models acceptable
- **Offline/async** (minutes OK): Any size with CPU inference possible

**Throughput Needs:**
- **Low** (<10 req/min): Single GPU, any model size fits budget
- **Medium** (10-100 req/min): Load balancing, vLLM optimization critical
- **High** (100-1000 req/min): Multi-GPU, MoE models, extensive batching
- **Very high** (>1000 req/min): Multi-node clusters, consider API hybrid

**Quality Requirements:**
- **Good enough** (70-80% task success): 7B-13B models with good prompts
- **Production quality** (85-95%): 34B-70B models or fine-tuned smaller models
- **Best possible** (95%+): 70B-405B models, ensemble approaches

### 3.3 Resource Constraints

**Budget Categories:**
- **Shoestring** ($0-5K): Consumer GPU (RTX 4090), 7B-13B models
- **Startup** ($5K-50K): Single A100/H100, 70B models quantized
- **SMB** ($50K-200K): 2-4x A100/H100, 70B+ full precision
- **Enterprise** ($200K+): Multi-node clusters, 405B models, MoE at scale

**Team Expertise:**
- **Beginner**: Use Ollama, LM Studio, pre-built Docker images
- **Intermediate**: HuggingFace Transformers, basic vLLM deployment
- **Advanced**: Custom vLLM/TensorRT-LLM, distributed inference, fine-tuning
- **Expert**: Custom kernels, model merging, advanced quantization

**Time to Deploy:**
- **1 day**: Ollama + 7B model on existing hardware
- **1 week**: vLLM + 70B model + basic monitoring
- **1 month**: Production-ready with HA, monitoring, fine-tuning pipeline
- **3+ months**: Custom infrastructure, multi-model serving, advanced features

### 3.4 Licensing Considerations

**License Types by Freedom Level:**

**Most Permissive (Unrestricted Commercial Use):**
- **Apache 2.0**: Mistral, Qwen, DeepSeek, Yi, DBRX, Arctic, InternLM, Falcon
- **MIT**: DeepSeek-R1, GPT-OSS

**Moderately Restricted:**
- **Llama License**: Free for most, restricted for >700M MAU services
- **Gemma License**: Custom terms, prohibited use policies for sensitive domains

**Research-Focused:**
- **CC-BY-NC**: Command R/R+ (non-commercial use only)
- **Responsible AI License**: BLOOM (open but with ethical constraints)

**Decision Guide:**
- Building commercial product → Use Apache 2.0/MIT models
- Large-scale service (>700M users) → Avoid Llama, use Apache 2.0
- Financial/medical advice → Check Gemma restrictions carefully
- Research/non-profit → All licenses OK

## 4. Model Comparison by Use Case

### 4.1 Code Generation

| Model | Size | Params | Strengths | Weaknesses | Hardware | License |
|-------|------|--------|-----------|------------|----------|---------|
| **DeepSeek-Coder 7B** | Small | 7B | Excellent code quality, fast | Limited reasoning | 16GB GPU | MIT |
| **CodeGemma 7B** | Small | 7B | Multi-language, instruction tuned | Smaller context (8K) | 16GB GPU | Gemma ToS |
| **StarCoder2 15B** | Medium | 15B | 600+ languages, code completion | Less chat-oriented | 32GB GPU | Apache 2.0 |
| **DeepSeek-Coder 33B** | Large | 33B | Best code + reasoning balance | Requires more VRAM | 70GB GPU | MIT |
| **Code Llama 70B** | XL | 70B | Strong reasoning, debugging | Slower inference | 140GB GPU | Llama |
| **Qwen 2.5 Coder 32B** | Large | 32B | Multi-lang, code explanation | Newer, less tested | 64GB GPU | Apache 2.0 |

**Recommendation:** Start with **DeepSeek-Coder 7B** for prototyping, upgrade to **33B** for production if quality matters more than speed.

### 4.2 General Purpose Chat

| Model | Size | Params | Strengths | Weaknesses | Hardware | License |
|-------|------|--------|-----------|------------|----------|---------|
| **Mistral 7B v0.3** | Small | 7B | Fast, efficient, solid quality | Limited context (8K) | 16GB GPU | Apache 2.0 |
| **Gemma 2 9B** | Small | 9B | Great quality/size ratio | Custom license restrictions | 20GB GPU | Gemma ToS |
| **Llama 3.1 8B** | Small | 8B | Good balance, 128K context | Not the smartest 8B | 16GB GPU | Llama |
| **Qwen 2.5 14B** | Medium | 14B | Strong Chinese + English | Less Western-focused tuning | 28GB GPU | Apache 2.0 |
| **Yi-34B** | Large | 34B | Bilingual excellence | Requires more resources | 70GB GPU | Apache 2.0 |
| **Qwen 2.5 72B** | XL | 72B | Top-tier open model | High resource needs | 144GB GPU | Apache 2.0 |
| **Llama 3.3 70B** | XL | 70B | GPT-4 class performance | High resource needs | 140GB GPU | Llama |
| **Command R 35B** | Large | 35B | RAG-optimized, 128K context | NC license limits use | 70GB GPU | CC-BY-NC |

**Recommendation:** **Mistral 7B** for resource-constrained, **Qwen 2.5 72B** or **Llama 3.3 70B** for best quality.

### 4.3 RAG and Document Q&A

| Model | Size | Params | Context | Strengths | Best For | License |
|-------|------|--------|---------|-----------|----------|---------|
| **Mistral 7B** | Small | 7B | 32K | Fast retrieval, good following | Short docs, high volume | Apache 2.0 |
| **Gemma 2 27B** | Large | 27B | 8K | Strong comprehension | Standard RAG | Gemma ToS |
| **Command R 35B** | Large | 35B | 128K | Built for RAG, citations | Long docs, enterprise | CC-BY-NC |
| **Qwen 2.5 72B** | XL | 72B | 128K | Best comprehension + context | Complex multi-doc RAG | Apache 2.0 |
| **Command R+ 104B** | XL | 104B | 128K | Enterprise RAG, tool use | Mission-critical RAG | CC-BY-NC |
| **Yi-34B-200K** | Large | 34B | 200K | Longest context in class | Extremely long docs | Apache 2.0 |

**Recommendation:** **Command R 35B** if non-commercial, **Qwen 2.5 72B** for commercial with long context needs.

### 4.4 SQL and Data Analysis

| Model | Size | Active | Strengths | Weaknesses | Hardware | License |
|-------|------|--------|-----------|------------|----------|---------|
| **DBRX** | 132B | 36B | Code-focused, fast MoE | Complex deployment | 80GB+ GPU | Apache 2.0 |
| **Snowflake Arctic** | 480B | 17B | Built for SQL, efficient | Specialized use case | 80GB+ GPU | Apache 2.0 |
| **DeepSeek V3** | 671B | ~37B | Best reasoning + SQL | Very new, less proven | 80GB+ GPU | MIT |
| **Qwen 2.5 72B** | 72B | 72B | Strong data analysis | Not SQL-specialized | 144GB GPU | Apache 2.0 |

**Recommendation:** **Snowflake Arctic** for SQL-heavy workloads, **DBRX** for mixed code/SQL.

### 4.5 Math and Reasoning

| Model | Size | Params | Strengths | Benchmarks | Hardware | License |
|-------|------|--------|-----------|------------|----------|---------|
| **DeepSeek-R1** | Various | 7B-70B | Chain-of-thought, reasoning | MATH: high | Varies | MIT |
| **DeepSeek V3** | 671B | ~37B active | Best reasoning quality | Near GPT-4 | 80GB+ GPU | MIT |
| **Qwen 2.5 72B** | 72B | 72B | Strong math + reasoning | MMLU: 85+ | 144GB GPU | Apache 2.0 |
| **Gemma 2 27B** | 27B | 27B | Solid reasoning, efficient | Good balance | 54GB GPU | Gemma ToS |

**Recommendation:** **DeepSeek V3** for best quality, **Qwen 2.5 72B** for balanced performance.

### 4.6 Multilingual Applications

| Model | Size | Params | Languages | Strengths | Hardware | License |
|-------|------|--------|-----------|-----------|----------|---------|
| **BLOOM** | XL | 176B | 46 + 13 prog | Most languages | 350GB GPU | Responsible AI |
| **Qwen 2.5 72B** | XL | 72B | 29 major | Chinese + English best | 144GB GPU | Apache 2.0 |
| **Yi-34B** | Large | 34B | Chinese + English | Bilingual excellence | 70GB GPU | Apache 2.0 |
| **Command R+ 104B** | XL | 104B | 10 major | Enterprise multilingual | 208GB GPU | CC-BY-NC |
| **Gemma 3 27B** | Large | 27B | 140+ | Wide coverage | 54GB GPU | Gemma ToS |

**Recommendation:** **Qwen 2.5 72B** for Chinese+English, **BLOOM** for maximum language coverage.

## 5. Hardware Requirements Guide

### 5.1 GPU Requirements by Model Size

**Memory Requirements (Full Precision - FP16):**

| Model Size | FP16 Memory | INT8 Memory | INT4 Memory | Example Models |
|------------|-------------|-------------|-------------|----------------|
| **7B** | ~14GB | ~7GB | ~4GB | Mistral 7B, Gemma 7B, Llama 3 8B |
| **13B** | ~26GB | ~13GB | ~7GB | Llama 2 13B, Qwen 14B |
| **20B-34B** | ~40-68GB | ~20-34GB | ~10-17GB | Yi-34B, Command R 35B, MPT-30B |
| **70B-72B** | ~140-144GB | ~70-72GB | ~35-36GB | Llama 3.3 70B, Qwen 2.5 72B |
| **104B** | ~208GB | ~104GB | ~52GB | Command R+ |
| **176B** | ~352GB | ~176GB | ~88GB | BLOOM |
| **405B** | ~810GB | ~405GB | ~203GB | Llama 3.1 405B |

**MoE Models (Only Active Parameters Matter for Inference):**

| Model | Total Params | Active | Memory Needed | GPU Config |
|-------|--------------|--------|---------------|------------|
| **Mixtral 8x7B** | 47B | 13B | ~26GB FP16 | 1x A100 40GB (INT8) |
| **DBRX** | 132B | 36B | ~72GB FP16 | 1x A100 80GB (INT8) |
| **Snowflake Arctic** | 480B | 17B | ~34GB FP16 | 1x A100 40GB |
| **DeepSeek V3** | 671B | ~37B | ~74GB FP16 | 1x H100 80GB |
| **Qwen 3 235B** | 235B | 22B | ~44GB FP16 | 1x A100 80GB (INT8) |

### 5.2 Recommended Hardware Configurations

**Tier 1: Development/Prototyping ($1K-5K)**
```
Option A: Consumer GPU
- GPU: NVIDIA RTX 4090 24GB (~$1,600)
- CPU: 8+ cores
- RAM: 64GB
- Storage: 1TB NVMe SSD
→ Can run: 7B FP16, 13B INT8, 34B INT4
→ Best for: Local development, 7B-13B models
```

**Tier 2: Small Production ($8K-20K)**
```
Option A: Single A100 40GB
- GPU: 1x A100 40GB (~$10K)
- CPU: 16+ cores (AMD EPYC/Intel Xeon)
- RAM: 128GB
- Storage: 2TB NVMe SSD
→ Can run: 34B FP16, 70B INT4, Mixtral 8x7B INT8
→ Best for: Small-scale production, 13B-34B models

Option B: Dual RTX 4090
- GPU: 2x RTX 4090 24GB (~$3,200)
- CPU: 16+ cores
- RAM: 128GB
- Storage: 2TB NVMe
→ Can run: 34B FP16, 70B INT8 (with model parallelism)
→ Best for: Budget-conscious production
```

**Tier 3: Production Scale ($20K-80K)**
```
Option A: Single A100 80GB
- GPU: 1x A100 80GB (~$15K)
- CPU: 32+ cores (AMD EPYC)
- RAM: 256GB
- Storage: 4TB NVMe SSD
→ Can run: 70B FP16, 176B INT4, MoE models
→ Best for: Production 70B models, efficient MoE

Option B: Dual A100 80GB
- GPU: 2x A100 80GB (~$30K)
- CPU: 64+ cores
- RAM: 512GB
- Storage: 8TB NVMe
→ Can run: 405B INT4, multiple 70B replicas
→ Best for: High throughput, model diversity

Option C: 4x A100 40GB
- GPU: 4x A100 40GB (~$40K)
- CPU: 64+ cores
- RAM: 512GB
- Storage: 8TB NVMe
→ Can run: Multiple 70B models, high concurrency
→ Best for: Multi-tenant, high request volume
```

**Tier 4: Enterprise Scale ($80K+)**
```
Option A: 8x H100 80GB
- GPU: 8x H100 80GB (~$240K)
- CPU: 128+ cores (AMD EPYC)
- RAM: 2TB
- Storage: 16TB NVMe
- Networking: InfiniBand/RoCE
→ Can run: Llama 3.1 405B FP16, multiple 70B replicas
→ Best for: Flagship models, research, multi-model serving

Option B: Multi-node cluster (16+ GPUs)
- 2-4 nodes with 4-8 GPUs each
- High-speed interconnect
→ Can run: Training, distributed inference, massive scale
→ Best for: Large enterprises, research institutions
```

### 5.3 Cloud Deployment Options

**Major Cloud Providers - GPU Instance Costs (On-Demand, US regions):**

| Provider | Instance | GPUs | vCPUs | RAM | Storage | Cost/Hour | Best For |
|----------|----------|------|-------|-----|---------|-----------|----------|
| **AWS** | g5.xlarge | 1x A10G 24GB | 4 | 16GB | 250GB | ~$1.00 | 7B dev |
| **AWS** | p4d.24xlarge | 8x A100 40GB | 96 | 1,152GB | 8TB | ~$32.77 | 70B prod |
| **AWS** | p5.48xlarge | 8x H100 80GB | 192 | 2TB | 30TB | ~$98.32 | 405B flagship |
| **GCP** | g2-standard-4 | 1x L4 24GB | 4 | 16GB | 375GB | ~$0.80 | 7B dev |
| **GCP** | a2-ultragpu-1g | 1x A100 80GB | 12 | 170GB | 375GB | ~$4.89 | 70B testing |
| **GCP** | a3-highgpu-8g | 8x H100 80GB | 208 | 1,872GB | 3TB | ~$90.00 | 405B prod |
| **Azure** | NC24ads A100 v4 | 1x A100 80GB | 24 | 220GB | 1TB | ~$3.67 | 70B prod |
| **Azure** | ND96isr H100 v5 | 8x H100 80GB | 96 | 1,900GB | 4TB | ~$81.85 | 405B prod |

**Spot/Preemptible Pricing (70-90% discount):**
- AWS Spot: ~$3-10/hour for 8x A100
- GCP Preemptible: ~$9-15/hour for 8x H100
- Azure Spot: ~$8-12/hour for 8x H100

**Cost Estimates (24/7 Operation):**
- Single A100 80GB: ~$3,500/month (on-demand) or ~$350-700/month (spot)
- 8x A100 40GB: ~$24,000/month (on-demand) or ~$2,400-4,800/month (spot)
- 8x H100 80GB: ~$70,000/month (on-demand) or ~$7,000-14,000/month (spot)

**Reserved Instances (1-3 year commitment):**
- 30-60% discount for 1-year
- 50-70% discount for 3-year
- Example: 8x A100 → ~$10K-15K/month (vs $24K on-demand)

### 5.4 Quantization Strategies

**Quality vs Speed vs Memory Tradeoffs:**

| Quantization | Memory Savings | Speed Increase | Quality Impact | Use When |
|--------------|----------------|----------------|----------------|----------|
| **FP16** | Baseline | Baseline | None | You have enough VRAM |
| **INT8** | 2x reduction | 1.5-2x faster | Minimal (<1%) | Standard production |
| **INT4** | 4x reduction | 2-4x faster | Small (1-3%) | VRAM constrained |
| **GPTQ** | 3-4x reduction | 2-3x faster | Small (1-2%) | Good balance |
| **AWQ** | 3-4x reduction | 2-4x faster | Minimal (<1%) | Best quality/size |
| **GGUF** | Variable | 2-5x faster | Variable | CPU inference |

**Quantization Decision Matrix:**

```
Available VRAM: 24GB, Model: Llama 3.3 70B (needs 140GB FP16)
├─ FP16: Not possible
├─ INT8 (70GB): Not possible
├─ INT4 (35GB): Not possible on single GPU
├─ GPTQ/AWQ 4-bit (35GB): Not possible on single GPU
└─ Solution: Use smaller model OR multiple GPUs OR extreme quantization

Available VRAM: 80GB, Model: Llama 3.3 70B
├─ FP16 (140GB): Not possible
├─ INT8 (70GB): ✅ Fits perfectly, recommended
├─ INT4 (35GB): ✅ Fits with room, faster but lower quality
└─ Recommendation: Use INT8 for best quality/speed

Available VRAM: 24GB, Model: Mistral 7B (needs 14GB FP16)
├─ FP16 (14GB): ✅ Fits
├─ INT8 (7GB): ✅ Faster, frees VRAM for batching
└─ Recommendation: FP16 for quality, INT8 for throughput
```

### 5.5 CPU-Only Inference

**When to Use CPU Inference:**
- Prototyping on laptops
- Very low traffic (<1 req/min)
- Air-gapped environments without GPUs
- Extremely cost-sensitive hobbyist projects

**Performance Expectations:**
- 7B model: ~10-50 tokens/second (depending on CPU)
- 13B model: ~5-20 tokens/second
- 34B+ model: <5 tokens/second (not recommended)

**Recommended Setup:**
- CPU: High core count (16+ cores), modern architecture (AMD Zen 4, Intel Sapphire Rapids)
- RAM: 32GB for 7B, 64GB for 13B, 128GB for 34B
- Tools: llama.cpp, GGUF models (Q4_K_M or Q5_K_M)

**Cost:**
- Dedicated server: $100-300/month
- Cloud CPU instance: $50-200/month
- Only makes sense for <100K tokens/day

## 6. Recommended Models by Category

### 6.1 Best Overall Value Models

**🥇 Tier 1: Best Value for Most Use Cases**

**1. Qwen 2.5 72B**
- **Why**: Best open-source model overall, Apache 2.0, 128K context, multilingual
- **Use for**: General chat, RAG, document analysis, code, math
- **Hardware**: 144GB VRAM (2x A100 80GB or INT8 on 1x H100)
- **Cost**: ~$0.50/M tokens (self-hosted)
- **License**: Apache 2.0 ✅

**2. Mistral 7B v0.3**
- **Why**: Incredibly efficient, fast, good quality for size
- **Use for**: High-volume chat, simple RAG, classification
- **Hardware**: 16GB VRAM (RTX 4090, A10G)
- **Cost**: ~$0.10/M tokens (self-hosted)
- **License**: Apache 2.0 ✅

**3. DeepSeek-Coder 33B**
- **Why**: Best code model under 70B, MIT license
- **Use for**: Code generation, review, refactoring
- **Hardware**: 70GB VRAM (1x A100 80GB INT8 or 2x A100 40GB)
- **Cost**: ~$0.40/M tokens (self-hosted)
- **License**: MIT ✅

**🥈 Tier 2: Premium Options**

**4. Llama 3.3 70B**
- **Why**: GPT-4 class performance, most tested/documented
- **Use for**: Enterprise chat, complex reasoning
- **Hardware**: 140GB VRAM (2x A100 80GB)
- **Cost**: ~$0.60/M tokens (self-hosted)
- **License**: Llama (restrictive for >700M MAU) ⚠️

**5. DeepSeek V3**
- **Why**: Best reasoning, MoE efficiency, MIT license
- **Use for**: Complex reasoning, math, SQL
- **Hardware**: 80GB VRAM (1x H100 80GB)
- **Cost**: ~$0.50/M tokens (self-hosted)
- **License**: MIT ✅

### 6.2 Budget-Conscious Recommendations

**For Startups (<$10K budget):**

**Development Phase:**
- Local: RTX 4090 24GB + Mistral 7B / Gemma 2 9B ($2K)
- Cloud: GCP L4 spot instance + 7B model (~$200/month)

**Production Phase:**
- Single A100 40GB + Qwen 2.5 32B INT8 (~$10K one-time or $1K/month cloud)
- Model: Mistral 7B for high-volume, Qwen 2.5 32B for quality

**Scaling Strategy:**
1. Start: Mistral 7B FP16 on RTX 4090
2. Grow: Qwen 2.5 32B INT8 on A100 40GB
3. Scale: Qwen 2.5 72B INT4 on A100 80GB or multiple A100 40GB

### 6.3 Enterprise Recommendations

**For Established Companies ($50K+ budget):**

**Multi-Model Strategy:**
```
Tier 1: Fast & Cheap (70% of requests)
└─ Mistral 7B / Gemma 2 9B (simple queries)

Tier 2: Balanced (25% of requests)
└─ Qwen 2.5 32B / Yi-34B (standard queries)

Tier 3: Premium (5% of requests)
└─ Qwen 2.5 72B / Llama 3.3 70B (complex queries)
```

**Hardware Setup:**
- 2-4x A100 80GB for load balancing ($30-60K)
- Run multiple model sizes concurrently
- Smart routing based on query complexity

**Cost Savings:**
- Average: ~$0.30/M tokens (vs $10-30 for GPT-4)
- 30-100x ROI at >100M tokens/month

### 6.4 Special Use Case Recommendations

**For Healthcare/Medical:**
- Base: Llama 3.3 70B or Qwen 2.5 72B
- Fine-tune on medical literature (PubMed, clinical notes)
- Deploy on-premise for HIPAA compliance
- License: Apache 2.0 preferred (Qwen 2.5)

**For Legal/Law Firms:**
- Base: Qwen 2.5 72B (128K context for long docs)
- Fine-tune on legal precedents, contracts
- Air-gapped deployment for privilege
- License: Apache 2.0 required

**For Financial Services:**
- Base: DeepSeek V3 (reasoning) or Qwen 2.5 72B
- Fine-tune on financial data, reports
- On-premise for regulatory compliance
- License: Apache 2.0 or MIT

**For E-commerce:**
- Customer Support: Mistral 7B (multilingual via fine-tuning)
- Product Recommendations: Qwen 2.5 32B
- Content Generation: Gemma 2 27B
- Mixed deployment: cloud + edge

**For Education:**
- Tutoring: Qwen 2.5 32B or Llama 3.1 70B
- Math: DeepSeek-R1 or Qwen 2.5 72B
- Multilingual: BLOOM 176B or Qwen 2.5 72B
- Budget-friendly: Mistral 7B fine-tuned

## 7. Deployment Architecture

### 7.1 Inference Frameworks Comparison

| Framework | Best For | Throughput | Latency | Setup Difficulty | Quantization |
|-----------|----------|------------|---------|------------------|--------------|
| **vLLM** | Production serving | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Medium | AWQ, GPTQ, FP8 |
| **TensorRT-LLM** | NVIDIA GPUs max perf | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Hard | All formats |
| **Text Generation Inference** | HuggingFace ecosystem | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Easy | GPTQ, AWQ |
| **Ollama** | Local/development | ⭐⭐⭐ | ⭐⭐⭐ | Very Easy | GGUF |
| **llama.cpp** | CPU/edge inference | ⭐⭐ | ⭐⭐⭐ | Easy | GGUF |
| **HF Transformers** | Prototyping | ⭐⭐ | ⭐⭐ | Very Easy | Basic |

**Recommendation Matrix:**

```
Production + GPU → vLLM (most versatile)
Production + NVIDIA only → TensorRT-LLM (best performance)
Development → Ollama (easiest setup)
CPU inference → llama.cpp (most optimized)
Prototyping → HuggingFace Transformers (simplest)
```

### 7.2 Architecture Patterns

**Pattern 1: Single Model, Single Instance (Simplest)**
```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
┌──────▼──────────────────┐
│   Load Balancer         │
│   (NGINX/HAProxy)       │
└──────┬──────────────────┘
       │
┌──────▼──────────────────┐
│   vLLM Server           │
│   (Qwen 2.5 72B)        │
│   1x H100 80GB          │
└─────────────────────────┘
```
- **Good for**: <100 req/min, single model
- **Pros**: Simple, low latency
- **Cons**: No redundancy, limited scale

**Pattern 2: Replicated Instances (High Availability)**
```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
┌──────▼──────────────────┐
│   Load Balancer         │
│   (Round Robin)         │
└──────┬──────────────────┘
       │
       ├──────┬──────┬──────┐
       │      │      │      │
    ┌──▼──┐ ┌▼───┐ ┌▼───┐ ┌▼───┐
    │vLLM │ │vLLM│ │vLLM│ │vLLM│
    │ #1  │ │ #2 │ │ #3 │ │ #4 │
    └─────┘ └────┘ └────┘ └────┘
    70B FP16   70B FP16   70B FP16   70B FP16
    A100 80GB  A100 80GB  A100 80GB  A100 80GB
```
- **Good for**: 100-1000 req/min, HA required
- **Pros**: Redundancy, horizontal scaling
- **Cons**: Higher cost (4x GPUs)

**Pattern 3: Tiered Routing (Cost Optimization)**
```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
┌──────▼────────────────────┐
│   Smart Router            │
│   (Complexity Analysis)   │
└──────┬────────────────────┘
       │
       ├─────────────┬─────────────┐
       │             │             │
   Simple        Medium       Complex
   (70%)         (25%)         (5%)
       │             │             │
  ┌────▼───┐   ┌────▼───┐    ┌────▼───┐
  │Mistral │   │Qwen2.5 │    │Qwen2.5 │
  │  7B    │   │  32B   │    │  72B   │
  │ INT8   │   │  FP16  │    │  FP16  │
  └────────┘   └────────┘    └────────┘
  RTX 4090     A100 40GB     A100 80GB
  $0.10/M      $0.30/M       $0.60/M
```
- **Good for**: Cost-sensitive, variable complexity
- **Pros**: 3-5x cost savings, better resource use
- **Cons**: Complex routing logic

**Pattern 4: Multi-Tenant with Isolation**
```
                  ┌─────────────┐
                  │ API Gateway │
                  │ (Auth/Rate) │
                  └──────┬──────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
   Tenant A         Tenant B         Tenant C
   (Finance)        (Legal)          (Healthcare)
        │                │                │
   ┌────▼───┐      ┌────▼───┐       ┌────▼───┐
   │Qwen72B │      │Llama70B│       │Qwen72B │
   │Finance │      │Legal   │       │Medical │
   │Tuned   │      │Tuned   │       │Tuned   │
   └────────┘      └────────┘       └────────┘
   A100 80GB       A100 80GB        A100 80GB
```
- **Good for**: SaaS, multi-tenant, fine-tuned models
- **Pros**: Isolation, customization per tenant
- **Cons**: Requires multiple GPUs

### 7.3 Deployment Tools

**Container Orchestration:**

**Kubernetes + KServe/Seldon**
```yaml
# Example KServe InferenceService
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: qwen-72b
spec:
  predictor:
    containers:
    - name: vllm
      image: vllm/vllm-openai:latest
      command:
      - python
      - -m
      - vllm.entrypoints.openai.api_server
      - --model=Qwen/Qwen2.5-72B-Instruct
      - --tensor-parallel-size=2
      resources:
        limits:
          nvidia.com/gpu: 2
```

**Docker Compose (Simple)**
```yaml
version: '3.8'
services:
  vllm:
    image: vllm/vllm-openai:latest
    command:
      - --model
      - Qwen/Qwen2.5-72B-Instruct
      - --tensor-parallel-size
      - "2"
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 2
              capabilities: [gpu]
    ports:
      - "8000:8000"
```

**Systemd Service (Bare Metal)**
```ini
[Unit]
Description=vLLM Inference Server
After=network.target

[Service]
Type=simple
User=llm-user
WorkingDirectory=/opt/vllm
ExecStart=/opt/vllm/venv/bin/python -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen2.5-72B-Instruct \
  --tensor-parallel-size 2
Restart=always

[Install]
WantedBy=multi-user.target
```

### 7.4 Monitoring and Observability

**Essential Metrics to Track:**

```python
# Key Performance Indicators
1. Inference Latency
   - Time to First Token (TTFT): <500ms target
   - Time Per Output Token (TPOT): <50ms target
   - End-to-End Latency: <2s for typical queries

2. Throughput
   - Requests per Second (RPS)
   - Tokens per Second (TPS)
   - Concurrent Requests Handled

3. Resource Utilization
   - GPU Utilization: >80% target
   - GPU Memory Usage: <90% to avoid OOM
   - CPU Usage
   - Network I/O

4. Model Quality
   - Response Length Distribution
   - Error Rate (<1% target)
   - Retry Rate

5. Business Metrics
   - Cost per 1K Tokens
   - Uptime/Availability (99.9% target)
   - User Satisfaction (if tracked)
```

**Monitoring Stack:**
```
Prometheus + Grafana (metrics)
  │
  ├─ vLLM metrics endpoint (/metrics)
  ├─ Node Exporter (system metrics)
  ├─ NVIDIA DCGM Exporter (GPU metrics)
  └─ Application logs

ELK Stack / Loki (logs)
  │
  └─ vLLM logs, application logs, audit logs

OpenTelemetry (traces)
  │
  └─ Request tracing, latency breakdown
```

## 8. Cost Analysis

### 8.1 Total Cost of Ownership (TCO)

**Self-Hosted vs API Pricing Comparison:**

Scenario: 100M tokens/month, general chat task

**Option 1: OpenAI GPT-4**
```
Cost: $10-30 per 1M tokens
Monthly: $1,000,000 - $3,000,000
Annual: $12,000,000 - $36,000,000
```

**Option 2: Self-Hosted Llama 3.3 70B (On-Premise)**
```
Initial Investment:
- 2x A100 80GB: $30,000
- Server + networking: $10,000
- Setup + integration: $20,000
Total Initial: $60,000

Monthly Operating:
- Power (2kW * 24/7 * $0.12/kWh): $175
- Cooling: $100
- Bandwidth: $200
- Maintenance: $500
Total Monthly: $975

Cost per 1M tokens: ~$0.60
Monthly tokens cost: $60,000
First Year Total: $60,000 + ($975 * 12) + $60,000 = $131,700

Annual (after year 1): $71,700
3-Year TCO: $275,100
```

**Option 3: Self-Hosted Qwen 2.5 72B (Cloud Spot)**
```
Hardware: 2x A100 80GB spot instances
Hourly: ~$6-8 (spot pricing)
Monthly: ~$4,320-5,760 (24/7)

Cost per 1M tokens: ~$0.50
Monthly tokens cost: $50,000

Total Monthly: $54,320-55,760
Annual: $651,840-669,120
```

**Option 4: Tiered Approach (70% on 7B, 25% on 32B, 5% on 72B)**
```
Infrastructure:
- 7B model (Mistral): 1x RTX 4090 ($2K)
- 32B model (Qwen): 1x A100 40GB ($10K)
- 72B model (Qwen): 2x A100 80GB ($30K)
Total: $42,000

Token Distribution (100M total):
- 70M on 7B @ $0.10/M = $7,000
- 25M on 32B @ $0.30/M = $7,500
- 5M on 72B @ $0.60/M = $3,000
Total Monthly: $17,500

First Year: $42,000 + ($975 * 12) + $210,000 = $263,700
Annual (after year 1): $221,700
```

**Break-Even Analysis:**

| Volume (tokens/month) | API Cost (GPT-4 @$15/M) | Self-Host (70B) | Break-Even |
|-----------------------|-------------------------|-----------------|------------|
| 1M | $15 | $60K initial + $1K | Never |
| 10M | $150 | $60K initial + $1K | 40 months |
| 50M | $750 | $60K initial + $1K | 7 months |
| 100M | $1,500 | $60K initial + $1K | 4 months |
| 500M | $7,500 | $60K initial + $1K | <2 months |
| 1B | $15,000 | $60K initial + $1K | 1 month |

**Recommendation:** Self-hosting becomes cost-effective at **>10M tokens/month** (break-even in 4-7 months).

### 8.2 Cloud vs On-Premise Economics

**On-Premise:**
- **Pros**: Lowest long-term cost, full control, no vendor lock-in, data never leaves premise
- **Cons**: High upfront cost, maintenance burden, hardware obsolescence risk (3-5 years)
- **Best for**: >50M tokens/month, 3+ year commitment, privacy requirements

**Cloud Reserved Instances:**
- **Pros**: 40-60% cheaper than on-demand, flexible commitment (1-3 years), vendor support
- **Cons**: Still more expensive than on-premise long-term, commitment lock-in
- **Best for**: 20-100M tokens/month, 1-2 year planning horizon, prefer managed

**Cloud Spot Instances:**
- **Pros**: 70-90% cheaper than on-demand, very flexible
- **Cons**: Can be interrupted (need fault tolerance), availability not guaranteed
- **Best for**: Batch processing, fault-tolerant workloads, cost-sensitive

**Hybrid Approach:**
```
Base Load (predictable): On-premise / reserved instances
├─ 70% of traffic
├─ Stable, cost-effective
└─ 1-2 primary models

Burst/Peak: Spot instances
├─ 20% of traffic
├─ Handle spikes
└─ Same models as base

Experimental: On-demand
├─ 10% of traffic
├─ Test new models
└─ No commitment
```

### 8.3 Optimization Strategies for Cost Reduction

**Strategy 1: Right-Sizing Models**
```
Before: Using 70B for all tasks
Cost: $0.60/M tokens
Volume: 100M tokens/month
Monthly: $60,000

After: Tiered approach
- 60% on 7B @ $0.10/M = 60M * $0.10 = $6,000
- 30% on 32B @ $0.30/M = 30M * $0.30 = $9,000
- 10% on 70B @ $0.60/M = 10M * $0.60 = $6,000
Monthly: $21,000

Savings: $39,000/month (65% reduction)
```

**Strategy 2: Aggressive Quantization**
```
Before: 70B FP16 (140GB) on 2x A100 80GB
Hardware: $30,000
Monthly: $6/hr * 730hr = $4,380 (cloud)

After: 70B INT4 (35GB) on 1x A100 40GB
Hardware: $10,000
Monthly: $3/hr * 730hr = $2,190 (cloud)

Savings: 50% on hardware + cloud cost
Quality Impact: <3% on most tasks
```

**Strategy 3: Batch Processing**
```
Real-time serving (wasteful):
- Latency: <100ms per request
- Batch size: 1-4
- GPU utilization: 40-60%
- Cost: $0.60/M tokens

Batch processing (efficient):
- Latency: 1-5 seconds OK
- Batch size: 32-128
- GPU utilization: 85-95%
- Cost: $0.25/M tokens

When applicable: Saves 60%
```

**Strategy 4: Prompt Caching**
```
Problem: Repeated context in RAG
- System prompt: 500 tokens
- Retrieved context: 2000 tokens
- User query: 200 tokens
- Total: 2700 tokens * 1000 requests = 2.7M tokens

With prompt caching (system + context):
- Cached: 2500 tokens (charged once)
- Variable: 200 tokens * 1000 = 200K tokens
- Total: 2500 + 200K = 202.5K tokens

Savings: 92% on input tokens
```

**Strategy 5: Fine-Tuning Smaller Models**
```
Generic 70B model:
- Hardware: 2x A100 80GB
- Cost: $0.60/M tokens
- Quality: 95% task success

Fine-tuned 13B model:
- Hardware: 1x RTX 4090
- Cost: $0.15/M tokens
- Quality: 90-93% task success (domain-specific)
- Fine-tuning cost: $500 one-time

If acceptable quality: 75% cost savings
Break-even: After 3.3M tokens (~1 week at 500K/day)
```

## 9. Step-by-Step Selection Process

### Step 1: Define Your Requirements (15 minutes)

**Checklist:**
```
□ Primary use case(s):
  □ General chat
  □ Code generation
  □ RAG/document Q&A
  □ SQL generation
  □ Math/reasoning
  □ Other: ___________

□ Volume expectations:
  □ Tokens per day: ___________
  □ Peak requests per minute: ___________
  □ Concurrent users: ___________

□ Quality requirements:
  □ Good enough (70-80% success)
  □ Production quality (85-95%)
  □ Best possible (95%+)

□ Latency requirements:
  □ Real-time (<100ms)
  □ Interactive (<500ms)
  □ Async OK (>1s)

□ Context length needed:
  □ Short (<4K tokens)
  □ Medium (8K-32K)
  □ Long (64K-128K)
  □ Very long (>128K)

□ Language support:
  □ English only
  □ Chinese + English
  □ 10+ languages
  □ 46+ languages

□ Privacy/compliance:
  □ On-premise required (HIPAA, etc.)
  □ Data localization required
  □ Cloud OK

□ Budget:
  □ Initial investment: $___________
  □ Monthly operating: $___________
  □ Per-token target: $___________/M
```

### Step 2: Determine Hardware Constraints (10 minutes)

**Option A: Using Existing Hardware**
```
What do you have?
□ GPU model: ___________
□ GPU memory: ___________
□ Number of GPUs: ___________
□ CPU cores: ___________
□ System RAM: ___________

→ Use Section 5.1 to see which models fit
```

**Option B: Buying New Hardware**
```
Budget: $___________

$0-5K → RTX 4090 24GB
  ├─ Can run: 7B FP16, 13B INT8, 34B INT4
  └─ Best for: Development, 7B-13B production

$5K-20K → A100 40GB or 2x RTX 4090
  ├─ Can run: 34B FP16, 70B INT4
  └─ Best for: 13B-34B production

$20K-50K → A100 80GB or 2x A100 40GB
  ├─ Can run: 70B FP16, multiple models
  └─ Best for: 70B production, multi-model

$50K+ → Multiple A100/H100 GPUs
  ├─ Can run: 70B+ replicas, 405B models
  └─ Best for: Enterprise scale
```

**Option C: Using Cloud**
```
Budget: $___________/month

$100-500/month → Spot instances (A10G/L4)
  └─ 7B-13B models, development

$500-2K/month → Reserved A100 40GB
  └─ 13B-34B production

$2K-10K/month → Reserved A100 80GB or multiple GPUs
  └─ 70B production

$10K+/month → H100s, multi-GPU
  └─ Enterprise scale
```

### Step 3: Shortlist Models (20 minutes)

**Based on use case from Section 4:**

1. Go to Section 4 and find your use case
2. Select top 3 models that match your requirements
3. Check hardware compatibility (Section 5)
4. Verify license compatibility (Section 3.4)

**Example:**
```
Use Case: General chat for customer support
Volume: 50M tokens/month
Quality: Production (90%+)
Hardware: $20K budget (can get A100 80GB)
Languages: English + Chinese

Shortlist from Section 4.2:
1. Qwen 2.5 72B (72B, Apache 2.0, bilingual) ✅
2. Llama 3.3 70B (70B, Llama license) ✅
3. Yi-34B (34B, Apache 2.0, bilingual) ✅

Hardware check (Section 5.1):
- Qwen 72B: 144GB FP16 → Need INT8 (72GB) ✅ fits A100 80GB
- Llama 70B: 140GB FP16 → Need INT8 (70GB) ✅ fits A100 80GB
- Yi-34B: 68GB FP16 ✅ fits A100 80GB comfortably

License check:
- Qwen: Apache 2.0 ✅ unrestricted commercial
- Llama: Custom ⚠️ check if >700M MAU applies
- Yi: Apache 2.0 ✅ unrestricted commercial

Winner: Qwen 2.5 72B INT8 on A100 80GB
Backup: Yi-34B FP16 if need lower latency
```

### Step 4: Proof of Concept (1-3 days)

**Quick PoC Process:**

```bash
# Day 1: Setup (2-4 hours)

# 1. Install Ollama for rapid testing
curl -fsSL https://ollama.com/install.sh | sh

# 2. Pull your shortlisted model
ollama pull qwen2.5:72b

# 3. Test basic functionality
ollama run qwen2.5:72b "Explain quantum computing"

# 4. Test with your actual use case data
ollama run qwen2.5:72b "$(cat your-test-prompt.txt)"

# Day 2: Benchmark (4-8 hours)

# Create test dataset (100-500 examples)
# Run batch evaluation
for prompt in test_prompts/*.txt; do
    ollama run qwen2.5:72b "$(cat $prompt)" > results/$(basename $prompt)
done

# Measure:
# - Response quality (human eval on 50-100 examples)
# - Latency (avg, p50, p95, p99)
# - Error rate

# Day 3: Production Framework Test (4-8 hours)

# Switch to production framework (vLLM)
pip install vllm

# Start vLLM server
python -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen2.5-72B-Instruct \
    --quantization awq \
    --max-model-len 4096

# Run same benchmarks via API
# Compare performance vs Ollama
```

**PoC Success Criteria:**
```
□ Quality meets requirements (>X% success rate)
□ Latency acceptable (<Yms at p95)
□ Model fits on available hardware
□ Cost projections meet budget
□ License allows intended use
```

**If PoC fails:**
- Quality insufficient → Try larger model or fine-tuning
- Too slow → Try smaller model or better quantization
- OOM errors → More aggressive quantization or smaller model
- Cost too high → Smaller model or optimization strategies

### Step 5: Fine-Tuning Evaluation (Optional, 1-2 weeks)

**When to fine-tune:**
- Generic model quality <85% on your task
- Domain-specific jargon/terminology
- Specific output format requirements
- Have ≥1,000 high-quality examples

**Fine-Tuning Process:**

```python
# Using LLaMA-Factory (easiest)

# 1. Prepare dataset (JSON format)
# {
#   "instruction": "Your input prompt",
#   "output": "Expected output"
# }

# 2. Fine-tune (LoRA for efficiency)
llamafactory-cli train \
    --model_name_or_path Qwen/Qwen2.5-72B-Instruct \
    --dataset your_dataset \
    --finetuning_type lora \
    --lora_rank 8 \
    --output_dir output/qwen-finetuned

# 3. Merge LoRA weights (optional)
llamafactory-cli export \
    --model_name_or_path Qwen/Qwen2.5-72B-Instruct \
    --adapter_name_or_path output/qwen-finetuned \
    --export_dir output/qwen-merged

# 4. Evaluate on test set
llamafactory-cli eval \
    --model_name_or_path output/qwen-merged \
    --dataset your_test_set
```

**Cost of Fine-Tuning:**
- Hardware: 1x A100 80GB for 72B model ($10K or $4/hr cloud)
- Time: 6-24 hours for 1,000-10,000 examples
- Total: $50-200 (cloud) or free (owned hardware)

**Expected Improvements:**
- Task-specific: +5-15% success rate
- Domain terminology: +10-20% accuracy
- Format adherence: +15-30% compliance

### Step 6: Production Deployment (1-2 weeks)

**Week 1: Infrastructure Setup**

Day 1-2: Server Setup
```bash
# Install dependencies
apt-get update
apt-get install -y nvidia-driver-535 nvidia-docker2

# Install Python environment
conda create -n vllm python=3.10
conda activate vllm
pip install vllm

# Download model weights
huggingface-cli download Qwen/Qwen2.5-72B-Instruct-AWQ
```

Day 3-4: vLLM Configuration
```python
# config.yaml
model: "Qwen/Qwen2.5-72B-Instruct-AWQ"
tensor_parallel_size: 1
max_model_len: 4096
gpu_memory_utilization: 0.9
quantization: "awq"

# Start server
vllm serve $MODEL \
    --tensor-parallel-size 1 \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.9 \
    --quantization awq
```

Day 5-7: Monitoring & Testing
```bash
# Setup Prometheus + Grafana
docker-compose up -d prometheus grafana

# Load testing
locust -f load_test.py --host http://localhost:8000

# Monitor:
# - GPU utilization (should be >80%)
# - Request latency (p95, p99)
# - Error rate (should be <1%)
```

**Week 2: Integration & Go-Live**

Day 8-10: Application Integration
```python
# Integrate into your application
from openai import OpenAI

client = OpenAI(
    base_url="http://your-vllm-server:8000/v1",
    api_key="dummy"  # vLLM doesn't need key
)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-72B-Instruct-AWQ",
    messages=[{"role": "user", "content": "Hello"}]
)
```

Day 11-12: Gradual Rollout
```
10% traffic → Monitor 24h
├─ Check error rate, latency, quality
└─ If OK, proceed

50% traffic → Monitor 24h
├─ Check at scale
└─ If OK, proceed

100% traffic → Monitor 48h
└─ Full production
```

Day 13-14: Documentation & Handoff
- Document runbooks
- Alert configuration
- Scaling procedures
- Troubleshooting guide

## 10. Production Deployment Checklist

### 10.1 Pre-Deployment Checklist

**Infrastructure:**
```
□ Hardware provisioned and tested
  □ GPUs accessible (nvidia-smi working)
  □ Drivers installed (CUDA, cuDNN)
  □ Sufficient cooling/power
  □ Network connectivity verified

□ Software environment ready
  □ Python 3.10+ installed
  □ vLLM/inference framework installed
  □ Model weights downloaded
  □ Dependencies verified

□ Storage sufficient
  □ Model storage: 100-500GB per model
  □ Logs: 10-50GB/month
  □ Temporary: 50GB+ free
```

**Security:**
```
□ Network security configured
  □ Firewall rules (only necessary ports)
  □ SSL/TLS certificates (if public-facing)
  □ API authentication (if needed)
  □ Rate limiting configured

□ Access control
  □ SSH key-based auth only
  □ Separate user accounts
  □ Audit logging enabled
  □ Secrets management (no hardcoded keys)

□ Compliance (if applicable)
  □ HIPAA requirements met
  □ GDPR compliance verified
  □ Data residency confirmed
  □ Audit trail implemented
```

**Monitoring:**
```
□ Metrics collection
  □ Prometheus/similar installed
  □ GPU metrics (DCGM exporter)
  □ System metrics (Node exporter)
  □ Application metrics (vLLM /metrics)

□ Logging
  □ Centralized logging (ELK/Loki)
  □ Log rotation configured
  □ Error tracking (Sentry/similar)

□ Alerting
  □ High latency (p95 > threshold)
  □ High error rate (>1%)
  □ GPU OOM errors
  □ Disk space low (<10%)
  □ Service down
```

**Backup & Recovery:**
```
□ Model weights backed up
□ Configuration version controlled
□ Database backups (if applicable)
□ Disaster recovery plan documented
□ RTO/RPO defined
```

### 10.2 Deployment Day Checklist

**T-1 Hour:**
```
□ Stakeholders notified
□ Rollback plan prepared
□ On-call team ready
□ Monitoring dashboards open
□ Change window started
```

**Deployment:**
```
□ Deploy to staging
□ Smoke tests passed
□ Deploy to production (1 instance)
□ Health check passed
□ Traffic routed (10%)
□ Monitor 30 minutes
□ Gradual traffic increase (25%, 50%, 100%)
□ Monitor at each stage
```

**Post-Deployment:**
```
□ All health checks green
□ Latency within SLA
□ Error rate <1%
□ GPU utilization normal
□ No alerts firing
□ Rollback plan discarded (or executed)
□ Stakeholders notified (success/failure)
□ Post-mortem scheduled (if issues)
```

### 10.3 Ongoing Operations Checklist

**Daily:**
```
□ Check dashboards (5 min)
□ Review error logs (10 min)
□ Verify backups completed
```

**Weekly:**
```
□ Review metrics trends (30 min)
  □ Latency trending up? → Investigate
  □ Error rate increasing? → Investigate
  □ GPU utilization low? → Right-size
  □ Cost higher than expected? → Optimize

□ Review capacity (15 min)
  □ Peak traffic vs capacity
  □ Disk space remaining
  □ Need to scale?

□ Security review (15 min)
  □ Unusual access patterns?
  □ Failed auth attempts?
  □ Software updates needed?
```

**Monthly:**
```
□ Cost analysis (1 hour)
  □ Actual vs projected costs
  □ Optimization opportunities
  □ ROI review

□ Performance review (1 hour)
  □ SLA compliance
  □ Quality metrics
  □ User feedback

□ Capacity planning (1 hour)
  □ Traffic growth trends
  □ Scaling needed?
  □ Hardware refresh needed?

□ Model updates (2 hours)
  □ New model versions available?
  □ Benchmark new versions
  □ Plan upgrade if beneficial
```

**Quarterly:**
```
□ Full architecture review (4 hours)
  □ Current state assessment
  □ New model families review
  □ Cost optimization deep dive
  □ Technology stack updates
  □ Scaling strategy

□ Disaster recovery test (4 hours)
  □ Simulate failure scenarios
  □ Test backup restoration
  □ Verify RTO/RPO
  □ Update runbooks
```

## 11. Troubleshooting and Optimization

### 11.1 Common Issues and Solutions

**Issue 1: CUDA Out of Memory (OOM)**

Symptoms:
```
RuntimeError: CUDA out of memory. Tried to allocate XXX MiB
```

Solutions:
```python
# Option 1: More aggressive quantization
--quantization int4  # vs int8 or fp16

# Option 2: Reduce max sequence length
--max-model-len 2048  # vs 4096

# Option 3: Lower GPU memory utilization
--gpu-memory-utilization 0.85  # vs 0.95

# Option 4: Reduce batch size
--max-num-seqs 64  # vs 256

# Option 5: Enable tensor parallelism
--tensor-parallel-size 2  # spread across 2 GPUs

# Option 6: Use a smaller model
# Replace 70B with 34B or 13B
```

**Issue 2: High Latency**

Symptoms:
```
p95 latency > 2 seconds (target: <500ms)
```

Diagnosis:
```python
# Check GPU utilization
nvidia-smi dmon -s u

# If utilization < 60%:
#   → Increase batch size
#   → Enable continuous batching

# If utilization > 95%:
#   → Add more GPU capacity
#   → Use smaller/faster model
```

Solutions:
```python
# Option 1: Enable continuous batching (vLLM does this by default)
# Ensure you're using vLLM, not vanilla transformers

# Option 2: Increase batch size for throughput
--max-num-batched-tokens 8192

# Option 3: Use faster quantization
--quantization awq  # faster than gptq

# Option 4: Reduce context length
--max-model-len 2048  # if you don't need 4096

# Option 5: Use faster model
# Mixtral 8x7B (13B active) vs Llama 70B
# MoE models have lower latency for same quality

# Option 6: FlashAttention (usually enabled by default)
# Ensure vLLM is compiled with FA support
```

**Issue 3: Low Throughput**

Symptoms:
```
Can only handle 10 req/min (target: 100 req/min)
GPU utilization: 40%
```

Solutions:
```python
# Option 1: Increase batch size
--max-num-seqs 256  # increase concurrent requests

# Option 2: Increase max tokens per batch
--max-num-batched-tokens 16384

# Option 3: Enable speculative decoding (if supported)
--speculative-model <smaller-model>

# Option 4: Multiple replicas with load balancing
# Deploy 4 instances instead of 1
# Load balance across them

# Option 5: Check if CPU-bound
# If CPU at 100%, GPU at 40%:
#   → More CPU cores
#   → Reduce tokenization overhead
```

**Issue 4: Quality Issues**

Symptoms:
```
Model producing incorrect/incoherent responses
```

Solutions:
```
# Option 1: Check quantization quality
# INT4 can degrade quality by 2-5%
# Try INT8 or FP16

# Option 2: Improve prompting
# Add examples, be more specific
# Use system prompts effectively

# Option 3: Adjust generation parameters
temperature = 0.7  # vs 1.0 (more focused)
top_p = 0.9        # vs 1.0 (more coherent)
repetition_penalty = 1.1  # reduce repetition

# Option 4: Use larger/better model
# Yi-34B → Qwen 2.5 72B
# Or fine-tune for your domain

# Option 5: Fine-tuning
# Collect 1000+ examples of desired outputs
# Fine-tune with LoRA/QLoRA
```

**Issue 5: High Cost**

Symptoms:
```
Spending $10K/month on 100M tokens
(Target: $0.30/M = $3K/month)
```

Solutions:
```
# Option 1: Tiered model approach (see Section 8.3)
# Route 70% to 7B, 30% to 70B
# Saves 40-60%

# Option 2: Move to on-premise
# If sustained high volume
# Break-even in 4-6 months

# Option 3: Spot instances
# 70-90% cheaper than on-demand
# Requires fault tolerance

# Option 4: Aggressive quantization
# INT4 instead of FP16
# 4x memory savings → cheaper instance

# Option 5: Prompt caching
# Cache common prefixes (system prompt, RAG context)
# Saves 50-90% on repeated tokens

# Option 6: Batch processing
# If real-time not required
# Much higher GPU utilization
```

### 11.2 Performance Optimization Techniques

**Optimization 1: Batch Size Tuning**

```python
# Goal: Maximize throughput without OOM

# Start conservative
batch_size = 32

# Gradually increase until:
# 1. GPU OOM error (too high)
# 2. Latency degrades (queue buildup)
# 3. GPU utilization > 90% (good spot)

# Optimal batch size typically:
# - 7B models: 64-256
# - 34B models: 32-128
# - 70B models: 16-64
```

**Optimization 2: KV Cache Optimization**

```python
# KV cache stores attention states
# Can be large for long contexts

# Enable chunked prefill
--enable-chunked-prefill

# Optimize KV cache size
--max-model-len 4096  # vs 8192 if not needed
# Each halving saves significant VRAM

# Use KV cache quantization (if available)
--kv-cache-dtype fp8
# Saves 2x memory with minimal quality loss
```

**Optimization 3: Prompt Optimization**

```python
# Bad: Verbose system prompt repeated every request
system_prompt = """
You are a helpful AI assistant created by Company Inc.
You should always be polite and professional.
You should answer questions accurately.
You should admit when you don't know something.
... (500 tokens)
"""

# Good: Concise system prompt, leverage model's training
system_prompt = "You are a helpful and accurate AI assistant."
# Saves 450+ tokens per request
# 1000 req/day * 450 tokens = 450K tokens/day saved

# Also: Use prompt caching for static prefixes
```

**Optimization 4: Output Length Control**

```python
# Problem: Users asking "Why is X?" getting 1000-token essays
# When 200 tokens would suffice

# Solution: Set max tokens based on use case
max_tokens = 200  # for general chat
max_tokens = 100  # for classification/short answers
max_tokens = 1000 # for blog posts/long-form

# Impact: 5x cost savings if avg output 200 vs 1000 tokens
```

**Optimization 5: Model Selection**

```python
# Use smallest model that meets quality bar

# Example: Customer support classification
# Tested models:
# - Llama 70B: 97% accuracy, 200ms latency, $0.60/M
# - Qwen 32B: 95% accuracy, 100ms latency, $0.30/M
# - Mistral 7B: 92% accuracy, 30ms latency, $0.10/M

# If 92% acceptable → 6x cost savings
# If need 95% → 2x cost savings
# Only use 70B if 97% critical
```

**Optimization 6: Inference Engine Selection**

```python
# Benchmark on your hardware with your model

# Example: Llama 70B on 2x A100 80GB

# HuggingFace Transformers: 5 tok/s (baseline)
# Text Generation Inference: 12 tok/s (2.4x)
# vLLM: 25 tok/s (5x)
# TensorRT-LLM: 35 tok/s (7x)

# TensorRT-LLM hardest to setup
# vLLM best balance of performance and ease
# Use vLLM unless absolute max performance needed
```

### 11.3 Scaling Strategies

**Vertical Scaling (Scale Up)**

```
Single Instance → More Powerful Instance

Before: 1x A100 40GB
After: 1x A100 80GB

Pros:
+ Simple (no distributed complexity)
+ Lower latency (no network hops)
+ Easier to manage

Cons:
- Single point of failure
- Limited by largest available GPU
- Expensive at high end

When to use:
- <100 req/min
- Prefer simplicity
- Single model
```

**Horizontal Scaling (Scale Out)**

```
Single Instance → Multiple Instances + Load Balancer

Before: 1x server with 1x A100 80GB
After: 4x servers with 1x A100 80GB each

Pros:
+ Higher availability (redundancy)
+ Linear scaling (4x capacity)
+ Cost-effective at scale

Cons:
- More complex setup
- Need load balancing
- Higher latency (marginal)

When to use:
- >100 req/min
- Need HA/redundancy
- Multiple replicas of same model
```

**Model Parallelism (Scale Within)**

```
Model Too Large → Split Across Multiple GPUs

Model: Llama 70B (140GB FP16)
Hardware: 2x A100 80GB

# Tensor parallelism
--tensor-parallel-size 2
# Splits model layers across GPUs

Pros:
+ Can run larger models
+ Lower latency than sequential

Cons:
- Requires fast GPU interconnect
- More complex
- Doesn't increase throughput

When to use:
- Model doesn't fit on single GPU
- Have multi-GPU server
```

**Hybrid Approach (Scale Smart)**

```
Tiered Architecture with Auto-Scaling

Tier 1 (Fast Lane):
├─ 4x Mistral 7B on RTX 4090
├─ Simple queries (70%)
└─ Auto-scale 2-8 instances

Tier 2 (Standard):
├─ 2x Qwen 32B on A100 40GB
├─ Medium complexity (25%)
└─ Auto-scale 1-4 instances

Tier 3 (Premium):
├─ 1x Qwen 72B on A100 80GB
├─ Complex queries (5%)
└─ Manual scaling

Benefits:
+ Cost-optimized
+ Quality-appropriate
+ Resource-efficient
```

**Auto-Scaling Rules:**

```python
# Kubernetes HPA (Horizontal Pod Autoscaler)

# Scale up when:
if avg_queue_time > 5 seconds:
    add_replica()

if gpu_utilization > 90% for 5 minutes:
    add_replica()

if request_rate > 80% of capacity:
    add_replica()

# Scale down when:
if avg_queue_time < 1 second for 10 minutes:
    remove_replica()

if gpu_utilization < 50% for 15 minutes:
    remove_replica()

# Limits:
min_replicas = 2  # for HA
max_replicas = 10  # cost control
```

## 12. References and Tools

### 12.1 Model Repositories

**Primary Sources:**
- HuggingFace Hub: https://huggingface.co/models
- Ollama Library: https://ollama.com/library
- TheBloke Quantized Models: https://huggingface.co/TheBloke

**Vendor-Specific:**
- Meta Llama: https://llama.meta.com/
- Mistral AI: https://mistral.ai/
- DeepSeek: https://github.com/deepseek-ai
- Qwen (Alibaba): https://github.com/QwenLM
- Google Gemma: https://ai.google.dev/gemma
- 01.AI Yi: https://github.com/01-ai/Yi

### 12.2 Inference Frameworks

**Production Serving:**
- vLLM: https://github.com/vllm-project/vllm
- TensorRT-LLM: https://github.com/NVIDIA/TensorRT-LLM
- Text Generation Inference: https://github.com/huggingface/text-generation-inference

**Development/Local:**
- Ollama: https://ollama.com/
- llama.cpp: https://github.com/ggerganov/llama.cpp
- LM Studio: https://lmstudio.ai/

**Training/Fine-tuning:**
- LLaMA-Factory: https://github.com/hiyouga/LLaMA-Factory
- Axolotl: https://github.com/OpenAccess-AI-Collective/axolotl
- Unsloth: https://github.com/unslothai/unsloth

### 12.3 Evaluation Tools

**Benchmarking:**
- lm-evaluation-harness: https://github.com/EleutherAI/lm-evaluation-harness
- OpenLLM Leaderboard: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
- LMSYS Chatbot Arena: https://chat.lmsys.org/

**Performance Testing:**
- Locust: https://locust.io/
- k6: https://k6.io/
- Apache JMeter: https://jmeter.apache.org/

### 12.4 Monitoring and Observability

**Metrics:**
- Prometheus: https://prometheus.io/
- Grafana: https://grafana.com/
- NVIDIA DCGM Exporter: https://github.com/NVIDIA/dcgm-exporter

**Logging:**
- ELK Stack: https://www.elastic.co/elk-stack
- Loki: https://grafana.com/oss/loki/
- Fluentd: https://www.fluentd.org/

**Tracing:**
- OpenTelemetry: https://opentelemetry.io/
- Jaeger: https://www.jaegertracing.io/

### 12.5 Cost Calculators

**Cloud Pricing:**
- AWS Calculator: https://calculator.aws/
- GCP Pricing Calculator: https://cloud.google.com/products/calculator
- Azure Pricing Calculator: https://azure.microsoft.com/en-us/pricing/calculator/

**GPU Rental Marketplaces:**
- Vast.ai: https://vast.ai/
- RunPod: https://www.runpod.io/
- Lambda Labs: https://lambdalabs.com/

### 12.6 Community Resources

**Forums:**
- r/LocalLLaMA: https://reddit.com/r/LocalLLaMA
- HuggingFace Forums: https://discuss.huggingface.co/
- EleutherAI Discord: https://discord.gg/eleutherai

**Documentation:**
- vLLM Docs: https://docs.vllm.ai/
- HuggingFace Docs: https://huggingface.co/docs
- Ollama Docs: https://github.com/ollama/ollama/tree/main/docs

**Tutorials:**
- LLM University: https://docs.cohere.com/docs/llmu
- DeepLearning.AI: https://www.deeplearning.ai/short-courses/
- Sebastian Raschka's Blog: https://magazine.sebastianraschka.com/

---

## Appendix: Quick Reference Cards

### A1. Model Selection Cheat Sheet

| If you need... | Recommended Model | Alt Model | Size | Min GPU |
|----------------|------------------|-----------|------|---------|
| **Fast prototyping** | Ollama + Mistral 7B | Gemma 2 9B | 7-9B | 16GB |
| **Best bang/buck** | Qwen 2.5 32B | Yi-34B | 32-34B | 64GB |
| **Best overall** | Qwen 2.5 72B | Llama 3.3 70B | 70B+ | 144GB |
| **Code generation** | DeepSeek-Coder 33B | Code Llama 70B | 33-70B | 70-140GB |
| **RAG/long docs** | Command R 35B* | Qwen 2.5 72B | 35-72B | 70-144GB |
| **SQL/data** | Snowflake Arctic | DBRX | 480B/132B MoE | 80GB+ |
| **Math/reasoning** | DeepSeek V3 | Qwen 2.5 72B | 671B/72B | 80-144GB |
| **Multilingual** | BLOOM 176B | Qwen 2.5 72B | 176B/72B | 350GB/144GB |
| **Budget (<$5K)** | Mistral 7B | Gemma 2 9B | 7-9B | RTX 4090 |
| **Enterprise** | Qwen 72B + Mistral 7B tiered | Custom | Various | Multi-GPU |

*Non-commercial license

### A2. Hardware Quick Reference

| Your Budget | Buy This | Can Run | Best For |
|-------------|----------|---------|----------|
| **<$2K** | RTX 4090 24GB | 7B FP16, 13B INT8 | Development |
| **$5-10K** | A100 40GB | 34B FP16, 70B INT4 | Small production |
| **$15-30K** | A100 80GB or 2x A100 40GB | 70B FP16 | Production |
| **$40-60K** | 2x A100 80GB or 4x A100 40GB | 70B replicas, 405B INT4 | Scale |
| **$100K+** | 4-8x H100 80GB | 405B, multi-model | Enterprise |

### A3. Quantization Quick Reference

| Format | Memory | Speed | Quality Loss | When to Use |
|--------|--------|-------|--------------|-------------|
| **FP16** | 1x | 1x | 0% | Have enough VRAM |
| **INT8** | 0.5x | 1.5-2x | <1% | Standard production |
| **AWQ INT4** | 0.25x | 2-4x | 1-2% | VRAM constrained |
| **GPTQ INT4** | 0.25x | 2-3x | 1-3% | Good balance |
| **GGUF Q4** | 0.25x | 2-5x | 2-5% | CPU inference |

### A4. Cost Comparison Quick Reference

| Scenario | Proprietary API | Self-Hosted | Savings |
|----------|----------------|-------------|---------|
| **10M tok/month** | $150-300 (GPT-4) | $60K initial + $1K/mo | Break-even: 40 months |
| **50M tok/month** | $750-1500 | $60K initial + $1K/mo | Break-even: 7 months |
| **100M tok/month** | $1500-3000 | $60K initial + $1K/mo | Break-even: 4 months |
| **500M tok/month** | $7500-15000 | $60K initial + $1K/mo | Break-even: <2 months |

### A5. License Quick Reference

| License Type | Commercial OK? | Attribution | Models |
|--------------|---------------|-------------|---------|
| **Apache 2.0** | ✅ Yes | Required | Mistral, Qwen, DeepSeek, Yi, DBRX, Arctic |
| **MIT** | ✅ Yes | Required | DeepSeek-R1, GPT-OSS |
| **Llama** | ⚠️ Mostly | Required | Llama (not if >700M MAU) |
| **Gemma ToS** | ⚠️ Restricted | Required | Gemma (check prohibited uses) |
| **CC-BY-NC** | ❌ No | Required | Command R/R+ (research only) |

---

**Document Version:** 1.0
**Last Updated:** January 2025
**Target Audience:** ML Engineers, DevOps, Technical Decision Makers
**Estimated Reading Time:** 60-90 minutes
**Estimated Implementation Time:** 1-4 weeks (depends on scale)

For questions, corrections, or contributions, please open an issue on our GitHub repository.

**Disclaimer:** Model capabilities, pricing, and hardware requirements evolve rapidly. Verify current specifications before making procurement decisions. This guide is for informational purposes and does not constitute professional advice for your specific use case.
