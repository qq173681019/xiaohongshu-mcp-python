"""直接测试 QwenClient 与 DeepSeek"""
import asyncio
import sys
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent / "src"))

from ai_social_scheduler.client.llm.qwen_client import QwenClient
from langchain_core.messages import HumanMessage

async def test_qwen_client():
    """测试 QwenClient"""
    print("=" * 60)
    print("测试 QwenClient 与 DeepSeek API")
    print("=" * 60)
    
    # 创建客户端
    try:
        client = QwenClient(
            api_key="sk-bdd85ba18ab54a699617d8b25fbecfea",
            endpoint="https://api.deepseek.com/v1",
            model="deepseek-chat",
            temperature=0.7
        )
        print(f"✅ 客户端创建成功")
        print(f"   模型: {client.model}")
        print(f"   endpoint: {client.endpoint}")
        print(f"   api_key: {client.api_key[:20]}...")
        
        # 测试生成
        print("\n测试生成文本...")
        messages = [HumanMessage(content="你好，请用一句话介绍自己")]
        response = await client.generate(messages)
        print(f"\n✅ 生成成功！")
        print(f"   回复: {response}")
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_qwen_client())
