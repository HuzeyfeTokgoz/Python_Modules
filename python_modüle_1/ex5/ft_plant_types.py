class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_info(self) -> str:
        return f"{self._name} ({self._height}cm, {self._age} days)"

class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self._name} is blooming in {self.color}!")

class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self._name} is providing shade with its {self.trunk_diameter}cm trunk.")

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "Red")
    oak = Tree("Oak", 300, 1000, 50)
    carrot = Vegetable("Carrot", 15, 60, "Autumn", "High Vitamin A")

    # Babadan (Plant) gelen get_info() metodunu hepsi kullanabilir
    print(rose.get_info())
    rose.bloom() # Sadece Flower'a özel metod
    
    print(oak.get_info())
    oak.produce_shade() # Sadece Tree'ye özel metod
    
    print(carrot.get_info())
    print(f"{carrot._name} is harvested in {carrot.harvest_season} and provides {carrot.nutritional_value}.")


    ## hatalı devam edilecek