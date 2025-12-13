"""
小红书笔记发布 - 自动演示（无交互）
"""
import requests
import json
import time
import sys

API = "http://localhost:8012/api/v1/chat"

def chat(msg, tid=None):
    """发送聊天消息"""
    print(f"\n{'='*70}")
    print(f"💬 你: {msg}")
    print(f"{'='*70}")
    
    try:
        r = requests.post(API, json={"message": msg, "thread_id": tid}, timeout=60)
        
        if r.status_code == 200:
            d = r.json()
            print(f"\n🤖 AI回复:")
            print(f"{'-'*70}")
            print(d.get('response', ''))
            print(f"{'-'*70}")
            
            m = d.get('metadata', {})
            if m:
                print(f"\n📊 元数据:")
                print(f"   意图: {m.get('intent')}")
                print(f"   下一步: {m.get('next_agent')}")
                print(f"   置信度: {m.get('confidence')}")
            
            return d.get('thread_id'), d
        else:
            print(f"\n❌ HTTP错误: {r.status_code}")
            print(r.text)
            return None, None
            
    except requests.exceptions.ConnectionError:
        print(f"\n❌ 连接失败！请确保服务正在运行")
        print(f"   服务地址: {API}")
        return None, None
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        return None, None


def main():
    """主演示流程"""
    print("""
╔═══════════════════════════════════════════════════════════╗
║         🎯 小红书笔记发布 - 自动演示                      ║
╚═══════════════════════════════════════════════════════════╝

将演示:
  ✓ 生成笔记内容  
  ✓ 发布到小红书
  ✓ 查询发布状态

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)
    
    tid = None
    
    # 步骤1: 生成笔记
    print("\n【步骤 1/3】生成小红书笔记")
    print("━"*70)
    tid, result = chat("帮我写一篇关于冬季护肤的小红书笔记，要有吸引人的标题和emoji", tid)
    
    if not tid:
        print("\n❌ 演示失败，请检查服务状态")
        sys.exit(1)
    
    time.sleep(3)
    
    # 步骤2: 发布笔记
    print("\n\n【步骤 2/3】发布笔记到小红书")
    print("━"*70)
    tid, result = chat("发布这篇笔记", tid)
    
    time.sleep(3)
    
    # 步骤3: 查询状态
    print("\n\n【步骤 3/3】查询发布状态")
    print("━"*70)
    tid, result = chat("笔记发布成功了吗？", tid)
    
    # 完成
    print(f"""
\n{'='*70}
✅ 演示完成！
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
会话ID: {tid}
{'='*70}

💡 提示:
   - 你可以使用这个会话ID继续对话
   - 查看服务终端可以看到详细日志
   - API文档: http://localhost:8012/docs
    """)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 演示已取消")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
