"""XHS Test"""
import requests
import time

URL = "http://localhost:8012/api/v1/chat"
print("\n[1/3] Hello...")
r1 = requests.post(URL, json={"message": "Hello", "thread_id": None}, timeout=30)
tid = r1.json()['thread_id']
print(f"OK, ID: {tid}")

time.sleep(2)
print("\n[2/3] Generate...")
# DeepSeek 可能会比较慢，增加超时时间到 300 秒
r2 = requests.post(URL, json={"message": "Write about winter skincare", "thread_id": tid}, timeout=300)
print("OK")

time.sleep(2)
print("\n[3/3] Publish...")
r3 = requests.post(URL, json={"message": "Publish", "thread_id": tid}, timeout=300)
print(f"OK: {r3.json()['response']}\n")
