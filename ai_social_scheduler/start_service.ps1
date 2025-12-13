# AI Social Scheduler Start Script
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  AI Social Scheduler - Starting..." -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Set-Location "c:\Users\admin\Documents\GitHub\xiaohongshu-mcp-python\ai_social_scheduler"
$env:PYTHONIOENCODING = "utf-8"

Write-Host "Working Directory: $(Get-Location)" -ForegroundColor Yellow
Write-Host "Service URL: http://localhost:8012" -ForegroundColor Green
Write-Host "Keep this window open!`n" -ForegroundColor Gray

Write-Host "Starting service..." -ForegroundColor Cyan

& uv run python run.py
