from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def fetch():
    """ returns data """
    return {"data" : "data"}

@mcp.tool()
def process(path: str):
    """ returns processed data """
    return {"processed_data" : "processed_data " + path}

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host = "localhost", port = 8050)