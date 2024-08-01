# Работа со словарями:

# Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
my_dict = {
    'Python': 1991,
    'Javascript': 1995,
    'Java': 1995,
    'C++': 1983,
}

# - Выведите на экран словарь my_dict.
print(f"Dictionary: {my_dict}")

# - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print(f"Python creation year: {my_dict.get('Python', 'No such entry')}")
print(f"C# creation year: {my_dict.get('C#', 'No such entry')}")

# - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict.update(
    {
        'C#': 2001,
        'Swift': 2014,
    }
)

# - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
# - Выведите на экран словарь my_dict.
swift_creation_date = my_dict.pop('Swift')
print(f"Swift created in: {swift_creation_date}")
print(f"Programming languages: {my_dict}")

# Работа с множествами:

# - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
my_set = {1, 1, 2, 2, 'apple', 'apple'}

# - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
print(f"Set: {my_set}")

# - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add(3)
my_set.add('orange')

# - Удалите один любой элемент из множества my_set.
my_set.discard(3)

# - Выведите на экран измененное множество my_set.
print(f"Modified set: {my_set}")
