import sys
import platform

print(f"Python: {platform.python_version()} ({sys.executable})")

packages = {
    'numpy': 'np',
    'pandas': 'pd',
    'scipy': 'scipy',
    'requests': 'requests',
    'yaml': 'yaml',
    'matplotlib': 'matplotlib',
    'PIL': 'PIL'
}

# Import and show versions
import importlib

for pkg_name, alias in packages.items():
    try:
        mod = importlib.import_module(pkg_name if pkg_name != 'PIL' else 'PIL')
        version = getattr(mod, '__version__', None) or getattr(mod, 'VERSION', 'unknown')
        print(f"Imported {pkg_name}: version {version}")
    except Exception as e:
        print(f"Failed to import {pkg_name}: {e}")

# Small functional checks
print('\nFunctional checks:')
try:
    import numpy as np
    arr = np.arange(10)
    print('numpy test: sum(arr)=', int(np.sum(arr)))
except Exception as exc:
    print('numpy test failed:', exc)

try:
    import pandas as pd
    df = pd.DataFrame({'x': [1,2,3]})
    print('pandas test: df.mean() ->', df.mean().to_dict())
except Exception as exc:
    print('pandas test failed:', exc)

try:
    from scipy import linalg
    import numpy as np
    mat = np.array([[1,2],[3,4]])
    print('scipy test: det(mat)=', float(linalg.det(mat)))
except Exception as exc:
    print('scipy test failed:', exc)

try:
    import requests
    resp = requests.get('https://httpbin.org/get', timeout=5)
    print('requests test: status_code=', resp.status_code)
except Exception as exc:
    print('requests test failed (network may be limited):', exc)

try:
    import yaml
    y = yaml.safe_load("{a: 1}")
    print('yaml test: safe_load ->', y)
except Exception as exc:
    print('yaml test failed:', exc)

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    x = [1,2,3,4]
    y = [i*i for i in x]
    plt.plot(x, y)
    plt.savefig('demo_plot.png')
    print('matplotlib test: saved demo_plot.png')
except Exception as exc:
    print('matplotlib test failed:', exc)

try:
    from PIL import Image
    img = Image.new('RGB', (64, 64), color='blue')
    img.save('demo_image.png')
    print('Pillow test: saved demo_image.png')
except Exception as exc:
    print('Pillow test failed:', exc)

print('\nDemo finished')
