from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())

# Обычная клавиатура
kb_init = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Рассчитать'),
        KeyboardButton(text='Информация')
    ]
], resize_keyboard=True)

kb_gender = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Мужчина'),
        KeyboardButton(text='Женщина')
    ]
], resize_keyboard=True)

inline_kb = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(button_calories)
inline_kb.add(button_formulas)


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()
    gender = State()


@dp.message_handler(commands=['start'])
async def start_message(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_init)


@dp.message_handler(text='Информация')
async def information(message: Message):
    await message.answer("С помощью этого бота вы можете рассчитать свою норму калорий\n"
                         "Для расчёта используется формула Миффлина — Сан Жеора\n"
                         "Чтобы приступить, нажмите кнопку 'Рассчитать'", reply_markup=kb_init)


@dp.message_handler(text='Рассчитать')
async def main_menu(message: Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        "Формула Миффлина — Сан Жеора:\n"
        "Для мужчин: (10 × вес) + (6.25 × рост) - (5 × возраст) + 5\n"
        "Для женщин: (10 × вес) + (6.25 × рост) - (5 × возраст) - 161"
    )
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_gender(call: types.CallbackQuery):
    await call.message.answer("Выберите свой пол (по кнопке внизу):", reply_markup=kb_gender)
    await UserState.gender.set()
    await call.answer()


@dp.message_handler(state=UserState.gender)
async def set_height(message: Message, state):
    await state.update_data(gender=message.text)
    await message.answer("Введите свой рост в сантиметрах:", reply_markup=ReplyKeyboardRemove())
    await UserState.height.set()


@dp.message_handler(state=UserState.height)
async def set_weight(message: Message, state):
    await state.update_data(height=message.text)
    await message.answer("Введите свой вес в килограммах:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_age(message: Message, state):
    await state.update_data(weight=message.text)
    await message.answer("Укажите ваш возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def send_calories(message: Message, state):
    try:
        await state.update_data(age=message.text)
        data = await state.get_data()

        calories = 0
        age = int(data['age'])
        height = float(data['height'])
        weight = float(data['weight'])
        gender = data['gender']

        if gender == 'Мужчина':
            calories = (10 * weight) + (6.25 * height) - (5 * age) + 5  # формула для мужчин
        elif gender == 'Женщина':
            calories = (10 * weight) + (6.25 * height) - (5 * age) - 161  # формула для женщин
        else:
            await message.answer("Убедитесь что вы выбрали пол корректно.")
            return

        await message.answer(f"Ваша норма калорий: {calories:.2f}", reply_markup=kb_init)

    except ValueError:
        await message.answer("Пожалуйста, вводите только числа. Попробуйте ещё раз.", reply_markup=kb_init)
    finally:
        await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
