from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F

from router import router

from database import get_user_info

@router.message(F.text.lower() == "info")
@router.message(F.text.lower() == "information")
async def help(message:Message):
    # need to connect to the database
    # need to format the user info
    # to send the user

    user = get_user_info(telegram_id=message.from_user.id)
    
    # if not None
    if user is None:
        await message.answer(text="You are not in the database")
        return
    else:
        text = "======Information======"
        text += f"\n\nID: {user.get('id')}"
        text += f"\n FIO: {user.get('fullname')}"
        await message.answer(text=text)


