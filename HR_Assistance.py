from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from LLM.HuggingFaceModel import model
import streamlit as st

import asyncio

st.header("HR Assistant")

async def main():
    client = MultiServerMCPClient(
        {
            'Employee' : {
                'command' : "python3",
                'args' : ['Z_Employee_MCP.py'],
                'transport' : 'stdio'
            },
            'HR Policy' : {
                'command' : "python3",
                'args' : ['Z_HR_Policy.py'],
                'transport' : 'stdio'
            }
        }
    )

    all_tools = await client.get_tools()

    agent = create_react_agent(model,all_tools)

    query = st.text_input("Enter Here ")

    button = st.button("Send")

    if button:

        response = await agent.ainvoke({
            # "messages" : [{"role" : "user",'content' : "Add new Employee name as Jaydev Patel, department as QA and salary as 50,000"}]
            "messages" : [{"role" : "user",'content' : query}]
        })

        print(response['messages'][-1].content)
        ai_response = response['messages'][-1].content
        st.write(ai_response)

if __name__ == "__main__":
    asyncio.run(main())



