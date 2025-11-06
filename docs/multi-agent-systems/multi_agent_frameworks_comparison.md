# Multi-Agent AI Frameworks & SDKs: Comprehensive Comparison (2025)

A detailed analysis of leading multi-agent AI frameworks and SDKs, their communication protocols, orchestration patterns, and use cases - including production-ready SDKs from OpenAI, Anthropic, and Google.

*Last Updated: October 31, 2025*

---

## Table of Contents

1. [Overview](#overview)
2. [Framework & SDK Comparison Matrix](#framework--sdk-comparison-matrix)
3. [Detailed Framework Analysis](#detailed-framework-analysis)
   - Part I: Production SDKs
     - OpenAI Agents SDK
     - Claude Agent SDK
     - Google ADK
   - Part II: Open-Source Frameworks
     - AG2 (AutoGen)
     - CrewAI
     - LangGraph
     - Microsoft Agent Framework
     - PydanticAI
     - OpenAI Swarm (Deprecated)
     - smolagents
     - Haystack
4. [Communication Protocols](#communication-protocols)
5. [Orchestration Patterns](#orchestration-patterns)
6. [Use Case Recommendations](#use-case-recommendations)
7. [Getting Started Guide](#getting-started-guide)
8. [Key Takeaways](#key-takeaways)
9. [Resources](#resources)
10. [Conclusion](#conclusion)

---

## Overview

Multi-agent AI frameworks and SDKs enable developers to build sophisticated systems where multiple AI agents collaborate to solve complex problems. This comprehensive guide covers both **vendor-provided production SDKs** (OpenAI, Anthropic, Google) and **open-source frameworks** (AutoGen, CrewAI, LangGraph, etc.).

### Key Concepts

- **Agent**: An autonomous AI entity that can perceive, reason, and act
- **SDK vs Framework**: SDKs are production-ready vendor solutions; frameworks are community-driven tools
- **Communication Protocol**: The method by which agents exchange information
- **Orchestration**: The coordination and management of multiple agents
- **State Management**: How agents maintain and share context
- **Tool Calling**: How agents access external capabilities
- **Computer Use**: Direct system access for file operations and terminal commands

---

## Framework & SDK Comparison Matrix

### Production SDKs (Vendor-Supported)

| SDK | Vendor | Released | Type | Model Support | Computer Use | Multi-Agent | Learning Curve | Typical Cost |
|-----|--------|----------|------|---------------|--------------|-------------|----------------|--------------|
| **OpenAI Agents SDK** | OpenAI | Mar 2025 | Multi-provider | 100+ via LiteLLM | Limited | Handoffs | Low | $500-$50K+/mo |
| **Claude Agent SDK** | Anthropic | Sep 2025 | Computer-use | Claude only | Best-in-class | Subagents | Medium | $500-$75K+/mo |
| **Google ADK** | Google | Apr 2025 | Model-agnostic | Multi-provider | Good | Hierarchical | Medium | $300-$40K+/mo |

### Open-Source Frameworks

| Framework | Developer | Stars | Released | Type | Communication Style | Orchestration | Learning Curve |
|-----------|-----------|-------|----------|------|-------------------|---------------|----------------|
| **AG2 (AutoGen)** | Microsoft Research | 30,000+ | 2023 | Conversational | Message-passing | Async conversations | Medium |
| **CrewAI** | CrewAI Inc | 30,000+ | 2023 | Role-based | Tool delegation | Sequential/Hierarchical | Low |
| **LangGraph** | LangChain | 15,000+ | 2024 | Graph-based | Node routing | Stateful DAG | High |
| **Microsoft Agent Framework** | Microsoft | New | 2025 | Unified SDK | Multi-pattern | 4 orchestration modes | Medium |
| **PydanticAI** | Pydantic | Growing | 2024 | Type-safe | Schema-based | Structured validation | Low |
| **smolagents** | Hugging Face | Growing | 2024 | Minimalist | Code-centric | Flexible | Very Low |
| **Haystack** | deepset | 15,000+ | 2020 | Tool-driven | Modular | Pipeline-based | Medium |

---

## Detailed Framework Analysis

## Part I: Production SDKs

### 1. OpenAI Agents SDK

**Tagline**: Production-Ready Multi-Agent Framework with Provider Flexibility

**Release Date**: March 11, 2025 (successor to Swarm experimental framework)

#### Architecture & Philosophy
- **Core Philosophy**: Lightweight, Python-first framework with minimal abstractions for building multi-agent workflows
- **Design Principle**: Simplicity through primitives - Agents, Handoffs, Guardrails, and Sessions
- **Target Audience**: Developers building multi-agent systems for customer support, research, and enterprise workflows

#### Primary Components
- **Agents**: LLMs configured with instructions, tools, and behaviors
- **Handoffs**: Specialized tool calls for transferring control between agents
- **Guardrails**: Input/output validation and safety checks
- **Sessions**: Automatic conversation history management
- **Runners**: Execution orchestration (sync/async)
- **Tools**: Function decorators that turn Python functions into agent tools
- **Tracing**: Built-in execution visualization and debugging

#### Model & Provider Support
**Supported Models:**
- **OpenAI Models**: GPT-4o, GPT-4.1, GPT-4o-mini, o1, o3-mini
- **Other Providers via LiteLLM**: Anthropic Claude, Google Gemini, Mistral, DeepSeek, Groq, Ollama, and 100+ other models
- **vLLM Support**: ✅ Full compatibility with OpenAI-compatible endpoints

#### Built-in Capabilities
- Web Search via Responses API
- File Search for document retrieval and RAG
- Limited computer use capabilities
- Code execution via code interpreter
- Function tools with automatic schema generation
- MCP (Model Context Protocol) integration

#### Multi-Agent Orchestration
**Pattern**: Handoff-based delegation
- Deterministic flows with predefined agent chains
- Dynamic routing where LLM decides handoff targets
- Flat or simple two-level hierarchies
- No native parallel execution (requires custom implementation)

**Example Use Cases**:
- Triage agent → specialist agents (research, coding, analysis)
- Customer support routing to departments
- Multi-step workflows with clear handoff points

#### Strengths
✅ Simplest API and lowest learning curve
✅ Production-ready with built-in tracing
✅ Strong multi-agent handoff patterns
✅ Provider-agnostic (100+ models)
✅ Excellent documentation and examples
✅ Growing ecosystem and community
✅ Temporal integration for long-running workflows

#### Limitations
❌ Limited computer use capabilities
❌ Less sophisticated orchestration than ADK
❌ No native parallel agent execution
❌ Requires external solutions for complex state management

#### Best For
- Customer support automation with department routing
- Multi-agent research systems
- Content generation pipelines
- API-first applications
- Teams already using OpenAI models
- Teams wanting provider flexibility

#### Pricing
**SDK**: Free and open source

**Runtime Costs**:
- Model API costs (varies by provider)
- GPT-4o: $3/1M input, $12/1M output tokens
- Tool costs via Responses API (web search, file search)
- Infrastructure: Standard hosting ($50-$5,000+/month)

**Monthly Estimate**: $500-$2,000 (small), $2,000-$10,000 (medium), $10,000-$50,000+ (enterprise)

#### Code Example
```python
from agents import Agent, Runner

# Define agent with handoff capability
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o"
)

# Run synchronously
result = Runner.run_sync(agent, "Hello!")
print(result.final_output)
```

#### Installation
```bash
pip install openai-agents
```

#### Resources
- Documentation: https://openai.github.io/openai-agents-python/
- GitHub: https://github.com/openai/openai-agents-python
- Examples: https://github.com/openai/openai-agents-python/tree/main/examples

---

### 2. Claude Agent SDK

**Tagline**: Computer-Use Focused Framework Built on Claude Code Infrastructure

**Release Date**: September 2025 (renamed from Claude Code SDK)

#### Architecture & Philosophy
- **Core Philosophy**: Give agents access to a computer to work like humans do
- **Design Principle**: Agentic loop with computer access - gather context, take action, verify work, repeat
- **Key Strength**: Code generation and bash commands as primary execution methods
- **Target Audience**: Developers building agents that need deep file system access and developer-like workflows

#### Primary Components
- **Agent Harness**: Core execution engine from Claude Code
- **Tools**: Bash, file operations (Read, Write, Grep), code execution, web search, MCP servers
- **Hooks**: Custom code execution at specific agent lifecycle points
- **Subagents**: Specialized agents defined in Markdown files (`.claude/agents/`)
- **Memory**: CLAUDE.md for persistent project context
- **Permissions**: Fine-grained control over tool access
- **Context Management**: Automatic compaction and summarization

#### Model Support
**Supported Models:**
- **Anthropic Models Only**: Claude Sonnet 4.5, Claude Opus 4.1, Claude Haiku 4.5, Claude 3.x family
- **Via Third-Party APIs**:
  - Amazon Bedrock (set `CLAUDE_CODE_USE_BEDROCK=1`)
  - Google Vertex AI (set `CLAUDE_CODE_USE_VERTEX=1`)
- **vLLM Support**: ❌ No support (Claude-specific)

#### Built-in Capabilities
**Best-in-class computer use:**
- **Bash**: Full terminal/shell command execution
- **File Operations**: Read, Write, Edit, Grep, Find, Create files
- **Code Execution**: Python, JavaScript, and other languages
- **Web Search**: Integrated web search capabilities
- **Web Fetch**: Retrieve content from URLs
- **MCP Servers**: Connect to external tools and services
  - In-process MCP servers (no subprocess overhead)
  - SDK MCP server creation with `create_sdk_mcp_server()`

#### Multi-Agent Orchestration
**Pattern**: Subagent delegation with computer use
- Subagents defined in `.claude/agents/` as Markdown files
- Agent skills as reusable capabilities in `.claude/skills/`
- Sequential execution with main agent delegating to subagents
- Context sharing via file system and CLAUDE.md
- Primarily sequential delegation patterns

**Example Use Cases**:
- Main agent with security reviewer subagent
- Research agent with data extraction subagent
- Development agent with test execution subagent

#### Safety & Permissions
- **Permission Modes**: `manual`, `acceptEdits`, `acceptAll`
- **Allowed/Blocked Tools**: Fine-grained tool control
- **Hooks**: Custom validation at tool execution points
- **Bash Command Filtering**: Block dangerous patterns
- Working directory restrictions

#### Strengths
✅ Best-in-class computer use capabilities
✅ Native file system and terminal access
✅ Built on proven Claude Code infrastructure
✅ Excellent for code generation tasks
✅ Fine-grained permission control
✅ Automatic context management and compaction
✅ Strong IDE integrations (VS Code, JetBrains)
✅ Powerful bash-based automation

#### Limitations
❌ Claude models only (vendor lock-in)
❌ Requires Claude Code CLI installation
❌ Less structured orchestration patterns
❌ Limited multi-agent sophistication
❌ File system dependency for deployment

#### Best For
- Developer tools and coding assistants
- SRE and DevOps automation
- Cybersecurity agents
- Financial analysis requiring code execution
- Research agents with data processing
- Applications needing file manipulation

#### Pricing
**SDK**: Free and open source

**Runtime Costs**:
- Claude Sonnet 4.5: $3/1M input, $15/1M output tokens
- Claude Opus 4.1: $15/1M input, $75/1M output tokens
- Claude Haiku 4.5: $0.80/1M input, $4/1M output tokens
- Alternative: Claude Pro/Max subscription ($20-$200/month)
- Infrastructure with file system access ($100-$1,000+/month)

**Monthly Estimate**: $500-$2,500 (small), $2,500-$15,000 (medium), $15,000-$75,000+ (enterprise)

#### Code Example
```python
from claude_agent_sdk import query
import asyncio

async def main():
    async for message in query(
        prompt="Create a hello.py file"
    ):
        print(message)

asyncio.run(main())
```

#### Installation
```bash
pip install claude-agent-sdk
# Requires Claude Code CLI
```

#### Resources
- Documentation: https://docs.claude.com/en/api/agent-sdk/overview
- GitHub: https://github.com/anthropics/claude-agent-sdk-python
- Blog: https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk

---

### 3. Google ADK (Agent Development Kit)

**Tagline**: Model-Agnostic Framework Optimized for Gemini Ecosystem

**Release Date**: April 9, 2025 (launched at Google Cloud NEXT 2025)

#### Architecture & Philosophy
- **Core Philosophy**: Flexible, modular, and model-agnostic framework that makes agent development feel like software development
- **Design Principle**: Hierarchical multi-agent architecture with workflow orchestration
- **Key Feature**: Supports both LLM-driven reasoning agents and deterministic workflow agents
- **Target Audience**: Enterprise developers building scalable, production-grade multi-agent systems

#### Primary Components
- **Agents**: LlmAgent (reasoning), SequentialAgent, ParallelAgent, LoopAgent
- **Tools**: FunctionTool, AgentTool, built-in tools (search, code exec)
- **Runners**: Execution flow management with event handling
- **Sessions**: Context and state persistence via SessionService
- **Callbacks**: Custom code at specific execution points
- **Model Integration**: Direct (Gemini) or LiteLLM wrapper (others)
- **Workflows**: Deterministic orchestration patterns

#### Model & Provider Support
**Supported Models:**
- **Google Models**: Gemini 2.0 Flash, Gemini 2.5 Pro, Gemini family (native)
- **Vertex AI Models**: Claude, Llama, Mistral, AI21 Labs, and 200+ models via Model Garden
- **Via LiteLLM**: OpenAI, Anthropic, Mistral, Meta, Cohere, and others
- **Self-hosted**: Ollama, vLLM with OpenAI-compatible endpoints
- **vLLM Support**: ✅ Full compatibility via LiteLLM wrapper

#### Built-in Capabilities
- **Search**: Web search functionality
- **Code Execution**: Built-in code interpreter
- **FunctionTool**: Custom Python functions as tools
- **AgentTool**: Use other agents as tools (hierarchical composition)
- **MCP Integration**: Connect to MCP servers and tools
- **Third-party Libraries**: LangChain, LlamaIndex, CrewAI, LangGraph as tools
- Long-running tool support for async operations
- Bidirectional streaming for audio/video

#### Multi-Agent Orchestration
**Pattern**: Hierarchical multi-agent with workflow agents

**Capabilities:**
- **Workflow Agents**: SequentialAgent, ParallelAgent, LoopAgent
- **LLM-driven Transfer**: Dynamic routing based on model decisions
- **Agent Hierarchies**: Deep multi-level agent compositions
- **Parallel Execution**: Native ParallelAgent for concurrent tasks
- **Mixed Patterns**: Combine LLM and workflow agents

**Example Use Cases**:
- Parallel flight + hotel booking agents
- Sequential data fetch → process → analyze → report
- Hierarchical customer service with specialized departments
- Loop-based data processing workflows

#### Deployment Options
**Recommended**: Vertex AI Agent Engine Runtime (fully managed)
- Managed scaling, security, monitoring
- Built-in evaluation and quality metrics
- State and memory management
- Streaming support (text, audio, video)

**Other Options**: Local development, Docker, Kubernetes, Cloud Run, GKE

#### Strengths
✅ Most sophisticated multi-agent orchestration
✅ Native parallel and sequential workflows
✅ Model-agnostic with broad ecosystem
✅ Fully managed deployment via Agent Engine
✅ Battle-tested (powers Google products)
✅ Excellent interoperability with other frameworks
✅ Built-in evaluation and quality tools
✅ Multimodal streaming support
✅ Strong enterprise features

#### Limitations
❌ Steeper learning curve
❌ More complex architecture
❌ Best experience requires Google Cloud
❌ Java support newer than Python
❌ Larger framework with more abstraction

#### Best For
- Enterprise multi-agent systems
- Google Cloud native applications
- Hierarchical agent architectures
- Production systems requiring managed infrastructure
- Multimodal applications (audio, video streaming)
- Framework-agnostic development
- Applications using other frameworks as tools

#### Pricing
**SDK**: Free and open source

**Runtime Costs**:
- Gemini 2.0 Flash: Competitive pricing
- Gemini 2.5 Pro: Higher tier pricing
- Vertex AI Agent Engine (optional): vCPU, memory, storage costs
- Self-hosted: Standard infrastructure costs

**Monthly Estimate**: $300-$1,500 (small), $1,500-$8,000 (medium), $8,000-$40,000+ (enterprise)

**Note**: Google generally 10-20X less expensive than AWS/Azure for AI workloads

#### Code Example
```python
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

# Define agent
agent = Agent(
    name="assistant",
    model="gemini-2.0-flash",
    instruction="You are a helpful assistant"
)

# Run with session management
session_service = InMemorySessionService()
runner = Runner(session_service=session_service)

result = runner.run(
    agent=agent,
    user_message="What are three interesting facts about space?"
)

print(result.response)
```

#### Installation
```bash
pip install google-adk
```

#### Resources
- Documentation: https://google.github.io/adk-docs/
- GitHub: https://github.com/google/adk
- Vertex AI: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-development-kit/overview
- Blog: https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/

---

## Part II: Open-Source Frameworks

### 4. AG2 (AutoGen)

**Tagline**: The Open-Source Operating System for Agentic AI

#### Architecture
- **Communication**: Conversational message-passing with async support
- **Message Format**: Dictionary-based OpenAI format
  ```python
  {"content": "message content", "role": "system|user|assistant"}
  ```
- **Storage**: `_oai_messages` (defaultdict of lists)

#### Key Features
- **ConversableAgent**: Base class for all agents
- **Group Chat**: Multiple agents in collaborative discussions
- **A2A Protocol Support**: Cross-framework communication via `A2aAgentServer` and `A2aRemoteAgent`
- **Human-in-the-loop**: Native human-AI collaboration

#### Communication Methods
- `run()`: Returns iterator with events, messages, metadata
- `process()`: Helper for chat-like console experience
- Direct agent-to-agent message passing

#### Strengths
✅ Intuitive conversational approach
✅ Flexible async agent interactions
✅ Strong for dynamic role-switching
✅ Built-in conversation patterns
✅ A2A protocol compatible

#### Limitations
❌ Requires understanding of async patterns
❌ Can become complex with many agents
❌ Less structured than role-based frameworks

#### Best For
- Customer service chatbots
- Brainstorming and ideation
- Dynamic multi-turn dialogues
- Real-time collaborative tasks

#### Code Example
```python
from autogen import ConversableAgent

agent1 = ConversableAgent(
    name="researcher",
    system_message="You are a research assistant"
)

agent2 = ConversableAgent(
    name="writer",
    system_message="You are a content writer"
)

# Agents communicate via message passing
agent1.initiate_chat(agent2, message="Research the latest AI trends")
```

---

### 5. CrewAI

**Tagline**: Framework for Orchestrating Role-Playing, Autonomous AI Agents

#### Architecture
- **Communication**: Tool-based delegation
- **Orchestration**: Role-based team coordination
- **Processes**: Sequential (default) or Hierarchical

#### Core Communication Tools

When `allow_delegation=True`, agents gain access to:

1. **Delegate Work Tool**
   ```
   Delegate work to coworker(task: str, context: str, coworker: str)
   ```

2. **Ask Question Tool**
   ```
   Ask question to coworker(question: str, context: str, coworker: str)
   ```

#### Message Structure
- **task/question**: Primary content
- **context**: Background information
- **coworker**: Target agent identifier

#### Process Models

**Sequential Process**
- Tasks execute in predefined order
- Output of one task → context for next
- All agents can delegate if enabled

**Hierarchical Process**
- Manager agent coordinates workflow
- Dynamic task allocation based on capabilities
- Manager: `allow_delegation=True`
- Specialists: `allow_delegation=False` (prevents loops)

#### Strengths
✅ Intuitive role-based design
✅ Excellent for team-oriented tasks
✅ Built-in memory modules
✅ Well-documented and beginner-friendly
✅ Growing community (30,000+ stars)

#### Limitations
❌ Linear/loop-based flows (no DAG)
❌ No built-in execution graph
❌ Agents self-organize (less control)
❌ Limited complex workflow support

#### Best For
- Content creation workflows (research → write → edit)
- Customer support teams
- Data analysis pipelines
- Sequential business processes

#### Code Example
```python
from crewai import Agent, Task, Crew, Process

researcher = Agent(
    role='Researcher',
    goal='Find relevant information',
    allow_delegation=True,
    backstory='Expert at finding information'
)

writer = Agent(
    role='Writer',
    goal='Create compelling content',
    allow_delegation=True,
    backstory='Skilled content creator'
)

task1 = Task(
    description='Research AI trends',
    agent=researcher
)

task2 = Task(
    description='Write article based on research',
    agent=writer
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    process=Process.sequential
)

result = crew.kickoff()
```

---

### 6. LangGraph

**Tagline**: Build Stateful, Multi-Actor Applications with LLMs

#### Architecture
- **Communication**: Graph-based routing
- **Structure**: Directed graph with nodes and edges
- **State**: Each agent/node maintains own state
- **Flow**: Supports cycles, conditionals, parallel execution

#### Key Concepts

**Nodes**: Represent agents or operations
**Edges**: Define transitions between nodes
**State**: Shared context across graph
**Conditionals**: Dynamic routing logic

#### Graph Components
```python
# Node types
- Agent nodes (LLM-powered)
- Tool nodes (function execution)
- Supervisor nodes (orchestration)
- Human nodes (human-in-the-loop)

# Edge types
- Direct edges (A → B)
- Conditional edges (if/else routing)
- Parallel edges (fork/join)
```

#### Strengths
✅ Precise control over workflow
✅ Complex state management
✅ DAG-based execution
✅ Iterative and cyclical flows
✅ Multi-team coordination
✅ Hierarchical supervision

#### Limitations
❌ Steepest learning curve
❌ Requires upfront planning
❌ More code for simple tasks
❌ Complex debugging

#### Best For
- Complex multi-step workflows
- Scenarios requiring branching logic
- Error handling and retry mechanisms
- Long-running stateful processes
- Multi-team coordination

#### Code Example
```python
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage

# Define state
class AgentState(TypedDict):
    messages: list[HumanMessage]
    next_agent: str

# Create graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("researcher", research_agent)
workflow.add_node("writer", writing_agent)
workflow.add_node("editor", editing_agent)

# Add edges with conditional routing
workflow.add_conditional_edges(
    "researcher",
    lambda state: state["next_agent"],
    {
        "writer": "writer",
        "end": END
    }
)

workflow.set_entry_point("researcher")
app = workflow.compile()
```

---

### 7. Microsoft Agent Framework

**Tagline**: Enterprise-Ready Multi-Agent Orchestration

#### Architecture
- **Unified SDK**: Combines Semantic Kernel + AutoGen
- **Production-Ready**: Enterprise foundations
- **Multi-Pattern**: Flexible orchestration

#### Orchestration Patterns

1. **Sequential Orchestration**
   - Step-by-step workflows
   - Predictable execution order
   - Output chaining

2. **Concurrent Orchestration**
   - Parallel agent execution
   - Performance optimization
   - Independent task handling

3. **Group Chat Orchestration**
   - Collaborative brainstorming
   - Multi-agent discussions
   - Consensus building

4. **Handoff Orchestration**
   - Context-aware transitions
   - Responsibility transfer
   - Dynamic routing

#### Integration Standards
- **OpenAPI**: Any REST API integration
- **A2A**: Cross-runtime agent collaboration
- **MCP**: Dynamic tool connections

#### Strengths
✅ Enterprise-grade reliability
✅ Multiple orchestration patterns
✅ Comprehensive integration support
✅ Production deployment focus
✅ Microsoft ecosystem integration

#### Limitations
❌ Newer framework (less community)
❌ May have vendor lock-in concerns
❌ Documentation still evolving

#### Best For
- Enterprise multi-agent systems
- Production-grade applications
- Complex orchestration needs
- Microsoft Azure deployments

---

### 8. PydanticAI

**Tagline**: Type-Safe AI Agent Framework

#### Architecture
- **Type-Safe**: Pydantic validation
- **Structured**: Schema-first design
- **Dependency Injection**: Clean state management

#### Key Features

**Dataclass-Based State**
```python
from pydantic import BaseModel

class AgentState(BaseModel):
    user_id: int
    context: str
    history: list[str]
```

**Type Checking**
- Compile-time validation
- Runtime type checking
- Schema enforcement

**Tool Contracts**
- Typed input parameters
- Validated outputs
- Clear interfaces

**A2A Compatible**
- Can expose as A2A server
- Interoperable with other frameworks

#### Strengths
✅ Type safety
✅ Easy prototyping
✅ Clear contracts
✅ Validation-first
✅ Great for structured I/O

#### Limitations
❌ Less flexible for unstructured tasks
❌ Smaller ecosystem
❌ Newer framework

#### Best For
- API-driven agents
- Structured data processing
- Type-safe production systems
- Teams valuing correctness

#### Code Example
```python
from pydantic_ai import Agent
from pydantic import BaseModel

class ResearchContext(BaseModel):
    topic: str
    depth: int
    sources: list[str]

agent = Agent(
    'openai:gpt-4',
    deps_type=ResearchContext,
    result_type=str
)

@agent.tool
def search_papers(ctx: ResearchContext, query: str) -> list[str]:
    # Type-safe tool with validated inputs
    return ["paper1", "paper2"]

result = agent.run_sync(
    'Research AI trends',
    deps=ResearchContext(topic="AI", depth=5, sources=[])
)
```

---

### 9. OpenAI Swarm (Deprecated - See OpenAI Agents SDK)

**Status**: ⚠️ Experimental framework deprecated in favor of OpenAI Agents SDK (March 2025)

**Tagline**: Lightweight Multi-Agent Orchestration (Superseded by OpenAI Agents SDK)

#### Note
OpenAI Swarm was an experimental framework that has been succeeded by the production-ready **OpenAI Agents SDK** (see Section 1). The Agents SDK provides all of Swarm's capabilities plus:
- Production-ready features
- Built-in tracing and evaluation
- Better error handling
- Comprehensive documentation
- Active development and support

#### Legacy Architecture
- **Minimalist**: Focus on essentials
- **Handoff-Based**: Simple agent transitions
- **Rapid Prototyping**: Quick setup

#### Migration Path
Users should migrate to **OpenAI Agents SDK** for production use. The Agents SDK maintains similar handoff patterns while adding production-grade features.

---

### 10. smolagents

**Tagline**: Ultra-Minimal AI Agent Tools

#### Architecture
- **Minimalist**: Bare essentials only
- **Code-Centric**: Python-first approach
- **LLM-Agnostic**: Works with any model

#### Key Features
- Ultra-lightweight
- Easy to read and extend
- Fast execution
- Modular design

#### Strengths
✅ Minimal overhead
✅ Maximum flexibility
✅ Easy to understand
✅ Fast execution
✅ Any LLM support

#### Limitations
❌ Manual orchestration
❌ No built-in patterns
❌ DIY everything

#### Best For
- Single-agent tasks
- Small multi-agent systems
- Code-centric workflows
- Learning fundamentals

---

### 11. Haystack Agents

**Tagline**: Tool-Driven NLP Agent Framework

#### Architecture
- **Tool-Driven**: Modular tools for specific tasks
- **NLP-Focused**: Document search, QA, summarization
- **Pipeline-Based**: Component chaining

#### Key Features
- Document search tools
- Calculation engines
- API interaction modules
- Multi-step reasoning

#### Strengths
✅ Powerful for NLP
✅ Flexible tool integration
✅ Multi-step reasoning
✅ Mature framework

#### Limitations
❌ More NLP-specific
❌ Less general-purpose
❌ Learning curve for pipelines

#### Best For
- NLP applications
- Document processing
- Question answering systems
- Search and retrieval

---

## Communication Protocols

### Agent-to-Agent Protocols

#### 1. A2A (Agent2Agent Protocol)

**Overview**: Standardized protocol for distributed agent communication (introduced by Google, April 2025)

**Message Structure**:
```
{
  "header": {
    "protocol_version": "1.0",
    "message_id": "uuid",
    "timestamp": "ISO 8601",
    "type": "REQUEST|RESPONSE|EVENT|HEARTBEAT"
  },
  "sender": {
    "agent_id": "string",
    "endpoint": "url",
    "auth": "credentials"
  },
  "recipient": {
    "agent_id": "string",
    "endpoint": "url"
  },
  "payload": {
    "content_type": "application/json",
    "encoding": "utf-8|base64",
    "compression": "gzip|none",
    "data": {...}
  },
  "metadata": {
    "conversation_id": "uuid",
    "routing": {...},
    "qos": {...}
  },
  "security": {
    "signature": "digital_signature"
  }
}
```

**Content Types**:
- **TextPart**: Plain text
- **FilePart**: File representations
- **DataPart**: Structured JSON

**Communication Lifecycle**:
1. **Discovery**: Registry lookup
2. **Handshake**: Secure connection
3. **Negotiation**: Parameter agreement
4. **Execution**: Task processing
5. **Delivery**: Results + session closure

**Supported By**: AG2, Google ADK, Microsoft Agent Framework, PydanticAI

**Use Case**: Distributed agents across processes, machines, or frameworks

---

#### 2. ACP (Agent Communication Protocol)

**Overview**: RESTful API standard for agent interoperability (AGNTCY Initiative, 2025)

**Features**:
- Framework-agnostic
- RESTful architecture
- Standardized endpoints
- Technology-independent

**Supported By**: CrewAI, LangChain, smolagents, others

**Use Case**: Cross-framework agent communication via REST APIs

---

#### 3. AG-UI Protocol (Agent User Interaction)

**Overview**: Event-based protocol for frontend-agent interaction (CopilotKit)

**Features**:
- Event-driven communication
- Real-time interactions
- State management
- Streaming responses
- Tool usage tracking

**Supported By**: CrewAI, other frameworks via CopilotKit

**Use Case**: Rich UI interactions with AI agents

---

### Agent-to-Service Protocols

#### MCP (Model Context Protocol)

**Overview**: Protocol for agent-to-external-service communication (Anthropic)

**Features**:
- Access external data sources
- API integrations
- Database connections
- File system access
- IDE integrations

**Supported By**: Microsoft Agent Framework, Google ADK, various frameworks

**Use Case**: Agents accessing external tools and services

---

### Interoperability Standards

#### OASF (Open Agentic Schema Framework)

**Launched**: Early 2025

**Features**:
- Standardized capability schemas
- Agent attribute definitions
- Relationship descriptions
- Schema validation tools
- Interoperability foundation

**Purpose**: Enable cross-framework agent discovery and interaction

---

## Orchestration Patterns

### 1. Sequential Orchestration

**Pattern**: Tasks execute one after another in predefined order

**Flow**:
```
Agent A → Agent B → Agent C → Result
```

**Frameworks**: CrewAI, Microsoft Agent Framework, Google ADK

**Best For**:
- Linear workflows
- Clear dependencies
- Predictable processes

**Example Use Cases**:
- Research → Write → Edit
- Data Collection → Analysis → Reporting
- Design → Develop → Test

---

### 2. Parallel Orchestration

**Pattern**: Multiple agents execute simultaneously

**Flow**:
```
        ┌→ Agent A →┐
Start → ┼→ Agent B →┼→ Combine → Result
        └→ Agent C →┘
```

**Frameworks**: Microsoft Agent Framework, Google ADK, LangGraph

**Best For**:
- Independent tasks
- Performance optimization
- Embarrassingly parallel work

**Example Use Cases**:
- Multi-source data gathering
- Parallel analysis
- A/B testing

---

### 3. Hierarchical Orchestration

**Pattern**: Manager agent coordinates specialist agents

**Flow**:
```
      Manager Agent
     /      |      \
Agent A  Agent B  Agent C
```

**Frameworks**: CrewAI (hierarchical mode), LangGraph (supervisor)

**Best For**:
- Complex delegation
- Dynamic task allocation
- Quality control

**Example Use Cases**:
- Team coordination
- Multi-stage validation
- Dynamic resource allocation

---

### 4. Graph-Based Orchestration

**Pattern**: Agents connected in directed graph with conditional routing

**Flow**:
```
Start → Agent A → [condition]
                    ├→ Agent B → Agent D → End
                    └→ Agent C ─┘
```

**Frameworks**: LangGraph, Google ADK

**Best For**:
- Complex branching logic
- Conditional workflows
- Iterative processes

**Example Use Cases**:
- Error handling with retries
- Multi-path decision trees
- Adaptive workflows

---

### 5. Conversational Orchestration

**Pattern**: Agents communicate through async message passing

**Flow**:
```
Agent A ⇄ Agent B
   ⇅         ⇅
Agent C ⇄ Agent D
```

**Frameworks**: AG2 (AutoGen), Microsoft Agent Framework (group chat)

**Best For**:
- Dynamic interactions
- Collaborative discussions
- Emergent behavior

**Example Use Cases**:
- Brainstorming sessions
- Consensus building
- Multi-perspective analysis

---

### 6. Handoff Orchestration

**Pattern**: Sequential agent activation with context passing

**Flow**:
```
Agent A → [handoff + context] → Agent B → [handoff + context] → Agent C
```

**Frameworks**: Microsoft Agent Framework, OpenAI Swarm

**Best For**:
- Context preservation
- Smooth transitions
- Specialized expertise chains

**Example Use Cases**:
- Customer service escalation
- Multi-stage approvals
- Specialized processing pipelines

---

## Use Case Recommendations

### By Task Type

#### Developer Tools & Coding Assistants
**Recommended**: Claude Agent SDK, OpenAI Agents SDK
- **Claude Agent SDK**: Best-in-class computer use, file system access, code generation
- **OpenAI Agents SDK**: Multi-provider flexibility with code interpreter

#### Content Creation
**Recommended**: CrewAI, AG2, OpenAI Agents SDK
- **CrewAI**: Research → Write → Edit workflow
- **AG2**: Collaborative content generation
- **OpenAI Agents SDK**: Production-ready with handoffs

#### Customer Support
**Recommended**: OpenAI Agents SDK, AG2, CrewAI, Microsoft Agent Framework
- **OpenAI Agents SDK**: Production-ready handoff patterns for routing
- **AG2**: Dynamic conversational support
- **CrewAI**: Tiered support teams
- **MS Agent Framework**: Enterprise handoff orchestration

#### Data Analysis & Processing
**Recommended**: LangGraph, Google ADK, CrewAI, Claude Agent SDK
- **LangGraph**: Complex analysis pipelines
- **Google ADK**: Parallel data processing
- **CrewAI**: Sequential analysis workflow
- **Claude Agent SDK**: Code-heavy data processing with file access

#### Research & Information Gathering
**Recommended**: AG2, OpenAI Agents SDK, Haystack, CrewAI
- **OpenAI Agents SDK**: Production web search and file search
- **AG2**: Collaborative research
- **Haystack**: Document search and QA
- **CrewAI**: Research → Synthesis workflow

#### Complex Decision Making
**Recommended**: LangGraph, Google ADK, Microsoft Agent Framework
- **LangGraph**: Conditional decision trees
- **Google ADK**: Hierarchical multi-agent decisions
- **MS Agent Framework**: Multi-pattern evaluation

#### DevOps & Automation
**Recommended**: Claude Agent SDK
- **Claude Agent SDK**: Terminal access, bash automation, file operations

#### Rapid Prototyping
**Recommended**: OpenAI Agents SDK, smolagents, PydanticAI
- **OpenAI Agents SDK**: Simple API, quick setup
- **smolagents**: Minimal overhead
- **PydanticAI**: Type-safe prototypes

---

### By Team Experience

#### Beginners
1. **OpenAI Agents SDK** - Simplest production SDK, low learning curve
2. **CrewAI** - Intuitive role-based model
3. **PydanticAI** - Clear structure with type safety

#### Intermediate
1. **Claude Agent SDK** - Computer use with moderate complexity
2. **Google ADK** - Workflow-based orchestration
3. **AG2 (AutoGen)** - Conversational patterns
4. **Microsoft Agent Framework** - Multiple patterns

#### Advanced
1. **LangGraph** - Complex state management
2. **Google ADK** - Deep hierarchical architectures
3. **Custom combinations** - Mix frameworks and SDKs
4. **Protocol-level integration** - A2A, MCP

---

### By Deployment Context

#### Cloud-Native (Managed Services)
- **Google ADK** (Vertex AI Agent Engine - fully managed)
- **Microsoft Agent Framework** (Azure)
- **OpenAI Agents SDK** (OpenAI Platform)

#### Cloud-Deployed (Self-Managed)
- **OpenAI Agents SDK** (any cloud - most flexible)
- **Claude Agent SDK** (requires file system access)
- **Google ADK** (containerized deployment)
- **AG2** (self-hosted)
- **CrewAI** (self-hosted)

#### On-Premise
- **OpenAI Agents SDK** (with vLLM or local models)
- **Google ADK** (with vLLM support)
- **AG2** (self-hosted)
- **CrewAI** (self-hosted)
- **smolagents** (minimal dependencies)

#### Edge/Embedded
- **smolagents** (lightweight)
- **Custom minimal implementations**

#### Multi-Cloud & Provider-Agnostic
- **OpenAI Agents SDK** (100+ models via LiteLLM)
- **Google ADK** (multi-provider via LiteLLM)
- **PydanticAI** (portable)
- **LangGraph** (framework-agnostic)
- **Frameworks with A2A support**

---

## Getting Started Guide

### Quick Start Matrix

| If You Want... | Start With... | Why? |
|----------------|---------------|------|
| **Production-ready SDK** | **OpenAI Agents SDK** | Simplest API, built-in tracing, 100+ models |
| **Computer use & coding** | **Claude Agent SDK** | Best file/terminal access, code generation |
| **Enterprise scale** | **Google ADK** | Managed deployment, sophisticated orchestration |
| **Role-based teams** | **CrewAI** | Intuitive, well-documented |
| **Conversations** | **AG2** | Natural dialogue patterns |
| **Type safety** | **PydanticAI** | Validation built-in |
| **Maximum control** | **LangGraph** | Precise workflow management |
| **Multi-pattern** | **Microsoft Agent Framework** | 4 orchestration modes |
| **Minimal code** | **smolagents** | Bare essentials |

---

### Installation Commands

```bash
# Production SDKs
pip install openai-agents        # OpenAI Agents SDK
pip install claude-agent-sdk     # Claude Agent SDK (requires Claude Code CLI)
pip install google-adk           # Google ADK

# Open-Source Frameworks
pip install ag2                  # AG2 (AutoGen)
pip install crewai crewai-tools  # CrewAI
pip install langgraph            # LangGraph
pip install microsoft-agent-framework  # Microsoft Agent Framework
pip install pydantic-ai          # PydanticAI
pip install smolagents           # smolagents
pip install haystack-ai          # Haystack
```

---

### Hello World Examples

#### AG2 (AutoGen)
```python
from autogen import ConversableAgent

agent = ConversableAgent(
    name="assistant",
    system_message="You are a helpful assistant",
    llm_config={"model": "gpt-4"}
)

response = agent.generate_reply(
    messages=[{"content": "Hello!", "role": "user"}]
)
print(response)
```

#### CrewAI
```python
from crewai import Agent, Task, Crew

agent = Agent(
    role='Assistant',
    goal='Help users',
    backstory='Helpful AI assistant'
)

task = Task(
    description='Say hello',
    agent=agent
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
print(result)
```

#### LangGraph
```python
from langgraph.graph import StateGraph, END

def agent_node(state):
    return {"messages": ["Hello World!"]}

workflow = StateGraph(dict)
workflow.add_node("agent", agent_node)
workflow.set_entry_point("agent")
workflow.add_edge("agent", END)

app = workflow.compile()
result = app.invoke({"messages": []})
print(result)
```

#### PydanticAI
```python
from pydantic_ai import Agent

agent = Agent('openai:gpt-4')

result = agent.run_sync('Hello!')
print(result.data)
```

---

## Key Takeaways

### Production SDKs

### Choose OpenAI Agents SDK If:
- ✅ Want simplest API and fastest time-to-production
- ✅ Need provider flexibility (100+ models via LiteLLM)
- ✅ Building customer support, research, or content generation
- ✅ Value built-in tracing and evaluation
- ✅ Want handoff-based multi-agent patterns
- ✅ Need strong observability from day one

### Choose Claude Agent SDK If:
- ✅ Building developer tools or coding assistants
- ✅ Need deep file system and terminal access
- ✅ Require extensive code generation capabilities
- ✅ Building DevOps/SRE automation
- ✅ Want proven infrastructure (Claude Code)
- ✅ Okay with Claude-only models
- ✅ Need powerful bash-based automation

### Choose Google ADK If:
- ✅ Need sophisticated multi-agent orchestration
- ✅ Want parallel AND sequential workflow patterns
- ✅ Building on Google Cloud infrastructure
- ✅ Need fully managed deployment (Agent Engine)
- ✅ Want model-agnostic flexibility
- ✅ Require enterprise-grade features and support
- ✅ Need multimodal streaming (audio, video)

---

### Open-Source Frameworks

### Choose AG2 If:
- You need conversational multi-agent systems
- Async communication is important
- Dynamic role-switching required
- Building chatbots or collaborative tools

### Choose CrewAI If:
- You have clear role-based workflows
- Team coordination metaphor fits
- Sequential or simple hierarchical processes
- You're new to multi-agent systems

### Choose LangGraph If:
- Complex workflows with branching logic
- Precise state management crucial
- Iterative processes with cycles
- You need maximum control

### Choose Microsoft Agent Framework If:
- Building enterprise applications
- Need multiple orchestration patterns (4 modes)
- Azure integration desired
- Production-grade requirements

### Choose PydanticAI If:
- Type safety is critical
- Structured I/O required
- API-driven agents
- Validation-first approach

### Choose smolagents If:
- Minimal overhead desired
- Maximum flexibility needed
- Code-centric approach
- Single or small multi-agent systems

---

## Resources

### Production SDK Documentation
- [OpenAI Agents SDK Docs](https://openai.github.io/openai-agents-python/)
- [OpenAI Agents SDK GitHub](https://github.com/openai/openai-agents-python)
- [Claude Agent SDK Docs](https://docs.claude.com/en/api/agent-sdk/overview)
- [Claude Agent SDK GitHub](https://github.com/anthropics/claude-agent-sdk-python)
- [Google ADK Docs](https://google.github.io/adk-docs/)
- [Google ADK GitHub](https://github.com/google/adk)
- [Google Vertex AI Agent Development Kit](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-development-kit/overview)

### Open-Source Framework Documentation
- [AG2 Docs](https://docs.ag2.ai/)
- [CrewAI Docs](https://docs.crewai.com/)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [Microsoft Agent Framework Docs](https://azure.microsoft.com/en-us/blog/introducing-microsoft-agent-framework/)
- [PydanticAI Docs](https://ai.pydantic.dev/)
- [Haystack Docs](https://haystack.deepset.ai/)

### Protocol Specifications
- [A2A Protocol Spec](https://a2agent.net/protocol-spec)
- [MCP Specification](https://modelcontextprotocol.io/)
- [OASF Framework](https://oasf.dev/)

### Community
- GitHub repositories for each framework
- Discord servers for CrewAI, LangChain, AG2
- Stack Overflow tags
- Reddit communities (r/LangChain, r/AI_Agents)

---

## Conclusion

The multi-agent AI landscape in 2025 has matured significantly with both **production SDKs** from major AI vendors and **robust open-source frameworks**:

### Production SDKs (Vendor-Supported)
- **OpenAI Agents SDK**: Best for speed-to-market, provider flexibility, and simple multi-agent patterns
- **Claude Agent SDK**: Unmatched for computer use, file operations, and code-heavy workflows
- **Google ADK**: Most sophisticated orchestration, enterprise scale, managed infrastructure

### Open-Source Frameworks
- **Beginners** should start with OpenAI Agents SDK or CrewAI
- **Conversational systems** benefit from AG2 or OpenAI Agents SDK
- **Complex workflows** need LangGraph or Google ADK
- **Enterprise deployments** fit Google ADK or Microsoft Agent Framework
- **Type-safe systems** use PydanticAI
- **Developer tools** leverage Claude Agent SDK
- **Rapid experiments** use OpenAI Agents SDK or smolagents

### Key Trends in 2025
1. **Production-Ready SDKs**: Major AI vendors now offer production-grade agent frameworks
2. **Standardized Protocols**: A2A, MCP, ACP, OASF enable cross-framework communication
3. **Computer Use**: Claude leads in giving agents true system-level access
4. **Model Flexibility**: OpenAI and Google support 100+ models via LiteLLM
5. **Managed Deployment**: Google's Vertex AI Agent Engine offers fully managed infrastructure
6. **Interoperability**: Agents can now communicate across frameworks and providers

The emergence of standardized protocols means the choice is less about lock-in and more about:
- **Use case fit**: Developer tools vs customer support vs enterprise orchestration
- **Developer experience**: Simple APIs vs maximum control
- **Deployment preferences**: Managed services vs self-hosted
- **Model preferences**: Single vendor vs multi-provider flexibility

---

*Last Updated: October 31, 2025*
*This comprehensive comparison reflects the state of multi-agent frameworks and SDKs as of October 2025, including the latest production SDKs from OpenAI, Anthropic, and Google.*
