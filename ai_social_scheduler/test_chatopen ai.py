"""测试 ChatOpenAI 与 DeepSeek"""
import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

async def test():
    print("Testing ChatOpenAI with DeepSeek...")
    
    client = ChatOpenAI(
        model="deepseek-chat",
        openai_api_key="sk-bdd85ba18ab54a699617d8b25fbecfea",
        base_url="https://api.deepseek.com/v1",
        temperature=0.7
    )
    
    try:
        response = await client.ainvoke([HumanMessage(content="你好")])
        print(f"✓ SUCCESS!")
        print(f"Response: {response.content}")
    except Exception as e:
        print(f"✗ FAILED: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test())
