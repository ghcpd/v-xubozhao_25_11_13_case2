import io
import numpy as np
import pandas as pd
from scipy import stats
import requests
import yaml
import matplotlib.pyplot as plt
from PIL import Image


def run_numpy_pandas_demo():
    arr = np.linspace(0, 9, 10)
    df = pd.DataFrame({"value": arr, "square": arr**2})
    stats_summary = df["square"].describe()
    print("Pandas DataFrame summary:\n", stats_summary.to_string())
    return df


def run_scipy_demo(arr):
    description = stats.describe(arr)
    print("SciPy describe result:", description)


def run_requests_demo():
    session = requests.Session()
    # Just create a session to confirm import and TLS stack works; uses no outbound calls.
    print("Requests session created successfully with headers:", session.headers["User-Agent"])


def run_pyyaml_demo():
    yaml_content = {"greeting": "hello", "values": [1, 2, 3]}
    serialized = yaml.safe_dump(yaml_content)
    parsed = yaml.safe_load(serialized)
    print("PyYAML round-trip:", parsed)


def run_matplotlib_demo():
    x = np.linspace(0, 1, 5)
    y = x**2
    plt.figure()
    plt.plot(x, y, marker="o")
    plt.title("Demo Plot")
    plt.xlabel("x")
    plt.ylabel("x squared")
    filename = "demo_plot.png"
    plt.savefig(filename)
    plt.close()
    print(f"Matplotlib demo wrote {filename}")


def run_pillow_demo():
    img = Image.new("RGBA", (64, 64), color=(120, 200, 240, 255))
    with io.BytesIO() as buffer:
        img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()
    print("Pillow demo created image with", len(img_bytes), "bytes")


def main():
    df = run_numpy_pandas_demo()
    run_scipy_demo(df["value"].to_numpy())
    run_requests_demo()
    run_pyyaml_demo()
    run_matplotlib_demo()
    run_pillow_demo()


if __name__ == "__main__":
    main()
