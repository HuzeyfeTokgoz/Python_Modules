class Plant:
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name = name
		self.height = height
		self.plant_age = age

	def print_plant(self):
		print(f"Created: {self.name} ({self.height}cm, {self.plant_age} days)")

if __name__ == "__main__":
	plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
	plants = []
	for name, height, age in plant_data:
		plants.append(Plant(name, height, age))
	
	print("=== Plant Factory Output ===")
	for p in plants:
		p.print_plant()
	print(f"\nTotal plants created: {len(plants)}")