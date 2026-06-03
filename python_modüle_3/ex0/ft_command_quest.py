import sys

def command_quest():
	arg_len = len(sys.argv)
	print("=== Command Quest ===")
	print(f"Program name: {sys.argv[0]}")
	if arg_len <= 1:
		print("No arguments provided!")
	else:
		print(f"Arguments received: {arg_len - 1}")
		i = 0
		for arg in sys.argv:
			if i > 0:
				print(f"Arguments {i}: {arg}")
			i += 1
	print(f"Total arguments: {arg_len}")

if __name__ == "__main__":
	command_quest()