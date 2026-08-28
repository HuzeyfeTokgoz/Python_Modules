import sys
import os
import site

def is_virtual() -> bool:
	return sys.prefix != sys.base_prefix

def matrix_status():
	if is_virtual:
		return ("You're still plugged in")
	else:
		return ("Welcome to the construct")

def virtual_env():
	if is_virtual():
		return os.path.basename(sys.prefix)
	else:
		return "None detected"

def is_env():
	if is_virtual():
		return "\nSUCCESS: You're in an isolated environment!\nSafe " \
				"to install packages without affecting the global system."
	else:
		return "\nWARNING: You're in the global environment!\nThe " \
				"machines can see everything you install."

def run_env():
	return ("\npython -m venv matrix_env\nsource " \
	   	"matrix_env/bin/activate # On Unix " \
		"\nmatrix_env\\Scripts\\activate # On Windows")

if __name__ == "__main__":
	print(is_virtual())
	print("MATRİX STATUS:", matrix_status())
	print("\nCurrent Python:", sys.executable)
	print("Virtual Environment:", virtual_env())
	if is_virtual():
		print("Environment Path:", sys.prefix)
	print(is_env())
	if is_virtual():
		print("\nPackage installation path:", site.getsitepackages()[0])
	else:
		print("\nTo enter the construct, run:", run_env())
		print("\nThen run this program again.")