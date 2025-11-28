"""
MCP Server with Calculator Tools - Complete Solution

This server exposes calculator tools via the Model Context Protocol:
- add: Add two numbers
- multiply: Multiply two numbers  
- subtract: Subtract two numbers
- divide: Divide two numbers

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


@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide the first number by the second.
    
    Args:
        a: Dividend (number to be divided)
        b: Divisor (number to divide by)
        
    Returns:
        The quotient (a / b)
        
    Raises:
        ValueError: If b is zero (division by zero)
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    # Run with stdio transport for local communication
    # This is the standard way to run MCP servers that will be called by agents
    mcp.run(transport="stdio")
