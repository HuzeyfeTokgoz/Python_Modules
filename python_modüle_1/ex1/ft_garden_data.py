class Plant:
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name = name
		self.height = height
		self.age = age

	def print_plant(self):
		print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
	p1 = Plant("Rose", 25, 30)
	p2 = Plant("Sunflower", 80, 45)
	p3 = Plant("Cactus", 15, 120)
	plants = [p1, p2, p3]
	print("=== Garden Plant Registry ===")
	for i in range(len(plants)):
		plants[i].print_plant()