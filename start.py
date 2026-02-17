from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import pymysql

from router import router

from database import register_user

@router.message(CommandStart())
async def start(message: Message):
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Ma'lumot")
    keyboard.button(text="Yordam")
    keyboard.adjust(2)

    await message.answer(
        text ="Assalomu alaykum!",
        reply_markup=keyboard.as_markup(resize_keyboard=True)
    )

    try:
        register_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name
        ) 
    
    except pymysql.IntegrityError:
        pass

