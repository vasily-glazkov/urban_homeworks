"""
Задача "Цепочка вопросов":
Необходимо сделать цепочку обработки состояний для нахождения нормы калорий для человека.
Группа состояний:
Импортируйте классы State и StatesGroup из aiogram.dispatcher.filters.state.

Создайте класс UserState наследованный от StatesGroup.
Внутри этого класса опишите 3 объекта класса State: age, growth, weight (возраст, рост, вес).
Эта группа(класс) будет использоваться в цепочке вызовов message_handler'ов. Напишите следующие функции для
обработки состояний:

Функцию set_age(message):
Оберните её в message_handler, который реагирует на текстовое сообщение 'Calories'.
Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:'.
После ожидать ввода возраста в атрибут UserState.age при помощи метода set.

Функцию set_growth(message, state):
Оберните её в message_handler, который реагирует на переданное состояние UserState.age.
Эта функция должна обновлять данные в состоянии age на message.text (написанное пользователем сообщение).
Используйте метод update_data.
Далее должна выводить в Telegram-бот сообщение 'Введите свой рост:'.
После ожидать ввода роста в атрибут UserState.growth при помощи метода set.

Функцию set_weight(message, state):
Оберните её в message_handler, который реагирует на переданное состояние UserState.growth.
Эта функция должна обновлять данные в состоянии growth на message.text (написанное пользователем сообщение).

Используйте метод update_data.
Далее должна выводить в Telegram-бот сообщение 'Введите свой вес:'.
После ожидать ввода роста в атрибут UserState.weight при помощи метода set.
Функцию send_calories(message, state):
Оберните её в message_handler, который реагирует на переданное состояние UserState.weight.
Эта функция должна обновлять данные в состоянии weight на message.text (написанное пользователем сообщение).
Используйте метод update_data.
Далее в функции запомните в переменную data все ранее введённые состояния при помощи state.get_data().
Используйте упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы калорий (для женщин или мужчин -
на ваше усмотрение). Данные для формулы берите из ранее объявленной переменной data по ключам age,
growth и weight соответственно.
Результат вычисления по формуле отправьте ответом пользователю в Telegram-бот.
Финишируйте машину состояний методом finish().
"""

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()
    gender = State()  # в задании не предусмотрено, ввел для выбора пола пользователя


@dp.message_handler(text=['Calories', 'calories'])
async def set_age(message: Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_height(message: Message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост в сантиметрах:")
    await UserState.height.set()


@dp.message_handler(state=UserState.height)
async def set_weight(message: Message, state):
    await state.update_data(height=message.text)
    await message.answer("Введите свой вес в килограммах:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_gender(message: Message, state):
    await state.update_data(weight=message.text)
    await message.answer("Укажите ваш пол (мужчина/женщина)")
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def send_calories(message: Message, state):
    try:
        await state.update_data(gender=message.text)
        data = await state.get_data()

        calories = 0
        age = int(data['age'])
        height = float(data['height'])
        weight = float(data['weight'])
        gender = data['gender']

        #  В задании этого нет, но я предусмотрел выбор пола пользователя
        if gender == 'мужчина':
            calories = (10 * weight) + (6.25 * height) - (5 * age) + 5  # формула для мужчин
            await message.answer(f"Ваша норма калорий: {calories:.2f}")
        elif gender == 'женщина':
            calories = (10 * weight) + (6.25 * height) - (5 * age) - 161  # формула для женщин
            await message.answer(f"Ваша норма калорий: {calories:.2f}")
        else:
            await message.answer("Убедитесь что вы ввели пол верно (мужчина или женщина) и попробуйте снова")

    except ValueError:
        await message.answer("Пожалуйста, вводите только числа. Попробуйте ещё раз.")
    finally:
        await state.finish()


@dp.message_handler(commands=['start'])
async def start_message(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
