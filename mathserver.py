from mcp.server.fastmcp import FastMCP
import math

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int) -> int:

    return a + b

@mcp.tool()
def multiply(a:int, b:int) -> int:

    return a*b

@mcp.tool()
def divide(a:int, b:int) -> float:

    return a/b

@mcp.tool()
def square(a:int) -> int:

    return a*a

@mcp.tool()
def cube(a:int) -> int:

    return a*a*a

@mcp.tool()
def square_root(a:int) -> float:

    return math.sqrt(a)

@mcp.tool()
def factorial(a:int) -> int:

    if a < 0:
        raise ValueError("Negative factorial not allowed")
    return math.factorial(a)

if __name__ == "__main__":
    mcp.run(mcp.run(transport="stdio"))