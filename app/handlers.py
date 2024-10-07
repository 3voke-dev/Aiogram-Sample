from aiogram import Bot, types, F, Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

import app.keyboards as kb

router = Router()

# @router.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer("Привет, друг! Мои доступные функции:",
#                          reply_markup=kb.main)

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет, друг!",
                         reply_markup=kb.main)

@router.message(F.text=="Привет")
async def cmd_hello(message: Message):
    await message.answer(
        f"Привет, хабиби {message.from_user.full_name}.",
        parse_mode=ParseMode.HTML)

@router.message(F.text=="привет")
async def cmd_hello1(message: Message):
    await message.answer(
        f"Привет, хабиби {message.from_user.full_name}.",
        parse_mode=ParseMode.HTML)

@router.message(F.text=="Функции")
async def cmd_function(message: Message):
    await message.answer(f"/start - Запуск бота\n/dice - Бросок кубика")

@router.message(F.text=="Тест")
async def cmd_test(message: Message):
    await message.answer("Тестовая кнопка")

@router.message(F.text=="Ссылки на разработчика")
async def cmd_my_dev(message: Message):
    await message.answer("↘️", reply_markup=kb.my_dev)

@router.message(F.new_chat_members)
async def somebody_added(message: Message):
    for user in message.new_chat_members:
        await message.answer(f"Привет, хабиби. \nМеня зовут Евлампий! \nЯ чат бот, меня разрабатывает Андрюша.")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(f"/start - Запуск бота\n/help - Доступные команды\n/dice - Бросок кубика")

@router.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

@router.message(Command("hello"))
async def cmd_hello(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}",
        parse_mode=ParseMode.HTML
    )

# @router.callback_query(F.data == "function")
# async def function(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.edit_text("🟢 Функции:", reply_markup=kb.function)
#
# @router.callback_query(F.data == "dice")
# async def function(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.answer("/dice")
#
# @router.callback_query(F.data == "test1")
# async def function(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.answer("/test1")
#
# @router.callback_query(F.data == "back_function")
# async def function(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.edit_text("🟢 Меню:", reply_markup=kb.main)
#
# @router.callback_query(F.data == "my_dev")
# async def function(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.edit_text("↘️", reply_markup=kb.my_dev)
#
# @router.callback_query(F.data == "back_my_dev")
# async def function(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.edit_text("🟢 Меню:", reply_markup=kb.main)
#
# @router.callback_query(F.data == "test2")
# async def function(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.answer("/test2")

# Код для того что бы бот отправлял сообщение в группу
# @router.message(Command("dice"))
# async def cmd_dice(message: types.Message, bot: Bot):
#     await bot.send_dice(-4526941371, )
