# 小红书自动化系统 - 完整一键启动脚本
# 启动所有4个服务

$ErrorActionPreference = "Continue"

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Xiaohongshu Automation System - Full Start" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Starting the following services:" -ForegroundColor Yellow
Write-Host "  1. XHS Content Generator (Port 8004)" -ForegroundColor White
Write-Host "  2. Image/Video Generator (Port 8003)" -ForegroundColor White
Write-Host "  3. Browser Automation (Port 8000)" -ForegroundColor White
Write-Host "  4. AI Social Scheduler (Port 8012)" -ForegroundColor White
Write-Host "`n========================================`n" -ForegroundColor Cyan

$baseDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Service 1: XHS Content Generator MCP
Write-Host "[1/4] Starting XHS Content Generator..." -ForegroundColor Yellow
$contentGenDir = Join-Path $baseDir "xhs-content-generator-mcp"
Start-Process powershell -ArgumentList "-NoExit", "-Command", @"
Set-Location '$contentGenDir'
`$env:PYTHONPATH = Join-Path '$contentGenDir' 'src'
Write-Host 'XHS Content Generator MCP (Port 8004)' -ForegroundColor Green
uv run python -m xhs_content_generator_mcp.main 8004
"@
Start-Sleep -Seconds 5

# Service 2: Image/Video MCP
Write-Host "[2/4] Starting Image/Video Generator..." -ForegroundColor Yellow
$imageDir = Join-Path $baseDir "image_video_mcp"
Start-Process powershell -ArgumentList "-NoExit", "-Command", @"
Set-Location '$imageDir'
Write-Host 'Image/Video MCP (Port 8003)' -ForegroundColor Green
uv run python -m image_video_mcp.main --port 8003
"@
Start-Sleep -Seconds 3

# Service 3: Browser Automation MCP
Write-Host "[3/4] Starting Browser Automation..." -ForegroundColor Yellow
$browserDir = Join-Path $baseDir "xhs-browser-automation-mcp"
Start-Process powershell -ArgumentList "-NoExit", "-Command", @"
Set-Location '$browserDir'
Write-Host 'Browser Automation MCP (Port 8000)' -ForegroundColor Green
uv run python -m xiaohongshu_mcp_python.main --port 8000
"@
Start-Sleep -Seconds 3

# Service 4: AI Social Scheduler
Write-Host "[4/4] Starting AI Social Scheduler..." -ForegroundColor Yellow
$schedulerDir = Join-Path $baseDir "ai_social_scheduler"
Start-Process powershell -ArgumentList "-NoExit", "-Command", @"
Set-Location '$schedulerDir'
Write-Host 'AI Social Scheduler (Port 8012)' -ForegroundColor Green
uv run python run.py
"@
Start-Sleep -Seconds 3

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "  ✅ All services started!" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Green

Write-Host "Service List:" -ForegroundColor Cyan
Write-Host "  • XHS Content Generator: http://localhost:8004" -ForegroundColor White
Write-Host "  • Image/Video Generator: http://localhost:8003" -ForegroundColor White
Write-Host "  • Browser Automation:    http://localhost:8000" -ForegroundColor White
Write-Host "  • AI Social Scheduler:   http://localhost:8012" -ForegroundColor White

Write-Host "`n📝 Quick Test:" -ForegroundColor Cyan
Write-Host "  cd ai_social_scheduler" -ForegroundColor White
Write-Host "  uv run python quick_xhs_test.py" -ForegroundColor White

Write-Host "`n📚 API Docs:" -ForegroundColor Cyan
Write-Host "  http://localhost:8012/docs" -ForegroundColor White

Write-Host "`n⚠️  Please keep the 4 new windows open`n" -ForegroundColor Yellow

Write-Host "Press Enter to close this launcher..." -ForegroundColor Gray
Read-Host
