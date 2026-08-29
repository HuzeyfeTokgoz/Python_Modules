import importlib
import sys


def check_module() -> None:
    print("LOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    req_lst: dict[str, str] = {"pandas": "Data manipulation ready",
                               "numpy": "Numerical computation ready",
                               "matplotlib": "Visualization ready"}

    for pkg, desc in req_lst.items():
        try:
            module = importlib.import_module(pkg)
            if module:
                print(f"[OK] {pkg} ({module.__version__}) - {desc}")
        except ImportError:
            print(f"[MISSING] {pkg} - {desc}")
            print("\n[ERROR] Dependencies missing. Install them using:")
            print(" pip:    pip install -r requirements.txt")
            print(" Poetry: poetry install")
            sys.exit(1)
    matrix()


def matrix() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Analyzing Matrix data...")
    rng = np.random.default_rng()
    arr = rng.integers(0, 5, size=(4, 4))
    df = pd.DataFrame(arr)

    print("Generating visualization...")
    plt.plot(df[0], df[1], color="green")
    plt.title("Matrix Coordinate Path")
    plt.grid(True)
    plt.savefig("matrix")
    plt.show()

    print("Results saved to: matrix.png")
    print("Analysis complete!")


if __name__ == "__main__":
    check_module()
