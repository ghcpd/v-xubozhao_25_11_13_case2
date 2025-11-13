#!/usr/bin/env bash
set -euo pipefail

LOG_DIR=logs
mkdir -p "$LOG_DIR"

if [ ! -d .venv ]; then
    echo "Virtualenv not found, creating..."
    python -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python demo.py | tee "$LOG_DIR/demo.log"

if [ ${PIPESTATUS[0]} -ne 0 ]; then
    echo "Demo failed. Check $LOG_DIR/demo.log for details." >&2
    exit 1
fi

echo "Tests completed successfully. Logs: $LOG_DIR/demo.log"
