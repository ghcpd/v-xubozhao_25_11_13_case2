def test_imports():
    import numpy as np
    import pandas as pd
    import scipy
    import requests
    import yaml
    import matplotlib
    from PIL import Image

    assert np.__version__ != ""
    assert pd.__version__ != ""
    assert scipy.__version__ != ""
    assert requests.__version__ != ""
    assert yaml.__version__ != ""
    assert matplotlib.__version__ != ""
    assert Image.__version__ != ""


def test_numpy_mean():
    import numpy as np
    a = np.array([1, 2, 3])
    assert float(np.mean(a)) == 2.0
