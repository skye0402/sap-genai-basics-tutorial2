# 06 - MCP Tutorial: Building an Agentic AI

In this exercise, you'll learn how to build an **agentic AI** using:
- **LangGraph** with a **React Agent** pattern
- **Model Context Protocol (MCP)** for tool communication

## What You'll Learn

1. **MCP Server**: How to create tools that can be called by AI agents
2. **React Agent**: How an agent reasons, acts, and observes in a loop
3. **Tool Integration**: How to connect MCP tools to LangGraph

## Architecture

```
┌─────────────────┐         stdio          ┌─────────────────┐
│                 │ ◄────────────────────► │                 │
│  React Agent    │                        │   MCP Server    │
│  (LangGraph)    │                        │  (Calculator)   │
│                 │  tool calls/results    │                 │
└────────┬────────┘                        └─────────────────┘
         │                                   Tools:
         │ LLM calls                         • add(a, b)
         ▼                                   • multiply(a, b)
┌─────────────────┐                          • subtract(a, b)
│   SAP AI Core   │
│   (GPT-4.1)     │
└─────────────────┘
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
| `mcp_server.py` | MCP server with calculator tools (add, multiply, subtract) |
| `agent_client.py` | LangGraph React agent that connects to the MCP server |
| `pyproject.toml` | Project dependencies |

## Setup

1. **Navigate to this directory:**
   ```bash
   cd 06-mcp-tutorial
   ```

2. **Create virtual environment and install dependencies:**
   ```bash
   uv sync
   ```

3. **Ensure your `.env` file is configured** (in the repo root):
   - SAP AI Core credentials must be set
   - See `.env.example` for required variables

## Running the Exercise

### Option 1: Run the Agent Client (Recommended)

The agent client automatically starts the MCP server as a subprocess:

```bash
uv run python agent_client.py
```

You'll see:
```
🔌 Connecting to MCP Calculator Server...
--------------------------------------------------
✅ Loaded 3 tools from MCP server:
   - add: Add two numbers together.
   - multiply: Multiply two numbers together.
   - subtract: Subtract the second number from the first.
--------------------------------------------------

🤖 React Agent Ready!
Ask me math questions and I'll use the calculator tools.
Type 'quit' or press Enter on empty line to exit.

You: 
```

### Try These Prompts

```
You: What is 42 + 17?
You: Calculate 7 times 8
You: What is 100 minus 37?
You: If I have 5 apples and buy 3 more, then give away 2, how many do I have?
You: What is (10 + 5) * 3?
```

### Option 2: Test MCP Server Separately

You can test the MCP server using the MCP development tools:

```bash
# Start the MCP Inspector (opens in browser)
uv run mcp dev mcp_server.py
```

## Understanding the Code

### MCP Server (`mcp_server.py`)

The server uses `FastMCP` to define tools:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b
```

Key points:
- `@mcp.tool()` decorator exposes functions as MCP tools
- Docstrings become tool descriptions for the LLM
- Type hints define the tool's input schema

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

## Exercises

### Exercise 1: Add a New Tool

Add a `divide` tool to `mcp_server.py`:

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
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### Exercise 2: Add a Power Tool

```python
@mcp.tool()
def power(base: int, exponent: int) -> int:
    """Raise a number to a power.
    
    Args:
        base: The base number
        exponent: The power to raise to
        
    Returns:
        base raised to the power of exponent
    """
    return base ** exponent
```

### Exercise 3: Create a Different MCP Server

Create a new server with string manipulation tools:

```python
@mcp.tool()
def reverse_string(text: str) -> str:
    """Reverse a string."""
    return text[::-1]

@mcp.tool()
def count_words(text: str) -> int:
    """Count words in a string."""
    return len(text.split())
```

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
