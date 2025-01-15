"""
Задача "Модель пользователя":
Подготовка:
Используйте CRUD запросы из предыдущей задачи.
Создайте пустой список users = []
Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
id - номер пользователя (int)
username - имя пользователя (str)
age - возраст пользователя (int)
"""

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []

"""
Измените и дополните ранее описанные 4 CRUD запроса:
get запрос по маршруту '/users' теперь возвращает список users.
post запрос по маршруту '/user/{username}/{age}', теперь:
Добавляет в список users объект User.
id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
Все остальные параметры объекта User - переданные в функцию username и age соответственно.
В конце возвращает созданного пользователя.
put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
delete запрос по маршруту '/user/{user_id}', теперь:
Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
"""


@app.get('/users')
async def get_all_users() -> List[User]:
    """
    GET запрос по маршруту '/users', который возвращает список users
    :return: list
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
    user_id = len(users) + 1 if users else 1
    users.append(User(id=user_id, username=username, age=age))
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: int,
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
    :param user_id: int
    :param username: str
    :param age: int
    :return: возвращает строку "The user <user_id> is updated"
    """
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return f"The user {user_id} is updated"
    raise HTTPException(status_code=404, detail="User not found")


@app.delete('/user/{user_id}', response_model=dict)
async def delete_user(user_id: int) -> dict:
    """
    DELETE запрос по маршруту '/user/{user_id}'
    :param user_id: int
    :return: возвращает строку "User <user_id> is deleted"
    """
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return {"detail": "user was deleted"}
    raise HTTPException(status_code=404, detail="User not found")
