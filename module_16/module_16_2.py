from fastapi import FastAPI, Path
from typing import Annotated

# создаем приложение (объект) FastAPI
app = FastAPI()


# Создайте маршрут к главной странице - "/". По нему должно выводиться сообщение "Главная страница".
@app.get("/")
async def main_page() -> str:
    """
    Отображает главную страницу
    """
    return "Главная страница"


# Создайте маршрут к странице администратора - "/user/admin".
# По нему должно выводиться сообщение "Вы вошли как администратор".
@app.get("/user/admin")
async def admin_page() -> str:
    """
    Страница администратора
    """
    return "Вы вошли как администратор"


# Допишите валидацию для маршрутов из предыдущей задачи при помощи классов Path и Annotated:
# '/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id,
# для которого необходимо написать следующую валидацию:
# Должно быть целым числом
# Ограничено по значению: больше или равно 1 и меньше либо равно 100.
# Описание - 'Enter User ID'
# Пример - '1' (можете подставить свой пример не противоречащий валидации)
@app.get("/user/{user_id}")
async def user_login(user_id: Annotated[int, Path(
    ge=1, le=100, description="Enter User ID", example="7"
)]) -> str:
    """
    Вход по id пользователя
    """
    return f"Вы вошли как пользователь № {user_id}"


# '/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту,
# принимает аргументы username и age, для которых необходимо написать следующую валидацию:
# username - строка, age - целое число.
# username ограничение по длине: больше или равно 5 и меньше либо равно 20.
# age ограничение по значению: больше или равно 18 и меньше либо равно 120.
# Описания для username и age - 'Enter username' и 'Enter age' соответственно.
# Примеры для username и age - 'UrbanUser' и '24' соответственно.
# (можете подставить свои примеры не противоречащие валидации).
@app.get("/user/{username}/{age}")
async def user_info(
        username: Annotated[str, Path(
            min_length=5,
            max_length=20,
            description="Enter username",
            example="frodo"
        )],
        age: Annotated[int, Path(
            ge=18,
            le=120,
            description="Enter age",
            example="110"
        )]) -> str:
    """
    Возвращает информацию о пользователе
    :param username: string
    :param age: integer
    :return: string
    """
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
