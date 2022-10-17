from typing import List
from abc import ABC, abstractmethod

"""
1. На основе Диаграмы классов ModelElements, разработать классы: Model Store, 
PoligonalModel (Texture, Poligon), Flash, Camera, Scene
"""


class Point3D:
    ...


class Angle3D:
    ...


class Color:
    ...


class Texture:
    ...


class Poligon:

    def __init__(self, points: Point3D):
        self.points = points


class PoligonalModel:

    def __init__(self, poligons: List[Poligon], textures: List[Texture] = None):
        self.poligons = poligons
        self.textures = textures


class Flash:

    def __init__(self, location: Point3D, angle: Angle3D, color: Color, power: float):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, new_angle: Angle3D):
        self.angle = new_angle

    def move(self, new_location: Point3D):
        self.location = new_location


class Camera:

    def __init__(self, location: Point3D, angle: Angle3D):
        self.location = location
        self.angle = angle

    def rotate(self, new_angle: Angle3D):
        self.angle = new_angle

    def move(self, new_location: Point3D):
        self.location = new_location


class Scene:

    def __init__(self, scene_id: int, models: List[PoligonalModel], flashes: List[Flash] = None):
        self.scene_id = scene_id
        self.models = models
        self.flashes = flashes

    def method1(self, i: int) -> int:
        return i * len(self.models)

    def method2(self, i: int, n: int) -> int:
        return i * n * len(self.models)


class IModelChangedObserver(ABC):

    @abstractmethod
    def apply_update_model(self):
        pass


class IModelChanger(ABC):

    @abstractmethod
    def notify_change(self):
        pass


class ModelStore:

    def __init__(self, models: List[PoligonalModel], scenes: List[Scene], flashes: List[Flash], cameras: List[Camera],
                 change_observers: IModelChangedObserver):
        self.models = models
        self.scenes = scenes
        self.flashes = flashes
        self.cameras = cameras
        self.__change_observers = change_observers

    def get_scena(self, scene_id: int) -> Scene:
        return next(filter(lambda x: x.scene_id == scene_id, self.scenes), None)

    def notify_change(self, model_changer: IModelChanger):
        ...
