from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Информация', callback_data='info')
kb.add(button)


@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer("Рады вас видеть", reply_markup=kb)


@dp.callback_query_handler(text='info')
async def infor(call):
    await call.message.answer("Информация о боте")
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
