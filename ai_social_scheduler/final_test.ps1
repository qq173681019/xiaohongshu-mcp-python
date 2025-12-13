# XHS Note Publishing Test
$tid=$null
Write-Host "`n[1/3] Greeting" -ForegroundColor Yellow
$r1=Invoke-RestMethod -Uri "http://localhost:8012/api/v1/chat" -Method Post -Body (@{message="Hello";thread_id=$null}|ConvertTo-Json) -ContentType "application/json" -TimeoutSec 60
Write-Host "Success: $($r1.response)" -ForegroundColor Green
$tid=$r1.thread_id
Start-Sleep 2

Write-Host "`n[2/3] Generating note..." -ForegroundColor Yellow
$r2=Invoke-RestMethod -Uri "http://localhost:8012/api/v1/chat" -Method Post -Body (@{message="Write a Xiaohongshu note about winter skincare";thread_id=$tid}|ConvertTo-Json) -ContentType "application/json" -TimeoutSec 90
Write-Host "Success: Generated" -ForegroundColor Green
Start-Sleep 2

Write-Host "`n[3/3] Publishing..." -ForegroundColor Yellow
$r3=Invoke-RestMethod -Uri "http://localhost:8012/api/v1/chat" -Method Post -Body (@{message="Publish this note";thread_id=$tid}|ConvertTo-Json) -ContentType "application/json" -TimeoutSec 90
Write-Host "Success: $($r3.response)" -ForegroundColor Green
Write-Host "`nDone! Thread ID: $tid`n" -ForegroundColor Cyan
