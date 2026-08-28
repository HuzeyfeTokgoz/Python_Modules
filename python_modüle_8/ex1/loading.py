import importlib
import sys

def check_module():
	print("LOADING STATUS: Loading programs...")
	print("Checking dependencies:")
	req_lst: dict[str, str] = {"pandas": "Data manipulation ready", 
								"numpy": "Numerical computation ready",
								"matplotlib": "Visualization ready"}

	for pkg, desc in req_lst.items():
		try:
			module = importlib.import_module(pkg)
			version = getattr(module, "__version__", "unknown")
			if module:
				print(f"[OK] {pkg} ({module.__version__}) - {desc}")
		except ImportError:
			print(f"[MISSING] {pkg} - {desc}")
			print("\n[!] Dependencies missing. Install them using:")
			print("  pip:    pip install -r requirements.txt")
			print("  Poetry: poetry install")
			sys.exit(1)


def matrix():
	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt

	print("Analyzing Matrix data...")
	print("Processing 1000 data points...")
	# arr = np.array([
	# 		[0, 0],
	# 		[2, 0],
	# 		[1, 1],
	# 		[0, 0]
	# 	])
	print("Analyzing Matrix data...")
	rng = np.random.default_rng()
	arr = rng.integers(0, 5, size=(4, 2))
	df = pd.DataFrame(arr)
	plt.plot(df[0], df[1])
	plt.title("Matrix Coordinate Path")
	plt.grid(True)
	plt.savefig("matrix")

if __name__ == "__main__":
	check_module()
	matrix()
