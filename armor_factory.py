from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum


class ArmorType(Enum):
    LEATHER_ARMOR = 1
    CHAIN_ARMOR = 2


class ArmorClass(Enum):
    STANDARD = 1
    LEGENDARY = 2


class Armor(ABC):

    def __init__(self, armor_type: ArmorType, level: int = 0):
        self.level = level
        self.armor_class = ArmorClass.STANDARD
        self.armor_type = armor_type
        self._upgrade_if_level()

    def level_up(self):
        self.level += 1
        self._upgrade_if_level()

    @abstractmethod
    def _upgrade_if_level(self):
        pass

    def _upgrade(self):
        if self.armor_class != ArmorClass.LEGENDARY:
            self.armor_class = ArmorClass.LEGENDARY

    def __str__(self) -> str:
        return f"Тип: {self.armor_type.name}\nКласс: {self.armor_class.name} \nУровернь: {self.level}"


class LeatherArmor(Armor):

    def __init__(self, level: int = 0):
        super().__init__(ArmorType.LEATHER_ARMOR, level)

    def _upgrade_if_level(self):
        if self.level >= 10:
            self._upgrade()


class ChainArmor(Armor):

    def __init__(self, level: int = 0):
        super().__init__(ArmorType.CHAIN_ARMOR, level)

    def _upgrade_if_level(self):
        if self.level >= 5:
            self._upgrade()


class ArmorFactory:
    armor_dict = {
        ArmorType.CHAIN_ARMOR: ChainArmor,
        ArmorType.LEATHER_ARMOR: LeatherArmor
    }

    @classmethod
    def create_armor(cls, armor_type: ArmorType, level: int = 0) -> Armor:
        if method := cls.armor_dict.get(armor_type, None):
            return method(level)

    @staticmethod
    def upgrade_armor(armor: Armor):
        armor._upgrade()


if __name__ == '__main__':
    leather = ArmorFactory.create_armor(ArmorType.LEATHER_ARMOR)

    print(leather)
    leather.level_up()
    print(leather)
    ArmorFactory.upgrade_armor(leather)
    print(leather)

    chain = ArmorFactory.create_armor(ArmorType.CHAIN_ARMOR, 10)
    print(chain)
    chain.level_up()
    print(chain)
