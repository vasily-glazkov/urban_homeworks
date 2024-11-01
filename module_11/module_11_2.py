"""
Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и
проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).


Пример работы:
number_info = introspection_info(42)
print(number_info)

Вывод на консоль:
{'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
"""
from pprint import pprint


def introspection_info(obj):
    #  Определение типа объекта
    obj_type = type(obj).__name__

    #  Получение атрибутов и методов объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    #  Определение модуля объекта
    module = getattr(obj, '__module__', 'builtins')

    #  Словарь с информацией
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
    }

    return info


class Book:
    def __init__(self, title):
        self.title = title

    def read(self):
        return f"Читаю книгу {self.title}"

    def __str__(self):
        return self.title


book1 = Book("Остров сокровищ")

info = introspection_info(book1)

pprint(info)
