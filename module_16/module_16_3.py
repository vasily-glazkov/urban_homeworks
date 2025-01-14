"""
Задача "Имитация работы с БД":
Создайте новое приложение FastAPI и сделайте CRUD запросы.

Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}

Реализуйте 4 CRUD запроса:

get запрос по маршруту '/users', который возвращает словарь users.
post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по
значению ключом значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из
словаря users под ключом user_id на строку "Имя: {username}, возраст: {age}".
И возвращает строку "The user <user_id> is updated"
delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
"""

from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

# создаем приложение (объект) FastAPI
app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    """
    GET запрос по маршруту '/users', который возвращает словарь users
    :return: dict
    """
    return users


@app.post('/user/{username}/{age}')
async def add_user(
        username: Annotated[str, Path(
            min_length=4,
            max_length=20,
            description="Enter username",
            example="Gandalf"
        )],
        age: Annotated[int, Path(
            ge=18,
            le=120,
            description="Enter user age",
            example=120
        )]
) -> str:
    """
    POST запрос по маршруту '/user/{username}/{age}'
    :param username: str
    :param age: int
    :return: возвращает строку "User <user_id> is registered"
    """
    user_id = str(int(max(users.keys(), key=int)) + 1) if users else '1'
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: str,
        username: Annotated[str, Path(
            min_length=4,
            max_length=20,
            description="Enter username",
            example="Frodo"
        )],
        age: Annotated[int, Path(
            ge=18,
            le=120,
            description="Enter user age",
            example=80
        )]
) -> str:
    """
    PUT запрос по маршруту '/user/{user_id}/{username}/{age}'
    :param user_id: str
    :param username: str
    :param age: int
    :return: возвращает строку "The user <user_id> is updated"
    """
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    raise HTTPException(status_code=404, detail="User not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    """
    DELETE запрос по маршруту '/user/{user_id}'
    :param user_id: str
    :return: возвращает строку "User <user_id> is deleted"
    """
    if user_id in users:
        print(f"Attempting to delete user_id: {user_id}")
        print(f"Current users: {users}")
        del users[user_id]
        return f"User {user_id} is deleted"
    raise HTTPException(status_code=404, detail="User not found")
