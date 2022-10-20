from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum


class WeaponType(Enum):
    SWORD = 1
    BOW = 2


class WeaponClass(Enum):
    STANDARD = 1
    LEGENDARY = 2


class Weapon(ABC):

    def __init__(self, weapon_type: WeaponType, level: int = 0):
        self.level = level
        self.weapon_class = WeaponClass.STANDARD
        self.weapon_type = weapon_type
        self._upgrade_if_level()

    def level_up(self):
        self.level += 1
        self._upgrade_if_level()

    @abstractmethod
    def _upgrade_if_level(self):
        pass

    def _upgrade(self):
        if self.weapon_class != WeaponClass.LEGENDARY:
            self.weapon_class = WeaponClass.LEGENDARY

    def __str__(self) -> str:
        return f"Тип: {self.weapon_type.name}\nКласс: {self.weapon_class.name} \nУровернь: {self.level}"


class Sword(Weapon):

    def __init__(self, level: int = 0):
        super().__init__(WeaponType.SWORD, level)

    def _upgrade_if_level(self):
        if self.level >= 10:
            self._upgrade()


class Bow(Weapon):

    def __init__(self, level: int = 0):
        super().__init__(WeaponType.BOW, level)

    def _upgrade_if_level(self):
        if self.level >= 5:
            self._upgrade()


class WeaponFactory:

    @staticmethod
    def create_weapon(weapon_type: WeaponType, level: int = 0) -> Weapon:
        if weapon_type == WeaponType.SWORD:
            return Sword(level)
        elif weapon_type == WeaponType.BOW:
            return Bow(level)

    @staticmethod
    def upgrade_weapon(weapon: Weapon):
        weapon._upgrade()


if __name__ == '__main__':
    bow = WeaponFactory.create_weapon(WeaponType.BOW)

    print(bow)
    bow.level_up()
    print(bow)
    WeaponFactory.upgrade_weapon(bow)
    print(bow)

    sword = WeaponFactory.create_weapon(WeaponType.SWORD,10)
    print(sword)
    sword.level_up()
    print(sword)
