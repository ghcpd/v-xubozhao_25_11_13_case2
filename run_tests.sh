#!/bin/bash
# Test runner script - executes the demo.py verification script

set -e  # Exit on error

echo "========================================"
echo "Python Dependency Test Runner"
echo "========================================"
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "✗ Virtual environment not found!"
    echo "Please run setup.sh first:"
    echo "  bash setup.sh"
    exit 1
fi

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate
echo ""

# Show Python info
echo "✓ Python environment:"
which python
python --version
echo ""

# Show installed packages
echo "✓ Installed packages:"
pip list --format=columns | head -20
echo ""

# Run demo
echo "========================================"
echo "Running demo.py..."
echo "========================================"
echo ""

if [ -f "demo.py" ]; then
    python demo.py
    DEMO_EXIT_CODE=$?
else
    echo "✗ ERROR: demo.py not found!"
    exit 1
fi

echo ""
echo "========================================"
if [ $DEMO_EXIT_CODE -eq 0 ]; then
    echo "✓ All tests passed!"
    echo "========================================"
    exit 0
else
    echo "✗ Some tests failed!"
    echo "========================================"
    exit 1
fi
