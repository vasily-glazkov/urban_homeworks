"""
Задача "Ещё больше выбора":
Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
С текстом 'Рассчитать норму калорий' и callback_data='calories'
С текстом 'Формулы расчёта' и callback_data='formulas'
Создайте новую функцию main_menu(message), которая:
Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
Создайте новую функцию get_formulas(call), которая:
Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
Будет присылать сообщение с формулой Миффлина-Сан Жеора.
Измените функцию set_age и декоратор для неё:
Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
По итогу получится следующий алгоритм:
Вводится команда /start
На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.
"""

import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardRemove
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
import os
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(storage=MemoryStorage())


async def run_bot():
    await dp.start_polling(bot)


kb_init = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')]
], resize_keyboard=True)

kb_gender = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Мужчина', callback_data='male'),
            InlineKeyboardButton(text='Женщина', callback_data='female')]
    ], resize_keyboard=True)

#  Инициализация инлайновых кнопок по заданию
inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='count_calories')],
    [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
])


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()
    gender = State()


@dp.message(CommandStart())
async def start_message(message: Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb_init)


@dp.message(lambda message: message.text == 'Информация')
async def information(message: Message):
    await message.answer("С помощью этого бота вы можете рассчитать свою норму калорий\n"
                         "Для расчёта используется формула Миффлина — Сан Жеора\n"
                         "Чтобы приступить, нажмите кнопку 'Рассчитать'")


@dp.message(lambda message: message.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)


#  обработка нажатия на кнопку Формулы расчёта
@dp.callback_query(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        "Формула Миффлина — Сан Жеора:\n"
        "Для мужчин: (10 × вес) + (6.25 × рост) - (5 × возраст) + 5\n"
        "Для женщин: (10 × вес) + (6.25 × рост) - (5 × возраст) - 161"
    )
    await call.answer()


#  обработка нажатия на кнопку Рассчитать норму калорий
@dp.callback_query(lambda call: call.data == 'count_calories')
async def get_gender(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Выберите свой пол:", reply_markup=kb_gender)
    await state.set_state(UserState.gender)
    await call.answer()


#  Этап выбора пола и дальнейший каскад действий
@dp.callback_query(lambda call: call.data in ['male', 'female'])
async def set_gender(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(gender=call.data)

    #  Убираем инлайновую клавиатуру выбора пола, путем редактирования сообщения
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
