class Plant:
    name: str
    height: float
    days: int
    growth_rate: float
    total_growth: float

    def show(self) -> None:
        print(f"{self.name}: {self.height} cm, {self.days} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)
        self.total_growth += self.growth_rate

    def age(self) -> None:
        self.days += 1


def ft_plant_growth() -> None:
    plant1 = Plant()
    plant1.name = "Coconut Tree"
    plant1.height = 350
    plant1.days = 10
    plant1.growth_rate = 7.5
    plant1.total_growth = 0
    plant1.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
    print(f"Growth this week: {plant1.total_growth} cm")


def main() -> None:
    print("=== Garden Plant Growth ===")
    ft_plant_growth()


if __name__ == "__main__":
    main()
