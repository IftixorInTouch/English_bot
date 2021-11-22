from aiogram import Dispatcher, Bot
from load_env import BOT_TOKEN
from Database.users import Database
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()
