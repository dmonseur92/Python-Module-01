class Plant:
    name: str
    height: float
    days: int

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self._height = height
        self._days = days

    def get_age(self) -> int:
        return self._days

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_days) -> None:
        if new_days >= 0:
            self._days = new_days
        else:
            print(f"{self.name}: "
                  "Error, age can't be negative\nAge update rejected\n")

    def set_height(self, new_height) -> None:
        if new_height >= 0:
            self._height = new_height
        else:
            print(f"{self.name}: "
                  "Error, height can't be negative\nHeight update rejected")

    def show(self) -> str:
        return (f"{self.name}: "
                f"{self.get_height()} cm, {self.get_age()} days old")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print(f"Plant created: {plant.show()}\n")
    plant.set_height(25)
    plant.set_age(30)
    print(f"Height updated: {plant.get_height()}cm")
    print(f"Age updated: {plant.get_age()} days\n")
    plant.set_height(-25)
    plant.set_age(-30)
    print(f"Current state: {plant.show()}")


if __name__ == "__main__":
    ft_garden_security()
