"""
小红书笔记发布 - 完整演示
"""
import requests
import json
import time

API = "http://localhost:8012/api/v1/chat"

def chat(msg, tid=None):
    print(f"\n{'='*70}\n💬 你: {msg}\n{'='*70}")
    r = requests.post(API, json={"message": msg, "thread_id": tid}, timeout=60)
    if r.status_code == 200:
        d = r.json()
        print(f"\n🤖 AI:\n{'-'*70}\n{d.get('response')}\n{'-'*70}")
        m = d.get('metadata', {})
        if m:
            print(f"\n📊 意图:{m.get('intent')} | 下一步:{m.get('next_agent')} | 置信度:{m.get('confidence')}")
        return d.get('thread_id'), d
    print(f"❌ 错误: {r.status_code}")
    return None, None

print("""
╔═══════════════════════════════════════════════════════════╗
║         🎯 小红书笔记发布 - 自动演示                      ║
╚═══════════════════════════════════════════════════════════╝

将演示:
  ✓ 生成笔记内容  
  ✓ 发布到小红书
  ✓ 查询状态

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

input("确保服务正在运行，按 Enter 开始...")

tid = None

print("\n\n【步骤 1/3】生成笔记")
tid, _ = chat("帮我写一篇关于冬季护肤的小红书笔记，要有吸引人的标题和emoji", tid)
time.sleep(2)

print("\n\n【步骤 2/3】发布笔记")  
tid, _ = chat("发布这篇笔记", tid)
time.sleep(2)

print("\n\n【步骤 3/3】查询状态")
tid, _ = chat("发布成功了吗？", tid)

print(f"""
\n{'='*70}
✅ 演示完成！
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
会话ID: {tid}
{'='*70}
""")
