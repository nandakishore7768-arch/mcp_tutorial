from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

async def main():
    json_file = {
        "data_fetch_mcp":{
            "transport" : "stdio",
            "command" : r"C:\Users\Nadakishore\Desktop\coding\concepts\mcp_tutorial\.venv\Scripts\python.exe",
            "args" : [r"C:\Users\Nadakishore\Desktop\coding\concepts\mcp_tutorial\files\server1.py"]
        }
    }

    client = MultiServerMCPClient(json_file)

    tools = await client.get_tools()
    print(tools)

if __name__ == "__main__":
    asyncio.run(main())