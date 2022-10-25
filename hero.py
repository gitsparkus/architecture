from factories import *


class Hero(ABC):

    def __init__(self, name: str):
        self.armor = None
        self.weapon = None
        self.name = name
        self.health = 100

    @abstractmethod
    def get_equipment(self):
        pass

    def __str__(self):
        return f"Имя: {self.name}\nЗдоровье:{self.health}\n{self.weapon}\n{self.armor}"


class Archer(Hero):

    def __init__(self, name: str):
        super().__init__(name)

    def get_equipment(self):
        self.weapon = WeaponFactory().create(WeaponType.BOW)
        self.armor = ArmorFactory().create(ArmorType.LEATHER_ARMOR)


class Knight(Hero):
    def __init__(self, name: str):
        super().__init__(name)

    def get_equipment(self):
        self.weapon = WeaponFactory().create(WeaponType.SWORD)
        self.armor = ArmorFactory().create(ArmorType.CHAIN_ARMOR)


if __name__ == '__main__':
    knight = Knight('Arthur')
    archer = Archer('Серёжа')
    knight.get_equipment()
    archer.get_equipment()
    print(knight, '\n\n')
    print(archer)
