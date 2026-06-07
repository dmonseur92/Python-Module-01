class Plant:
    name: str
    height: int
    age: int
    growth_rate: int

    def show(self) -> None:
        print(f"{self.name}: {self.height} cm, {self.age} days old")


def ft_garden_data() -> None:
    plant1 = Plant()
    plant2 = Plant()
    plant3 = Plant()
    plant1.name = "Brocoli"
    plant1.height = 5
    plant1.age = 2
    plant2.name = "Baobab"
    plant2.height = 5000
    plant2.age = 200000
    plant3.name = "Bananatree"
    plant3.height = 100
    plant3.age = 25
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()
