from abc import ABC, abstractmethod
from __future__ import annotations


class Hero(ABC):

    def __int__(self, name: str, health: int):
        self.name = name
        self.health = health

    @abstractmethod
    def attak(self, antagonist: Hero):
        pass


class Archer(Hero):
    ...


class Khight(Hero):
    ...




