from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F

from router import router

@router.callback_query(F.data.startswith("category:"))
async def start(callback: CallbackQuery):
    
    data = callback.data
    category_type = data.split(":")[1]
    
    keyboard = InlineKeyboardBuilder()
    caption = ""
    photo = ""
    # Lavash
    if category_type == "1":
        caption = "Choose one of the lavash types:"
        photo = "https://media.istockphoto.com/id/1448582745/photo/chicken-doner-kebab-and-fresh-vegetables-in-roll-of-pita-bread-lavash-durum-chicken-doner.jpg?s=1024x1024&w=is&k=20&c=wh7mpBKD1Io4nggr2xh0jrvn7V7y2p5kPksTa23Lgp8="

        keyboard.button(text="Mini Lavash", callback_data="...")
        keyboard.button(text="Cheese Lavash", callback_data="...")
        keyboard.button(text="Chicken Lavash", callback_data="...")
        keyboard.button(text="Pineapple Lavash", callback_data="...")
        keyboard.button(text="Mini Turkey Lavash", callback_data="...")
        keyboard.button(text="Vegeterian Lavash", callback_data="back_to_categories")
        keyboard.adjust(2)

    # Burger
    elif category_type == "2":
        caption = "Choose one of the burger types:"
        photo = "https://plus.unsplash.com/premium_photo-1683619761468-b06992704398?q=80&w=965&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

        keyboard.button(text="Mini Burger", callback_data="category:burger_mini")
        keyboard.button(text="Standard Burger", callback_data="category:burger_standart")
        keyboard.button(text="Extra Burger", callback_data="category:burger_extra")
        keyboard.button(text="Cheese Burger", callback_data="category:burger_chiz")

        
    # Drinks
    elif category_type == "3":
        caption = "Choose one of the drink types:"
        photo = "https://images.unsplash.com/photo-1551024709-8f23befc6f87?q=80&w=2157&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

        keyboard.button(text="Hydrolife 0.5L", callback_data="category:hydrolife_0.5")
        keyboard.button(text="Hydrolife 1L", callback_data="category:hydrolife_1")
        keyboard.button(text="Mojito 0.25L", callback_data="category:moxito_0.25")
        keyboard.button(text="Mojito 0.5L", callback_data="category:moxito_0.5")


    # Desserts
    elif category_type == "4":
        caption = "Choose one of the desserts:"
        photo = "https://images.unsplash.com/photo-1702742322469-36315505728f?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        
        keyboard.button(text="Chocolate Donut", callback_data="category:shokoladli_donut")
        keyboard.button(text="Vanilla Donut", callback_data="category:vanil_donut")
        keyboard.button(text="Creamy Baklava", callback_data="category:qaymoqli_paxlava")
        keyboard.button(text="Chocolate Napoleon", callback_data="category:shokoladli_napaleon")


    # Back button
    keyboard.adjust(2)
    keyboard.row(
        InlineKeyboardButton(text="👈🏻Back", callback_data="back_to_categories")
    )

    await callback.message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=caption,
        reply_markup=keyboard.as_markup()
    )
    
    await callback.answer()


