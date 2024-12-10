"""
Создайте файл crud_functions.py и напишите там следующие функции:
initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
Эта таблица должна содержать следующие поля:
id - целое число, первичный ключ
title(название продукта) - текст (не пустой)
description(описание) - текст
price(цена) - целое число (не пустой)
get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
"""
import sqlite3

connection = sqlite3.connect("database.db")

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
            price INTEGER NOT NULL
        );
    """)
    connection.commit()


def get_all_products():
    """
    Возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
    """
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    products_list = [
        {"id": product[0], "title": product[1], "description": product[2], "price": product[3]}
        for product in all_products
    ]
    return products_list


def add_product(title, description, price) -> None:
    """
    Добавляет продукт в базу данных
    :param title: название продукта, str
    :param description: описание, str
    :param price: цена, int
    :return: None
    """
    cursor.execute("SELECT * FROM Products WHERE title = ?", (title,))
    existing_product = cursor.fetchone()
    if existing_product is None:
        cursor.execute("""
            INSERT INTO Products (title, description, price) VALUES(?, ?, ?)
        """, (title, description, price))
        connection.commit()
    else:
        print(f"Продукт {title} уже в базе данных")
