"""
小红书登录脚本
"""
import asyncio
import sys
from pathlib import Path

# 添加 src 目录到 Python 路径
src_path = Path(__file__).parent / "src"
sys.path.append(str(src_path))

from xiaohongshu_mcp_python.managers.user_session_manager import UserSessionManager
from xiaohongshu_mcp_python.config import settings

async def login():
    print("\n========================================")
    print("  小红书扫码登录工具")
    print("========================================\n")
    print("正在启动浏览器...")
    print("请在弹出的浏览器窗口中扫码登录小红书")
    
    # 强制使用有头模式
    manager = UserSessionManager()
    
    try:
        # 创建新会话（强制有头模式）
        result = await manager.get_or_create_session(
            username=settings.GLOBAL_USER,
            headless=False,  # 必须显示浏览器
            wait_for_completion=True  # 等待登录完成
        )
        
        if result.get("status") == "logged_in":
            print("\n✅ 登录成功！")
            print(f"Cookies 已保存为用户: {settings.GLOBAL_USER}")
            print("现在你可以运行自动化任务了。")
        else:
            print(f"\n❌ 登录失败: {result.get('message')}")
            
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")

if __name__ == "__main__":
    asyncio.run(login())
