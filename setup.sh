#!/bin/bash
# Setup script for Python dependency installation
# Creates virtual environment and installs upgraded dependencies

set -e  # Exit on error

echo "========================================"
echo "Python Dependency Setup Script"
echo "========================================"
echo ""

# Detect OS and Python
PYTHON_CMD="python3"
if command -v python &> /dev/null; then
    PYTHON_CMD="python"
fi

echo "✓ Using Python: $PYTHON_CMD"
$PYTHON_CMD --version
echo ""

# Create virtual environment
echo "✓ Creating virtual environment..."
if [ -d "venv" ]; then
    echo "  Virtual environment already exists, skipping creation."
else
    $PYTHON_CMD -m venv venv
    echo "  Virtual environment created."
fi
echo ""

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate
echo "  Virtual environment activated."
echo ""

# Upgrade pip
echo "✓ Upgrading pip, setuptools, and wheel..."
pip install --upgrade pip setuptools wheel
echo ""

# Install dependencies
echo "✓ Installing dependencies from requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "  Dependencies installed successfully."
else
    echo "✗ ERROR: requirements.txt not found!"
    exit 1
fi
echo ""

# Verify installation
echo "✓ Verifying installation..."
pip list
echo ""

echo "========================================"
echo "✓ Setup completed successfully!"
echo "========================================"
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run the demo, execute:"
echo "  python demo.py"
echo ""
