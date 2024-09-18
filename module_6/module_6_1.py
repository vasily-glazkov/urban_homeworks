"""
Создайте:
2 класса родителя: Animal, Plant
Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название
каждого животного.
Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения

4 класса наследника:
Mammal, Predator для Animal.
Flower, Fruit для Plant.

У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.

Метод eat должен работать следующим образом:
Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
меняется атрибут fed на True.
Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
меняется атрибут alive на False.
Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)

Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.

"""


# Создайте классы Animal и Plant с соответствующими атрибутами и методами

class Animal:
    """
    Создает экземпляр животного
    """

    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    """
    Создает экземпляр растения
    """
    def __init__(self, name):
        self.edible = False
        self.name = name


# Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
# При необходимости переопределите значения атрибутов.

class Mammal(Animal):
    """
    Создает экземпляр травоядного. Наследует класс Animal
    """
    pass


class Predator(Animal):
    """
    Создает экземпляр хищника. Наследует класс Animal
    """
    pass


class Flower(Plant):
    """
    Создает экземпляр растения. Наследует класс Plant
    """
    pass


class Fruit(Plant):
    """
    Создает экземпляр растения. Наследует класс Plant
    """
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


# Создайте объекты этих классов.

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

