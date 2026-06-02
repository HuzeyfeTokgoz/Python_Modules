#!/usr/bin/env python3

class GardenError(Exception):
	def __init__(self, error="Unknown garden error"):
		super().__init__(error)

class PlantError(GardenError):
	def __init__(self, error="Unknown plant error"):
		super().__init__(error)

class WaterError(GardenError):
	def __init__(self, error="Unknown water error"):
		super().__init__(error)

def test_error_types():
	print("=== Custom Garden Errors Demo ===\n")
	try:
		print("Testing PlantError...")
		raise PlantError("The tomato plant is wilting!")

	except PlantError as e:
		print(f"caught PlantError: {e}\n")
	
	try:
		print("Testing WaterError...")
		raise WaterError("Not enough water in the tank!")
	except WaterError as e:
		print(f"caught WaterError: {e}\n")

	print("Testing catching all garden errors...")
	try:
		raise PlantError("The tomato plant is wilting!")
	except GardenError as e:
		print(f"Caught GardenError: {e}")
	try:
		raise WaterError("Not enough water in the tank!")
	except GardenError as e:
		print(f"Caught GardenError: {e}")

	print("\nAll custom error types work correctly!")
if __name__ == "__main__":
	test_error_types()