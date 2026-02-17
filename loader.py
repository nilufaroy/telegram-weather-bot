from aiogram import  Bot, Dispatcher

from environs import Env



env = Env()
env.read_env()


bot = Bot(token=env.str("BOT_TOKEN"))
dp = Dispatcher()