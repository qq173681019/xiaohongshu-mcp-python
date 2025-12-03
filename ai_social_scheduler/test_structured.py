"""测试 DeepSeek 是否支持结构化输出"""
import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

class TestOutput(BaseModel):
    """测试输出"""
    name: str = Field(description="名字")
    age: int = Field(description="年龄")

async def test_structured_output():
    """测试结构化输出"""
    print("=" * 60)
    print("测试 DeepSeek 结构化输出支持")
    print("=" * 60)
    
    # 创建客户端
    llm = ChatOpenAI(
        model="deepseek-chat",
        openai_api_key="sk-bdd85ba18ab54a699617d8b25fbecfea",
        base_url="https://api.deepseek.com/v1",
        temperature=0.7
    )
    
    print("\n测试 1: 普通调用")
    try:
        response = await llm.ainvoke([HumanMessage(content="你好")])
        print(f"✅ 成功: {response.content[:50]}")
    except Exception as e:
        print(f"❌ 失败: {e}")
    
    print("\n测试 2: 结构化输出")
    try:
        structured_llm = llm.with_structured_output(TestOutput)
        response = await structured_llm.ainvoke([
            HumanMessage(content="返回一个人的信息，名字是张三，年龄是25")
        ])
        print(f"✅ 成功: {response}")
    except Exception as e:
        print(f"❌ 失败: {e}")
        print(f"\n这意味着 DeepSeek 不支持 function calling/structured output")
        print(f"需要改用 JSON mode 或纯文本解析")

if __name__ == "__main__":
    asyncio.run(test_structured_output())
