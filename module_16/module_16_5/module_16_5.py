"""

"""

from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


templates = Jinja2Templates(directory="/Users/vasily/Desktop/urban_homeworks/module_16/module_16_5/templates")

users: List[User] = []

"""
Напишите новый запрос по маршруту '/':
Функция по этому запросу должна принимать аргумент request и возвращать TemplateResponse.
TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request и 
список users. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
"""


@app.get(path='/')
async def get_all_users(request: Request) -> HTMLResponse:
    """
        GET запрос по маршруту '/', который возвращает список пользователей
        через TemplateResponse с использованием шаблона 'users.html'.
        :param request: объект Request
        :return: TemplateResponse с шаблоном 'users.html' и списком пользователей
    """
    return templates.TemplateResponse("users.html", {
        "request": request,
        "users": users
    })


"""
Измените get запрос по маршруту '/user' на '/user/{user_id}':
Функция по этому запросу теперь принимает аргумент request и user_id.
Вместо возврата объекта модели User, теперь возвращается объект TemplateResponse.
TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request и 
одного из пользователей - user. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
"""


@app.get(path='/user/{user_id}')
async def get_all_users(request: Request, user_id: int) -> HTMLResponse:
    """
       GET запрос по маршруту '/user/{user_id}', который возвращает одного пользователя
       через TemplateResponse с использованием шаблона 'users.html'.
       :param request: объект Request
       :param user_id: ID пользователя
       :return: TemplateResponse с шаблоном 'users.html' и данными пользователя
    """
    try:
        return templates.TemplateResponse("users.html", {
            "request": request,
            "user": users[user_id]
        })
    except IndexError:
        raise HTTPException(status_code=404, detail="user not found")


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
    if users:
        user_id = max(user.id for user in users) + 1
    else:
        user_id = 0
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
