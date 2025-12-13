# PowerShell test script
$ErrorActionPreference = "Continue"

Write-Host "杀死旧的Python进程..." -ForegroundColor Yellow
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue

Write-Host "清空旧的日志文件..." -ForegroundColor Yellow
"" | Out-File -FilePath "api_debug.txt" -Encoding utf8
"" | Out-File -FilePath "router_error.txt" -Encoding utf8

Write-Host "启动API服务..." -ForegroundColor Green
Set-Location "c:\Users\admin\Documents\GitHub\xiaohongshu-mcp-python\ai_social_scheduler"
$env:PYTHONIOENCODING = "utf-8"

# 启动服务（后台）
$job = Start-Job -ScriptBlock {
    Set-Location "c:\Users\admin\Documents\GitHub\xiaohongshu-mcp-python\ai_social_scheduler"
    $env:PYTHONIOENCODING = "utf-8"
    & uv run python -m ai_social_scheduler.api
}

Write-Host "等待服务启动..." -ForegroundColor Yellow
Start-Sleep -Seconds 8

Write-Host "发送测试请求..." -ForegroundColor Green
try {
    $body = @{
        message = "你好"
        thread_id = "test-123"
    } | ConvertTo-Json -Compress
    
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/v1/chat" `
        -Method POST `
        -Body $body `
        -ContentType "application/json" `
        -UseBasicParsing `
        -TimeoutSec 30
    
    Write-Host "状态码: $($response.StatusCode)" -ForegroundColor Green
    Write-Host "响应:" -ForegroundColor Green
    $response.Content | ConvertFrom-Json | ConvertTo-Json -Depth 10
} catch {
    Write-Host "请求失败: $_" -ForegroundColor Red
}

Write-Host "`n等待日志写入..." -ForegroundColor Yellow
Start-Sleep -Seconds 2

Write-Host "`n检查API调试日志..." -ForegroundColor Cyan
if (Test-Path "api_debug.txt") {
    Write-Host "=== API Debug Log ===" -ForegroundColor Cyan
    Get-Content "api_debug.txt"
} else {
    Write-Host "未找到 api_debug.txt" -ForegroundColor Yellow
}

Write-Host "`n检查Router错误日志..." -ForegroundColor Cyan
if (Test-Path "router_error.txt") {
    $content = Get-Content "router_error.txt" -Raw
    if ($content.Trim()) {
        Write-Host "=== Router Error Log ===" -ForegroundColor Red
        Write-Host $content
    } else {
        Write-Host "router_error.txt 为空 - 没有错误" -ForegroundColor Green
    }
} else {
    Write-Host "未找到 router_error.txt - 没有错误发生" -ForegroundColor Green
}

Write-Host "`n停止服务..." -ForegroundColor Yellow
Stop-Job $job -ErrorAction SilentlyContinue
Remove-Job $job -Force -ErrorAction SilentlyContinue
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue

Write-Host "`n测试完成!" -ForegroundColor Green
