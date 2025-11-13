import sys
import os

print("Demo: verify imports and basic functionality")

# Numpy
try:
    import numpy as np
    a = np.array([1, 2, 3])
    print("numpy:", np.__version__, "mean:", float(np.mean(a)))
except Exception as e:
    print("numpy import/test failed:", e)

# Pandas
try:
    import pandas as pd
    df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    print("pandas:", pd.__version__, "df shape:", df.shape)
except Exception as e:
    print("pandas import/test failed:", e)

# SciPy
try:
    import scipy
    from scipy import stats
    print("scipy:", scipy.__version__)
    r = stats.describe([1, 2, 3, 4])
    print("scipy.stats describe nobs:", r.nobs)
except Exception as e:
    print("scipy import/test failed:", e)

# requests
try:
    import requests
    print("requests:", requests.__version__)
    try:
        r = requests.get("https://httpbin.org/get", timeout=5)
        print("requests: httpbin status", r.status_code)
    except Exception as e:
        print("requests: network test skipped or failed -", e)
except Exception as e:
    print("requests import/test failed:", e)

# PyYAML
try:
    import yaml
    print("PyYAML:", yaml.__version__)
    s = """
    a: 1
    b: [1, 2, 3]
    """
    data = yaml.safe_load(s)
    print("yaml safe_load keys:", list(data.keys()))
except Exception as e:
    print("PyYAML import/test failed:", e)

# matplotlib
try:
    import matplotlib
    import matplotlib.pyplot as plt
    print("matplotlib:", matplotlib.__version__)
    fig = plt.figure()
    plt.plot([0,1,2], [0,1,4])
    out = os.path.join(os.getcwd(), "demo_plot.png")
    fig.savefig(out)
    print("matplotlib: saved plot to", out)
    plt.close(fig)
except Exception as e:
    print("matplotlib import/test failed:", e)

# Pillow
try:
    from PIL import Image
    print("Pillow:", Image.__version__)
    img = Image.new("RGB", (16, 16), color=(255, 0, 0))
    out = os.path.join(os.getcwd(), "demo_image.png")
    img.save(out)
    print("Pillow: created image", out)
except Exception as e:
    print("Pillow import/test failed:", e)

print("Demo finished. Python:", sys.version)
