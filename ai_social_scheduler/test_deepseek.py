"""测试 DeepSeek 集成"""
import asyncio
import httpx

async def test_api():
    """测试 API"""
    url = "http://localhost:8012/api/v1/chat"
    
    # 测试1: 简单问候
    print("=" * 60)
    print("测试 1: 简单问候")
    print("=" * 60)
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            url,
            json={"message": "你好"}
        )
        data = response.json()
        print(f"状态码: {response.status_code}")
        print(f"回复: {data['response']}")
        print(f"对话ID: {data['thread_id']}")
        thread_id = data['thread_id']
    
    print("\n" + "=" * 60)
    print("测试 2: 请求生成小红书")
    print("=" * 60)
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            url,
            json={
                "message": "帮我写一篇关于冬日穿搭的小红书",
                "thread_id": thread_id
            }
        )
        data = response.json()
        print(f"状态码: {response.status_code}")
        print(f"回复: {data['response']}")
        print(f"消息数: {data['message_count']}")

if __name__ == "__main__":
    asyncio.run(test_api())
