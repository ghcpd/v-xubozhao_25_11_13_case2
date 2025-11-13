#!/usr/bin/env bash
set -euo pipefail

# This script creates a virtualenv and installs dependencies from requirements.txt
python -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Environment setup completed. Activate with: source .venv/bin/activate or .\.venv\Scripts\Activate (Windows)."
