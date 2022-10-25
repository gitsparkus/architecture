from abc import ABC, abstractmethod
from enum import Enum


class SingletonBaseClass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class WeaponType(Enum):
    SWORD = 1
    BOW = 2


class Weapon(ABC):

    def __str__(self) -> str:
        return f"Тип оружия: {self.__class__.__name__}"


class Sword(Weapon):
    pass


class Bow(Weapon):
    pass


class ArmorType(Enum):
    LEATHER_ARMOR = 1
    CHAIN_ARMOR = 2


class Armor(ABC):

    def __str__(self) -> str:
        return f"Тип брони: {self.__class__.__name__}"


class LeatherArmor(Armor):
    pass


class ChainArmor(Armor):
    pass


class Factory(metaclass=SingletonBaseClass):

    @staticmethod
    @abstractmethod
    def create(object_type: Enum):
        pass


class WeaponFactory(Factory):

    @staticmethod
    def create(weapon_type: WeaponType) -> Weapon:
        if weapon_type == WeaponType.SWORD:
            return Sword()
        elif weapon_type == WeaponType.BOW:
            return Bow()


class ArmorFactory(Factory):

    @staticmethod
    def create(armor_type: ArmorType) -> Armor:
        if armor_type == ArmorType.CHAIN_ARMOR:
            return ChainArmor()
        elif armor_type == ArmorType.LEATHER_ARMOR:
            return LeatherArmor()


if __name__ == '__main__':
    # Оружие
    weapon_factory1 = WeaponFactory()
    bow = weapon_factory1.create(WeaponType.BOW)
    print(bow)

    weapon_factory2 = WeaponFactory()
    sword = weapon_factory2.create(WeaponType.SWORD)
    print(sword)

    print(weapon_factory1 is weapon_factory2)
    print(id(weapon_factory1), id(weapon_factory2))

    # Броня
    armor_factory1 = ArmorFactory()
    leather = armor_factory1.create(ArmorType.LEATHER_ARMOR)
    print(leather)

    armor_factory2 = ArmorFactory()
    chain = armor_factory2.create(ArmorType.CHAIN_ARMOR)
    print(chain)

    print(armor_factory1 is armor_factory2)
    print(id(armor_factory1), id(armor_factory2))
