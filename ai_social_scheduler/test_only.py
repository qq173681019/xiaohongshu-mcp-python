"""
仅测试API - 假设服务已在另一个窗口运行
"""
import requests
import json

print("\n" + "="*50)
print("  测试 AI Social Scheduler API")
print("="*50 + "\n")

print("📡 发送请求到 http://localhost:8012/api/v1/chat ...")

try:
    response = requests.post(
        "http://localhost:8012/api/v1/chat",
        json={"message": "你好，介绍一下你自己", "thread_id": None},
        timeout=30
    )
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ 成功！\n")
        print("="*50)
        print("AI回复:")
        print("-"*50)
        print(data.get("response", ""))
        print("="*50)
        print(f"\n线程ID: {data.get('thread_id', '')}")
        
        metadata = data.get("metadata", {})
        if metadata:
            print(f"\n元数据:")
            print(json.dumps(metadata, indent=2, ensure_ascii=False))
    else:
        print(f"\n❌ HTTP错误: {response.status_code}")
        print(response.text)
        
except requests.exceptions.ConnectionError:
    print("\n❌ 连接失败！")
    print("\n请确保:")
    print("1. 在另一个终端窗口中运行了服务")
    print("   命令: cd ai_social_scheduler; uv run python run.py")
    print("2. 服务显示 'Uvicorn running on http://0.0.0.0:8012'")
    
except requests.exceptions.Timeout:
    print("\n⏱️ 请求超时 (API响应时间较长，这是正常的)")
    print("建议等待30秒以上再试")
    
except Exception as e:
    print(f"\n❌ 错误: {e}")

print("\n")
