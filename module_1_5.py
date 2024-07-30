# Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
#   - Выполните операции вывода кортежа immutable_var на экран.

immutable_var = ('monty', 'python', True, 1991, [20, 2, 1991])
print(type(immutable_var))
print(f"Immutable tuple: {immutable_var}")
print(f'Дата создания языка Python: {immutable_var[-1]}')

# Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

# TypeError: 'tuple' object does not support item assignment
# Кортежи в Python являются неизменяемыми (immutable) последовательностями, что означает, что их элементы не могут быть изменены после создания.

# immutable_var[2] = False

# Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.

mutable_list = ["Изменяемый список",
                {
                    "language": "Python",
                    "creation_date": "20.02.1991"
                },
                True
                ]

mutable_list[0] = "Это изменяемый список"
mutable_list.insert(2, {"language": "Javascript", "creation_date": "1995"})
print(f"Mutable list: {mutable_list}")
