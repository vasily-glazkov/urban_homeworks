"""
Задание:
Создайте новый проект или продолжите работу в текущем проекте.
Напишите код, который форматирует строки для следующих сценариев.
Укажите переменные, которые должны быть вставлены в каждую строку:

Использование %:

Переменные: количество участников первой команды (team1_num).
Пример итоговой строки: "В команде Мастера кода участников: 5 ! "

Переменные: количество участников в обеих командах (team1_num, team2_num).
Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"

Использование format():
Переменные: количество задач решённых командой 2 (score_2).
Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"

Переменные: время за которое команда 2 решила задачи (team1_time).
Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"

Использование f-строк:
Переменные: количество решённых задач по командам: score_1, score_2
Пример итоговой строки: "Команды решили 40 и 42 задач.”

Переменные: исход соревнования (challenge_result).
Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"

Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
"""

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Логика для определения результата соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Использование % для форматирования строк
# 1. Количество участников первой команды
print("В команде Мастера кода участников: %d !" % team1_num)

# 2. Количество участников в обеих командах
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

# Использование метода format() для форматирования строк
# 3. Количество задач, решённых командой 2
print("Команда Волшебники данных решила задач: {} !".format(score_2))

# 4. Время, за которое команда 2 решила задачи
print("Волшебники данных решили задачи за {:.1f} с !".format(team2_time))

# Использование f-строк для форматирования строк
# 5. Количество решённых задач по командам
print(f"Команды решили {score_1} и {score_2} задач.")

# 6. Исход соревнования
print(f"Результат битвы: {challenge_result}")

# 7. Количество задач и среднее время решения
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!")
