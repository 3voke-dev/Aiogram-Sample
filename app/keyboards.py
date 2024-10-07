from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Функции"),
     KeyboardButton(text="Тест")],
    [KeyboardButton(text="Ссылки на разработчика")]],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт...")

my_dev = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="GitHub", url="https://github.com/3voke-dev")],
    [InlineKeyboardButton(text="LinkedIn", url="https://linkedin.com/in/andrey-gluchshenko")],
    [InlineKeyboardButton(text="Discord", url="https://discord.com/users/489425454789427200")]
])

function = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="/start - Запуск бота", callback_data="start")],
    [InlineKeyboardButton(text="/dice - Бросок кубика", callback_data="dice")],
    [InlineKeyboardButton(text="Назад", callback_data="back_function")]
])
