from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio 

async def main():
    json_config = {
        "data_fetch_mcp" : {
            "transport" : "streamable-http",
            "url" : "http://localhost:8050/mcp"
        }
    }

    client = MultiServerMCPClient(json_config)

    tools = await client.get_tools()
    print(tools)

if __name__ == "__main__":
    asyncio.run(main())


