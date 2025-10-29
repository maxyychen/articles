# Academic Researcher Discovery Crawler

A specialized multi-agent web crawler for discovering professors and researchers in specific fields, extracting their profiles, publications, affiliations, and contact information.

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Use Case Specifications](#use-case-specifications)
3. [Specialized Agent Architecture](#specialized-agent-architecture)
4. [Data Schema](#data-schema)
5. [Agent Design](#agent-design)
6. [Workflow](#workflow)
7. [Code Examples](#code-examples)
8. [Data Sources](#data-sources)
9. [Implementation Roadmap](#implementation-roadmap)

---

## Executive Summary

### Project Goal

Build an intelligent multi-agent crawler that discovers **professors and researchers** working in specific research fields by:

1. **Accepting research keywords** (e.g., "multi-agent systems", "reinforcement learning")
2. **Expanding keywords** to related academic terms
3. **Discovering researcher profiles** from multiple sources:
   - University faculty pages
   - Google Scholar profiles
   - Research lab websites
   - Conference proceedings
   - Academic social networks (ResearchGate, Academia.edu)
4. **Extracting structured information**:
   - Full name, title, position
   - Current affiliation (university, department, lab)
   - Research interests and areas
   - Recent publications (titles, venues, years)
   - Contact information (email, office, website)
   - Social profiles (Google Scholar, ORCID, LinkedIn)
5. **Storing in structured database** for querying and analysis

### Key Features

- 🔍 **Intelligent Query Expansion**: "multi-agent systems" → "MAS", "agent coordination", "distributed AI", etc.
- 🎓 **Multi-Source Discovery**: Aggregates from universities, Google Scholar, research labs
- 📊 **Publication Extraction**: Recent papers with titles, venues, co-authors
- 📧 **Contact Discovery**: Email, phone, office location, personal website
- 🏛️ **Affiliation Tracking**: University, department, lab, research group
- 🔗 **Profile Linking**: Links duplicate profiles of same researcher
- 📈 **Relevance Scoring**: Ranks researchers by relevance to query

---

## Use Case Specifications

### Input

```python
query = {
    "keywords": ["multi-agent systems", "agent coordination"],
    "filters": {
        "regions": ["USA", "Europe"],  # Optional
        "institutions": ["MIT", "Stanford", "CMU"],  # Optional
        "min_publications": 5,  # Minimum recent publications
        "years": [2020, 2025]  # Publication date range
    }
}
```

### Output

**Structured Researcher Profiles:**

```json
{
    "researcher_id": "uuid",
    "name": "Dr. Jane Smith",
    "title": "Associate Professor",
    "affiliation": {
        "university": "Stanford University",
        "department": "Computer Science",
        "lab": "Multi-Agent Systems Lab",
        "country": "USA"
    },
    "research_interests": [
        "Multi-agent systems",
        "Reinforcement learning",
        "Agent coordination"
    ],
    "recent_publications": [
        {
            "title": "Scalable Multi-Agent Coordination via...",
            "venue": "ICML 2024",
            "year": 2024,
            "authors": ["Jane Smith", "John Doe"],
            "citations": 15,
            "url": "https://..."
        }
    ],
    "contact": {
        "email": "jsmith@stanford.edu",
        "office": "Gates 392",
        "phone": "+1-650-xxx-xxxx",
        "website": "https://jsmith.stanford.edu"
    },
    "profiles": {
        "google_scholar": "https://scholar.google.com/citations?user=...",
        "orcid": "0000-0001-2345-6789",
        "linkedin": "https://linkedin.com/in/jsmith",
        "twitter": "@jsmith_ai"
    },
    "relevance_score": 0.92,
    "last_updated": "2025-10-29"
}
```

---

## Specialized Agent Architecture

### Agent Hierarchy

```
                    ┌──────────────────┐
                    │  User Keywords   │
                    │ (Research Field) │
                    └────────┬─────────┘
                             ▼
                    ┌──────────────────┐
                    │ Academic Query   │
                    │ Expansion Agent  │
                    └────────┬─────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                     Coordinator Agent                        │
└────────────┬────────────────────────────────────────────────┘
             │
             ├──────────────┬──────────────┬──────────────┬──────────────┐
             ▼              ▼              ▼              ▼              ▼
    ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐
    │ Academic   │  │ Profile    │  │Publication │  │  Profile   │  │    Data    │
    │   URL      │  │ Extraction │  │ Extraction │  │  Linking   │  │Persistence │
    │ Discovery  │  │   Agent    │  │   Agent    │  │   Agent    │  │   Agent    │
    └─────┬──────┘  └─────┬──────┘  └─────┬──────┘  └─────┬──────┘  └─────┬──────┘
          │               │               │               │               │
          ▼               ▼               ▼               ▼               ▼
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                          Message Queues                                  │
    └─────────────────────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌──────────────────────┐
              │    SQLite Database   │
              │ (Researcher Profiles)│
              └──────────────────────┘
```

### Specialized Agents

1. **Academic Query Expansion Agent**: Expands research field keywords into academic terminology
2. **Academic URL Discovery Agent**: Finds university faculty pages, Google Scholar profiles, lab pages
3. **Profile Extraction Agent**: Extracts researcher name, title, affiliation, contact from web pages
4. **Publication Extraction Agent**: Extracts recent publications from Google Scholar, DBLP, etc.
5. **Profile Linking Agent**: Links duplicate profiles of the same researcher across sources
6. **Data Persistence Agent**: Stores structured researcher profiles in database

---

## Data Schema

### Database Tables

```sql
-- Researchers
CREATE TABLE researchers (
    researcher_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL,
    name TEXT NOT NULL,
    normalized_name TEXT NOT NULL, -- For matching duplicates
    title TEXT, -- Professor, Associate Professor, Research Scientist, etc.
    position_level TEXT, -- Assistant, Associate, Full, Emeritus, Postdoc, PhD Student
    affiliation_university TEXT,
    affiliation_department TEXT,
    affiliation_lab TEXT,
    affiliation_country TEXT,
    research_interests TEXT, -- JSON array
    h_index INTEGER,
    total_citations INTEGER,
    relevance_score FLOAT, -- 0.0 to 1.0
    discovered_from TEXT, -- Source URL
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (job_id) REFERENCES crawl_jobs(job_id) ON DELETE CASCADE
);

CREATE INDEX idx_researchers_job ON researchers(job_id);
CREATE INDEX idx_researchers_name ON researchers(normalized_name);
CREATE INDEX idx_researchers_affiliation ON researchers(affiliation_university);
CREATE INDEX idx_researchers_relevance ON researchers(relevance_score DESC);

-- Contact Information
CREATE TABLE researcher_contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    researcher_id TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    office TEXT,
    website TEXT,
    verified BOOLEAN DEFAULT 0, -- Email/phone verified
    FOREIGN KEY (researcher_id) REFERENCES researchers(researcher_id) ON DELETE CASCADE
);

CREATE INDEX idx_contacts_researcher ON researcher_contacts(researcher_id);
CREATE INDEX idx_contacts_email ON researcher_contacts(email);

-- Social Profiles
CREATE TABLE researcher_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    researcher_id TEXT NOT NULL,
    profile_type TEXT NOT NULL, -- 'google_scholar', 'orcid', 'linkedin', 'researchgate', 'twitter'
    profile_url TEXT NOT NULL,
    profile_id TEXT, -- Platform-specific ID
    verified BOOLEAN DEFAULT 0,
    FOREIGN KEY (researcher_id) REFERENCES researchers(researcher_id) ON DELETE CASCADE
);

CREATE INDEX idx_profiles_researcher ON researcher_profiles(researcher_id);
CREATE INDEX idx_profiles_type ON researcher_profiles(profile_type);

-- Publications
CREATE TABLE publications (
    publication_id TEXT PRIMARY KEY,
    researcher_id TEXT NOT NULL,
    title TEXT NOT NULL,
    venue TEXT, -- Conference or journal name
    venue_type TEXT, -- 'conference', 'journal', 'workshop', 'arxiv'
    year INTEGER,
    authors TEXT, -- JSON array of author names
    abstract TEXT,
    citations INTEGER,
    url TEXT,
    doi TEXT,
    pdf_url TEXT,
    FOREIGN KEY (researcher_id) REFERENCES researchers(researcher_id) ON DELETE CASCADE
);

CREATE INDEX idx_pubs_researcher ON publications(researcher_id);
CREATE INDEX idx_pubs_year ON publications(year DESC);
CREATE INDEX idx_pubs_citations ON publications(citations DESC);
CREATE INDEX idx_pubs_venue ON publications(venue);

-- Publication-Keyword Relevance
CREATE TABLE publication_keywords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    publication_id TEXT NOT NULL,
    keyword TEXT NOT NULL,
    relevance FLOAT, -- How relevant this pub is to the keyword
    FOREIGN KEY (publication_id) REFERENCES publications(publication_id) ON DELETE CASCADE
);

CREATE INDEX idx_pubkeys_publication ON publication_keywords(publication_id);
CREATE INDEX idx_pubkeys_keyword ON publication_keywords(keyword);

-- Profile Links (for deduplication)
CREATE TABLE profile_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    researcher_id TEXT NOT NULL, -- Primary researcher ID
    duplicate_id TEXT NOT NULL, -- Duplicate researcher ID
    confidence FLOAT, -- 0.0 to 1.0, how confident this is same person
    link_reason TEXT, -- 'name_match', 'email_match', 'publication_overlap', etc.
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (researcher_id) REFERENCES researchers(researcher_id) ON DELETE CASCADE
);

CREATE INDEX idx_links_researcher ON profile_links(researcher_id);
CREATE INDEX idx_links_duplicate ON profile_links(duplicate_id);

-- Discovery URLs (for tracking sources)
CREATE TABLE discovery_urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT NOT NULL,
    url TEXT NOT NULL,
    url_type TEXT, -- 'faculty_page', 'google_scholar', 'lab_page', 'personal_site'
    status TEXT DEFAULT 'pending', -- 'pending', 'processed', 'failed'
    researcher_count INTEGER DEFAULT 0, -- How many researchers found from this URL
    processed_at TIMESTAMP,
    FOREIGN KEY (job_id) REFERENCES crawl_jobs(job_id) ON DELETE CASCADE
);

CREATE INDEX idx_discovery_job ON discovery_urls(job_id);
CREATE INDEX idx_discovery_status ON discovery_urls(status);
CREATE INDEX idx_discovery_type ON discovery_urls(url_type);
```

---

## Agent Design

### 1. Academic Query Expansion Agent

**Specialized for academic terminology**

**Expansion Strategy:**
```python
Input: "multi-agent systems"

Synonyms:
- MAS
- agent-based systems
- distributed agent systems

Related Academic Terms:
- agent coordination
- multi-agent learning
- agent communication
- cooperative agents
- distributed artificial intelligence

Narrower (Specific Topics):
- multi-agent reinforcement learning
- agent negotiation
- coalition formation
- task allocation

Conference/Venue Names:
- AAMAS (Autonomous Agents and Multi-Agent Systems)
- AAAI
- IJCAI

Key Researchers (for bootstrapping):
- Michael Wooldridge
- Milind Tambe
- Nicholas Jennings
```

**LLM Prompt:**
```python
prompt = f"""You are an academic research expert. Expand the research field keyword into comprehensive academic search terms.

Research Field: {keyword}

Provide:
1. Synonyms and abbreviations used in academia
2. Related research topics and subtopics
3. Specific technical terms and methods
4. Major conferences and journals in this field
5. Well-known researchers in this field (for bootstrapping)

Return as JSON with relevance scores (0.0-1.0).
"""
```

---

### 2. Academic URL Discovery Agent

**Specialized for finding academic sources**

**Target Sources:**

1. **University Faculty Pages**
   - Search: `"[field] professor" site:edu`
   - Examples:
     - `stanford.edu/cs/faculty`
     - `mit.edu/eecs/people`

2. **Google Scholar Profiles**
   - Search: `site:scholar.google.com "[field]"`
   - Direct profile URLs

3. **Research Lab Pages**
   - Search: `"[field] lab" OR "[field] research group"`
   - Examples:
     - `Multi-Agent Systems Lab`
     - `Robotics Institute`

4. **Academic Social Networks**
   - ResearchGate: `site:researchgate.net "[field]"`
   - Academia.edu: `site:academia.edu "[field]"`

5. **Conference Proceedings**
   - DBLP: `site:dblp.org "[field]"`
   - ACM Digital Library
   - IEEE Xplore

**Discovery Strategy:**
```python
async def discover_academic_urls(self, expanded_terms, job_id):
    """Discover academic URLs using multiple strategies"""
    urls = []

    # Strategy 1: University faculty pages
    for term in expanded_terms:
        query = f'"{term}" professor site:.edu'
        results = await self.search_mcp.search(query, max_results=20)
        urls.extend(self._filter_faculty_pages(results))

    # Strategy 2: Google Scholar profiles
    for term in expanded_terms:
        query = f'site:scholar.google.com "{term}"'
        results = await self.search_mcp.search(query, max_results=50)
        urls.extend(self._filter_scholar_profiles(results))

    # Strategy 3: Research lab pages
    for term in expanded_terms:
        query = f'"{term}" lab OR "{term}" research group'
        results = await self.search_mcp.search(query, max_results=20)
        urls.extend(self._filter_lab_pages(results))

    # Strategy 4: Academic social networks
    for term in expanded_terms:
        queries = [
            f'site:researchgate.net "{term}"',
            f'site:academia.edu "{term}"'
        ]
        for query in queries:
            results = await self.search_mcp.search(query, max_results=20)
            urls.extend(results)

    return self._deduplicate_urls(urls)
```

---

### 3. Profile Extraction Agent

**Specialized for extracting researcher information from web pages**

**Extraction Targets:**

From **Faculty Pages**:
- Name (with title: Dr., Prof.)
- Position (Assistant/Associate/Full Professor)
- Department and Lab affiliation
- Email (often obfuscated: `name [at] domain [dot] edu`)
- Office location
- Personal website link

From **Google Scholar Profiles**:
- Name
- Affiliation
- Research interests (listed explicitly)
- H-index, i10-index
- Total citations
- Recent publications (top 10-20)

From **Personal Websites**:
- Bio and research overview
- CV/Resume link
- Publication list
- Contact information

**LLM-Based Extraction Prompt:**
```python
extraction_prompt = f"""Extract researcher profile information from this web page.

URL: {url}
Content:
{content}

Extract the following fields (return "null" if not found):

{{
    "name": "Full name with title (Dr., Prof.)",
    "title": "Academic title/position",
    "position_level": "Assistant/Associate/Full/Emeritus/Postdoc/PhD Student",
    "affiliation": {{
        "university": "University name",
        "department": "Department name",
        "lab": "Lab or research group name"
    }},
    "research_interests": ["topic1", "topic2", ...],
    "contact": {{
        "email": "email@domain.edu",
        "phone": "+1-xxx-xxx-xxxx",
        "office": "Building Room",
        "website": "Personal website URL"
    }},
    "profiles": {{
        "google_scholar": "URL if found",
        "orcid": "ORCID ID if found",
        "linkedin": "URL if found"
    }}
}}

Be thorough but accurate. Only extract information explicitly stated on the page.
"""
```

---

### 4. Publication Extraction Agent

**Specialized for extracting publication data**

**Data Sources:**

1. **Google Scholar Profile** (Best source)
   - Recent publications automatically listed
   - Citation counts
   - Co-authors

2. **Personal Website CV**
   - Often has complete publication list
   - May have PDFs

3. **DBLP**
   - Computer science publications
   - Structured data (venue, year, co-authors)

4. **Semantic Scholar API** (if available)
   - Rich publication metadata
   - Citations, references, abstracts

**Extraction Strategy:**
```python
async def extract_publications(self, researcher_id, google_scholar_url):
    """Extract recent publications from Google Scholar profile"""

    # Fetch Google Scholar profile
    html = await self.http_client.get(google_scholar_url)
    soup = BeautifulSoup(html, 'lxml')

    publications = []

    # Parse publication list
    for pub_row in soup.select('.gsc_a_tr'):
        title = pub_row.select_one('.gsc_a_at').text
        authors = pub_row.select_one('.gs_gray').text
        venue_year = pub_row.select_one('.gs_gray:nth-of-type(2)').text
        citations = pub_row.select_one('.gsc_a_c').text

        # Parse venue and year
        venue, year = self._parse_venue_year(venue_year)

        publications.append({
            'title': title,
            'authors': authors.split(', '),
            'venue': venue,
            'year': year,
            'citations': int(citations) if citations else 0
        })

    return publications[:20]  # Top 20 recent publications
```

**LLM-Based Publication Relevance Scoring:**
```python
relevance_prompt = f"""Rate how relevant this publication is to the research field "{keyword}".

Publication:
Title: {title}
Abstract: {abstract}
Keywords: {keywords}

Relevance Score (0.0-1.0):
- 1.0: Directly addresses the field
- 0.7-0.9: Highly related
- 0.5-0.7: Moderately related
- 0.3-0.5: Tangentially related
- 0.0-0.3: Barely related

Return JSON: {{"relevance": 0.85, "reason": "This paper directly addresses..."}}
"""
```

---

### 5. Profile Linking Agent

**Specialized for deduplicating researchers**

**Matching Strategy:**

1. **Name Matching**
   - Normalize names (remove titles, standardize format)
   - Handle variations: "J. Smith" vs "Jane Smith"
   - Fuzzy matching for typos

2. **Email Domain Matching**
   - Same email domain (e.g., `@stanford.edu`)
   - Strong indicator if name also matches

3. **Publication Overlap**
   - Count shared publications (by title similarity)
   - If >3 shared publications, likely same person

4. **Affiliation Consistency**
   - Same university + department
   - Consistent research interests

**Linking Algorithm:**
```python
async def link_profiles(self, researcher1_id, researcher2_id):
    """Determine if two researcher profiles are the same person"""

    r1 = await self.get_researcher(researcher1_id)
    r2 = await self.get_researcher(researcher2_id)

    confidence = 0.0
    reasons = []

    # Name similarity
    name_sim = self._name_similarity(r1['name'], r2['name'])
    if name_sim > 0.85:
        confidence += 0.4
        reasons.append(f'name_match_{name_sim:.2f}')

    # Email domain match
    if r1['email'] and r2['email']:
        if r1['email'].split('@')[1] == r2['email'].split('@')[1]:
            confidence += 0.3
            reasons.append('email_domain_match')

    # Affiliation match
    if r1['affiliation_university'] == r2['affiliation_university']:
        confidence += 0.2
        reasons.append('affiliation_match')

    # Publication overlap
    pub_overlap = await self._count_publication_overlap(researcher1_id, researcher2_id)
    if pub_overlap > 3:
        confidence += 0.3
        reasons.append(f'publication_overlap_{pub_overlap}')

    # Link if confidence > 0.7
    if confidence >= 0.7:
        await self._create_link(researcher1_id, researcher2_id, confidence, reasons)
        return True

    return False
```

---

## Workflow

### Complete Workflow

```
User Input: keywords = ["multi-agent systems"]
    ↓
┌─────────────────────────────────────────────┐
│ Stage 0: Academic Query Expansion           │
├─────────────────────────────────────────────┤
│ - Expand to: MAS, agent coordination,       │
│   multi-agent learning, MARL, etc.          │
│ - Generate 20-30 academic terms             │
│ - Include conference/journal names          │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│ Stage 1: Academic URL Discovery             │
├─────────────────────────────────────────────┤
│ Search for:                                  │
│ - University faculty pages (.edu)           │
│ - Google Scholar profiles                   │
│ - Research lab pages                        │
│ - ResearchGate, Academia.edu                │
│ Result: 200-500 URLs                        │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│ Stage 2: Profile Extraction (Parallel)      │
├─────────────────────────────────────────────┤
│ For each URL:                                │
│ - Extract researcher name, title            │
│ - Extract affiliation (uni, dept, lab)      │
│ - Extract research interests                │
│ - Extract contact (email, phone, office)    │
│ - Extract profile links (Scholar, ORCID)    │
│ Result: 100-300 researcher profiles         │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│ Stage 3: Publication Extraction (Parallel)  │
├─────────────────────────────────────────────┤
│ For each researcher:                         │
│ - Fetch Google Scholar profile              │
│ - Extract recent publications (top 20)      │
│ - Get citation counts                       │
│ - Score publication relevance               │
│ Result: 1000-5000 publications              │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│ Stage 4: Profile Linking (Sequential)       │
├─────────────────────────────────────────────┤
│ - Compare all researcher pairs              │
│ - Match by: name, email, affiliation, pubs │
│ - Link duplicates (confidence > 0.7)        │
│ - Merge profiles                            │
│ Result: 80-200 unique researchers           │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│ Stage 5: Relevance Scoring                  │
├─────────────────────────────────────────────┤
│ For each researcher:                         │
│ - Score based on publication relevance      │
│ - Weight by citations and recency           │
│ - Boost for keyword match in interests      │
│ Result: Ranked list of researchers          │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│ Stage 6: Data Persistence                   │
├─────────────────────────────────────────────┤
│ - Store in SQLite database                  │
│ - Index for fast querying                   │
│ - Generate summary report                   │
└─────────────────┬───────────────────────────┘
                  ↓
            Results Ready!
```

### Execution Time Estimate

For query: `"multi-agent systems"`

| Stage | Time | Details |
|-------|------|---------|
| Query Expansion | 3-5s | 1 keyword → 25 terms |
| URL Discovery | 30-60s | 25 terms × 20 results = 500 URLs |
| Profile Extraction | 2-5 min | 500 URLs × 2-5s per URL (parallel) |
| Publication Extraction | 3-8 min | 200 profiles × 10-20s per profile (parallel) |
| Profile Linking | 1-2 min | 200 profiles → pairwise comparison |
| Relevance Scoring | 30-60s | Score 200 researchers |
| Persistence | 10-30s | Batch writes to SQLite |
| **Total** | **8-17 min** | **End-to-end for ~200 researchers** |

---

## Code Examples

### Example 1: Academic Query Expansion

```python
class AcademicQueryExpansionAgent:
    """Specialized for academic terminology expansion"""

    async def expand_academic_query(self, keywords: list[str], job_id: str) -> dict:
        """Expand research field keywords into academic terms"""

        expanded = {
            'synonyms': [],
            'related_topics': [],
            'specific_methods': [],
            'conferences': [],
            'journals': [],
            'key_researchers': []
        }

        for keyword in keywords:
            result = await self._expand_academic_term(keyword)

            for key in expanded.keys():
                if key in result:
                    expanded[key].extend(result[key])

            # Store in database
            await self._store_academic_expansion(job_id, keyword, result)

        return expanded

    async def _expand_academic_term(self, keyword: str) -> dict:
        """Use LLM to expand academic keyword"""

        prompt = f"""You are an academic research expert. Expand this research field keyword:

Research Field: "{keyword}"

Provide comprehensive academic search terms:

1. Synonyms and Abbreviations (used in academia):
2. Related Research Topics and Subtopics:
3. Specific Technical Terms and Methods:
4. Major Conferences in this field:
5. Major Journals in this field:
6. Well-known Researchers (3-5 prominent names):

Return as JSON:
{{
    "synonyms": [{{"term": "...", "relevance": 0.95}}],
    "related_topics": [{{"term": "...", "relevance": 0.85}}],
    "specific_methods": [{{"term": "...", "relevance": 0.80}}],
    "conferences": ["AAMAS", "AAAI", ...],
    "journals": ["JAIR", "AIJ", ...],
    "key_researchers": ["Michael Wooldridge", ...]
}}

Be accurate and use official names/abbreviations.
"""

        response = await self.llm_client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an academic research expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,  # Lower for accuracy
            max_tokens=800,
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)


# Example usage
agent = AcademicQueryExpansionAgent(llm_config, sqlite_tool)
expanded = await agent.expand_academic_query(["multi-agent systems"], job_id)

print("Synonyms:", expanded['synonyms'][:5])
# Output: [{'term': 'MAS', 'relevance': 1.0},
#          {'term': 'agent-based systems', 'relevance': 0.95}, ...]

print("Conferences:", expanded['conferences'])
# Output: ['AAMAS', 'AAAI', 'IJCAI', 'ICML']

print("Key Researchers:", expanded['key_researchers'])
# Output: ['Michael Wooldridge', 'Milind Tambe', 'Nicholas Jennings']
```

---

### Example 2: Profile Extraction Agent

```python
class ProfileExtractionAgent:
    """Extract researcher profiles from web pages"""

    async def extract_profile(self, url: str, job_id: str) -> dict:
        """Extract researcher profile from a web page"""

        # Fetch page content
        html = await self.http_client.get(url)

        # Determine page type
        page_type = self._detect_page_type(url)

        # Extract based on page type
        if page_type == 'google_scholar':
            profile = await self._extract_from_scholar(html, url)
        elif page_type == 'faculty_page':
            profile = await self._extract_from_faculty_page(html, url)
        elif page_type == 'personal_site':
            profile = await self._extract_from_personal_site(html, url)
        else:
            profile = await self._extract_generic(html, url)

        # Add metadata
        profile['job_id'] = job_id
        profile['discovered_from'] = url
        profile['researcher_id'] = self._generate_id(profile)

        return profile

    async def _extract_from_scholar(self, html: str, url: str) -> dict:
        """Extract from Google Scholar profile page"""
        soup = BeautifulSoup(html, 'lxml')

        # Name
        name = soup.select_one('#gsc_prf_in').text if soup.select_one('#gsc_prf_in') else None

        # Affiliation
        affiliation_text = soup.select_one('#gsc_prf_i').text if soup.select_one('#gsc_prf_i') else ""
        affiliation = self._parse_affiliation(affiliation_text)

        # Research interests
        interests = [tag.text for tag in soup.select('#gsc_prf_int a')]

        # Metrics
        h_index_elem = soup.select_one('td.gsc_rsb_std:nth-of-type(2)')
        h_index = int(h_index_elem.text) if h_index_elem else None

        citations_elem = soup.select_one('td.gsc_rsb_std:nth-of-type(1)')
        total_citations = int(citations_elem.text) if citations_elem else None

        # Email (sometimes available)
        email = soup.select_one('.gsc_prf_ila')
        email = email.text if email else None

        return {
            'name': name,
            'affiliation': affiliation,
            'research_interests': interests,
            'h_index': h_index,
            'total_citations': total_citations,
            'contact': {
                'email': email
            },
            'profiles': {
                'google_scholar': url
            }
        }

    async def _extract_from_faculty_page(self, html: str, url: str) -> dict:
        """Extract from university faculty page using LLM"""

        # Clean and truncate content
        soup = BeautifulSoup(html, 'lxml')
        text_content = soup.get_text(separator='\n', strip=True)
        text_content = text_content[:4000]  # Limit for LLM

        prompt = f"""Extract researcher profile from this faculty page.

URL: {url}
Content:
{text_content}

Extract (return null if not found):
{{
    "name": "Full name with title",
    "title": "Position (e.g., Associate Professor)",
    "position_level": "Assistant/Associate/Full/etc.",
    "affiliation": {{
        "university": "University name",
        "department": "Department",
        "lab": "Research lab/group"
    }},
    "research_interests": ["topic1", "topic2"],
    "contact": {{
        "email": "email@domain.edu",
        "phone": "phone if available",
        "office": "office location",
        "website": "personal website URL"
    }}
}}

Be precise. Only extract information explicitly stated.
"""

        response = await self.llm_client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert at extracting structured information from academic web pages."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=600,
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)

    def _parse_affiliation(self, affiliation_text: str) -> dict:
        """Parse affiliation text into structured format"""
        # Example: "Computer Science, Stanford University"
        parts = [p.strip() for p in affiliation_text.split(',')]

        return {
            'department': parts[0] if len(parts) > 0 else None,
            'university': parts[1] if len(parts) > 1 else None,
            'lab': parts[2] if len(parts) > 2 else None
        }

    def _generate_id(self, profile: dict) -> str:
        """Generate unique researcher ID"""
        import hashlib

        # Use name + affiliation for ID
        id_string = f"{profile['name']}_{profile['affiliation'].get('university', '')}"
        return hashlib.md5(id_string.encode()).hexdigest()[:16]
```

---

### Example 3: Publication Extraction Agent

```python
class PublicationExtractionAgent:
    """Extract publications from various sources"""

    async def extract_publications(self, researcher_id: str, google_scholar_url: str) -> list:
        """Extract recent publications from Google Scholar"""

        # Fetch Scholar profile
        html = await self.http_client.get(google_scholar_url)
        soup = BeautifulSoup(html, 'lxml')

        publications = []

        # Parse each publication row
        for row in soup.select('.gsc_a_tr')[:20]:  # Top 20
            try:
                # Title and URL
                title_elem = row.select_one('.gsc_a_at')
                title = title_elem.text
                pub_url = f"https://scholar.google.com{title_elem['href']}"

                # Authors
                authors_elem = row.select('.gs_gray')[0]
                authors = authors_elem.text

                # Venue and year
                venue_year_elem = row.select('.gs_gray')[1]
                venue_year_text = venue_year_elem.text
                venue, year = self._parse_venue_year(venue_year_text)

                # Citations
                citations_elem = row.select_one('.gsc_a_c')
                citations = int(citations_elem.text) if citations_elem and citations_elem.text else 0

                pub_id = hashlib.md5(f"{title}_{year}".encode()).hexdigest()[:16]

                publications.append({
                    'publication_id': pub_id,
                    'researcher_id': researcher_id,
                    'title': title,
                    'authors': authors,
                    'venue': venue,
                    'year': year,
                    'citations': citations,
                    'url': pub_url
                })

            except Exception as e:
                print(f"Error parsing publication: {e}")
                continue

        return publications

    def _parse_venue_year(self, text: str) -> tuple:
        """Parse venue and year from text like 'ICML 2024' or 'arXiv preprint, 2023'"""
        import re

        # Extract year (4-digit number)
        year_match = re.search(r'\b(19|20)\d{2}\b', text)
        year = int(year_match.group()) if year_match else None

        # Venue is everything except year
        if year_match:
            venue = text.replace(year_match.group(), '').strip(', ')
        else:
            venue = text

        return venue, year

    async def score_publication_relevance(self, publication: dict, keywords: list[str]) -> float:
        """Score how relevant a publication is to the query keywords"""

        # Simple keyword matching in title
        title_lower = publication['title'].lower()
        keyword_matches = sum(1 for kw in keywords if kw.lower() in title_lower)

        if keyword_matches > 0:
            base_score = min(0.9, 0.5 + (keyword_matches * 0.2))
        else:
            base_score = 0.3  # Default for no matches

        # Boost for recent publications
        current_year = 2025
        if publication['year']:
            years_ago = current_year - publication['year']
            recency_factor = max(0, 1.0 - (years_ago * 0.1))  # Decay 10% per year
            base_score *= (0.5 + 0.5 * recency_factor)

        # Boost for high citations (log scale)
        if publication['citations'] > 10:
            citation_factor = min(1.2, 1.0 + (0.05 * (publication['citations'] / 50)))
            base_score *= citation_factor

        return min(1.0, base_score)
```

---

### Example 4: Main Orchestration

```python
class AcademicResearcherCrawler:
    """Main crawler orchestration for academic researchers"""

    def __init__(self, config):
        # Initialize tools
        self.search_tool = SearchTool(config['search_mcp'])
        self.sqlite_tool = SqliteTool(config['sqlite_mcp'])

        # Initialize agents
        self.query_expansion_agent = AcademicQueryExpansionAgent(config['llm_config'], self.sqlite_tool)
        self.url_discovery_agent = AcademicURLDiscoveryAgent(self.search_tool, self.sqlite_tool)
        self.profile_extraction_agent = ProfileExtractionAgent(config['llm_config'], self.sqlite_tool)
        self.publication_agent = PublicationExtractionAgent(self.sqlite_tool)
        self.linking_agent = ProfileLinkingAgent(self.sqlite_tool)

    async def discover_researchers(self, keywords: list[str], filters: dict = None) -> str:
        """
        Main entry point: Discover researchers in a field

        Args:
            keywords: Research field keywords (e.g., ["multi-agent systems"])
            filters: Optional filters (regions, institutions, min_publications, etc.)

        Returns:
            job_id for tracking and retrieving results
        """
        job_id = str(uuid.uuid4())

        print(f"🔍 Starting researcher discovery: {keywords}")
        print(f"📋 Job ID: {job_id}")

        # Create job in database
        await self._create_job(job_id, keywords, filters)

        # Stage 0: Query Expansion
        print("\n📚 Stage 0: Expanding academic keywords...")
        expanded = await self.query_expansion_agent.expand_academic_query(keywords, job_id)

        print(f"   ✓ Expanded to {sum(len(v) for v in expanded.values() if isinstance(v, list))} terms")
        print(f"   - Conferences: {', '.join(expanded['conferences'][:5])}")
        print(f"   - Key researchers: {', '.join(expanded['key_researchers'][:3])}")

        # Stage 1: URL Discovery
        print("\n🌐 Stage 1: Discovering academic URLs...")
        urls = await self.url_discovery_agent.discover_academic_urls(expanded, job_id, filters)

        print(f"   ✓ Found {len(urls)} URLs")
        print(f"   - Faculty pages: {len([u for u in urls if u['type'] == 'faculty_page'])}")
        print(f"   - Google Scholar: {len([u for u in urls if u['type'] == 'google_scholar'])}")
        print(f"   - Lab pages: {len([u for u in urls if u['type'] == 'lab_page'])}")

        # Stage 2: Profile Extraction (Parallel)
        print("\n👤 Stage 2: Extracting researcher profiles...")
        profiles = await self._extract_profiles_parallel(urls, job_id)

        print(f"   ✓ Extracted {len(profiles)} profiles")

        # Stage 3: Publication Extraction (Parallel)
        print("\n📄 Stage 3: Extracting publications...")
        pub_count = await self._extract_publications_parallel(profiles, job_id, keywords)

        print(f"   ✓ Extracted {pub_count} publications")

        # Stage 4: Profile Linking
        print("\n🔗 Stage 4: Linking duplicate profiles...")
        links_count = await self.linking_agent.link_all_profiles(job_id)

        unique_count = len(profiles) - links_count
        print(f"   ✓ Found {links_count} duplicates, {unique_count} unique researchers")

        # Stage 5: Relevance Scoring
        print("\n⭐ Stage 5: Scoring researcher relevance...")
        await self._score_researchers(job_id, keywords)

        # Mark job complete
        await self._complete_job(job_id)

        print(f"\n✅ Discovery complete! Job ID: {job_id}")
        print(f"   Run `get_results('{job_id}')` to retrieve researchers")

        return job_id

    async def get_results(self, job_id: str, min_relevance: float = 0.5, limit: int = 50) -> list:
        """
        Get discovered researchers for a job

        Args:
            job_id: Job ID from discover_researchers()
            min_relevance: Minimum relevance score (0.0-1.0)
            limit: Maximum number of results

        Returns:
            List of researcher profiles sorted by relevance
        """
        results = await self.sqlite_tool.query("""
            SELECT
                r.researcher_id,
                r.name,
                r.title,
                r.affiliation_university,
                r.affiliation_department,
                r.research_interests,
                r.relevance_score,
                c.email,
                c.website,
                p.profile_url as google_scholar,
                COUNT(DISTINCT pub.publication_id) as publication_count
            FROM researchers r
            LEFT JOIN researcher_contacts c ON r.researcher_id = c.researcher_id
            LEFT JOIN researcher_profiles p ON r.researcher_id = p.researcher_id
                AND p.profile_type = 'google_scholar'
            LEFT JOIN publications pub ON r.researcher_id = pub.researcher_id
            WHERE r.job_id = ? AND r.relevance_score >= ?
            GROUP BY r.researcher_id
            ORDER BY r.relevance_score DESC
            LIMIT ?
        """, (job_id, min_relevance, limit))

        # Format results
        researchers = []
        for row in results:
            researchers.append({
                'researcher_id': row[0],
                'name': row[1],
                'title': row[2],
                'university': row[3],
                'department': row[4],
                'research_interests': json.loads(row[5]) if row[5] else [],
                'relevance_score': row[6],
                'email': row[7],
                'website': row[8],
                'google_scholar': row[9],
                'publication_count': row[10]
            })

        return researchers


# Example usage
async def main():
    config = {
        'search_mcp': {'endpoint': 'http://localhost:8001'},
        'sqlite_mcp': {'database': 'researchers.db'},
        'llm_config': {
            'base_url': 'http://localhost:8080/v1',
            'model': 'gpt-oss:20b',
            'api_key': 'not-needed'
        }
    }

    crawler = AcademicResearcherCrawler(config)

    # Discover researchers
    job_id = await crawler.discover_researchers(
        keywords=["multi-agent systems", "agent coordination"],
        filters={
            'min_publications': 5,
            'years': [2020, 2025]
        }
    )

    # Get results
    researchers = await crawler.get_results(job_id, min_relevance=0.7, limit=20)

    # Display results
    print(f"\n{'='*80}")
    print(f"Top {len(researchers)} Researchers in Multi-Agent Systems")
    print(f"{'='*80}\n")

    for i, r in enumerate(researchers, 1):
        print(f"{i}. {r['name']} (Relevance: {r['relevance_score']:.2f})")
        print(f"   {r['title']} at {r['university']}")
        print(f"   Research: {', '.join(r['research_interests'][:3])}")
        print(f"   Publications: {r['publication_count']}")
        if r['email']:
            print(f"   Email: {r['email']}")
        if r['google_scholar']:
            print(f"   Scholar: {r['google_scholar']}")
        print()

if __name__ == '__main__':
    asyncio.run(main())
```

---

## Data Sources

### Primary Sources

| Source | Type | Information Available | API/Scraping |
|--------|------|----------------------|--------------|
| **University Faculty Pages** | Directory | Name, title, department, email, office | Scraping |
| **Google Scholar** | Profile | Name, affiliation, publications, h-index, citations | Scraping |
| **DBLP** | Database | CS publications, venues, co-authors | API available |
| **Semantic Scholar** | API | Publications, citations, abstracts, PDFs | API (free) |
| **ORCID** | Registry | Researcher ID, publications, affiliations | API (free) |
| **ResearchGate** | Social | Profile, publications, co-authors | Scraping |
| **Academia.edu** | Social | Profile, papers, interests | Scraping |
| **ACM Digital Library** | Database | CS publications, citations | API (paid) |
| **IEEE Xplore** | Database | Engineering publications | API (paid) |
| **arXiv** | Preprint | Recent papers, abstracts, PDFs | API (free) |

### Search Strategies

**For University Faculty:**
```
"multi-agent systems" professor site:.edu
"agent coordination" faculty site:.edu
"[university name]" computer science faculty
```

**For Google Scholar:**
```
site:scholar.google.com "multi-agent systems"
site:scholar.google.com "AAMAS" (conference name)
```

**For Research Labs:**
```
"multi-agent" lab OR "multi-agent" research group
"Stanford" "agent" lab
```

---

## Implementation Roadmap

### Phase 1: Core Infrastructure

**Goals**: Database, MCP integration, basic agents

**Tasks**:
1. Set up SQLite database with researcher schema
2. Configure Search & SQLite MCP tools
3. Implement Academic Query Expansion Agent
4. Test keyword expansion with sample queries

**Deliverables**:
- Working database with all tables
- Query expansion generating 20-30 terms

---

### Phase 2: URL Discovery

**Goals**: Find academic sources

**Tasks**:
1. Implement Academic URL Discovery Agent
2. Add filters for page types (faculty, scholar, lab)
3. Test with multiple research fields
4. Optimize search queries for recall

**Deliverables**:
- Discover 200-500 URLs per query
- Categorize by source type

---

### Phase 3: Profile Extraction

**Goals**: Extract researcher information

**Tasks**:
1. Implement Profile Extraction Agent
2. Add specialized extractors for:
   - Google Scholar profiles
   - Faculty pages
   - Personal websites
3. LLM-based extraction for unstructured pages
4. Test extraction accuracy

**Deliverables**:
- Extract profiles with >85% accuracy
- Handle multiple page formats

---

### Phase 4: Publication Extraction

**Goals**: Get researcher publications

**Tasks**:
1. Implement Publication Extraction Agent
2. Parse Google Scholar publication lists
3. Extract from DBLP (if available)
4. Score publication relevance to query

**Deliverables**:
- Extract 10-20 recent publications per researcher
- Relevance scoring implemented

---

### Phase 5: Profile Linking

**Goals**: Deduplicate researchers

**Tasks**:
1. Implement Profile Linking Agent
2. Name matching algorithm
3. Publication overlap detection
4. Affiliation matching
5. Merge duplicate profiles

**Deliverables**:
- Link duplicates with >90% accuracy
- Reduce profile count by 20-40%

---

### Phase 6: End-to-End Testing

**Goals**: Complete system validation

**Tasks**:
1. Test with 10 different research fields
2. Validate extraction accuracy manually
3. Optimize performance (parallel processing)
4. Generate comprehensive reports

**Deliverables**:
- System discovers 100-300 researchers per field
- 8-15 minute end-to-end time
- >85% profile accuracy

---

## Success Metrics

### Quantitative Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Recall** | >80% | % of known researchers found |
| **Precision** | >85% | % of extracted profiles that are relevant |
| **Profile Completeness** | >70% | % of profiles with email + publications |
| **Deduplication Accuracy** | >90% | % of correctly linked duplicates |
| **Relevance Scoring** | >0.75 | Average relevance score of top 50 results |
| **Processing Time** | <15 min | End-to-end for 200 researchers |

### Qualitative Metrics

- ✅ Discovers both junior and senior researchers
- ✅ Finds researchers from diverse institutions
- ✅ Extracts accurate contact information
- ✅ Recent publications (last 5 years) included
- ✅ Handles different page formats robustly

---

## Conclusion

This specialized academic researcher crawler provides a **comprehensive solution** for discovering professors and researchers in specific fields by:

- 🎓 **Academic-focused**: Optimized for academic sources (faculty pages, Google Scholar, labs)
- 🔍 **Comprehensive**: Discovers 100-300 researchers per field
- 📊 **Structured**: Extracts detailed profiles with publications and contact info
- 🔗 **Intelligent**: Links duplicate profiles automatically
- ⭐ **Ranked**: Scores and ranks researchers by relevance
- ⚡ **Fast**: Completes in 8-17 minutes using local GPT-OSS:20B

Perfect for:
- **Literature reviews**: Find key researchers in a field
- **Collaboration discovery**: Identify potential collaborators
- **Hiring**: Discover candidates for academic positions
- **Conference planning**: Find experts for invited talks
- **Grant writing**: Identify researchers for consortiums

---

*Created: October 2025*
*Status: Implementation Ready*
