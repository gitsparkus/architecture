from abc import ABC, abstractmethod
from armor_factory import *
from weapon_factory import *


class Hero(ABC):

    def __init__(self, name: str):
        self.armor = None
        self.weapon = None
        self.name = name
        self.health = 100
        self.get_equipment()

    @abstractmethod
    def get_equipment(self):
        pass

    def __str__(self):
        return f"Имя: {self.name}\nЗдоровье:{self.health}\nОружие:\n{self.weapon}\nБроня:\n{self.armor}"


class Archer(Hero):

    def __init__(self, name: str):
        super().__init__(name)

    def get_equipment(self):
        self.weapon = WeaponFactory.create_weapon(WeaponType.BOW)
        self.armor = ArmorFactory.create_armor(ArmorType.LEATHER_ARMOR)


class Knight(Hero):
    def __init__(self, name: str):
        super().__init__(name)

    def get_equipment(self):
        self.weapon = WeaponFactory.create_weapon(WeaponType.SWORD)
        self.armor = ArmorFactory.create_armor(ArmorType.CHAIN_ARMOR)


if __name__ == '__main__':
    knight = Knight('Arthur')
    archer = Archer('Серёжа')

    print(knight, '\n\n')
    print(archer)

    print(knight, '\n\n')
    WeaponFactory.upgrade_weapon(archer.weapon)
    print(archer)
