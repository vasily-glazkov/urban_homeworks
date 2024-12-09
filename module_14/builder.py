from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


data = ("СуперВитамин", "МегаВит", "Супер Минералы", "Мега витамины + Женьшень")

async def products_btn():
    keyboard = InlineKeyboardBuilder()
    for product in data:
        keyboard.add(InlineKeyboardButton(text=product, callback_data="product_buying"))
    return keyboard.adjust(2).as_markup()
