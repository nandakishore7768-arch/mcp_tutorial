from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool(name = "fetch", description = "consist of returned data from the server")
def fetch():
    """ Returns data from the server side """
    return {"data" : "returned data"}

@mcp.tool(name = "process", description = "mcp tool to process files")
def process(path: str):
    """processes files and returns data"""

    return {"processed_data" : "file_content" + path}

if __name__ == "__main__":
    mcp.run(transport = "stdio")

