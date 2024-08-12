"""
Задача "Счётчик вызовов":
Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
Давайте реализуем данную фишку самостоятельно!

Вам необходимо написать 3 функции:
Функция count_calls подсчитывающая вызовы остальных функций.
Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
"""

# Пункты задачи:
# Создать переменную calls = 0 вне функций.

calls = 0


# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.

def count_calls():
    global calls
    calls += 1


# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# 1й способ
# def is_contains(string, list_to_search):
#     count_calls()
#     for item in list_to_search:
#         if string.lower() == item.lower():
#             return True
#     return False

# 2й способ реализации функции
def is_contains(string, list_to_search):
    count_calls()
    return any(string.lower() == item.lower() for item in list_to_search)


# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

# Вывести значение переменной calls на экран(в консоль).

print(f"Количество вызовов: {calls}")
