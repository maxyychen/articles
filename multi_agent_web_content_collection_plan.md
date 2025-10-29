# Multi-Agent LLM Web Content Collection

A comprehensive plan for building an intelligent web crawler using multi-agent architecture with MCP tools (Search + SQLite).

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Architecture Overview](#architecture-overview)
3. [Agent Design](#agent-design)
4. [Data Flow & Communication](#data-flow--communication)
5. [Database Schema](#database-schema)
6. [Technology Stack](#technology-stack)
7. [Implementation Phases](#implementation-phases)
8. [Code Examples](#code-examples)
9. [Performance & Scalability](#performance--scalability)
10. [Monitoring & Observability](#monitoring--observability)
11. [Security & Compliance](#security--compliance)
12. [Testing Strategy](#testing-strategy)

---

## Executive Summary

### Project Overview
Build an intelligent, multi-agent web crawler that can:
- Expand user keywords with synonyms and related terms for comprehensive discovery
- Discover and crawl web pages based on seed URLs
- Extract and analyze content using LLMs
- Store structured data in SQLite database
- Scale horizontally with parallel agent execution
- Handle errors gracefully with retry mechanisms

### Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Architecture Pattern** | Hierarchical + Parallel Hybrid | Coordinator manages workflow, specialists run in parallel |
| **Framework** | CrewAI (Hierarchical) or Microsoft Agent Framework | Built-in delegation, MCP support, proven reliability |
| **Communication** | Message Queue (async) | Non-blocking, scalable, fault-tolerant |
| **Database** | SQLite via MCP | Simple, serverless, perfect for structured crawl data |
| **Parallelization** | Discovery, Extraction, Analysis | Maximize throughput while maintaining data consistency |

### Success Metrics
- **Throughput**: 100+ pages/minute
- **Accuracy**: >95% successful content extraction
- **Reliability**: <1% data loss
- **Scalability**: Linear scaling up to 10 parallel agents

---

## Architecture Overview

### High-Level Architecture

```
                    ┌──────────────────┐
                    │  User Keyword    │
                    └────────┬─────────┘
                             ▼
                    ┌──────────────────┐
                    │ Query Expansion  │
                    │     Agent        │
                    │ (Generate        │
                    │  Synonyms)       │
                    └────────┬─────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                     Coordinator Agent                        │
│         (Orchestrates workflow, manages state)               │
└────────────┬────────────────────────────────────────────────┘
             │
             ├──────────────┬──────────────┬──────────────┬──────────────┐
             ▼              ▼              ▼              ▼              ▼
    ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐
    │   Query    │  │    URL     │  │  Content   │  │  Content   │  │    Data    │
    │ Expansion  │  │ Discovery  │  │ Extraction │  │  Analysis  │  │Persistence │
    │   Agent    │  │   Agent    │  │   Agent    │  │   Agent    │  │   Agent    │
    └─────┬──────┘  └─────┬──────┘  └─────┬──────┘  └─────┬──────┘  └─────┬──────┘
          │               │               │               │               │
          ▼               ▼               ▼               ▼               ▼
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                          Message Queues                                  │
    │  [Expansion Queue] [URL Queue] [Content Queue] [Analysis Queue]         │
    └─────────────────────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌──────────────────────┐
              │    SQLite Database   │
              │      (via MCP)       │
              └──────────────────────┘
```

### Architecture Pattern: Hierarchical + Parallel Hybrid

**Why This Pattern?**

1. **Hierarchical Component**:
   - Coordinator agent manages overall workflow
   - Clear authority and responsibility
   - Centralized error handling

2. **Parallel Component**:
   - URL discovery agents work concurrently
   - Content extraction scales horizontally
   - Analysis agents process multiple pages simultaneously

3. **Sequential Bottleneck**:
   - Single persistence agent prevents write conflicts
   - Maintains data consistency
   - Simplifies transaction management

### Workflow Stages

```
Stage 0: Query Expansion (First, One-time)
  ├─ Accept user keyword(s)
  ├─ Generate synonyms using LLM
  ├─ Generate related terms
  ├─ Generate hyponyms/hypernyms
  └─ Store expanded query terms

Stage 1: URL Discovery (Parallel)
  ├─ Use Search MCP with expanded terms
  ├─ Extract links from crawled pages
  ├─ Validate and deduplicate URLs
  └─ Add to URL queue

Stage 2: Content Extraction (Parallel)
  ├─ Fetch HTML content
  ├─ Parse and clean HTML
  ├─ Extract text, metadata, links
  └─ Add to content queue

Stage 3: Content Analysis (Parallel)
  ├─ LLM-based summarization
  ├─ Entity extraction
  ├─ Topic classification
  └─ Add to persistence queue

Stage 4: Data Persistence (Sequential)
  ├─ Store in SQLite via MCP
  ├─ Update crawl state
  ├─ Handle duplicates
  └─ Update indexes
```

---

## Agent Design

### 1. Coordinator Agent

**Role**: Orchestration and workflow management

**Responsibilities**:
- Accept crawl job requests from users
- Initialize crawl jobs in database
- Distribute work to specialist agents
- Monitor progress and agent health
- Aggregate results and generate reports
- Handle global error conditions

**Tools**:
- SQLite MCP (for job state management)

**Configuration**:
```python
coordinator = Agent(
    role="Crawl Coordinator",
    goal="Orchestrate efficient web crawling workflow",
    backstory="Expert at managing distributed crawling operations",
    allow_delegation=True,
    verbose=True,
    tools=[sqlite_query_tool, sqlite_write_tool]
)
```

**Key Methods**:
- `start_crawl_job(seed_url, max_depth, filters, keywords)`
- `monitor_progress(job_id)`
- `handle_agent_failure(agent_id, error)`
- `aggregate_results(job_id)`

---

### 2. Query Expansion Agent

**Role**: Expand user keywords with synonyms and related terms

**Responsibilities**:
- Accept user-provided keyword(s)
- Generate synonyms using LLM (e.g., "AI" → "artificial intelligence", "machine learning", "deep learning")
- Generate related terms and concepts
- Generate hyponyms (more specific terms) and hypernyms (more general terms)
- Generate domain-specific variations
- Store expanded terms in database for search optimization
- Provide relevance scoring for each expanded term

**Tools**:
- LLM (local GPT-OSS:20B or cloud API)
- SQLite MCP (to store expanded queries)

**Configuration**:
```python
query_expansion_agent = Agent(
    role="Query Expansion Specialist",
    goal="Generate comprehensive synonym and related term lists for thorough searching",
    backstory="Expert linguist and semantic analyst who understands relationships between words and concepts",
    allow_delegation=False,
    llm_config={"model": "gpt-oss:20b", "temperature": 0.7},
    tools=[sqlite_write_tool]
)
```

**Key Methods**:
- `expand_query(keywords: list[str]) -> dict`
- `generate_synonyms(keyword: str) -> list[str]`
- `generate_related_terms(keyword: str) -> list[str]`
- `generate_hyponyms_hypernyms(keyword: str) -> dict`
- `score_relevance(original: str, expanded: str) -> float`

**Expansion Strategies**:

1. **Synonym Generation**:
   - Direct synonyms: "car" → "automobile", "vehicle"
   - Informal variations: "doctor" → "doc", "physician", "MD"
   - Acronyms: "artificial intelligence" → "AI"

2. **Related Terms**:
   - Associated concepts: "Python" → "Django", "Flask", "NumPy"
   - Domain-specific: "machine learning" → "neural networks", "supervised learning", "training data"

3. **Hierarchical Terms**:
   - Hypernyms (broader): "car" → "vehicle", "transportation"
   - Hyponyms (narrower): "car" → "sedan", "SUV", "electric car"

4. **Contextual Variations**:
   - Technical vs. common: "ML" ↔ "machine learning"
   - British vs. American: "colour" ↔ "color"
   - Plural forms: "database" → "databases"

**LLM Prompt Example**:
```python
expansion_prompt = """
You are a semantic analysis expert. Given a keyword, generate a comprehensive list of related search terms.

Keyword: {keyword}

Provide the following:
1. **Synonyms**: Direct synonyms and equivalent terms (5-10 terms)
2. **Related Terms**: Closely related concepts (5-10 terms)
3. **Broader Terms**: More general concepts (2-3 terms)
4. **Narrower Terms**: More specific concepts (5-10 terms)
5. **Common Variations**: Abbreviations, acronyms, informal terms (3-5 terms)

For each term, provide a relevance score (0.0-1.0) indicating how related it is to the original keyword.

Return as JSON:
{{
    "original": "{keyword}",
    "synonyms": [
        {{"term": "...", "relevance": 0.95}},
        ...
    ],
    "related": [
        {{"term": "...", "relevance": 0.85}},
        ...
    ],
    "broader": [
        {{"term": "...", "relevance": 0.70}},
        ...
    ],
    "narrower": [
        {{"term": "...", "relevance": 0.90}},
        ...
    ],
    "variations": [
        {{"term": "...", "relevance": 1.0}},
        ...
    ]
}}

Be comprehensive but relevant. Focus on terms that would help find related web content.
"""
```

**Example Output**:

Input: `"artificial intelligence"`

Output:
```json
{
    "original": "artificial intelligence",
    "synonyms": [
        {"term": "AI", "relevance": 1.0},
        {"term": "machine intelligence", "relevance": 0.95},
        {"term": "cognitive computing", "relevance": 0.85}
    ],
    "related": [
        {"term": "machine learning", "relevance": 0.90},
        {"term": "deep learning", "relevance": 0.88},
        {"term": "neural networks", "relevance": 0.85},
        {"term": "natural language processing", "relevance": 0.80},
        {"term": "computer vision", "relevance": 0.75}
    ],
    "broader": [
        {"term": "computer science", "relevance": 0.60},
        {"term": "technology", "relevance": 0.50}
    ],
    "narrower": [
        {"term": "GPT", "relevance": 0.85},
        {"term": "transformer models", "relevance": 0.82},
        {"term": "reinforcement learning", "relevance": 0.80},
        {"term": "supervised learning", "relevance": 0.78}
    ],
    "variations": [
        {"term": "A.I.", "relevance": 1.0},
        {"term": "Artificial Intelligence", "relevance": 1.0},
        {"term": "AI systems", "relevance": 0.95}
    ]
}
```

**Integration with URL Discovery**:
The expanded terms are used by URL Discovery agents to search more comprehensively:
```python
# Instead of just searching "AI"
search_queries = [
    "artificial intelligence",
    "AI",
    "machine learning",
    "deep learning",
    "neural networks",
    # ... all expanded terms with relevance > 0.7
]

for query in search_queries:
    results = search_mcp.search(query)
    # Process results...
```

**Parallelization**:
- Single agent runs at the start of crawl job
- Runs once per job (not per URL)
- Blocks coordinator until expansion completes
- Results cached for the entire job duration

**Optimization for Local GPT-OSS:20B**:
```python
# Simpler prompt for 20B model
simplified_prompt = """
List synonyms and related terms for: {keyword}

Synonyms (same meaning):
- ...

Related terms (similar concepts):
- ...

Return as JSON list.
"""
```

---

### 3. URL Discovery Agent

**Role**: Find and validate URLs to crawl

**Responsibilities**:
- Use Search MCP tool to discover relevant URLs
- Extract links from crawled HTML pages
- Validate URL formats (http/https, reachable)
- Check against SQLite for already-crawled URLs
- Apply filters (domain whitelist, content type, etc.)
- Add discovered URLs to queue with metadata

**Tools**:
- Search MCP (for URL discovery)
- SQLite MCP (read-only, for deduplication)

**Configuration**:
```python
url_discovery_agent = Agent(
    role="URL Discovery Specialist",
    goal="Discover and validate new URLs efficiently",
    backstory="Expert at finding relevant web pages",
    allow_delegation=False,
    tools=[search_tool, sqlite_query_tool]
)
```

**Key Methods**:
- `discover_urls(seed_url, search_query)`
- `extract_links(html_content, base_url)`
- `validate_url(url)`
- `check_already_crawled(url, job_id)`
- `apply_filters(urls, filters)`

**Parallelization**:
- Multiple discovery agents (3-5) work simultaneously
- Each agent processes different seed URLs or domains
- Coordinator distributes work via queue

---

### 4. Content Extraction Agent

**Role**: Fetch and parse web page content

**Responsibilities**:
- Download HTML content from URLs
- Handle different content types (HTML, JSON, XML)
- Extract text content, removing ads and boilerplate
- Extract metadata (title, description, author, date)
- Extract outbound links for discovery
- Handle rate limiting per domain
- Respect robots.txt
- Handle redirects and errors

**Tools**:
- Search MCP (for content fetching)
- HTTP client with user-agent rotation

**Configuration**:
```python
content_extraction_agent = Agent(
    role="Content Extraction Specialist",
    goal="Extract clean, structured content from web pages",
    backstory="Expert at parsing HTML and extracting meaningful content",
    allow_delegation=False,
    tools=[search_tool]
)
```

**Key Methods**:
- `fetch_content(url)`
- `parse_html(html, url)`
- `extract_text(soup)`
- `extract_metadata(soup)`
- `extract_links(soup, base_url)`
- `handle_rate_limit(domain)`

**Parallelization**:
- 5-10 extraction agents working simultaneously
- Domain-based queue distribution (respect rate limits)
- Configurable delays between requests per domain

---

### 5. Content Analysis Agent

**Role**: Analyze and enrich extracted content using LLM

**Responsibilities**:
- Generate concise summaries of content
- Extract named entities (people, places, organizations)
- Classify content by topic/category
- Identify key themes and concepts
- Extract structured data (dates, prices, etc.)
- Generate embeddings for semantic search (optional)
- Assess content quality and relevance

**Tools**:
- LLM API (GPT-4, Claude, etc.)
- SQLite MCP (read-only, for context)

**Configuration**:
```python
content_analysis_agent = Agent(
    role="Content Analysis Specialist",
    goal="Analyze and enrich crawled content with AI insights",
    backstory="Expert at understanding and categorizing web content",
    allow_delegation=False,
    llm_config={"model": "gpt-4-turbo", "temperature": 0.3},
    tools=[sqlite_query_tool]
)
```

**Key Methods**:
- `summarize_content(text, max_length=200)`
- `extract_entities(text)`
- `classify_topic(text, categories)`
- `assess_quality(text, metadata)`
- `generate_tags(text)`

**Analysis Prompt Example**:
```python
analysis_prompt = """
Analyze the following web page content and provide:

1. A concise 2-3 sentence summary
2. Key entities (people, organizations, places)
3. Primary topic/category
4. 5 relevant tags
5. Content quality score (0-10)

Content:
{text}

Metadata:
- URL: {url}
- Title: {title}
- Published: {date}

Return as JSON.
"""
```

**Parallelization**:
- 3-5 analysis agents working simultaneously
- Analysis is CPU/token-intensive, so fewer agents
- Queue-based distribution of content

---

### 6. Data Persistence Agent

**Role**: Store crawled data in SQLite database

**Responsibilities**:
- Write URLs, content, and metadata to SQLite
- Handle duplicate URLs gracefully
- Manage crawl state transitions
- Create and maintain database indexes
- Handle transaction errors and retries
- Provide query interface for results

**Tools**:
- SQLite MCP (read/write)

**Configuration**:
```python
persistence_agent = Agent(
    role="Data Persistence Specialist",
    goal="Reliably store crawled data in structured format",
    backstory="Expert at database management and data integrity",
    allow_delegation=False,
    tools=[sqlite_write_tool, sqlite_query_tool]
)
```

**Key Methods**:
- `store_url(url, job_id, depth, status)`
- `store_content(url, content, metadata)`
- `store_entities(url, entities)`
- `update_url_status(url, status)`
- `handle_duplicate(url, new_data)`

**Why Sequential?**
- SQLite has limited concurrent write support
- Single writer prevents lock contention
- Simpler transaction management
- Can batch writes for efficiency

**Optimization**:
- Batch inserts (50-100 records at a time)
- Use transactions for atomicity
- WAL mode for better concurrency
- Async queue for non-blocking operation

---

## Data Flow & Communication

### Message Queue Architecture

```python
# Queue structure
queues = {
    "query_expansion": asyncio.Queue(maxsize=100),     # User keywords
    "url_discovery": asyncio.Queue(maxsize=10000),     # URLs to discover
    "content_extraction": asyncio.Queue(maxsize=5000), # URLs to crawl
    "content_analysis": asyncio.Queue(maxsize=1000),   # Content to analyze
    "data_persistence": asyncio.Queue(maxsize=500)     # Data to store
}
```

### Data Flow Diagram

```
User Request (with keywords)
    │
    ▼
[Coordinator Agent]
    │
    ├─ Create job in SQLite
    ├─ Add keywords to query_expansion queue
    │
    ▼
[Query Expansion Queue] ── Query Expansion Agent
    │
    ├─ Generate synonyms & related terms
    ├─ Store expanded terms in SQLite
    ├─ Add expanded terms to url_discovery queue
    │
    ▼
[URL Discovery Queue] ─┬─ Discovery Agent 1
                       ├─ Discovery Agent 2
                       └─ Discovery Agent 3
    │
    ├─ Search with expanded terms via Search MCP
    ├─ Validate and deduplicate
    ├─ Add to content_extraction queue
    │
    ▼
[Content Extraction Queue] ─┬─ Extraction Agent 1
                             ├─ Extraction Agent 2
                             ├─ Extraction Agent 3
                             ├─ Extraction Agent 4
                             └─ Extraction Agent 5
    │
    ├─ Fetch and parse HTML
    ├─ Extract text, metadata, links
    ├─ Add to content_analysis queue
    ├─ Add new links to url_discovery queue
    │
    ▼
[Content Analysis Queue] ─┬─ Analysis Agent 1
                          ├─ Analysis Agent 2
                          └─ Analysis Agent 3
    │
    ├─ Summarize with LLM
    ├─ Extract entities
    ├─ Classify topics
    ├─ Add to data_persistence queue
    │
    ▼
[Data Persistence Queue] ── Persistence Agent (single)
    │
    ├─ Write to SQLite via MCP
    ├─ Update crawl state
    ├─ Handle duplicates
    │
    ▼
[SQLite Database]
    │
    ▼
Results Available
```

### Communication Protocol

**Queue Messages Format**:

```python
# URL Discovery Message
{
    "type": "url_to_discover",
    "job_id": "job_123",
    "url": "https://example.com",
    "depth": 1,
    "timestamp": "2025-10-29T10:00:00Z"
}

# Content Extraction Message
{
    "type": "url_to_crawl",
    "job_id": "job_123",
    "url": "https://example.com",
    "depth": 1,
    "parent_url": "https://seed.com",
    "timestamp": "2025-10-29T10:00:05Z"
}

# Content Analysis Message
{
    "type": "content_to_analyze",
    "job_id": "job_123",
    "url": "https://example.com",
    "title": "Page Title",
    "content": "Page text content...",
    "metadata": {
        "author": "John Doe",
        "published_date": "2025-10-20",
        "word_count": 1500
    },
    "links": ["https://link1.com", "https://link2.com"],
    "timestamp": "2025-10-29T10:00:10Z"
}

# Data Persistence Message
{
    "type": "data_to_store",
    "job_id": "job_123",
    "url": "https://example.com",
    "title": "Page Title",
    "content": "Page text content...",
    "summary": "AI-generated summary...",
    "entities": [
        {"type": "PERSON", "value": "John Doe", "confidence": 0.95}
    ],
    "metadata": {...},
    "timestamp": "2025-10-29T10:00:15Z"
}
```

### Error Handling Flow

```
Error Occurs in Agent
    │
    ▼
Agent logs error and sends to coordinator
    │
    ▼
Coordinator evaluates error severity
    │
    ├─ Transient error (network timeout)
    │   └─> Retry with exponential backoff
    │
    ├─ Permanent error (404, invalid content)
    │   └─> Mark URL as failed, continue
    │
    └─ Critical error (MCP tool unavailable)
        └─> Pause job, alert admin, wait for recovery
```
---
## Performance & Scalability

### Expected Performance

| Metric | Target | Notes |
|--------|--------|-------|
| Pages/minute | 100-200 | With 5 extraction agents |
| LLM analysis/minute | 50-100 | Depends on token limits |
| Database writes/sec | 50+ | Batched writes |
| Memory usage | <2GB | For 10,000 URLs in queue |
| Disk space | ~10MB per 1000 pages | Including analysis |

### Scaling Strategies

**Horizontal Scaling**:
```python
# Increase agent counts
config = {
    'num_url_agents': 5,          # More URL discovery
    'num_extraction_agents': 10,  # More HTTP requests
    'num_analysis_agents': 5,     # More LLM calls
}
```

**Vertical Scaling**:
- Increase queue sizes for better buffering
- Increase SQLite cache size
- Use faster disks (SSD/NVMe)

**Distributed Scaling** (Advanced):
- Use Redis for distributed queues
- Multiple crawler instances
- Shared SQLite database (or migrate to PostgreSQL)
- Load balancer for coordination

### Bottleneck Analysis

**Potential Bottlenecks**:

1. **LLM API Rate Limits**
   - Solution: Batch requests, use multiple API keys, implement retry with backoff

2. **SQLite Write Lock**
   - Solution: Batch writes, use WAL mode, consider PostgreSQL for high concurrency

3. **Network I/O**
   - Solution: Increase extraction agents, use connection pooling, implement caching

4. **Memory (Large Queues)**
   - Solution: Limit queue sizes, implement disk-backed queues, process in batches

---

## Monitoring & Observability

### Key Metrics to Track

```python
metrics = {
    # Throughput
    'urls_discovered_per_minute': 0,
    'pages_crawled_per_minute': 0,
    'pages_analyzed_per_minute': 0,

    # Queue Depths
    'url_queue_size': 0,
    'extraction_queue_size': 0,
    'analysis_queue_size': 0,
    'persistence_queue_size': 0,

    # Success Rates
    'extraction_success_rate': 0.0,
    'analysis_success_rate': 0.0,
    'persistence_success_rate': 0.0,

    # Performance
    'avg_extraction_time_ms': 0,
    'avg_analysis_time_ms': 0,
    'avg_persistence_time_ms': 0,

    # Costs
    'total_tokens_used': 0,
    'estimated_cost_usd': 0.0,

    # Errors
    'http_errors': 0,
    'parse_errors': 0,
    'llm_errors': 0,
    'database_errors': 0
}
```

### Logging Strategy

```python
from loguru import logger

# Configure logging
logger.add(
    "logs/crawler_{time}.log",
    rotation="100 MB",
    retention="7 days",
    level="INFO",
    format="{time} | {level} | {name}:{function}:{line} | {message}"
)

# Log examples
logger.info(f"Started crawl job {job_id}")
logger.warning(f"Failed to fetch {url}: {error}")
logger.error(f"Database error: {error}")
logger.debug(f"Queue sizes: {queue_sizes}")
```

### Dashboard (Simple)

```python
# Simple text-based dashboard
import curses

def display_dashboard(stdscr, metrics):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== Multi-Agent Crawler Dashboard ===")
    stdscr.addstr(2, 0, f"Throughput:")
    stdscr.addstr(3, 2, f"URLs/min: {metrics['urls_discovered_per_minute']}")
    stdscr.addstr(4, 2, f"Pages/min: {metrics['pages_crawled_per_minute']}")
    stdscr.addstr(6, 0, f"Queues:")
    stdscr.addstr(7, 2, f"URL: {metrics['url_queue_size']}")
    stdscr.addstr(8, 2, f"Extraction: {metrics['extraction_queue_size']}")
    stdscr.addstr(9, 2, f"Analysis: {metrics['analysis_queue_size']}")
    stdscr.addstr(11, 0, f"Success Rates:")
    stdscr.addstr(12, 2, f"Extraction: {metrics['extraction_success_rate']:.1%}")
    stdscr.addstr(13, 2, f"Analysis: {metrics['analysis_success_rate']:.1%}")
    stdscr.refresh()
```

---

## Security & Compliance

### Security Considerations

1. **Robots.txt Compliance**
   ```python
   from urllib.robotparser import RobotFileParser

   async def check_robots_txt(url: str) -> bool:
       """Check if URL is allowed by robots.txt"""
       rp = RobotFileParser()
       rp.set_url(f"{urlparse(url).scheme}://{urlparse(url).netloc}/robots.txt")
       rp.read()
       return rp.can_fetch("MultiAgentCrawler", url)
   ```

2. **Rate Limiting (Respectful Crawling)**
   ```python
   from collections import defaultdict
   import time

   class RateLimiter:
       def __init__(self, requests_per_second=1):
           self.rps = requests_per_second
           self.last_request = defaultdict(float)

       async def wait_if_needed(self, domain: str):
           """Wait if we're crawling too fast"""
           now = time.time()
           time_since_last = now - self.last_request[domain]
           min_interval = 1.0 / self.rps

           if time_since_last < min_interval:
               await asyncio.sleep(min_interval - time_since_last)

           self.last_request[domain] = time.time()
   ```

3. **Data Privacy**
   - Don't store personally identifiable information (PII)
   - Implement data retention policies
   - Provide data deletion mechanisms

4. **Access Control**
   - Authenticate crawl job requests
   - Restrict database access
   - Encrypt sensitive data at rest

### Compliance

**Terms of Service**:
- Respect website TOS
- Don't crawl sites that explicitly prohibit it
- Honor opt-out requests

**Legal Considerations**:
- Check copyright laws in your jurisdiction
- Comply with GDPR, CCPA if applicable
- Maintain audit logs

---

## Testing Strategy

### Unit Tests

```python
import pytest
from agents.url_discovery import URLDiscoveryAgent

@pytest.mark.asyncio
async def test_url_validation():
    """Test URL validation logic"""
    agent = URLDiscoveryAgent(search_tool, sqlite_tool)

    # Valid URLs
    assert await agent.validate_url("https://example.com", "job_123")
    assert await agent.validate_url("http://test.org/path", "job_123")

    # Invalid URLs
    assert not await agent.validate_url("not-a-url", "job_123")
    assert not await agent.validate_url("ftp://ftp.example.com", "job_123")

@pytest.mark.asyncio
async def test_link_extraction():
    """Test link extraction from HTML"""
    agent = URLDiscoveryAgent(search_tool, sqlite_tool)

    html = '<a href="/page1">Link 1</a><a href="https://other.com">Link 2</a>'
    links = await agent.extract_links(html, "https://example.com")

    assert "https://example.com/page1" in links
    assert "https://other.com" in links
```

### Integration Tests

```python
@pytest.mark.asyncio
async def test_full_crawl_pipeline():
    """Test complete crawl workflow"""
    # Setup
    crawler = MultiAgentCrawler(test_config)

    # Start crawl
    job_id = await crawler.coordinator.start_crawl_job(
        "https://example.com",
        max_depth=1
    )

    # Wait for completion
    await asyncio.sleep(30)

    # Verify results
    stats = await crawler.coordinator.monitor_progress(job_id)
    assert stats['crawled'] > 0

    # Check database
    content = await crawler.sqlite_tool.query("""
        SELECT COUNT(*) FROM content WHERE job_id = ?
    """, (job_id,))

    assert content[0][0] > 0
```

### Load Tests

```python
import asyncio

async def load_test_extraction():
    """Test extraction agent under load"""
    agent = ContentExtractionAgent(search_tool)

    # Generate 100 concurrent requests
    urls = [f"https://example.com/page{i}" for i in range(100)]
    tasks = [agent.fetch_content(url) for url in urls]

    start = time.time()
    results = await asyncio.gather(*tasks)
    elapsed = time.time() - start

    success_rate = sum(1 for r in results if r['status'] == 'success') / len(results)
    throughput = len(urls) / elapsed

    print(f"Success rate: {success_rate:.1%}")
    print(f"Throughput: {throughput:.1f} pages/sec")

    assert success_rate > 0.9
    assert throughput > 10
```

---

## Conclusion

This implementation plan provides a comprehensive blueprint for building a production-ready multi-agent web crawler using:

- **Hierarchical + Parallel** architecture for optimal performance
- **MCP tools** (Search + SQLite) for discovery and persistence
- **LLM-based analysis** for content enrichment
- **Queue-based communication** for scalability
- **Comprehensive error handling** for reliability

### Next Steps

1. **Week 1-2**: Build foundation (database, MCP integration, coordinator)
2. **Week 2-3**: Implement discovery and extraction agents
3. **Week 3-4**: Add LLM analysis and persistence
4. **Week 4-5**: Complete orchestration and monitoring
5. **Week 5-6**: Testing, optimization, documentation

### Success Criteria

- ✅ Can crawl 1000+ pages reliably
- ✅ >95% successful content extraction
- ✅ High-quality LLM summaries and analysis
- ✅ Real-time monitoring and alerting
- ✅ Comprehensive test coverage
- ✅ Complete documentation

---

*Created: October 2025*
*Status: Implementation Ready*
