from aiogram import Dispatcher, Bot
from load_env import BOT_TOKEN
from Database.users import Database

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
db = Database()
