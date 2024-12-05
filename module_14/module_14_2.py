"""
Задача "Средний баланс пользователя":

Для решения этой задачи вам понадобится решение предыдущей.

Для решения необходимо дополнить существующий код:
1 - Удалите из базы данных not_telegram.db запись с id = 6.
2 - Подсчитать общее количество записей.
3 - Посчитать сумму всех балансов.
4 - Вывести в консоль средний баланс всех пользователей.
"""

import sqlite3

connection = sqlite3.connect('not_telegram.db')

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
""")

cursor.execute(
    '''
        CREATE INDEX IF NOT EXISTS idx_email ON Users (email)
    '''
)

cursor.execute("SELECT COUNT(*) FROM Users")
if cursor.fetchone()[0] == 0:
    for i in range(1, 11):
        cursor.execute("""
            INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
        """, (f"user{i}", f"example{i}@gmail.com", f"{i * 10}", "1000"))

cursor.execute("""
    UPDATE Users
    SET balance = 500
    WHERE id % 2 = 1
""")

cursor.execute("""
    DELETE FROM Users WHERE id % 3 = 1
""")

cursor.execute("""
    SELECT username, email, age, balance FROM Users WHERE age != ?
""", (60,))

# users = cursor.fetchall()
#
# for user in users:
#     print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

# 1 - Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute("DELETE FROM Users WHERE id = 6")

# 2 - Подсчитать общее количество записей.
cursor.execute("SELECT COUNT(*) FROM Users")
total_db_records = cursor.fetchone()[0]

# 3 - Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]

# 4 - Вывести в консоль средний баланс всех пользователей.
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(f"Средний баланс всех пользователей: {avg_balance}")

#  Второй способ посчитать средний баланс
# print(total_balance / total_db_records)

connection.commit()
connection.close()
