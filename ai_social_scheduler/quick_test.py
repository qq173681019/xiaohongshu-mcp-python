"""快速测试脚本 - 启动并测试"""
import subprocess
import time
import requests
from pathlib import Path

print("="*60)
print("Quick Test - Starting service and testing immediately")
print("="*60)

# 启动服务
venv_python = Path(__file__).parent / ".venv" / "Scripts" / "python.exe"
run_script = Path(__file__).parent / "run.py"

print("\n[1/2] Starting service...")
server = subprocess.Popen(
    [str(venv_python), str(run_script)],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

print("[2/2] Waiting 10 seconds...")
time.sleep(10)

print("\nTesting API...")
print("-"*60)

url = "http://localhost:8012/api/v1/chat"

try:
    response = requests.post(
        url,
        json={"message": "你好"},
        timeout=40
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n✓ SUCCESS!")
        print(f"\nAI Response:")
        print(data['response'])
        print(f"\nThread ID: {data['thread_id']}")
        print(f"Message Count: {data['message_count']}")
    else:
        print(f"\n✗ FAILED - Status: {response.status_code}")
        print(response.text)
        
except Exception as e:
    print(f"\n✗ FAILED: {e}")

# 显示服务器日志
print("\n" + "="*60)
print("Server logs (last 30 lines):")
print("="*60)
try:
    output, _ = server.communicate(timeout=1)
except subprocess.TimeoutExpired:
    server.kill()
    output, _ = server.communicate()

for line in output.split('\n')[-30:]:
    if line.strip():
        print(line)

print("\n" + "="*60)
print("Test complete!")
print("="*60)
