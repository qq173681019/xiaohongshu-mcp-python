"""完整测试流程"""
import asyncio
import httpx

async def full_test():
    """完整测试"""
    url = "http://localhost:8012/api/v1/chat"
    
    print("=" * 60)
    print("完整测试流程")
    print("=" * 60)
    
    test_messages = [
        "你好",
        "帮我写一篇关于冬日穿搭的小红书",
    ]
    
    thread_id = None
    
    for i, msg in enumerate(test_messages, 1):
        print(f"\n测试 {i}: {msg}")
        print("-" * 60)
        
        payload = {"message": msg}
        if thread_id:
            payload["thread_id"] = thread_id
        
        try:
            async with httpx.AsyncClient(timeout=60) as client:
                response = await client.post(url, json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"✅ 成功 (状态码: {response.status_code})")
                    print(f"   AI 回复: {data['response']}")
                    print(f"   对话ID: {data['thread_id']}")
                    print(f"   消息数: {data['message_count']}")
                    thread_id = data['thread_id']
                else:
                    print(f"❌ 失败 (状态码: {response.status_code})")
                    print(f"   响应: {response.text}")
        except Exception as e:
            print(f"❌ 异常: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(full_test())
