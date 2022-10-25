"""
Написать любом языке программирования, в которой идёт со следующими геометрическими фигурами:
1. Треугольник
2. Квадрат
3. Прямоугольник.
4. Круг
В программе имеется массив фигур, с которым можно сделать следующие операции:
1. Добавить новую фигуру
2. Посчитать периметр у всех фигур
3. Посчитать площадь у всех фигур
Для фигуры использовать базовый абстрактный класс фигуры, у которого есть методы посчитать периметр и посчитать площадь
фигуры. Массив фигур в программе должен быть представлен как массив объектов этого базового класса. Массив фигур должен
создаваться и вся работа с ним идёт внутри main. При создании фигур необходимо осуществлять проверку входных данных на
возможность создания данной фигуры и в случае ошибки выдавать соответствующие сообщения.
"""

from abc import ABC, abstractmethod
from math import pi, tan, radians


class ArgumentTypeError(ValueError):
    pass


class ArgumentValueError(ValueError):
    pass


class GeometryError(ValueError):
    pass


class Shape(ABC):

    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass


class Polygon(Shape):

    def __init__(self, *args: float):
        self._sides = args

    @abstractmethod
    def get_area(self) -> float:
        pass

    def get_perimeter(self) -> float:
        return sum(self._sides)


class Triangle(Polygon):

    def __init__(self, a: float, b: float, c: float):
        if a + b <= c or a + c <= b or b + c <= a:
            raise GeometryError('Из переданных отрезков невозможно собрать треугольник!')
        super().__init__(a, b, c)

    def get_area(self) -> float:
        p = self.get_perimeter() / 2
        return (p * (p - self._sides[0]) * (p - self._sides[1]) * (p - self._sides[2])) ** 0.5


class Rectangle(Polygon):

    def __init__(self, a: float, b: float):
        super().__init__(a, b, a, b)

    def get_area(self) -> float:
        return self._sides[0] * self._sides[1]


class Square(Rectangle):

    def __init__(self, a: float):
        super().__init__(a, a)


class Circle(Shape):

    def __init__(self, r: float):
        if r <= 0:
            raise ArgumentValueError('Радиус должен быть больше 0!')
        self.radius = r

    def get_area(self) -> float:
        return pi * (self.radius ** 2)

    def get_perimeter(self) -> float:
        return 2 * pi * self.radius


class ShapeList(list):

    def append(self, shape: Shape):
        if not isinstance(shape, Shape):
            raise ArgumentTypeError('В список фигур можно добавлять только объекты классов, унаследованных от Shape')
        super().append(shape)

    def get_sum_perimeter(self) -> float:
        return sum((shape.get_perimeter() for shape in self))

    def get_sum_area(self) -> float:
        return sum((shape.get_area() for shape in self))


if __name__ == '__main__':
    shapes_list = ShapeList()

    triangle = Triangle(1, 1, 1)
    square = Square(12)
    rectangle = Rectangle(5, 6)
    circle = Circle(4)

    shapes_list.append(triangle)
    shapes_list.append(square)
    shapes_list.append(rectangle)
    shapes_list.append(circle)

    for item in shapes_list:
        print(item.__class__)
        print(item.get_area())

