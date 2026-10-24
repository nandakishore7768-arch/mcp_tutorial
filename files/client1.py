import os
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters, client 
import asyncio

#path to the mcp server 
mcp_server_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "server1.py")

server_params = StdioServerParameters(
    command = "python",
    args = [str(mcp_server_script)],
    env = {}
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            
            result = await session.call_tool("process", arguments={"path" : "Path/to/the/file"})
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
