import math
import time
from module6hard import Figure, Circle, Triangle, Cube

TIME_COUNT = 3


print("Проверка класса Figure... ")
time.sleep(TIME_COUNT)
assert "sides_count" in Figure.__dict__, "Создайте классовый атрибут sides_count над конструктором"
assert "_Figure__sides" not in Figure.__dict__, "Атрибут __sides не должен быть классовым атрибутом. Он должен быть в конструкторе. Иначе случится так, что если вы создадите два объекта, измените список у одного из них - он автоматически изменится у другого. Попробуйте. так быть не должно"
assert "_Figure__color" not in Figure.__dict__, "Атрибут __color не должен быть классовым атрибутом. Он должен быть в конструкторе. Иначе случится так, что если вы создадите два объекта, измените список у одного из них - он автоматически изменится у другого. Попробуйте. так быть не должно"
assert "get_color" in Figure.__dict__, "Забыли метод get_color"
assert "set_color" in Figure.__dict__, "Забыли метод set_color"
assert "get_sides" in Figure.__dict__, "Забыли метод get_sides"
assert "set_sides" in Figure.__dict__, "Забыли метод set_sides"
assert "__len__" in Figure.__dict__, "Забыли метод __len__"
assert "_Figure__is_valid_color" in Figure.__dict__, "Забыли метод __is_valid_color"
assert "_Figure__is_valid_sides" in Figure.__dict__, "Забыли метод __is_valid_sides"
assert Figure.sides_count == 0, "Figure: sides_count должен быть равен 0"
try:
    f1 = Figure((-100, -100, -100), 1)
    f2 = Figure((0, 0, 0), 2)
    f3 = Figure((300, 300, 300), 3)
    f4 = Figure([5, 5, 5], 5, 6, 7, 8, 9, 10)
    f5 = Figure([127, 14, 48], 5, 6, 7, 8, 9, 10, 11)
except:
    print("Вы забыли создать конструктор, либо он не имеет вид def __init__(self, color: list, *sides: int): или попроще def __init__(self, color, *sides):")
    exit()
assert isinstance(f3._Figure__color, list), "В конструкторе нужно сделать self.__color списком"
assert f1.get_color() == [
    0, 0, 0], "У вас сейчас можно при создании объекта записать отрицательные числа в цвет. Добавьте проверку set_color"

assert f2.get_color() == [0, 0, 0] or f2.get_color() == (
    0, 0, 0), "У вас нельзя записать 0 в качестве значения цвета в конструкторе"
assert f3.get_color() == [0, 0, 0] or f3.get_color() == (
    0, 0, 0), "У вас сейчас можно при создании объекта записать числа, больше 255 в цвете"
assert len(f1._Figure__sides) == 0, "В конструкторе длина списка sides не равна 0"
assert len(f1.get_sides()) == 0, "Геттер get_sides выдает список не из 0 элементов"
assert isinstance(f1.get_sides(), list), "get_sides должен возвращать список сторон"
assert f1.get_sides() == [] or f5.get_sides() == [], "Если в конструкторе передано сторон меньше, чем sides_count, то sides должен состоять из 0 единиц: [] по количеству sides_count (не создавать просто [])"
assert f4.get_sides() == [], "Обратите внимание, что в конструктор передается *sides - неограниченное количество сторон, и если количество переданных сторон совпадает с sides_count, то стороны записываются в список sides. Метод get_sides должен выдавать именно их."
try:
    f4.set_color("red", "green", "blue")
except:
    print("Добавьте проверку в __is_valid_color, что цвет является числом")
class Sixter(Figure):
    sides_count = 6
f4 = Sixter([5, 5, 5], 5, 6, 7, 8, 9, 10)
f4.set_color(300, 300, 300)
assert f4.get_color() == [5, 5, 5], "Проверка __is_valid_color пропускает числа, больше 255, либо у вас не сохраняется в set_color изначальное значение цвета. Метод должен работать так: если переданный цвет является валидным, то self.__color = этому новому цвету. В противном случае ничего не происходит"
f4.set_color(255, 255, 255)
assert f4.get_color() == [255, 255, 255], "Число 255 почему-то не входит в диапазон разрешенных значений в set_color"
f4.set_color(0, 0, 0)
assert f4.get_color() == [0, 0, 0], "Число 0 почему-то не входит в диапазон разрешенных значений в set_color"
f4.set_sides(1, 2, 3, 4, 5, 6)
assert f4.get_sides() == [
    1, 2, 3, 4, 5, 6], f"Передал в set_sides числа 1,2,3,4,5,6, а get_sides не выдал [1,2,3,4,5,6]. Вышло {f4.get_sides()} Что за ошибка вкралась?"
f4.set_sides(5)
assert f4.get_sides() == [
    1, 2, 3, 4, 5, 6], "Поправьте __is_valid_sides - первые строки в методе: if len(sides) != self.sides_count: return False. Сейчас при передаче одной стороны в set_sides список сторон не сохраняется исходным"
f4.set_sides(5.5, 5.5, 5.5, 5.5, 5.5, 5.5)
assert f4.get_sides() == [
    1, 2, 3, 4, 5, 6], "Поправьте __is_valid_sides - если в set_sides передаются нецелые числа, то список сторон не должен меняться на эти переданные числа"
assert len(f4) == sum(f4.get_sides()), "Метод __len__ должен выдавать сумму всех сторон. Используйте return sum(self.__sides)"
print("Ошибок нет! Класс Figure хорош.")

print("\nТеперь класс Circle...")
print("Не забывайте, что в этом и следующем классах к сторонам нужно обращаться self.get_sides(), а к цвету - self.get_color()")
time.sleep(TIME_COUNT)
assert issubclass(
    Circle, Figure), "Класс Circle должен наследоваться от класса Figure. Используйте следующий синтаксис: class Circle(Figure)"
assert "sides_count" in Circle.__dict__, "Создайте классовый атрибут sides_count над конструктором. Он должен равняться 1."
assert "_Circle__sides" not in Circle.__dict__, "Атрибут __sides не должен быть классовым атрибутом. Он должен быть в конструкторе. Иначе случится так, что если вы создадите два объекта, измените список у одного из них - он автоматически изменится у другого. Попробуйте. так быть не должно"
assert "_Circle__color" not in Circle.__dict__, "Атрибут __color не должен быть классовым атрибутом. Он должен быть в конструкторе. Иначе случится так, что если вы создадите два объекта, измените список у одного из них - он автоматически изменится у другого. Попробуйте. так быть не должно"
assert Circle.sides_count == 1, "sides_count должен быть равен 1"
circle = Circle((255, 150, 150), 3, 4, 5)
assert circle.get_sides() == [1], "При передаче нескольких сторон при создании круга, в списке sides должно быть [1]"
true_radius = 1/(2 * math.pi)
assert circle._Circle__radius - \
       true_radius < 0.01, "Неправильная формула расчета радиуса. Используйте 0-й элемент списка сторон и делите его на (2 * math.pi)"
true_area = math.pi
assert circle.get_square() - true_area < 0.01, "Неправильно высчитывается площадь, формула такова: math.pi * (self.__radius ** 2)"
circle._Circle__radius = 5
true_area = math.pi * 25
assert circle.get_square() - true_area < 0.01, "Неправильно высчитывается площадь, формула такова: math.pi * (self.__radius ** 2)"
print("С кругом у вас тоже полный порядок!")

time.sleep(1)
print("\nТеперь смотрим класс Triangle...")
time.sleep(TIME_COUNT)
assert issubclass(
    Triangle, Figure), "Класс Triangle должен наследоваться от класса Figure. Используйте следующий синтаксис: class Circle(Figure)"
assert "sides_count" in Triangle.__dict__, "Создайте классовый атрибут sides_count над конструктором"
assert "_Triangle__sides" not in Triangle.__dict__, "Атрибут __sides не должен быть классовым атрибутом. Он должен быть в конструкторе. Иначе случится так, что если вы создадите два объекта, измените список у одного из них - он автоматически изменится у другого. Попробуйте. так быть не должно"
assert "_Triangle__color" not in Triangle.__dict__, "Атрибут __color не должен быть классовым атрибутом. Он должен быть в конструкторе. Иначе случится так, что если вы создадите два объекта, измените список у одного из них - он автоматически изменится у другого. Попробуйте. так быть не должно"
assert Triangle.sides_count == 3, "sides_count должен быть равен 1"
triangle = Triangle((5, 5, 5), 3, 4, 5)

assert triangle.get_square() - 6.0 < 0.01, "Формула подсчета площади работает некорректно. Не забывайте скобки и использование math.sqrt"

print(f"С классом Треугольника тоже порядок!")

time.sleep(1)
print(f"\nТеперь смотрим на последний класс - Cube")
assert issubclass(
    Cube, Figure), "Класс Cube должен наследоваться от класса Figure. Используйте следующий синтаксис: class Circle(Figure)"
assert "sides_count" in Cube.__dict__, "Создайте классовый атрибут sides_count над конструктором"
assert "_Cube__sides" not in Cube.__dict__, "Атрибут __sides не должен быть классовым атрибутом. Он должен быть в конструкторе. Иначе случится так, что если вы создадите два объекта, измените список у одного из них - он автоматически изменится у другого. Попробуйте. так быть не должно"
assert "_Cube__color" not in Cube.__dict__, "Атрибут __color не должен быть классовым атрибутом. Он должен быть в конструкторе. Иначе случится так, что если вы создадите два объекта, измените список у одного из них - он автоматически изменится у другого. Попробуйте. так быть не должно"
assert Cube.sides_count == 12, "sides_count должен быть равен 12"
cube = Cube((2, 2, 2), 9, 12)
assert cube.get_sides() == [1] * \
       12, "Когда передается несколько сторон в конструктор, список должен состоять из 12-ти единиц"
cube = Cube((2, 2, 2), 3)
assert cube.get_sides() == [
    3] * 12 or cube.get_sides() == (3,)*12, "Нужно переопределить конструктор. После вызова родительского конструктора - self.set_sides(*list(sides)*12)"
assert cube.get_volume() == 27, "Метод подсчета объема куба некорректен, проверьте формулу и не забудьте, что для получения списка сторон используется self.get_sides(), а сторона вам нужна только одна, которую нужно возвести в степень 3"
print(f"Всё правильно!")
print("\n\nПОЗДРАВЛЯЮ С ОКОНЧАНИЕМ 6 МОДУЛЯ!")
