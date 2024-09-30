import math


# Родительский класс Figure
class Figure:
    sides_count = 0

    def __init__(self, color: list, *sides):
        self.__color = list(color)
        # Проверка корректности цвета при инициализации
        if self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color = [0, 0, 0]  # Стандартный цвет - черный

        self.filled = False
        if not self.__is_valid_sides(*sides):
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in [r, g, b])

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        return all(isinstance(s, int) and s > 0 for s in sides) and len(sides) == self.sides_count

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


# Класс Circle (наследник Figure)
class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


# Класс Triangle (наследник Figure)
class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        s = sum(sides) / 2
        return math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))


# Класс Cube (наследник Figure)
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * 12
        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


# Тесты
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
