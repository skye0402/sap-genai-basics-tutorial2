"""
MCP Server with Calculator and S/4HANA Product API Tools - Complete Solution

This server exposes tools via the Model Context Protocol:

Calculator Tools:
- add: Add two numbers
- multiply: Multiply two numbers  
- subtract: Subtract two numbers
- divide: Divide two numbers

S/4HANA Product API Tools:
- get_product_api_documentation: Get API documentation for querying products
- query_products: Query S/4HANA Product Master API with OData parameters

Run with:
    uv run python mcp_server.py
"""

import os
from pathlib import Path

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables from parent directory
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# S/4HANA configuration
S4HANA_USER = os.getenv("S4HANA_USER", "")
S4HANA_PASSWORD = os.getenv("S4HANA_PASSWORD", "")
S4PRODUCT_ENDPOINT = os.getenv("S4PRODUCT_MASTER_ENDPOINT", "")

# Create an MCP server with a descriptive name
mcp = FastMCP("Calculator and S4HANA Server")


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


# =============================================================================
# S/4HANA Product API Tools
# =============================================================================

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
        search_text: Text to search for in product descriptions.
            Examples: "cat", "food", "battery", "LED"
        language: Language code for the description. Default "EN" for English.
            Common codes: EN (English), DE (German), JA (Japanese), 
            FR (French), ES (Spanish), ZH (Chinese), KO (Korean)
        top: Maximum number of results (default: 20)
    
    Returns:
        Dictionary with products matching the search text in their description.
        Each result includes Product ID, Language, and ProductDescription.
    """
    if not S4PRODUCT_ENDPOINT:
        return {
            "success": False,
            "error": "S4PRODUCT_MASTER_ENDPOINT not configured in .env",
            "data": [],
            "count": 0,
        }
    
    if not S4HANA_USER or not S4HANA_PASSWORD:
        return {
            "success": False,
            "error": "S4HANA_USER or S4HANA_PASSWORD not configured in .env",
            "data": [],
            "count": 0,
        }
    
    # Query the ProductDescription entity directly
    url = f"{S4PRODUCT_ENDPOINT.rstrip('/')}/ProductDescription"
    
    # Build filter: search text in description AND specific language.
    # NOTE: Backend does not support tolower(), so we rely on its collation for case handling.
    # Escape single quotes in search text for OData
    safe_search = search_text.replace("'", "''")
    filter_expr = f"contains(ProductDescription,'{safe_search}') and Language eq '{language.upper()}'"
    
    params = {
        "$filter": filter_expr,
        "$select": "Product,Language,ProductDescription",
        "$top": str(top),
        "$count": "true",
    }
    
    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.get(
                url,
                params=params,
                auth=(S4HANA_USER, S4HANA_PASSWORD),
                headers={"Accept": "application/json"},
            )
            
            if response.status_code == 200:
                data = response.json()
                results = data.get("value", [])
                total_count = data.get("@odata.count", len(results))
                
                return {
                    "success": True,
                    "data": results,
                    "count": len(results),
                    "total_available": total_count,
                    "search_info": {
                        "search_text": search_text,
                        "language": language.upper(),
                    },
                    "error": None,
                }
            else:
                return {
                    "success": False,
                    "error": f"API returned status {response.status_code}: {response.text[:500]}",
                    "data": [],
                    "count": 0,
                }
                
    except httpx.TimeoutException:
        return {
            "success": False,
            "error": "Request timed out.",
            "data": [],
            "count": 0,
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Request failed: {str(e)}",
            "data": [],
            "count": 0,
        }


@mcp.tool()
def get_product_api_documentation() -> str:
    """Get documentation for the S/4HANA Product Master API.
    
    Call this tool FIRST to understand how to query products from S/4HANA.
    The documentation explains:
    - Available OData query parameters ($filter, $select, $top, etc.)
    - How to search for products using contains(), startswith(), eq
    - Common fields and their meanings
    - Example queries
    
    Returns:
        Comprehensive API documentation as a string
    """
    from s4hana_product_api_docs import PRODUCT_API_DOCUMENTATION
    return PRODUCT_API_DOCUMENTATION


@mcp.tool()
def query_products(
    filter_expression: str = "",
    select_fields: str = "",
    top: int = 10,
    skip: int = 0,
    orderby: str = "",
    expand: str = "",
) -> dict:
    """Query the S/4HANA Product Master API with flexible OData parameters.
    
    CRITICAL: The 'Product' field is just a technical ID (like 'APJ123'), NOT the readable name!
    To get human-readable product names, you MUST use expand="_ProductDescription".
    
    Args:
        filter_expression: OData $filter - works on Product entity fields ONLY.
            - "startswith(Product,'APJ')" - Products with ID starting with 'APJ'
            - "ProductType eq 'FERT'" - Only finished products
            - NOTE: Cannot filter on _ProductDescription! Fetch and scan instead.
        select_fields: Comma-separated fields. Example: "Product,ProductType,BaseUnit"
        top: Max results (default: 10). Use 20-50 when searching by description.
        skip: Skip N results for pagination (default: 0)
        orderby: Sort field. Example: "Product asc" or "CreationDate desc"
        expand: IMPORTANT! Use "_ProductDescription" to get readable product names.
            Without this, you only get technical IDs, not product names!
    
    Returns:
        Dictionary with 'success', 'data' (products), 'count', 'error'.
        When expand="_ProductDescription", each product has _ProductDescription array
        with Language and ProductDescription (the actual readable name).
    
    Example for searching products by name (e.g., "cat food"):
        expand="_ProductDescription", top=30
        Then scan _ProductDescription[].ProductDescription for "cat"
    """
    if not S4PRODUCT_ENDPOINT:
        return {
            "success": False,
            "error": "S4PRODUCT_MASTER_ENDPOINT not configured in .env",
            "data": [],
            "count": 0,
        }
    
    if not S4HANA_USER or not S4HANA_PASSWORD:
        return {
            "success": False, 
            "error": "S4HANA_USER or S4HANA_PASSWORD not configured in .env",
            "data": [],
            "count": 0,
        }
    
    # Build the query URL
    url = f"{S4PRODUCT_ENDPOINT.rstrip('/')}/Product"
    
    # Build query parameters
    params = {}
    if filter_expression:
        params["$filter"] = filter_expression
    if select_fields:
        params["$select"] = select_fields
    if top:
        params["$top"] = str(top)
    if skip:
        params["$skip"] = str(skip)
    if orderby:
        params["$orderby"] = orderby
    if expand:
        params["$expand"] = expand
    
    # Always request count
    params["$count"] = "true"
    
    try:
        # Make the API request with Basic Auth
        with httpx.Client(timeout=30.0) as client:
            response = client.get(
                url,
                params=params,
                auth=(S4HANA_USER, S4HANA_PASSWORD),
                headers={"Accept": "application/json"},
            )
            
            if response.status_code == 200:
                data = response.json()
                products = data.get("value", [])
                total_count = data.get("@odata.count", len(products))
                
                return {
                    "success": True,
                    "data": products,
                    "count": len(products),
                    "total_available": total_count,
                    "query_used": {
                        "filter": filter_expression or "(none)",
                        "select": select_fields or "(all fields)",
                        "top": top,
                        "skip": skip,
                    },
                    "error": None,
                }
            else:
                return {
                    "success": False,
                    "error": f"API returned status {response.status_code}: {response.text[:500]}",
                    "data": [],
                    "count": 0,
                }
                
    except httpx.TimeoutException:
        return {
            "success": False,
            "error": "Request timed out. Try reducing $top or simplifying the filter.",
            "data": [],
            "count": 0,
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Request failed: {str(e)}",
            "data": [],
            "count": 0,
        }


if __name__ == "__main__":
    # Run with stdio transport for local communication
    # This is the standard way to run MCP servers that will be called by agents
    mcp.run(transport="stdio")
