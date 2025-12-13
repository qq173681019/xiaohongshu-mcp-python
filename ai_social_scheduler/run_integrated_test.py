"""一体化测试脚本 - 输出到文件"""
import subprocess
import time
import sys
from pathlib import Path

# 输出文件
output_file = Path(__file__).parent / "test_results.txt"

def log(msg):
    """写入日志"""
    with open(output_file, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)

# 清空输出文件
with open(output_file, "w", encoding="utf-8") as f:
    f.write("测试开始\n")
    f.write("="*60 + "\n")

log("\n1. 启动 API 服务...")

# 启动 API 服务 (后台)
import os
os.chdir(Path(__file__).parent)

server_proc = subprocess.Popen(
    [sys.executable, "-m", "ai_social_scheduler.api"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    encoding="utf-8"
)

log("等待服务启动...")
time.sleep(5)

log("\n2. 发送测试请求...")

# 发送请求
import requests
import json

try:
    response = requests.post(
        "http://localhost:8000/api/v1/chat",
        json={"message": "你好", "thread_id": "test-123"},
        timeout=30
    )
    log(f"状态码: {response.status_code}")
    log(f"响应: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
except Exception as e:
    log(f"请求失败: {e}")

log("\n3. 检查错误日志...")

# 等待错误写入
time.sleep(2)

# 读取错误文件
error_file = Path(__file__).parent / "router_error.txt"
if error_file.exists():
    with open(error_file, "r", encoding="utf-8") as f:
        content = f.read()
        if content.strip():
            log("\n" + "="*60)
            log("发现Router错误:")
            log("="*60)
            log(content)
        else:
            log("router_error.txt 文件为空")
else:
    log("未发现 router_error.txt - 可能没有错误")

log("\n4. 停止服务...")
server_proc.terminate()
server_proc.wait(timeout=5)

log("\n测试完成!")
log(f"\n结果已保存到: {output_file}")
