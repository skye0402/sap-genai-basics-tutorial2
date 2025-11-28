"""
MCP Server with Calculator Tools - Exercise

This server exposes calculator tools via the Model Context Protocol (MCP).
Your task is to complete the missing tools!

Run with:
    uv run python mcp_server.py

Test with MCP Inspector:
    uv run mcp dev mcp_server.py
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server with a descriptive name
mcp = FastMCP("Calculator Server")


# ============================================================================
# EXAMPLE: This tool is already implemented for you
# ============================================================================

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


# ============================================================================
# EXERCISE 1: Implement the multiply tool
# ============================================================================

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
    """
    # TODO: Implement this function
    # Hint: Use the * operator
    raise NotImplementedError("Exercise 1: Implement the multiply function")


# ============================================================================
# EXERCISE 2: Implement the subtract tool
# ============================================================================

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first.
    
    Args:
        a: First number (minuend)
        b: Second number (subtrahend)
        
    Returns:
        The difference (a - b)
    """
    # TODO: Implement this function
    # Hint: Use the - operator
    raise NotImplementedError("Exercise 2: Implement the subtract function")


# ============================================================================
# BONUS EXERCISE: Add a divide tool
# ============================================================================

# TODO: Create a new tool called 'divide' that divides a by b
# Remember to:
# 1. Use the @mcp.tool() decorator
# 2. Add type hints for parameters and return value
# 3. Write a helpful docstring (the LLM reads this!)
# 4. Handle division by zero with an error message
#
# Example structure:
# @mcp.tool()
# def divide(a: int, b: int) -> float:
#     """Your docstring here"""
#     # Your code here


if __name__ == "__main__":
    # Run with stdio transport for local communication
    mcp.run(transport="stdio")
