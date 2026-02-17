import asyncio
import logging

from loader import dp, bot
from router import router

import start    # /start
import help     # /help
import menu     # /menu
import info
import close_menu 
import categories


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    await dp.start_polling(bot)

    

asyncio.run(main())

