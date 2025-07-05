from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Greetings")

@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    print("Greetings tool is running...")
    print("Use the greet function to send greetings.")