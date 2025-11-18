if (Test-Path "venv\Scripts\Activate.ps1") {
    Write-Host "Активирую виртуальное окружение..." -ForegroundColor Green
    & "venv\Scripts\Activate.ps1"
}
else {
    Write-Host "Виртуальное окружение не найдено" -ForegroundColor Red
}