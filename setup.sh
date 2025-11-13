#!/usr/bin/env bash
# Purpose: Install updated dependencies and keep the environment reproducible
set -euo pipefail

# Use python command available in PATH
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

# Verify installed versions
python - <<'PY'
import importlib
pkgs = ['numpy','pandas','scipy','requests','yaml','matplotlib','PIL']
for p in pkgs:
    try:
        mod = importlib.import_module(p if p != 'PIL' else 'PIL')
        v = getattr(mod, '__version__', None) or getattr(mod, 'VERSION', None) or 'unknown'
        print(f"{p}: {v}")
    except Exception as e:
        print(f"{p}: not installed or failed import -> {e}")
PY
