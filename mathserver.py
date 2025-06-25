from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int) -> int:
    """
    Add two numbers a and b
    """
    return a + b

@mcp.tool()
def multiply(a:int, b:int) -> int:
    """
    Multiply two numbers a and b
    """
    return a*b

@mcp.tool()
def divide(a:int, b:int) -> float:
    """
    Divide two numbers a and b
    """
    return a/b

@mcp.tool()
def square(a:int) -> int:
    """
    Calculate square of given number a
    """
    return a*a

@mcp.tool()
def cube(a:int) -> int:
    """
    Calculate cube of given number a
    """
    return a*a*a

if __name__ == "__main__":
    mcp.run(transport='stdio')