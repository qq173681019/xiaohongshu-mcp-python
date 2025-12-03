#!/usr/bin/env python3
"""小红书自动化服务启动器"""

import subprocess
import time
import os
import sys
import requests
from pathlib import Path

def check_port(port):
    """检查端口是否可用"""
    try:
        response = requests.get(f"http://localhost:{port}", timeout=5)
        return True
    except:
        return False

def start_xiaohongshu_service():
    """启动小红书发布服务"""
    print("🚀 启动小红书发布服务...")
    
    base_dir = Path("C:/Users/ext.jgu/Documents/GitHub/xiaohongshu-mcp-python")
    xhs_dir = base_dir / "xhs-browser-automation-mcp"
    
    # 设置环境变量
    env = os.environ.copy()
    env['PYTHONPATH'] = str(xhs_dir / "src")
    env['WANT2I_API_KEY'] = "sk-17a3f073c8d3405bb1a2c9d8b159f250"
    
    # 启动命令
    cmd = [
        "uv", "run", "python", "-c",
        "import sys; sys.path.insert(0, 'src'); from xiaohongshu_mcp_python.main import main; main()"
    ]
    
    try:
        process = subprocess.Popen(
            cmd,
            cwd=str(xhs_dir),
            env=env,
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        print(f"   ✅ 小红书服务已启动 (PID: {process.pid})")
        return process
    except Exception as e:
        print(f"   ❌ 启动失败: {e}")
        return None

def start_image_service():
    """启动图像生成服务"""
    print("🎨 启动图像生成服务...")
    
    base_dir = Path("C:/Users/ext.jgu/Documents/GitHub/xiaohongshu-mcp-python")
    img_dir = base_dir / "image_video_mcp"
    
    # 设置环境变量
    env = os.environ.copy()
    env['WANT2I_API_KEY'] = "sk-17a3f073c8d3405bb1a2c9d8b159f250"
    
    # 启动命令
    cmd = ["uv", "run", "python", "-m", "image_video_mcp.main"]
    
    try:
        process = subprocess.Popen(
            cmd,
            cwd=str(img_dir),
            env=env,
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        print(f"   ✅ 图像服务已启动 (PID: {process.pid})")
        return process
    except Exception as e:
        print(f"   ❌ 启动失败: {e}")
        return None

def wait_for_services():
    """等待服务启动"""
    print("\n⏳ 等待服务启动...")
    
    for i in range(30):  # 等待30秒
        time.sleep(1)
        xhs_ok = check_port(8000)
        img_ok = check_port(8003)
        
        if xhs_ok and img_ok:
            print("✅ 所有服务启动成功!")
            return True
        elif i % 5 == 0:  # 每5秒显示一次进度
            print(f"   等待中... ({i+1}/30)")
    
    print("⚠️  服务启动超时")
    return False

def show_access_info():
    """显示访问信息"""
    print("\n" + "="*60)
    print("🌐 服务访问信息")
    print("="*60)
    
    print("小红书发布服务:")
    print("   URL: http://localhost:8000")
    print("   MCP: http://localhost:8000/mcp")
    
    print("\n图像生成服务:")
    print("   URL: http://localhost:8003")
    print("   MCP: http://localhost:8003/mcp")
    
    print("\n🔧 使用方法:")
    print("1. 在浏览器中打开上述URL查看服务状态")
    print("2. 运行 python xiaohongshu_usage_example.py 查看使用示例")
    print("3. 首次使用时会自动打开浏览器登录小红书")

def main():
    """主函数"""
    print("🎯 小红书自动化服务启动器")
    print("="*60)
    
    # 启动服务
    xhs_process = start_xiaohongshu_service()
    time.sleep(2)  # 稍等一下
    img_process = start_image_service()
    
    if xhs_process and img_process:
        # 等待服务启动完成
        if wait_for_services():
            show_access_info()
            
            print("\n🎉 启动完成!")
            print("按任意键退出启动器...")
            input()
        else:
            print("\n❌ 服务启动失败，请检查错误信息")
    else:
        print("\n❌ 无法启动服务，请检查配置")

if __name__ == "__main__":
    main()