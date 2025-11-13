$LogDir = "logs"
if (-not (Test-Path -Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir | Out-Null }

if (-not (Test-Path -Path ".venv")) {
    Write-Host "Virtualenv not found, creating..."
    python -m venv .venv
}

. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python demo.py 2>&1 | Tee-Object -FilePath "$LogDir\demo.log"
if ($LASTEXITCODE -ne 0) { Write-Error "Demo failed. Check $LogDir\demo.log for details."; exit 1 }
Write-Host "Tests completed successfully. Logs: $LogDir\demo.log"