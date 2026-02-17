from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F

from router import router

@router.message(Command(commands=["help"]))
@router.message(F.text.lower() == "Yordam")
async def help(message:Message):
    await message.answer(
        text = "Do you need help?"
    )