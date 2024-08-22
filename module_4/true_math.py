from math import inf

def divide(first, second):
    """
    Функция деления двух чисел
    :param first: int делимое
    :param second: int делитель
    :return: результат деления first на second, если second не равно 0, иначе inf
    """
    if second == 0:
        return inf
    return first / second
