"""
Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов,
file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием
после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков.
Как это сделать рассказано в лекции к домашнему заданию.
"""
# Алгоритм работы кода:
# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков

from time import sleep
from datetime import datetime
from threading import Thread


# Вариант 1 с использованием цикла for
# def write_words(word_count, file_name):
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for num in range(1, word_count + 1):
#             file.write(f"Какое-то слово №{num}\n")
#             sleep(0.1)
#     print(f"Завершилась запись в файл {file_name}")

# Для практики выполнил 2 других реализации
# Вариант 2 с использованием лямбда функции
# def write_words(word_count, file_name):
#     with open(file_name, 'w', encoding='utf-8') as file:
#         list(map(lambda num: (file.write(f"Какое-то слово №{num}\n"), sleep(0.1)), range(1, word_count + 1)))
#     print(f"Завершилась запись в файл {file_name}")

# Вариант 3 с использованием генератора
def write_words(word_count, file_name):
    def word_generator():
        for num in range(1, word_count + 1):
            yield f"Какое-то слово №{num}\n"
            sleep(0.1)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(word_generator())
    print(f"Завершилась запись в файл {file_name}")


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
completion_time = time_end - time_start
print(completion_time)  # 0:00:35.206513

thr_1 = Thread(target=write_words, args=(10, 'example1.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example2.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example3.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example4.txt'))

time_start = datetime.now()
thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()
time_end = datetime.now()
completion_time = time_end - time_start

print(completion_time)  # 0:00:20.713111
