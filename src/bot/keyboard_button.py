from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Command

def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="/yandex")
    kb.button(text="/pay")
    kb.button(text="/pict")
    kb.button(text="/google")
    kb.button(text="/date")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder='выберите одно из действий')