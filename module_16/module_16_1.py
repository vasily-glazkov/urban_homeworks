from fastapi import FastAPI

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


# Создайте маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}".
# По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".
@app.get("/user/{user_id}")
async def user_login(user_id) -> str:
    """
    Вход по id пользователя
    """
    return f"Вы вошли как пользователь № {user_id}"


# Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user".
# По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".
@app.get("/user")
async def user_info(username: str, age: int) -> str:
    """
    Возвращает информацию о пользователе
    :param username: string
    :param age: integer
    :return: string
    """
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
