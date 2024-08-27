from dis import dis

def divide(first, second):
    """
    Функция деления двух чисел
    :param first: int делимое
    :param second: int делитель
    :return: результат деления или 'Ошибка' в случае деления на 0
    """
    if second == 0:
        return 'Ошибка'
    return first / second

dis(divide)
