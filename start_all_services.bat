@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

echo.
echo ========================================
echo   小红书自动化系统 - 完整启动
echo ========================================
echo.
echo 将启动以下服务:
echo   1. XHS Content Generator (端口 8004)
echo   2. Image/Video Generator (端口 8003)
echo   3. Browser Automation (端口 8000)
echo   4. AI Social Scheduler (端口 8012)
echo.
echo ========================================
echo.

set "BASE_DIR=%~dp0"

:: 服务1: XHS Content Generator MCP
echo [1/4] 启动 XHS Content Generator...
cd /d "%BASE_DIR%xhs-content-generator-mcp"
set PYTHONPATH=%CD%\src
start "XHS Content Generator MCP" cmd /k "echo XHS Content Generator MCP (Port 8004) && uv run python -m xhs_content_generator_mcp.main 8004"
timeout /t 5 /nobreak > nul

:: 服务2: Image/Video MCP
echo [2/4] 启动 Image/Video Generator...
cd /d "%BASE_DIR%image_video_mcp"
start "Image Video MCP" cmd /k "echo Image/Video MCP (Port 8003) && uv run python -m image_video_mcp.main --port 8003"
timeout /t 3 /nobreak > nul

:: 服务3: Xiaohongshu Browser MCP
echo [3/4] 启动 Browser Automation...
cd /d "%BASE_DIR%xhs-browser-automation-mcp"
start "Xiaohongshu Browser MCP" cmd /k "echo Browser Automation MCP (Port 8000) && uv run python -m xiaohongshu_mcp_python.main --port 8000"
timeout /t 3 /nobreak > nul

:: 服务4: AI Social Scheduler
echo [4/4] 启动 AI Social Scheduler...
cd /d "%BASE_DIR%ai_social_scheduler"
start "AI Social Scheduler" cmd /k "echo AI Social Scheduler (Port 8012) && uv run python run.py"
timeout /t 3 /nobreak > nul

echo.
echo ========================================
echo   ✅ 所有服务已启动！
echo ========================================
echo.
echo 服务列表:
echo   • XHS Content Generator: http://localhost:8004
echo   • Image/Video Generator: http://localhost:8003
echo   • Browser Automation:    http://localhost:8000
echo   • AI Social Scheduler:   http://localhost:8012
echo.
echo 📝 快速测试:
echo   cd ai_social_scheduler
echo   uv run python quick_xhs_test.py
echo.
echo 📚 API文档:
echo   http://localhost:8012/docs
echo.
echo ⚠️  保持4个服务窗口开启运行
echo.
echo 按任意键关闭此启动器...
pause > nul
