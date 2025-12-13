@echo off
cd /d "%~dp0xhs-content-generator-mcp"
set PYTHONPATH=%CD%\src
echo Starting XHS Content Generator MCP on port 8004...
echo.
uv run python -m xhs_content_generator_mcp.main 8004
pause
