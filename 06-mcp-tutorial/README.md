# 06 - MCP Tutorial: Building an Agentic AI

In this exercise, you'll learn how to build an **agentic AI** using:
- **LangGraph** with a **React Agent** pattern
- **Model Context Protocol (MCP)** for tool communication
- **S/4HANA Cloud API** integration for real enterprise data

## Learning Objectives

After completing this exercise, you will understand:
1. How MCP servers expose tools to AI agents
2. How the React agent pattern works (Reasoning + Acting loop)
3. How to create custom tools for LLM agents
4. How to integrate enterprise APIs (S/4HANA) with AI agents

## Architecture Overview

```
┌─────────────────┐         stdio          ┌─────────────────┐
│                 │ ◄────────────────────► │                 │
│  React Agent    │                        │   MCP Server    │
│  (LangGraph)    │                        │                 │
│                 │  tool calls/results    │                 │
└────────┬────────┘                        └────────┬────────┘
         │                                          │
         │ LLM calls                      Tools:    │ HTTP/OData
         ▼                                • add ✅   ▼
┌─────────────────┐                       • multiply ❓  ┌─────────────────┐
│   SAP AI Core   │                       • subtract ❓  │  S/4HANA Cloud  │
│   (GPT-4.1)     │                       • divide ❓    │  Product API    │
└─────────────────┘                       • query_products ⭐ └─────────────────┘
```

## Setup (5 minutes)

1. **Navigate to this directory:**
   ```bash
   cd 06-mcp-tutorial
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Verify your `.env` file** is configured in the repo root with:
   - SAP AI Core credentials
   - S/4HANA credentials (`S4HANA_USER`, `S4HANA_PASSWORD`, `S4PRODUCT_MASTER_ENDPOINT`)

## Optional: Test MCP Server with MCP Inspector

After setup you can test the MCP server **on its own** using the MCP Inspector web UI.
This is useful for debugging your tools before wiring them into the agent.

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
4. Click **Connect**, then use the **Tools** tab to call your MCP tools interactively.

---

# Part 1: Calculator Tools (Warmup - 15 minutes)

## Exercise 1.1: Implement the `multiply` Tool (5 minutes)

Open `mcp_server.py` and find the `multiply` function. It currently raises a `NotImplementedError`.

**Your task:** Replace the `raise` statement with the actual implementation.

```python
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    # TODO: Implement this function
    raise NotImplementedError("Exercise 1: Implement the multiply function")
```

**Hint:** The implementation is just one line using the `*` operator.

### Test Your Solution

```bash
uv run python agent_client.py --verbose
```

Try: `What is 7 times 8?`

---

## Exercise 1.2: Implement `subtract` and `divide` (10 minutes)

Implement the remaining calculator tools in `mcp_server.py`:

1. **subtract(a, b)**: Return `a - b`
2. **divide(a, b)**: Return `a / b` as a float, handle division by zero!

### Test Your Solution

```bash
uv run python agent_client.py --verbose
```

Try: `What is 100 minus 37?` and `What is 100 divided by 4?`

---

# Part 2: S/4HANA Product API Integration (Main Exercise - 30 minutes)

Now let's build something more interesting: connect your AI agent to a real enterprise system!

## Exercise 2.1: Add the API Documentation Tool (10 minutes)

The AI needs to understand how to query the S/4HANA Product API. Create a tool that provides this documentation.

**Your task:** In `mcp_server.py`, implement the `get_product_api_documentation` tool:

```python
@mcp.tool()
def get_product_api_documentation() -> str:
    """Get documentation for the S/4HANA Product Master API.
    
    Call this tool FIRST to understand how to query products from S/4HANA.
    The documentation explains available OData query parameters.
    
    Returns:
        API documentation as a string
    """
    # TODO: Return the API documentation from s4hana_product_api_docs.py
    raise NotImplementedError("Exercise 2.1: Return the PRODUCT_API_DOCUMENTATION")
```

**Hint:** Import and return `PRODUCT_API_DOCUMENTATION` from `s4hana_product_api_docs.py`

---

## Exercise 2.2: Implement the Product Query Tool (20 minutes)

Now implement the tool that actually calls the S/4HANA API!

**Your task:** Complete the `query_products` function in `mcp_server.py`:

```python
@mcp.tool()
def query_products(
    filter_expression: str = "",
    select_fields: str = "",
    top: int = 10,
) -> dict:
    """Query the S/4HANA Product Master API.
    
    Args:
        filter_expression: OData $filter (e.g., "contains(Product,'CAT')")
        select_fields: Comma-separated fields to return
        top: Maximum results (default: 10)
    
    Returns:
        Dictionary with success status and product data
    """
    # TODO: Implement the API call using httpx
    raise NotImplementedError("Exercise 2.2: Implement the API call")
```

**Implementation steps:**
1. Build the URL: `{S4PRODUCT_ENDPOINT}/Product`
2. Add query parameters: `$filter`, `$select`, `$top`
3. Make HTTP GET request with Basic Auth
4. Return the results as a dictionary

**Hint:** Use `httpx.Client()` with `auth=(S4HANA_USER, S4HANA_PASSWORD)`

### Test Your Solution

```bash
uv run python agent_client.py --verbose
```

Try these questions:
- `What products do we have?`
- `Search for products containing CAT`
- `Show me finished products (FERT type)`

---

## Bonus Exercise: HTTP Streaming Transport (20 minutes)

Currently, the MCP server uses **stdio** (standard input/output) for communication. 
This works well for local tools but doesn't scale to network services.

**Challenge:** Convert the server to use **HTTP Streaming** transport.

### Step 1: Modify the MCP Server

Change the transport from `stdio` to `streamable-http`:

```python
if __name__ == "__main__":
    # Change this:
    # mcp.run(transport="stdio")
    
    # To this:
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8005)
```

### Step 2: Create a New Client

Create `agent_client_http.py` that connects via HTTP instead of stdio.

**Key changes needed:**

```python
# Instead of:
from mcp.client.stdio import stdio_client

# Use:
from mcp.client.streamable_http import streamablehttp_client

# Instead of:
async with stdio_client(server_params) as (read, write):

# Use:
async with streamablehttp_client("http://127.0.0.1:8005/mcp") as (read, write, _):
```

### Step 3: Run Separately

```bash
# Terminal 1: Start the HTTP server
uv run python mcp_server.py

# Terminal 2: Run the client
uv run python agent_client_http.py
```

---

## The React Agent Pattern

**React** = **Re**asoning + **Act**ing

```
User: "What is 5 times 3 plus 2?"

Agent Thinking: I need to multiply 5 and 3 first
Agent Action:   multiply(5, 3) → 15

Agent Thinking: Now I add 2 to the result  
Agent Action:   add(15, 2) → 17

Agent Thinking: I have the final answer
Agent Response: "5 times 3 plus 2 equals 17"
```

Use `--verbose` flag to see this in action!

---

## Key Concepts

### MCP Tool Decorator

```python
@mcp.tool()
def my_tool(param: str) -> str:
    """This docstring is shown to the LLM!
    
    Write it clearly so the AI knows when to use this tool.
    """
    return result
```

### Why MCP?

- **Standardized Protocol**: Tools work with any MCP-compatible AI system
- **Separation of Concerns**: Tools are independent from the AI logic
- **Reusability**: Same tools can be used by different agents
- **Testability**: Test tools independently with MCP Inspector

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Run `uv sync` |
| Tool not being called | Check your docstring - is it clear? |
| `NotImplementedError` | You haven't implemented the exercise yet! |
| Division by zero crash | Add error handling in your divide function |

---

## Solution

See `../06-mcp-tutorial-complete/` for the complete implementation.

## Further Reading

- [MCP Python SDK](https://modelcontextprotocol.io/docs)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [React Paper](https://arxiv.org/abs/2210.03629) - The original ReAct research
