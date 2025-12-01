# auto_activate.ps1
$venvPath = "venv"
if (Test-Path $venvPath) {
    & "$venvPath\Scripts\Activate.ps1"
} else {
    Write-Host "Venv not found at: $venvPath" -ForegroundColor Red
}
