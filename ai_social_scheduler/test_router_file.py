"""测试脚本 - 输出到文件"""
import asyncio
import sys
from pathlib import Path

# 重定向输出到文件
output_file = Path(__file__).parent / "test_output.txt"
sys.stdout = open(output_file, "w", encoding="utf-8")
sys.stderr = sys.stdout

sys.path.insert(0, str(Path(__file__).parent / "src"))

from ai_social_scheduler.agents.router import RouterAgent
from ai_social_scheduler.core.state import AgentState
from langchain_core.messages import HumanMessage

async def test_router():
    """测试 Router Agent"""
    print("=" * 60)
    print("测试 Router Agent - 使用 __call__ 方法")
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
        # 使用 __call__ 方法
        result = await router(state)
        print(f"\n✅ 执行成功!")
        print(f"   结果类型: {type(result)}")
        print(f"   结果keys: {result.keys() if isinstance(result, dict) else 'N/A'}")
        if 'decision' in result:
            print(f"   决策: {result['decision']}")
        if 'messages' in result and result['messages']:
            print(f"   AI 回复: {result['messages'][-1].content}")
    except Exception as e:
        print(f"\n❌ 执行失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_router())
    print("\n输出已保存到 test_output.txt")
