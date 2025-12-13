"""
小红书自动化系统 - 一键启动所有服务
启动4个服务:
1. XHS Content Generator MCP (端口 8004) - 内容生成
2. Image/Video MCP (端口 8003) - 图片生成
3. Xiaohongshu Browser MCP (端口 8000) - 浏览器自动化
4. AI Social Scheduler (端口 8012) - 主服务API
"""
import subprocess
import sys
import time
from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).parent

# 服务配置
SERVICES = [
    {
        "name": "XHS Content Generator MCP",
        "port": 8004,
        "cwd": BASE_DIR / "xhs-content-generator-mcp",
        "command": ["cmd", "/k", "uv", "run", "--python", "3.11", "python", "-m", "xhs_content_generator_mcp.main", "8004"],
        "env": {"PYTHONPATH": str(BASE_DIR / "xhs-content-generator-mcp" / "src")},
    },
    {
        "name": "Image/Video MCP",
        "port": 8003,
        "cwd": BASE_DIR / "image_video_mcp",
        "command": ["cmd", "/k", "uv", "run", "python", "-m", "image_video_mcp.main", "--port", "8003"],
        "env": {"PYTHONPATH": str(BASE_DIR / "image_video_mcp" / "src")},
    },
    {
        "name": "Xiaohongshu Browser MCP",
        "port": 8000,
        "cwd": BASE_DIR / "xhs-browser-automation-mcp",
        "command": ["cmd", "/k", "uv", "run", "python", "-m", "xiaohongshu_mcp_python.main", "--port", "8000"],
        "env": {"PYTHONPATH": str(BASE_DIR / "xhs-browser-automation-mcp" / "src")},
    },
    {
        "name": "AI Social Scheduler",
        "port": 8012,
        "cwd": BASE_DIR / "ai_social_scheduler",
        "command": ["cmd", "/k", "uv", "run", "python", "run.py"],
        "env": {"PYTHONIOENCODING": "utf-8"},
    },
]

def print_banner():
    """打印启动横幅"""
    print("\n" + "="*70)
    print("  小红书自动化系统 - 一键启动脚本")
    print("="*70 + "\n")

def start_service(service):
    """启动单个服务"""
    name = service["name"]
    port = service["port"]
    cwd = service["cwd"]
    command = service["command"]
    env = service.get("env", {})
    
    print(f"[启动] {name} (端口 {port})...")
    print(f"  目录: {cwd}")
    print(f"  命令: {' '.join(command)}")
    
    # 合并环境变量
    import os
    full_env = os.environ.copy()
    full_env.update(env)
    
    try:
        # Windows: CREATE_NEW_CONSOLE 标志
        if sys.platform == "win32":
            process = subprocess.Popen(
                command,
                cwd=str(cwd),
                env=full_env,
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            # Linux/Mac: 在后台运行
            process = subprocess.Popen(
                command,
                cwd=str(cwd),
                env=full_env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        
        print(f"  ✓ 已启动 (PID: {process.pid})\n")
        return process
        
    except Exception as e:
        print(f"  ✗ 启动失败: {e}\n")
        return None

def main():
    """主函数"""
    print_banner()
    
    print("正在启动所有服务...\n")
    
    processes = []
    
    for i, service in enumerate(SERVICES, 1):
        print(f"[{i}/{len(SERVICES)}] ", end="")
        process = start_service(service)
        
        if process:
            processes.append({
                "name": service["name"],
                "port": service["port"],
                "process": process
            })
        
        # 等待服务启动
        if i < len(SERVICES):
            print("  等待服务初始化...")
            time.sleep(5 if i == 1 else 3)
    
    # 显示服务状态
    print("\n" + "="*70)
    print("  服务启动完成！")
    print("="*70 + "\n")
    
    print("运行中的服务:\n")
    for svc in processes:
        print(f"  ✓ {svc['name']:<30} http://localhost:{svc['port']}")
    
    print("\n" + "="*70)
    print("  使用指南")
    print("="*70 + "\n")
    print("1. 测试服务:")
    print("   cd ai_social_scheduler")
    print("   uv run python quick_xhs_test.py")
    print()
    print("2. API文档:")
    print("   http://localhost:8012/docs")
    print()
    print("3. 关闭所有服务:")
    print("   关闭所有弹出的终端窗口")
    print("   或按 Ctrl+C 终止本脚本")
    print("\n" + "="*70 + "\n")
    
    # 保持脚本运行
    try:
        print("按 Ctrl+C 停止所有服务...\n")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n正在停止所有服务...")
        for svc in processes:
            try:
                svc["process"].terminate()
                print(f"  ✓ 已停止 {svc['name']}")
            except:
                pass
        print("\n所有服务已停止\n")

if __name__ == "__main__":
    main()
