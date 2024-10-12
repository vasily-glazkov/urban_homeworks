"""
Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:

Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое",
если результат 1ой функции будет простым числом и "Составное" в противном случае.

Пример:
result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11

Примечания:
Не забудьте написать внутреннюю функцию wrapper в is_prime
Функция is_prime должна возвращать wrapper
@is_prime - декоратор для функции sum_three

"""


def is_prime(func):
    def wrapper(*args, **kwargs):
        sum_result = func(*args, **kwargs)
        if sum_result <= 1:
            print("Составное")
        elif sum_result == 2:
            print("Простое")
        elif sum_result % 2 == 0:
            print("Составное")
        else:
            for i in range(3, int(sum_result ** 0.5) + 1, 2):
                if sum_result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return sum_result

    return wrapper


@is_prime
def sum_three(num1, num2, num3):
    return num1 + num2 + num3


result = sum_three(2, 3, 6)
print(result)
