# Complete Demo Script
$ErrorActionPreference = "Continue"

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  AI Social Scheduler - DEMO" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Set-Location "c:\Users\admin\Documents\GitHub\xiaohongshu-mcp-python\ai_social_scheduler"
$env:PYTHONIOENCODING = "utf-8"

# Start service in background job
Write-Host "[1/3] Starting service..." -ForegroundColor Yellow
$job = Start-Job -ScriptBlock {
    Set-Location "c:\Users\admin\Documents\GitHub\xiaohongshu-mcp-python\ai_social_scheduler"
    $env:PYTHONIOENCODING = "utf-8"
    & uv run python run.py 2>&1
}

Write-Host "[2/3] Waiting for startup (8 seconds)..." -ForegroundColor Yellow
Start-Sleep -Seconds 8

Write-Host "[3/3] Testing API...`n" -ForegroundColor Yellow

# Test 1
Write-Host "Test 1: Hello" -ForegroundColor Cyan
Write-Host "----------------------------------------" -ForegroundColor Gray
try {
    $response1 = Invoke-RestMethod -Uri "http://localhost:8012/api/v1/chat" `
        -Method Post `
        -Body '{"message":"你好"}' `
        -ContentType "application/json" `
        -TimeoutSec 30
    
    Write-Host "SUCCESS!" -ForegroundColor Green
    Write-Host "Response: $($response1.response)" -ForegroundColor White
    Write-Host "Thread ID: $($response1.thread_id)" -ForegroundColor Gray
    
    $threadId = $response1.thread_id
    
    # Test 2
    Write-Host "`nTest 2: Generate Content" -ForegroundColor Cyan
    Write-Host "----------------------------------------" -ForegroundColor Gray
    
    $response2 = Invoke-RestMethod -Uri "http://localhost:8012/api/v1/chat" `
        -Method Post `
        -Body "{`"message`":`"帮我写一篇关于冬日穿搭的小红书`",`"thread_id`":`"$threadId`"}" `
        -ContentType "application/json" `
        -TimeoutSec 60
    
    Write-Host "SUCCESS!" -ForegroundColor Green
    $preview = $response2.response.Substring(0, [Math]::Min(200, $response2.response.Length))
    Write-Host "Response (first 200 chars): $preview..." -ForegroundColor White
    Write-Host "Full length: $($response2.response.Length) chars" -ForegroundColor Gray
    
} catch {
    Write-Host "FAILED: $_" -ForegroundColor Red
    Write-Host "Error details:" -ForegroundColor Yellow
    Write-Host $_.Exception.Message -ForegroundColor Red
}

# Show server logs
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Server Logs (last 20 lines):" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Receive-Job $job -Keep 2>&1 | Select-Object -Last 20 | ForEach-Object { Write-Host $_ }

# Cleanup
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Stopping service..." -ForegroundColor Yellow
Stop-Job $job -ErrorAction SilentlyContinue
Remove-Job $job -Force -ErrorAction SilentlyContinue

Write-Host "Demo complete!" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan
