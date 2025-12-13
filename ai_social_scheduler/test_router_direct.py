"""直接测试 Router Agent"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from ai_social_scheduler.agents.router import RouterAgent
from ai_social_scheduler.core.state import AgentState
from langchain_core.messages import HumanMessage

async def test_router():
    """测试 Router Agent"""
    print("=" * 60)
    print("测试 Router Agent 直接调用")
    print("=" * 60)
    
    # 创建 Router Agent
    router = RouterAgent(
        llm_model="deepseek-chat",
        temperature=0.3
    )
    
    # 创建测试状态
    state: AgentState = {
        "messages": [HumanMessage(content="你好")],
    }
    
    print("\n测试输入: 你好")
    print("\n正在调用 Router Agent...")
    
    try:
        # 使用 __call__ 方法，就像 LangGraph 那样调用
        result = await router(state)
        print(f"\n✅ 执行成功!")
        print(f"   决策: {result.get('decision')}")
        print(f"   AI 回复: {result.get('messages', [])[-1].content if result.get('messages') else 'None'}")
    except Exception as e:
        print(f"\n❌ 执行失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_router())
