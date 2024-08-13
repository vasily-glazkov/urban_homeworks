"""
Функция с параметрами по умолчанию:
Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию
(например сейчас это: 1, 'строка', True).
Функция должна выводить эти параметры.
Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
"""


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  # 1 строка True
print_params(b=25)  # 1 25 True
print_params(c=[1, 2, 3])  # 1 строка [1, 2, 3]
print_params('hello', 2, 0)  # hello 2 0

"""
Распаковка параметров:
Создайте список values_list с тремя элементами разных типов.
Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, 
и значениями разных типов.
Передайте values_list и values_dict в функцию print_params, 
используя распаковку параметров (* для списка и ** для словаря).
"""

values_list = [7, True, 'seven']
values_dict = {
    'a': 'Python',
    'b': True,
    'c': 1989,
}

print_params(*values_list)  # 7 True seven
print_params(**values_dict)  # Python True 1989

"""
Распаковка + отдельные параметры:
Создайте список values_list_2 с двумя элементами разных типов
Проверьте, работает ли print_params(*values_list_2, 42)
"""

values_list_2 = [100500, 'Cito Citissimo']

print_params(*values_list_2, 42)  # 100500 Cito Citissimo 42
