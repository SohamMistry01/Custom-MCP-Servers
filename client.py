from langchain_groq import  ChatGroq 
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():

    client = MultiServerMCPClient(
        {
            "Math" : {
                "command":"python",
                "args":["mathserver.py"], # Absolute path of the MCP server
                "transport":"stdio"
            }
        }
    )

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    tools = await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b")
    agent = create_react_agent(model, tools)
    user_input = input("Ask any mathematical equation: ")

    math_response = await agent.ainvoke(
        {"messages":[{"role":"user", "content":f"Solve {user_input}."}]}
    )
    
    print("Math response: ", math_response['messages'][-1].content)

asyncio.run(main())