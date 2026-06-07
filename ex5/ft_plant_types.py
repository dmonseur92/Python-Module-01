class Plant:
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: "
              f"{self.height} cm, {self.days} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.days += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float, color: str, bloomed: bool) -> None:
        super().__init__(name, height, days, growth_rate)
        self.color = color
        self.bloomed = bloomed

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!\n")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, days, growth_rate)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"{self.name} now produces a shade of "
              f"{self.height}cm long and {self.trunk_diameter}cm wide.\n")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int, growth_rate: float,
                 harvest_season: str, nutritional_value: float) -> None:
        super().__init__(name, height, days, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow_age(self) -> None:
        print("[make tomato grow and age for 20 days]")
        for _ in range(0, 20):
            super().grow()
            super().age()
            self.nutritional_value += 1


def ft_plant_types() -> None:
    rose = Flower("Rose", 15.0, 10, 0.1, "red", False)
    oak = Tree("Oak", 200.0, 365, 0.5, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April", 0)
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    print("=== Vegetable")
    tomato.show()
    tomato.grow_age()
    tomato.show()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    ft_plant_types()
