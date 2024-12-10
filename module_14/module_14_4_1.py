"""
Эксперимент с хранением изображений на внешнем хранилище

По итогу, эксперимент удачный, изображения подгружаются ощутимо быстрее
"""

import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from crud_functions_ import *

import os
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(storage=MemoryStorage())

initiate_db()  # инициализируем БД

# data = [
#     {"name": "СуперВитамин", "description": "Витаминный комплекс для спортсменов", "price": 100,
#      "img_path": "https://i.ibb.co/X5nCmvj/product1.png"},
#     {"name": "МегаВит", "description": "Витамины на каждый день", "price": 200,
#      "img_path": "https://i.ibb.co/NTzJfYT/product2.png"},
#     {"name": "Супер Минералы", "description": "Минеральный комплекс для всех", "price": 300,
#      "img_path": "https://i.ibb.co/8YjrhJZ/product3.png"},
#     {"name": "Мега женьшень", "description": "Витаминно-минеральный комплекс, усиленный экстрактом женьшеня",
#      "price": 400, "img_path": "https://i.ibb.co/Ltm8PM2/product4.png"},
# ]
#
#
# #  Заполняем БД продуктами, если не заполнили ранее
# for product in data:
#     title = product["name"]
#     description = product["description"]
#     price = product["price"]
#     img_path = product["img_path"]
#     add_product(title, description, price, img_path)

#  Получаем данные из БД
products = get_all_products()


async def run_bot():
    await dp.start_polling(bot)


#  В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
kb_init = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
    [KeyboardButton(text="Купить")]
], resize_keyboard=True)

kb_gender = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Мужчина', callback_data='male'),
            InlineKeyboardButton(text='Женщина', callback_data='female')]
    ], resize_keyboard=True)

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='count_calories')],
    [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
])


#  Используем InlineKeyboardBuilder для динамической генерации кнопок
async def products_btn():
    keyboard = InlineKeyboardBuilder()
    for product in products:
        keyboard.add(InlineKeyboardButton(text=product['title'], callback_data="product_buying"))
    return keyboard.adjust(2).as_markup()


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()
    gender = State()


@dp.message(CommandStart())
async def start_message(message: Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb_init)


@dp.message(F.text == 'Информация')
async def information(message: Message):
    await message.answer("С помощью этого бота вы можете рассчитать свою норму калорий\n"
                         "Для расчёта используется формула Миффлина — Сан Жеора\n"
                         "Чтобы приступить, нажмите кнопку 'Рассчитать'")


@dp.message(F.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)


# Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
# Функция get_buying_list должна выводить надписи 'Название: Product<number> | Описание: описание <number> |
# Цена: <number * 100>' 4 раза. После каждой надписи выводите картинки к продуктам.
# В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".
@dp.message(F.text == "Купить")
async def get_buying_list(message: Message):
    for product in products:
        title = product["title"]
        description = product["description"]
        price = product["price"]
        img_path = product["img_path"]

        await message.answer(f"Название: {title} | Описание: {description} | Цена: {price}")
        await message.answer_photo(img_path)

    await message.answer("Выберите продукт для покупки:", reply_markup=await products_btn())


# Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
# Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"
@dp.callback_query(F.data == "product_buying")
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


#  обработка нажатия на кнопку Формулы расчёта
@dp.callback_query(F.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        "Формула Миффлина — Сан Жеора:\n"
        "Для мужчин: (10 × вес) + (6.25 × рост) - (5 × возраст) + 5\n"
        "Для женщин: (10 × вес) + (6.25 × рост) - (5 × возраст) - 161"
    )
    await call.answer()


#  обработка нажатия на кнопку Рассчитать норму калорий
@dp.callback_query(F.data == 'count_calories')
async def get_gender(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Выберите свой пол:", reply_markup=kb_gender)
    await state.set_state(UserState.gender)
    await call.answer()


@dp.callback_query(lambda call: call.data in ['male', 'female'])
async def set_gender(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(gender=call.data)

    await call.message.edit_reply_markup(reply_markup=None)

    await call.message.answer(f"Вы выбрали: {'Мужчина' if call.data == 'male' else 'Женщина'}")
    await call.message.answer("Введите свой рост в сантиметрах:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserState.height)
    await call.answer()


@dp.message(StateFilter(UserState.height))
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(height=message.text)
    await message.answer("Введите свой вес в килограммах:")
    await state.set_state(UserState.weight)


@dp.message(StateFilter(UserState.weight))
async def set_age(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await message.answer("Укажите ваш возраст:")
    await state.set_state(UserState.age)


@dp.message(StateFilter(UserState.age))
async def send_calories(message: Message, state: FSMContext):
    try:
        await state.update_data(age=message.text)
        data = await state.get_data()

        calories = 0
        age = int(data['age'])
        height = float(data['height'])
        weight = float(data['weight'])
        gender = data['gender']

        if gender == 'male':
            calories = (10 * weight) + (6.25 * height) - (5 * age) + 5
        elif gender == 'female':
            calories = (10 * weight) + (6.25 * height) - (5 * age) - 161
        else:
            await message.answer("Убедитесь что вы выбрали пол корректно.")
            return

        await message.answer(f"Ваша норма калорий: {calories:.2f}", reply_markup=kb_init)

    except ValueError:
        await message.answer("Пожалуйста, вводите только числа. Попробуйте ещё раз.", reply_markup=kb_init)
    finally:
        await state.clear()


@dp.message()
async def all_messages(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print(datetime.now())
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        print('Exit')
