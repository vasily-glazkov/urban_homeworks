# Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
# Вывести количество символов введённого текста
my_string = input('Введите ваш текст: ')
print(f"В строке {len(my_string)} символов.")

# Выведите строку my_string в верхнем регистре.
print(my_string.upper())

# Выведите строку my_string в нижнем регистре.
print(my_string.lower())

# Измените строку my_string, удалив все пробелы.
no_spaces_str = my_string.replace(' ', '')
print(no_spaces_str)

# Выведите первый символ строки my_string.
print(f"Первый символ: {my_string[0]}")

# Выведите последний символ строки my_string.
print(f"Последний символ: {my_string[-1]}")
