"""
Примитивная ORM
"""
import sqlite3

connection = sqlite3.connect("new_db.db")

cursor = connection.cursor()


def initiate_db():
    """
    Создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            img_path TEXT
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        );
    """)
    connection.commit()


def add_user(username, email, age, balance=1000):
    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if check_user.fetchone() is None:
        cursor.execute(
            """
                    INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
                """, (username, email, age, balance))
    else:
        print(f"Пользователь с таким именем {username} уже зарегистрирован")
    connection.commit()


def is_included(username):
    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    connection.commit()
    if check_user.fetchone():
        return True
    return False


def get_all_products():
    """
    Возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
    """
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    products_list = [
        {"id": product[0], "title": product[1], "description": product[2], "price": product[3], "img_path": product[4]}
        for product in all_products
    ]
    connection.commit()
    return products_list


def add_product(title, description, price, img_path) -> None:
    """
    Добавляет продукт в базу данных
    :param img_path: ссылка на изображение, str
    :param title: название продукта, str
    :param description: описание, str
    :param price: цена, int
    :return: None
    """
    cursor.execute("SELECT * FROM Products WHERE title = ?", (title,))
    existing_product = cursor.fetchone()
    if existing_product is None:
        cursor.execute("""
            INSERT INTO Products (title, description, price, img_path) VALUES(?, ?, ?, ?)
        """, (title, description, price, img_path))
        connection.commit()
    else:
        print(f"Продукт {title} уже в базе данных")
