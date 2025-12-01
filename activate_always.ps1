# Принудительная активация venv
$venvPath = Join-Path $PSScriptRoot "venv"
if (Test-Path $venvPath) {
    & "$venvPath\Scripts\Activate.ps1"
}
