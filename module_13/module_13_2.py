from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message: Message):
    print('Привет! Я бот помогающий твоему здоровью.')  # Выводит в консоль по условию задачи
    await message.answer('Привет! Я бот помогающий твоему здоровью.')  # Возвращает ответ в чате (так интереснее :))


@dp.message_handler()
async def all_messages(message):
    print("Введите команду /start, чтобы начать общение.")  # Вывод в консоль по условию задачи
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
