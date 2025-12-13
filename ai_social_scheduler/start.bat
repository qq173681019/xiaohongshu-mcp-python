@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo.
echo ========================================
echo   AI Social Scheduler - Starting
echo ========================================
echo.
echo Service URL: http://localhost:8012
echo.
set PYTHONIOENCODING=utf-8
uv run python run.py
pause
