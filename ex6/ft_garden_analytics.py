class Plant:

    class Statistic:

        def __init__(self):
            self.nbr_grow = 0
            self.nbr_age = 0
            self.nbr_show = 0


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

    def age(self, n: int) -> None:
        self.set_age(self.get_age() + n)

    @staticmethod
    def check_age(days: int) -> bool:
        return days >= 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0)


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
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self.name} to grow and bloom]")
        self.grow()
        self.bloomed = True

class Seed(Flower):
    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float, color: str, bloomed: bool, seed_nbr: int = 0) -> None:
        super().__init__(name, height, days, growth_rate, color, bloomed)
        self.seed_nbr = seed_nbr

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed_nbr}")

    def bloom(self) -> None:
        print(f"[make {self.name} grow, age and bloom]")
        self.grow()
        self.bloomed = True
        self.age(20)
        self.seed_nbr += 42


class Tree(Plant):

    class Statistic(Plant.Statistic):

        def __init__(self):
            super().__init__()
            self.nbr_shade = 0

    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, days, growth_rate)
        self.trunk_diameter = trunk_diameter
        self.stats = self.Statistic()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"{self.name} now produces a shade of "
              f"{self.get_height()}cm long and {self.trunk_diameter}cm wide.\n")


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

def ft_garden_analytics() -> None:
    rose = Flower("Rose", 15.0, 10, 8.0, "red", False)
    oak = Tree("Oak", 200.0, 365, 0.5, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, 30.0, "yellow", 0)
    anonymous = Plant.create_anonymous()
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
    print()
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    print("=== Seed")
    sunflower.show()
    sunflower.bloom()
    sunflower.show()
    print()
    print("===  Anonymous")
    anonymous.show()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    ft_garden_analytics()
