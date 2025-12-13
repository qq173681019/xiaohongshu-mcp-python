"""
一键启动和测试 AI Social Scheduler
"""
import subprocess
import time
import requests
import json
import sys
from pathlib import Path

# 切换到正确的目录
project_dir = Path(__file__).parent
import os
os.chdir(project_dir)

print("\n" + "="*50)
print("  AI Social Scheduler - 一键启动测试")
print("="*50 + "\n")

# 启动服务
print("🚀 启动服务...")
service_process = subprocess.Popen(
    ["uv", "run", "python", "run.py"],
    cwd=project_dir,
    env={**os.environ, "PYTHONIOENCODING": "utf-8"}
)

print("⏳ 等待服务启动 (15秒)...")
time.sleep(15)

# 测试API
print("\n📡 测试API...")
try:
    response = requests.post(
        "http://localhost:8012/api/v1/chat",
        json={"message": "你好，介绍一下你自己", "thread_id": None},
        timeout=30
    )
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ 成功！\n")
        print("AI回复:", data.get("response", ""))
        print("\n线程ID:", data.get("thread_id", ""))
        print("\n元数据:", json.dumps(data.get("metadata", {}), indent=2, ensure_ascii=False))
    else:
        print(f"\n❌ 错误: HTTP {response.status_code}")
        print(response.text)
        
except Exception as e:
    print(f"\n❌ 测试失败: {e}")
    
finally:
    print("\n\n🛑 按 Ctrl+C 停止服务，或直接关闭窗口")
    try:
        service_process.wait()
    except KeyboardInterrupt:
        print("\n正在停止服务...")
        service_process.terminate()
        service_process.wait()
        print("已停止")
