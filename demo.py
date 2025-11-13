#!/usr/bin/env python3
"""
Demo script to verify upgraded Python dependencies.
Tests basic functionality of: numpy, pandas, scipy, requests, PyYAML, matplotlib, Pillow
"""

import sys
import io
from io import StringIO

# Handle Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def test_numpy():
    """Test numpy functionality"""
    print("✓ Testing numpy...")
    import numpy as np
    
    # Create arrays
    arr = np.array([1, 2, 3, 4, 5])
    assert arr.sum() == 15, "NumPy sum failed"
    assert np.mean(arr) == 3.0, "NumPy mean failed"
    
    # Matrix operations
    matrix = np.array([[1, 2], [3, 4]])
    assert matrix.shape == (2, 2), "NumPy shape failed"
    
    print(f"  - numpy version: {np.__version__}")
    print(f"  - Array operations: PASS")
    return True

def test_pandas():
    """Test pandas functionality"""
    print("✓ Testing pandas...")
    import pandas as pd
    
    # Create DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': ['x', 'y', 'z']
    })
    
    assert df.shape == (3, 3), "DataFrame shape failed"
    assert df['A'].sum() == 6, "DataFrame sum failed"
    assert list(df['C']) == ['x', 'y', 'z'], "DataFrame column access failed"
    
    # Series operations
    series = pd.Series([10, 20, 30, 40, 50])
    assert series.mean() == 30, "Series mean failed"
    
    print(f"  - pandas version: {pd.__version__}")
    print(f"  - DataFrame operations: PASS")
    return True

def test_scipy():
    """Test scipy functionality"""
    print("✓ Testing scipy...")
    from scipy import stats
    import numpy as np
    
    # Statistical operations
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    mean = np.mean(data)
    std = np.std(data)
    assert abs(mean - 5.0) < 0.001, "SciPy mean failed"
    
    # Correlation
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    corr = stats.pearsonr(x, y)
    assert abs(corr[0] - 1.0) < 0.001, "SciPy correlation failed"
    
    print(f"  - scipy version: {__import__('scipy').__version__}")
    print(f"  - Statistical operations: PASS")
    return True

def test_requests():
    """Test requests functionality"""
    print("✓ Testing requests...")
    import requests
    
    # Test that requests module loads and has expected attributes
    assert hasattr(requests, 'get'), "Requests missing GET method"
    assert hasattr(requests, 'post'), "Requests missing POST method"
    assert hasattr(requests, 'Session'), "Requests missing Session class"
    
    # Verify version security
    version = requests.__version__
    major, minor, patch = map(int, version.split('.')[:3])
    assert major >= 2 and minor >= 25, f"Requests version {version} may have vulnerabilities"
    
    print(f"  - requests version: {version}")
    print(f"  - Module structure: PASS")
    return True

def test_pyyaml():
    """Test PyYAML functionality"""
    print("✓ Testing PyYAML...")
    import yaml
    
    # Safe loading test
    yaml_string = """
    config:
      name: test
      values:
        - 1
        - 2
        - 3
    """
    data = yaml.safe_load(yaml_string)
    assert data['config']['name'] == 'test', "YAML parsing failed"
    assert data['config']['values'] == [1, 2, 3], "YAML list parsing failed"
    
    # Dumping test
    dumped = yaml.dump({'test': 'value'})
    assert 'test: value' in dumped, "YAML dumping failed"
    
    print(f"  - PyYAML version: {yaml.__version__}")
    print(f"  - YAML parsing operations: PASS")
    return True

def test_matplotlib():
    """Test matplotlib functionality (without display)"""
    print("✓ Testing matplotlib...")
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Create a simple plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Test Plot")
    
    # Save to buffer instead of displaying
    buf = StringIO()
    fig.savefig('test_plot.png', format='png')
    plt.close(fig)
    
    print(f"  - matplotlib version: {matplotlib.__version__}")
    print(f"  - Plot creation: PASS")
    return True

def test_pillow():
    """Test Pillow functionality"""
    print("✓ Testing Pillow...")
    from PIL import Image
    import numpy as np
    
    # Create a simple image
    img_array = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    img = Image.fromarray(img_array, 'RGB')
    
    assert img.size == (100, 100), "Image creation failed"
    assert img.mode == 'RGB', "Image mode failed"
    
    # Save and load test
    img.save('test_image.png')
    loaded_img = Image.open('test_image.png')
    assert loaded_img.size == img.size, "Image save/load failed"
    
    print(f"  - Pillow version: {Image.__version__ if hasattr(Image, '__version__') else __import__('PIL').__version__}")
    print(f"  - Image operations: PASS")
    return True

def main():
    """Run all tests"""
    print("=" * 60)
    print("Python Dependency Verification Demo")
    print("=" * 60)
    print()
    
    tests = [
        test_numpy,
        test_pandas,
        test_scipy,
        test_requests,
        test_pyyaml,
        test_matplotlib,
        test_pillow,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append((test.__name__, result))
        except Exception as e:
            print(f"  ✗ FAILED: {e}")
            results.append((test.__name__, False))
        print()
    
    # Summary
    print("=" * 60)
    print("Test Summary")
    print("=" * 60)
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print()
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All dependencies verified successfully!")
        return 0
    else:
        print("✗ Some tests failed. Please review the output above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
