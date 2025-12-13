"""
启动XHS Content Generator MCP服务
"""
import subprocess
import sys
from pathlib import Path

print("\n" + "="*60)
print("  XHS Content Generator MCP - 启动中...")
print("="*60 + "\n")

mcp_dir = Path(__file__).parent / "xhs-content-generator-mcp"

print(f"工作目录: {mcp_dir}")
print(f"端口: 8004")
print(f"访问: http://localhost:8004\n")

try:
    subprocess.run(
        ["uv", "run", "--python", "3.11", "python", "-m", "xhs_content_generator_mcp.main", "8004"],
        cwd=str(mcp_dir),
        check=True
    )
except KeyboardInterrupt:
    print("\n\n服务已停止")
except Exception as e:
    print(f"\n启动失败: {e}")
    print("\n可能的原因:")
    print("  1. 依赖未安装 - 运行: cd xhs-content-generator-mcp && uv sync")
    print("  2. Python版本不对 - 需要Python 3.11+")
    sys.exit(1)
