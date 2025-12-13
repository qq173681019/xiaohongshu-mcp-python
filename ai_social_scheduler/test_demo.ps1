# AI Social Scheduler 测试脚本
Write-Host "`n╔════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║        AI Social Scheduler - API 测试               ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════╝`n" -ForegroundColor Cyan

$baseUrl = "http://localhost:8012/api/v1/chat"

# 测试 1: 问候
Write-Host "【测试 1】发送问候消息 '你好'..." -ForegroundColor Yellow
try {
    $body1 = @{
        message = "你好"
        thread_id = "demo-$(Get-Date -Format 'HHmmss')"
    } | ConvertTo-Json -Compress
    
    $response1 = Invoke-RestMethod -Uri $baseUrl -Method Post -Body $body1 -ContentType "application/json" -TimeoutSec 30
    
    Write-Host "✅ 成功！" -ForegroundColor Green
    Write-Host "`n📝 AI 回复:" -ForegroundColor Cyan
    Write-Host $response1.response -ForegroundColor White
    Write-Host "`n📊 会话信息:" -ForegroundColor Gray
    Write-Host "  Thread ID: $($response1.thread_id)" -ForegroundColor Gray
    Write-Host "  消息数: $($response1.message_count)" -ForegroundColor Gray
    
    $threadId = $response1.thread_id
    
    # 测试 2: 生成内容
    Write-Host "`n----------------------------------------" -ForegroundColor Gray
    Write-Host "【测试 2】请求生成小红书内容..." -ForegroundColor Yellow
    
    $body2 = @{
        message = "帮我写一篇关于冬日穿搭的小红书"
        thread_id = $threadId
    } | ConvertTo-Json -Compress
    
    $response2 = Invoke-RestMethod -Uri $baseUrl -Method Post -Body $body2 -ContentType "application/json" -TimeoutSec 60
    
    Write-Host "✅ 成功！" -ForegroundColor Green
    Write-Host "`n📝 AI 回复（前300字符）:" -ForegroundColor Cyan
    $preview = $response2.response.Substring(0, [Math]::Min(300, $response2.response.Length))
    Write-Host "$preview..." -ForegroundColor White
    Write-Host "`n📊 会话信息:" -ForegroundColor Gray
    Write-Host "  消息数: $($response2.message_count)" -ForegroundColor Gray
    Write-Host "  完整内容长度: $($response2.response.Length) 字符" -ForegroundColor Gray
    
} catch {
    Write-Host "❌ 失败: $_" -ForegroundColor Red
    Write-Host "请确保服务正在运行 (运行 start_service.ps1)" -ForegroundColor Yellow
}

Write-Host "`n╚════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host "测试完成！" -ForegroundColor Green
