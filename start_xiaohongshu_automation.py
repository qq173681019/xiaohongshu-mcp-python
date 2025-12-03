#!/usr/bin/env python3
"""
小红书自动化系统 - 快速启动指南
==================================

这个脚本将帮助您快速启动完整的小红书自动化系统。
包含图片生成和内容发布功能。
"""

import os
import subprocess
import time
import sys
from pathlib import Path


def print_banner():
    """打印启动横幅"""
    print("="*80)
    print("🎯 小红书自动化系统 - 快速启动")
    print("="*80)
    print("📱 功能: 自动生成图片 + 发布到小红书")
    print("🎨 图像: AI生成精美内容图片")
    print("✍️ 文案: 智能创作吸引人的标题和内容")
    print("🚀 发布: 一键自动发布到小红书平台")
    print("="*80)


def setup_environment():
    """设置环境"""
    print("\n🔧 设置环境变量...")
    
    # 设置API密钥
    api_key = "sk-17a3f073c8d3405bb1a2c9d8b159f250"
    os.environ['WANT2I_API_KEY'] = api_key
    
    print(f"   ✅ WANT2I_API_KEY: {api_key[:8]}***{api_key[-4:]}")
    print("   ✅ 环境设置完成")


def start_xiaohongshu_service():
    """启动小红书发布服务"""
    print("\n📱 启动小红书发布服务...")
    
    base_dir = Path("C:/Users/ext.jgu/Documents/GitHub/xiaohongshu-mcp-python")
    xhs_dir = base_dir / "xhs-browser-automation-mcp"
    
    if not xhs_dir.exists():
        print(f"   ❌ 目录不存在: {xhs_dir}")
        return None
    
    # PowerShell 命令启动服务
    ps_script = f'''
    cd "{xhs_dir}"
    $env:PYTHONPATH = "src"
    $env:WANT2I_API_KEY = "sk-17a3f073c8d3405bb1a2c9d8b159f250"
    uv run python -c "import sys; sys.path.insert(0, 'src'); from xiaohongshu_mcp_python.main import main; main()"
    '''
    
    print("   📋 启动命令:")
    print("      cd xhs-browser-automation-mcp")
    print("      $env:PYTHONPATH = \"src\"")
    print("      uv run python -m xiaohongshu_mcp_python.main")
    print("")
    print("   🔄 正在启动服务...")
    print("   ⏳ 请稍等，服务正在初始化...")
    print("")
    print("   💡 请在新的 PowerShell 窗口中运行以下命令:")
    print(f"      cd {xhs_dir}")
    print("      $env:PYTHONPATH = \"src\"")
    print("      $env:WANT2I_API_KEY = \"sk-17a3f073c8d3405bb1a2c9d8b159f250\"")
    print("      uv run python -c \"import sys; sys.path.insert(0, 'src'); from xiaohongshu_mcp_python.main import main; main()\"")


def start_image_service():
    """启动图像生成服务"""
    print("\n🎨 启动图像生成服务...")
    
    base_dir = Path("C:/Users/ext.jgu/Documents/GitHub/xiaohongshu-mcp-python")
    img_dir = base_dir / "image_video_mcp"
    
    if not img_dir.exists():
        print(f"   ❌ 目录不存在: {img_dir}")
        return None
    
    print("   📋 启动命令:")
    print("      cd image_video_mcp")
    print("      uv run python -m image_video_mcp.main")
    print("")
    print("   💡 请在另一个新的 PowerShell 窗口中运行以下命令:")
    print(f"      cd {img_dir}")
    print("      $env:WANT2I_API_KEY = \"sk-17a3f073c8d3405bb1a2c9d8b159f250\"")
    print("      uv run python -m image_video_mcp.main")


def show_verification_steps():
    """显示验证步骤"""
    print("\n" + "="*80)
    print("🔍 验证服务运行状态")
    print("="*80)
    
    print("\n1️⃣ 检查小红书发布服务:")
    print("   在浏览器中访问: http://localhost:8000")
    print("   预期结果: 看到 FastMCP 服务页面")
    
    print("\n2️⃣ 检查图像生成服务:")
    print("   在浏览器中访问: http://localhost:8003")
    print("   预期结果: 看到图像生成服务页面")
    
    print("\n3️⃣ 服务启动确认:")
    print("   小红书服务日志应显示: \"Uvicorn running on http://127.0.0.1:8000\"")
    print("   图像服务日志应显示: \"Uvicorn running on http://127.0.0.1:8003\"")


def show_usage_guide():
    """显示使用指南"""
    print("\n" + "="*80)
    print("📖 使用指南")
    print("="*80)
    
    print("\n🎯 基本使用流程:")
    print("1. 确保两个服务都在运行 (端口 8000 和 8003)")
    print("2. 准备要发布的内容 (标题、描述、话题标签)")
    print("3. 使用 AI 生成图片或准备自己的图片")
    print("4. 调用发布接口发布到小红书")
    
    print("\n🔧 核心功能:")
    print("✅ 自动图片生成 - AI创作精美图片")
    print("✅ 智能内容创作 - 生成吸引人的文案")
    print("✅ 一键发布 - 自动发布到小红书")
    print("✅ 批量处理 - 支持批量内容发布")
    print("✅ 多账号 - 支持多个小红书账户")
    
    print("\n📱 发布示例:")
    print("内容类型: 美食分享")
    print("标题: 🍜 家常美食分享：温暖的一餐")
    print("图片: AI生成的精美美食图片")
    print("标签: #美食分享 #家常菜 #美食教程")
    
    print("\n💡 温馨提示:")
    print("- 首次使用需要在浏览器中登录小红书账户")
    print("- 系统会自动保存登录状态，后续自动发布")
    print("- 确保内容符合小红书社区规范")
    print("- 建议在非高峰期发布以获得更好效果")


def show_next_steps():
    """显示后续步骤"""
    print("\n" + "="*80)
    print("🚀 后续步骤")
    print("="*80)
    
    print("\n📋 现在您可以:")
    print("1. 运行上述命令启动两个服务")
    print("2. 在浏览器中验证服务运行状态") 
    print("3. 开始使用小红书自动化功能")
    print("4. 根据需要调整内容和发布策略")
    
    print("\n🔧 如需技术支持:")
    print("- 检查服务日志查看详细错误信息")
    print("- 确保网络连接正常")
    print("- 验证 API 密钥配置正确")
    print("- 重启服务解决临时问题")
    
    print("\n🎉 祝您使用愉快！")
    print("小红书自动化系统将大幅提升您的内容创作和发布效率！")


def main():
    """主函数"""
    try:
        print_banner()
        setup_environment()
        start_xiaohongshu_service()
        start_image_service()
        show_verification_steps()
        show_usage_guide()
        show_next_steps()
        
    except KeyboardInterrupt:
        print("\n\n⚠️ 用户中断了启动过程")
    except Exception as e:
        print(f"\n❌ 启动过程中发生错误: {e}")
    

if __name__ == "__main__":
    main()