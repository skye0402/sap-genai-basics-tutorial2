"""
MCP Server with Calculator and S/4HANA Tools - Exercise

This server exposes tools via the Model Context Protocol (MCP).
Your task is to complete the missing tools!

Part 1: Calculator Tools (Warmup)
- add: Already implemented ✅
- multiply: Exercise 1.1
- subtract: Exercise 1.2
- divide: Exercise 1.2

Part 2: S/4HANA Product API Tools (Main Exercise)
- get_product_api_documentation: Exercise 2.1
- query_products: Exercise 2.2

Run with:
    uv run python mcp_server.py

Test with MCP Inspector:
    uv run mcp dev mcp_server.py
"""

import os
from pathlib import Path

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables from parent directory
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# S/4HANA configuration (used in Exercise 2)
S4HANA_USER = os.getenv("S4HANA_USER", "")
S4HANA_PASSWORD = os.getenv("S4HANA_PASSWORD", "")
S4PRODUCT_ENDPOINT = os.getenv("S4PRODUCT_MASTER_ENDPOINT", "")

# Create an MCP server with a descriptive name
mcp = FastMCP("Calculator and S4HANA Server")


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
# EXERCISE 1.1: Implement the multiply tool
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
    raise NotImplementedError("Exercise 1.1: Implement the multiply function")


# ============================================================================
# EXERCISE 1.2: Implement subtract and divide tools
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
    raise NotImplementedError("Exercise 1.2: Implement the subtract function")


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
    # TODO: Implement this function
    # Hint: Check if b is zero first, then use the / operator
    raise NotImplementedError("Exercise 1.2: Implement the divide function")


# =============================================================================
# PART 2: S/4HANA Product API Tools
# =============================================================================

# ============================================================================
# EXERCISE 2.1: Search Product Descriptions Tool (RECOMMENDED for text search)
# ============================================================================

@mcp.tool()
def search_product_descriptions(
    search_text: str,
    language: str = "EN",
    top: int = 20,
) -> dict:
    """Search for products by their description text in a specific language.
    
    This is the BEST way to find products by name/text (e.g., "cat food", "battery").
    It searches the ProductDescription entity directly, which is much faster than
    fetching all products and scanning.
    
    Args:
        search_text: Text to search for in product descriptions (case-insensitive).
            Examples: "cat", "food", "battery", "LED"
        language: Language code for the description. Default "EN" for English.
            Common codes: EN (English), DE (German), JA (Japanese), 
            FR (French), ES (Spanish), ZH (Chinese), KO (Korean)
        top: Maximum number of results (default: 20)
    
    Returns:
        Dictionary with products matching the search text in their description.
        Each result includes Product ID, Language, and ProductDescription.
    """
    # TODO: Implement the ProductDescription search
    #
    # Steps:
    # 1. Check if S4PRODUCT_ENDPOINT, S4HANA_USER, S4HANA_PASSWORD are configured
    # 2. Build the URL: f"{S4PRODUCT_ENDPOINT.rstrip('/')}/ProductDescription"
    # 3. Build filter: contains(ProductDescription,'{search_text}') and Language eq '{language}'
    #    (escape single quotes in search_text using search_text.replace("'", "''"))
    # 4. Make HTTP GET request using httpx with Basic Auth
    # 5. Return results
    #
    # Hint: The filter should look like:
    # f"contains(ProductDescription,'{search_text}') and Language eq '{language.upper()}'"
    
    raise NotImplementedError("Exercise 2.1: Implement search_product_descriptions")


# ============================================================================
# EXERCISE 2.2: Get API Documentation Tool
# ============================================================================

@mcp.tool()
def get_product_api_documentation() -> str:
    """Get documentation for the S/4HANA Product Master API.
    
    Returns comprehensive API documentation as a string.
    """
    # TODO: Import and return PRODUCT_API_DOCUMENTATION from s4hana_product_api_docs.py
    # Hint: from s4hana_product_api_docs import PRODUCT_API_DOCUMENTATION
    raise NotImplementedError("Exercise 2.2: Return the API documentation")


# ============================================================================
# EXERCISE 2.3: Query Products Tool (for ID-based search and full details)
# ============================================================================

@mcp.tool()
def query_products(
    filter_expression: str = "",
    select_fields: str = "",
    top: int = 10,
    skip: int = 0,
    orderby: str = "",
) -> dict:
    """Query the S/4HANA Product Master API with flexible OData parameters.
    
    IMPORTANT: Call get_product_api_documentation() first to understand the query syntax!
    
    Args:
        filter_expression: OData $filter expression for searching products.
            Examples:
            - "contains(Product,'CAT')" - Products containing 'CAT'
            - "ProductType eq 'FERT'" - Only finished products
            - "contains(Product,'FOOD') and ProductType eq 'FERT'" - Combined
        select_fields: Comma-separated list of fields to return.
            Example: "Product,ProductType,ProductGroup,BaseUnit"
            Leave empty for all fields.
        top: Maximum number of results to return (default: 10)
        skip: Number of results to skip for pagination (default: 0)
        orderby: Field to sort by, with optional 'asc' or 'desc'.
            Example: "Product asc" or "CreationDate desc"
    
    Returns:
        Dictionary with 'success' boolean, 'data' (list of products), 
        'count' (number returned), and 'error' (if any)
    """
    # TODO: Implement the S/4HANA API call
    # 
    # Steps:
    # 1. Check if S4PRODUCT_ENDPOINT, S4HANA_USER, S4HANA_PASSWORD are configured
    # 2. Build the URL: f"{S4PRODUCT_ENDPOINT.rstrip('/')}/Product"
    # 3. Build query params dict with $filter, $select, $top, etc.
    # 4. Make HTTP GET request using httpx:
    #    with httpx.Client(timeout=30.0) as client:
    #        response = client.get(url, params=params, auth=(S4HANA_USER, S4HANA_PASSWORD))
    # 5. Parse response.json() and return results
    #
    # Return format:
    # {
    #     "success": True/False,
    #     "data": [...products...],
    #     "count": number_of_results,
    #     "error": None or "error message"
    # }
    
    raise NotImplementedError("Exercise 2.3: Implement the S/4HANA API call")


if __name__ == "__main__":
    # Run with stdio transport for local communication
    mcp.run(transport="stdio")
