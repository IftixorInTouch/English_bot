import Handlers
from aiogram import executor
from aiogram.types import BotCommand
from data import dp, db


async def my_commands(dp):
    await db.create_pool()
    await db.create_table_users()
    await dp.bot.set_my_commands(
        [
            BotCommand(command="start", description="start")
        ]
    )


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=my_commands)
