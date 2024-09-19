"""
Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) -
наследник класса Vehicle.

I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:

Атрибут owner(str) - владелец транспорта. (владелец может меняться)
Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
А так же атрибут класса:
Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)

Каждый объект Vehicle должен содержать следующие методы:

Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
а так же владельца в конце в формате "Владелец: <имя>"
Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color,
если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
"Нельзя сменить цвет на <новый цвет>".

Взаимосвязь методов и скрытых атрибутов:

Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами:
__model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)

"""


# Создайте классы Vehicle и Sedan.
# Напишите соответствующие свойства в обоих классах.
# Не забудьте сделать Sedan наследником класса Vehicle.

class Vehicle:
    """
    Создаёт экземпляр класса Vehicle,
    с атрибутами owner: str, model: str, engine_power: int, color: str
    """
    __COLOR_VARIANTS = ['белый', 'синий', 'красный']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(f"{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    """
    СОздаёт класс Sedan, наследует класс Vehicle
    """
    __PASSENGERS_LIMIT: int = 5


# Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.

v1 = Sedan('Фродо', 'Toyota Mark II', 500, 'синий')
# Изначальные свойства
v1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
v1.set_color('Pink')
v1.set_color('краСнЫй')
v1.owner = 'Vasyok'

# Проверяем что поменялось
v1.print_info()
