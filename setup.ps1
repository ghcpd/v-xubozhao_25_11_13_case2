Write-Host "Creating virtual environment and installing requirements..."
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Write-Host "Environment setup completed. Activate with: .\\.venv\\Scripts\\Activate.ps1"