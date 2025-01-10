from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello, World!!!"}

@app.get("/main")
async def main_page() -> dict:
    """
    Возвращает главную страницу
    :return: dictionary
    """
    return {"message": "This is the main page"}
