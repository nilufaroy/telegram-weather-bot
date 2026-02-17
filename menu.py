from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
from aiogram.filters import Command

from router import router


@router.message(Command(commands=["menu"]))
async def show_menu(message: Message):
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="🌯 Lavash", callback_data="category:1")
    keyboard.button(text="🍔 Burger", callback_data="category:2")
    keyboard.button(text="🧋 Drinks", callback_data="category:3")
    keyboard.button(text="🍧 Desserts", callback_data="category:4")
    keyboard.adjust(2)

    await message.answer_photo(
        photo="https://images.pexels.com/photos/19138491/pexels-photo-19138491.jpeg?_gl=1*1opl8lc*_ga*NTE4NDg1NTE3LjE3NzEzMzE2OTE.*_ga_8JE65Q40S6*czE3NzEzMzE2OTAkbzEkZzEkdDE3NzEzMzE3MTkkajMxJGwwJGgw",
        caption="Choose one of the below:",
        reply_markup=keyboard.as_markup()
    )


@router.callback_query(F.data == "back_to_categories")
async def back_to_categories(call: CallbackQuery):
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="🌯 Lavash", callback_data="category:1")
    keyboard.button(text="🍔 Burger", callback_data="category:2")
    keyboard.button(text="🧋 Drinks", callback_data="category:3")
    keyboard.button(text="🍧 Desserts", callback_data="category:4")
    keyboard.adjust(2)

    await call.message.delete()
    await call.message.answer_photo(
        photo="https://images.pexels.com/photos/19138491/pexels-photo-19138491.jpeg?_gl=1*1opl8lc*_ga*NTE4NDg1NTE3LjE3NzEzMzE2OTE.*_ga_8JE65Q40S6*czE3NzEzMzE2OTAkbzEkZzEkdDE3NzEzMzE3MTkkajMxJGwwJGgw",
        caption="Choose one of the below: ",
        reply_markup=keyboard.as_markup()
    )

    await call.answer()