"""
MCP Server with simple calculator tools.

This server exposes three simple tools via the Model Context Protocol:
- add: Add two numbers
- multiply: Multiply two numbers  
- subtract: Subtract two numbers

Run with:
    uv run python mcp_server.py
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server with a descriptive name
mcp = FastMCP("Calculator Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
    """
    return a * b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first.
    
    Args:
        a: First number (minuend)
        b: Second number (subtrahend)
        
    Returns:
        The difference (a - b)
    """
    return a - b


if __name__ == "__main__":
    # Run with stdio transport for local communication
    # This is the standard way to run MCP servers that will be called by agents
    mcp.run(transport="stdio")
