# 06 - MCP Tutorial: Building an Agentic AI

In this exercise, you'll learn how to build an **agentic AI** using:
- **LangGraph** with a **React Agent** pattern
- **Model Context Protocol (MCP)** for tool communication

## Learning Objectives

After completing this exercise, you will understand:
1. How MCP servers expose tools to AI agents
2. How the React agent pattern works (Reasoning + Acting loop)
3. How to create custom tools for LLM agents

## Architecture Overview

```
┌─────────────────┐         stdio          ┌─────────────────┐
│                 │ ◄────────────────────► │                 │
│  React Agent    │                        │   MCP Server    │
│  (LangGraph)    │                        │  (Calculator)   │
│                 │  tool calls/results    │                 │
└────────┬────────┘                        └─────────────────┘
         │                                   Tools:
         │ LLM calls                         • add(a, b) ✅
         ▼                                   • multiply(a, b) ❓
┌─────────────────┐                          • subtract(a, b) ❓
│   SAP AI Core   │                          • divide(a, b) ⭐
│   (GPT-4.1)     │
└─────────────────┘
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

3. **Verify your `.env` file** is configured in the repo root.

---

## Exercise 1: Implement the `multiply` Tool (10 minutes)

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

## Exercise 2: Implement the `subtract` Tool (10 minutes)

Find the `subtract` function in `mcp_server.py` and implement it.

**Your task:** Replace the `raise` statement with code that subtracts `b` from `a`.

### Test Your Solution

```bash
uv run python agent_client.py --verbose
```

Try: `What is 100 minus 37?`

---

## Exercise 3: Add a `divide` Tool (15 minutes)

Create a completely new tool from scratch!

**Your task:** Add a `divide` tool that:
1. Takes two numbers `a` and `b`
2. Returns `a / b` as a float
3. Handles division by zero gracefully

**Template to get started:**

```python
@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide the first number by the second.
    
    Args:
        a: Dividend (number to be divided)
        b: Divisor (number to divide by)
        
    Returns:
        The quotient (a / b)
    """
    # Your implementation here
    pass
```

**Important:** The docstring is read by the LLM! Write it clearly.

### Test Your Solution

Try: `What is 100 divided by 4?`

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
