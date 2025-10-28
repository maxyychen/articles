# Agent, Tools, and MCP: Complete Data Flow Guide

A comprehensive explanation of how AI agents interact with tools through the Model Context Protocol (MCP), including detailed architecture, data flow, and message formats.

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Core Components](#core-components)
3. [MCP Protocol Deep Dive](#mcp-protocol-deep-dive)
4. [Complete Data Flow](#complete-data-flow)
5. [Message Format Examples](#message-format-examples)
6. [Tool Execution Lifecycle](#tool-execution-lifecycle)
7. [Multi-Tool Orchestration](#multi-tool-orchestration)

---

## Architecture Overview

### High-Level Component Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                          USER                                   │
│                      (Human User)                               │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ 1. User Input: "Show me all users"
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                     HOST APPLICATION                            │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                    AI AGENT                               │  │
│  │  • Manages conversation context                          │  │
│  │  • Coordinates LLM + Tools                               │  │
│  │  • Orchestrates multi-step workflows                     │  │
│  │                                                           │  │
│  │  Components:                                              │  │
│  │  - Conversation history (messages[])                      │  │
│  │  - Tool registry (available tools)                        │  │
│  │  - Execution loop (agentic reasoning)                     │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Examples: Claude Desktop, Cursor IDE, Custom chatbot          │
└─────────────────────────────────────────────────────────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ↓              ↓              ↓
    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
    │ MCP Client  │  │ MCP Client  │  │ MCP Client  │
    │     #1      │  │     #2      │  │     #3      │
    └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
           │                │                │
           │ JSON-RPC 2.0   │ JSON-RPC 2.0   │ JSON-RPC 2.0
           │ over           │ over           │ over
           │ STDIO/HTTP     │ STDIO/HTTP     │ STDIO/HTTP
           │                │                │
           ↓                ↓                ↓
    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
    │ MCP Server  │  │ MCP Server  │  │ MCP Server  │
    │ (Database)  │  │ (Filesystem)│  │  (Search)   │
    └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
           │                │                │
           ↓                ↓                ↓
    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
    │  External   │  │  External   │  │  External   │
    │  Resources  │  │  Resources  │  │  Resources  │
    │             │  │             │  │             │
    │ • Database  │  │ • Files     │  │ • Web APIs  │
    │ • APIs      │  │ • Docs      │  │ • Services  │
    └─────────────┘  └─────────────┘  └─────────────┘
```

### Key Relationships

1. **User ↔ Host Application**: Human interaction interface
2. **Host ↔ Agent**: Application contains agent logic
3. **Agent ↔ LLM**: Agent sends prompts, receives responses
4. **Agent ↔ MCP Client**: Agent requests tool execution
5. **MCP Client ↔ MCP Server**: Protocol-based communication (1:1 relationship)
6. **MCP Server ↔ External Resources**: Actual tool implementation

---

## Core Components

### 1. Host Application

**Definition**: The application the user directly interacts with.

**Examples**:
- Claude Desktop
- Cursor IDE
- VS Code with Claude extension
- Custom chatbot application

**Responsibilities**:
- Provide user interface
- Manage application lifecycle
- Host the AI agent
- Coordinate multiple MCP clients

---

### 2. AI Agent

**Definition**: The intelligent orchestrator that manages conversation context and coordinates between the LLM and tools.

**Core Functions**:

#### a) Conversation Management
```python
messages = [
    {"role": "system", "content": "You are a helpful assistant..."},
    {"role": "user", "content": "Show me all users"},
    {"role": "assistant", "content": "", "tool_calls": [...]},
    {"role": "tool", "content": "Tool result: [...]"},
    {"role": "assistant", "content": "I found 2 users..."}
]
```

#### b) Tool Registry
- Maintains list of available tools from all connected MCP servers
- Formats tool schemas for LLM consumption
- Maps tool names to MCP client instances

#### c) Execution Loop (Agentic Reasoning)
```
User Input
    ↓
Agent receives request
    ↓
Agent sends to LLM with tools
    ↓
LLM decides: Text response OR Tool call?
    ↓
If Tool call:
    - Agent extracts tool_calls
    - Agent routes to appropriate MCP client
    - MCP client executes via MCP server
    - Agent receives result
    - Agent appends to conversation
    - Loop back to LLM (max iterations)
    ↓
Final response to user
```

**Key Properties**:
- Stateful (maintains conversation history)
- Multi-modal (can handle text, tool calls, errors)
- Iterative (supports multi-step reasoning)

---

### 3. MCP Client

**Definition**: The connector component that implements the MCP protocol to communicate with MCP servers.

**Location**: Lives inside the Host application

**Relationship**: **1:1 with MCP Server** (each client connects to exactly one server)

**Communication Protocol**: JSON-RPC 2.0

**Transport Mechanisms**:
1. **STDIO** (Standard Input/Output)
   - For local integrations
   - Server runs as subprocess
   - Messages via stdin/stdout

2. **HTTP + SSE** (Server-Sent Events)
   - For remote connections
   - HTTP for client requests
   - SSE for server responses/streaming

**Responsibilities**:

#### a) Tool Discovery
```json
// Client → Server
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}

// Server → Client
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "execute_query",
        "description": "Execute SQL query on database",
        "inputSchema": {
          "type": "object",
          "properties": {
            "query": {
              "type": "string",
              "description": "SQL query to execute"
            }
          },
          "required": ["query"]
        }
      }
    ]
  }
}
```

#### b) Tool Execution
```json
// Client → Server
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "execute_query",
    "arguments": {
      "query": "SELECT * FROM users"
    }
  }
}

// Server → Client
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "[{\"id\": 1, \"name\": \"Alice\"}, {\"id\": 2, \"name\": \"Bob\"}]"
      }
    ]
  }
}
```

#### c) Tool Schema Translation
- Converts MCP tool schemas to LLM-compatible format (e.g., OpenAI function calling)
- Translates LLM tool calls back to MCP format
- Handles type conversions and validations

---

### 4. MCP Server

**Definition**: External program that exposes tools, resources, and prompts via the MCP protocol.

**Types of Capabilities**:

1. **Tools** - Functions the AI can execute
   ```
   Examples: execute_query, search_web, create_file
   ```

2. **Resources** - Context and data accessible to AI
   ```
   Examples: file://documents/report.pdf, db://users/table
   ```

3. **Prompts** - Templated messages and workflows
   ```
   Examples: code_review_prompt, data_analysis_template
   ```

**Implementation**:
- Standalone service (can be in any language)
- Implements MCP protocol (JSON-RPC 2.0)
- Manages actual business logic
- Interacts with external resources (databases, APIs, filesystems)

**Lifecycle**:
1. **Initialization**: Server starts and registers capabilities
2. **Connection**: Client connects and negotiates capabilities
3. **Discovery**: Client requests tool/resource/prompt listings
4. **Execution**: Client invokes tools, server executes and returns results
5. **Shutdown**: Graceful connection termination

---

### 5. Large Language Model (LLM)

**Definition**: The intelligence layer that understands user intent and decides when to use tools.

**Role in Data Flow**:
- Receives: User messages + conversation history + tool schemas
- Analyzes: User intent and available capabilities
- Decides: Generate text response OR make tool call(s)
- Generates: Natural language or structured tool calls
- Processes: Tool results to generate final response

**Key Capabilities**:
- Natural language understanding
- Tool selection reasoning
- Multi-step planning
- Result synthesis

---

## MCP Protocol Deep Dive

### Protocol Foundation: JSON-RPC 2.0

MCP uses **JSON-RPC 2.0** as its message format. This provides:
- Standardized request/response structure
- Bidirectional communication
- Error handling
- Batch operations

### Message Types

#### 1. Request
Client initiates an action on the server.

**Structure**:
```json
{
  "jsonrpc": "2.0",
  "id": "unique-request-id",
  "method": "method_name",
  "params": { /* method parameters */ }
}
```

**Key Fields**:
- `jsonrpc`: Always "2.0"
- `id`: Unique identifier to pair with response
- `method`: The operation to perform
- `params`: Input parameters (optional)

#### 2. Response
Server replies to a request (success or error).

**Success Response**:
```json
{
  "jsonrpc": "2.0",
  "id": "unique-request-id",
  "result": { /* operation result */ }
}
```

**Error Response**:
```json
{
  "jsonrpc": "2.0",
  "id": "unique-request-id",
  "error": {
    "code": -32603,
    "message": "Internal error",
    "data": { /* additional error info */ }
  }
}
```

#### 3. Notification
One-way message (no response expected).

**Structure**:
```json
{
  "jsonrpc": "2.0",
  "method": "notification_method",
  "params": { /* parameters */ }
}
```

**Note**: No `id` field since no response is expected.

---

### Core MCP Methods

#### Tool Discovery: `tools/list`

**Request**:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

**Response**:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "execute_query",
        "description": "Execute SQL query on database",
        "inputSchema": {
          "type": "object",
          "properties": {
            "query": {
              "type": "string",
              "description": "SQL query to execute"
            }
          },
          "required": ["query"]
        }
      },
      {
        "name": "list_tables",
        "description": "List all database tables",
        "inputSchema": {
          "type": "object",
          "properties": {}
        }
      }
    ]
  }
}
```

#### Tool Execution: `tools/call`

**Request**:
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "execute_query",
    "arguments": {
      "query": "SELECT * FROM users WHERE age > 25"
    }
  }
}
```

**Response**:
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "[\n  {\"id\": 1, \"name\": \"Alice\", \"age\": 30},\n  {\"id\": 3, \"name\": \"Charlie\", \"age\": 28}\n]"
      }
    ],
    "isError": false
  }
}
```

**Error Response**:
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "error": {
    "code": -32602,
    "message": "Invalid SQL syntax",
    "data": {
      "query": "SELECT * FROM users WHERE age >",
      "error": "Syntax error near EOF"
    }
  }
}
```

#### Resource Access: `resources/read`

**Request**:
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "resources/read",
  "params": {
    "uri": "file:///documents/report.pdf"
  }
}
```

**Response**:
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "contents": [
      {
        "uri": "file:///documents/report.pdf",
        "mimeType": "application/pdf",
        "text": "Document content as text..."
      }
    ]
  }
}
```

---

## Complete Data Flow

### Scenario: User asks "Show me all users in the database"

#### Phase 1: Initialization (Happens at startup)

```
┌──────────────┐
│ Host Startup │
└──────┬───────┘
       │
       ↓
┌────────────────────────────────────────┐
│ Agent initializes MCP Clients         │
│                                        │
│ client1 = MCPClient("database-server") │
│ client2 = MCPClient("filesystem")      │
└────────┬───────────────────────────────┘
         │
         ↓
┌─────────────────────────────────────────────────────────┐
│ Each MCP Client connects to its MCP Server              │
│                                                         │
│ 1. Establish connection (STDIO or HTTP+SSE)            │
│ 2. Negotiate capabilities                              │
│ 3. Request tool list (tools/list)                      │
└────────┬────────────────────────────────────────────────┘
         │
         ↓
┌─────────────────────────────────────────────────────────┐
│ MCP Servers respond with tool schemas                   │
│                                                         │
│ Database Server:                                        │
│   - execute_query(query: string)                        │
│   - list_tables()                                       │
│                                                         │
│ Filesystem Server:                                      │
│   - read_file(path: string)                             │
│   - write_file(path: string, content: string)           │
└────────┬────────────────────────────────────────────────┘
         │
         ↓
┌─────────────────────────────────────────────────────────┐
│ Agent builds unified tool registry                      │
│                                                         │
│ tools = {                                               │
│   "execute_query": client1,                             │
│   "list_tables": client1,                               │
│   "read_file": client2,                                 │
│   "write_file": client2                                 │
│ }                                                       │
└─────────────────────────────────────────────────────────┘
```

---

#### Phase 2: User Query Processing

**Step 1: User Input**
```
User → Host Application → Agent

Input: "Show me all users in the database"
```

**Step 2: Agent Prepares Context**
```python
# Agent builds conversation context
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant with access to database tools."
    },
    {
        "role": "user",
        "content": "Show me all users in the database"
    }
]

# Agent prepares tool schemas for LLM
tools = [
    {
        "type": "function",
        "function": {
            "name": "execute_query",
            "description": "Execute SQL query on database",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "SQL query to execute"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_tables",
            "description": "List all database tables",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]
```

**Step 3: Agent Sends to LLM**
```
Agent → LLM API

POST /api/chat
{
    "model": "gpt-4",
    "messages": [...],  // conversation history
    "tools": [...]      // available tools
}
```

**Step 4: LLM Reasoning**
```
LLM Internal Process:
1. Parse user intent: "User wants to see database users"
2. Check available tools: "I have execute_query and list_tables"
3. Reason: "To get users, I need to query the users table"
4. Generate tool call: execute_query with SELECT * FROM users
```

**Step 5: LLM Response with Tool Call**
```
LLM → Agent

{
    "message": {
        "role": "assistant",
        "content": "",  // empty when making tool call
        "tool_calls": [
            {
                "id": "call_abc123",
                "type": "function",
                "function": {
                    "name": "execute_query",
                    "arguments": "{\"query\": \"SELECT * FROM users\"}"
                }
            }
        ]
    }
}
```

---

#### Phase 3: Tool Execution

**Step 6: Agent Extracts Tool Call**
```python
# Agent parses LLM response
tool_call = response.message.tool_calls[0]

tool_name = tool_call.function.name  # "execute_query"
arguments = json.loads(tool_call.function.arguments)  # {"query": "SELECT * FROM users"}

# Agent looks up which MCP client handles this tool
mcp_client = tool_registry[tool_name]  # client1 (database client)
```

**Step 7: Agent Routes to MCP Client**
```python
# Agent requests tool execution from MCP client
result = mcp_client.call_tool(
    name="execute_query",
    arguments={"query": "SELECT * FROM users"}
)
```

**Step 8: MCP Client Sends JSON-RPC Request**
```
MCP Client → MCP Server

Via STDIO or HTTP:
{
    "jsonrpc": "2.0",
    "id": "req_xyz789",
    "method": "tools/call",
    "params": {
        "name": "execute_query",
        "arguments": {
            "query": "SELECT * FROM users"
        }
    }
}
```

**Step 9: MCP Server Executes Tool**
```python
# MCP Server receives request
def handle_tool_call(method, params):
    if params["name"] == "execute_query":
        query = params["arguments"]["query"]

        # Execute actual business logic
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        # Format results
        users = [
            {"id": row[0], "name": row[1], "email": row[2]}
            for row in results
        ]

        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(users, indent=2)
                }
            ],
            "isError": False
        }
```

**Step 10: MCP Server Returns Result**
```
MCP Server → MCP Client

{
    "jsonrpc": "2.0",
    "id": "req_xyz789",
    "result": {
        "content": [
            {
                "type": "text",
                "text": "[\n  {\"id\": 1, \"name\": \"Alice\", \"email\": \"alice@example.com\"},\n  {\"id\": 2, \"name\": \"Bob\", \"email\": \"bob@example.com\"},\n  {\"id\": 3, \"name\": \"Charlie\", \"email\": \"charlie@example.com\"}\n]"
            }
        ],
        "isError": false
    }
}
```

**Step 11: MCP Client Returns to Agent**
```python
# MCP Client parses JSON-RPC response
result = {
    "tool_call_id": "call_abc123",
    "content": "[\n  {\"id\": 1, \"name\": \"Alice\", \"email\": \"alice@example.com\"},\n  {\"id\": 2, \"name\": \"Bob\", \"email\": \"bob@example.com\"},\n  {\"id\": 3, \"name\": \"Charlie\", \"email\": \"charlie@example.com\"}\n]"
}

# Returns to agent
return result
```

---

#### Phase 4: Result Processing

**Step 12: Agent Appends Tool Result to Conversation**
```python
# Agent adds tool result to conversation history
messages.append({
    "role": "assistant",
    "content": "",
    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "execute_query",
                "arguments": "{\"query\": \"SELECT * FROM users\"}"
            }
        }
    ]
})

messages.append({
    "role": "tool",
    "tool_call_id": "call_abc123",
    "content": "[\n  {\"id\": 1, \"name\": \"Alice\", \"email\": \"alice@example.com\"},\n  {\"id\": 2, \"name\": \"Bob\", \"email\": \"bob@example.com\"},\n  {\"id\": 3, \"name\": \"Charlie\", \"email\": \"charlie@example.com\"}\n]"
})
```

**Step 13: Agent Sends Back to LLM**
```
Agent → LLM API

POST /api/chat
{
    "model": "gpt-4",
    "messages": [
        {"role": "system", "content": "..."},
        {"role": "user", "content": "Show me all users in the database"},
        {"role": "assistant", "tool_calls": [...]},
        {"role": "tool", "content": "[{\"id\": 1, ...}, ...]"}
    ],
    "tools": [...]
}
```

**Step 14: LLM Processes Result**
```
LLM Internal Process:
1. See tool result in conversation
2. Parse the data: 3 users (Alice, Bob, Charlie)
3. Generate human-friendly response
4. No more tool calls needed
```

**Step 15: LLM Returns Final Response**
```
LLM → Agent

{
    "message": {
        "role": "assistant",
        "content": "I found 3 users in the database:\n\n1. Alice (alice@example.com)\n2. Bob (bob@example.com)\n3. Charlie (charlie@example.com)\n\nWould you like more details about any of these users?",
        "tool_calls": null
    }
}
```

**Step 16: Agent Checks for More Tool Calls**
```python
# Agent checks if there are more tool calls
if response.message.tool_calls:
    # Loop back to Step 6 (execute more tools)
    pass
else:
    # No more tool calls, return final response
    final_response = response.message.content
```

**Step 17: Agent Returns to User**
```
Agent → Host Application → User

Display:
"I found 3 users in the database:

1. Alice (alice@example.com)
2. Bob (bob@example.com)
3. Charlie (charlie@example.com)

Would you like more details about any of these users?"
```

---

## Message Format Examples

### Example 1: Simple Tool Call

**Scenario**: Get current time

**LLM Output**:
```json
{
  "role": "assistant",
  "tool_calls": [
    {
      "id": "call_001",
      "function": {
        "name": "get_current_time",
        "arguments": "{}"
      }
    }
  ]
}
```

**MCP Request**:
```json
{
  "jsonrpc": "2.0",
  "id": "mcp_001",
  "method": "tools/call",
  "params": {
    "name": "get_current_time",
    "arguments": {}
  }
}
```

**MCP Response**:
```json
{
  "jsonrpc": "2.0",
  "id": "mcp_001",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "2025-10-28T14:30:00Z"
      }
    ]
  }
}
```

---

### Example 2: Parallel Tool Calls

**Scenario**: Get weather and news simultaneously

**LLM Output**:
```json
{
  "role": "assistant",
  "tool_calls": [
    {
      "id": "call_weather",
      "function": {
        "name": "get_weather",
        "arguments": "{\"location\": \"San Francisco\"}"
      }
    },
    {
      "id": "call_news",
      "function": {
        "name": "get_news",
        "arguments": "{\"category\": \"technology\"}"
      }
    }
  ]
}
```

**Agent Executes Both**:
```python
# Agent executes in parallel
results = await asyncio.gather(
    mcp_client_weather.call_tool("get_weather", {"location": "San Francisco"}),
    mcp_client_news.call_tool("get_news", {"category": "technology"})
)

# Both results added to conversation
messages.append({"role": "tool", "tool_call_id": "call_weather", "content": results[0]})
messages.append({"role": "tool", "tool_call_id": "call_news", "content": results[1]})
```

---

### Example 3: Error Handling

**Scenario**: Invalid SQL query

**MCP Error Response**:
```json
{
  "jsonrpc": "2.0",
  "id": "mcp_error",
  "error": {
    "code": -32602,
    "message": "Invalid parameters",
    "data": {
      "error": "SQL syntax error near 'FORM'",
      "query": "SELECT * FORM users"
    }
  }
}
```

**Agent Handling**:
```python
# Agent converts error to tool result
messages.append({
    "role": "tool",
    "tool_call_id": "call_123",
    "content": "Error: SQL syntax error near 'FORM'. Please check the query syntax."
})

# LLM sees error and can retry or explain to user
```

---

## Tool Execution Lifecycle

### Complete Lifecycle Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     INITIALIZATION PHASE                        │
└─────────────────────────────────────────────────────────────────┘

1. Host Application Starts
         ↓
2. Agent Initializes
         ↓
3. Agent Creates MCP Clients
         ↓
4. Each MCP Client Connects to MCP Server
         ↓
5. Connection Handshake (JSON-RPC)
         ↓
6. Capability Negotiation
         ↓
7. Tool Discovery (tools/list)
         ↓
8. Agent Builds Tool Registry
         ↓
┌─────────────────────────────────────────────────────────────────┐
│                    READY FOR USER QUERIES                       │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                     EXECUTION PHASE                             │
└─────────────────────────────────────────────────────────────────┘

User Input
    ↓
┌───────────────────┐
│ Agent receives    │
│ user message      │
└────────┬──────────┘
         │
         ↓
┌───────────────────┐
│ Agent appends to  │
│ conversation      │
│ history           │
└────────┬──────────┘
         │
         ↓
┌───────────────────────────────────┐
│ AGENTIC LOOP                      │
│ (max iterations: typically 5-10)  │
└───────────────────────────────────┘
         │
         ↓
┌─────────────────────┐
│ Send messages +     │
│ tools to LLM        │
└──────────┬──────────┘
           │
           ↓
┌──────────────────────┐
│ LLM analyzes intent  │
│ and decides action   │
└──────────┬───────────┘
           │
           ↓
     ┌────┴────┐
     │Decision?│
     └────┬────┘
          │
   ┌──────┴──────┐
   │             │
   ↓             ↓
┌──────┐    ┌──────────┐
│ Text │    │Tool Call │
│Response    └────┬─────┘
└───┬──┘         │
    │            ↓
    │    ┌───────────────────┐
    │    │ Agent extracts    │
    │    │ tool_calls        │
    │    └────────┬──────────┘
    │             │
    │             ↓
    │    ┌───────────────────┐
    │    │ For each tool:    │
    │    │ 1. Lookup client  │
    │    │ 2. Call tool      │
    │    └────────┬──────────┘
    │             │
    │             ↓
    │    ┌────────────────────┐
    │    │ MCP Client sends   │
    │    │ JSON-RPC request   │
    │    └────────┬───────────┘
    │             │
    │             ↓
    │    ┌────────────────────┐
    │    │ MCP Server         │
    │    │ executes tool      │
    │    └────────┬───────────┘
    │             │
    │             ↓
    │    ┌────────────────────┐
    │    │ MCP Server returns │
    │    │ result/error       │
    │    └────────┬───────────┘
    │             │
    │             ↓
    │    ┌────────────────────┐
    │    │ Agent appends tool │
    │    │ result to messages │
    │    └────────┬───────────┘
    │             │
    │             ↓
    │    ┌────────────────────┐
    │    │ Iteration count++  │
    │    └────────┬───────────┘
    │             │
    │             ↓
    │    ┌────────────────────┐
    │    │ Max iterations?    │
    │    └────┬───────┬───────┘
    │         │       │
    │         No      Yes
    │         │       │
    │         │       └─→ Force final response
    │         │
    │         └─→ Loop back to "Send to LLM"
    │
    └─────────────┬
                  │
                  ↓
         ┌────────────────┐
         │ Final response │
         │ to user        │
         └────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                     SHUTDOWN PHASE                              │
└─────────────────────────────────────────────────────────────────┘

Application Exit
    ↓
Agent cleanup
    ↓
MCP Clients disconnect
    ↓
MCP Servers shutdown
    ↓
Resources released
```

---

## Multi-Tool Orchestration

### Sequential Tool Execution

**Scenario**: Research → Analyze → Report

```
User: "Research AI trends, analyze the data, and create a report"

Iteration 1:
  LLM → Tool Call: search_web("AI trends 2025")
  Tool Result → LLM sees: "10 articles about AI trends..."

Iteration 2:
  LLM → Tool Call: analyze_data(articles)
  Tool Result → LLM sees: "Key findings: GenAI adoption, etc..."

Iteration 3:
  LLM → Tool Call: create_document(title="AI Trends Report", content="...")
  Tool Result → LLM sees: "Document created at /reports/ai_trends.pdf"

Iteration 4:
  LLM → Text Response: "I've completed the report. Here's a summary..."
```

**Conversation Flow**:
```python
messages = [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "Research AI trends, analyze, and report"},

    # Iteration 1
    {"role": "assistant", "tool_calls": [{"function": {"name": "search_web", ...}}]},
    {"role": "tool", "content": "10 articles found..."},

    # Iteration 2
    {"role": "assistant", "tool_calls": [{"function": {"name": "analyze_data", ...}}]},
    {"role": "tool", "content": "Analysis complete: Key findings..."},

    # Iteration 3
    {"role": "assistant", "tool_calls": [{"function": {"name": "create_document", ...}}]},
    {"role": "tool", "content": "Document created successfully..."},

    # Iteration 4
    {"role": "assistant", "content": "I've completed the comprehensive report..."}
]
```

---

### Parallel Tool Execution

**Scenario**: Check multiple data sources simultaneously

```
User: "Get weather, stock prices, and news"

Single Iteration with 3 parallel tool calls:
  LLM → Tool Calls:
    1. get_weather("San Francisco")
    2. get_stock_price("AAPL")
    3. get_news("technology")

  Agent executes all 3 in parallel via different MCP clients

  All results returned to LLM in one iteration

  LLM → Final response synthesizing all data
```

---

### Error Recovery

**Scenario**: Tool fails, LLM adapts

```
User: "Show users older than 30"

Iteration 1:
  LLM → Tool Call: execute_query("SELECT * FROM users WHERE age > 30")
  Tool Error → "Table 'users' does not exist"

Iteration 2:
  LLM → Tool Call: list_tables()
  Tool Result → ["customers", "orders", "products"]

Iteration 3:
  LLM → Tool Call: execute_query("SELECT * FROM customers WHERE age > 30")
  Tool Result → Successfully returns data

Iteration 4:
  LLM → Text Response: "I found the user data in the 'customers' table..."
```

---

## Key Takeaways

### Data Flow Summary

1. **User → Agent**: User provides natural language input
2. **Agent → LLM**: Agent sends conversation + tool schemas
3. **LLM → Agent**: LLM returns text or tool calls
4. **Agent → MCP Client**: Agent routes tool calls to appropriate client
5. **MCP Client → MCP Server**: JSON-RPC request via STDIO/HTTP
6. **MCP Server → External Resources**: Executes actual business logic
7. **External Resources → MCP Server**: Returns data
8. **MCP Server → MCP Client**: JSON-RPC response
9. **MCP Client → Agent**: Formatted tool result
10. **Agent → LLM**: Tool result appended to conversation (loop)
11. **LLM → Agent**: Final natural language response
12. **Agent → User**: Display response

### Component Relationships

- **Agent**: Orchestrator (1 per application)
- **MCP Client**: Protocol connector (N clients, one per server)
- **MCP Server**: Tool provider (N servers, independent services)
- **LLM**: Intelligence layer (called iteratively by agent)

### Protocol Details

- **Format**: JSON-RPC 2.0
- **Transport**: STDIO (local) or HTTP+SSE (remote)
- **Methods**: `tools/list`, `tools/call`, `resources/read`, etc.
- **Error Handling**: Standard JSON-RPC error responses

### Iteration Loop

- Agent manages **agentic loop** (typically 5-10 max iterations)
- Each iteration can have **multiple parallel tool calls**
- LLM decides when to **stop calling tools** and return final response
- Enables **multi-step reasoning** and complex orchestration

---

## Conclusion

The MCP architecture provides a clean separation of concerns:

- **Agents** handle orchestration and conversation management
- **MCP Clients** implement the protocol and manage connections
- **MCP Servers** provide tools and execute business logic
- **LLMs** provide intelligence and decision-making

This architecture enables:
- **Extensibility**: Add new tools by adding MCP servers
- **Reusability**: Same MCP server can serve multiple clients
- **Standardization**: JSON-RPC 2.0 ensures interoperability
- **Flexibility**: Local (STDIO) or remote (HTTP) communication
- **Intelligence**: LLM-driven tool selection and orchestration

The result is a powerful, flexible system where AI agents can seamlessly access external tools and resources through a standardized protocol.

---

*Last Updated: October 2025*
