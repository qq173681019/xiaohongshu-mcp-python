"""简单演示脚本 - 启动服务并测试"""
import subprocess
import time
import requests
import json
from pathlib import Path

print("\n" + "="*60)
print("AI Social Scheduler - Demo")
print("="*60 + "\n")

# 启动服务
print("[1/3] Starting service...")
venv_python = Path(__file__).parent / ".venv" / "Scripts" / "python.exe"
run_script = Path(__file__).parent / "run.py"

server = subprocess.Popen(
    [str(venv_python), str(run_script)],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT
)

print("[2/3] Waiting 6 seconds...")
time.sleep(6)

print("[3/3] Testing API...\n")

url = "http://localhost:8012/api/v1/chat"

# Test 1
print("Test 1: Hello")
print("-" * 60)
try:
    r1 = requests.post(url, json={"message": "你好"}, timeout=30)
    data1 = r1.json()
    print(f"✓ SUCCESS!")
    print(f"  Response: {data1['response']}")
    print(f"  Thread ID: {data1['thread_id']}")
    
    thread_id = data1['thread_id']
    
    # Test 2
    print("\nTest 2: Generate Content")
    print("-" * 60)
    r2 = requests.post(
        url,
        json={"message": "帮我写一篇关于冬日穿搭的小红书", "thread_id": thread_id},
        timeout=60
    )
    data2 = r2.json()
    print(f"✓ SUCCESS!")
    preview = data2['response'][:200]
    print(f"  Response (first 200 chars): {preview}...")
    print(f"  Full length: {len(data2['response'])} chars")
    
except Exception as e:
    print(f"✗ FAILED: {e}")

# Stop service
print("\n" + "="*60)
print("Stopping service...")
server.terminate()
server.wait(timeout=5)

print("Demo complete!")
print("="*60 + "\n")
