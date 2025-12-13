"""最终测试 - 验证修复"""
import asyncio
from pathlib import Path
import sys

# 添加路径
sys.path.insert(0, str(Path(__file__).parent / "src"))

from ai_social_scheduler.agents.router import RouterAgent
from ai_social_scheduler.core.state import AgentState
from langchain_core.messages import HumanMessage

async def test_router():
    """测试 Router Agent"""
    print("=" * 60)
    print("测试 DeepSeek JSON 解析（无 response_format）")
    print("=" * 60)
    
    # 创建 Router Agent
    router = RouterAgent(
        llm_model="deepseek-chat",
        temperature=0.3
    )
    
    # 测试状态
    state: AgentState = {
        "messages": [HumanMessage(content="你好")],
    }
    
    print("\n测试消息: 你好")
    print("\n正在调用...")
    
    try:
        # 使用 __call__ 方法（就像 LangGraph 调用）
        result = await router(state)
        print(f"\n✅ 成功!")
        print(f"决策: {result.get('decision')}")
        print(f"响应: {result.get('messages', [])[-1].content if result.get('messages') else 'None'}")
        return True
    except Exception as e:
        print(f"\n❌ 失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_router())
    sys.exit(0 if success else 1)
