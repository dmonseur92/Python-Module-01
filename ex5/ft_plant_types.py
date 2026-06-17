class Plant:
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float) -> None:
        self.name = name
        self._height = height
        self._days = days
        self.growth_rate = growth_rate

    def get_age(self) -> int:
        return self._days

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_days: int) -> None:
        if new_days >= 0:
            self._days = new_days
        else:
            print(f"{self.name}: "
                  "Error, age can't be negative\nAge update rejected\n")

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
        else:
            print(f"{self.name}: "
                  "Error, height can't be negative\nHeight update rejected")

    def show(self) -> None:
        print(f"{self.name}: "
              f"{self.get_height()} cm, {self.get_age()} days old")

    def grow(self) -> None:
        self.set_height(round(self.get_height() + self.growth_rate, 1))

    def age(self) -> None:
        self.set_age(self.get_age() + 1)


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
              f"{self.get_height()}cm long and "
              f"{self.trunk_diameter}cm wide.\n")


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
