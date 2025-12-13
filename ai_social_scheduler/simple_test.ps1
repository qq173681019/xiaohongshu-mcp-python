# Simple test - start and test
Write-Host "Starting service..." -ForegroundColor Green
Set-Location "c:\Users\admin\Documents\GitHub\xiaohongshu-mcp-python\ai_social_scheduler"
$env:PYTHONIOENCODING = "utf-8"

$job = Start-Job -ScriptBlock {
    Set-Location "c:\Users\admin\Documents\GitHub\xiaohongshu-mcp-python\ai_social_scheduler"
    $env:PYTHONIOENCODING = "utf-8"
    & ".venv\Scripts\python.exe" run.py 2>&1
}

Write-Host "Waiting..." -ForegroundColor Yellow
Start-Sleep -Seconds 6

Write-Host "Job output:" -ForegroundColor Cyan
Receive-Job $job

Write-Host "`nTesting..." -ForegroundColor Cyan
try {
    $response = Invoke-RestMethod -Uri "http://localhost:8012/api/v1/chat" -Method Post -Body '{"message":"你好"}' -ContentType "application/json" -TimeoutSec 10
    Write-Host "Success: $($response.response)" -ForegroundColor Green
} catch {
    Write-Host "Failed: $_" -ForegroundColor Red
}

Write-Host "`nLogs:" -ForegroundColor Yellow
if (Test-Path "router_error.txt") { Get-Content "router_error.txt" -Tail 20 }

Stop-Job $job -ErrorAction SilentlyContinue
Remove-Job $job -Force -ErrorAction SilentlyContinue
