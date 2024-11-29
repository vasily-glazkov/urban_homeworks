"""
Задача "Меньше текста, больше кликов":
Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий выдавались
по нажатию кнопки.
Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать',
а не на 'Calories'.
Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом: 'Рассчитать' и
'Информация'.
Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи параметра resize_keyboard.
Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками.
При нажатии на кнопку с надписью 'Рассчитать' срабатывает функция set_age,
 с которой начинается работа машины состояний для age, growth и weight.
"""

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())

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


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()
    gender = State()


@dp.message_handler(text='Информация')
async def information(message: Message):
    await message.answer("С помощью этого бота вы можете рассчитать свою норму калорий\n"
                         "Для рассчёта используется формула Миффлина — Сан Жеора\n"
                         "Чтобы приступить, нажмите кнопку 'Рассчитать'", reply_markup=kb_init)


@dp.message_handler(text='Рассчитать')
async def set_gender(message: Message):
    await message.answer("Выберите свой пол (по кнопке внизу):", reply_markup=kb_gender)
    await UserState.gender.set()


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
            await message.answer(f"Ваша норма калорий: {calories:.2f}", reply_markup=kb_init)
        elif gender == 'Женщина':
            calories = (10 * weight) + (6.25 * height) - (5 * age) - 161  # формула для женщин
            await message.answer(f"Ваша норма калорий: {calories:.2f}", reply_markup=kb_init)
        else:
            await message.answer("Убедитесь что вы ввели пол верно (мужчина или женщина) и попробуйте снова")

    except ValueError:
        await message.answer("Пожалуйста, вводите только числа. Попробуйте ещё раз.", reply_markup=kb_init)
    finally:
        await state.finish()


@dp.message_handler(commands=['start'])
async def start_message(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_init)


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
