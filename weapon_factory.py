from __future__ import annotations
from abc import ABC, abstractmethod


class Weapon(ABC):

    @abstractmethod
    def upgrade(self):
        pass


class WeaponFactory(ABC):

    @abstractmethod
    def create_weapon(self):
        pass

    def upgrade_weapon(self, weapon: Weapon):
        weapon.upgrade()


class Sword(Weapon):
    def upgrade(self) -> str:
        return "{Result of the ConcreteProduct1}"


class Bow(Weapon):
    def upgrade(self) -> str:
        return "{Result of the ConcreteProduct2}"


class SwordFactory(WeaponFactory):

    def create_weapon(self) -> Weapon:
        return Sword()


class BowFactory(WeaponFactory):
    def create_weapon(self) -> Weapon:
        return Bow()
