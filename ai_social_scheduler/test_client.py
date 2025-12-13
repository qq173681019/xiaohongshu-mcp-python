"""简单的 API 客户端测试脚本"""
import requests
import json
import time

def test_api():
    url = "http://localhost:8000/api/v1/chat"
    
    payload = {
        "message": "你好",
        "thread_id": "test-123"
    }
    
    print(f"发送请求: {payload}")
    print(f"URL: {url}")
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        print(f"\n状态码: {response.status_code}")
        print(f"响应: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 等待一下，让错误写入文件
    time.sleep(1)
    
    # 读取错误文件
    try:
        with open("router_error.txt", "r", encoding="utf-8") as f:
            content = f.read()
            if content:
                print("\n" + "="*60)
                print("Router Error Log:")
                print("="*60)
                print(content)
    except FileNotFoundError:
        print("\n没有发现router_error.txt文件 - 可能没有错误发生")

if __name__ == "__main__":
    test_api()

