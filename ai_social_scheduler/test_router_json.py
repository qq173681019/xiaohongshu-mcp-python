"""测试 Router Agent 的 JSON 解析"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from ai_social_scheduler.client.llm.qwen_client import QwenClient
from langchain_core.messages import HumanMessage, SystemMessage

ROUTER_SYSTEM_PROMPT = """你是一个智能路由助手，负责分析用户意图并决定下一步行动。

## 你的职责
1. 理解用户的请求意图
2. 决定是否需要调用专业 Agent
3. 生成友好的回复

## 可用的 Agent
- **xhs_agent**: 小红书内容生成专家
  - 触发关键词：小红书、笔记、发布、生成内容、写一篇等

## 决策规则
1. **xhs_agent**: 当用户想要创建、生成或发布小红书内容时
2. **wait**: 当需要用户提供更多信息或等待用户输入时
3. **end**: 当对话可以自然结束时（如用户说再见、完成任务等）

## 输出格式
**重要：你必须只返回纯 JSON，不要有任何其他文本或解释。**

JSON 格式：
{
  "next_agent": "xhs_agent" | "wait" | "end",
  "intent": "create_content" | "query_status" | "get_help" | "casual_chat" | "feedback",
  "reasoning": "决策理由",
  "response": "给用户的回复",
  "extracted_params": {},
  "confidence": 0.0-1.0
}

示例 - 用户: "你好"
{"next_agent": "wait", "intent": "casual_chat", "reasoning": "用户打招呼", "response": "你好！我可以帮你生成小红书内容。", "extracted_params": {}, "confidence": 1.0}
"""

async def test_router_json():
    """测试 Router JSON 输出"""
    print("=" * 60)
    print("测试 Router Agent JSON 解析")
    print("=" * 60)
    
    client = QwenClient(
        api_key="sk-bdd85ba18ab54a699617d8b25fbecfea",
        endpoint="https://api.deepseek.com/v1",
        model="deepseek-chat",
        temperature=0.3
    )
    
    messages = [
        SystemMessage(content=ROUTER_SYSTEM_PROMPT),
        HumanMessage(content="你好")
    ]
    
    print("\n发送消息: 你好")
    print("\n等待 DeepSeek 响应...")
    
    response = await client.generate(messages)
    print(f"\n原始响应:\n{response}\n")
    
    # 尝试解析
    import json
    import re
    
    json_match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
        print(f"提取的 JSON (从代码块):\n{json_str}\n")
    else:
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        json_str = json_match.group(0) if json_match else response
        print(f"提取的 JSON (直接匹配):\n{json_str}\n")
    
    try:
        data = json.loads(json_str)
        print(f"✅ JSON 解析成功!")
        print(f"   next_agent: {data.get('next_agent')}")
        print(f"   intent: {data.get('intent')}")
        print(f"   response: {data.get('response')}")
    except Exception as e:
        print(f"❌ JSON 解析失败: {e}")

if __name__ == "__main__":
    asyncio.run(test_router_json())
