"""查看服务器日志的脚本"""
import httpx
import time

print("=" * 60)
print("触发请求并等待服务器处理...")
print("=" * 60)

# 发送请求
try:
    response = httpx.post(
        "http://localhost:8012/api/v1/chat",
        json={"message": "你好"},
        timeout=30
    )
    print(f"\n状态码: {response.status_code}")
    print(f"响应: {response.json()}")
    print("\n请查看服务器终端的日志输出，应该能看到详细的错误信息")
except Exception as e:
    print(f"错误: {e}")
