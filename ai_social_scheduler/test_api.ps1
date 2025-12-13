# 测试 AI Social Scheduler API
# 请确保服务已经在另一个窗口运行 (运行 start.bat)

Write-Host "Testing AI Social Scheduler API..." -ForegroundColor Cyan
Write-Host ""

$body = @{
    message = "你好，介绍一下你自己"
    thread_id = $null
} | ConvertTo-Json -Depth 10

$headers = @{
    "Content-Type" = "application/json"
}

try {
    Write-Host "Sending request..." -ForegroundColor Yellow
    $response = Invoke-RestMethod -Uri "http://localhost:8012/api/v1/chat" -Method Post -Body $body -Headers $headers -TimeoutSec 30
    
    Write-Host ""
    Write-Host "✅ SUCCESS!" -ForegroundColor Green
    Write-Host ""
    Write-Host "AI Response:" -ForegroundColor Cyan
    Write-Host $response.response -ForegroundColor White
    Write-Host ""
    Write-Host "Thread ID:" -ForegroundColor Cyan
    Write-Host $response.thread_id -ForegroundColor White
    Write-Host ""
    Write-Host "Metadata:" -ForegroundColor Cyan
    Write-Host ($response.metadata | ConvertTo-Json -Depth 5) -ForegroundColor Gray
    
} catch {
    Write-Host ""
    Write-Host "❌ ERROR!" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
    Write-Host "请确保:" -ForegroundColor Yellow
    Write-Host "1. 服务正在运行 (在另一个窗口运行 start.bat)" -ForegroundColor White
    Write-Host "2. 端口 8012 未被占用" -ForegroundColor White
}

Write-Host "Stopping service..." -ForegroundColor Yellow
Stop-Job $job -ErrorAction SilentlyContinue
Remove-Job $job -Force -ErrorAction SilentlyContinue

Write-Host "=== Done ===" -ForegroundColor Cyan
