import subprocess
import sys
import importlib
import os


def test_basic_imports():
    # Import lightweight modules and check versions
    import numpy as np
    import pandas as pd
    import requests
    import yaml
    from PIL import Image

    assert hasattr(np, '__version__') and len(np.__version__) > 0
    assert hasattr(pd, '__version__') and len(pd.__version__) > 0
    assert hasattr(requests, '__version__') and len(requests.__version__) > 0
    assert hasattr(yaml, '__version__') or hasattr(yaml, 'VERSION')
    assert hasattr(Image, 'new')


def test_numpy_function():
    import numpy as np
    arr = np.arange(10)
    assert int(np.sum(arr)) == 45


def test_run_demo_script(tmp_path):
    # Run the demo.py script using the current Python executable and ensure it completes
    python_exec = sys.executable
    result = subprocess.run([python_exec, 'demo.py'], cwd=os.getcwd(), capture_output=True, text=True, timeout=30)
    assert result.returncode == 0, f"demo.py failed: stdout: {result.stdout}\nstderr: {result.stderr}"
    assert 'Demo finished' in result.stdout
