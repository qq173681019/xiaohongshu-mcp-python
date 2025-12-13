#!/usr/bin/env pwsh
# Quick Start Script for AI Social Scheduler

Set-Location $PSScriptRoot
$env:PYTHONIOENCODING = "utf-8"

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  AI Social Scheduler - Quick Start" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting service on http://localhost:8012..." -ForegroundColor Green
Write-Host "Keep this window open!" -ForegroundColor Yellow
Write-Host ""

# Run the service
uv run python run.py
