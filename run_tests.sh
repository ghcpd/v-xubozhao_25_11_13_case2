#!/usr/bin/env bash
# Run the demo and exit with the same code
set -euo pipefail

python demo.py | tee demo_output.log
