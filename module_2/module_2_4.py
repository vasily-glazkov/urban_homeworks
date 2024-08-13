"""
Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создайте пустые списки primes и not_primes.
primes = []
not_primes = []

# При помощи цикла for переберите список numbers.
for number in numbers:
    # Пропускаем числа меньше 2, т.к. они не являются ни простыми, ни составными
    if number < 2:
        continue

# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
# Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    # В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Выведите списки primes и not_primes на экран(в консоль).
print("Primes: ", primes)
print("Not primes: ", not_primes)
