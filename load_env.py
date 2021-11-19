import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
db_user = os.getenv("DB.USER")
db_password = os.getenv("DB.PASSWORD")
db_host = os.getenv("DB.HOST")
db_name = os.getenv("DB.NAME")
