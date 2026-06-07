class Plant:
    name: str
    height: float
    days: int

    def __init__(self, name, height, days) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> str:
        return (f"{self.name}: {self.height} cm, {self.days} days old")

    def age(self) -> None:
        self.days += 1


def ft_plant_factory() -> None:
    plants = [
        Plant("Cactus", 50, 30),
        Plant("Oaktree", 200, 66),
        Plant("Daisy", 5, 1),
        Plant("Rose", 72, 50),
        Plant("Bokchoi", 8, 21)
    ]

    for plant in plants:
        print(f"Created: {plant.show()}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    ft_plant_factory()
