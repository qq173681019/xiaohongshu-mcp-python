"""
发布小红书笔记 - 完整示例
"""
import requests
import json
import time

API_BASE = "http://localhost:8012/api/v1"

def send_message(message, thread_id=None):
    """发送消息到AI"""
    print(f"\n{'='*70}")
    print(f"👤 你说: {message}")
    print(f"{'='*70}")
    
    response = requests.post(
        f"{API_BASE}/chat",
        json={"message": message, "thread_id": thread_id},
        timeout=60
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n🤖 AI回复:\n{data.get('response', '')}")
        
        # 显示关键信息
        metadata = data.get('metadata', {})
        if metadata:
            print(f"\n📌 意图: {metadata.get('intent')}")
            print(f"📌 下一步: {metadata.get('next_agent')}")
            
            params = metadata.get('extracted_params', {})
            if params:
                print(f"📌 提取信息: {json.dumps(params, ensure_ascii=False, indent=2)}")
        
        return data.get('thread_id'), data
    else:
        print(f"❌ 错误: {response.status_code} - {response.text}")
        return None, None


print("""
╔══════════════════════════════════════════════════════════╗
║       小红书笔记发布助手 - 使用指南                      ║
╚══════════════════════════════════════════════════════════╝

你可以这样说：

📝 生成笔记：
   • "帮我写一篇关于秋天穿搭的小红书"
   • "生成一篇冬季护肤的笔记"
   • "创作一篇美食探店的内容"

🚀 发布笔记：
   • "发布这篇笔记"
   • "帮我发到小红书"
   • "立即发布"

📊 查询状态：
   • "发布成功了吗？"
   • "笔记状态如何？"
   • "查看发布结果"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

print("现在开始对话（输入 'quit' 退出）:\n")

thread_id = None

while True:
    user_input = input("\n👤 你: ").strip()
    
    if user_input.lower() in ['quit', 'exit', '退出', 'q']:
        print("\n👋 再见！")
        break
    
    if not user_input:
        continue
    
    thread_id, result = send_message(user_input, thread_id)
    
    # 如果返回了任务信息，显示详细内容
    if result and 'task_context' in result.get('metadata', {}):
        task = result['metadata']['task_context']
        print(f"\n📋 任务信息:")
        print(f"   状态: {task.get('status')}")
        print(f"   类型: {task.get('task_type')}")
