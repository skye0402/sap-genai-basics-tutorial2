# 07 - MCP Tutorial: Complete Solution

> **Note:** This is the complete solution. For the exercise version, see `../07-mcp-tutorial/`

This folder contains a working **agentic AI** implementation using:
- **LangGraph** with a **React Agent** pattern
- **Model Context Protocol (MCP)** for tool communication
- **S/4HANA Cloud API** integration for real enterprise data

## Architecture

```
┌─────────────────┐         stdio          ┌─────────────────┐
│                 │ ◄────────────────────► │                 │
│  React Agent    │                        │   MCP Server    │
│  (LangGraph)    │                        │                 │
│                 │  tool calls/results    │                 │
└────────┬────────┘                        └────────┬────────┘
         │                                          │
         │ LLM calls                      Tools:    │ HTTP/OData
         ▼                                          ▼
┌─────────────────┐              ┌──────────────────────────────┐
│   SAP AI Core   │              │  Calculator                  │
│   (GPT-4.1)     │              │  • add, subtract,            │
└─────────────────┘              │    multiply, divide          │
                                 │                              │
                                 │  S/4HANA Product API         │
                                 │  • product_api (universal)   │
                                 │  • search_product_descriptions│
                                 │  • query_products            │
                                 │  • get_product_api_documentation│
                                 │                              │
                                 │  S/4HANA Material Stock API  │
                                 │  • stock_api (universal)     │
                                 │                              │
                                 │  Memory                      │
                                 │  • memory_load / _save /     │
                                 │    _delete                   │
                                 │    (agent_memory.md)         │
                                 └──────────────────────────────┘
```

## The React Agent Pattern

**React** stands for **Re**asoning + **Act**ing. The agent follows this loop:

1. **Observe**: Receive user input or tool results
2. **Think**: LLM reasons about what to do next
3. **Act**: Either call a tool or respond to user
4. **Repeat**: Continue until the task is complete

```
User: "What is 5 times 3 plus 2?"

Agent Thinking: I need to multiply 5 and 3 first
Agent Action: multiply(5, 3) → 15

Agent Thinking: Now I need to add 2 to the result
Agent Action: add(15, 2) → 17

Agent Thinking: I have the answer
Agent Response: "5 times 3 plus 2 equals 17"
```

## Files

| File | Description |
|------|-------------|
| `mcp_server.py` | MCP server with calculator, S/4HANA Product & Stock API, and memory tools |
| `agent_client.py` | LangGraph React agent that connects to the MCP server |
| `s4hana_product_api_docs.py` | API documentation for the S/4HANA Product Master API |
| `agent_memory.md` | Persistent memory file — the agent reads/writes numbered notes here |
| `pyproject.toml` | Project dependencies |

## Setup

1. **Navigate to this directory:**
   ```bash
   cd 07-mcp-tutorial-complete
   ```

2. **Create virtual environment and install dependencies:**
   ```bash
   uv sync
   ```

3. **Ensure your `.env` file is configured** (in the repo root)

## Running

### Basic Mode

```bash
uv run python agent_client.py
```

### Verbose Mode (See Tool Calls)

```bash
uv run python agent_client.py --verbose
```

Example with verbose mode:
```
You: What is 3 + 7 times 2?

  🔧 Calling tool: multiply({'a': 7, 'b': 2})
  ✅ Result: 14
  🔧 Calling tool: add({'a': 3, 'b': 14})
  ✅ Result: 17

You: 
```

### Try These Prompts

**Calculator:**
```
You: What is 42 + 17?
You: Calculate 7 times 8
You: What is 100 minus 37?
You: If I have 5 apples and buy 3 more, then give away 2, how many do I have?
```

**S/4HANA Product API:**
```
You: What products do we have?
You: Search for products containing CAT
You: Show me finished products (type FERT)
You: Get me the sales text for a product
```

**S/4HANA Material Stock:**
```
You: What stock do we have for material TG11?
You: Show me stock levels at plant 1710
```

**Memory (persistent across sessions):**
```
You: My name is Günter and I work for SAP.
(next session)
You: Hi!
→ Agent greets you by name, remembering who you are.
```

### Option 2: Test MCP Server Separately (MCP Inspector)

You can also test the MCP server **directly** using the MCP Inspector web UI.
This is helpful to debug tools without running the agent client.

1. From this folder, activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
2. Then start the inspector:
   ```bash
   npx @modelcontextprotocol/inspector
   ```
3. In the Inspector UI:
   - **Transport type**: `STDIO`
   - **Command**: `python`
   - **Arguments**: `mcp_server.py`
4. Click **Connect**, then use the **Tools** tab to invoke and debug the MCP tools.

## Understanding the Code

### MCP Server (`mcp_server.py`)

The server uses `FastMCP` to define tools:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator and S4HANA Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b
```

Key points:
- `@mcp.tool()` decorator exposes functions as MCP tools
- Docstrings become tool descriptions for the LLM
- Type hints define the tool's input schema

**Universal API tools** (`product_api`, `stock_api`) follow a thin-gateway pattern:
the LLM constructs the OData path + query string, and the tool just handles
authentication and the base URL. This keeps the tools simple and lets the LLM
use the full power of OData (any entity, filter, expand, etc.).

**Memory tools** (`memory_load`, `memory_save`, `memory_delete`) persist numbered
notes to `agent_memory.md`. The agent loads memory at the start of every
conversation and saves new discoveries automatically — so it remembers user
preferences and API learnings across sessions.

### Agent Client (`agent_client.py`)

The client connects to MCP and creates a React agent:

```python
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.tools import load_mcp_tools

# Connect to MCP server
async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        
        # Load MCP tools as LangChain tools
        tools = await load_mcp_tools(session)
        
        # Create React agent
        agent = create_react_agent(llm, tools, prompt=SYSTEM_PROMPT)
```

Key points:
- `stdio_client` communicates with the MCP server via stdin/stdout
- `load_mcp_tools` converts MCP tools to LangChain format
- `create_react_agent` creates the reasoning loop

## Troubleshooting

### "ModuleNotFoundError: No module named 'mcp'"

Run `uv sync` to install dependencies.

### "Connection refused" or timeout errors

The MCP server runs via stdio, not network ports. Make sure you're using `agent_client.py` which starts the server automatically.

### LLM not using tools

- Check that the system prompt encourages tool use
- Try more explicit requests like "Use the add tool to calculate 5 + 3"

## Further Reading

- [MCP Python SDK Documentation](https://modelcontextprotocol.io/docs)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [React Agent Pattern](https://arxiv.org/abs/2210.03629)
