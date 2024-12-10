"""
Задача "Регистрация покупателей":
Подготовка:
Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.

Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:
initiate_db дополните созданием таблицы Users, если она ещё не создана при помощи SQL запроса.
Эта таблица должна содержать следующие поля:
id - целое число, первичный ключ
username - текст (не пустой)
email - текст (не пустой)
age - целое число (не пустой)
balance - целое число (не пустой)

add_user(username, email, age), которая принимает: имя пользователя, почту и возраст.
Данная функция должна добавлять в таблицу Users вашей БД запись с переданными данными.
Баланс у новых пользователей всегда равен 1000. Для добавления записей в таблице используйте SQL запрос.

is_included(username) принимает имя пользователя и возвращает True, если такой пользователь есть в таблице Users,
в противном случае False. Для получения записей используйте SQL запрос.

Изменения в Telegram-бот:
Кнопки главного меню дополните кнопкой "Регистрация".
Напишите новый класс состояний RegistrationState с следующими объектами класса State: username, email, age,
balance(по умолчанию 1000).

Создайте цепочку изменений состояний RegistrationState.
Фукнции цепочки состояний RegistrationState:

sing_up(message):
Оберните её в message_handler, который реагирует на текстовое сообщение 'Регистрация'.
Эта функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
После ожидать ввода имени в атрибут RegistrationState.username при помощи метода set.

set_username(message, state):
Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
Если пользователя message.text ещё нет в таблице, то должны обновляться данные в состоянии username на message.text.
Далее выводится сообщение "Введите свой email:" и принимается новое состояние RegistrationState.email.
Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует, введите другое имя" и
запрашивать новое состояние для RegistrationState.username.

set_email(message, state):
Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
Далее выводить сообщение "Введите свой возраст:":
После ожидать ввода возраста в атрибут RegistrationState.age.

set_age(message, state):
Оберните её в message_handler, который реагирует на состояние RegistrationState.age.
Эта функция должна обновляться данные в состоянии RegistrationState.age на message.text.
Далее брать все данные (username, email и age) из состояния и записывать в таблицу Users при помощи ранее написанной crud-функции add_user.
В конце завершать приём состояний при помощи метода finish().
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


kb_init = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
    [KeyboardButton(text="Купить"), KeyboardButton(text='Регистрация')]
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


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


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


@dp.message(F.text == "Регистрация")
async def sign_up(message: Message, state: FSMContext):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await state.set_state(RegistrationState.email)
    else:
        await message.answer(f"Пользователь {message.text} существует, введите другое имя")
        await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await state.set_state(RegistrationState.age)


@dp.message(RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    try:
        await state.update_data(age=message.text)
        data = await state.get_data()
        username = data.get('username')
        email = data.get('email')
        age = data.get('age')
        add_user(username, email, age)
        await message.answer("Регистрация завершена!")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
    finally:
        await state.clear()


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
