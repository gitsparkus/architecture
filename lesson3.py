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
from math import pi


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


class ShapeList(list):

    def append(self, shape: Shape):
        if not isinstance(shape, Shape):
            raise ArgumentTypeError('В список фигур можно добавлять только объекты классов, унаследованных от Shape')
        super().append(shape)

    def get_sum_perimeter(self) -> float:
        return sum((shape.get_perimeter() for shape in self))

    def get_sum_area(self) -> float:
        return sum((shape.get_area() for shape in self))


class Triangle(Shape):

    def __init__(self, a: float, b: float, c: float):

        if a <= 0 or b <= 0 or c <= 0:
            raise ArgumentValueError('Все стороны фигуры должны быть больше 0!')
        if a + b <= c or a + c <= b or b + c <= a:
            raise GeometryError('Из переданных отрезков невозможно собрать треугольник!')
        self.__a = a
        self.__b = b
        self.__c = c

    def get_area(self) -> float:
        p = self.get_perimeter() / 2
        return (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5

    def get_perimeter(self) -> float:
        return self.__a + self.__b + self.__c


class Circle(Shape):

    def __init__(self, r: float):
        if r <= 0:
            raise ArgumentValueError('Радиус должен быть больше 0!')
        self.__r = r

    def get_area(self) -> float:
        return pi * (self.__r ** 2)

    def get_perimeter(self) -> float:
        return 2 * pi * self.__r


class Rectangle(Shape):

    def __init__(self, a: float, b: float):
        if a <= 0 or b <= 0:
            raise ArgumentValueError('Сторона фигуры не может быть меньше 0!')
        self.__a = a
        self.__b = b

    def get_area(self) -> float:
        return self.__a * self.__b

    def get_perimeter(self) -> float:
        return 2 * (self.__a + self.__b)


class Square(Rectangle):

    def __init__(self, a: float):
        super().__init__(a, a)


if __name__ == '__main__':
    shapes_list = ShapeList()

    shapes_list.append(Triangle(1, 1, 1))
    shapes_list.append(Square(12))
    shapes_list.append(Rectangle(5, 6))
    shapes_list.append(Circle(4))

    sum_perimeter = sum((shape.get_perimeter() for shape in shapes_list))
    print(sum_perimeter)
    print(shapes_list.get_sum_perimeter())

    sum_area = sum((shape.get_area() for shape in shapes_list))
    print(sum_area)
    print(shapes_list.get_sum_area())
