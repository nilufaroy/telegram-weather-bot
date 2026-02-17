from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import F

from router import router

@router.message(F.text.lower() == "close menu")
@router.message(F.text.lower() == "close the menu")
async def help(message:Message):
    await message.answer(
        text = "Menu is closed!",
        reply_markup=ReplyKeyboardRemove()
    )
